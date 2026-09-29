import json, openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.comments import Comment
B="/tmp/claude-0/-home-user-BESS/078f934e-4ca0-5169-be3f-cb66ff0e2514/scratchpad/build"
D=json.load(open(f"{B}/data.json"))
NAVY="001E60"; GOLD="FFC72C"; BURG="6E1F2E"; GRAY="D9D9D9"
hdr_font=Font(name="Arial",bold=True,color="FFFFFF",size=10); hdr_fill=PatternFill("solid",fgColor=NAVY)
sub_fill=PatternFill("solid",fgColor="E8EDF5"); gold_fill=PatternFill("solid",fgColor="FFF3CC")
thin=Side(style="thin",color="BFBFBF"); border=Border(left=thin,right=thin,top=thin,bottom=thin)
base=Font(name="Arial",size=10); bold=Font(name="Arial",size=10,bold=True); blue=Font(name="Arial",size=10,color="0000FF")
title_font=Font(name="Arial",size=14,bold=True,color=NAVY)
wb=openpyxl.Workbook()
def header(ws,row,cols,widths=None):
    for i,c in enumerate(cols,1):
        cell=ws.cell(row=row,column=i,value=c); cell.font=hdr_font; cell.fill=hdr_fill; cell.alignment=Alignment(wrap_text=True,vertical="center"); cell.border=border
    if widths:
        for i,w in enumerate(widths,1): ws.column_dimensions[get_column_letter(i)].width=w
def style_range(ws,r1,r2,c1,c2,font=base,fmt=None):
    for r in range(r1,r2+1):
        for c in range(c1,c2+1):
            cell=ws.cell(row=r,column=c); cell.font=font; cell.border=border
            if fmt and c>=2: cell.number_format=fmt
# ---------------- README ----------------
ws=wb.active; ws.title="README"
ws["A1"]="Hyde Park BESS (Project 21334 / 24211) - Cost Analysis Workbook"; ws["A1"].font=title_font
lines=[
("Purpose","Traceable data source behind the Cost Analysis deck, Basis of Estimate and all-in cost whitepaper. Every number on a slide ties to a cell here."),
("Prepared","Eversource Cost Estimating CoE, 29 Sep 2026. Source of record: ESF - Hyde Park BESS Total Rev 3.xlsm (24 Sep 2026), Item and Overview tabs."),
("Convention","Blue font = input value keyed from a source document (editable). Black = formula. Navy header = section. Gold fill = headline metric."),
("Tab: Layers","Rev 3 line items rolled into 13 cost layers (A-M). Directs are as-estimated; the 'Loaded' column spreads Station 360 risk, contingency, indirects and AFUDC pro rata over direct layers so each layer carries its full share of the approval-level total."),
("Tab: Unit Costs","$/kW and $/kWh at each boundary: vendor contract only, battery system installed, station complete, all-in approval level, and all-in including the D-Line interconnection (24211)."),
("Tab: Timeline","Every funding action, estimate and vendor price point from the 2021 IFR to Rev 3, with basis and in-service date drift."),
("Tab: Sept 2026 Walk","Rev 0 -> Rev 1 -> Rev 2 -> Rev 3 variance walk from the ESF revisions and the 9/1-9/23/2026 email record."),
("Tab: Benchmarks","Published industry benchmarks with metric definition, dollar year and duration. Source quality tier: green = primary, yellow = secondary."),
("Tab: 2023 Indicative","July 2023 five-bidder indicative pricing (Site Two = Hyde Park 10 MW/20 MWh) and what each excluded."),
("Tab: Line Items","All 292 Rev 3 line items with the layer assignment used for the roll-up. Change a layer letter in column K and the Layers tab recalculates."),
("Vintage / escalation","Rev 3 carries $2,948,100 of escalation (ESF Overview). Battery line escalated at 3%/yr to 2027-28 delivery even though the Nomad price is fixed until Final Acceptance; see BOE section 'Escalation'."),
("Accuracy","Rev 3 is classed Conceptual (-25% / +50%) on the ESF. Sta 360 preliminary engineering is in progress (Sep 2026); IFC expected Aug 2027."),
]
for i,(k,v) in enumerate(lines,3):
    ws.cell(row=i,column=1,value=k).font=bold; c=ws.cell(row=i,column=2,value=v); c.font=base; c.alignment=Alignment(wrap_text=True,vertical="top")
