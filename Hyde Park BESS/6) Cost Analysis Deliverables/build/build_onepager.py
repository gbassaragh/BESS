import sys, json
sys.path.insert(0,"/tmp/claude-0/-home-user-BESS/078f934e-4ca0-5169-be3f-cb66ff0e2514/scratchpad/build")
from docx_common import *
from docx.shared import Inches, Pt
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
B="/tmp/claude-0/-home-user-BESS/078f934e-4ca0-5169-be3f-cb66ff0e2514/scratchpad/build"
D=json.load(open(f"{B}/data.json")); L=D["layers_direct"]
A=L["A. Battery supply contract (Nomad)"]; Bv=L["B. Battery installation & integration (owner scope)"]; C=L["C. Battery balance-of-plant (GSUs, EMS/comms, aux power)"]
Dv=L["D. Station 360 13.8 kV switching & interconnection facilities"]; E=L["E. Site development & civil (former landfill site)"]
G=L["G. Testing & commissioning"]; Hh=L["H. Owner soft costs (engineering, siting, environmental, outreach, PM, land)"]; I=L["I. Taxes, CWIP, builders-risk insurance"]
lad=[("1  Vendor contract as quoted",12106850,"Twelve LFP units, PCS, BMS, fire protection, 10-yr warranty, spares, support, supervision. Fixed price (Nomad, 10 Mar 2026)."),
("2  Battery as carried in estimate",A,"Adds $1.13M escalation on the unpaid balance."),
("3  Battery installed",A+Bv+C,"Adds installation labor, foundation pads, fire suppression, four 3 MVA step-up transformers, EMS, auxiliary power."),
("4  Station complete, direct",A+Bv+C+Dv+E+G+Hh+I,"Adds the 13.8 kV switching station (four breaker skids, metering, cable, duct bank, ground grid), landfill site development, testing, engineering, Article 80 siting, outreach, project management, taxes."),
("5  Station 360 approval level",49994200,"Adds risk register, contingency, corporate indirects, AFUDC."),
("6  Project 21334 approval level",57247300,"Adds Station 496 feeder protection: 20 relays, transfer trip, RTU, testing ($7.25M)."),
("7  All-in incl. D-Line (memo)",57247300+4793000,"Adds the 5,465 ft circuit extension under project 24211 ($4.79M, Feb 2024 conceptual, not re-based).")]
# chart
fig,ax=plt.subplots(figsize=(7.0,2.1),dpi=200)
labels=[l.split("  ")[1] for l,_,_ in lad]; vals=[v/20000 for _,v,_ in lad]
cols=["#FFC72C","#001E60","#001E60","#001E60","#001E60","#6E1F2E","#6E1F2E"]
bars=ax.barh(range(len(vals))[::-1],vals,color=cols,height=0.62)
for i,(b,v) in enumerate(zip(bars,vals)): ax.text(v+30,b.get_y()+b.get_height()/2,f"${v:,.0f}",va="center",fontsize=8,color="#1F2A44",fontweight="bold")
ax.set_yticks(range(len(vals))[::-1]); ax.set_yticklabels(labels,fontsize=8); ax.set_xlim(0,3700); ax.set_xticks([])
for sp in ("top","right","bottom"): ax.spines[sp].set_visible(False)
ax.spines["left"].set_color("#C9D1E0"); ax.tick_params(axis="y",length=0)
ax.set_title("$ per kWh at each boundary (20 MWh)",fontsize=8.5,loc="left",color="#001E60",fontweight="bold")
plt.tight_layout(pad=0.4); fig.savefig(f"{B}/ladder.png"); plt.close(fig)
d=new_doc()
s=d.sections[0]; s.left_margin=s.right_margin=Inches(0.65); s.top_margin=Inches(0.55); s.bottom_margin=Inches(0.5)
st=d.styles["Normal"]; st.font.size=Pt(9.5); st.paragraph_format.space_after=Pt(3); st.paragraph_format.line_spacing=1.0
para(d,"HYDE PARK BATTERY ENERGY STORAGE SYSTEM  |  PROJECT 21334  |  10 MW / 20 MWh",bold=True,size=8,color=BURG,after=0)
para(d,"One project, seven cost boundaries",bold=True,size=19,color=NAVY,after=1)
para(d,"The battery supply contract is $12.1 million. The project that puts it into service is $57.2 million. Both figures are correct; they describe different scopes. The table shows the same project at each boundary where a cost can be quoted, so that any published benchmark can be set beside the row that shares its definition.",size=9.5,after=4)
d.add_picture(f"{B}/ladder.png",width=Inches(6.6))
d.paragraphs[-1].paragraph_format.space_after=Pt(2)
rows=[[a,d0(v),f"${v/10000:,.0f}",f"${v/20000:,.0f}",f"{v/12106850:.1f}x",c] for a,v,c in lad]
table(d,["Boundary","Total","$/kW","$/kWh","x","What this boundary adds"],rows,widths=[1.45,1.0,0.55,0.6,0.4,3.2],num_cols=(1,2,3,4),font=8,zebra=True)
para(d,"Where the other 79 percent sits (loaded, i.e. with risk, contingency, indirects and AFUDC spread across Station 360 layers): station and feeder interconnection facilities $18.3M (32%); battery installation and balance of plant $6.2M (11%); engineering, siting, outreach, project management, testing and taxes $10.9M (19%); battery supply contract $21.9M (38%).",size=9,after=4)
callout(d,"Reading a benchmark against this table.","A published $/kWh figure belongs beside the boundary that shares its scope. Pack and cell prices (BloombergNEF, $70 to $108/kWh in 2025) stop at the factory door and compare to nothing here. Turnkey system prices (BloombergNEF US $219/kWh, 2025; Anza distribution-scale $203/kWh, Q1 2026) stop at the fence and compare to boundary 3, after adjusting a four-hour, 100 MW reference to two hours and 10 MW. All-in developer benchmarks (NREL $334/kWh, EIA and Sargent & Lundy $436/kWh, LBNL $458/kWh, all four-hour, 60 to 150 MW) compare to boundary 4, less a developer's margin. Disclosed utility-owned projects (Eversource Provincetown $1,289/kWh, 1.5-hour, 2022; NV Energy Reid Gardner $584/kWh, 2-hour, 220 MW on an existing switchyard) are the only family that carries a utility's scope, and none carries a separate switching station, a feeder protection program at the source substation, or AFUDC. Five attributes must travel with every figure quoted: boundary, duration, size, dollar year and what is inside the fence.",fill="FFF3CC")
para(d,"Basis: ESF Total Rev 3, 24 Sep 2026 (Conceptual, -25%/+50%); Nomad cover agreement Exhibit C, 10 Mar 2026; SSF Feb 2024 for the D-Line memo. All 292 estimate lines are assigned to thirteen layers in the companion workbook and reconcile to the $57,247,544 unrounded total. Benchmarks are from published sources as retrieved 29 Sep 2026 with confidence tags in the whitepaper; verify against primary documents before external filing. Prepared by the Cost Estimating Center of Excellence, Eversource Energy, 29 Sep 2026. Internal; contains vendor-confidential pricing.",size=7.5,color=GRAY,after=0)
d.save(f"{B}/Hyde_Park_BESS_Unit_Cost_Ladder_OnePager.docx"); print("saved")
