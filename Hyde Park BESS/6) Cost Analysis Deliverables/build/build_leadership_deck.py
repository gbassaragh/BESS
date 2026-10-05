"""Leadership brief: what can be done to drive the Hyde Park BESS cost down.
Action-first cut of the cost analysis: every lever with a dollar range, an owner and a date.
Reads the same JSON outputs as build_deck.py."""
import json, os
from pptx_common import *
B=os.path.dirname(os.path.abspath(__file__))
SV=json.load(open(f"{B}/savings.json")); SVI={i["id"]:i for i in SV["items"]}; SVT=SV["tiers"]
SC=json.load(open(f"{B}/scope_challenge.json")); MS=json.load(open(f"{B}/mc_scope_results.json"))
ODDS={r["driver"][:2]:r["p"] for r in MS["ranked_opportunities"]}
APPROVAL=57247300.0
def m(v): return f"${v/1e6:.1f}M"
def rng(a,b): return m(a) if abs(a-b)<5e4 else f"${a/1e6:.1f} to {b/1e6:.1f}M"
def grp(ids): return sum(SVI[i]["lo_loaded"] for i in ids), sum(SVI[i]["hi_loaded"] for i in ids)
NOW=["A1","A2","A4","A5","B5","C3"]; STUDY=["A3","B1","B2","B3","B4","B6","B7","B8"]; REV=["C1","C2"]
now_lo,now_hi=grp(NOW); st_lo,st_hi=grp(STUDY); rev_lo,rev_hi=grp(REV)
C=SC["cases"]; T=SC["totals"]; cont=C["contained"]; resc=C["rescoped"]; expo=C["exposures"]; heg=C["heg"]; net=C["net"]
MC=MS["cases"]; SCH=MS["schedule"]
p=prs(); n=0
SHORT={"A1":"Strike the escalation carried on the fixed-price battery","A2":"Re-word two risk lines that duplicate that escalation","A3":"Confirm the four design-basis items Haugland priced as deducts","A4":"Take the E&S overhead basis off the vendor contract","A5":"Split commissioning hours with Nomad in the test plan","B1":"Price the Station 496 relay program at benchmark","B2":"Two feeders instead of four if hosting capacity allows","B3":"Size the platform and wall after geotech, not before","B4":"Battery install labor from a crew build-up","B5":"Strike the disconnects and PTs the Siemens skids already carry","B6":"GSU install hours and count settled in writing","B7":"Lighting to the security need, not 12 HPS luminaires","B8":"Siting and PM task budgets from outside counsel","C1":"Section 48E investment tax credit (30%)","C2":"Energy-community adder (+10 points)","C3":"Pay the battery at delivery, not a year ahead (AFUDC)"}
NEEDS={"A1":"Decision; Exhibit C read for pass-through","A2":"Re-word and re-size the two lines","A4":"Accounting ruling","A5":"Test plan split written","B5":"Siemens confirms skid scope in writing","C3":"Nomad milestone schedule in the SOV","A3":"Haugland-to-Rev 3 scope map, signed","B1":"Two recent EMA relay actuals","B2":"Hosting-capacity study","B3":"Geotech report; MassDEP post-closure conditions","B4":"Crew build-up with Nomad and HEG","B6":"Topology and GSU count in writing","B7":"Lighting design","B8":"Task budget from outside counsel"}
DATE={"A1":"Nov 2026","A2":"Nov 2026","A4":"Nov 2026","A5":"Nov 2026","B5":"Nov 2026","C3":"Nov 2026","A3":"Q1 2027","B1":"Q1 2027","B2":"Q1 2027","B3":"Q1 2027","B4":"Q1 2027","B6":"Q1 2027","B7":"Q1 2027","B8":"Q1 2027"}