ws.column_dimensions["A"].width=22; ws.column_dimensions["B"].width=120
# ---------------- Line Items ----------------
li=wb.create_sheet("Line Items")
header(li,1,["Estimate","CBS1","CBS4","Seq","Description","Qty","Unit","Direct Cost ($)","Manhours","Note","Layer","Layer code"],[28,6,12,6,60,8,6,15,10,50,60,8])
for i,r in enumerate(D["rows"],2):
    vals=[r["est"],r["cbs1"],r["cbs4"],r["seq"],r["desc"],r["qty"],r["unit"],r["cost"],r["mh"],r["note"][:250],r["layer"]]
    for j,v in enumerate(vals,1):
        c=li.cell(row=i,column=j,value=v); c.font=base; c.border=border
    li.cell(row=i,column=8).number_format='#,##0'; li.cell(row=i,column=8).font=blue
    c=li.cell(row=i,column=12,value=f'=LEFT(K{i},1)'); c.font=base; c.border=border
n_last=len(D["rows"])+1
li.cell(row=n_last+1,column=7,value="Total").font=bold
c=li.cell(row=n_last+1,column=8,value=f"=SUM(H2:H{n_last})"); c.font=bold; c.number_format='#,##0'
li.freeze_panes="A2"; li.auto_filter.ref=f"A1:L{n_last}"
# ---------------- Layers ----------------
la=wb.create_sheet("Layers",1)
la["A1"]="Cost layers - ESF Total Rev 3 (24 Sep 2026), Project 21334 (Sta 360 + Sta 496)"; la["A1"].font=title_font
la["A2"]="Directs by layer are SUMIFS over the Line Items tab. Loaded = Station 360 direct layers x load factor (risk + contingency + indirects + AFUDC spread pro rata); Station 496 is carried whole as an interconnection cost."; la["A2"].font=base; la["A2"].alignment=Alignment(wrap_text=True); la.merge_cells("A2:G2"); la.row_dimensions[2].height=30
header(la,4,["Layer","Direct ($)","% of total","Loaded ($)","% of loaded","Cumulative loaded ($)","What it is"],[70,16,10,16,10,18,80])
layers=list(D["layers_direct"].keys())
what={
"A":"Nomad fixed-price supply contract $12,106,850 (12 Voyager 3.0 LFP units, PCS, BMS, fire protection, 10-yr warranty, spares, remote support) as carried in Rev 3: $1,213,043 actual LNTP payments + $11,778,062 to-go (escalated).",
"B":"Owner-scope work that exists only because of the batteries: 5,557 mh installation labor, 12 foundation pads, fire suppression, GSU-to-BESS conduit and 600 V cable.",
"C":"Four 3 MVA 13.8 kV/480 V generator step-up transformers, site EMS/communications, AC/DC auxiliary power panels. Vendors often bundle these in a 'turnkey' quote; here they are owner-furnished.",
"D":"The new 13.8 kV switching station (Sta 360): four Siemens SDV7 1200 A breaker skids with relays/PTs/DC, disconnects, metering transclosures, station service transformer, riser poles, 15 kV cable, duct bank to feeder manholes, ground grid, lighting, control cable.",
"E":"Developing a 200 ft x 200 ft yard on a closed construction-debris landfill: clear and grub, 760 ft access road, 24+12 soil borings, 2,520 CY cut, imported fill, trap rock, 14 ft retaining wall, fence, mob/demob.",
"F":"Station 496 protection upgrades required to accept the BESS on four feeders: 20 SEL relays, transfer trip over dark fiber, RTU/SCADA points, removals. Carried at its full approval level incl. its own indirects/AFUDC/contingency.",
"G":"Lead commissioning engineer, field test engineers, field SCADA and telecom commissioning.",
"H":"Engineering (internal and Leidos/VHB), Article 80 siting and legal, environmental permits (DEP post-closure use, SWPPP, Tier II), community outreach, project management, construction reps, land.",
"I":"Property tax, CWIP, sales and use tax on external material, builders all-risk insurance.",
"J":"Twelve enumerated risk items on Sta 360 (see BOE).",
"K":"General contingency on Sta 360.",
"L":"Corporate indirects: E&S station overhead, general services, non-productive time, payroll benefits, AS&E, MDEC, vehicles, lobby stock.",
"M":"Allowance for funds used during construction, Sta 360.",
}
r=5
for L in layers:
    la.cell(row=r,column=1,value=L).font=base
    la.cell(row=r,column=2,value=f"=SUMIFS('Line Items'!$H:$H,'Line Items'!$L:$L,\"{L[0]}\")").number_format='#,##0'
    la.cell(row=r,column=3,value=f"=B{r}/$B$18").number_format='0.0%'
    if L[0] in "ABCDEGHI":
        la.cell(row=r,column=4,value=f"=B{r}*$B$21").number_format='#,##0'
    elif L[0]=="F":
        la.cell(row=r,column=4,value=f"=B{r}").number_format='#,##0'
    else:
        la.cell(row=r,column=4,value=0).number_format='#,##0'
    la.cell(row=r,column=5,value=f"=D{r}/$D$18").number_format='0.0%'
    la.cell(row=r,column=6,value=f"=SUM($D$5:D{r})").number_format='#,##0'
    la.cell(row=r,column=7,value=what[L[0]]).alignment=Alignment(wrap_text=True,vertical="top")
    r+=1
