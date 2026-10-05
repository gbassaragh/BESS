import sys, json
sys.path.insert(0,"/tmp/claude-0/-home-user-BESS/078f934e-4ca0-5169-be3f-cb66ff0e2514/scratchpad/build")
from docx_common import *
B="/tmp/claude-0/-home-user-BESS/078f934e-4ca0-5169-be3f-cb66ff0e2514/scratchpad/build"
D=json.load(open(f"{B}/data.json")); L=D["layers_direct"]; LD=D["layers_loaded"]
R=json.load(open(f"{B}/stats_results.json")); RC=R["reference_class"]; RCU=R["reference_class_utility"]; P=R["ols_parsimonious"]; AJ=json.load(open(f"{B}/adjust_results.json")); CL=AJ["classes"]["reference_class"]["indices"]; k_=lambda v: f"${v:,.0f}"
LX=json.load(open(f"{B}/layer_index_results.json")); LXM=LX["classes"]["reference_class"]["methods"]; LXF=LX["factors"]["2018"]; LXR=LX["series_ratio_2018"]; LJ=json.load(open(f"{B}/indices_layers.json")); SV=json.load(open(f"{B}/savings.json")); SVT=SV["tiers"]; IT=SV["itc"]; SC=json.load(open(f"{B}/scope_challenge.json"))
_m=lambda v: f"${v/1e6:.1f}M"; _rng=lambda a,b: (f"${a/1e6:.1f}M" if abs(a-b)<5e4 else f"${a/1e6:.1f} to {b/1e6:.1f}M")
import os as _os, numpy as _np
_api=json.load(open(f"{B}/indices_layers_api.json")) if _os.path.exists(f"{B}/indices_layers_api.json") else {}
def _cagr(key,y0,y1):
    pts=_api.get(key,{}).get("points") or LJ["series"][key]["points"]; xs=sorted(int(k) for k in pts); f=lambda y: float(_np.interp(y,xs,[float(pts[str(x)]) for x in xs]))
    return (f(y1)/f(y0))**(1/(y1-y0))-1
