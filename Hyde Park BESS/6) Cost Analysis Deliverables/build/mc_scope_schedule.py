"""Integrated Monte Carlo on cost, scope and schedule for Hyde Park BESS (5 Oct 2026).
Three postures on one simulation: STATUS QUO (no lever pursued; threats live), MANAGED (levers pursued at the assessed
probability of realization), CEILING (every lever realized at its mid value). Threats and estimate-accuracy ranges are live in
all three. Schedule: siting-chain slip, long-lead equipment slip and construction variance, converted to dollars per month.
Outputs mc_scope_results.json and three charts. Deterministic seed."""
import json, numpy as np
B="/tmp/claude-0/-home-user-BESS/078f934e-4ca0-5169-be3f-cb66ff0e2514/scratchpad/build"
D=json.load(open(f"{B}/data.json")); L=D["layers_direct"]; SV=json.load(open(f"{B}/savings.json")); SC=json.load(open(f"{B}/scope_challenge.json"))
MARG=SV["marginal_loader"]; APP=D["approval_21334"]; rng=np.random.default_rng(21334); N=20000
def pert(lo,mode,hi,n=N,lam=4.0):
    if hi<=lo: return np.full(n,float(mode))
    a=1+lam*(mode-lo)/(hi-lo); b=1+lam*(hi-mode)/(hi-lo); return lo+(hi-lo)*rng.beta(a,b,n)
def bern(p,n=N): return rng.random(n)<p
A=L["A. Battery supply contract (Nomad)"]; Bv=L["B. Battery installation & integration (owner scope)"]; C=L["C. Battery balance-of-plant (GSUs, EMS/comms, aux power)"]
Dv=L["D. Station 360 13.8 kV switching & interconnection facilities"]; E=L["E. Site development & civil (former landfill site)"]; F=L["F. Station 496 feeder protection upgrades (interconnection)"]
G=L["G. Testing & commissioning"]; Hh=L["H. Owner soft costs (engineering, siting, environmental, outreach, PM, land)"]; I=L["I. Taxes, CWIP, builders-risk insurance"]
J=L["J. Risk register"]; K=L["K. Contingency"]; Ll=L["L. Indirects / overheads"]; M=L["M. AFUDC"]
dirs0=A+Bv+C+Dv+E+G+Hh+I; L_actual=1964236.0; L_basis=Ll-L_actual
# ---------------- estimate accuracy by layer (two-sided), ranges as in mc_model.py with the battery fixed ----------------
acc={"B. Install labor basis":Bv*(pert(0.8,1.0,1.9)-1),"C. GSUs and auxiliaries":C*(pert(0.85,1.0,1.35)-1),"D. Switching station (unit library)":Dv*(pert(0.8,1.0,1.45)-1),
     "E. Landfill platform and civil":E*(pert(0.6,1.0,2.6)-1),"F. Station 496 program":F*(pert(0.8,1.0,1.4)-1),"G. Testing hours":G*(pert(0.8,1.0,1.5)-1),"H. Owner soft costs":Hh*(pert(0.9,1.0,1.6)-1),"I. Taxes and insurance":I*(pert(0.9,1.0,1.2)-1)}
# ---------------- opportunities: (label, probability of realization, low, high, loaded?) ----------------
SVI={i["id"]:i for i in SV["items"]}
OPP=[("A1 Battery escalation removed",0.80,SVI["A1"]["lo_loaded"],SVI["A1"]["hi_loaded"]),("A2 Risk lines that duplicate escalation",0.70,SVI["A2"]["lo"],SVI["A2"]["hi"]),
     ("A4 E&S overhead basis off the vendor contract",0.30,SVI["A4"]["lo"],SVI["A4"]["hi"]),("A5 Commissioning overlap with Nomad",0.50,SVI["A5"]["lo_loaded"],SVI["A5"]["hi_loaded"]),
     ("B1 Station 496 relay program at benchmark",0.50,SVI["B1"]["lo"],SVI["B1"]["hi"]),("B2 Two-feeder topology",0.35,SVI["B2"]["lo_loaded"],SVI["B2"]["hi_loaded"]),
     ("B3 Platform and wall after geotech",0.40,SVI["B3"]["lo_loaded"],SVI["B3"]["hi_loaded"]),("B4 Battery install crew build-up",0.60,SVI["B4"]["lo_loaded"],SVI["B4"]["hi_loaded"]),
     ("B5 Disconnect and PT double count",0.90,SVI["B5"]["lo_loaded"],SVI["B5"]["hi_loaded"]),("B6 GSU install hours",0.60,SVI["B6"]["lo_loaded"],SVI["B6"]["hi_loaded"]),
     ("B7 Switchyard lighting",0.70,SVI["B7"]["lo_loaded"],SVI["B7"]["hi_loaded"]),("B8 Siting task budgets",0.40,SVI["B8"]["lo_loaded"],SVI["B8"]["hi_loaded"]),("C3 AFUDC: battery payment timing",0.50,SVI["C3"]["lo"],SVI["C3"]["hi"])]
