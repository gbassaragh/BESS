import sys, json, os
sys.path.insert(0,"/tmp/claude-0/-home-user-BESS/078f934e-4ca0-5169-be3f-cb66ff0e2514/scratchpad/build")
from pptx_common import *
B="/tmp/claude-0/-home-user-BESS/078f934e-4ca0-5169-be3f-cb66ff0e2514/scratchpad/build"
D=json.load(open(f"{B}/data.json")); L=D["layers_direct"]; LD=D["layers_loaded"]
BM=json.load(open(f"{B}/benchmarks.json")) if os.path.exists(f"{B}/benchmarks.json") else None
A=L["A. Battery supply contract (Nomad)"]; Bv=L["B. Battery installation & integration (owner scope)"]; C=L["C. Battery balance-of-plant (GSUs, EMS/comms, aux power)"]
Dv=L["D. Station 360 13.8 kV switching & interconnection facilities"]; E=L["E. Site development & civil (former landfill site)"]; F=L["F. Station 496 feeder protection upgrades (interconnection)"]
G=L["G. Testing & commissioning"]; Hh=L["H. Owner soft costs (engineering, siting, environmental, outreach, PM, land)"]; I=L["I. Taxes, CWIP, builders-risk insurance"]
J=L["J. Risk register"]; K=L["K. Contingency"]; Ll=L["L. Indirects / overheads"]; M=L["M. AFUDC"]
TOT=57247300; NOMAD=12106850; DLINE=4793000
def mm(v): return f"${v/1e6:.1f}M"
p=prs(); n=0
# ---------------- 1 Title ----------------
s=blank(p); n+=1; rect(s,0,0,W,H,NAVY)
text(s,0.8,2.0,11.5,1.6,"A $12 million battery. A $57 million project.",size=44,bold=True,color=WHITE,font=HEAD)
text(s,0.8,3.55,11.5,1.2,"Hyde Park BESS (Project 21334): where the cost of a utility-owned, distribution-connected battery storage station actually sits, and how it compares to industry benchmarks",size=20,color=MID)
text(s,0.8,5.5,11.5,0.45,"Cost Estimating Center of Excellence  |  Estimate basis: ESF Total Rev 3, 24 Sep 2026  |  29 Sep 2026",size=14,color=GOLD)
text(s,0.8,6.05,11.5,0.4,"Internal. Contains vendor-confidential pricing.",size=12,color=MID)
notes(s,"Open on the promise, not a joke. The one sentence the audience should be able to repeat afterwards: the battery is 21 percent of the project, and the other 79 percent is what it takes to put a battery on a landfill in Boston and connect it to four feeders safely.")
# ---------------- 2 Promise + three numbers ----------------
s=blank(p); n+=1; chrome(s,"By the end of this deck you can answer one question in one breath",eyebrow="The promise",n=n)
text(s,0.6,1.55,12,0.7,"“Why is a $12 million battery a $57 million project?”  Because the battery is the only part a vendor prices. The station, the site, the feeder protection, the siting case, the risk and the cost of money are ours.",size=19,color=INK)
stat(s,0.6,2.7,3.9,2.4,"$12.1M","Vendor fixed-price contract","Nomad cover agreement, 10 Mar 2026. 12 Voyager LFP units, PCS, BMS, fire protection, 10-yr warranty. $605/kWh, $1,211/kW.")
stat(s,4.72,2.7,3.9,2.4,"$57.2M","Project 21334 approval level","ESF Total Rev 3. Station 360 $50.0M plus Station 496 protection $7.3M. $2,862/kWh, $5,725/kW. Conceptual, -25%/+50%.",vcolor=BURG)
stat(s,8.84,2.7,3.9,2.4,"21%","Battery share of the total","Add the D-Line circuit extension (24211, $4.8M conceptual) and the share drops to 20%. Four dollars of every five are not the battery.")
text(s,0.6,5.4,12.1,1.4,[[("What this deck contributes: ",{"bold":True,"color":NAVY}),("a line-by-line extraction of the Rev 3 estimate into thirteen cost layers, unit costs at every boundary a benchmark could be quoted at, the cost history from the 2021 IFR to today, and the reconciliations that must close before full funding.",{})]],size=16)
notes(s,"Three numbers. Vendor contract, approval level, share. Everything after this slide is proof.")
# ---------------- 3 What the vendor prices vs what we build ----------------
s=blank(p); n+=1; chrome(s,"What a vendor quote contains, and what it leaves for the utility",eyebrow="Two framings of the same project",n=n)
rect(s,0.6,1.55,5.9,5.2,LIGHT); rect(s,6.85,1.55,5.9,5.2,LIGHT)
text(s,0.8,1.65,5.5,0.45,"Inside the $12.1M Nomad price",size=17,bold=True,color=NAVY,font=HEAD)
bullets(s,0.8,2.2,5.6,4.5,["12 containerized LFP units, 10 MW / 20 MWh, 12 MVA","Inverters (PCS), BMS, HVAC, fire detection and suppression inside the container","Spares $125K, shipping $90K, remote support $210K","10-year warranty; years 3-7 extension $798K","Field assembly supervision, commissioning, training: $246K","Fixed until Final Acceptance; LDs capped at 10%"],size=15,gap=5)
text(s,7.05,1.65,5.5,0.45,"Outside it: $45.1M, 79% of the project",size=17,bold=True,color=BURG,font=HEAD)
bullets(s,7.05,2.2,5.6,4.5,[("Station 360, ",f"{mm(Dv)} direct: four 15 kV breaker skids, GSUs, SSVT, metering, cable, duct bank, ground grid"),("Site, ",f"{mm(E)} direct: a 200 ft x 200 ft platform on a closed landfill, access road, retaining wall"),("Station 496, ",f"{mm(F)}: 20 relays, transfer trip, RTU work so four feeders can accept 2.5 MW each"),("Owner scope, ",f"{mm(Bv+C+G+Hh+I)}: install labor, GSUs, EMS, testing, engineering, Article 80 siting, outreach, PM, taxes"),("Station 360 risk, contingency, indirects, AFUDC, ",f"{mm(J+K+Ll+M)}: 35% of the total (Station 496 carries its own inside its $7.3M)")],size=15,gap=5)
notes(s,"The vendor is not wrong. Their number is a real number for what they sell. It is simply not the project.")
# ---------------- 4 Layer build-up chart ----------------
s=blank(p); n+=1; chrome(s,"Thirteen layers between the battery contract and the approval level",eyebrow="Cost layer extraction, ESF Total Rev 3 (directs, $M)",n=n)
cats=["A Battery contract","B Battery install","C Battery BOP (GSU, EMS)","D Sta 360 switching","E Site & civil","F Sta 496 protection","G Testing","H Owner soft costs","I Taxes, CWIP, BAR","J Risk","K Contingency","L Indirects","M AFUDC"]
vals=[A,Bv,C,Dv,E,F,G,Hh,I,J,K,Ll,M]
cum=[]; run=0
base=[]; 
for v in vals: base.append(run); run+=v
cd=CategoryChartData(); cd.categories=[f"{c}\n${v/1e6:.1f}M" for c,v in zip(cats,vals)]
cd.add_series("base",[round(b/1e6,2) for b in base]); cd.add_series("Layer",[round(v/1e6,2) for v in vals])
gf=s.shapes.add_chart(XL_CHART_TYPE.COLUMN_STACKED,Inches(0.5),Inches(1.5),Inches(12.3),Inches(5.3),cd); ch=gf.chart
style_chart(ch,legend=False,size=11)
ch.plots[0].gap_width=40
sb=ch.series[0]; sb.format.fill.background(); sb.format.line.fill.background()
sl=ch.series[1]; sl.format.fill.solid(); sl.format.fill.fore_color.rgb=NAVY
for i,pt in enumerate(sl.points):
    pt.format.fill.solid(); pt.format.fill.fore_color.rgb = GOLD if i==0 else (TEAL if i in (3,4,5) else (BURG if i>=9 else NAVY))