# ---------- 1 Title ----------
s=blank(p); n+=1; rect(s,0,0,W,H,NAVY); rect(s,0,0,W,0.06,GOLD)
text(s,0.8,1.9,11.5,1.6,"Driving the Hyde Park BESS cost down: $57M to $47M, and who owns each dollar",size=38,bold=True,color=WHITE,font=HEAD,line_spacing=1.0)
text(s,0.8,3.75,11.5,1.0,f"Sixteen levers, three gates and a design-to-cost target that take Project 21334 from the $57.2M approval level to a {rng(resc['lo'],resc['hi'])} re-scoped project, with the decisions leadership is asked to make now",size=18,color=MID)
text(s,0.8,5.5,11.5,0.45,"Cost Estimating Center of Excellence  |  Leadership brief  |  Basis: ESF Total Rev 3, 24 Sep 2026  |  5 Oct 2026",size=13,color=GOLD)
text(s,0.8,5.95,11.5,0.35,"Internal. Contains vendor-confidential pricing. Backup: Hyde Park BESS Cost Analysis Deck (41 slides).",size=11,color=MID)
notes(s,"Executive mode. The promise: by the end of this brief leadership can say what will be done to lower the cost, who owns each action, what it is worth and by when. The analysis behind every number is in the 41-slide reference deck, the whitepaper and the workbook; none of it is repeated here.")

# ---------- 2 The promise: three numbers and the ask ----------
s=blank(p); n+=1; chrome(s,f"The number can be driven from $57.2M to {rng(resc['lo'],resc['hi'])}. About a third of that needs only a decision.",eyebrow="What can be done",n=n)
stat(s,0.6,1.55,3.9,2.0,"$57.2M","Approved, Rev 3","24 Sep 2026; includes $7.6M of risk and contingency and $20.3M of loaders",vsize=26)
stat(s,4.7,1.55,3.9,2.0,rng(cont['lo'],cont['hi']),"Contained: decisions only","Six decisions, no scope change, no study, by the November 2026 PAF",vsize=26)
stat(s,8.8,1.55,3.9,2.0,rng(resc['lo'],resc['hi']),"Re-scoped after four studies","Geotech, hosting capacity, relay actuals, Haugland scope map; Q1 2027",vsize=26)
bullets(s,0.6,3.85,12.1,3.0,[
 ("Decide now (no study): ",f"{rng(now_lo,now_hi)} loaded. Strike the escalation on a fixed price, re-word two risk lines that duplicate it, rule on the overhead basis, strike the double-counted disconnects, pay the battery at delivery."),
 ("Decide after a study (Q1 2027): ",f"{rng(st_lo,st_hi)} loaded. Two feeders instead of four, the relay program at benchmark, civil sized after geotech, a crew build-up for install."),
 ("Outside the estimate, larger than both: ",f"{rng(rev_lo,rev_hi)} of Section 48E credit on the revenue requirement, plus {rng(SVI['C2']['lo_loaded'],SVI['C2']['hi_loaded'])} if the landfill qualifies as an energy community. Owner: Tax."),
 ("Then hold it: ",f"a station-direct design-to-cost target of ${SC['target_kwh']:,} per kWh ($50M loaded), competitive lump-sum pricing before construction, and a monthly number someone owns.")],size=15,gap=8)
notes(s,"The three numbers are the scope-challenge cases (scope_challenge.json). The honest planning range once the Haugland reconciliation and the unpriced exposures are added back is "+rng(net['lo'],net['hi'])+"; it is on slide 9, not here, because the question in the room is what can be done, and the answer is the two groups of decisions plus the target.")

# ---------- 3 Where the dollars come from (bridge) ----------
s=blank(p); n+=1; chrome(s,"Where the dollars come from: a bridge from the approval level to the re-scoped project, loaded",eyebrow="The levers, grouped by what they need",n=n)
steps=[("Rev 3 approval",APPROVAL,None),("Decide now (6 levers)",-(now_lo+now_hi)/2,"A"),("Decide after a study (8 levers)",-(st_lo+st_hi)/2,"B"),("Re-scoped midpoint",None,"T"),("Exposures not yet carried",(expo['lo']+expo['hi'])/2,"X"),("Haugland reconciliation (if half is ours)",(heg['lo']+heg['hi'])/2*SV['marginal_loader'],"X"),("Honest planning midpoint",None,"T")]
cd=CategoryChartData(); cats=[];base=[];up=[];dn=[];tot=[];run=0
for lab,v,k in steps:
    cats.append(lab)
    if k is None: run=v; base.append(0); up.append(0); dn.append(0); tot.append(v/1e6)
    elif k=="T": base.append(0); up.append(0); dn.append(0); tot.append(run/1e6)
    elif v<0: run+=v; base.append(run/1e6); dn.append(-v/1e6); up.append(0); tot.append(0)
    else: base.append(run/1e6); up.append(v/1e6); dn.append(0); run+=v; tot.append(0)