d=new_doc()
# ---------- Title ----------
p=para(d,"Basis of Estimate",bold=True,size=22,color=NAVY,after=2); p.alignment=WD_ALIGN_PARAGRAPH.LEFT
para(d,"Hyde Park Battery Energy Storage System, Station 360 and Station 496",size=13,color=BURG,after=2)
para(d,"Project 21334 (D SS), Work Order 80089926. Companion project 24211 (D Line) referenced for the all-in view.",size=10,color=GRAY,after=10)
table(d,["Field","Value","Field","Value"],[
 ["Date of estimate","24 Sep 2026 (ESF Total Rev 3)","Region","Eversource EMA, Boston (Hyde Park / Roslindale)"],
 ["Project name","Hyde Park BESS","Project number","21334 (D SS); 24211 (D Line, memo only)"],
 ["Work order","80089926","Estimate name","Hyde Park BESS - Sta. 360 - Rev 3; Sta. 496 - Rev 2"],
 ["Project manager","Robert Herman (Adam Kelley through PF Rev 3)","Project estimator","Brian Roche; lead review Justin Niderno; peer review PAG, D. Piccorelli"],
 ["Estimate class","Conceptual, -25% / +50% (ESF)","In-service date","28 Dec 2028"],
 ["Approval-level total, 21334","$57,247,300","Actuals to 23 Sep 2026","$5,222,045 (21334)"],
 ["BOE prepared by","Cost Estimating Center of Excellence","BOE date","29 Sep 2026; benchmark section revised 2 and 5 Oct 2026; escalator check and savings register added 3 Oct 2026"],
],widths=[1.3,2.0,1.3,2.0])
callout(d,"Reading this document.","This Basis of Estimate follows the Eversource Estimate Basis Document template (rev 1) heading by heading. Every dollar figure carries its source: the ESF Total Rev 3 workbook (Item, Summary and Overview tabs), the Nomad cover agreement dated 10 Mar 2026, the E-23-373 conceptual estimate of 8 Dec 2023, the July 2023 indicative pricing, the PAF Rev 3 approved 25 Jun 2026, and the project email record of 12 Aug to 23 Sep 2026. Confidence tags (High, Medium, Low) mark the quantitative claims that carry weight in a leadership setting.")
# ---------- 1 General ----------
d.add_heading("1. General Estimate Information",1)
d.add_heading("1.1 Estimate purpose",2)
para(d,"The estimate supports the Full Funding Project Authorization Form (PAF) for the Hyde Park BESS, planned for the Eversource Project Approval Committee (EPAC) in November 2026 per PAF Rev 3, and replaces the $43,926K conceptual placeholder that has been carried since the E-23-373 estimate of December 2023. The estimate also serves a second purpose that this document treats explicitly in Section 3: separating the battery supply contract from the station, site, interconnection and owner costs so that leadership can compare the project against published industry benchmarks on a like-for-like basis.")
d.add_heading("1.2 Update to previous estimate",2)
para(d,"Rev 3 is the fourth revision in a five-week cycle that began when the project team requested a re-estimate against the 30 Jun 2026 scope of work. The sequence and its drivers are in the table below. Confidence: High (ESF revision files and the email record).")
table(d,["Revision","Date","Approval level","Change","Driver"],[
 ["Rev 0","26 Aug 2026","$47,201,100","","Station 360 rebuilt from E-23-373 quantities and the 28 Jul 2023 indicative pricing; battery material carried at about $6M."],
 ["Rev 1","1 Sep 2026","$51,867,100","+$4,665,900","Battery material increased at project team request."],
 ["Rev 2","10 Sep 2026","$63,640,300","+$11,773,200","Battery line reset to the Nomad cover agreement and escalated to $13,119,867; $1,545,014 of 'relays, P&C systems for batteries' carried from 2023 Company 1 pricing; three station service transformers; engineering hours from E-23-373."],
 ["Rev 3","24 Sep 2026","$57,247,300","-$6,393,000","Relay line deleted as a duplicate of the $300K-per-breaker Siemens price (P&C Engineering, 22 Sep); station service transformer quantity 3 to 1; engineering re-based to $501,000 to go plus actuals (18 Sep); actuals updated to 23 Sep; battery line set to the contract balance."],
],widths=[0.6,0.8,1.0,0.9,3.3],num_cols=(2,3))
para(d,"Against the $43,926K full-funding placeholder, Rev 3 is $13,321K higher (30.3%). The placeholder was built on July 2023 indicative pricing with an April 2027 in-service date. Rev 3 carries a contracted battery price, a December 2028 in-service date, two more years of escalation, the Station 496 protection scope that E-23-373 did not price, and a risk register sized against a landfill site. Section 4 walks the difference.")
d.add_heading("1.3 Benchmark discussion",2)
para(d,"The project sits well above published all-in benchmarks on a $/kWh basis and roughly at the vendor-quote benchmark on a battery-only basis. That gap is the subject of the companion whitepaper. The numbers that matter for the comparison are these, all at 10 MW / 20 MWh (Confidence: High for the project figures; the benchmark figures and their sources are tabulated in the whitepaper):")
table(d,["Cost boundary","Total","$/kW","$/kWh","Multiple of vendor quote"],[
 ["Vendor fixed-price contract (Nomad, Exhibit C)","$12,106,850","$1,211","$605","1.00x"],
 ["Battery system installed, direct (layers A+B+C)",d0(L["A. Battery supply contract (Nomad)"]+L["B. Battery installation & integration (owner scope)"]+L["C. Battery balance-of-plant (GSUs, EMS/comms, aux power)"]),f"${(L['A. Battery supply contract (Nomad)']+L['B. Battery installation & integration (owner scope)']+L['C. Battery balance-of-plant (GSUs, EMS/comms, aux power)'])/10000:,.0f}",f"${(L['A. Battery supply contract (Nomad)']+L['B. Battery installation & integration (owner scope)']+L['C. Battery balance-of-plant (GSUs, EMS/comms, aux power)'])/20000:,.0f}",f"{(L['A. Battery supply contract (Nomad)']+L['B. Battery installation & integration (owner scope)']+L['C. Battery balance-of-plant (GSUs, EMS/comms, aux power)'])/12106850:.2f}x"],
 ["Station 360 approval level (loaded)","$49,994,200","$4,999","$2,500","4.13x"],
 ["Project 21334 approval level (Sta 360 + Sta 496)","$57,247,300","$5,725","$2,862","4.73x"],
 ["All-in incl. D-Line 24211 conceptual (memo)","$62,040,300","$6,204","$3,102","5.12x"],
],widths=[2.9,1.1,0.8,0.8,1.0],num_cols=(1,2,3,4))
para(d,"A small, distribution-connected, urban, landfill-sited, utility-owned two-hour system carries fixed costs (a switching station, feeder protection at the source station, siting under Article 80, a 200 ft by 200 ft platform on a capped landfill, corporate indirects and AFUDC) that do not scale with MWh. Published benchmarks are dominated by 100 MW-class, four-hour, developer-built projects on greenfield sites. The whitepaper sets out which benchmark boundary each of the rows above should be compared against.")
para(d,f"Reference class (companion statistical memo, 2 October 2026; restricted to built projects 5 October 2026, {R['status_counts']['not_built']} unbuilt rows excluded). Against {RC['n']} built public projects at or below 100 MWh with an all-in disclosed cost ({RC['n_utility']} utility-owned, {RC['n_developer']} developer-owned; median {k_(RC['median_kwh'])}/kWh, interquartile {k_(RC['q25'])} to {k_(RC['q75'])}), the installed battery (boundary 3, $833/kWh) ranks at the {RC['hp_rank']['b3']:.0%} percentile, the station-complete direct cost (boundary 4, $1,483/kWh) at the {RC['hp_rank']['b4']:.0%} percentile ({RCU['hp_rank']['b4']:.0%} within the {RCU['n']} utility-owned members, median {k_(RCU['median_kwh'])}), and the approval level above every member. A log-log regression on {P['n']} public projects (size elasticity {P['coef']['ln_mwh']['b']:+.2f}, duration elasticity {P['coef']['ln_dur']['b']:+.2f}, year not significant) predicts {k_(P['hp_pred_kwh']['p50'])}/kWh for a 20 MWh, two-hour project in 2028 with an 80 percent prediction interval of {k_(P['hp_pred_kwh']['pi80_lo'])} to {k_(P['hp_pred_kwh']['pi80_hi'])}; boundary 4 sits at the {P['hp_percentile']['b4']:.0%} percentile of that distribution. Re-based to 2026 dollars (battery share back-cast to the project's own year and deflated on a published index, remainder on the Handy-Whitman utility construction index) the class median is {k_(min(CL[k]['by_owner']['median'] for k in ('installed','pack','turnkey','nrel')))} to {k_(max(CL[k]['by_owner']['median'] for k in ('installed','pack','turnkey','nrel')))} and the boundary 4 percentile {min(CL[k]['by_owner']['hp_pct']['station_direct'] for k in CL):.0%} to {max(CL[k]['by_owner']['hp_pct']['station_direct'] for k in CL):.0%}. Confidence: Medium; the public figures are search-excerpt retrievals with per-row confidence tags and the developer-owned members are gross of incentives.")
para(d,f"Escalator check (3 October 2026; memo section 3.4, whitepaper 5.3). Re-basing the comparables with one published index per cost layer instead of one construction index (IBEW Local 103 rate for labor-driven layers, BLS PPI for transformers and for switchgear, ENR CCI for civil, PPI engineering services for owner soft costs) leaves the class median at {k_(LXM['layer_developer']['median'])}/kWh and Hyde Park's station-direct percentile at {LXM['layer_developer']['hp_pct']['station_direct']:.0%}, the same as the two-component model. A 2018 project with this project's physical scope costs {LXF['hp_composite']:.2f}x in 2026 dollars and a 2016 one {LX['factors']['2016']['hp_composite']:.2f}x (quantities held fixed; the review challenge of 5 Oct 2026 that older batteries were far dearer is reflected); the non-battery series rose {min(LXR[k] for k in ('labor','civil','engineering','switchgear','transformer')):.2f}x to {max(LXR[k] for k in ('labor','civil','engineering','switchgear','transformer')):.2f}x since 2018 while the installed battery index fell to {LXR['bat_installed']:.2f}x. (Confidence: High for the BLS series, pulled from the FRED and BLS APIs; Medium for ENR and IBEW from published tables.)")
# ---------- 2 Scope ----------
d.add_heading("2. Scope",1)
d.add_heading("2.1 Station (Station 360, new 13.8 kV BESS station)",2)
bullets(d,[
 "Develop a new 200 ft x 200 ft station site at 401-433 Cummins Highway on Eversource-owned property (the former Barry construction-debris landfill); 2.5 acres clear and grub, 1.75 acres cleared for a 760 ft x 20 ft access road with curb cut.",
 "Twelve Nomad Voyager 3.0 (Eagle) LFP battery units with PCS, BMS and fire protection, 10 MW / 20 MWh, 12 MVA, 6 MVAr, on twelve 251 in x 108 in foundation pads. Furnished under the Nomad cover agreement; installed by others with Nomad field assembly supervision.",
 "Four 15 kV Siemens SDV7 standalone 1,200 A breaker skids with foundations. Each skid includes the breaker, frame, disconnects, PTs, relays, control cabinet and DC battery at $300K each (Siemens budgetary, +/-30%, 12 Aug 2026). No control house.",
 "Four 3 MVA 13.8 kV / 480 V pad-mount generator step-up transformers with pads; one 1,500 kVA 13.8 kV / 480 V station service transformer; four metering transclosures; eight 45 ft wood riser poles; 2,750 ft of 250 MCM 15 kV cable riser-to-GSU; 2,000 ft of 4/0 600 V cable GSU-to-BESS; 2x2 duct bank from riser poles to the GSUs (440 ft) and to the feeder connection manholes (800 ft).",
 "Ground grid, station lighting, 800 ft perimeter fence, two vehicle gates and a main gate, control cabinets and 10,000 ft of control cable, telecom conduit, 280 ft of 14 ft formed retaining wall, trap rock surfacing over 4,900 SY.",
 "Interconnection to four Hyde Park 13.8 kV feeders: 496-H1XY, 441-1401H, 362-1207H and 362-1209H, one 2.5 MW / 5 MWh block per feeder.",
])
d.add_heading("2.2 Station (Station 496 Hyde Park, feeder protection)",2)
bullets(d,[
 "Install four SEL-351S feeder relays, four SEL-351S transformer relays, four SEL-751 feeder relays, four SEL-751 transformer relays, four SEL-735 transformer relays and eight relay plates; remove four SEL-551 feeder, four SEL-551 transformer, four ABB REF610 feeder and four ABB REF610 transformer relays.",
 "SCADA point lists for the RTU (Orion+ or similar) and the SEL RTAC/AXION devices; transfer trip signaling between Station 496 and the Station 360 feeders over dedicated dark fiber.",
 "Key quantity 20 relays; $362,700 per relay at approval level.",
])
d.add_heading("2.3 Line (D Line, project 24211, memo)",2)
para(d,"Not in the 21334 estimate. Per the SSF of February 2024: extend the four feeders 5,465 ft to the Cummins Highway property with three 6 ft x 10 ft x 8 ft manholes, 1,270 ft of six 5 in EB conduit encased in concrete, removal of 13,065 ft of 15 kV cable and installation of 16,395 ft of 3-700 FS 15 kV cable across 47 sections. Conceptual cost $4,793,000 (-25% / +50%). Partial funding of $2,085K approved by MPAC on 5 Aug 2024. The Haugland Class 3 preliminary estimate of September 2026 prices a duct bank of eight 6 in ducts over 10,160 ft, which is larger than the SSF configuration; the D Line estimate has not been re-based and is carried here as a memo item only. Confidence: Low on the D Line figure.")
d.add_heading("2.4 Other",2)
para(d,"Estimate excludes duct bank costs outside the substation (carried under 24211), spot generation (removed from E-23-373 scope by the project team on 12 Aug 2026, although the SSF and PAF state that 2 to 8 MW of spot generation is required if the BESS misses its need date; ownership of that cost is unassigned), a control house (none per Substation Solutions Engineering, 19 Aug 2026), sound walls (carried as a risk, not a scope item), and any augmentation, long-term service agreement or O&M.")
# ---------- 3 Layer extraction ----------
d.add_heading("3. Cost Layer Extraction: Battery versus Station versus Interconnection",1)
para(d,"Every one of the 292 Rev 3 line items was assigned to one of thirteen layers. The assignment is reproducible from the 'Line Items' tab of the companion workbook and reconciles to the $57,247,544 unrounded grand total. Directs are shown as estimated. The 'Loaded' column spreads Station 360 risk, contingency, indirects and AFUDC over the Station 360 direct layers pro rata (load factor 1.6853); Station 496 is carried whole at its own approval level. Confidence: High on the totals; Medium on the boundary between layers B, C and D, which is a judgment about what a vendor 'turnkey' quote would normally include.")
rows=[]
cum=0
for kk in sorted(LD.keys()):
    cum+=LD[kk]; rows.append([kk, d0(L[kk]), f"{L[kk]/57247544:.1%}", d0(LD[kk]), f"{LD[kk]/57247544:.1%}"])