va=ch.value_axis; va.has_major_gridlines=True; va.major_gridlines.format.line.color.rgb=MID; va.tick_labels.font.size=Pt(10); va.tick_labels.number_format='"$"0"M"'; va.tick_labels.number_format_is_linked=False; va.maximum_scale=60; va.format.line.fill.background()
ca=ch.category_axis; ca.tick_labels.font.size=Pt(9); ca.format.line.color.rgb=MID
text(s,0.6,6.65,12,0.35,"Gold = battery contract as carried in Rev 3 ($12.1M contract plus $1.1M escalation on the unpaid balance; see slide 12). Teal = station, site and feeder protection. Burgundy = risk, contingency, indirects, AFUDC. Total $57.2M.",size=11,color=GRAY)
notes(s,"Read left to right. The battery contract is the first bar. Everything to its right is the utility's project.")
# ---------------- 5 Layer table ----------------
s=blank(p); n+=1; chrome(s,"Where the $57.2M sits when risk, contingency, indirects and AFUDC are spread",eyebrow="Loaded view: every layer carries its share of the loaders (factor 1.685 on Station 360 directs)",n=n)
rows=[]
for kk in sorted(LD.keys()):
    rows.append([kk[3:], f"${L[kk]/1e6:,.1f}M", f"${LD[kk]/1e6:,.1f}M", f"{LD[kk]/TOT:.0%}"])
