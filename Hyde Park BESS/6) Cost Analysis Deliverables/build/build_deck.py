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
text(s,0.6,1.55,12,0.7,"“Why is a $12 million battery a $57 million project?”  Because a vendor prices the battery. We build the station, the site, the feeder protection and the siting case, and we carry the risk and the cost of money.",size=19,color=INK)
stat(s,0.6,2.7,3.9,2.4,"$12.1M","Vendor fixed-price contract","Nomad cover agreement, 10 Mar 2026. 12 Voyager LFP units, PCS, BMS, fire protection, 10-yr warranty. $605/kWh, $1,211/kW.")
stat(s,4.72,2.7,3.9,2.4,"$57.2M","Project 21334 approval level","ESF Total Rev 3. Station 360 $50.0M plus Station 496 protection $7.3M. $2,862/kWh, $5,725/kW. Conceptual, -25%/+50%.",vcolor=BURG)
stat(s,8.84,2.7,3.9,2.4,"21%","Battery share of the total","Add the D-Line circuit extension (24211, $4.8M conceptual) and the share drops to 20%. Four dollars of every five are not the battery.")
text(s,0.6,5.4,12.1,1.2,[[("Three sections: ",{"bold":True,"color":NAVY}),("where the money sits (thirteen layers, unit costs, benchmarks); how the cost changed (2021 to today); can the number be defended (red team, stress tests, what must close).",{})]],size=16)
notes(s,"Three numbers. Vendor contract, approval level, share. Everything after this slide is proof. CORE PATH for a 25-minute slot: slides 1, 2, 3, 6, 4, 7, 8, 9, 10, 12, 16, 20, 23, 27. Everything else is reachable from the appendix.")
SECTION[0]="1 · WHERE THE MONEY SITS"
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
text(s,0.6,6.65,12,0.35,"Gold = battery contract as carried in Rev 3 ($12.1M contract plus $1.1M escalation on the unpaid balance; see slide 19). Teal = station, site and feeder protection. Burgundy = risk, contingency, indirects, AFUDC. Total $57.2M.",size=11,color=GRAY)
notes(s,"Read left to right. The battery contract is the first bar. Everything to its right is the utility's project.")
# ---------------- 5 Layer table ----------------
s=blank(p); n+=1; chrome(s,"Where the $57.2M sits when risk, contingency, indirects and AFUDC are spread",eyebrow="Loaded view, factor 1.685 on Station 360 directs",n=n)
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
# ---------------- 13 Interconnection & station ----------------
s=blank(p); n+=1; chrome(s,"Station and interconnection: $18.3M loaded, none of it in a vendor quote",eyebrow="What it takes to put 10 MW on four 13.8 kV feeders",n=n)
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
# ---------------- 7 Benchmarks ----------------
s=blank(p); n+=1; chrome(s,"The battery is at market; the project is above it for reasons benchmarks exclude",eyebrow="Industry benchmarks vs Hyde Park boundaries, $/kWh nominal",n=n)
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
# ---------------- 7b Battery installed-cost curve ----------------
from pptx.chart.data import XyChartData
from pptx.enum.chart import XL_MARKER_STYLE
from pptx.enum.dml import MSO_LINE_DASH_STYLE
from lxml import etree
CV=json.load(open(f"{B}/curve.json"))
s=blank(p); n+=1; chrome(s,"Battery installed-cost curve: the Nomad price sits on it once duration and size are adjusted",eyebrow="Industry curve 2015-2028 vs Hyde Park, $/kWh, log scale",n=n)
cd=XyChartData()
dummy=cd.add_series("_")   # LibreOffice drops XY series that precede the longest series on import; make this hidden series the longest (points sit outside the axis range)
for xx in range(2000,2006): dummy.add_data_point(xx,100)
for sr_ in CV["series"]:
    ser=cd.add_series(sr_["name"].split(" (")[0])
    for x,y in sr_["points"]: ser.add_data_point(x,y)
hp_rng=cd.add_series("Hyde Park 2023 indicative bids (range)")
for pt_ in CV["hyde_park"]:
    if pt_.get("kind")=="range":
        hp_rng.add_data_point(pt_["x"],pt_["y"][0]); hp_rng.add_data_point(pt_["x"],pt_["y"][1])
hp_pts=cd.add_series("Hyde Park 2026 (equipment, contract, as carried, installed)")
for pt_ in CV["hyde_park"]:
    if "kind" not in pt_: hp_pts.add_data_point(pt_["x"],pt_["y"])
