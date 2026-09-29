"""Monte Carlo on Hyde Park BESS Rev 3 cost elements (Station 360 + Station 496), layer level.
Distributions are documented in-line with their source; outputs P10/P50/P80/P90 of the loaded total, the battery share,
and $/kWh at boundaries 3, 4 and 6. Deterministic seed for reproducibility."""
import json, numpy as np
B="/tmp/claude-0/-home-user-BESS/078f934e-4ca0-5169-be3f-cb66ff0e2514/scratchpad/build"
D=json.load(open(f"{B}/data.json")); L=D["layers_direct"]
import sys
WIDE = len(sys.argv)>1 and sys.argv[1]=="wide"
rng=np.random.default_rng(21334); N=20000
W = 1.6 if WIDE else 1.0  # widen the upside of every range by this factor of its (high-mode) spread
def tri(low,mode,high,n=N): return rng.triangular(low,mode,high,n)
def pert(low,mode,high,n=N,lam=4.0):
    high=mode+(high-mode)*W; low=mode-(mode-low)*min(W,1.0)
    a=1+lam*(mode-low)/(high-low); b=1+lam*(high-mode)/(high-low); return low+(high-low)*rng.beta(a,b,n)
A=L["A. Battery supply contract (Nomad)"]; Bv=L["B. Battery installation & integration (owner scope)"]; C=L["C. Battery balance-of-plant (GSUs, EMS/comms, aux power)"]
Dv=L["D. Station 360 13.8 kV switching & interconnection facilities"]; E=L["E. Site development & civil (former landfill site)"]; F=L["F. Station 496 feeder protection upgrades (interconnection)"]
G=L["G. Testing & commissioning"]; Hh=L["H. Owner soft costs (engineering, siting, environmental, outreach, PM, land)"]; I=L["I. Taxes, CWIP, builders-risk insurance"]
J=L["J. Risk register"]; K=L["K. Contingency"]; Ll=L["L. Indirects / overheads"]; M=L["M. AFUDC"]
contract=12106850.0; paid=1213042.82
# ---- element distributions (documented) ----
elem={}
# A: fixed-price contract. Uncertainty only on (i) whether $1.13M escalation is spent (contract fixes price) and (ii) change orders / scope adds (LDs cap 10%; MPA change-order exposure). Model: contract + change orders PERT(0%,2%,8%) of contract.
elem["A"]=contract + contract*pert(0.0,0.02,0.08)
# B: install labor basis is a percentage of a 2023 site total (25% vs 50% used in Rev 2); pads/fire suppression unit-priced. PERT(0.8x, 1.0x, 1.9x) on the labor-heavy layer.
elem["B"]=Bv*pert(0.8,1.0,1.9)
# C: GSUs from 2023 bidder list +3%/yr; HEG one-line showed 12 vs 4 GSUs (deduct booked if 4). PERT(0.85,1.0,1.35).
elem["C"]=C*pert(0.85,1.0,1.35)
# D: Siemens budgetary +/-30% on $1.2M of breakers; remaining station items from ESF unit library at conceptual maturity. PERT(0.8,1.0,1.45).
elem["D"]=Dv*pert(0.8,1.0,1.45)
# E: landfill platform. HEG deducts (retaining wall -$534K, basin -$156K, footprint -$581K, platform -$383K) vs HEG 4-F exposures (geotech $0.6M/$1.6M/$3.5M, soil $0.4M-$2.6M). Asymmetric: PERT(0.6, 1.0, 2.6).
elem["E"]=E*pert(0.6,1.0,2.6)
# F: Station 496 is its own approval-level estimate incl. its loaders; conceptual class. PERT(0.8,1.0,1.4).
elem["F"]=F*pert(0.8,1.0,1.4)
# G: testing hours from E-23-373; commissioning ownership of the 63-day window unresolved. PERT(0.8,1.0,1.5).
elem["G"]=G*pert(0.8,1.0,1.5)
# H: engineering flagged low (1.6% of total); siting/legal to Feb 2028 with EFSB fallback (18-24 mo). PERT(0.9,1.0,1.6).
elem["H"]=Hh*pert(0.9,1.0,1.6)
# I: taxes/CWIP/BAR follow the base. PERT(0.9,1.0,1.2).
elem["I"]=I*pert(0.9,1.0,1.2)
directs=sum(elem[k] for k in "ABCDEGHI")   # Sta 360 directs (stochastic)
# Loaders: indirects and AFUDC scale with Sta 360 directs and with schedule. AFUDC schedule factor PERT(0.95,1.0,1.35) for 0-12 months of siting slip.
ind=Ll*(directs/ (A+Bv+C+Dv+E+G+Hh+I))
afudc=M*(directs/(A+Bv+C+Dv+E+G+Hh+I))*pert(0.95,1.0,1.35)
# Risk register + contingency: the element ranges above already model the outcomes the register funds, so J and K are NOT added again (avoids double count). Report both views.
total_excl_JK=directs+ind+afudc+elem["F"]
total_incl_JK=total_excl_JK+J+K
approval=57247300.0
def q(x): return {p:float(np.percentile(x,p)) for p in (10,50,80,90)}
out=dict(N=N,
  total_excl_JK=q(total_excl_JK), total_incl_JK=q(total_incl_JK),
  p_exceed_approval_excl_JK=float((total_excl_JK>approval).mean()),
  p_exceed_approval_incl_JK=float((total_incl_JK>approval).mean()),
  battery_share=q(elem["A"]/total_excl_JK),
  b3_per_kwh=q((elem["A"]+elem["B"]+elem["C"])/20000),
  b4_per_kwh=q(directs/20000),
  b6_per_kwh=q(total_excl_JK/20000),
  contributions={k:float(np.std(elem[k])) for k in elem},
  mean_by_layer={k:float(np.mean(elem[k])) for k in elem},
  det_by_layer={"A":A,"B":Bv,"C":C,"D":Dv,"E":E,"F":F,"G":G,"H":Hh,"I":I},
)
# implied contingency needed to reach P80 vs risk+contingency carried
out["implied_P80_reserve_over_directs"]=out["total_excl_JK"][80]-(A+Bv+C+Dv+E+G+Hh+I+Ll+M+F)
out["carried_risk_plus_contingency"]=J+K
sfx="_wide" if WIDE else ""
json.dump(out,open(f"{B}/mc_results{sfx}.json","w"),indent=1)
np.save(f"{B}/mc_total_excl_JK{sfx}.npy",total_excl_JK); np.save(f"{B}/mc_b4{sfx}.npy",directs/20000); np.save(f"{B}/mc_b3{sfx}.npy",(elem["A"]+elem["B"]+elem["C"])/20000)
for k,v in out.items():
    if k not in ("contributions","mean_by_layer","det_by_layer"): print(k, v)
print("std by layer:",{k:round(v/1e6,2) for k,v in out["contributions"].items()})