# r now 18
la.cell(row=18,column=1,value="Total - Project 21334 approval level").font=bold
la.cell(row=18,column=2,value="=SUM(B5:B17)").number_format='#,##0'; la.cell(row=18,column=2).font=bold
la.cell(row=18,column=4,value="=SUM(D5:D17)").number_format='#,##0'; la.cell(row=18,column=4).font=bold
la.cell(row=18,column=3,value="=SUM(C5:C17)").number_format='0.0%'; la.cell(row=18,column=5,value="=SUM(E5:E17)").number_format='0.0%'
la.cell(row=20,column=1,value="Station 360 direct layers A-E, G-I (sum)").font=base
la.cell(row=20,column=2,value="=SUMPRODUCT(--(LEFT(A5:A17,1)<>\"F\"),--(LEFT(A5:A17,1)<>\"J\"),--(LEFT(A5:A17,1)<>\"K\"),--(LEFT(A5:A17,1)<>\"L\"),--(LEFT(A5:A17,1)<>\"M\"),B5:B17)").number_format='#,##0'
la.cell(row=21,column=1,value="Load factor = (Sta 360 directs + J+K+L+M) / Sta 360 directs").font=base
la.cell(row=21,column=2,value="=(B20+B14+B15+B16+B17)/B20").number_format='0.0000'
la.cell(row=22,column=1,value="Check: loaded total less direct total (should be 0)").font=base
la.cell(row=22,column=2,value="=D18-B18").number_format='#,##0'
la.cell(row=24,column=1,value="Memo: D-Line interconnection, project 24211 (SSF Feb 2024 conceptual, not re-estimated)").font=base
la.cell(row=24,column=2,value=D["dline_conceptual"]).number_format='#,##0'; la.cell(row=24,column=2).font=blue
la.cell(row=24,column=2).comment=Comment("Solution Selection Form, approved SDC 2/15/2024: 'Conceptual (-25%/+50%) Distribution Scope Cost Estimate: $4.793 million'. Partial funding of $2,085K approved MPAC 8/5/2024. Scope: 5,465 ft circuit extension, 3 manholes, 1,270 ft 6-5in duct bank, 16,395 ft 3-700 cable.","CoE")
la.cell(row=25,column=1,value="Memo: Nomad contract fixed price (Exhibit C, cover agreement dated 3/10/2026)").font=base
la.cell(row=25,column=2,value=D["nomad_contract"]).number_format='#,##0'; la.cell(row=25,column=2).font=blue
la.cell(row=26,column=1,value="Memo: escalation carried on the fixed-price battery line (Rev 3 line 432 less contract balance)").font=base
la.cell(row=26,column=2,value="=11778061.83-(11860850-1213042.82)").number_format='#,##0'
la.cell(row=26,column=2).comment=Comment("Rev 3 note on seq 432: 'cover agreement dated 12/6/25 = $11,860,850 minus actual cost and downpayment $1,213,042.82, total = $10,647,808'. Line carries $11,778,062, i.e. 10.6% escalation on a price that Exhibit C fixes until Final Acceptance. The $246,000 labor portion of the SOV is not visible on a separate line.","CoE")
style_range(la,5,17,1,7)
for rr in range(5,18):
    for cc in (2,4,6): la.cell(row=rr,column=cc).number_format='#,##0'
    for cc in (3,5): la.cell(row=rr,column=cc).number_format='0.0%'
