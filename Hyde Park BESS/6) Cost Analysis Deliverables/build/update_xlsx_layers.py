import json, openpyxl
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.workbook.properties import CalcProperties
B="/tmp/claude-0/-home-user-BESS/078f934e-4ca0-5169-be3f-cb66ff0e2514/scratchpad/build"
LX=json.load(open(f"{B}/layer_index_results.json")); LJ=json.load(open(f"{B}/indices_layers.json")); IXJ=json.load(open(f"{B}/indices.json")); SV=json.load(open(f"{B}/savings.json")); D=json.load(open(f"{B}/data.json"))
wb=openpyxl.load_workbook(f"{B}/Hyde_Park_BESS_Cost_Analysis.xlsx")
NAVY="001E60"; hdr=Font(bold=True,color="FFFFFF",name="Calibri",size=10); hfill=PatternFill("solid",fgColor=NAVY)
base=Font(name="Calibri",size=10); blue=Font(name="Calibri",size=10,color="0000FF"); bold=Font(name="Calibri",size=10,bold=True); title=Font(name="Georgia",size=14,bold=True,color=NAVY); note=Font(name="Calibri",size=9,italic=True,color="6B7280")
def H(ws,r,c,vals):
    for j,v in enumerate(vals):
        cell=ws.cell(row=r,column=c+j,value=v); cell.font=hdr; cell.fill=hfill; cell.alignment=Alignment(wrap_text=True,vertical="center")
# ---------- Layer Escalators
for nm in ("Layer Escalators","Savings Register"):
    if nm in wb.sheetnames: del wb[nm]
ws=wb.create_sheet("Layer Escalators", index=wb.sheetnames.index("2026$ Adjustment")+1)
ws["A1"]="Per-layer escalators: one published index per cost layer (deck slides 17-18)"; ws["A1"].font=title
ws["A2"]="cost_2026 = cost_y x SUM_i( w_i x I_i(2026) / I_i(y) ). Weights from the Rev 3 loaded layers (Hyde Park) or the NREL/PNNL merchant structure (developer). Blue = input. Series values and confidence tags from indices_layers.json; fetch_indices.py replaces them from the FRED/BLS APIs when the hosts are allowed."; ws["A2"].font=note
keys=[("bat_installed","Battery: EIA/LBNL installed",IXJ["indices"]["installed"]["points"]),("labor","Labor: IBEW 103 base rate",LJ["series"]["labor"]["points"]),("transformer","PPI transformers WPU117409",LJ["series"]["transformer"]["points"]),("switchgear","PPI switchgear WPU1175",LJ["series"]["switchgear"]["points"]),("civil","ENR CCI 20-city",LJ["series"]["civil"]["points"]),("engineering","PPI engineering services WPU4532",LJ["series"]["engineering"]["points"]),("hw","Handy-Whitman NA production plant",IXJ["construction_index"]["points"]),("hw_dist_station","Handy-Whitman NA dist. station equipment (362)",LJ["series"]["hw_dist_station"]["points"]),("eci_construction","ECI construction (alt. labor)",LJ["series"]["eci_construction"]["points"]),("construction_inputs","PPI construction inputs WPUIP2300001",LJ["series"]["construction_inputs"]["points"])]
import numpy as np
def ip(d,y):
    xs=sorted(int(k) for k in d); return float(np.interp(y,xs,[float(d[str(x)]) for x in xs]))
r=4; ws.cell(row=r,column=1,value="A. Index series (published points in blue; interpolated between, held flat outside)").font=bold; r+=1
H(ws,r,1,["Year"]+[k[1] for k in keys]); r+=1; t0=r
for y in range(2015,2027):
    ws.cell(row=r,column=1,value=y).font=base
    for j,(k,lab,pts) in enumerate(keys,2):
        c=ws.cell(row=r,column=j,value=round(ip(pts,y),2)); c.font=blue if str(y) in pts else base
    r+=1