cd.categories=cats
for name,vals in (("base",base),("total",tot),("down",dn),("up",up)): cd.add_series(name,[round(x,3) for x in vals])
gf=s.shapes.add_chart(XL_CHART_TYPE.COLUMN_STACKED,Inches(0.5),Inches(1.5),Inches(8.2),Inches(5.3),cd); ch=gf.chart; style_chart(ch,legend=False,size=10)
ch.series[0].format.fill.background(); ch.series[0].format.line.fill.background()
for sr,col in ((ch.series[1],NAVY),(ch.series[2],TEAL),(ch.series[3],BURG)): sr.format.fill.solid(); sr.format.fill.fore_color.rgb=col
ch.plots[0].gap_width=45; ch.plots[0].overlap=100
ch.value_axis.minimum_scale=30; ch.value_axis.maximum_scale=60; ch.value_axis.major_unit=5; ch.value_axis.has_major_gridlines=True; ch.value_axis.major_gridlines.format.line.color.rgb=MID; ch.value_axis.tick_labels.number_format='"$"0"M"'; ch.value_axis.tick_labels.number_format_is_linked=False; ch.value_axis.tick_labels.font.size=Pt(10)
ch.category_axis.tick_labels.font.size=Pt(9)
for sr in (ch.series[1],ch.series[2],ch.series[3]):
    sr.data_labels.show_value=True; sr.data_labels.number_format='"$"0.0"M";;'; sr.data_labels.number_format_is_linked=False; sr.data_labels.font.size=Pt(10); sr.data_labels.font.bold=True; sr.data_labels.position=XL_LABEL_POSITION.INSIDE_END
ch.series[1].data_labels.font.color.rgb=WHITE; ch.series[3].data_labels.font.color.rgb=WHITE; ch.series[2].data_labels.font.color.rgb=WHITE
table(s,8.9,1.55,3.9,3.4,["Group","Loaded"],[["Decide now, 6 levers",rng(now_lo,now_hi)],["After a study, 8 levers",rng(st_lo,st_hi)],["Subtotal, the estimate",rng(now_lo+st_lo,now_hi+st_hi)],["Exposures to add back","-"+rng(expo['lo'],expo['hi'])],["Haugland gap, direct","-$4 to 8M"],["48E and adder, revenue req.",rng(rev_lo,rev_hi)]],col_w=[2.4,1.5],size=11,align_right=(1,))
text(s,8.9,5.1,3.9,1.8,"Midpoints plotted. Every lever is sized from the Rev 3 line items and loaded at the marginal loader of 1.44 (contingency, basis-driven indirects and AFUDC scale with directs). The two red steps are not levers: they are what must be managed so the savings stick (slide 9).",size=11,color=GRAY)
notes(s,"Bridge built from savings.json and scope_challenge.json. The 'honest planning midpoint' is the net case: re-scoped, plus the exposures the estimate does not carry, plus the Haugland midpoint loaded. The 48E credit is not on the bridge because it reduces the revenue requirement, not the project cost.")

# ---------- 4 Decide now ----------
s=blank(p); n+=1; chrome(s,f"Decide now, before the November PAF: six levers worth {rng(now_lo,now_hi)}, none of which changes scope",eyebrow="Group 1: decisions, no study",n=n)
rows=[[i,SHORT[i],rng(SVI[i]["lo_loaded"],SVI[i]["hi_loaded"]),(f"{int(ODDS[i]*100)}%" if i in ODDS else "with T1"),NEEDS[i],SVI[i]["owner"],DATE[i]] for i in NOW]
rows.append(["","Total",rng(now_lo,now_hi),"","","",""])
t=table(s,0.6,1.5,12.1,4.3,["#","Lever","Loaded","Odds","What it takes","Owner","By"],rows,col_w=[0.45,4.1,1.3,0.7,2.6,2.1,0.85],size=11.5,align_right=(2,3),bold_last=True)
for i,id_ in enumerate(NOW,1):
    c=t.cell(i,0); c.fill.solid(); c.fill.fore_color.rgb=TEAL if id_[0]=="A" else (NAVY if id_[0]=="B" else BURG); c.text_frame.paragraphs[0].runs[0].font.color.rgb=WHITE; c.text_frame.paragraphs[0].runs[0].font.bold=True
