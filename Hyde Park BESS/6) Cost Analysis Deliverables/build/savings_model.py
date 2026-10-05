"""Cost-saving opportunity register for Hyde Park BESS (deck narrative 2).
Every item is sized from the Rev 3 rows in data.json. Direct-dollar ranges; loaded at the MARGINAL loader
(contingency + basis-driven indirects + AFUDC over Station 360 directs; the risk register and the indirect
rows already booked as actuals do not scale), not the 1.685 average loader used elsewhere in the deck.
"""
import json, numpy as np
B="/tmp/claude-0/-home-user-BESS/078f934e-4ca0-5169-be3f-cb66ff0e2514/scratchpad/build"
D=json.load(open(f"{B}/data.json")); L=D["layers_direct"]; LL=D["layers_loaded"]; rows=D["rows"]
R=lambda f: sum(r["cost"] for r in rows if f(r)); MH=lambda f: sum(r["mh"] for r in rows if f(r))
dirs=sum(v for k,v in L.items() if k[0] in "ABCDEGHI")
L_actual=R(lambda r: r["layer"].startswith("L.") and "actual" in r["note"].lower())
MARG=1+(L["K. Contingency"]+L["L. Indirects / overheads"]-L_actual+L["M. AFUDC"])/dirs      # ~1.44
ES=R(lambda r: r["layer"].startswith("L.") and "E&S" in r["desc"]); es_rate=ES/dirs
# --- Station 496 relay program
s496=lambda r: r["est"].endswith("496 - Rev 2")
relay_furnish=R(lambda r: s496(r) and r["cbs1"]=="06" and "Relays SEL" in r["desc"])
relay_install=R(lambda r: s496(r) and r["cbs1"]=="07" and "Relays SEL" in r["desc"]); relay_install_mh=MH(lambda r: s496(r) and r["cbs1"]=="07" and "Relays SEL" in r["desc"])
relay_test=R(lambda r: s496(r) and r["cbs1"]=="08"); relay_test_mh=MH(lambda r: s496(r) and r["cbs1"]=="08")
relay_remove=R(lambda r: s496(r) and r["cbs1"]=="10")
n_relays=20; sta496=D["sta496"]
# --- battery install labor (layer B)
bi=[r for r in rows if r["layer"].startswith("B.") and "(Install)" in r["desc"] and "Voyager" in r["desc"]][0]; fire=R(lambda r: r["layer"].startswith("B.") and "Fire Suppress" in r["desc"])
# --- civil (layer E) key lines
wall=R(lambda r: r["layer"].startswith("E.") and "Retaining wall" in r["desc"]); borings=R(lambda r: r["layer"].startswith("E.") and "Soil Borings" in r["desc"])
earth=R(lambda r: r["layer"].startswith("E.") and ("Soil Disposal" in r["desc"] or "Backfill" in r["desc"] or "Trap Rock" in r["desc"]))
# --- station D equipment driven by the four-feeder topology
brk=R(lambda r: r["layer"].startswith("D.") and "Circuit Breakers" in r["desc"]); brk_f=R(lambda r: r["layer"].startswith("D.") and "Circuit Breakers" in r["desc"] and "(Furnish)" in r["desc"]); meter=R(lambda r: r["layer"].startswith("D.") and "Metering" in r["desc"]); disc=R(lambda r: r["layer"].startswith("D.") and "Disconnect" in r["desc"])
gsu=R(lambda r: r["layer"].startswith("C.") and "GSU" in r["desc"]); gsu_i=R(lambda r: r["layer"].startswith("C.") and "GSU" in r["desc"] and "(Ins" in r["desc"]); gsu_mh=MH(lambda r: r["layer"].startswith("C.") and "GSU" in r["desc"] and "(Ins" in r["desc"]); light=R(lambda r: r["layer"].startswith("D.") and "Switchyard Lighting" in r["desc"]); light_mh=MH(lambda r: r["layer"].startswith("D.") and "Switchyard Lighting" in r["desc"]); site_ext=R(lambda r: r["est"].endswith("360 - Rev 3") and "Siting, External" in r["desc"]); site_ext_496=R(lambda r: r["est"].endswith("496 - Rev 2") and "Siting, External" in r["desc"]); gsu_f=R(lambda r: r["layer"].startswith("C.") and "GSU" in r["desc"] and "(Furnish)" in r["desc"])
# --- risk register overlap with escalation
risk_labor=R(lambda r: "Risk" in r["desc"] and "Labor costs" in r["desc"]); risk_mat=R(lambda r: "Risk" in r["desc"] and "Mat'l costs" in r["desc"])
non_batt_mat=3687000  # Rev 3 non-battery material (curve.json)
esc_batt=1130255
# --- testing & commissioning overlap with the Nomad contract
tc_field=R(lambda r: r["layer"].startswith("G.") and "Field Test" in r["desc"]); tc_lce=R(lambda r: r["layer"].startswith("G.") and "LCE" in r["desc"])
nomad_support=D["nomad_support"]; nomad_labor=D["nomad_labor"]
# --- ITC (financial lever; parameters are assumptions to be confirmed by Tax)
itc={"rate_base":0.30,"energy_community_adder":0.10,"basis_lo":LL["A. Battery supply contract (Nomad)"]+LL["B. Battery installation & integration (owner scope)"]+LL["C. Battery balance-of-plant (GSUs, EMS/comms, aux power)"],
     "basis_hi":sum(LL[k] for k in LL if k[0] in "ABCDEG")}