for kk in ["J. Risk register","K. Contingency","L. Indirects / overheads","M. AFUDC"]:
    rows.append([kk, d0(L[kk]), f"{L[kk]/57247544:.1%}", "(spread)", ""])
rows.append(["**Total, project 21334", "**$57,247,544","**100%","**$57,247,544","**100%"])
table(d,["Layer","Direct","%","Loaded","%"],rows,widths=[3.4,1.0,0.6,1.0,0.6],num_cols=(1,2,3,4),font=9)
para(d,"What each layer contains:")
bullets(d,[
 ("A. Battery supply contract. ","Nomad fixed price $12,106,850: $10,638,000 for twelve Voyager units with PCS, BMS and fire protection; $125,000 spares; $797,850 warranty years 3-7; $210,000 remote support; $90,000 shipping; $246,000 field supervision, commissioning and training. Rev 3 carries $1,213,043 of LNTP actuals (two 5% milestones) plus $11,778,062 to go, which is the $10,647,808 contract balance escalated at 3% per year to 2027-28."),
 ("B. Battery installation and integration. ","5,557 manhours of installation labor (the line note applies 25% of the 16,801 mh E-23-373 site total, 4,200 mh, and the quantity of 2 raises the line to 5,557 mh), twelve foundation pads, fire suppression furnish and install, twelve 4 in GRC conduit runs and 2,000 ft of 600 V cable from the GSUs to the units."),
 ("C. Battery balance of plant. ","Four 3 MVA GSUs ($241,029 each from the 2023 bidder list plus 3% per year) with pads and installation, site communications/EMS ($237,922), AC/DC auxiliary power panels. A developer's turnkey quote normally bundles these with the battery."),
 ("D. Station 360 switching and interconnection facilities. ","Four Siemens breaker skids, disconnects, metering transclosures, station service transformer, riser poles, 15 kV cable and terminations, duct bank to the feeder manholes, ground grid and grounding transformers, lighting, control cable, switching and tagging, traffic control."),
 ("E. Site development and civil. ","Clear and grub, access road, 36 soil borings, 2,520 CY cut, 570 CY imported fill, trap rock surfacing, fence and gates, retaining wall, mobilization and demobilization."),
 ("F. Station 496 protection upgrades. ","The full $7,253,100 approval level of the Sta 496 Rev 2 estimate, of which $1,814,500 is testing and commissioning and $1,389,400 is construction labor for 20 relay replacements."),
 ("G. Testing and commissioning (Sta 360). ","1,600 mh lead commissioning engineer, 3,200 mh field test engineers, 1,650 mh field SCADA, 120 mh field telecom."),
 ("H. Owner soft costs. ","Engineering $895,100 (of which $501,000 to go per Substation Engineering, 18 Sep 2026); siting $1,255,600 including $1,052,144 external application and legal for Article 80 and the Zoning Board of Appeal; environmental $179,200; outreach $291,000; project management team $1,796,300 including construction reps; land $3,100."),
 ("I. Taxes, CWIP and insurance. ","Property tax actuals $38,348, CWIP distribution $525,184, sales and use tax on external material $58,459, builders all-risk insurance $165,542 at 0.7% of material, labor and equipment."),
])
# ---------- 4 Quantity basis ----------
d.add_heading("4. Quantity Basis",1)
table(d,["Discipline","Basis","Source","Confidence"],[
 ["Civil","200 ft x 200 ft yard, 760 ft road, 2.5 + 1.75 acres clearing, 2,520 CY cut, 280 ft retaining wall, 4,900 SY trap rock","Estimator take-off from concept drawing C-001 and the 30 Jun 2026 scope of work; constructability review 4-6 Aug 2026","Medium: Haugland's Class 3 take-off reads the retaining wall at 135 ft x 10 ft and the BESS area at 17,040 SF versus 36,100 SF; both reconciliations are open"],
 ["Structural / foundations","12 battery pads 251 in x 108 in; 4 GSU pads 6.6 CY; 4 breaker pads 6.81 CY; 1 SSVT pad; 4 transclosure pads; 1 SCADA cabinet pad","Nomad unit dimensions; Eversource standard D-station foundation units","Medium: platform depth on the landfill cap is a 2.5 ft placeholder pending geotechnical investigation"],
 ["Buildings","None. No control house.","Substation Solutions Engineering, 19 Aug 2026","High"],
 ["Substation electrical","4 breakers, 8 disconnects, 4 GSUs, 1 SSVT, 4 transclosures, 8 riser poles, cable lengths per estimator","Station one-line 25 Aug 2026; Siemens budgetary price; project team answers 12-20 Aug 2026","Medium: the 25 Aug one-line shows twelve GSUs; the scope of work and the estimate carry four. Haugland priced twelve and books a $632,000 deduct if four governs"],
 ["Line","Riser-to-manhole duct bank only (800 ft); circuit extension is under 24211","Scope of work","High for 21334 boundary"],
 ["P&C (Sta 496)","20 relays, 8 plates, RTU/RTAC points, dark fiber transfer trip","P&C Engineering scope, Sta 496 Rev 2","Medium"],
],widths=[1.1,2.3,1.7,1.7],font=9)
# ---------- 5 ROW / Real estate ----------
d.add_heading("5. ROW / Easements / Land",1)
para(d,"Eversource owns the parcel. Actuals of $3,110 for easement and land services are carried; no purchase is required. The MWRA sewer easement crossing the site constrains the duct bank alignment; Haugland carries a $129,888 to $140,088 re-route exposure if the easement instrument places the duct bank outside the priced alignment. No allowance is carried in Rev 3 for that exposure beyond the risk register.")
# ---------- 6 Environmental ----------
d.add_heading("6. Environmental Approvals / Permits",1)
para(d,"Internal environmental 160 mh and contractor environmental 160 mh from E-23-373, plus the following permit actions priced by hours: City of Boston zoning relief and permits (40), MassDEP post-closure use permit for construction on a closed landfill (40), EPA 2022 Construction General Permit eNOI (24) with SWPPP development and inspections (80), MassDEP Tier II reporting for batteries (24), soil sampling and a soil management plan (120). Legal environmental actuals $70,700 and permit fees $10,303. Resources: Eversource with contractor support. Risk register carries $300,000 for additional DEP requirements and landfill closure document review and $300,000 for unexpected remediation.")
# ---------- 7 SCS ----------
d.add_heading("7. SCS Outreach",1)
para(d,"Actuals $84,801 plus 480 mh internal and 480 mh contractor to go, and a traditional outreach campaign allowance of $91,690 (internal $36,676, external $55,014) from the ESF template. The neighborhood has raised loss of open land, visual impact near the shopping plaza and traffic; screening and buffering for the abutting residential neighborhood is expected. Risk register carries $250,000 for additional outreach.")
# ---------- 8 Siting ----------
d.add_heading("8. Siting Approvals / Permits",1)
para(d,"Article 80 Small Project Review by the Boston Planning Department and a Conditional Use Permit from the Zoning Board of Appeal, filed with outside counsel. If the City does not grant relief, a zoning exemption petition to the EFSB would take 18 to 24 months. Rev 3 carries siting at $1,255,600 for Station 360: actuals $74,903, 180 mh internal, an internal application allowance of $116,905 and an external application and legal allowance of $1,052,144. The P6 schedule of 3 Aug 2026 shows siting determination in February 2028 after the Article 80E (7 months) and ZBA (5 months) reviews, and construction cannot start in the public way before that determination and the winter moratorium. Risk register carries $250,000 for siting and permitting delay.")
# ---------- 9 Engineering ----------
d.add_heading("9. Engineering / Design",1)
para(d,"Internal oversight with external detail design. Station 360 engineering is carried at $895,100: actuals of $388,000 to 23 Sep 2026 plus $501,000 to go per the Substation Engineering email of 18 Sep 2026, distributed as civil 80 + 80 mh, station 360 + 1,050 mh, P&C 440 + 900 mh, SCADA 120 + 160 mh, telecom 80 + 80 mh, drafting 380 mh (internal + contractor). Labor rates are the 2026 ESF template rates for EMA station work. Station 496 engineering is 440 mh ($61,200). The PAF Rev 3 partial funding separately authorized $1,500,000 of Leidos and $59,300 of VHB external engineering to IFC and $402,062 of internal engineering hours (6,433 hours); those authorizations are part of the actuals-plus-to-go figure above, not additional to it. Confidence: Medium. Engineering at 1.6% of the approval level is low for a first-of-a-kind distribution BESS station; the 12 Sep 2026 engineering comments flagged that the E-23-373 hours were carried in full on top of actuals ('are we double dipping'), which the 18 Sep re-base corrected.")
# ---------- 10 Material ----------
d.add_heading("10. Equipment / Material Pricing",1)
table(d,["Item","Qty","Price basis","Amount in Rev 3"],[
 ["Nomad Voyager 3.0 BESS, 12 units","1 LS","Cover agreement 10 Mar 2026, Exhibit C fixed price $12,106,850; SOV 8 Dec 2025. Rev 3 carries balance after $1,213,043 paid, escalated 3%/yr","$11,778,062 + $1,213,043 actual"],
 ["Siemens SDV7 15 kV 1,200 A breaker skids","4","Siemens budgetary +/-30%, $300,000 each incl. relays, PTs, DC battery, cabinet, disconnects (12 and 20 Aug 2026), escalated","$1,327,379"],
 ["3 MVA 13.8 kV/480 V GSU, pad mount","4","2023 bidder list $882,302 for four, +3%/yr = $964,116 ($241,029 each), escalated","$1,066,456"],
 ["1,500 kVA station service transformer","1","Maximo item 534534","$87,657"],
 ["Metering transclosures","4","ESF unit library","$152,649"],
 ["Communications / EMS","1","2023 bidder list $217,733 +3%/yr","$263,177"],
 ["AC/DC panels, aux power","1","2023 bidder list $56,030 +3%/yr","$67,725"],
 ["Grounding transformers and grid","1 + 4,400 ft","2023 bidder list $123,768 +3%/yr less $30,244 grid material shown separately","$116,146 + $32,569"],
 ["Fire suppression","1","2023 bidder list $68,640 +3%/yr","$86,952 (carried under construction 07)"],
 ["15 kV cable, 600 V cable, terminations, elbows, conduit, duct bank, poles, fence, lighting","various","ESF unit library and estimator lengths","see Line Items tab"],
],widths=[2.0,0.5,3.0,1.3],font=9)
para(d,"Two items are flagged for the full-funding cycle. First, the battery line is escalated by $1,130,255 (10.6%) although Exhibit C fixes the price until Final Acceptance; the lead estimator raised the point on 23 Sep 2026 and the PM elected to leave escalation in place. Second, the $246,000 labor component of the Nomad SOV (field assembly supervision $36,000, testing and commissioning $180,000, training $30,000) is not visible as a separate line; the to-go figure is built from the $11,860,850 material total. Confidence: High on both observations.")
# ---------- 11 Construction ----------
d.add_heading("11. Construction Approach",1)
bullets(d,[
 ("Resources. ","Civil and electrical construction external (Haugland Energy Group is the Strategic Sourcing Partner under a T&M preconstruction engagement of $607,583 authorized in PF Rev 3). Battery unit installation by others with Nomad supervision. Cable pulling and termination for the distribution extension by internal resources per the constructability review. Switching and tagging internal, 32 mh."),
 ("Pricing basis. ","ESF unit manhours and 2026 EMA contractor rates; no competitive construction bid yet. Haugland's Class 3 preliminary (30%) estimate, Scenario B, carries a base of $19,216,899 for its scope, which includes the distribution tie-in and platform work on the landfill cap. That figure has not been reconciled to the Rev 3 construction layers (D + E + B installation, $8.3M direct) and the scope boundaries differ; reconciliation is the first action for full funding."),
 ("Work week. ","Straight time, 8-hour days, five days. No outage premium, night or weekend switching support carried. If outage windows require night or weekend work, affected hours move from a 1.35 to a 1.70 factor (Haugland item 24)."),
 ("Site supervision and indirects. ","Construction manager 1,548 mh (9 months x 4.3 weeks x 40 hours) plus actuals $89,382; contractor PM 2,172 mh; mobilization and demobilization $156,741 each."),
 ("Field commissioning. ","See Section 12."),
 ("Heavy haul. ","Container shipping and unloading is inside the Nomad price ($90,000). Crane class for container setting is priced by Haugland as a 250-300 ton all-terrain unit over 34 days pending the pick radius."),
 ("Misc. ","Traffic control $11,593; police details are in the Haugland base (400 hours) and not in Rev 3."),
])
# ---------- 12 Testing ----------
d.add_heading("12. Testing / Commissioning",1)
para(d,"External. Station 360: LCE 1,600 mh (50% of field test engineering), field test engineers 3,200 mh from E-23-373, field SCADA 1,650 mh, field telecom 120 mh; $1,262,900. Station 496: $1,814,500 for relay replacement testing and commissioning. Nomad's own commissioning (two people, five days per unit, twelve units, $180,000) is inside the contract price. Battery system commissioning ownership is excluded from Haugland's scope and the 63-day system commissioning window is Eversource's (Haugland item 23); no separate owner cost for that window is carried beyond the hours above.")
# ---------- 13 PMT ----------
d.add_heading("13. PMT Project Management Team",1)
para(d,"$1,796,300 for Station 360: PM actuals $413,557 plus 1,278 mh; contractor PM actuals $207,014 plus 2,172 mh and $188,729 of APM actuals; construction manager $355,648; project controls $228,465; system planning $56,633; estimating $19,915; contracts and purchasing $11,934; asset management, vegetation management. Station 496: $96,900.")
# ---------- 14 Schedule ----------
d.add_heading("14. Milestones / Schedule / Escalation Basis",1)
table(d,["Milestone","Date","Source"],[
 ["Preliminary design complete","Sep 2026","PAF Rev 3"],
 ["EPAC full funding","Nov 2026 (P6 of 3 Aug 2026 shows Jan 2027)","PAF Rev 3; P6"],
 ["Nomad FAT complete","26 Nov 2027","Cover agreement Attachment C-2"],
 ["Siting determination (Article 80E + ZBA)","Feb 2028","PAF Rev 3; P6"],
 ["Equipment delivery to site","28 Jan 2028","Attachment C-2"],
 ["Construction start (civil)","Feb 2028","PAF Rev 3"],
 ["Nomad final acceptance","14 Aug 2028","Attachment C-2"],
 ["In-service date","28 Dec 2028","ESF; PAF Rev 3"],
],widths=[2.6,2.0,2.2])
para(d,"In-service date history: Q3 2025 (IFR, June 2021); 23 Apr 2027 (E-23-373, Dec 2023); Sep 2027 (SSF, Feb 2024); Aug 2028 (PF Rev 2, Jan 2026); 28 Dec 2028 (PF Rev 3, Jun 2026, after a four-month BESS re-bid). Escalation of $2,948,100 is included in the approval level ($2,622,100 Sta 360; $326,100 Sta 496) at the ESF template rates applied to the 2026-2028 spend curve. Escalation on the fixed-price battery balance is discussed in Section 10.")
para(d,f"Template rate against the published series (3 October 2026). The ESF template escalates at about 3 percent a year. Over 2023 to 2026 the series that fit this estimate's layers ran: BLS PPI power and distribution transformers {_cagr('transformer',2023,2026):.1%} a year, PPI switchgear and switchboard {_cagr('switchgear',2023,2026):.1%}, IBEW Local 103 journeyman base {_cagr('labor',2023,2026):.1%}, ENR Construction Cost Index {_cagr('civil',2023,2026):.1%}, PPI engineering services {_cagr('engineering',2023,2026):.1%}. The template rate is right for labor, civil and engineering and light for switchgear: the breaker package in layer D is the line to re-quote rather than escalate (savings register B5). The GSU line, priced from a July 2023 bidder list plus 3 percent a year, has tracked the transformer index over that span; the exposure there is lead time (29 to 70 weeks reported for three-phase pad-mounts in 2026) rather than price. (Confidence: High for the series; the comparison is a check on the template, not a change to the estimate.)")
# ---------- 15-16 Removals / other ----------
d.add_heading("15. Removals",1)
para(d,"$123,500 at Station 496 for the sixteen relays removed. None at Station 360 beyond clearing.")
d.add_heading("16. Other Costs (Sales and Use Tax, CWIP, Property Tax)",1)
para(d,"Sales and use tax on external material $58,459; CWIP set to yes per lead review (25 Aug 2026), $525,184 Sta 360; property tax actuals $38,348; Sta 496 other $76,400.")
d.add_heading("17. BAR Basis",1)
para(d,"Builders all-risk at 0.7% of material, labor and equipment for stations, $165,542. Deductibles of $250,000 to $500,000 are carried in the risk register at $250,000.")
# ---------- 18 Risks ----------
d.add_heading("18. Risks / Contingency",1)
para(d,"Risk register, Station 360, $5,300,000 (Confidence: Medium; the values are estimator judgments, not a quantified Monte Carlo):")
table(d,["Risk","Amount","Basis"],[[kk,d0(v),""] for kk,v in D["risk_items_360"].items()]+[["Station 496 (scope, labor, material, weather)","$770,000",""],["**Total risks","**$6,070,000",""]],widths=[3.2,1.0,2.6],num_cols=(1,))
para(d,"Risk families not in the register (red team, 29 Sep 2026): siting denial as a decision risk (only $250K of delay is carried; the EFSB fallback is 18 to 24 months); ownership of the 63-day battery commissioning window (excluded from Haugland scope); Nomad counterparty exposure (letter of credit $1.2M against a $12.1M contract); Station 496 outage-window premium (1.35 to 1.70 factor on affected hours, no outage plan yet); FEOC and ITC eligibility; resource competition with the 21192 long-term substation. The $1.0M material and tariff item is sized on total material although the battery (72% of material) is fixed by contract, and it overlaps the 3% per year escalation already in the lines. None of the twelve values carries a basis, probability or correlation.")
para(d,"Contingency: $2,283,517 Sta 360 and $331,723 Sta 496, $2,615,200 total. Risks plus contingency equal 17.9% of the approval level less risks and contingency, inside the 15-18% lead-review guidance. Haugland's Attachment 4-F contingency table separately carries nine allowances for its own scope, including geotechnical ($600K low / $1.6M likely / $3.5M high), fault study driven equipment change ($250K / $700K / $1.8M) and the demarcation structure ($150K / $400K / $900K); those exposures overlap the Eversource register and have not been reconciled.")
para(d,f"Overlap with escalation (savings register A2, 3 October 2026). Two register lines describe escalation rather than risk: 'labor costs impact: salaries increase yearly' ($800,000 Sta 360, $220,000 Sta 496) and 'material costs impact' ($1,000,000 and $300,000), while the directs already carry $2,948,100 of escalation at the template rate. Re-worded as a labor-shortage risk and a tariff allowance sized on the $3.69 million of non-battery material, the two lines fall by {_rng(SV['items'][1]['lo'],SV['items'][1]['hi'])}. The reduction is not booked here; it is a decision for the lead review.")
# ---------- 19-21 ----------
d.add_heading("19. Indirect / Overheads",1)
para(d,"EMA station work rates from the 2026 ESF template: E&S station overhead, general services, non-productive time, payroll benefits, AS&E, MDEC, vehicles, lobby stock. Station 360 $8,064,700 (of which $1,964,236 actual); Station 496 $1,922,000. Indirects are 17.4% of the approval level. No modification to approved rates.")
para(d,f"Open question (savings register A4): the E&S station basis rows total {_m(SV['es_rate']*sum(v for k,v in L.items() if k[0] in 'ABCDEGHI'))} at {SV['es_rate']:.1%} of Station 360 directs and are applied to the vendor-furnished, vendor-commissioned battery contract as to any other material; on the battery line alone that is {_m(SV['es_rate']*L['A. Battery supply contract (Nomad)'])}. Whether the basis should load a turnkey vendor contract is a policy question for Accounting, not an estimating judgment; the estimate follows the template until answered.")
d.add_heading("20. AFUDC",1)
para(d,"Included. $4,680,899 Sta 360 (actual $376,893) and $333,100 Sta 496, computed by the ESF template on the spend curve from July 2021 to December 2028. AFUDC is 8.8% of the approval level, high for a project of this size because of the seven-year development window.")
para(d,f"Payment timing (savings register C3): the Nomad Attachment C-2 milestones put most of the battery price into CWIP ahead of the January 2028 delivery; each $10 million carried twelve months earlier accrues about $0.75 million of AFUDC at the template rate. Aligning the milestone schedule to delivery is worth {_rng(SV['items'][-1]['lo'],SV['items'][-1]['hi'])}; every month of siting slip costs about $0.4 million across AFUDC, escalation, PM and indirects.")
d.add_heading("21. Reimbursables / Customer Contribution",1)
para(d,"None.")
# ---------- 22 Clarifications ----------
d.add_heading("22. Additional Clarifications and Open Items for Full Funding",1)
bullets(d,[
 ("Reconcile Haugland's Class 3 base to the Rev 3 construction layers. ","$19,216,899 versus about $8.3M direct in layers B (install), D and E; scope boundaries (distribution tie-in, platform on cap, police details, owner-furnished material) must be mapped line by line before either figure is quoted."),
 ("Confirm the four written items Haugland values at $1,469,000. ","Retaining wall quantity ($534K), detention basin volume ($156K), duct bank configuration ($147K) and GSU count ($632K). Haugland has priced the larger of each pair; Rev 3 carries the smaller GSU count already."),
 ("Decide on escalation of the fixed-price battery balance. ","$1,130,255 is carried against a price fixed by contract; removing it or moving it to the risk register is a leadership decision."),
 ("Re-base the D Line (24211) estimate. ","$4,793,000 is a 2023 conceptual figure and the Haugland take-off implies a larger duct bank."),
 ("Commission the geotechnical investigation before IFC. ","Platform depth and bearing on engineered fill drive a $383,000 deduct or a $600K to $3.5M exposure."),
 ("Hazard mitigation analysis (NFPA 855) before civil design freeze. ","Sets the BESS footprint ($581K deduct if 17,040 SF is buildable) and the fire-water containment ($104,500 carried by Haugland)."),
 ("Battery installation labor basis. ","The line note applies 25% of the 16,801 mh E-23-373 site total (4,200 mh) and the line carries 5,557 mh; Rev 2 used 50% (9,757 mh). Nomad supervision assumes two people for one day per container; a bottom-up crew estimate should replace the percentage."),
 ("Estimate class. ","Rev 3 is labeled Conceptual (-25% / +50%). Its deliverable maturity is Class 4 under 96R-18: 30% engineering, unit-library construction with no bid, install labor as a percentage of a 2023 site total, a placeholder platform depth. Present the November number at that class and range unless the geotechnical report, the hazard mitigation analysis, the Haugland reconciliation and a crew build-up close first; then Planning grade (-15% / +25%)."),
 ("Station 496 unit rate. ","$362,700 per relay at approval level, with $1.81M of testing and $1.39M of construction labor on a 20-relay swap. Compare to two recent EMA feeder relay-replacement actuals before full funding; if the rate reflects transfer-trip and outage-window complexity, write that basis down."),
 ("E&S overhead basis on the vendor contract. ",f"Ruling from Accounting on whether the station E&S basis applies to a vendor-furnished, vendor-commissioned contract (savings register A4, {_rng(SV['items'][3]['lo'],SV['items'][3]['hi'])})."),
 ("Commissioning split. ","Write the Nomad-versus-owner commissioning scope into the test plan; the field-test and LCE hours are carried from E-23-373 and overlap the $210,000 of support and $246,000 of vendor labor in the contract (A5)."),
 ("Interconnection topology. ","System Planning hosting-capacity study: can two 13.8 kV feeders take 5 MW each? Five feeder cabinets, four GSUs, four breakers and four metering sets scale with the number of connections (B2). If the answer is no, the item is zero."),
 ("Lines the Siemens skids already carry. ",f"Siemens' 12 Aug 2026 budgetary ($300K per skid, +/-30%) includes the disconnects, PTs, relays, cabinets and DC battery; Rev 3 also carries eight disconnect switches and the PT cutouts as station lines (${SC['double_count_disconnects']/1e3:,.0f}K, 1,040 mh). Strike them once the skid scope is confirmed in writing (savings register B5)."),
 ("GSU count and installation hours. ","Rev 3 carries four 3 MVA pad-mounts at 524 man-hours each to set; the project manager's 9 Sep 2026 email refers to twelve GSUs and Haugland priced the larger count. Settle the topology in writing; the install hours are a reduction (B6), the count is an exposure of $0.6M to $1.0M."),
 ("Sound mitigation, screening, police details, NFPA 855. ","E-23-373 carried $467K of sound mitigation; Rev 3 carries none and the risk register does not list it. The constructability review expects visual screening and a possible facade; the estimate carries $12K of traffic control for Boston public-way work and no hazard mitigation analysis line. Price or register them ($0.6M to $1.2M direct exposure)."),
 ("Switchyard lighting. ",f"${SC['lighting']/1e3:,.0f}K for twelve HPS luminaires and 1,200 ft of hookup at about $200 a foot on an unmanned one-acre pad; design to the security need (B7)."),
 ("Nomad payment milestones and AFUDC. ","Align Attachment C-2 to the January 2028 delivery where the contract allows (C3)."),
 ("Section 48E investment tax credit. ",f"Not in the estimate and not an estimate matter, but the largest single lever on what customers pay: {_rng(IT['lo'],IT['hi'])} at 30 percent on a {_m(IT['basis_lo'])} to {_m(IT['basis_hi'])} eligible basis, plus {_rng(IT['ec_lo'],IT['ec_hi'])} if the landfill qualifies as a brownfield energy community. Tax to opine on eligible basis, the prohibited-foreign-entity cost ratio (65 percent for a 2028 construction start under Notice 2026-15) on the Voyager cells, the section 50(d)(2) normalization election and DPU treatment. Ask Nomad for cell and module origin before the final-drawings milestone."),
 ("Siting float. ","Determination, construction start and container delivery all land in Q1 2028 for a Dec 2028 ISD. Establish a float target on the siting chain and assign owners to five early-warning indicators: geotech by IFC-civil freeze, ZBA hearing date within 90 days of filing, HEG reconciliation before the PAF, Nomad drawing milestones, Station 496 outage plan before construction pricing."),
])
d.add_heading("23. Scope challenge and cost containment (5 Oct 2026)",1)
para(d,f"At leadership's request the Rev 3 scope was challenged layer by layer against what the function requires (companion deck slides 30 to 33; whitepaper section 8.1). Reductions that survive the challenge total {_rng(SC['totals']['reduction_lo'],SC['totals']['reduction_hi'])} direct ({_rng(SC['totals']['reduction_lo_loaded'],SC['totals']['reduction_hi_loaded'])} loaded); exposures the estimate does not carry total {_rng(-SC['totals']['exposure_lo'],-SC['totals']['exposure_hi'])} direct. Three numbers follow: Rev 3 as estimated ${SC['approval']/1e6:.1f}M; contained by decisions alone {_rng(SC['cases']['contained']['lo'],SC['cases']['contained']['hi'])}; re-scoped after every study closes {_rng(SC['cases']['rescoped']['lo'],SC['cases']['rescoped']['hi'])}; and the honest planning range once the exposures and the Haugland reconciliation are added back, {_rng(SC['cases']['net']['lo'],SC['cases']['net']['hi'])}. The containment plan sets a station-direct design-to-cost target at the reference-class 75th percentile and a loaded target of $50M at the IFC gate, with a change control board, monthly trend reporting and competitive lump-sum pricing of the station, civil and installation scope before construction pricing.")
table(d,["Layer","Rev 3 carries","The function requires","Challenge","Direct $"],[[r["layer"],r["carries"],r["requires"],r["challenge"],(_rng(r["lo"],r["hi"]) if r["kind"]=="reduction" else "exposure "+_rng(-r["lo"],-r["hi"]))] for r in SC["rows"]],widths=[0.9,1.9,1.5,2.1,0.8],font=7.5)
footer(d,"Eversource Energy | Cost Estimating Center of Excellence | Hyde Park BESS Basis of Estimate | Rev 3 basis, 29 Sep 2026, revised 5 Oct 2026 | Internal, contains vendor-confidential pricing")
d.save(f"{B}/Hyde_Park_BESS_Basis_of_Estimate.docx"); print("saved BOE")