bullets(s,0.6,5.95,12.1,1.0,[("The ask: ","approve these six as estimate corrections for the November 2026 PAF. The odds are the simulation's assessed probability of each landing; the expected value of the six is about "+m(sum(SVI[i]['lo_loaded']/2+SVI[i]['hi_loaded']/2 for i in NOW)*0.65)+".")],size=14)
notes(s,"Group 1 is estimate hygiene plus one commercial term (C3). A1: the Nomad price is fixed until Final Acceptance, so the $1.13M escalation on the unpaid balance is not a cost. A2: two risk-register lines describe the same escalation in words. A4: whether the E&S station overhead basis should load a vendor-furnished, vendor-commissioned contract is an Accounting ruling. B5: the Siemens budgetary quote of 12 Aug 2026 includes disconnects, PTs, relays and cabinets in the $300K skid price; Rev 3 carries them again. C3: paying at delivery rather than a year ahead changes AFUDC.")

# ---------- 5 Decide after a study ----------
s=blank(p); n+=1; chrome(s,f"Decide at Gate 1 (Q1 2027): eight levers worth {rng(st_lo,st_hi)}, each closed by a study already on the critical path",eyebrow="Group 2: decisions that need a study",n=n)
rows=[[i,SHORT[i],rng(SVI[i]["lo_loaded"],SVI[i]["hi_loaded"]),(f"{int(ODDS[i]*100)}%" if i in ODDS else "with T1"),NEEDS[i],SVI[i]["owner"],DATE[i]] for i in STUDY]
rows.append(["","Total",rng(st_lo,st_hi),"","","",""])
t=table(s,0.6,1.5,12.1,4.9,["#","Lever","Loaded","Odds","What closes it","Owner","By"],rows,col_w=[0.45,4.1,1.3,0.7,2.6,2.1,0.85],size=11,align_right=(2,3),bold_last=True)
for i,id_ in enumerate(STUDY,1):
    c=t.cell(i,0); c.fill.solid(); c.fill.fore_color.rgb=TEAL if id_[0]=="A" else NAVY; c.text_frame.paragraphs[0].runs[0].font.color.rgb=WHITE; c.text_frame.paragraphs[0].runs[0].font.bold=True
bullets(s,0.6,6.45,12.1,0.6,[("The ask: ","fund and schedule the four studies now (geotech, hosting capacity, two EMA relay actuals, the Haugland scope map) so every one of these is decided before IFC, not discovered after.")],size=14)
notes(s,"Group 2 is value engineering. The biggest single item, B2, is a two-feeder interconnection if the hosting-capacity study says two feeders carry 5 MW each; it removes two breaker skids, two GSUs and two metering sets. B1 benchmarks the 710 man-hours per relay at Station 496 against two recent EMA relay-replacement actuals. B3 is the platform and retaining wall, sized today on a 2.5 ft fill placeholder.")