itc["lo"]=itc["rate_base"]*itc["basis_lo"]; itc["hi"]=itc["rate_base"]*itc["basis_hi"]; itc["ec_lo"]=itc["energy_community_adder"]*itc["basis_lo"]; itc["ec_hi"]=itc["energy_community_adder"]*itc["basis_hi"]
afudc_rate=0.075; afudc_shift=0.75*D["nomad_contract"]  # three quarters of the battery price paid a year earlier than delivery
items=[
 # id, tier, title, layer, direct_lo, direct_hi, scales(with marginal loader), conf, owner, what_must_close, evidence
 dict(id="A1",tier="A",title="Remove escalation carried on the fixed-price Nomad balance",layer="A",lo=esc_batt,hi=esc_batt,scales=True,conf="High",owner="Cost Estimating / Sourcing",close="Exhibit C read for tariff and change-in-law pass-through; decision minuted",
      ev=f"Rev 3 applies the ESF template rate to the ${D['nomad_contract']/1e6:.1f}M contract balance; the price is fixed until Final Acceptance."),
 dict(id="A2",tier="A",title="Risk register: labor-cost and material-cost lines overlap the escalation already in the directs",layer="J",lo=0.5*risk_labor+(risk_mat-0.15*non_batt_mat),hi=risk_labor+(risk_mat-0.15*non_batt_mat),scales=False,conf="Medium",owner="Cost Estimating + PM",close="Re-word the two lines as labor-shortage and tariff risks and size them on exposure, not on the whole material and labor base",
      ev=f"'Salaries increase yearly' (${risk_labor/1e3:,.0f}K) and 'material costs increase' (${risk_mat/1e3:,.0f}K) describe escalation, which Rev 3 already carries at $2.95M; a tariff allowance of 15% on ${non_batt_mat/1e6:.2f}M of non-battery material is ${0.15*non_batt_mat/1e3:,.0f}K."),
 dict(id="A3",tier="A",title="Confirm the four written design-basis items Haugland priced as deducts",layer="D/E",lo=0.6e6,hi=0.8e6,scales=True,conf="Medium",owner="Substation Engineering",close="Retaining wall, basin, duct bank and GSU count confirmed in writing; HEG map signed first",
      ev="HEG deduct ceiling $1.47M; GSU count already four in Rev 3, so about $0.8M net (red team report)."),
 dict(id="A4",tier="A",title="Engineering & supervision overhead basis applied to the vendor turnkey contract",layer="L",lo=0.5*es_rate*L["A. Battery supply contract (Nomad)"],hi=es_rate*L["A. Battery supply contract (Nomad)"],scales=False,conf="Low",owner="Accounting / Cost Estimating",close="Ruling on whether the E&S station basis applies to vendor-furnished, vendor-commissioned equipment",
      ev=f"E&S basis rows ${ES/1e6:.2f}M = {es_rate:.1%} of Station 360 directs; applied to the ${L['A. Battery supply contract (Nomad)']/1e6:.1f}M battery line that is {es_rate*L['A. Battery supply contract (Nomad)']/1e6:.1f}M."),
 dict(id="A5",tier="A",title="Commissioning hours carried from E-23-373 overlap Nomad's commissioning support",layer="G",lo=0.15e6,hi=0.35e6,scales=True,conf="Low",owner="Capital Projects Eng. + Nomad",close="Commissioning split (Nomad vs owner) written into the test plan",
      ev=f"Field test {tc_field/1e3:,.0f}K + LCE {tc_lce/1e3:,.0f}K carried at 2023 hours; the contract already holds ${nomad_support/1e3:,.0f}K of support and ${nomad_labor/1e3:,.0f}K of vendor labor."),
 dict(id="B1",tier="B",title="Station 496 relay program: 710 man-hours per relay",layer="F",lo=0.35*(relay_install+relay_test),hi=0.5*(relay_install+relay_test),scales=False,conf="Medium",owner="P&C Engineering + EMA",close="Two recent relay-replacement actuals; confirm the four SEL-735 are protection, not metering; outage windows priced",
      ev=f"{n_relays} relays: hardware ${relay_furnish/1e3:,.0f}K, install {relay_install_mh:,.0f} mh (${relay_install/1e6:.2f}M), test {relay_test_mh:,.0f} mh (${relay_test/1e6:.2f}M), E&S basis $1.46M; ${sta496/n_relays/1e3:,.0f}K per relay all-in. Loaded effect includes the E&S basis on the hours."),
 dict(id="B2",tier="B",title="Interconnection topology: five feeder cabinets, four GSUs, four breakers, four metering sets for 10 MW",layer="C/D",lo=0.35*(brk+meter+disc+0.5*gsu),hi=0.5*(brk+meter+disc+0.5*gsu),scales=True,conf="Low",owner="System Planning + Substation Eng.",close="Hosting-capacity study: can two feeders take 5 MW each? If not, the item is zero",
      ev=f"Breakers ${brk/1e6:.2f}M, metering ${meter/1e3:,.0f}K, disconnects ${disc/1e3:,.0f}K, GSUs ${gsu/1e6:.2f}M scale with the number of feeder connections."),
 dict(id="B3",tier="B",title="Platform and retaining wall sized after geotech, not before",layer="E",lo=0.3e6,hi=0.8e6,scales=True,conf="Low",owner="Civil + Capital Projects Eng.",close="Geotech report; MassDEP SW45 post-closure permit conditions; NFPA 855 spacing",
      ev=f"14-ft retaining wall ${wall/1e3:,.0f}K, earthwork and surfacing ${earth/1e3:,.0f}K, 36 borings ${borings/1e3:,.0f}K on a placeholder 2.5-ft platform. Two-sided: the red team's downside is $0.6M to $3.5M."),
 dict(id="B4",tier="B",title="Battery installation labor from a crew build-up instead of 25% of a 2023 total; fire suppression bought twice?",layer="B",lo=(bi['mh']-3000)/bi['mh']*bi['cost'],hi=(bi['mh']-2400)/bi['mh']*bi['cost']+fire,scales=True,conf="Medium",owner="Cost Estimating + Nomad + HEG",close="Crew build-up: crane set, anchoring, DC and AC terminations per Voyager unit; confirm whether the Voyager enclosure carries its own suppression ($132K carried)",
      ev=f"{bi['mh']:,.0f} mh (${bi['cost']/1e6:.2f}M) for 12 units = {bi['mh']/12:,.0f} mh each; build-up at 200 to 250 mh per unit gives 2,400 to 3,000 mh. NREL ATB installation labor and equipment: $19/kWh (2019$, 60 MW), i.e. about $0.4M at 20 MWh before the small-project premium."),
 dict(id="B5",tier="B",title="Disconnect switches and PT cutouts priced as separate lines although the Siemens skids carry them",layer="D",lo=259459,hi=259459,scales=True,conf="High",owner="Substation Eng. + Cost Estimating",close="Strike lines 07.03.02.04, 06.02.09.00 and the PT cutouts once Siemens confirms the skid scope in writing",
      ev="Siemens budgetary of 12 Aug 2026: $300K per skid for breaker, frame, disconnects, PTs, relays and DC battery (so the $332K breaker line is not a price lever); the 8 disconnects ($238K, 1,040 mh) and PT cutouts are carried again as station lines whose own notes say 'located on breaker skid'."),
 dict(id="B6",tier="B",title="GSU installation hours: 524 man-hours per pad-mount; count to be settled (four carried, twelve mentioned)",layer="C",lo=0.5*gsu_i,hi=0.65*gsu_i,scales=True,conf="Medium",owner="Substation Eng. + Nomad",close="Topology and GSU count in writing; crew build-up for a pad-mount set; 2026 transformer quote with the 29-70 week lead time in the schedule",
      ev=f"Install ${gsu_i/1e3:,.0f}K for four units ({gsu_mh/4:,.0f} mh each) against a normal 100-150 mh pad-mount set. The furnish price ($267K each from a 2023 bidder list plus 3%/yr) is not the lever; the count is the exposure (PM email 9 Sep 2026: 'GSU transformers (12)')."),
 dict(id="B7",tier="B",title="Switchyard lighting: 12 HPS luminaires and $200 a foot of hookup on an unmanned one-acre pad",layer="D",lo=0.5*light,hi=0.65*light,scales=True,conf="Medium",owner="Substation Eng.",close="Lighting design to the security need (fence-line LED, motion); hookup length and rate from the layout",
      ev=f"${light/1e3:,.0f}K and {light_mh:,.0f} mh across four lighting lines (07.03.02.99)."),
 dict(id="B8",tier="B",title="Siting and project management: external siting at $1.05M and a $157K siting line inside Station 496",layer="H/F",lo=0.2e6+site_ext_496,hi=0.4e6+site_ext_496,scales=True,conf="Low",owner="Siting + PM",close="Task budget from outside counsel for Article 80 small-project review and the ZBA permit; confirm what the Station 496 siting application is for",
      ev=f"04.02.00.00 Sta 360 ${site_ext/1e3:,.0f}K external siting; Sta 496 04.02.00.00 ${site_ext_496/1e3:,.0f}K for relay work inside an existing fence."),
 dict(id="C1",tier="C",title="Section 48E investment tax credit on the storage property",layer="rev. req.",lo=itc["lo"],hi=itc["hi"],scales=False,conf="Medium",owner="Tax + Regulatory",close="Eligible-basis opinion; FEOC cost-ratio test (65% non-PFE for a 2028 construction start); normalization election; DPU treatment",
      ev=f"30% of an eligible basis of ${itc['basis_lo']/1e6:.0f}M (battery, install, BOP loaded) to ${itc['basis_hi']/1e6:.0f}M (plus station, site, testing). Not an estimate change: a revenue-requirement reduction."),
 dict(id="C2",tier="C",title="Energy-community adder if the closed landfill qualifies as a brownfield",layer="rev. req.",lo=itc["ec_lo"],hi=itc["ec_hi"],scales=False,conf="Low",owner="Tax + Environmental",close="Phase II ESA or a prior brownfield-program assessment (the Phase I safe harbor stops at 5 MW)",
      ev="Additional 10 percentage points on the same basis."),
 dict(id="C3",tier="C",title="AFUDC: pay the battery at delivery, not a year ahead; protect the siting float",layer="M",lo=0.5*afudc_rate*afudc_shift,hi=afudc_rate*afudc_shift,scales=False,conf="Medium",owner="PM + Sourcing + Treasury",close="Milestone payment schedule in the Nomad SOV aligned to 2028 delivery; float target on the ZBA chain",
      ev=f"AFUDC ${L['M. AFUDC']/1e6:.1f}M. Shifting ${afudc_shift/1e6:.1f}M of battery payments twelve months later saves about {afudc_rate:.1%} of it; every month of schedule slip costs about $0.4M across AFUDC, escalation, PM and indirects (slide 34)."),
]
for it in items:
    it["lo_loaded"]=it["lo"]*(MARG if it["scales"] else 1); it["hi_loaded"]=it["hi"]*(MARG if it["scales"] else 1)