gf=s.shapes.add_chart(XL_CHART_TYPE.XY_SCATTER_LINES,Inches(0.5),Inches(1.5),Inches(7.7),Inches(4.95),cd); ch=gf.chart; style_chart(ch,legend=True,size=9.5,legend_pos=XL_LEGEND_POSITION.BOTTOM)
cols=[WHITE,INK,NAVY,TEAL,GRAY,BURG,GOLD]
for i,ser in enumerate(ch.series):
    ser.smooth=False; ser.format.line.color.rgb=cols[i]; ser.format.line.width=Pt(2.0)
    if i==0: ser.format.line.fill.background(); ser.marker.style=XL_MARKER_STYLE.NONE; continue
    i-=1
    ser.marker.style=XL_MARKER_STYLE.CIRCLE; ser.marker.size=7; ser.marker.format.fill.solid(); ser.marker.format.fill.fore_color.rgb=cols[i]; ser.marker.format.line.color.rgb=cols[i]
    if i==3: ser.format.line.dash_style=MSO_LINE_DASH_STYLE.DASH
    if i==4: ser.format.line.width=Pt(3.5); ser.marker.style=XL_MARKER_STYLE.DASH; ser.marker.size=12
    if i==5: ser.format.line.fill.background(); ser.marker.style=XL_MARKER_STYLE.DIAMOND; ser.marker.size=11; ser.marker.format.line.color.rgb=NAVY
va=ch.value_axis; va.minimum_scale=100; va.maximum_scale=3000; va.has_major_gridlines=True; va.major_gridlines.format.line.color.rgb=MID; va.tick_labels.number_format='"$"#,##0'; va.tick_labels.number_format_is_linked=False; va.tick_labels.font.size=Pt(9.5); va.format.line.color.rgb=MID
scaling=va._element.find('{http://schemas.openxmlformats.org/drawingml/2006/chart}scaling'); lb=etree.SubElement(scaling,'{http://schemas.openxmlformats.org/drawingml/2006/chart}logBase'); lb.set('val','10'); scaling.insert(0,lb)
lg=ch.legend._element; le=etree.SubElement(lg,'{http://schemas.openxmlformats.org/drawingml/2006/chart}legendEntry'); etree.SubElement(le,'{http://schemas.openxmlformats.org/drawingml/2006/chart}idx').set('val','0'); etree.SubElement(le,'{http://schemas.openxmlformats.org/drawingml/2006/chart}delete').set('val','1'); lg.find('{http://schemas.openxmlformats.org/drawingml/2006/chart}legendPos').addnext(le)
ca=ch.category_axis; ca.minimum_scale=2014.5; ca.maximum_scale=2029; ca.major_unit=2; ca.tick_labels.number_format='0'; ca.tick_labels.number_format_is_linked=False; ca.tick_labels.font.size=Pt(9.5); ca.has_major_gridlines=False; ca.format.line.color.rgb=MID
# labels on the Hyde Park points
for j,pt_ in enumerate([q for q in CV["hyde_park"] if "kind" not in q]):
    dl=ch.series[6].points[j].data_label; dl.has_text_frame=True; dl.text_frame.text=pt_["label"].split(",")[-1].strip(); dl.text_frame.paragraphs[0].runs[0].font.size=Pt(9); dl.text_frame.paragraphs[0].runs[0].font.bold=True; dl.text_frame.paragraphs[0].runs[0].font.color.rgb=NAVY; dl.position=[XL_LABEL_POSITION.BELOW,XL_LABEL_POSITION.LEFT,XL_LABEL_POSITION.RIGHT,XL_LABEL_POSITION.RIGHT][j]