# ---------- 6 48E ----------
s=blank(p); n+=1; chrome(s,f"The largest lever is not in the estimate: {rng(SVI['C1']['lo_loaded'],SVI['C1']['hi_loaded'])} of Section 48E credit to customers, and nobody owns it yet",eyebrow="Group 3: revenue requirement",n=n)
stat(s,0.6,1.55,3.9,1.9,rng(SVI['C1']['lo_loaded'],SVI['C1']['hi_loaded']),"30% credit, eligible basis","Battery, install, balance of plant ($28M); up to $41M with station, site and testing",vsize=28)
stat(s,4.7,1.55,3.9,1.9,"+"+rng(SVI['C2']['lo_loaded'],SVI['C2']['hi_loaded']),"Energy-community adder","Only if the closed landfill qualifies as a brownfield; not assumed",vsize=28)
stat(s,8.8,1.55,3.9,1.9,"65%","Non-PFE cost ratio","Cell origin on the Voyager units decides whether the credit is zero",vsize=28)
table(s,0.6,3.7,12.1,2.5,["Decision","Owner","By","Why it matters"],[["Eligible-basis opinion: which layers are energy storage property","Tax","Dec 2026","Sets the $28M to $41M range"],["FEOC cost-ratio test on the Nomad cells (Notice 2026-15)","Tax + Sourcing + Nomad","Before final drawings","A failed test is a zero credit"],["Normalization election; DPU treatment of the credit","Regulatory","2027 filing","Decides how fast customers see it"],["Prevailing wage and apprenticeship in the construction contracts","Sourcing + Construction","Gate 3","6% credit becomes 30%"]],col_w=[5.2,2.4,1.5,3.0],size=12)
bullets(s,0.6,6.35,12.1,0.6,[("The ask: ","open the 48E memo with Tax this month. It is larger than every estimate lever combined and it has a construction-start deadline.")],size=14)
notes(s,"Section 48E storage credit for a utility-owned, 2028 construction start: 30% base with prevailing wage and apprenticeship; prohibited-foreign-entity restrictions phased in by begin-construction date; the IRA added an election out of normalization for storage. Confidence medium on the mechanism (law-firm summaries of the July 2025 reconciliation law and Notice 2026-15), low on the dollars until Tax opines. Research pass of 3 Oct 2026 logged in the research log.")

# ---------- 7 Design-to-cost ----------
s=blank(p); n+=1; chrome(s,f"Hold it: a station-direct target of ${SC['target_kwh']:,} per kWh, $50M loaded, with change control and a monthly number",eyebrow="Gate 2: design-to-cost (before IFC, mid-2027)",n=n)
stat(s,0.6,1.55,3.9,2.0,f"${SC['target_kwh']:,}/kWh","Station-direct target",f"${SC['target_direct']/1e6:.0f}M direct: the reference-class 75th percentile for a built project this size",vsize=36)
stat(s,4.7,1.55,3.9,2.0,"$1,483/kWh","Where Rev 3 sits","$29.7M direct, the 77th percentile of 35 built projects at or below 100 MWh",vsize=36)
stat(s,8.8,1.55,3.9,2.0,"$50M","Loaded target","The contained case, held through IFC, construction pricing and in-service",vsize=36)
bullets(s,0.6,3.85,12.1,3.1,[
 ("Why a target and not a forecast: ","an estimate that is re-forecast every revision has moved from $43.9M to $57.2M in three years. A target with change control turns it into a managed number."),
 ("The rule: ","no scope is added without a funded source. A change control board with the CoE decides every addition against the target, in writing."),
 ("The measure: ","station-direct $/kWh against target, forecast at completion, open scope questions, the exposures register. One page, monthly, to the sponsor, until in-service."),
 ("Why this level: ","it is defensible outside the company. A regulator can be told the project was designed to the 75th percentile of what utilities have actually built, and why it stopped where it stopped.")],size=15,gap=8)
notes(s,"Target from scope_challenge.json: the reference-class 75th percentile of station-direct $/kWh, rounded to $50. The reference class is the 35 built projects at or below 100 MWh verified on 5 Oct 2026 via EIA-860M and regulator records. The monthly report is the standing item in the containment plan.")