t1=r-1
ws.cell(row=r,column=1,value="2018 to 2026 ratio").font=bold
for j in range(2,2+len(keys)):
    col=openpyxl.utils.get_column_letter(j); c=ws.cell(row=r,column=j,value=f"={col}{t1}/{col}{t0+3}"); c.font=bold; c.number_format="0.00"
rr=r; r+=1
ws.cell(row=r,column=1,value="Confidence: "+"; ".join(f"{k[1]}: {LJ['series'].get(k[0],{}).get('conf', IXJ['indices'].get('installed',{}).get('conf','') if k[0]=='bat_installed' else IXJ['construction_index']['conf'])}" for k in keys)).font=note; r+=2
ws.cell(row=r,column=1,value="B. Layer map and weights (Hyde Park = Rev 3 loaded layers; blue = editable)").font=bold; r+=1
H(ws,r,1,["Layer","Loaded $ (Rev 3)","Weight","Escalator column","2018 to 2026 ratio","Weight / ratio"]); r+=1; m0=r
LL=D["layers_loaded"]; tot=sum(LL.values()); colof={k[0]:openpyxl.utils.get_column_letter(j) for j,k in enumerate(keys,2)}
for layer in "ABCDEFGHI":
    name=[k for k in LL if k[0]==layer][0]; esc=LX["map_hp"][layer]
    ws.cell(row=r,column=1,value=name).font=base; c=ws.cell(row=r,column=2,value=round(LL[name])); c.font=base; c.number_format='"$"#,##0'
    w=ws.cell(row=r,column=3,value=f"=B{r}/SUM($B${m0}:$B${m0+8})"); w.number_format="0.0%"
    ws.cell(row=r,column=4,value=[k[1] for k in keys if k[0]==esc][0]).font=blue
    ws.cell(row=r,column=5,value=f"={colof[esc]}{rr}").number_format="0.00"
    ws.cell(row=r,column=6,value=f"=C{r}/E{r}").number_format="0.000"; r+=1
ws.cell(row=r,column=1,value="Composite, Hyde Park scope, quantities fixed: a 2018 project in 2026 dollars = 1 / SUM(weight / ratio)").font=bold; c=ws.cell(row=r,column=6,value=f"=1/SUM(F{m0}:F{r-1})"); c.font=bold; c.number_format="0.00"; r+=1
ws.cell(row=r,column=1,value=f"Two-component model, fixed quantities (anchor 40%): {LX['factors']['2018']['two_component']:.3f} for 2018, {LX['factors']['2016']['two_component']:.3f} for 2016; earlier fixed-share form: {LX['factors']['2018']['two_component_fixed_share']:.3f} / {LX['factors']['2016']['two_component_fixed_share']:.3f}; whole cost at the battery rate: {LX['factors']['2018']['naive_battery']:.3f}; Handy-Whitman only: {LX['factors']['2018']['hw_only']:.3f}").font=note; r+=2
ws.cell(row=r,column=1,value="C. Reference class (55 projects) under each method, 2026 $/kWh (values from layer_index_model.py)").font=bold; r+=1
H(ws,r,1,["Method","Class median","Q25","Q75","HP installed pct","HP station pct","Utility subclass median","HP station pct (utility)"]); r+=1
labs={"nominal":"As published","naive_battery":"Whole cost at the battery rate","two_component":"Battery 40% + Handy-Whitman 60%","layer_developer":"One index per layer, developer weights","layer_hp":"One index per layer, Hyde Park weights","layer_developer_pack":"Layer method, BNEF pack for the battery","layer_developer_turnkey":"Layer method, BNEF turnkey for the battery","two_component_fixed_share":"Earlier version: today's 40% share held fixed (superseded 5 Oct 2026)","layer_hp_fixed_share":"Earlier layer version, fixed shares (superseded)"}
M=LX["classes"]["reference_class"]["methods"]; MU=LX["classes"]["reference_class_utility"]["methods"]
for k,lab in labs.items():
    v=M[k]; u=MU[k]; vals=[lab,round(v["median"]),round(v["q25"]),round(v["q75"]),v["hp_pct"]["installed"],v["hp_pct"]["station_direct"],round(u["median"]),u["hp_pct"]["station_direct"]]
    for j,x in enumerate(vals,1):
        c=ws.cell(row=r,column=j,value=x); c.font=base
        if j in (2,3,4,7): c.number_format='"$"#,##0'
        if j in (5,6,8): c.number_format="0%"
    r+=1