rows.append(["Total, project 21334 (directs incl. $20.3M of loaders J-M)", "$57.2M", "$57.2M", "100%"])
table(s,0.6,1.55,12.1,4.8,["Layer","Direct","Loaded","Share"],rows,col_w=[7.3,2.0,1.6,1.2],size=13,bold_last=True,align_right=(1,2,3))
text(s,0.6,6.45,12.1,0.5,"Battery-related layers A+B+C loaded: "+f"${(LD['A. Battery supply contract (Nomad)']+LD['B. Battery installation & integration (owner scope)']+LD['C. Battery balance-of-plant (GSUs, EMS/comms, aux power)'])/1e6:.1f}M ({(LD['A. Battery supply contract (Nomad)']+LD['B. Battery installation & integration (owner scope)']+LD['C. Battery balance-of-plant (GSUs, EMS/comms, aux power)'])/TOT:.0%}). "+f"Station, site and feeder interconnection D+E+F loaded: ${(LD['D. Station 360 13.8 kV switching & interconnection facilities']+LD['E. Site development & civil (former landfill site)']+F)/1e6:.1f}M ({(LD['D. Station 360 13.8 kV switching & interconnection facilities']+LD['E. Site development & civil (former landfill site)']+F)/TOT:.0%}). Owner soft costs, testing and taxes: ${(LD['G. Testing & commissioning']+LD['H. Owner soft costs (engineering, siting, environmental, outreach, PM, land)']+LD['I. Taxes, CWIP, builders-risk insurance'])/1e6:.1f}M.",size=13,color=INK)
notes(s,"The loaded view is the honest comparison basis. When someone quotes an all-in industry $/kWh, it already carries developer overhead and financing; ours carries indirects and AFUDC.")
# ---------------- 6 Unit cost ladder ----------------
s=blank(p); n+=1; chrome(s,"The same project is $605/kWh or $2,862/kWh depending on where you draw the line",eyebrow="Unit cost at each boundary, 20 MWh / 10 MW",n=n)
lad=[("Vendor contract",NOMAD),("Battery as carried (contract + escalation)",A),("Battery installed (A+B+C)",A+Bv+C),("Station complete, direct (no loaders)",A+Bv+C+Dv+E+G+Hh+I),("Station 360 approval level",49994200),("Project 21334 (Sta 360 + 496)",TOT),("All-in incl. D-Line memo",TOT+DLINE)]
cd=CategoryChartData(); cd.categories=[l for l,_ in lad]; cd.add_series("$/kWh",[round(v/20000) for _,v in lad])
gf=s.shapes.add_chart(XL_CHART_TYPE.BAR_CLUSTERED,Inches(0.5),Inches(1.5),Inches(7.6),Inches(5.3),cd); ch=gf.chart; style_chart(ch,legend=False,size=11)
sr=ch.series[0]; sr.format.fill.solid(); sr.format.fill.fore_color.rgb=NAVY
for i,pt in enumerate(sr.points):
    pt.format.fill.solid(); pt.format.fill.fore_color.rgb = GOLD if i==0 else (BURG if i>=5 else NAVY)
sr.data_labels.show_value=True; sr.data_labels.number_format='"$"#,##0'; sr.data_labels.number_format_is_linked=False; sr.data_labels.position=XL_LABEL_POSITION.OUTSIDE_END; sr.data_labels.font.size=Pt(11); sr.data_labels.font.bold=True
ch.plots[0].gap_width=45; ch.category_axis.reverse_order=True; ch.category_axis.tick_labels.font.size=Pt(11); ch.value_axis.visible=False; ch.value_axis.has_major_gridlines=False; ch.category_axis.format.line.color.rgb=MID; ch.value_axis.maximum_scale=3900
table(s,8.35,1.55,4.4,3.6,["Boundary","$/kW","$/kWh","x"],[[ "Vendor contract","$1,211","$605","1.0x"],["Battery installed","$1,666","$833","1.4x"],["Sta 360 approval","$4,999","$2,500","4.1x"],["Project 21334","$5,725","$2,862","4.7x"],["Incl. D-Line","$6,204","$3,102","5.1x"]],col_w=[1.7,0.9,0.9,0.9],size=12,align_right=(1,2,3))
text(s,8.35,5.3,4.4,1.5,"A benchmark is only meaningful against the row that matches its definition. Pack and DC-block prices belong beside the top bar; NREL and EIA installed costs beside 'battery installed' or 'station complete'; nothing published includes a utility's own indirects and AFUDC.",size=12.5,color=GRAY)
notes(s,"This is the slide that ends the argument. The multiple between the vendor line and the approval level is 4.7x, and each step between them is a named scope.")
# ---------------- 7 Benchmarks ----------------
s=blank(p); n+=1; chrome(s,"The battery is at market; the project is above it, for reasons the benchmarks exclude",eyebrow="Industry benchmarks vs Hyde Park boundaries ($/kWh, nominal)",n=n)
if BM and BM.get("chart_rows"):
    cats=[r["label"] for r in BM["chart_rows"]]; vals=[r["value"] for r in BM["chart_rows"]]
    cd=CategoryChartData(); cd.categories=cats; cd.add_series("$/kWh",vals)
    gf=s.shapes.add_chart(XL_CHART_TYPE.BAR_CLUSTERED,Inches(0.5),Inches(1.5),Inches(7.4),Inches(5.4),cd); ch=gf.chart; style_chart(ch,legend=False,size=10)
    sr=ch.series[0]
    for i,pt in enumerate(sr.points):
        pt.format.fill.solid(); pt.format.fill.fore_color.rgb = {"hp":GOLD,"hpall":BURG}.get(BM["chart_rows"][i].get("kind"),NAVY)
    sr.data_labels.show_value=True; sr.data_labels.number_format='"$"#,##0'; sr.data_labels.number_format_is_linked=False; sr.data_labels.position=XL_LABEL_POSITION.OUTSIDE_END; sr.data_labels.font.size=Pt(10)
    ch.plots[0].gap_width=40; ch.category_axis.reverse_order=True; ch.category_axis.tick_labels.font.size=Pt(10); ch.value_axis.visible=False; ch.value_axis.has_major_gridlines=False; ch.category_axis.format.line.color.rgb=MID; ch.value_axis.maximum_scale=max(vals)*1.25
    bullets(s,8.1,1.55,4.7,5.3,BM["takeaways"],size=13,gap=6)