# ---------- 8 Commercial strategy ----------
s=blank(p); n+=1; chrome(s,"Buy it differently: competitive lump-sum pricing before construction, owner-furnished equipment, a change-order cap",eyebrow="Gate 3: commercial strategy (Q3 2027)",n=n)
table(s,0.6,1.5,12.1,3.9,["Action","What it changes","Owner","By"],[
 ["Competitive lump-sum pricing for station, civil and install: Haugland plus two bidders","Converts a unit-library estimate at 30% engineering into a bid; retires the +25% construction stress test","Sourcing + PM","Q3 2027"],
 ["Owner-furnished GSUs and breaker skids on alliance pricing","Takes contractor markup off $3.8M of equipment; locks the 29 to 70 week transformer lead time","Sourcing + Substation Eng.","Q2 2027"],
 ["Nomad payment milestones aligned to the January 2028 delivery","Removes a year of AFUDC on $12M; protects the siting float","PM + Sourcing + Treasury","Nov 2026"],
 ["Change-order cap and a tariff pass-through clause read before signature","Bounds the $0.6M Nomad change-order exposure in the simulation","Sourcing + Legal","Nov 2026"],
 ["Outage windows at Station 496 priced explicitly","The relay program's outage premium is unpriced today","P&C Eng. + EMA","Gate 1"]],col_w=[4.6,4.4,2.1,1.0],size=12)
bullets(s,0.6,5.55,12.1,1.4,[("The ask: ","approve the contracting strategy at Gate 3 rather than defaulting to the alliance contractor on unit rates. The simulation's two largest accuracy ranges, the civil layer and Station 496, are both unit-library numbers with no bid behind them.")],size=14)
notes(s,"The civil layer (E) and Station 496 (F) carry the widest two-sided accuracy ranges in the integrated Monte Carlo (-$0.9M to +$2.6M and -$1.1M to +$2.0M). A competitive lump-sum converts that range into a contract price. Owner-furnished GSUs and skids match the Siemens budgetary quote of 12 Aug 2026 and the transformer lead-time guidance.")

# ---------- 9 Protect the downside ----------
s=blank(p); n+=1; chrome(s,"Two risks can eat every dollar saved: the Haugland reconciliation and the siting calendar. Both have an owner and a date.",eyebrow="What must be managed so the savings stick",n=n)
s.shapes.add_picture(f"{B}/mc_lead_tornado.png",Inches(0.4),Inches(1.5),width=Inches(7.4))
bullets(s,8.0,1.55,4.8,5.4,[
 ("Haugland reconciliation, +$4 to 8M direct, 58% of the variance. ","Haugland's Class 3 base for overlapping scope is $19.2M; Rev 3 carries $8.3M. Until a signed scope map says which is right, every saving on slides 4 and 5 is provisional. Owner: PM + Cost Estimating + HEG. By: before the November PAF."),
 ("Siting schedule, +5 months at P50, +9 at P80, 14% of the variance. ","Every month costs about $0.37M in AFUDC, escalation and PM. Action: file Article 80 early, pre-brief the abutters on screening and sound, set the ZBA date within 90 days of filing. Owner: Siting + PM. By: Q1 2027."),
 ("Exposures to carry honestly, "+rng(expo['lo'],expo['hi'])+". ","Sound mitigation ($467K dropped from the 2023 estimate), visual screening, police details, NFPA 855 changes, the GSU count. Price them now; a surprise in 2028 costs more than a line today."),
 ("Everything on the left is ours to take. ","No single lever exceeds $2M; together they are worth about "+m(sum(r['ev'] for r in MS['ranked_opportunities']))+" at the assessed odds and "+m(sum(r['full'] for r in MS['ranked_opportunities']))+" if every one lands.")],size=12,gap=7)
notes(s,"Tornado from the integrated Monte Carlo (20,000 trials, mc_scope_schedule.py): each driver's P10 to P90 effect on the loaded total. Variance shares are Spearman contributions to the spread of the managed outcome. The leadership point: the downside is concentrated in two items with owners, the upside is distributed across sixteen items that are mostly decisions.")