r+=1; ws.cell(row=r,column=1,value="Developer composition (shares): "+", ".join(f"{k} {v:.0%}" for k,v in LX["weights_dev"].items())+". "+LJ["composition_developer"]["note"]).font=note
for col,wd in zip("ABCDEFGHIJK",(44,16,12,30,14,12,16,16,14,14,14)): ws.column_dimensions[col].width=wd
# ---------- Savings Register
ws=wb.create_sheet("Savings Register", index=wb.sheetnames.index("Statistics")+1)
ws["A1"]="Cost-saving opportunity register (deck slides 27-29), sized from the Rev 3 rows"; ws["A1"].font=title
ws["A2"]="Direct ranges from savings_model.py. Loaded = direct x marginal loader for items that scale with directs (contingency, basis-driven indirects, AFUDC); the risk register, overhead policy items and Tier C do not scale. Tier C reduces the revenue requirement, not the $57.2M. Tiers A and B are gross of the Haugland reconciliation (red team KS1, +$4M to +$8M direct). Blue = input."; ws["A2"].font=note
ws["A4"]="Marginal loader"; c=ws["B4"]; c.value=round(SV["marginal_loader"],3); c.font=blue; ws["C4"]="1 + (contingency + basis-driven indirects + AFUDC) / Station 360 directs; the average loader on slide 5 is 1.685"; ws["C4"].font=note
ws["A5"]="Approval level"; c=ws["B5"]; c.value=SV["approval"]; c.number_format='"$"#,##0'
r=7; H(ws,r,1,["#","Tier","Lever","Layer","Direct low","Direct high","Scales with loader (1/0)","Loaded low","Loaded high","Confidence","Owner","What must close","Evidence"]); r+=1; i0=r
for it in SV["items"]:
    vals=[it["id"],it["tier"],it["title"],it["layer"],round(it["lo"]),round(it["hi"]),1 if it["scales"] else 0,f"=E{r}*IF(G{r}=1,$B$4,1)",f"=F{r}*IF(G{r}=1,$B$4,1)",it["conf"],it["owner"],it["close"],it["ev"]]
    for j,x in enumerate(vals,1):
        c=ws.cell(row=r,column=j,value=x); c.font=blue if j in (5,6,7) else base; c.alignment=Alignment(wrap_text=True,vertical="top")
        if j in (5,6,8,9): c.number_format='"$"#,##0'
    r+=1
i1=r-1; r+=1
for t,lab in (("A","Tier A: estimate hygiene"),("B","Tier B: value engineering"),("C","Tier C: financial and structural (revenue requirement)")):
    ws.cell(row=r,column=3,value=lab).font=bold
    for j,col in ((5,"E"),(6,"F"),(8,"H"),(9,"I")):
        c=ws.cell(row=r,column=j,value=f'=SUMIF($B${i0}:$B${i1},"{t}",{col}{i0}:{col}{i1})'); c.font=bold; c.number_format='"$"#,##0'
    r+=1
ws.cell(row=r,column=3,value="Tiers A + B against the approval level").font=bold
for j,col in ((8,"H"),(9,"I")):
    c=ws.cell(row=r,column=j,value=f'=SUMIF($B${i0}:$B${i1},"A",{col}{i0}:{col}{i1})+SUMIF($B${i0}:$B${i1},"B",{col}{i0}:{col}{i1})'); c.font=bold; c.number_format='"$"#,##0'