bullets(s,8.4,1.55,4.4,5.0,[("The curve is a 4-h, 60-150 MW, real-dollar curve. ","EIA's reported all-in fell from $2,152 (2015) to $625 (2018); BNEF turnkey from $324 (2022) to $117 global and $219 US (2025); NREL's 4-h bottom-up base is $334 (2024), $247 by 2035."),("Hyde Park is 2-h, 10 MW, nominal. ","NREL's structure puts a 2-h system at 1.3-1.5x the 4-h $/kWh; the size elasticity in Appendix B adds 1.5x at 20 MWh. Adjusted US turnkey: $440-$505. Nomad equipment: $532."),("Install is the layer the curve never shows. ","Owner-scope installation, integration and balance of plant (B+C) add $183/kWh to the $650 battery line: $833 installed. BNEF's install sits inside a developer's EPC; ours is Eversource scope at New England rates."),("The 2026 turn. ","Lithium carbonate roughly doubled year on year by August 2026 and tariffs lifted delivered US prices. The March 2026 fixed price sits below where a 2027 re-procurement would land.")],size=12,gap=5)
text(s,0.6,6.5,7.6,0.5,"Plotted as published: EIA-860 nominal; BNEF real survey-year; NREL 2024$ (2028 interpolated between the 2024 base and the 2035 mid case). 2023 bar = five indicative bids, $479-$911/kWh, differing scopes. Retrieved from search excerpts; verify before external use.",size=9.5,color=GRAY)
notes(s,"Answer to 'is there a battery curve': yes, and the Nomad price lands on it. The curve is for four-hour, 60 to 150 MW systems in real dollars; our system is two-hour and 10 MW in nominal dollars, which is why the raw comparison looks unfavorable and the adjusted one does not. Sources: EIA Today in Energy #45596 (2015-2018 $/kWh); BNEF Energy Storage System Cost Surveys 2022-2025 (bnef.com/insights/30443, 33081, 35543, 38229); NREL Cole et al. 2025 Update (NREL/TP-6A40-93281); Anza and ESS News for the 2026 tariff and lithium moves. Duration factor from NREL's cost structure; size factor from the Appendix B regression.")
# ---------------- 7c Escalation basis ----------------
ES=CV["escalation"]; k=lambda v: f"${v/1e3:,.0f}K"; kwh=lambda v: f"${v/20000:,.0f}"
s=blank(p); n+=1; chrome(s,"Escalation is already in the number: $2.9M at template rates, $1.1M of it on a fixed price",eyebrow="Escalation basis and the common-dollar comparison",n=n)
text(s,0.6,1.5,6.0,0.35,"Where the escalation sits (Rev 3, included in the directs)",size=13,bold=True,color=NAVY)
table(s,0.6,1.9,6.0,2.35,["Item","$","$/kWh"],[["Escalation in the approval level (Sta 360 $2,622K + Sta 496 $326K)",k(ES["total"]),kwh(ES["total"])],["on the Nomad balance, which Exhibit C fixes until Final Acceptance",k(ES["battery"]),kwh(ES["battery"])],["on station, site, feeder protection, testing and owner scope",k(ES["total"]-ES["battery"]),kwh(ES["total"]-ES["battery"])],["Spend curve it is applied to: actuals $5.2M, 2026 $13.5M, 2027 $12.5M, 2028 $26.1M","",""]],col_w=[4.5,0.8,0.7],size=11,align_right=(1,2))
text(s,0.6,4.4,6.0,0.35,"Same comparison, same dollars (per kWh)",size=13,bold=True,color=NAVY)
table(s,0.6,4.8,6.0,1.95,["Boundary","Nominal","Ex-escalation","Benchmark brought to 2028 at 3%/yr"],[["Vendor contract","$605","$605 (fixed)","BNEF US turnkey $219 (2025) = $239"],["Battery as carried (A)","$650","$593","NREL 4-h $334 (2024$) = $376"],["Battery installed (A+B+C)","$833","~$756","NREL adjusted to 2-h, 10 MW: $750-$870"],["Station complete, direct","$1,483","$1,352","EIA/S&L $436 (2023$) = $505; LBNL $458 = $516"]],col_w=[1.55,0.85,1.1,2.5],size=10.5,align_right=(1,2))
bullets(s,6.9,1.5,5.9,5.3,[("Rates. ","ESF template escalation, about 3% a year, on the 2026-2028 spend curve. $2.9M is 5.1% of the approval level and 7.4% of directs. Benchmarks are 2023-2025 dollars; Rev 3 is 2026-2028 nominal, so one side must move before they are compared."),("Decision pending. ","$1.13M sits on a price the contract fixes. Remove it or move it to the risk register with a stated rationale (open item, slide 23)."),("Brought to the same year, the installed battery is on the index. ","NREL's $334 is $376 in 2028 dollars and $750-$870 after the 2-h and 10 MW adjustments; Hyde Park installed is $833."),("What 3% does not cover. ","Lithium carbonate and tariffs moved faster than 3% in 2026. The battery is fixed by contract, so the exposure is the $3.7M of non-battery material and the labor lines. The $1.0M tariff item in the risk register is sized on total material, battery included."),("Schedule. ","Twelve months of slip adds about $1.2M of escalation on the $38.6M scheduled for 2027-2028, before AFUDC, PM and indirects (about $5M in total)."),("Ex-escalation values ","strip the station's $131/kWh from the direct boundaries; the B+C share (~$20/kWh) is allocated pro rata and is approximate.")],size=11.5,gap=4)
notes(s,"Answer to 'escalation to be included': it is, at $2.95M on the ESF Overview tab (Sta 360 $2,622,100; Sta 496 $326,100), inside the directs at the template rates. The slide shows what it is applied to, which part of it is contestable ($1.13M on the fixed-price battery balance), and what the comparison looks like once both sides are in the same dollar year. The ex-escalation column removes the station escalation from the direct boundaries; the allocation of the non-battery escalation to B+C is pro rata to direct cost and approximate. The 2028 benchmark column compounds each published figure at 3% from its dollar year; the 2-h and 10 MW adjustment is the same one used on the curve slide.")
# ---------------- 7d Comparables re-based to 2026 dollars ----------------
AJ=json.load(open(f"{B}/adjust_results.json")); IX=AJ["indices"]; RC=json.load(open(f"{B}/stats_results.json"))["reference_class"]
s=blank(p); n+=1; chrome(s,f"Re-based to 2026 dollars, the {RC['n']}-project class moves by at most a tenth and Hyde Park's station cost stays in the top fifth",eyebrow=f"{RC['n']} comparables at or below 100 MWh ({RC['n_utility']} utility-, {RC['n_developer']} developer-owned), nominal vs 2026$",n=n)
s.shapes.add_picture(f"{B}/adjust_dumbbell.png",Inches(0.45),Inches(1.45),height=Inches(5.45))
rows_=[["Nominal, as published",f"${AJ['nominal']['median']:,.0f}",f"{AJ['nominal']['hp_pct']['installed']:.0%}",f"{AJ['nominal']['hp_pct']['station_direct']:.0%}"]]+[[lab,f"${IX[k]['median']:,.0f}",f"{IX[k]['hp_pct']['installed']:.0%}",f"{IX[k]['hp_pct']['station_direct']:.0%}"] for k,lab in (("installed","Installed all-in (EIA, LBNL)"),("pack","BNEF pack price"),("turnkey","BNEF turnkey system"),("nrel","NREL bottom-up base year"),("lcos","Lazard LCOS midpoint"),("construction","Construction index only"))]
table(s,8.35,1.5,4.45,3.1,["Battery index (40% share)","Median $/kWh","HP installed","HP station"],rows_,col_w=[2.05,0.9,0.75,0.75],size=9.5,align_right=(1,2,3))
bullets(s,8.35,4.75,4.45,2.2,[("Two forces, one net. ","Batteries fell 1.4 to 2x since 2018; Handy-Whitman utility construction rose 49%. On a 40% battery share the net factor for a 2018 project is 1.1 to 1.2."),("Adding 31 projects, 18 of them developer-owned New York and New England sites, ","pulls the median from $1,235 to $831 and lifts Hyde Park's station-direct cost to the 86th percentile. That is the honest comparison and the argument still holds: those sites carry no utility station, no landfill and no siting case."),("The curve you pick moves the median by 4%; ","slide 14 shows what moves it more.")],size=10.5,gap=4)
notes(s,f"Reference class redefined on 2 Oct 2026 at the reviewer's request: every project at or below 100 MWh with an all-in disclosed cost, any owner. {RC['n']} members ({RC['n_utility']} utility-owned, {RC['n_developer']} developer-owned); utility-only subclass of {json.load(open(f'{B}/stats_results.json'))['reference_class_utility']['n']} kept in the workbook for continuity (median ${json.load(open(f'{B}/stats_results.json'))['reference_class_utility']['median_kwh']:,.0f}). Model: cost_2026 = cost x [ s x I(2026)/I(y) + (1 - s) x HW(2026)/HW(y) ], s = 0.40, I = the battery index in the row, HW = Handy-Whitman North Atlantic production-plant index (700 in 2015, 745 in 2018, 1,112 in 2026; PJM posting). The 3.5%/yr flat proxy used in the earlier version gives ${IX['installed_flat35']['median']:,.0f} at the installed index. Naive whole-cost deflation at the battery rate: ${IX['installed']['naive_median']:,.0f} (installed), ${IX['pack']['naive_median']:,.0f} (pack). Sources on the workbook tab '2026$ Adjustment' and in the research log.")
# ---------------- 7e New York cohort ----------------
NYC=json.load(open(f"{B}/ny_cohort.json")); NYR=[r for r in AJ["ny"]]
s=blank(p); n+=1; chrome(s,"New York is building the same thing: distribution-connected, 2025, $524 to $1,110 per kWh before any utility station",eyebrow="New York distribution-scale cohort vs Hyde Park, $/kWh nominal (2021-2027 dollars)",n=n)
ny_rows=[("NYSERDA retail avg, 2020-21 installs",464,None),("NYSERDA retail avg, 2022-23 installs",567,None),("Elevate, Victory Blvd SI, 15 MW / 60 MWh (2025)",524,None),("O&R Pomona, 3 MW / 12 MWh, utility (2021)",617,None),("Soltage Maspeth, 5 MW / 20 MWh* (2025)",805,None),("NineDot 28-site portfolio, financing floor (2026-27)",872,None),("NineDot Arthur Kill Rd, 9.8 MW / 39 MWh (2025)",1110,None),("Con Ed Ozone Park, 1.5 MW / 12 MWh, utility (2019)",1250,None),("NYPA Chateaugay, 20 MW / 20 MWh, utility (2023)",1490,None),("Hyde Park: vendor contract",605,"hp"),("Hyde Park: battery installed (A+B+C)",833,"hp"),("Hyde Park: station complete, direct",1483,"hpall"),("Hyde Park: project 21334 approval level",2862,"hpall")]
cd=CategoryChartData(); cd.categories=[r[0] for r in ny_rows]; cd.add_series("$/kWh",[r[1] for r in ny_rows])
gf=s.shapes.add_chart(XL_CHART_TYPE.BAR_CLUSTERED,Inches(0.5),Inches(1.5),Inches(7.6),Inches(5.0),cd); ch=gf.chart; style_chart(ch,legend=False,size=9.5)
sr=ch.series[0]
for i,pt in enumerate(sr.points):
    pt.format.fill.solid(); pt.format.fill.fore_color.rgb={"hp":GOLD,"hpall":BURG}.get(ny_rows[i][2],(TEAL if "utility" in ny_rows[i][0] else NAVY))
