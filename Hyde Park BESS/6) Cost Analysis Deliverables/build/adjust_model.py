"""Dollar-year adjustment of the public comparables to 2026 (deck slides 12-14, memo 3.1-3.3).
cost_2026 = cost_nominal x [ s x I(2026)/I(y) + (1-s) x (1+g)^(2026-y) ]
  s = battery share of the comparable's cost, I = battery index (indices.json), g = non-battery construction escalation.
"""
import json, numpy as np
B="/tmp/claude-0/-home-user-BESS/078f934e-4ca0-5169-be3f-cb66ff0e2514/scratchpad/build"
R=json.load(open(f"{B}/stats_results.json")); NY=json.load(open(f"{B}/ny_cohort.json")); IXJ=json.load(open(f"{B}/indices.json"))
HP={"contract":605.3,"installed":832.9,"station_direct":1483.3,"approval":2862.4}
SHARE=0.40; SHARES=(0.3,0.4,0.5); G=IXJ["construction_g"]
def interp(pts):
    xs=sorted(int(k) for k in pts); ys=[pts[str(x)] for x in xs]
    return lambda y: float(np.interp(y,xs,ys))   # np.interp holds flat outside the span
IDX={k:{**v,"f":interp(v["points"])} for k,v in IXJ["indices"].items() if len(v["points"])>=2}
IDX["construction"]={"label":"Construction index only (Handy-Whitman, no battery deflation)","source":IXJ["construction_index"]["source"],"conf":IXJ["construction_index"]["conf"],"f":None}
HW=interp(IXJ["construction_index"]["points"])
constr=lambda y: HW(2026)/HW(min(y,2026))          # Handy-Whitman North Atlantic production plant, primary non-battery escalator
constr_flat=lambda y:(1+G)**(2026-min(y,2026))   # 3.5%/yr proxy, sensitivity
def factor(key,y,s=SHARE):
    f=IDX[key]["f"]; y=min(y,2026)
    return constr(y) if f is None else s*f(2026)/f(y)+(1-s)*constr(y)
def summarize(P,key,s):
    adj=np.array([p["kwh"]*factor(key,int(p["cod_year"]),s) for p in P])
    return {"median":float(np.median(adj)),"q25":float(np.percentile(adj,25)),"q75":float(np.percentile(adj,75)),"min":float(adj.min()),"max":float(adj.max()),
            "hp_pct":{k:float((adj<v).mean()) for k,v in HP.items()}}
def factor_flat(key,y,s=SHARE):
    f=IDX[key]["f"]; y=min(y,2026)
    return constr_flat(y) if f is None else s*f(2026)/f(y)+(1-s)*constr_flat(y)
out={"share":SHARE,"g":G,"hp":HP,"classes":{},"hw_ratio_2018":HW(2026)/HW(2018)}
for cname in ("reference_class","reference_class_utility"):
    P=R[cname]["projects"]; blk={"n":len(P),"nominal":{"median":float(np.median([p["kwh"] for p in P])),"q25":float(np.percentile([p["kwh"] for p in P],25)),"q75":float(np.percentile([p["kwh"] for p in P],75)),"hp_pct":{k:float((np.array([p["kwh"] for p in P])<v).mean()) for k,v in HP.items()}},"indices":{},"projects":[]}
    for key,ix in IDX.items():
        f=ix["f"]
        naive=np.array([p["kwh"]*(f(2026)/f(min(int(p["cod_year"]),2026)) if f else constr(int(p["cod_year"]))) for p in P])
        blk["indices"][key]={"label":ix["label"],"source":ix["source"],"conf":ix["conf"],"ratio_2018":(f(2026)/f(2018) if f else constr(2018)),"naive_median":float(np.median(naive)),
                             "by_share":{str(s):summarize(P,key,s) for s in SHARES}}
    adjf=np.array([p["kwh"]*factor_flat("installed",int(p["cod_year"])) for p in P])
    blk["indices"]["installed_flat35"]={"label":"Installed index with 3.5%/yr flat non-battery escalation (proxy)","source":"sensitivity","conf":"Assumption","ratio_2018":IDX["installed"]["f"](2026)/IDX["installed"]["f"](2018),"naive_median":float(np.median(adjf)),"by_share":{"0.4":{"median":float(np.median(adjf)),"q25":float(np.percentile(adjf,25)),"q75":float(np.percentile(adjf,75)),"min":float(adjf.min()),"max":float(adjf.max()),"hp_pct":{k:float((adjf<v).mean()) for k,v in HP.items()}}}}
    for p in P:
        y=int(p["cod_year"]); blk["projects"].append({"project":p["project"],"state":p["state"],"utility":p.get("utility"),"mw":p["mw"],"mwh":p["mwh"],"cod_year":y,"nominal":p["kwh"],
            **{f"adj_{k}":p["kwh"]*factor(k,y) for k in IDX},"factor_installed":factor("installed",y)})
    out["classes"][cname]=blk
# convenience aliases used by the deck and workbook (primary class, primary index, 40% share)
C=out["classes"]["reference_class"]; out["nominal"]=C["nominal"]; out["projects"]=C["projects"]
out["indices"]={k:{"label":v["label"],"source":v["source"],"conf":v["conf"],"ratio_2018":v["ratio_2018"],"naive_median":v["naive_median"],**v["by_share"]["0.4"]} for k,v in C["indices"].items()}
for s in (0.3,0.5): out["indices"][f"installed_s{int(s*100)}"]={"label":f"Installed index, battery share {s:.0%}",**C["indices"]["installed"]["by_share"][str(s)]}
out["ny"]=[]
for p in NY["projects"]:
    y=int(p["cod_year"]); k=p["cost_usd"]/p["mwh"]/1000
    out["ny"].append({**{a:p[a] for a in ("project","owner","mw","mwh","cod_year","cost_basis","confidence")},"nominal":k,"kw":p["cost_usd"]/p["mw"]/1000,"adj_installed":k*factor("installed",y),"hours":p["mwh"]/p["mw"]})
for ix in NY["indices"]:
    out["ny"].append({"project":ix["name"],"owner":"NYSERDA program average","mw":None,"mwh":None,"cod_year":ix["year"],"cost_basis":ix["source"],"confidence":ix["confidence"],"nominal":ix["kwh"],"kw":None,"adj_installed":ix["kwh"]*factor("installed",ix["year"]),"hours":None})
json.dump(out,open(f"{B}/adjust_results.json","w"),indent=1)
for cname,blk in out["classes"].items():
    print(f"== {cname}: n={blk['n']} nominal median ${blk['nominal']['median']:,.0f}  HP stn pct {blk['nominal']['hp_pct']['station_direct']:.0%}")
    for key,v in blk["indices"].items():
        row=" | ".join(f"s{int(float(s)*100)}: ${b['median']:,.0f} ({b['hp_pct']['station_direct']:.0%})" for s,b in v["by_share"].items())
        print(f"   {key:13s} 2018->26 {v['ratio_2018']:.2f}  naive ${v['naive_median']:,.0f}  {row}")