else:
    text(s,0.6,1.6,12,1,"[benchmark data pending]",size=18,color=GRAY)
notes(s,BM["notes"] if BM else "")
# ---------------- 8 What doesn't scale ----------------
s=blank(p); n+=1; chrome(s,"Six things about Hyde Park that a 100 MW greenfield benchmark never has to pay for",eyebrow="Why a small urban utility-owned project sits above the index",n=n)
items=[("Size. ","10 MW / 20 MWh. A switching station, a siting case and a commissioning team cost about the same at 10 MW as at 100 MW; per kWh they are ten times heavier."),
("Duration. ","Two hours. Fixed $/kW items (PCS, breakers, GSUs, interconnection) are spread over half the MWh of a four-hour benchmark."),
("Site. ","A closed construction-debris landfill in Boston: DEP post-closure use permit, cap protection, 36 borings, imported platform fill, 14 ft retaining wall, unknown obstructions ($450K risk)."),
("Interconnection. ","Four feeder tie-ins at 13.8 kV, each with its own breaker skid, plus relay replacement and transfer trip at Station 496 ($7.3M) and a 5,465 ft circuit extension (24211)."),
("Siting and outreach. ","Article 80 Small Project Review, Zoning Board of Appeal, outside counsel, an EJ community, a neighborhood concerned about open land and views: $1.5M plus $0.5M in the risk register."),
("Utility accounting. ","Corporate indirects ($10.0M) and AFUDC over a seven-year development window ($5.0M) are real costs to customers that a developer's turnkey price never shows.")]
for i,(h,b) in enumerate(items):
    col=i%2; row=i//2; x=0.6+col*6.2; y=1.55+row*1.72
    rect(s,x,y,5.95,1.6,LIGHT); rect(s,x,y,0.09,1.6,GOLD)
    text(s,x+0.25,y+0.1,5.6,1.45,[[(h,{"bold":True,"color":NAVY,"size":15}),(b,{"size":13.5})]],size=13.5)
notes(s,"None of these six is optional and none of them is the battery.")
# ---------------- 9 Cost over time ----------------
s=blank(p); n+=1; chrome(s,"Five years, five in-service dates, and an estimate that moved from $44M to $57M",eyebrow="Cost history, 2021 to 2026 (approval-level estimates and vendor price points)",n=n)
tl=[("Jun 2021\nIFR","",0.2),("Jul 2023\nVendor indicative\n(Company 3, turnkey)","v",18.2),("Dec 2023\nE-23-373\nconceptual","e",43.9),("Feb 2024\nSSF incl.\nD-Line","e",49.2),("Mar 2026\nNomad\ncontract","v",12.1),("Aug 2026\nRev 0","e",47.2),("Sep 2026\nRev 2","e",63.6),("Sep 2026\nRev 3","e",57.2)]
cd=CategoryChartData(); cd.categories=[t[0] for t in tl]; cd.add_series("$M",[t[2] for t in tl])
gf=s.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED,Inches(0.5),Inches(1.5),Inches(8.3),Inches(5.3),cd); ch=gf.chart; style_chart(ch,legend=False,size=10)
sr=ch.series[0]
for i,pt in enumerate(sr.points):
    pt.format.fill.solid(); pt.format.fill.fore_color.rgb = GOLD if tl[i][1]=="v" else (NAVY if tl[i][1]=="e" else MID)
