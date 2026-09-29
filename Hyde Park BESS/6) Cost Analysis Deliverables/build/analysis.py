"""Hyde Park BESS cost analysis: classify ESF Total Rev 3 line items into layers and compute unit costs."""
import openpyxl, json, re, collections
REPO="/home/user/BESS"
OUT="/tmp/claude-0/-home-user-BESS/078f934e-4ca0-5169-be3f-cb66ff0e2514/scratchpad/build"
MW, MWH = 10.0, 20.0
f=f"{REPO}/Hyde Park BESS/1) Estimate Summary Form/ESF - Hyde Park BESS Total Rev 3.xlsm"
wb=openpyxl.load_workbook(f,read_only=True,data_only=True)
ws=wb["Item"]
rows=[]; cur=None
for r in ws.iter_rows(values_only=True):
    c=list(r)+[None]*10
    if isinstance(c[1],str) and c[1].startswith("Hyde Park BESS - Sta"): cur=c[1]; continue
    if cur and isinstance(c[1],str) and re.match(r"^\d\d$",c[1]):
        rows.append(dict(est=cur,cbs1=c[1],cbs4=c[2],seq=int(c[3] or 0),desc=str(c[4]),qty=c[5],unit=c[6],cost=float(c[7] or 0),mh=float(c[8] or 0),note=str(c[9] or "")))
# ---------- classification for Sta 360 ----------
SEQ = {}
def tag(seqs, layer): 
    for s in seqs: SEQ[s]=layer
tag([432,445],"A. Battery supply contract (Nomad)")
tag([485,430,431,480,481,393,395,394,396,413,414],"B. Battery installation & integration (owner scope)")
tag([338,339,336,337,476,477,478,479],"C. Battery balance-of-plant (GSUs, EMS/comms, aux power)")
tag([302,303,310,311,334,335,326,327,324,325,419,420,428,429,472,473,320,321,470,471,421,422,411,412,423,425,415,416,417,418,397,398,399,400,403,404,298,299,387,388,391,392,312,313,260,261,262,263,264,265,266,267,268,269,474,475,294,295,296,297,132,352,487],"D. Station 360 13.8 kV switching & interconnection facilities")
tag([283,288,289,341,342,343,344,290,291,292,293,286,287,270,271,276,277,278,279],"E. Site development & civil (former landfill site)")
def layer(row):
    if "Sta. 496" in row["est"]: return "F. Station 496 feeder protection upgrades (interconnection)"
    s=row["seq"]; d=row["desc"]
    if s in SEQ: return SEQ[s]
    if d.startswith("Mobilization") or d.startswith("Demobilization"): return "E. Site development & civil (former landfill site)"
    c=row["cbs1"]
    if c=="08": return "G. Testing & commissioning"
    if c in ("01","02","03","04","05","09"): return "H. Owner soft costs (engineering, siting, environmental, outreach, PM, land)"
    if c=="11": return "I. Taxes, CWIP, builders-risk insurance"
    if c=="12": return "J. Risk register"
    if c=="15": return "K. Contingency"
    if c=="13": return "L. Indirects / overheads"
    if c=="14": return "M. AFUDC"
    if c in ("06","07"): return "UNCLASSIFIED"
    return "UNCLASSIFIED"
for r in rows: r["layer"]=layer(r)
unc=[r for r in rows if r["layer"]=="UNCLASSIFIED"]
assert not unc, [(r["seq"],r["desc"],r["cost"]) for r in unc]
tot=collections.OrderedDict()
for r in rows: tot[r["layer"]]=tot.get(r["layer"],0)+r["cost"]
tot=collections.OrderedDict(sorted(tot.items()))
grand=sum(tot.values())
print(f"Grand total check: {grand:,.0f}")
for k,v in tot.items(): print(f"{k:75s} {v:>14,.0f} {v/grand:6.1%}")
# ---------- loaded view: allocate J,K,L,M across direct layers A-I pro rata (Sta 360 only), 496 stays whole ----------
sta360=[r for r in rows if "Sta. 360" in r["est"]]; sta496=[r for r in rows if "Sta. 496" in r["est"]]
def sums(rs):
    d={}
    for r in rs: d[r["layer"]]=d.get(r["layer"],0)+r["cost"]
    return d
