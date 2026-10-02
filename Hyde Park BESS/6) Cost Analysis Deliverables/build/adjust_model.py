"""Dollar-year adjustment of the public comparables to 2026 (deck slides 12-13).
Two-component model: cost_2026 = cost_nominal x [ s x I(2026)/I(y) + (1-s) x (1+g)^(2026-y) ]
  s = battery share of the comparable's cost (default 0.40), I = battery index, g = non-battery construction escalation (3.5%/yr).
"""
import json, numpy as np
B="/tmp/claude-0/-home-user-BESS/078f934e-4ca0-5169-be3f-cb66ff0e2514/scratchpad/build"
R=json.load(open(f"{B}/stats_results.json")); P=R["reference_class"]["projects"]
NY=json.load(open(f"{B}/ny_cohort.json"))
HP={"contract":605.3,"installed":832.9,"station_direct":1483.3,"approval":2862.4}
SHARE=0.40; G=0.035
def interp(pts):
    xs=sorted(pts); return lambda y: float(np.interp(y,xs,[pts[x] for x in xs]))
INDICES={
 "installed":{"label":"Installed all-in (EIA-860 2015-18, LBNL 2024)","f":interp({2015:2152,2017:834,2018:625,2024:458,2026:458}),"primary":True,
              "source":"EIA Today in Energy #45596 (2015-2018 $/kWh); LBNL Utility-Scale Solar 2025 ($458/kWh, 2024); held flat 2024-26","conf":"High (points) / interpolated between"},
 "pack":{"label":"BNEF pack price (real $/kWh)","f":interp({2015:373,2016:288,2017:214,2018:176,2019:156,2020:137,2021:132,2022:151,2023:139,2024:115,2025:108,2026:108}),
         "source":"BloombergNEF Lithium-Ion Battery Price Survey, 2015-2025 editions","conf":"Medium (2015-2017 from memory of the releases; verify)"},
 "turnkey":{"label":"BNEF turnkey 4-h (2022 on; flat before)","f":interp({2015:324,2022:324,2023:263,2024:165,2025:117,2026:117}),
            "source":"BNEF Energy Storage System Cost Survey 2022-2025","conf":"Medium; no pre-2022 values retrieved"},
 "lcos":{"label":"Lazard LCOS midpoint, 100 MW 4-h (2019 on; flat before)","f":interp({2015:245,2019:245,2020:191,2024:233,2025:185,2026:251}),
         "source":"Lazard LCOS v5.0, v6.0, LCOE+ 2024, 2025, 2026 (unsubsidized ranges, midpoints)","conf":"Medium"},
 "construction":{"label":"Construction index only (3.5%/yr), no battery deflation","f":None,"source":"ENR-class proxy","conf":"Assumption"},
}
constr=lambda y:(1+G)**(2026-y)
def factor(key,y,s=SHARE):
    f=INDICES[key]["f"]
    if f is None: return constr(y)
    return s*f(2026)/f(y)+(1-s)*constr(y)
out={"share":SHARE,"g":G,"hp":HP,"indices":{},"projects":[],"ny":[]}
for key,ix in INDICES.items():
    adj=np.array([p["kwh"]*factor(key,int(p["cod_year"])) for p in P]); naive=np.array([p["kwh"]*(ix["f"](2026)/ix["f"](int(p["cod_year"])) if ix["f"] else constr(int(p["cod_year"]))) for p in P])
    out["indices"][key]={"label":ix["label"],"source":ix["source"],"conf":ix["conf"],"ratio_2018":(ix["f"](2026)/ix["f"](2018) if ix["f"] else constr(2018)),
        "median":float(np.median(adj)),"q25":float(np.percentile(adj,25)),"q75":float(np.percentile(adj,75)),"naive_median":float(np.median(naive)),
        "hp_pct":{k:float((adj<v).mean()) for k,v in HP.items()}}
out["nominal"]={"median":float(np.median([p["kwh"] for p in P])),"hp_pct":{k:float((np.array([p["kwh"] for p in P])<v).mean()) for k,v in HP.items()}}
for s in (0.3,0.5):
    adj=np.array([p["kwh"]*factor("installed",int(p["cod_year"]),s) for p in P]); out["indices"][f"installed_s{int(s*100)}"]={"label":f"Installed index, battery share {s:.0%}","median":float(np.median(adj)),"hp_pct":{k:float((adj<v).mean()) for k,v in HP.items()}}
for p in P:
    y=int(p["cod_year"]); out["projects"].append({"project":p["project"],"state":p["state"],"mw":p["mw"],"mwh":p["mwh"],"cod_year":y,"nominal":p["kwh"],
        "adj_installed":p["kwh"]*factor("installed",y),"adj_pack":p["kwh"]*factor("pack",y),"adj_lcos":p["kwh"]*factor("lcos",y),"factor_installed":factor("installed",y)})
for p in NY["projects"]:
    y=int(p["cod_year"]); k=p["cost_usd"]/p["mwh"]/1000
    out["ny"].append({**{a:p[a] for a in ("project","owner","mw","mwh","cod_year","cost_basis","confidence")},"nominal":k,"kw":p["cost_usd"]/p["mw"]/1000,"adj_installed":k*factor("installed",min(y,2026)),"hours":p["mwh"]/p["mw"]})
for ix in NY["indices"]:
    out["ny"].append({"project":ix["name"],"owner":"NYSERDA program average","mw":None,"mwh":None,"cod_year":ix["year"],"cost_basis":ix["source"],"confidence":ix["confidence"],"nominal":ix["kwh"],"kw":None,"adj_installed":ix["kwh"]*factor("installed",ix["year"]),"hours":None})
json.dump(out,open(f"{B}/adjust_results.json","w"),indent=1)
print("nominal median",round(out["nominal"]["median"]))
for k,v in out["indices"].items(): print(f"{k:16s} median {v['median']:7.0f}  naive {v.get('naive_median',0):7.0f}  HP inst/stn/appr {v['hp_pct']['installed']:.0%}/{v['hp_pct']['station_direct']:.0%}/{v['hp_pct']['approval']:.0%}")
for r in out["ny"]: print(f"NY {r['project'][:48]:48s} {r['cod_year']} nominal {r['nominal']:6.0f} adj {r['adj_installed']:6.0f}")