for rr in range(5,18): la.row_dimensions[rr].height=48
la.freeze_panes="A5"
# ---------------- Unit Costs ----------------
uc=wb.create_sheet("Unit Costs",2)
uc["A1"]="Unit costs at each cost boundary (10 MW / 20 MWh, 2-hour)"; uc["A1"].font=title_font
uc["A3"]="Nameplate MW"; uc["B3"]=D["mw"]; uc["A4"]="Nameplate MWh"; uc["B4"]=D["mwh"]; uc["B3"].font=blue; uc["B4"].font=blue
header(uc,6,["Boundary","Total ($)","$/kW","$/kWh","Multiple of vendor contract","Definition"],[58,16,12,12,14,90])
bounds=[
("1. Vendor contract as quoted (Nomad fixed price)","='Layers'!B25","What the vendor calls 'the project cost': containers, batteries, PCS, BMS, fire protection, spares, 7-yr warranty extension, remote support, shipping, supervision, commissioning, training."),
("2. Battery supply as carried in Rev 3 (contract + actuals + escalation) - Layer A","='Layers'!B5","Rev 3 line 432 + line 445."),
("3. Battery system installed (Layers A+B+C, direct)","=SUM('Layers'!B5:B7)","Adds owner installation labor, pads, fire suppression, GSUs, EMS/comms, aux power. Closest analogue to a 'turnkey BESS' benchmark before soft costs."),
("4. Station complete, direct (Layers A-E + G-I, no loaders)","='Layers'!B20","Adds the 13.8 kV switching station, landfill site development, testing, owner soft costs and taxes."),
("5. Station 360 approval level (loaded)","=SUM('Layers'!D5:D9)+SUM('Layers'!D11:D13)","Adds risk, contingency, indirects and AFUDC. Equals ESF 'Hyde Park BESS - Sta. 360 - Rev 3' $49,994,200."),
("6. Project 21334 approval level (Sta 360 + Sta 496)","='Layers'!D18","Adds the Station 496 feeder protection upgrades. Equals ESF Total Rev 3 $57,247,300."),
("7. All-in including D-Line interconnection 24211 (memo)","='Layers'!D18+'Layers'!B24","Adds the 2024 conceptual distribution circuit extension estimate. Not yet re-estimated; treat as indicative."),
]
for i,(a,b,c) in enumerate(bounds,7):
    uc.cell(row=i,column=1,value=a); uc.cell(row=i,column=2,value=b).number_format='#,##0'
    uc.cell(row=i,column=3,value=f"=B{i}/($B$3*1000)").number_format='#,##0'
    uc.cell(row=i,column=4,value=f"=B{i}/($B$4*1000)").number_format='#,##0'
    uc.cell(row=i,column=5,value=f"=B{i}/$B$7").number_format='0.00"x"'
    uc.cell(row=i,column=6,value=c).alignment=Alignment(wrap_text=True,vertical="top")