sr.data_labels.show_value=True; sr.data_labels.number_format='"$"0.0"M"'; sr.data_labels.number_format_is_linked=False; sr.data_labels.position=XL_LABEL_POSITION.OUTSIDE_END; sr.data_labels.font.size=Pt(10); sr.data_labels.font.bold=True
ch.plots[0].gap_width=50; ch.category_axis.tick_labels.font.size=Pt(9); ch.value_axis.visible=False; ch.value_axis.has_major_gridlines=False; ch.category_axis.format.line.color.rgb=MID; ch.value_axis.maximum_scale=72
text(s,9.0,1.55,3.8,0.4,"In-service date drift",size=15,bold=True,color=NAVY,font=HEAD)
table(s,9.0,1.95,3.8,2.3,["As of","Planned ISD"],[["Jun 2021","Q3 2025"],["Dec 2023","Apr 2027"],["Feb 2024","Sep 2027"],["Jan 2026","Aug 2028"],["Jun 2026","Dec 2028"]],col_w=[1.7,2.1],size=12)
text(s,9.0,4.45,3.8,2.4,"Gold bars are vendor prices for the battery scope only. Navy bars are full project estimates. The battery price fell from $18.2M turnkey-indicative (2023, incl. civil) to $12.1M contracted (2026); the project rose $13.3M in the same window. The 2023 conceptual carried a placeholder that was never re-based until August 2026.",size=12.5,color=GRAY)
notes(s,"The story is not that batteries got expensive. The battery got cheaper. The project got more real.")
# ---------------- 10 2023 vs 2026 category walk ----------------
s=blank(p); n+=1; chrome(s,"What changed between the December 2023 conceptual and Rev 3: $43.9M to $57.2M",eyebrow="PAF category comparison, project 21334 ($M)",n=n)
cats=["Materials","Construction","Testing","Engineering","Siting + Env + Outreach","PMT","Other","Risks","Contingency","Indirects","AFUDC"]
e23=D["e23373_categories"]; r3=D["rev3_categories_21334"]
old=[e23["Materials"],e23["Construction"],e23["Testing"],e23["Engineering"],e23["Siting"]+e23["Environmental"]+e23["Outreach"],e23["PMT"],e23["Other"],e23["Risks"],e23["Contingency"],e23["Indirects"],e23["AFUDC"]]
new=[r3["Materials"],r3["Construction"],r3["Testing"],r3["Engineering"],r3["Siting"]+r3["Environmental"]+r3["Project Services"],r3["PMT"],r3["Other"]+r3["Removals"]+r3["ROW/Land"],r3["Risks"],r3["Contingency"],r3["Indirects"],r3["AFUDC"]]
cd=CategoryChartData(); cd.categories=cats; cd.add_series("E-23-373 (Dec 2023)",[round(v/1e6,2) for v in old]); cd.add_series("Rev 3 (Sep 2026)",[round(v/1e6,2) for v in new])
gf=s.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED,Inches(0.5),Inches(1.5),Inches(8.4),Inches(5.3),cd); ch=gf.chart; style_chart(ch,legend=True,size=11)
ch.series[0].format.fill.solid(); ch.series[0].format.fill.fore_color.rgb=MID; ch.series[1].format.fill.solid(); ch.series[1].format.fill.fore_color.rgb=NAVY
for sr in ch.series:
    sr.data_labels.show_value=True; sr.data_labels.number_format='0.0'; sr.data_labels.number_format_is_linked=False; sr.data_labels.position=XL_LABEL_POSITION.OUTSIDE_END; sr.data_labels.font.size=Pt(9)
ch.plots[0].gap_width=60; ch.plots[0].overlap=-10; ch.category_axis.tick_labels.font.size=Pt(9); ch.value_axis.tick_labels.font.size=Pt(9); ch.value_axis.has_major_gridlines=True; ch.value_axis.major_gridlines.format.line.color.rgb=MID; ch.value_axis.format.line.fill.background(); ch.category_axis.format.line.color.rgb=MID
deltas=[(c,(nv-ov)/1e6) for c,ov,nv in zip(cats,old,new)]; deltas.sort(key=lambda t:-abs(t[1]))
text(s,9.1,1.55,3.7,0.4,"Largest movements",size=15,bold=True,color=NAVY,font=HEAD)
table(s,9.1,1.95,3.7,3.4,["Category","Delta"],[[c,f"{'+' if v>=0 else '-'}${abs(v):.1f}M"] for c,v in deltas[:7]],col_w=[2.3,1.4],size=12,align_right=(1,))
text(s,9.1,5.5,3.7,1.4,"Materials: contracted battery replaces 2023 indicative pricing, plus breaker skids and GSUs. Testing and siting: Station 496 scope and Article 80 were not in E-23-373. AFUDC: a 20-month later ISD on a larger base.",size=12,color=GRAY)
notes(s,"Materials up 2.9, testing up 2.0, siting up 1.4, risk up 2.1, AFUDC up 1.7. Those five are 10.1 of the 13.3.")
# ---------------- 11 September walk ----------------
s=blank(p); n+=1; chrome(s,"Four revisions in five weeks: how the September estimate settled at $57.2M",eyebrow="Revision walk, 26 Aug to 24 Sep 2026",n=n)
steps=[("Rev 0\n26 Aug",47.2,None),("Battery to\nproject team\nvalue",4.7,"up"),("Rev 1\n1 Sep",51.9,None),("Battery to\ncontract +\nrelays + eng",11.8,"up"),("Rev 2\n10 Sep",63.6,None),("Relays -1.5,\nSSVT, eng\nre-base",-6.4,"down"),("Rev 3\n24 Sep",57.2,None)]
base=[];vis=[];run=0
for lab,v,kind in steps:
    if kind is None: base.append(0); vis.append(v); run=v
    elif kind=="up": base.append(run); vis.append(v); run+=v
    else: base.append(run+v); vis.append(-v); run+=v
