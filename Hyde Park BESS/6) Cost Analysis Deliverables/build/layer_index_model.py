"""Per-layer dollar-year adjustment (deck narrative 1: scaling published costs to 2026).
cost_2026 = cost_y x sum_i w_i x I_i(2026)/I_i(y)   with one index per cost layer instead of one battery index + one construction index.
Compositions: 'hp' from the Rev 3 loaded layers; 'developer' from the NREL/PNNL component structure of a merchant 4-h project.
Series: indices_layers_api.json (FRED/BLS API, if fetched) overrides indices_layers.json (search-excerpt values); battery series from indices.json.
"""
import json, os, numpy as np
B="/tmp/claude-0/-home-user-BESS/078f934e-4ca0-5169-be3f-cb66ff0e2514/scratchpad/build"
D=json.load(open(f"{B}/data.json")); R=json.load(open(f"{B}/stats_results.json")); IXJ=json.load(open(f"{B}/indices.json")); LJ=json.load(open(f"{B}/indices_layers.json"))
if os.path.exists(f"{B}/indices_layers_api.json"):
    for k,v in json.load(open(f"{B}/indices_layers_api.json")).items():
        if len(v.get("points",{}))>=8: LJ["series"][k]={**LJ["series"].get(k,{}),**v,"source":v["source"]+" (overrides excerpt values)"}
HP={"contract":605.3,"installed":832.9,"station_direct":1483.3,"approval":2862.4}
def interp(pts):
    xs=sorted(int(k) for k in pts); ys=[float(pts[str(x)]) for x in xs]
    return lambda y: float(np.interp(y,xs,ys))
S={k:interp(v["points"]) for k,v in LJ["series"].items() if len(v.get("points",{}))>=2}
S["hw"]=interp(IXJ["construction_index"]["points"])
for k,v in IXJ["indices"].items():
    if len(v["points"])>=2: S["bat_"+k]=interp(v["points"])
for k in ("transformer","switchgear","engineering","labor","civil","hw_dist","interconnect"):
    if k not in S: S[k]=S["hw"]; LJ["series"].setdefault(k,{})["fallback"]="Handy-Whitman (series not retrieved)"
ratio=lambda k,y: S[k](2026)/S[k](min(max(y,2014),2026))
# --- layer -> index mapping (Hyde Park composition, loaded layers A-I plus the 496 interconnection)
LL=D["layers_loaded"]; tot=sum(LL.values())
MAP={ "A":("bat_installed","Battery contract: installed-system index (sensitivity: pack, turnkey)"),
      "B":("labor","Install labor: ECI construction"),
      "C":("transformer","GSUs, aux power: transformer PPI"),
      "D":("switchgear","Switching station: switchgear PPI (equipment) and labor"),
      "E":("civil","Site and civil: ENR CCI"),
      "F":("labor","Feeder protection: labor (14,200 of its hours are install and test)"),
      "G":("labor","Testing and commissioning: ECI construction"),
      "H":("engineering","Owner soft costs: PPI engineering services"),
      "I":("hw","Taxes and insurance: Handy-Whitman")}
w_hp={k[0]:v/tot for k,v in LL.items()}
# developer composition (NREL/PNNL structure, see indices_layers.json 'composition_developer'); shares sum to 1
w_dev=LJ["composition_developer"]["shares"]; dev_map=LJ["composition_developer"]["map"]
def comp_factor(y,weights,mapping,bat="bat_installed"):
    f=0.0
    for layer,w in weights.items():
        key=mapping[layer][0] if isinstance(mapping[layer],(list,tuple)) else mapping[layer]
        if key.startswith("bat_") and bat: key=bat
        f+=w*ratio(key,y)
    return f
HW=S["hw"]; two=lambda y,s=0.4: s*ratio("bat_installed",y)+(1-s)*HW(2026)/HW(min(y,2026))
out={"weights_hp":w_hp,"weights_dev":w_dev,"map_hp":{k:v[0] for k,v in MAP.items()},"map_dev":dev_map,"series_ratio_2018":{k:ratio(k,2018) for k in S},"series_meta":{k:{kk:vv for kk,vv in v.items() if kk!="points"} for k,v in LJ["series"].items()},
     "factors":{str(y):{"hp_composite":comp_factor(y,w_hp,MAP),"dev_composite":comp_factor(y,w_dev,dev_map),"two_component":two(y),"naive_battery":ratio("bat_installed",y),"hw_only":HW(2026)/HW(y)} for y in range(2015,2027)},
     "classes":{}}
for cname in ("reference_class","reference_class_utility"):
    P=R[cname]["projects"]; blk={"n":len(P),"methods":{}}
    for mname,fn in (("nominal",lambda y:1.0),("naive_battery",lambda y:ratio("bat_installed",y)),("two_component",two),("layer_developer",lambda y:comp_factor(y,w_dev,dev_map)),("layer_hp",lambda y:comp_factor(y,w_hp,MAP)),
                     ("layer_developer_pack",lambda y:comp_factor(y,w_dev,dev_map,"bat_pack")),("layer_developer_turnkey",lambda y:comp_factor(y,w_dev,dev_map,"bat_turnkey"))):
        adj=np.array([p["kwh"]*fn(int(p["cod_year"])) for p in P])
        blk["methods"][mname]={"median":float(np.median(adj)),"q25":float(np.percentile(adj,25)),"q75":float(np.percentile(adj,75)),"hp_pct":{k:float((adj<v).mean()) for k,v in HP.items()}}
    out["classes"][cname]=blk
# indexed series (2018 = 1.0) for the chart
out["indexed"]={}
for k,v in LJ["series"].items():
    if len(v.get("points",{}))>=2:
        base=S[k](2018); out["indexed"][k]={"label":v.get("label",k),"points":[[int(y),float(val)/base] for y,val in sorted(((int(a),b) for a,b in v["points"].items()))]}
json.dump(out,open(f"{B}/layer_index_results.json","w"),indent=1)
print("weights HP:",{k:round(v,3) for k,v in w_hp.items()})
print("2018->2026 ratios:",{k:round(v,2) for k,v in out["series_ratio_2018"].items()})
for y in (2018,2021,2023,2025): print(y,{k:round(v,3) for k,v in out["factors"][str(y)].items()})
for c,blk in out["classes"].items():
    print(c,blk["n"]); [print(f"   {m:24s} median ${v['median']:,.0f}  HP inst {v['hp_pct']['installed']:.0%} stn {v['hp_pct']['station_direct']:.0%}") for m,v in blk["methods"].items()]