# ---------- 10 The plan on a page ----------
s=blank(p); n+=1; chrome(s,"The plan on one page: five gates, each with an owner, a date and the dollars it decides",eyebrow="Save, contain, reduce",n=n)
PLAN=[["Now to the Nov 2026 PAF","The six no-study decisions (A1, A2, A4, A5, B5, C3); sound mitigation and screening priced or registered; the 48E memo opened with Tax","Cost Estimating, PM, Accounting, Tax","Estimate hygiene, about $3M to $5M loaded; the exposures carried honestly"],
["Gate 1, design basis (Q1 2027)","Geotech report; NFPA 855 hazard mitigation analysis; hosting-capacity study for two feeders; GSU count and topology in writing; Haugland-to-Rev 3 scope map signed","Substation Eng., Civil, System Planning, HEG","The two-feeder case ($1.4M to $1.9M), the civil layer, the GSU exposure, the Haugland gap"],
["Gate 2, design-to-cost (before IFC, mid-2027)",f"Station-direct target of ${SC['target_kwh']:,} per kWh and $50M loaded; monthly trend review; change control board with the CoE; no scope added without a funded source","PM (accountable), Cost Estimating, sponsor","Turns the estimate into a managed number instead of a forecast"],
["Gate 3, commercial strategy (Q3 2027)","Competitive lump-sum pricing for station, civil and install (Haugland plus two); owner-furnished GSUs and skids; Nomad milestones aligned to delivery; change-order cap; Station 496 outage windows priced","Sourcing, PM, Construction","Converts unit-library construction into a bid; retires the +25% construction stress test"],
["Standing, monthly to in-service","One-page cost-containment report: station-direct $/kWh against target, forecast at completion, open scope questions, exposures register, the 48E and FEOC milestones","PM, CoE","What leadership sees every month"]]
table(s,0.6,1.5,12.1,5.0,["When","What","Who","What it decides"],PLAN,col_w=[2.1,5.6,2.1,2.3],size=11)
text(s,0.6,6.6,12.1,0.35,f"Target: ${SC['target_kwh']:,} per kWh station-direct (${SC['target_direct']/1e6:.0f}M direct, $50M loaded); the CoE reports the trend monthly from the November 2026 PAF.",size=11,color=GRAY)
notes(s,"The containment plan from scope_challenge.json. The first gate is the November 2026 PAF; it carries the six no-study decisions and the honest exposures. Gate 1 closes the studies. Gate 2 sets the target. Gate 3 sets the contracting strategy. The standing item is the monthly report.")

# ---------- 11 What the plan is worth ----------
s=blank(p); n+=1; chrome(s,f"What the plan is worth: {m(MC['status_quo']['50']-MC['managed']['50'])} at the median if the levers are worked at their odds, {m(MC['status_quo']['50']-MC['ceiling']['50'])} if every one lands",eyebrow="20,000 trials on cost, scope and schedule",n=n)
s.shapes.add_picture(f"{B}/mc_scope_hist.png",Inches(0.5),Inches(1.55),width=Inches(7.2))
table(s,8.0,1.6,4.8,2.3,["Posture","P50","P80","Over $57.2M"],[["Nothing pursued",m(MC['status_quo']['50']),m(MC['status_quo']['80']),f"{MC['status_quo']['p_over_approval']:.0%}"],["Levers at their odds",m(MC['managed']['50']),m(MC['managed']['80']),f"{MC['managed']['p_over_approval']:.0%}"],["Every lever lands",m(MC['ceiling']['50']),m(MC['ceiling']['80']),f"{MC['ceiling']['p_over_approval']:.0%}"]],col_w=[1.8,0.9,0.9,1.2],size=11.5,align_right=(1,2,3))
bullets(s,8.0,4.1,4.8,2.9,[
 ("Read it plainly: ",f"with nothing pursued, {MC['status_quo']['p_over_approval']:.0%} of trials end above the approval level, because the Haugland gap, the unpriced exposures and the schedule are real and the estimate carries none of them."),
 ("With the plan: ",f"the median lands at {m(MC['managed']['50'])} and {MC['managed']['p_under_50']:.0%} of trials come in under $50M."),
 ("The reserve: ","$7.6M of risk and contingency covers the modeled ranges at about P75 only if the plan is executed.")],size=12.5,gap=7)
notes(s,"Integrated Monte Carlo (mc_scope_results.json): base = approval less reserves ($49.6M), plus layer accuracy ranges, plus threats not in the estimate at their odds, plus schedule cost, less the levers at their assessed odds (managed) or at full value (ceiling). Schedule: P50 slip 5 months, P80 9 months, 39% chance of more than 6 months.")