r+=2
ws.cell(row=r,column=1,value="Station 496 relay program detail").font=bold; r+=1
RL=SV["relay"]
for lab,v,fmt in (("Relays",RL["n"],"0"),("Hardware furnish $",RL["furnish"],'"$"#,##0'),("Install labor $",RL["install"],'"$"#,##0'),("Install man-hours",RL["install_mh"],"#,##0"),("Test and commissioning $",RL["test"],'"$"#,##0'),("Test man-hours",RL["test_mh"],"#,##0"),("Removals $",RL["remove"],'"$"#,##0'),("Station 496 total (incl. loaders)",RL["sta496"],'"$"#,##0'),("Per relay, all-in",RL["per_relay"],'"$"#,##0'),("Man-hours per relay",RL["mh_per_relay"],"0")):
    ws.cell(row=r,column=1,value=lab).font=base; c=ws.cell(row=r,column=2,value=round(v)); c.number_format=fmt; r+=1
r+=1; ws.cell(row=r,column=1,value="Section 48E assumptions").font=bold; r+=1
IT=SV["itc"]
for lab,v,fmt in (("Base rate (prevailing wage and apprenticeship)",IT["rate_base"],"0%"),("Energy-community adder",IT["energy_community_adder"],"0%"),("Eligible basis, low (A+B+C loaded)",IT["basis_lo"],'"$"#,##0'),("Eligible basis, high (A to G loaded)",IT["basis_hi"],'"$"#,##0')):
    ws.cell(row=r,column=1,value=lab).font=base; c=ws.cell(row=r,column=2,value=v); c.font=blue; c.number_format=fmt; r+=1
ws.cell(row=r,column=1,value="Credit, low / high").font=base; c=ws.cell(row=r,column=2,value=f"=B{r-4}*B{r-2}"); c.number_format='"$"#,##0'; c=ws.cell(row=r,column=3,value=f"=B{r-4}*B{r-1}"); c.number_format='"$"#,##0'; r+=1
ws.cell(row=r,column=1,value="Adder, low / high").font=base; c=ws.cell(row=r,column=2,value=f"=B{r-4}*B{r-3}"); c.number_format='"$"#,##0'; c=ws.cell(row=r,column=3,value=f"=B{r-4}*B{r-2}"); c.number_format='"$"#,##0'; r+=1
ws.cell(row=r,column=1,value="Assumptions to be confirmed by Tax: 30% with PWA; storage exempt from the 2027 wind/solar cliff (full credit through a 2033 construction start); interconnection property outside the 48E storage definition; FEOC cost ratio 65% for a 2028 construction start (Notice 2026-15); normalization election under section 50(d)(2); brownfield adder needs a Phase II ESA above 5 MW. Research pass 3 Oct 2026, search-excerpt sourced.").font=note
for col,wd in zip("ABCDEFGHIJKLM",(6,6,52,8,12,12,10,12,12,10,24,48,60)): ws.column_dimensions[col].width=wd
# README rows (dedupe by tab name)
rd=wb["README"]
for tab,desc in (("Layer Escalators","One published index per cost layer (IBEW 103 labor, PPI transformers, PPI switchgear, ENR CCI, PPI engineering services, Handy-Whitman) with Hyde Park and developer weights, the composite 2018-to-2026 factor, and the 55-project class under seven re-basing methods. Deck slides 17-18. Added 3 Oct 2026."),("Savings Register","Fourteen cost-saving levers in three tiers sized from the Rev 3 rows, direct and loaded at the marginal loader, with owner, closing condition and evidence; Station 496 relay detail; Section 48E assumptions. Deck slides 27-29. Added 3 Oct 2026.")):
    rows=[i for i in range(1,rd.max_row+1) if rd.cell(row=i,column=1).value in (tab,f"Tab: {tab}")]
    for i in rows[:-1] if rows else []: rd.delete_rows(i)
    tgt=rows[-1] if rows else rd.max_row+1
    rd.cell(row=tgt,column=1,value=f"Tab: {tab}").font=bold; rd.cell(row=tgt,column=2,value=desc).font=base
wb.calculation=CalcProperties(fullCalcOnLoad=True); wb.save(f"{B}/Hyde_Park_BESS_Cost_Analysis.xlsx"); print("workbook updated", wb.sheetnames)
