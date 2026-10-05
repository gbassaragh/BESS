"""Dollar-year adjustment of the public comparables to 2026 (deck slides 12 and 14-16, memo 3.1-3.3).
Revised 5 Oct 2026 after the review challenge on slide 12: the model now holds PHYSICAL QUANTITIES fixed, not dollar shares.
  C(y)      = s0 x I(y)/I(y0) + (1 - s0) x HW(y)/HW(y0)        composite price index of a project with anchor-year shares s0 (battery) at y0 = 2024
  factor(y) = C(2026) / C(y)                                    what a project built in year y would cost at 2026 prices, same MW/MWh and scope
  s(y)      = s0 x I(y)/I(y0) / C(y)                            the battery share that project had in its own year (rises as you go back)
The earlier version applied s0 to every year ("fixed share"), which understated the battery's weight in 2015-2019 projects and made every
old project dearer today. It is kept as a method for comparison. Anchor shares: utility-owned 0.40, developer-owned 0.55 (NREL/PNNL structure);
sensitivities at -0.10 and +0.10. I = battery index (indices.json), HW = Handy-Whitman North Atlantic.
"""
import json, numpy as np
B="/tmp/claude-0/-home-user-BESS/078f934e-4ca0-5169-be3f-cb66ff0e2514/scratchpad/build"
R=json.load(open(f"{B}/stats_results.json")); NY=json.load(open(f"{B}/ny_cohort.json")); IXJ=json.load(open(f"{B}/indices.json"))
HP={"contract":605.3,"installed":832.9,"station_direct":1483.3,"approval":2862.4}
Y0=2024; S_UTIL=0.40; S_DEV=0.55; SHARES=(0.3,0.4,0.5); G=IXJ["construction_g"]
def interp(pts):
    xs=sorted(int(k) for k in pts); ys=[pts[str(x)] for x in xs]
    return lambda y: float(np.interp(y,xs,ys))   # flat outside the span
IDX={k:{**v,"f":interp(v["points"])} for k,v in IXJ["indices"].items() if len(v["points"])>=2}
IDX["construction"]={"label":"Construction index only (Handy-Whitman, no battery deflation)","source":IXJ["construction_index"]["source"],"conf":IXJ["construction_index"]["conf"],"f":None}
HW=interp(IXJ["construction_index"]["points"]); hw=lambda y: HW(min(y,2026))/HW(Y0)
def comp(key,y,s0):
    f=IDX[key]["f"]; y=min(y,2026)
    return hw(y) if f is None else s0*f(y)/f(Y0)+(1-s0)*hw(y)
def factor(key,y,s0):            # fixed quantities (Laspeyres with 2024 weights)
    return comp(key,2026,s0)/comp(key,y,s0)
def share_at(key,y,s0):          # implied battery share in year y
    f=IDX[key]["f"]; y=min(y,2026)
    return None if f is None else s0*f(y)/f(Y0)/comp(key,y,s0)
def factor_fixed_share(key,y,s0):  # the earlier model, kept for the comparison
    f=IDX[key]["f"]; y=min(y,2026); c=HW(2026)/HW(y)
    return c if f is None else s0*f(2026)/f(y)+(1-s0)*c
def s_of(p,base=None):           # anchor share by owner type
    if base is not None: return base
    return S_UTIL if p.get("utility")==1 else S_DEV
def summarize(P,key,fn,base=None):
    adj=np.array([p["kwh"]*fn(key,int(p["cod_year"]),s_of(p,base)) for p in P])
    return {"median":float(np.median(adj)),"q25":float(np.percentile(adj,25)),"q75":float(np.percentile(adj,75)),"min":float(adj.min()),"max":float(adj.max()),
            "hp_pct":{k:float((adj<v).mean()) for k,v in HP.items()}}
out={"anchor_year":Y0,"share_utility":S_UTIL,"share_developer":S_DEV,"g":G,"hp":HP,"classes":{},"hw_ratio_2018":HW(2026)/HW(2018)}
for cname in ("reference_class","reference_class_utility"):
    P=R[cname]["projects"]; kw=np.array([p["kwh"] for p in P])
    blk={"n":len(P),"nominal":{"median":float(np.median(kw)),"q25":float(np.percentile(kw,25)),"q75":float(np.percentile(kw,75)),"hp_pct":{k:float((kw<v).mean()) for k,v in HP.items()}},"indices":{},"projects":[]}
    for key,ix in IDX.items():
        f=ix["f"]
        naive=np.array([p["kwh"]*(f(2026)/f(min(int(p["cod_year"]),2026)) if f else HW(2026)/HW(int(p["cod_year"]))) for p in P])
        blk["indices"][key]={"label":ix["label"],"source":ix["source"],"conf":ix["conf"],"ratio_2018":(f(2026)/f(2018) if f else HW(2026)/HW(2018)),
            "naive_median":float(np.median(naive)),"naive_hp_pct":{k:float((naive<v).mean()) for k,v in HP.items()},
            "by_owner":summarize(P,key,factor),                                   # primary: owner-specific anchor share, fixed quantities
            "by_owner_minus10":summarize(P,key,lambda k,y,s: factor(k,y,s-0.10)),"by_owner_plus10":summarize(P,key,lambda k,y,s: factor(k,y,s+0.10)),
            "by_share":{str(s): summarize(P,key,factor,base=s) for s in SHARES},  # uniform anchor share sensitivity
            "fixed_share_40":summarize(P,key,factor_fixed_share,base=0.40),       # the earlier model
            "factor_2018":factor(key,2018,S_UTIL),"factor_2016":factor(key,2016,S_UTIL),"share_2018":share_at(key,2018,S_UTIL),"share_2016":share_at(key,2016,S_UTIL)}
    for p in P:
        y=int(p["cod_year"]); s0=s_of(p)
        blk["projects"].append({"project":p["project"],"state":p["state"],"utility":p.get("utility"),"mw":p["mw"],"mwh":p["mwh"],"cod_year":y,"nominal":p["kwh"],"anchor_share":s0,
            **{f"adj_{k}":p["kwh"]*factor(k,y,s0) for k in IDX},"factor_installed":factor("installed",y,s0),"share_installed":share_at("installed",y,s0),"fixed_share_installed":p["kwh"]*factor_fixed_share("installed",y,0.40)})
    out["classes"][cname]=blk