sr.data_labels.show_value=True; sr.data_labels.number_format='"$"#,##0'; sr.data_labels.number_format_is_linked=False; sr.data_labels.position=XL_LABEL_POSITION.OUTSIDE_END; sr.data_labels.font.size=Pt(9)
ch.plots[0].gap_width=40; ch.category_axis.reverse_order=True; ch.category_axis.tick_labels.font.size=Pt(9); ch.value_axis.visible=False; ch.value_axis.has_major_gridlines=False; ch.category_axis.format.line.color.rgb=MID; ch.value_axis.maximum_scale=3600
table(s,8.3,1.5,4.5,2.1,["Per kW of power","$/kW"],[["NineDot Arthur Kill Rd (NYCIDA budget)","$4,427"],["NineDot portfolio financing (floor)","$3,476"],["Soltage Maspeth (NYCIDA)","$3,221"],["Elevate Victory Blvd (NYCIDA)","$2,096"],["Hyde Park station complete, direct","$2,967"],["Hyde Park approval level","$5,725"]],col_w=[3.4,1.1],size=10,align_right=(1,))
bullets(s,8.3,3.75,4.5,3.1,[("NineDot: ","11 projects at 6 NYC sites, 39 MW operating (Sep 2026); 28 more financed at $431M for 494 MWh. Thirteen NYC developer sites with NYCIDA-filed costs are now in the dataset (NineDot, Convergent, Soltage, Agilitas, Greenbacker, Elevate): $410 to $1,110/kWh, median about $830. Developer-owned 4-h sites on leased lots, VDER revenue, NYSERDA incentive, ITC; no utility station, no landfill, no siting case."),("Their own filed budget for Arthur Kill Road is $1,110/kWh and $4,427/kW, ","inside Hyde Park's installed-to-station band on $/kWh at twice the duration."),("Interconnection is the cost no index carries: ","Con Edison's two-part test added about $21M of upgrades per project on 34 projects (161 MW), per the NY-BEST and NYSEIA filing of 11 Mar 2026. Hyde Park's Station 496 scope is $7.3M."),("*Soltage duration assumed 4-h; ","incentives and ITC not netted from any row.")],size=10,gap=3)
notes(s,"Answer to the review comment that New York has built many more of these (NineDot Energy). Sources: NYCIDA public hearing notices and inducement resolutions (edc.nyc, Mar-Apr 2024) for the Arthur Kill Road, Victory Boulevard and Maspeth project costs; NineDot and Natixis releases (Feb 2026) for the 28-project financing; NYSERDA 6 GW Energy Storage Roadmap (Dec 2022) for the retail program averages; Utility Dive and the NY-BEST/NYSEIA filing in Case 24-E-0621 for the interconnection figures; existing dataset rows for Pomona, Ozone Park and Chateaugay. The NY cohort is 2021-2027 dollars and is not re-based (2025 to 2026 at the installed index is +2%). Developer-owned rows carry developer overhead and profit but not utility indirects or AFUDC. Thirteen NYCIDA-costed New York City sites are in the regression dataset and the reference class (2 Oct 2026 research pass); the financing floor and the NYSERDA averages are not project costs and are not. Appendix B carries the re-run regression.")
# ---------------- 7f What the choice of curve does ----------------
s=blank(p); n+=1; chrome(s,"The battery curve you choose moves the median 4%; the battery share and the construction index move it more",eyebrow="Normalizing to 2026: six indices x three battery shares, class median $/kWh",n=n)
CL=AJ["classes"]["reference_class"]["indices"]; keys=[("installed","Installed all-in"),("pack","BNEF pack"),("turnkey","BNEF turnkey"),("nrel","NREL base year"),("lcos","Lazard LCOS"),("construction","Construction only")]
cd=CategoryChartData(); cd.categories=[lab for _,lab in keys]
for sh in ("0.3","0.4","0.5"): cd.add_series(f"Battery share {int(float(sh)*100)}%",[round(CL[k]["by_share"][sh]["median"]) for k,_ in keys])
gf=s.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED,Inches(0.5),Inches(1.5),Inches(7.6),Inches(3.6),cd); ch=gf.chart; style_chart(ch,legend=True,size=9.5,legend_pos=XL_LEGEND_POSITION.BOTTOM)
for i,col in enumerate((MID,NAVY,TEAL)):
    sr=ch.series[i]; sr.format.fill.solid(); sr.format.fill.fore_color.rgb=col
    if i==1: sr.data_labels.show_value=True; sr.data_labels.number_format='"$"#,##0'; sr.data_labels.number_format_is_linked=False; sr.data_labels.position=XL_LABEL_POSITION.OUTSIDE_END; sr.data_labels.font.size=Pt(9)