style_range(uc,7,13,1,6)
for rr in range(7,14):
    uc.row_dimensions[rr].height=42
    uc.cell(row=rr,column=2).number_format='#,##0'; uc.cell(row=rr,column=3).number_format='#,##0'; uc.cell(row=rr,column=4).number_format='#,##0'; uc.cell(row=rr,column=5).number_format='0.00"x"'
for cc in range(1,7): uc.cell(row=7,column=cc).fill=gold_fill; uc.cell(row=12,column=cc).fill=gold_fill
uc["A15"]="Battery supply contract as share of project 21334 approval level"; uc["B15"]="=B7/B12"; uc["B15"].number_format='0.0%'
uc["A16"]="Everything that is not the battery contract ($)"; uc["B16"]="=B12-B7"; uc["B16"].number_format='#,##0'
uc["A17"]="Interconnection-driven cost, loaded: Layer D + Layer F ($)"; uc["B17"]="='Layers'!D8+'Layers'!D10"; uc["B17"].number_format='#,##0'
uc["A18"]="Interconnection-driven cost incl. D-Line memo ($)"; uc["B18"]="=B17+'Layers'!B24"; uc["B18"].number_format='#,##0'
for rr in range(15,19): uc.cell(row=rr,column=1).font=bold
# ---------------- Timeline ----------------
tl=wb.create_sheet("Timeline",3)
tl["A1"]="Cost and funding history, 2021 - 2026"; tl["A1"].font=title_font
header(tl,3,["Date","Event","Value ($)","Type","Basis / source","$/kWh at 20 MWh"],[12,52,16,10,90,14])
for i,t in enumerate(D["timeline"],4):
    tl.cell(row=i,column=1,value=t["date"]); tl.cell(row=i,column=2,value=t["label"]); c=tl.cell(row=i,column=3,value=t["value"]); c.number_format='#,##0'; c.font=blue
    tl.cell(row=i,column=4,value=t["kind"]); tl.cell(row=i,column=5,value=t["basis"]).alignment=Alignment(wrap_text=True)
    tl.cell(row=i,column=6,value=f"=C{i}/('Unit Costs'!$B$4*1000)").number_format='#,##0'
style_range(tl,4,3+len(D["timeline"]),1,6)
for rr in range(4,4+len(D["timeline"])): tl.cell(row=rr,column=3).number_format='#,##0'; tl.cell(row=rr,column=6).number_format='#,##0'; tl.row_dimensions[rr].height=30
r0=5+len(D["timeline"])
tl.cell(row=r0,column=1,value="In-service date drift").font=bold
header(tl,r0+1,["As of","Planned ISD"])
for i,(a,b) in enumerate(D["isd_history"],r0+2):
    tl.cell(row=i,column=1,value=a).font=base; tl.cell(row=i,column=2,value=b).font=base