C=out["classes"]["reference_class"]; out["nominal"]=C["nominal"]; out["projects"]=C["projects"]
out["indices"]={k:{"label":v["label"],"source":v["source"],"conf":v["conf"],"ratio_2018":v["ratio_2018"],"naive_median":v["naive_median"],"factor_2018":v["factor_2018"],"factor_2016":v["factor_2016"],"share_2018":v["share_2018"],"share_2016":v["share_2016"],**v["by_owner"]} for k,v in C["indices"].items()}
for s in (0.3,0.5): out["indices"][f"installed_s{int(s*100)}"]={"label":f"Installed index, uniform anchor share {s:.0%}",**C["indices"]["installed"]["by_share"][str(s)]}
out["indices"]["installed_fixed_share"]={"label":"Installed index, earlier fixed-share model (40%)",**C["indices"]["installed"]["fixed_share_40"]}
out["indices"]["installed_flat35"]={"label":"(retired) flat 3.5%/yr non-battery escalation",**C["indices"]["installed"]["by_owner"]}
out["share_by_year"]={str(y):{k:share_at(k,y,S_UTIL) for k in ("installed","pack","turnkey","nrel")} for y in range(2015,2027)}
out["factor_by_year"]={str(y):{k:factor(k,y,S_UTIL) for k in ("installed","pack","turnkey","nrel","lcos","construction")} for y in range(2015,2027)}
out["factor_by_year_dev"]={str(y):{k:factor(k,y,S_DEV) for k in ("installed","pack","turnkey","nrel")} for y in range(2015,2027)}
out["factor_by_year_fixed"]={str(y):{k:factor_fixed_share(k,y,0.40) for k in ("installed","pack","turnkey","nrel")} for y in range(2015,2027)}
out["ny"]=[]
for p in NY["projects"]:
    y=int(p["cod_year"]); k=p["cost_usd"]/p["mwh"]/1000; s0=S_UTIL if "utility" in p["owner"].lower() else S_DEV
    out["ny"].append({**{a:p[a] for a in ("project","owner","mw","mwh","cod_year","cost_basis","confidence")},"nominal":k,"kw":p["cost_usd"]/p["mw"]/1000,"adj_installed":k*factor("installed",y,s0),"hours":p["mwh"]/p["mw"]})
for ix in NY["indices"]:
    out["ny"].append({"project":ix["name"],"owner":"NYSERDA program average","mw":None,"mwh":None,"cod_year":ix["year"],"cost_basis":ix["source"],"confidence":ix["confidence"],"nominal":ix["kwh"],"kw":None,"adj_installed":ix["kwh"]*factor("installed",ix["year"],S_DEV),"hours":None})
out["indexed_series"]={}
for key,ix in IDX.items():
    if ix["f"] is None: continue
    pts=sorted(int(y) for y in IXJ["indices"][key]["points"]); base=ix["f"](2018)
    out["indexed_series"][key]={"label":ix["label"],"base_2018":base,"points":[[y,IXJ["indices"][key]["points"][str(y)]/base] for y in pts]}
out["indexed_series"]["hw"]={"label":"Handy-Whitman NA construction (non-battery)","base_2018":HW(2018),"points":[[int(y),v/HW(2018)] for y,v in sorted((int(k),v) for k,v in IXJ["construction_index"]["points"].items())]}
json.dump(out,open(f"{B}/adjust_results.json","w"),indent=1)
print("factor by year (installed, utility anchor 0.40) and implied battery share:")
for y in (2015,2016,2017,2018,2019,2020,2021,2022,2024): print(f"  {y}: factor {factor('installed',y,S_UTIL):.2f}  share {share_at('installed',y,S_UTIL):.0%}   fixed-share model {factor_fixed_share('installed',y,0.40):.2f}   pack: {factor('pack',y,S_UTIL):.2f} / {share_at('pack',y,S_UTIL):.0%}   developer anchor: {factor('installed',y,S_DEV):.2f}")
for cname,blk in out["classes"].items():
    print(f"== {cname}: n={blk['n']} nominal median ${blk['nominal']['median']:,.0f}  HP stn pct {blk['nominal']['hp_pct']['station_direct']:.0%}")
    for key,v in blk["indices"].items():
        b=v["by_owner"]; fs=v["fixed_share_40"]
        print(f"   {key:13s} owner-share: ${b['median']:,.0f} (inst {b['hp_pct']['installed']:.0%}, stn {b['hp_pct']['station_direct']:.0%})  -10/+10: ${v['by_owner_minus10']['median']:,.0f}/${v['by_owner_plus10']['median']:,.0f}  uniform 0.4: ${v['by_share']['0.4']['median']:,.0f}  old fixed-share: ${fs['median']:,.0f} ({fs['hp_pct']['station_direct']:.0%})  naive ${v['naive_median']:,.0f}")