# ---------- 12 Decisions requested (mirror) ----------
s=blank(p); n+=1; rect(s,0,0,W,H,NAVY); rect(s,0,0,W,0.06,GOLD)
text(s,0.6,0.3,12.1,0.3,"DECISIONS REQUESTED TODAY",size=11,bold=True,color=GOLD)
text(s,0.6,0.6,12.1,1.0,f"$57M becomes {rng(resc['lo'],resc['hi'])} through sixteen named levers, three gates and one target. Six of them need only a yes.",size=24,bold=True,color=WHITE,font=HEAD,line_spacing=1.0)
rect(s,0.6,1.9,12.1,4.9,RGBColor(0x0B,0x2A,0x72))
bullets(s,0.85,2.05,11.6,4.7,[
 ("1. Approve the six no-study corrections for the November 2026 PAF ",f"({rng(now_lo,now_hi)} loaded). Owners: Cost Estimating, PM, Accounting, Sourcing."),
 ("2. Fund and schedule the four studies now ","(geotech, hosting capacity, two EMA relay actuals, the Haugland scope map) so the eight study-gated levers ("+rng(st_lo,st_hi)+") are decided before IFC."),
 ("3. Open the Section 48E memo with Tax this month ",f"({rng(SVI['C1']['lo_loaded'],SVI['C1']['hi_loaded'])} on the revenue requirement; FEOC cell-origin test on the Nomad units)."),
 ("4. Adopt the design-to-cost target ",f"(${SC['target_kwh']:,} per kWh station-direct, $50M loaded) with change control and a monthly report from the CoE."),
 ("5. Approve competitive lump-sum pricing of the station, civil and install scope at Gate 3, ","with owner-furnished GSUs and skids."),
 ("6. Assign the two risks that can undo all of it: ","the Haugland reconciliation (PM + Cost Estimating + HEG, before the PAF) and the siting calendar (Siting + PM, Q1 2027).")],size=15,color=WHITE,gap=9,bullet_color=GOLD)
text(s,0.6,7.02,9,0.3,FOOT,size=10,color=MID); text(s,12.0,7.02,0.75,0.3,str(n),size=10,color=MID,align=PP_ALIGN.RIGHT)
notes(s,"Mirror of the open. This slide stays up during discussion. Each decision maps to a gate on slide 10 and to a row in the savings register in the workbook.")

# ---------- A. Backup: the full register ----------
s=blank(p); n+=1; chrome(s,f"Backup: the sixteen levers as sized from the Rev 3 line items",eyebrow=f"Appendix: savings register, {rng(SVT['A']['lo_loaded']+SVT['B']['lo_loaded'],SVT['A']['hi_loaded']+SVT['B']['hi_loaded'])} on the estimate, {rng(SVT['C']['lo_loaded'],SVT['C']['hi_loaded'])} on the revenue requirement",n=n)
rows=[[i["id"],i["title"],i["layer"],rng(i["lo"],i["hi"]),rng(i["lo_loaded"],i["hi_loaded"]),i["conf"],i["owner"]] for i in SV["items"]]
t=table(s,0.6,1.5,12.1,5.0,["#","Lever","Layer","Direct","Loaded","Conf.","Owner"],rows,col_w=[0.4,5.3,0.6,1.2,1.3,0.8,2.5],size=8,align_right=(3,4))
for i,it in enumerate(SV["items"],1):
    c=t.cell(i,0); c.fill.solid(); c.fill.fore_color.rgb={"A":TEAL,"B":NAVY,"C":BURG}[it["tier"]]; c.text_frame.paragraphs[0].runs[0].font.color.rgb=WHITE; c.text_frame.paragraphs[0].runs[0].font.bold=True
text(s,0.6,6.6,12.1,0.4,"Full basis, evidence lines and what must close for each lever: Hyde Park BESS Cost Analysis Deck slides 27 to 36, Whitepaper section 8, Workbook tabs Savings Register and Scope Challenge.",size=11,color=GRAY)
notes(s,"Backup only.")

out=f"{B}/Hyde_Park_BESS_Leadership_Brief.pptx"; p.save(out); print("saved",out,"slides",n)