# ---------------- threats: (label, probability, low, mode, high) direct unless noted; loaded where they sit in directs ----------------
THR=[("T1 Haugland reconciliation moves the construction base up",0.60,2.0e6*MARG,5.0e6*MARG,8.0e6*MARG),("T2 Sound mitigation",0.60,0.3e6*MARG,0.4e6*MARG,0.5e6*MARG),
     ("T3 Visual screening or facade",0.70,0.2e6*MARG,0.3e6*MARG,0.5e6*MARG),("T4 Police details and traffic control",0.80,0.1e6*MARG,0.2e6*MARG,0.3e6*MARG),
     ("T5 NFPA 855 hazard-analysis changes",0.40,0.1e6*MARG,0.3e6*MARG,0.6e6*MARG),("T6 GSU count: twelve, not four",0.35,0.6e6*MARG,0.8e6*MARG,1.0e6*MARG),
     ("T7 Nomad change orders and tariff pass-through",0.50,0.3e6,0.6e6,1.2e6),("T8 Outage-window premiums at Station 496",0.50,0.2e6,0.3e6,0.5e6)]
# ---------------- schedule ----------------
siting_slip=np.where(bern(0.50),pert(2,6,14),0.0); efsb=bern(0.08); siting_slip=np.where(efsb,pert(18,21,24),siting_slip)
equip_slip=np.where(bern(0.30),pert(2,4,6),0.0)                 # GSU / transformer lead time (29-70 weeks reported)
constr_var=pert(-1,0,3)                                            # construction duration variance
slip=np.maximum(siting_slip,equip_slip)+constr_var; slip=np.maximum(slip,-1)
cost_per_month=pert(0.30e6,0.37e6,0.45e6)                          # AFUDC on CWIP, escalation on remaining spend, PM/CM/owner, indirects on those (deck: about $5M per 12 months)
sched_cost=np.maximum(slip,0)*cost_per_month
# ---------------- assemble ----------------
acc_sum=sum(acc.values())
opp_draw={lab:np.where(bern(p),pert(lo,0.5*(lo+hi),hi),0.0) for lab,p,lo,hi in OPP}
opp_mid={lab:0.5*(lo+hi) for lab,p,lo,hi in OPP}
thr_draw={lab:np.where(bern(p),pert(lo,md,hi),0.0) for lab,p,lo,md,hi in THR}
acc_loaded=acc_sum*MARG   # accuracy ranges sit in the directs: contingency, basis indirects and AFUDC scale with them
thr_sum=sum(thr_draw.values()); opp_sum=sum(opp_draw.values()); opp_ceiling=sum(opp_mid.values())
base=APP-J-K   # the estimate without its reserves ($49.6M); the modeled outcomes are what the $7.6M of risk register and contingency exist to fund
status_quo=base+acc_loaded+thr_sum+sched_cost   # compared to the $57.2M approval: does the reserve cover the outcome?
managed=status_quo-opp_sum
ceiling=status_quo-opp_ceiling
def q(x): return {str(p):float(np.percentile(x,p)) for p in (10,50,80,90)}
res={"N":N,"approval":APP,"base_ex_reserve":APP-J-K,"reserve":J+K,"marginal_loader":MARG,
     "cases":{"status_quo":{**q(status_quo),"p_over_approval":float((status_quo>APP).mean()),"mean":float(status_quo.mean())},
              "managed":{**q(managed),"p_over_approval":float((managed>APP).mean()),"p_under_50":float((managed<50e6).mean()),"mean":float(managed.mean())},
              "ceiling":{**q(ceiling),"p_over_approval":float((ceiling>APP).mean()),"p_under_50":float((ceiling<50e6).mean()),"mean":float(ceiling.mean())}},
     "schedule":{"slip_months":q(slip),"p_slip_gt_0":float((slip>0.5).mean()),"p_slip_gt_6":float((slip>6).mean()),"p_slip_gt_12":float((slip>12).mean()),"p_efsb":float(efsb.mean()),"sched_cost":q(sched_cost),"cost_per_month":q(cost_per_month),
                 "isd_p50":"Dec 2028 + %.0f months"%np.percentile(slip,50),"isd_p80":"Dec 2028 + %.0f months"%np.percentile(slip,80)},
     "components":{"accuracy_loaded":q(acc_loaded),"threats":q(thr_sum),"opportunities_managed":q(opp_sum),"opportunity_ceiling":opp_ceiling,"schedule":q(sched_cost)}}