# ---------------- Sept 2026 Walk ----------------
wk=wb.create_sheet("Sept 2026 Walk",4)
wk["A1"]="September 2026 estimate revision walk (Project 21334 approval level)"; wk["A1"].font=title_font
header(wk,3,["Step","Date","Approval level ($)","Change ($)","Driver (from ESF clarifications and 9/1-9/23/2026 email record)"],[26,12,18,16,110])
walk=[
("Rev 0","2026-08-26",47201100,"Sta 360 built up from E-23-373 quantities and 7/28/2023 indicative pricing; battery material carried at about $6M (PM: 'change the battery cost (line 71) from 6 to 12.1M')."),
("Rev 1","2026-09-01",51867100,"Per project team, increase battery material cost."),
("Rev 2","2026-09-10",63640300,"Battery line reset to Nomad cover agreement and escalated to $13,119,867; $1,545,014 'Relays, P&C systems for batteries' carried from 2023 Company 1 pricing; 3 SSVTs; engineering hours from E-23-373; $609K LNTP actuals shown separately."),
("Rev 3","2026-09-24",57247300,"Relays deleted (-$1.5M, duplicated in $300K/breaker Siemens price per P&C Engineering 9/22); SSVT quantity 3 to 1; engineering re-based to $501K to-go plus actuals (9/18); actuals updated to 9/23 ($5.52M); battery line = contract less $1,213,043 paid, escalated."),
]
for i,(a,b,c,d) in enumerate(walk,4):
    wk.cell(row=i,column=1,value=a); wk.cell(row=i,column=2,value=b); cc=wk.cell(row=i,column=3,value=c); cc.number_format='#,##0'; cc.font=blue
    wk.cell(row=i,column=4,value=(f"=C{i}-C{i-1}" if i>4 else 0)).number_format='#,##0'
    wk.cell(row=i,column=5,value=d).alignment=Alignment(wrap_text=True,vertical="top"); wk.row_dimensions[i].height=60
style_range(wk,4,7,1,5)
for rr in range(4,8): wk.cell(row=rr,column=3).number_format='#,##0'; wk.cell(row=rr,column=4).number_format='#,##0'
wk["A9"]="Reference: full-funding placeholder carried in PF Rev 2 and Rev 3 PAFs"; wk["C9"]=43926100; wk["C9"].number_format='#,##0'; wk["C9"].font=blue
wk["A10"]="Rev 3 vs. full-funding placeholder"; wk["C10"]="=C7-C9"; wk["C10"].number_format='#,##0'; wk["D10"]="=C10/C9"; wk["D10"].number_format='0.0%'
# ---------------- 2023 Indicative ----------------
ind=wb.create_sheet("2023 Indicative",5)
ind["A1"]="July 28, 2023 indicative pricing - Site Two (Hyde Park, 10 MW / 20 MWh), five bidders"; ind["A1"].font=title_font
header(ind,3,["Bidder","Total indicative price ($)","$/kWh","Notes on scope / exclusions"],[24,20,10,110])
notes={"Company 1":"8 Hithium containers, 4 SMA 3950 PCS skids, switchgear $707K; excludes sound mitigation; prevailing wage and IRA compliance; 5-yr warranty; interconnection by Eversource.",
"Company 2 (Opt 1)":"Assumes connection to substation bus (no switchgear); augmentation required year 7; no LTSA/extended warranty; 'Eversource would be responsible for interconnection cost'.",
"Company 2 (Opt 2)":"As Option 1 with lower-cost enclosure option.",
"Company 3":"Basis of the E-23-373 estimate. Battery enclosure $10.58M, PCS $0.83M, step-up transformers $0.63M, sound mitigation $0.47M, turnkey civil/installation $4.56M, spares/transport $0.59M.",
"Company 4":"'Complete scope' line items; no step-up transformer; no builders risk; local permits only; no below-grade risk; non-union labor.",
"Company 5":"Highest engineering/PM line ($3.15M) and installation $2.05M."}
for i,(k,v) in enumerate(D["indicative_2023"].items(),4):
    ind.cell(row=i,column=1,value=k); c=ind.cell(row=i,column=2,value=v); c.number_format='#,##0'; c.font=blue
    ind.cell(row=i,column=3,value=f"=B{i}/('Unit Costs'!$B$4*1000)").number_format='#,##0'
    ind.cell(row=i,column=4,value=notes[k]).alignment=Alignment(wrap_text=True,vertical="top"); ind.row_dimensions[i].height=45