d360=sums(sta360); d496=sums(sta496)
direct_layers=[k for k in d360 if k[0] in "ABCDEFGHI"]
loaders=[k for k in d360 if k[0] in "JKLM"]
direct_sum=sum(d360[k] for k in direct_layers); load_sum=sum(d360[k] for k in loaders)
factor=(direct_sum+load_sum)/direct_sum
loaded={k:d360[k]*factor for k in direct_layers}
loaded["F. Station 496 feeder protection upgrades (interconnection)"]=sum(d496.values())
print(f"\nSta360 directs {direct_sum:,.0f}  loaders {load_sum:,.0f}  factor {factor:.4f}")
for k,v in sorted(loaded.items()): print(f"LOADED {k:75s} {v:>14,.0f}")
print("loaded total", sum(loaded.values()))
# ---------- key figures ----------
nomad_contract=12106850.0
dline_conceptual=4793000.0   # SSF Dec-2023, project 24211, not re-estimated
approval_21334=57247300.0
data=dict(
  mw=MW,mwh=MWH,
  nomad_contract=nomad_contract, nomad_equipment=10638000.0, nomad_spares=125000.0, nomad_warranty=797850.0, nomad_support=210000.0,
  nomad_shipping=90000.0, nomad_labor=246000.0, nomad_training=30000.0,
  approval_21334=approval_21334, sta360=49994200.0, sta496=7253100.0, dline_conceptual=dline_conceptual,
  layers_direct=tot, layers_loaded=loaded, load_factor=factor,
  actuals_to_date=5222044.99, actuals_date="2026-09-23",
  timeline=[
    dict(date="2021-06", label="Initial Funding Request (IFR)", value=200000, basis="IFR approved 6/11/2021; 15 MW/20 MWh concept; ISD Q3 2025", kind="funding"),
    dict(date="2023-05", label="IFR Rev 1", value=500000, basis="Cumulative initial funding $300K + $200K", kind="funding"),
    dict(date="2023-07", label="Vendor indicative pricing, 5 bidders (Site Two, 10 MW/20 MWh)", value=18222342, basis="Company 3 turnkey indicative price; range $9.59M-$18.22M across bidders", kind="vendor"),
    dict(date="2023-12", label="E-23-373 conceptual estimate", value=43926100, basis="Conceptual -25/+50%; ISD 4/23/2027; 2023 dollars escalated", kind="estimate"),
    dict(date="2024-02", label="SSF preferred alternative (BESS + D-Line)", value=49200000, basis="$44.379M station + $4.793M distribution; SDC 2/15/2024", kind="estimate"),
    dict(date="2024-07", label="Partial Funding Rev 1", value=4009000, basis="EPAC 7/10/2024", kind="funding"),
    dict(date="2026-02", label="Partial Funding Rev 2", value=5767000, basis="PowerPlan 2/18/2026; FF estimate still $43.926M", kind="funding"),
    dict(date="2026-03", label="Nomad cover agreement executed", value=12106850, basis="Fixed price, 12 Voyager units, 10-yr warranty; SOV dated 12/8/2025", kind="vendor"),
    dict(date="2026-06", label="Partial Funding Rev 3", value=8914000, basis="EPAC 6/25/2026; FF estimate still $43.926M; ISD 12/28/2028", kind="funding"),
    dict(date="2026-08", label="Sta 360 + 496 estimate Rev 0", value=47201100, basis="ESF 8/26/2026; battery line carried at ~$6M", kind="estimate"),
    dict(date="2026-09-01", label="Estimate Rev 1", value=51867100, basis="Battery material increased per project team", kind="estimate"),
    dict(date="2026-09-10", label="Estimate Rev 2", value=63640300, basis="Battery line reset to cover agreement ($13.1M escalated) + $1.5M relays", kind="estimate"),
    dict(date="2026-09-24", label="Estimate Rev 3 (current)", value=57247300, basis="Relays removed (-$1.5M), SSVT qty 3->1, engineering re-based to $501K + actuals", kind="estimate"),
  ],
  isd_history=[("2021-06","Q3 2025"),("2023-12","Apr 2027"),("2024-02","Sep 2027"),("2026-01","Aug 2028"),("2026-06","Dec 2028")],
  indicative_2023={"Company 1":11551925,"Company 2 (Opt 1)":10532000,"Company 2 (Opt 2)":9586600,"Company 3":18222342,"Company 4":11470000,"Company 5":13915000},
  e23373_categories={"Environmental":310100,"Outreach":275400,"Siting":252500,"Engineering":789600,"Materials":13761800,"Construction":6921200,"Testing":1063800,"PMT":1037700,"Other":934900,"Risks":3950000,"Indirects":9522600,"AFUDC":3298600,"Contingency":1807900},
  rev3_categories_21334={"ROW/Land":3100,"Environmental":179200,"Project Services":304600,"Siting":1429500,"Engineering":956300,"Materials":16678100,"Construction":8052600,"Testing":3077400,"PMT":1893200,"Removals":123500,"Other":863900,"Risks":6070000,"Indirects":9986700,"AFUDC":5014000,"Contingency":2615200},
  escalation_included=2948100,
  heg_class3_base=19216899, heg_savings_ceiling=2912000, heg_savings_cost=147000, heg_avoided=1467000,
  risk_items_360={"Environmental (DEP/landfill)":300000,"Additional outreach":250000,"P&C engineering":300000,"Station engineering":300000,"BAR deductibles":250000,"Design/scope changes":800000,"Labor cost":800000,"Material cost/tariffs":1000000,"UG obstructions":450000,"Siting/permitting delay":250000,"Soil contamination":300000,"Weather":300000},
)
data["rows"]=rows
json.dump(data,open(f"{OUT}/data.json","w"),indent=1,default=str)
print("written")