# ---------------- tornado: effect of each driver on the managed total (P10 to P90 of its own contribution; mean) ----------------
rows=[]
for lab,p,lo,hi in OPP:
    x=-opp_draw[lab]; rows.append({"driver":lab,"kind":"opportunity","p":p,"p10":float(np.percentile(x,10)),"p90":float(np.percentile(x,90)),"mean":float(x.mean()),"full":-0.5*(lo+hi),"owner":SVI[lab[:2]]["owner"]})
for lab,p,lo,md,hi in THR:
    x=thr_draw[lab]; rows.append({"driver":lab,"kind":"threat","p":p,"p10":float(np.percentile(x,10)),"p90":float(np.percentile(x,90)),"mean":float(x.mean()),"full":md})
for lab,x in acc.items():
    xl=x*MARG; rows.append({"driver":"Accuracy: "+lab,"kind":"accuracy","p":1.0,"p10":float(np.percentile(xl,10)),"p90":float(np.percentile(xl,90)),"mean":float(xl.mean())})
rows.append({"driver":"Schedule slip (siting chain, long-lead, construction)","kind":"schedule","p":float((slip>0.5).mean()),"p10":float(np.percentile(sched_cost,10)),"p90":float(np.percentile(sched_cost,90)),"mean":float(sched_cost.mean())})
# contribution to variance (Spearman) on the managed total
from scipy.stats import spearmanr
drivers={**{lab:-v for lab,v in opp_draw.items()},**thr_draw,**{"Accuracy: "+k:v*MARG for k,v in acc.items()},"Schedule slip (siting chain, long-lead, construction)":sched_cost}
rho={k:(spearmanr(v,managed).correlation if np.std(v)>0 else 0.0) for k,v in drivers.items()}
tot=sum(r*r for r in rho.values()); 
for r in rows: r["rho"]=float(rho[r["driver"]]); r["var_share"]=float(rho[r["driver"]]**2/tot)
rows.sort(key=lambda r: -max(abs(r["p10"]),abs(r["p90"])))
res["tornado"]=rows
# ranked aggressiveness table: expected value, controllability
rank=[{"driver":r["driver"],"ev":-r["mean"],"full":-r["full"],"p":r["p"],"owner":r.get("owner","")} for r in rows if r["kind"]=="opportunity"]; rank.sort(key=lambda r:-r["ev"]); res["ranked_opportunities"]=rank
res["threat_ev"]=sorted([{"driver":r["driver"],"ev":r["mean"],"p":r["p"],"full":r["full"]} for r in rows if r["kind"]=="threat"],key=lambda r:-r["ev"])
json.dump(res,open(f"{B}/mc_scope_results.json","w"),indent=1)
np.save(f"{B}/mc_scope_status_quo.npy",status_quo); np.save(f"{B}/mc_scope_managed.npy",managed); np.save(f"{B}/mc_scope_ceiling.npy",ceiling); np.save(f"{B}/mc_scope_slip.npy",slip)
for k,v in res["cases"].items(): print(k,{kk:(round(vv/1e6,1) if vv>1000 else round(vv,3)) for kk,vv in v.items()})
print("schedule",{k:(v if isinstance(v,str) else (round(v,2) if not isinstance(v,dict) else {kk:round(vv/1e6,2) if vv>1000 else round(vv,1) for kk,vv in v.items()})) for k,v in res["schedule"].items()})
print("components",{k:({kk:round(vv/1e6,2) for kk,vv in v.items()} if isinstance(v,dict) else round(v/1e6,2)) for k,v in res["components"].items()})
for r in rows: print(f"{r['kind']:11s} {r['driver'][:55]:55s} p={r['p']:.2f} p10 {r['p10']/1e6:+.2f} mean {r['mean']/1e6:+.2f} p90 {r['p90']/1e6:+.2f} var {r['var_share']:.2f}")