cd=CategoryChartData(); cd.categories=[t[0] for t in steps]; cd.add_series("base",base); cd.add_series("val",vis)
gf=s.shapes.add_chart(XL_CHART_TYPE.COLUMN_STACKED,Inches(0.5),Inches(1.5),Inches(7.6),Inches(5.3),cd); ch=gf.chart; style_chart(ch,legend=False,size=10)
ch.series[0].format.fill.background(); ch.series[0].format.line.fill.background()
sr=ch.series[1]
for i,pt in enumerate(sr.points):
    pt.format.fill.solid(); k=steps[i][2]; pt.format.fill.fore_color.rgb = NAVY if k is None else (BURG if k=="up" else TEAL)
sr.data_labels.show_value=True; sr.data_labels.number_format='"$"0.0"M"'; sr.data_labels.number_format_is_linked=False; sr.data_labels.position=XL_LABEL_POSITION.INSIDE_END; sr.data_labels.font.size=Pt(10); sr.data_labels.font.color.rgb=WHITE; sr.data_labels.font.bold=True
ch.plots[0].gap_width=35; ch.category_axis.tick_labels.font.size=Pt(9); ch.value_axis.visible=False; ch.value_axis.has_major_gridlines=False; ch.category_axis.format.line.color.rgb=MID; ch.value_axis.maximum_scale=70
bullets(s,8.3,1.55,4.5,5.3,[("Rev 0 carried the battery at about $6M ","from the 2023 indicative sheet. The PM: 'we know the BESS system itself is 12.'"),("Rev 2 reset it to the cover agreement, escalated to $13.1M, ","and carried $1.5M of 'relays for batteries' from a 2023 bidder that priced its own switchgear."),("Rev 3 removed the relays ","(P&C Engineering: included in the $300K Siemens skid), cut three SSVTs to one, and re-based engineering to $501K to go plus actuals."),("Net: ","+$10.0M from Rev 0, of which $7.0M is the battery line catching up to the contract.")],size=13.5,gap=7)
notes(s,"This walk is in the email record. It matters because the full-funding placeholder of $43.9M was never touched between December 2023 and August 2026.")
# ---------------- 12 Battery price over time ----------------
s=blank(p); n+=1; chrome(s,"The battery itself: a $9.6M-$18.2M indicative spread in 2023, a $12.1M fixed price in 2026",eyebrow="Battery scope price points ($/kWh at 20 MWh)",n=n)
ind=D["indicative_2023"]
rows=[(k,v) for k,v in ind.items()]
cats=[k for k,_ in rows]+["Nomad contract\nMar 2026"]; vals=[round(v/20000) for _,v in rows]+[round(NOMAD/20000)]
cd=CategoryChartData(); cd.categories=cats; cd.add_series("$/kWh",vals)
gf=s.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED,Inches(0.5),Inches(1.5),Inches(7.6),Inches(5.3),cd); ch=gf.chart; style_chart(ch,legend=False,size=10)
sr=ch.series[0]
for i,pt in enumerate(sr.points):
    pt.format.fill.solid(); pt.format.fill.fore_color.rgb = GOLD if i==len(vals)-1 else (BURG if i==3 else MID)