ch.plots[0].gap_width=60; ch.plots[0].overlap=-5; ch.category_axis.tick_labels.font.size=Pt(9.5); ch.value_axis.minimum_scale=0; ch.value_axis.maximum_scale=1600; ch.value_axis.has_major_gridlines=True; ch.value_axis.major_gridlines.format.line.color.rgb=MID; ch.value_axis.tick_labels.font.size=Pt(9); ch.value_axis.tick_labels.number_format='"$"#,##0'; ch.value_axis.tick_labels.number_format_is_linked=False; ch.category_axis.format.line.color.rgb=MID
text(s,0.6,5.15,7.5,0.35,f"Nominal median ${AJ['nominal']['median']:,.0f}. Hyde Park station complete, direct, is $1,483/kWh; its percentile under each index is at right. Deflating whole projects at the battery rate gives ${CL['turnkey']['naive_median']:,.0f} to ${CL['installed']['naive_median']:,.0f}.",size=10.5,color=GRAY)
rows_=[[lab,f"{CL[k]['ratio_2018']:.2f}x",f"{0.4*CL[k]['ratio_2018']+0.6*AJ['hw_ratio_2018']:.2f}x" if k!="construction" else f"{AJ['hw_ratio_2018']:.2f}x",f"{CL[k]['by_share']['0.4']['hp_pct']['station_direct']:.0%}"] for k,lab in keys]
table(s,8.35,1.5,4.45,2.9,["Index","2018 to 2026","Net factor, 2018 project, 40% share","HP station pct"],rows_,col_w=[1.45,0.95,1.3,0.75],size=9.5,align_right=(1,2,3))
bullets(s,8.35,4.55,4.45,2.4,[("Choice of battery curve: ","medians $828 to $923, a 4% spread outside LCOS. The curves disagree about packs, not about projects."),("Battery share: ","30% to 50% moves the median $26 to $53 under any curve; the share is a bigger lever than the curve."),("Construction index: ",f"Handy-Whitman North Atlantic rose 49% from 2018 to 2026 (10% a year in 2021-22); a flat 3.5% proxy gives 32%, and a median ${AJ['indices']['installed_flat35']['median']:,.0f} instead of ${AJ['indices']['installed']['median']:,.0f}."),("LCOS ","is a levelized $/MWh metric, flat since 2019; using it re-bases nothing on the battery side.")],size=10,gap=4)
text(s,0.6,5.55,7.5,1.3,"Indices as published (BNEF pack and ESS surveys 2014-2025; EIA-860 2015-18 and LBNL 2024; NREL 2022 and 2024 base years; Lazard LCOS v5.0-2026 midpoints; Handy-Whitman via PJM), linearly interpolated between published points and held flat outside them. Retrieved from search excerpts; verify before external use.",size=9.5,color=GRAY)
notes(s,"This is the answer to 'what do the different curves do'. Three levers in order of leverage: (1) the non-battery escalator, because 60% of a comparable is station, civil, labor and interconnection and Handy-Whitman says that cost rose half again since 2018; (2) the battery share, which nobody discloses per project; (3) the battery curve itself, where the five published series agree within 4% on the class median once the share is fixed. The ratios in the table: pack 0.61, turnkey 0.49 (2021 base), NREL 0.69 (2022 base), installed 0.73, LCOS 1.03, Handy-Whitman 1.49. Net factor = 0.4 x battery ratio + 0.6 x 1.49.")
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
SECTION[0]="2 · HOW THE COST CHANGED"
# ---------------- 9 Cost over time ----------------
s=blank(p); n+=1; chrome(s,"Five years, five in-service dates, and an estimate that moved from $44M to $57M",eyebrow="Cost history, 2021 to 2026",n=n)
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
s=blank(p); n+=1; chrome(s,"The battery: a $9.6M to $18.2M spread in 2023, a $12.1M fixed price in 2026",eyebrow="Battery scope price points ($/kWh at 20 MWh)",n=n)
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
bullets(s,8.3,1.55,4.5,5.3,[("July 2023, five bidders, 10 MW / 20 MWh: ","$9.6M to $18.2M. Every bidder excluded interconnection, permits beyond local, below-grade risk, sound walls or spares."),("Company 3 ($18.2M, burgundy) ","became the E-23-373 basis because it alone priced turnkey civil ($4.56M) and installation."),("March 2026 contract, $12.1M (gold): ","supply only, with supervision. Civil, install, GSUs, station and interconnection moved to Eversource scope."),("Equipment-only inside the contract: ","$10.64M, $532/kWh, in line with published 2025-26 turnkey system indices (slides 9-10)."),("Rev 3 adds $1.13M of escalation ","to a price the contract fixes until Final Acceptance.")],size=13,gap=6)
notes(s,"The lesson from 2023: a low bid with exclusions is not a low project. The lesson from 2026: the vendor price is defensible. It is the boundary that moved.")
SECTION[0]="3 · CAN THE NUMBER BE DEFENDED"
# ---------------- 15b Red team kill shots ----------------
s=blank(p); n+=1; chrome(s,"Three assumptions that, if wrong, move the number more than the reserve",eyebrow="Independent challenge, 29 Sep 2026",n=n)
ks=[("1. Construction may be low, not high.","Rev 3 layers B+D+E are $8.3M direct. Haugland's Class 3 base for overlapping scope is $19.2M with a $2.9M deduct ceiling. Nobody has mapped one to the other.","Settles it: a signed HEG-to-Rev 3 scope map before the PAF is drafted."),
("2. Siting is binary and carries no float.","ZBA determination, construction start and container delivery all land in Q1 2028 for a Dec 2028 ISD. Denial means an EFSB exemption at 18-24 months. The estimate carries $250K for siting delay.","Settles it: Article 80 filing date, ZBA calendar, P6 float on the siting chain."),
("3. The number is Class 4 wearing Class 3 clothes.","30% engineering, unit-library construction with no bid, install labor as a percentage of a 2023 total, a 2.5 ft platform placeholder. EPAC will hear $57.2M as a planning number.","Settles it: geotech, HMA, HEG map, crew build-up; then reclassify with a -15/+25% range.")]
for i,(h,b,e) in enumerate(ks):
    y=1.55+i*1.72; rect(s,0.6,y,12.1,1.6,LIGHT); rect(s,0.6,y,0.09,1.6,BURG)
    text(s,0.85,y+0.08,4.0,1.45,h,size=16,bold=True,color=BURG,font=HEAD)
    text(s,4.9,y+0.08,5.2,1.45,b,size=12.5)
    text(s,10.2,y+0.08,2.45,1.45,e,size=11.5,color=NAVY,italic=True)