tiers={}
for t in "ABC":
    sel=[i for i in items if i["tier"]==t]
    tiers[t]={"n":len(sel),"lo":sum(i["lo"] for i in sel),"hi":sum(i["hi"] for i in sel),"lo_loaded":sum(i["lo_loaded"] for i in sel),"hi_loaded":sum(i["hi_loaded"] for i in sel)}
out={"marginal_loader":MARG,"avg_loader":D["load_factor"],"es_rate":es_rate,"approval":D["approval_21334"],"items":items,"tiers":tiers,"itc":itc,
     "relay":{"n":n_relays,"furnish":relay_furnish,"install":relay_install,"install_mh":relay_install_mh,"test":relay_test,"test_mh":relay_test_mh,"remove":relay_remove,"sta496":sta496,"per_relay":sta496/n_relays,"mh_per_relay":(relay_install_mh+relay_test_mh)/n_relays},
     "heg_gap_note":"Red team KS1: Haugland Class 3 base $19.2M vs Rev 3 B+D+E $8.3M direct; +$4M to +$8M direct if half the gap is 21334 scope. Tier A and B savings are net of nothing until that closes."}
json.dump(out,open(f"{B}/savings.json","w"),indent=1)
print(f"marginal loader {MARG:.3f}; E&S rate {es_rate:.1%}")
for it in items: print(f"{it['id']} {it['title'][:70]:70s} ${it['lo']/1e6:5.2f}M-${it['hi']/1e6:5.2f}M  loaded ${it['lo_loaded']/1e6:5.2f}M-${it['hi_loaded']/1e6:5.2f}M  {it['conf']}")
for t,v in tiers.items(): print(t, f"${v['lo']/1e6:.1f}M-${v['hi']/1e6:.1f}M direct; loaded ${v['lo_loaded']/1e6:.1f}M-${v['hi_loaded']/1e6:.1f}M")
print("relay",{k:(round(v) if isinstance(v,float) else v) for k,v in out["relay"].items()})