sr.data_labels.show_value=True; sr.data_labels.number_format='"$"#,##0'; sr.data_labels.number_format_is_linked=False; sr.data_labels.position=XL_LABEL_POSITION.OUTSIDE_END; sr.data_labels.font.size=Pt(10); sr.data_labels.font.bold=True
ch.plots[0].gap_width=50; ch.category_axis.tick_labels.font.size=Pt(9); ch.value_axis.visible=False; ch.value_axis.has_major_gridlines=False; ch.category_axis.format.line.color.rgb=MID; ch.value_axis.maximum_scale=1150
bullets(s,8.3,1.55,4.5,5.3,[("July 2023, five bidders, 10 MW / 20 MWh: ","$9.6M to $18.2M. Every bidder excluded interconnection, permits beyond local, below-grade risk, sound walls or spares."),("Company 3 ($18.2M, burgundy) ","became the E-23-373 basis because it alone priced turnkey civil ($4.56M) and installation."),("March 2026 contract, $12.1M (gold): ","supply only, with supervision. Civil, install, GSUs, station and interconnection moved to Eversource scope."),("Equipment-only inside the contract: ","$10.64M, $532/kWh, in line with published 2025-26 turnkey system indices (slide 7)."),("Rev 3 adds $1.13M of escalation ","to a price the contract fixes until Final Acceptance.")],size=13,gap=6)
notes(s,"The lesson from 2023: a low bid with exclusions is not a low project. The lesson from 2026: the vendor price is defensible. It is the boundary that moved.")
# ---------------- 13 Interconnection & station ----------------
s=blank(p); n+=1; chrome(s,"Station and interconnection facilities: $18.3M loaded, and none of it in a vendor quote",eyebrow="What it takes to put 10 MW on four 13.8 kV feeders",n=n)
ic=[("Station 360 switching facilities (D)",LD["D. Station 360 13.8 kV switching & interconnection facilities"]),("Site development on landfill (E)",LD["E. Site development & civil (former landfill site)"]),("Station 496 protection (F)",F)]
cd=CategoryChartData(); cd.categories=[c for c,_ in ic]+["D-Line 24211 (memo)"]; cd.add_series("Loaded $M",[round(v/1e6,2) for _,v in ic]+[round(DLINE/1e6,2)])
gf=s.shapes.add_chart(XL_CHART_TYPE.BAR_CLUSTERED,Inches(0.5),Inches(1.5),Inches(6.4),Inches(3.2),cd); ch=gf.chart; style_chart(ch,legend=False,size=11)
sr=ch.series[0]; 
for i,pt in enumerate(sr.points): pt.format.fill.solid(); pt.format.fill.fore_color.rgb = MID if i==3 else TEAL
sr.data_labels.show_value=True; sr.data_labels.number_format='"$"0.0"M"'; sr.data_labels.number_format_is_linked=False; sr.data_labels.position=XL_LABEL_POSITION.OUTSIDE_END; sr.data_labels.font.size=Pt(11); sr.data_labels.font.bold=True
ch.plots[0].gap_width=40; ch.category_axis.reverse_order=True; ch.category_axis.tick_labels.font.size=Pt(11); ch.value_axis.visible=False; ch.value_axis.has_major_gridlines=False; ch.category_axis.format.line.color.rgb=MID; ch.value_axis.maximum_scale=9
tot_ic=sum(v for _,v in ic)
stat(s,0.6,4.9,3.0,1.9,f"${tot_ic/1e6:.1f}M","Loaded, in 21334",f"{tot_ic/TOT:.0%} of the approval level",vsize=32)
stat(s,3.75,4.9,3.15,1.9,f"${(tot_ic+DLINE)/1e6:.1f}M","Incl. D-Line memo",f"{(tot_ic+DLINE)/(TOT+DLINE):.0%} of the all-in view",vsize=32)
bullets(s,7.15,1.55,5.6,5.3,[("Four Siemens SDV7 breaker skids at $300K each ","(relays, PTs, DC battery, cabinet on the skid), disconnects, four metering transclosures, station service, riser poles, 15 kV cable and 1,240 ft of duct bank."),("Station 496: ","20 SEL relays replacing SEL-551 and REF610 units on four feeders, RTU and RTAC points, transfer trip over dark fiber; $1.8M of that is testing."),("Site: ","2.5 acres cleared, 760 ft road, 2,520 CY cut, imported fill, 14 ft retaining wall, ground grid, fence, lighting; Haugland's platform take-off is larger than ours and is unreconciled."),("D-Line (24211): ","5,465 ft feeder extension, three manholes, 16,395 ft of 3-700 cable; $4.8M is a 2023 conceptual figure.")],size=13,gap=6)
notes(s,"These are the facilities that make a battery a grid asset. A vendor's job ends at the container terminals.")
# ---------------- 14 Risk, contingency, loaders ----------------
s=blank(p); n+=1; chrome(s,"Risk, contingency, indirects and AFUDC are 41% of the approval level",eyebrow="Loaders on project 21334",n=n)
cd=CategoryChartData(); cd.categories=["Risk register","Contingency","Indirects / overheads","AFUDC"]; cd.add_series("$M",[round(v/1e6,2) for v in (6070000,2615200,9986700,5014000)])
gf=s.shapes.add_chart(XL_CHART_TYPE.PIE,Inches(0.5),Inches(1.5),Inches(5.2),Inches(5.2),cd); ch=gf.chart; style_chart(ch,legend=True,size=11,legend_pos=XL_LEGEND_POSITION.BOTTOM)
sr=ch.series[0]
for i,pt in enumerate(sr.points): pt.format.fill.solid(); pt.format.fill.fore_color.rgb=[BURG,GOLD,NAVY,TEAL][i]
sr.data_labels.show_value=True; sr.data_labels.number_format='"$"0.0"M"'; sr.data_labels.number_format_is_linked=False; sr.data_labels.font.size=Pt(11); sr.data_labels.font.color.rgb=WHITE; sr.data_labels.font.bold=True; sr.data_labels.position=XL_LABEL_POSITION.CENTER
table(s,6.0,1.55,6.75,3.5,["Station 360 risk item","$K"],[["Material cost, tariffs","1,000"],["Design / scope change orders","800"],["Labor cost, shortage, overtime","800"],["Unforeseen UG obstructions (landfill)","450"],["Environmental (DEP, landfill closure docs)","300"],["Soil contamination remediation","300"],["Station and P&C engineering changes","600"],["Weather, siting delay, outreach, BAR deductibles","1,050"]],col_w=[5.0,1.75],size=12,align_right=(1,))
text(s,6.0,5.2,6.75,1.6,"Risk plus contingency is 17.9% of the approval level before loaders, inside the 15-18% lead-review guidance. Indirects at 17.4% and AFUDC at 8.8% follow the EMA station template on a spend curve that runs from July 2021 to December 2028. Haugland's Attachment 4-F carries overlapping exposures (geotech $0.6M-$3.5M, fault-study equipment change $0.25M-$1.8M) that have not been reconciled with this register.",size=12.5,color=GRAY)
notes(s,"AFUDC is the cost of a seven-year development window. Every month of siting delay adds to it.")
# ---------------- 15 Open items ----------------
s=blank(p); n+=1; chrome(s,"What must close before this number goes to EPAC as full funding",eyebrow="Reconciliations and decisions, with the dollars at stake",n=n)
rows=[["Reconcile Haugland Class 3 base ($19.2M, its scope) to Rev 3 layers B+D+E ($8.3M direct)","Scope boundary","Unknown until mapped","Cost Estimating + PM + HEG"],
["Confirm four written design-basis items (retaining wall, detention basin, duct bank, GSU count)","Design confirmation","$1.47M HEG deduct ceiling","Substation Engineering"],
["Escalation on the fixed-price battery balance","Decision","$1.13M","PM / Cost Estimating"],
["Geotechnical investigation before IFC (platform depth, bearing)","Study","$0.38M deduct or $0.6M-$3.5M exposure","Civil Engineering"],
["NFPA 855 hazard mitigation analysis before civil freeze (footprint 36,100 vs 17,040 SF)","Study","$0.58M deduct; containment $0.10M","Capital Projects Eng."],
["Re-base D-Line 24211 (2023 conceptual $4.8M; HEG take-off larger)","Estimate","Unknown","Distribution Engineering"],
["Battery installation labor: replace 25%-of-16,801 mh with a crew build-up","Estimate","+/- $0.5M","Cost Estimating + Nomad"],
["Present full funding as Planning grade (-25/+25%) once the above close","Classification","Range narrows from -$14M/+$29M","Cost Estimating"]]
table(s,0.6,1.55,12.1,5.0,["Item","Type","Dollars at stake","Owner"],rows,col_w=[6.4,1.4,2.5,1.8],size=12)
text(s,0.6,6.6,12.1,0.4,"Haugland's own roll-up: $2.9M achievable deduct ceiling against its base, $0.15M to capture, plus $1.5M of avoided cost outside the base. Ceiling, not forecast.",size=12,color=GRAY)
notes(s,"Every item has an owner and a dollar figure. That is what makes it a plan rather than a worry list.")
# ---------------- 16 Contributions ----------------
s=blank(p); n+=1; rect(s,0,0,W,H,NAVY)
text(s,0.6,0.35,10,0.35,"CONTRIBUTIONS",size=12,bold=True,color=GOLD)
text(s,0.6,0.7,12.1,1.0,"A $12 million battery is a $57 million project, and now every dollar between them has a name",size=30,bold=True,color=WHITE,font=HEAD)
bullets(s,0.6,1.9,6.1,4.9,[("Cost layer extraction. ","292 Rev 3 line items in thirteen layers, reconciled to the penny. Direct shares: battery contract 23%, battery install and balance of plant 6%, station and interconnection 24%, owner scope 11%, Station 360 loaders 35%."),("Unit costs at every boundary. ","$605/kWh vendor, $833 installed, $2,500 Station 360, $2,862 project, $3,102 all-in. Benchmarks compared against the row that matches their definition."),("Cost history. ","2021 IFR to Rev 3, with the ISD drift and the five-week September walk documented from the ESF revisions and email record."),("Open-item register. ","Eight reconciliations with owners and dollars, led by the Haugland Class 3 reconciliation and the $1.13M escalation decision.")],size=14.5,color=WHITE,gap=8,bullet_color=GOLD)
rect(s,7.0,1.9,5.75,4.9,RGBColor(0x0B,0x2A,0x72))
text(s,7.2,2.05,5.4,0.4,"Decisions requested",size=16,bold=True,color=GOLD,font=HEAD)
bullets(s,7.2,2.5,5.4,4.2,["Adopt the layered view as the standard way this project is presented internally and to regulators: battery, station, interconnection, owner scope, loaders.","Direct the Haugland-to-Rev 3 reconciliation before the full-funding PAF is drafted.","Decide the escalation treatment on the fixed-price battery balance.","Fund the geotechnical investigation and the NFPA 855 hazard mitigation analysis now; both gate $1M of deducts and $3.5M of exposure.","Retire the $43.9M placeholder in the PAF narrative."],size=13.5,color=WHITE,gap=7,bullet_color=GOLD)
text(s,0.6,7.02,9,0.3,FOOT,size=10,color=MID)
notes(s,"Mirror the open. Leave this slide up for questions. Do not add a Questions slide.")
out=f"{B}/Hyde_Park_BESS_Cost_Analysis.pptx"; p.save(out); print("saved",out,"slides",n)