notes(s,"Steelman first: the battery is contracted, every dollar has a name, the direct cost is inside the reference class. These three are what an outside reviewer will find if we do not.")
# ---------------- 15c Stress tests + base rate ----------------
s=blank(p); n+=1; chrome(s,"Stress tests on our own numbers, and what history says about small utility batteries",eyebrow="Red team: quantified downside, loaded at 1.685",n=n)
rows=[["Construction unit costs +25% on B+D+E+G","+$4.0M","0","Yes, alone"],["HEG reconciliation at midpoint of the gap (+$5M direct)","+$8.4M","0","No"],["Schedule +12 months (siting or long-lead)","~+$5M","+12 mo","Partly"],["EFSB zoning exemption path","~+$8M to +$10M","+18-24 mo","No"],["Contractor bids +20% over estimate labor","+$2.1M","0","Yes, alone"],["Combination: HEG midpoint + 12-month slip","~+$13M (to ~$70M)","+12 mo","No"],["Battery change orders at the LD cap (10%)","+$1.2M","0","Yes"]]
table(s,0.6,1.5,7.6,4.2,["Scenario","Loaded cost","Date","Covered by $7.6M reserve?"],rows,col_w=[3.6,1.5,1.0,1.5],size=11)
text(s,0.6,5.8,7.6,1.0,"Untestable from the package: tariff or change-in-law pass-through on the Nomad price (Exhibit C terms), the AFUDC rate (assumed ~7% on CWIP), Station 496 outage premium (1.35 to 1.70 factor on affected hours), FEOC / ITC effect on net cost.",size=10.5,color=GRAY)
text(s,8.5,1.5,4.3,0.4,"Base rate: approved to actual",size=15,bold=True,color=NAVY,font=HEAD)
table(s,8.5,1.95,4.3,2.5,["Project","Uplift"],[["BGE Fairhaven 2.5 MW/9.7 MWh","+64%"],["HECO Waena 40 MW/160 MWh","+37%"],["SaskPower Regina 20 MW","+31%"],["Eversource Provincetown","+9% to +40%"],["Hyde Park, Dec 2023 to Sep 2026","+30%"],["Hyde Park, Rev 0 to Rev 3 (5 wks)","+21%"]],col_w=[3.0,1.3],size=11,align_right=(1,))
text(s,8.5,4.6,4.3,2.3,"Rev 3 carries 17.9% risk plus contingency. The exception case for beating the base rate rests on three anchors: a fixed battery price, a Siemens price on the skids, and Haugland engaged pre-construction. Together they cover about a third of the cost. The other two thirds have no such anchor.",size=11.5,color=INK)
notes(s,"The combination case is the one to plan against. It is not exotic: it is the HEG gap plus one missed siting season.")
# ---------------- 15d Pre-mortem ----------------
s=blank(p); n+=1; chrome(s,"Pre-mortem: June 2031, $74M, fifteen months late. What happened?",eyebrow="Red team: failure narrative and early-warning indicators",n=n)
rect(s,0.6,1.5,6.3,5.3,LIGHT)
text(s,0.8,1.7,5.9,5.0,"The ZBA conditioned approval on a smaller footprint and new screening; the civil package went back through Haugland in the winter of 2028. Spring 2027 borings found debris deeper than the 2014 closure set showed; the platform went from 2.5 ft of fill to piles, and the reconciliation that had never been done was done as a change order. Nomad's twelve containers arrived on time in January 2028 and sat in a rented yard for nine months. Station 496 cutovers needed night outages priced at straight time. AFUDC alone added $4M. The PAF had said Conceptual, -25/+50%. Everyone remembered $57M.",size=12.5,color=INK,italic=True)
text(s,7.2,1.5,5.6,0.4,"Early-warning indicators",size=15,bold=True,color=NAVY,font=HEAD)
table(s,7.2,1.95,5.6,4.9,["Indicator","Caught today?"],[["Geotech report not issued by IFC-civil design freeze (mid-2027)","No: no P6 gate ties IFC to it"],["ZBA hearing date not set within 90 days of Article 80 filing","No: siting carries hours, not milestones"],["HEG reconciliation not closed before the PAF is drafted (Nov 2026)","Only if the CoE makes it a precondition"],["Nomad final-drawings milestone (13 Jul 2026) slipped","Partly: payments tracked, not downstream effect on GSU spec and civil"],["Station 496 outage plan not issued before construction pricing","No"]],col_w=[3.4,2.2],size=11)
notes(s,"Five indicators, none of them expensive to watch. Three of them have no owner today.")
# ---------------- 15 Open items ----------------
s=blank(p); n+=1; chrome(s,"What must close before this number goes to EPAC as full funding",eyebrow="Reconciliations and decisions, red-team ranked",n=n)
rows=[["Reconcile Haugland Class 3 base ($19.2M, its scope) to Rev 3 layers B+D+E ($8.3M direct). Red team expects it to move the base up, not down.","Scope boundary","+$4M to +$8M direct if half the gap is 21334 scope","Cost Estimating + PM + HEG"],
["Siting chain has no float: ZBA determination Feb 2028, construction start Feb 2028, ISD Dec 2028; EFSB fallback 18-24 mo","Schedule","~$5M per 12 months (AFUDC, escalation, PM, indirects)","Siting + PM"],
["Present full funding at its real maturity: 30% engineering, no bid, placeholder platform = Class 4","Classification","Range is -25/+50% ($43M-$86M) until closed","Cost Estimating"],
["Geotechnical investigation and NFPA 855 hazard mitigation analysis before civil freeze","Study","$1.0M of deducts vs $0.6M-$3.5M exposure","Civil + Capital Projects Eng."],
["Confirm four written design-basis items (retaining wall, basin, duct bank, GSU count)","Design confirmation","$1.47M HEG deduct ceiling (~$0.8M net of GSUs already at 4)","Substation Engineering"],
["Escalation on the fixed-price battery balance; check Exhibit C for tariff / change-in-law pass-through","Decision","$1.13M","PM / Cost Estimating / Sourcing"],
["Battery installation labor: replace 25%-of-16,801 mh with a crew build-up","Estimate","+/- $0.5M (Rev 2 used 50%)","Cost Estimating + Nomad + HEG"],
["Station 496 at $363K per relay: compare to two recent EMA relay-replacement actuals; outage-window premium not priced","Benchmark","Unknown; $1.8M testing line","P&C Engineering"],
["Spot generation if the BESS misses Dec 2028 (SSF: 2-8 MW) was removed from scope; who carries it?","Scope / ownership","Not in project","System Planning"],
["Re-base D-Line 24211 (2023 conceptual $4.8M; HEG take-off larger)","Estimate","Unknown","Distribution Engineering"]]
table(s,0.6,1.45,12.1,4.9,["Item","Type","Dollars at stake","Owner"],rows,col_w=[6.6,1.3,2.5,1.7],size=10)
text(s,0.6,6.62,12.1,0.35,"Defensible reductions (~$3M: battery escalation, design-basis confirmations, material risk sized on non-battery material) are conditional on the Haugland reconciliation closing first.",size=11,color=GRAY)
notes(s,"Ranked by the red team. The first two items are the ones that can move the number by more than the whole reserve; the rest are hygiene.")
SECTION[0]=""
# ---------------- 16 Contributions ----------------
s=blank(p); n+=1; rect(s,0,0,W,H,NAVY)
text(s,0.6,0.35,10,0.35,"CONTRIBUTIONS",size=12,bold=True,color=GOLD)
text(s,0.6,0.7,12.1,1.0,"A $12 million battery is a $57 million project, and now every dollar between them has a name",size=30,bold=True,color=WHITE,font=HEAD)
bullets(s,0.6,1.9,6.1,4.9,[("Where the money sits. ","292 lines in thirteen layers, reconciled to the penny: battery contract 21%, station and interconnection 32% loaded, owner scope 19%, loaders 41%."),("Unit cost at every boundary. ","$605/kWh vendor, $833 installed, $1,483 station direct, $2,862 project. Each benchmark read against the row that shares its definition."),("How it changed. ","The battery got cheaper; the project got real. $43.9M to $57.2M, five in-service dates, documented from the ESF revisions and the email record."),("Can it be defended. ","Inside the reference class on direct cost; three kill shots, seven stress tests, a pre-mortem, and ten reconciliations with owners and dollars.")],size=14.5,color=WHITE,gap=9,bullet_color=GOLD)
rect(s,7.0,1.9,5.75,4.9,RGBColor(0x0B,0x2A,0x72))
text(s,7.2,2.05,5.4,0.4,"Decisions requested",size=16,bold=True,color=GOLD,font=HEAD)
bullets(s,7.2,2.5,5.4,4.2,["Adopt the layered view (battery, station, interconnection, owner scope, loaders) as the standard presentation of this project, internally and to regulators.","Make the Haugland-to-Rev 3 reconciliation, the geotech and the hazard mitigation analysis preconditions of the November PAF; present at Class 4 until they close.","Assign owners to the siting-chain float and the five early-warning indicators."],size=13.5,color=WHITE,gap=7,bullet_color=GOLD)
text(s,0.6,7.02,9,0.3,FOOT,size=10,color=MID)
notes(s,"Mirror the open. Leave this slide up for questions. Do not add a Questions slide.")
out=f"{B}/Hyde_Park_BESS_Cost_Analysis.pptx"; p.save(out); print("saved",out,"slides",n)