style_range(ind,4,9,1,4)
for rr in range(4,10): ind.cell(row=rr,column=2).number_format='#,##0'; ind.cell(row=rr,column=3).number_format='#,##0'
ind["A11"]="Low"; ind["B11"]="=MIN(B4:B9)"; ind["A12"]="High"; ind["B12"]="=MAX(B4:B9)"; ind["A13"]="Median"; ind["B13"]="=MEDIAN(B4:B9)"
for rr in (11,12,13): ind.cell(row=rr,column=2).number_format='#,##0'; ind.cell(row=rr,column=1).font=bold
ind["A15"]="Every bidder listed interconnection, permitting beyond local, below-grade risk, sound walls, spares or long-term service as excluded or 'Eversource responsibility'. Source: BESS_Indicative_Pricing.xlsx (attachment to 9/9/2026 email)."; ind["A15"].font=base
# ---------------- Benchmarks placeholder (filled by build_benchmarks) ----------------
bm=wb.create_sheet("Benchmarks",6)
bm["A1"]="Published industry benchmarks (filled from research log; see whitepaper references)"; bm["A1"].font=title_font
header(bm,3,["Source","Year","Metric","Value","Units","Duration","Dollar year","What is included","Confidence","URL"],[34,8,40,12,10,10,10,60,11,60])
wb.save(f"{B}/Hyde_Park_BESS_Cost_Analysis.xlsx"); print("saved")

# ---------------- fill Benchmarks tab + calc on load ----------------
import json as _json
BM=_json.load(open(f"{B}/benchmarks.json"))
wb=openpyxl.load_workbook(f"{B}/Hyde_Park_BESS_Cost_Analysis.xlsx")
bm=wb["Benchmarks"]
tier={"High":"C6EFCE","Medium":"FFEB9C","Low":"F8CBAD"}
for i,r in enumerate(BM["rows"],4):
    vals=[r["source"],r["year"],r["metric"],r["value"],r["units"],r["duration"],r["dollar_year"],r["scope"],r["confidence"],r["url"]]
    for j,v in enumerate(vals,1):
        c=bm.cell(row=i,column=j,value=v); c.font=base; c.border=border; c.alignment=Alignment(wrap_text=True,vertical="top")
    bm.cell(row=i,column=4).font=blue; bm.cell(row=i,column=4).number_format='#,##0'
    bm.cell(row=i,column=9).fill=PatternFill("solid",fgColor=tier.get(r["confidence"],"FFFFFF"))
    bm.row_dimensions[i].height=60
n=4+len(BM["rows"])
bm.cell(row=n+1,column=1,value="Hyde Park boundaries for comparison ($/kWh, from Unit Costs tab)").font=bold
hp=[("Nomad equipment only (12 units, PCS, BMS, fire)","=10638000/('Unit Costs'!$B$4*1000)"),("Vendor contract","='Unit Costs'!D7"),("Battery installed (A+B+C)","='Unit Costs'!D9"),("Station complete, direct","='Unit Costs'!D10"),("Station 360 approval level","='Unit Costs'!D11"),("Project 21334 approval level","='Unit Costs'!D12"),("All-in incl. D-Line memo","='Unit Costs'!D13")]
for i,(a,fml) in enumerate(hp,n+2):
    bm.cell(row=i,column=1,value=a).font=base; c=bm.cell(row=i,column=4,value=fml); c.number_format='#,##0'; c.font=base; bm.cell(row=i,column=5,value="$/kWh").font=base
bm.cell(row=n+10,column=1,value=BM["access_caveat"]).font=Font(name="Arial",size=9,italic=True)
bm.merge_cells(start_row=n+10,start_column=1,end_row=n+10,end_column=8); bm.cell(row=n+10,column=1).alignment=Alignment(wrap_text=True); bm.row_dimensions[n+10].height=40
from openpyxl.workbook.properties import CalcProperties
wb.calculation=CalcProperties(fullCalcOnLoad=True)
wb.save(f"{B}/Hyde_Park_BESS_Cost_Analysis.xlsx"); print("benchmarks tab filled, fullCalcOnLoad set")
