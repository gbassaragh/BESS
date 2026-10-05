import sys, json
sys.path.insert(0,"/tmp/claude-0/-home-user-BESS/078f934e-4ca0-5169-be3f-cb66ff0e2514/scratchpad/build")
from pptx_common import *
from pptx import Presentation
B="/tmp/claude-0/-home-user-BESS/078f934e-4ca0-5169-be3f-cb66ff0e2514/scratchpad/build"
R=json.load(open(f"{B}/stats_results.json")); MC=json.load(open(f"{B}/mc_results.json")); MCW=json.load(open(f"{B}/mc_results_wide.json"))
P=R["ols_parsimonious"]; RC=R["reference_class"]
p=Presentation(f"{B}/Hyde_Park_BESS_Cost_Analysis.pptx")
# insert before the Contributions slide (last). We add slides at the end then move the contributions slide to the end.
n=len(p.slides)
def k_(v): return f"${v:,.0f}"
# A1 reference class
RCU=R["reference_class_utility"]
s=blank(p); chrome(s,f"{RC['n']} built projects at or below 100 MWh, utility- and developer-owned: where Hyde Park sits",eyebrow="Appendix A. Reference class (public disclosures, nominal $/kWh)",n=n)
s.shapes.add_picture(f"{B}/stats_refclass.png",Inches(0.5),Inches(1.5),height=Inches(5.3))
AJ_=json.load(open(f"{B}/adjust_results.json"))
bullets(s,8.6,1.55,4.2,5.3,[("Median ",f"{k_(RC['median_kwh'])}/kWh; interquartile {k_(RC['q25'])} to {k_(RC['q75'])}. Utility-owned subclass ({RCU['n']}): median {k_(RCU['median_kwh'])}."),("Hyde Park battery installed, $833: ",f"{RC['hp_rank']['b3']:.0%} percentile."),("Station complete, direct, $1,483: ",f"{RC['hp_rank']['b4']:.0%} percentile ({RCU['hp_rank']['b4']:.0%} in the utility subclass), beside Fairhaven ($1,659 actual, 2023), Chateaugay ($1,490, 2023) and Provincetown ($1,289 actual, 2022)."),("Approval level, $2,862: ","above every member. The loaders ($23.7M) and the two interconnection scopes are what the comparables do not carry."),("Re-based to 2026 dollars (slides 12 and 14 to 18): ",f"median {k_(AJ_['indices']['installed']['median'])} at the installed index, {k_(AJ_['indices']['installed_s30']['median'])} to {k_(AJ_['indices']['installed_s50']['median'])} across 30 to 50% anchor battery share (2024 basis, back-cast to each project's year)."),("Built projects only (5 Oct 2026). ",f"Status of every dataset row verified; {R['status_counts']['not_built']} rows that were planned, under development, under construction or cancelled are excluded from the class and the regression. {R['reference_class_actuals']['n']} members carry a final or actual cost (median ${R['reference_class_actuals']['median_kwh']:,.0f}); the others are contract, budget or announcement figures for projects that were built."),("Caveat: ",f"figures from regulator, IDA, EIA and utility documents, verified by status audit; developer-owned members carry developer overhead and profit but no utility indirects or AFUDC; incentives are not netted.")],size=10,gap=3)
# A2 regression
s=blank(p); chrome(s,"Size and duration explain half the spread in public costs; Hyde Park's direct cost is high-normal",eyebrow=f"Appendix B. Regression on {P['n']} public projects",n=n+1)
s.shapes.add_picture(f"{B}/stats_scatter.png",Inches(0.5),Inches(1.5),width=Inches(7.9))
table(s,8.6,1.55,4.2,2.3,["Term","Coefficient","p"],[["Size (ln MWh)",f"{P['coef']['ln_mwh']['b']:+.2f}",f"{P['coef']['ln_mwh']['p']:.3f}"],["Duration (ln h)",f"{P['coef']['ln_dur']['b']:+.2f}",f"{P['coef']['ln_dur']['p']:.3f}"],["Year",f"{P['coef']['yr']['b']:+.3f}",f"{P['coef']['yr']['p']:.2f}"],["R-squared",f"{P['r2']:.2f}",f"n = {P['n']}"]],col_w=[1.8,1.3,1.1],size=11,align_right=(1,2))
bullets(s,8.6,4.05,4.2,2.8,[("20 MWh, 2-h, 2028 prediction: ",f"{k_(P['hp_pred_kwh']['p50'])}/kWh, 80% interval {k_(P['hp_pred_kwh']['pi80_lo'])} to {k_(P['hp_pred_kwh']['pi80_hi'])}."),("Hyde Park percentiles: ",f"contract {P['hp_percentile']['contract']:.0%}, installed {P['hp_percentile']['b3']:.0%}, station direct {P['hp_percentile']['b4']:.0%}, approval {P['hp_percentile']['b6']:.0%}."),("Use as a bracket, not a price. ",f"Residual spread is a factor of {2.718281828**P['resid_sd']:.1f}. In the fuller model utility ownership adds {(2.718281828**R['ols']['coef']['utility']['b']-1):.0%} at the same size, duration and year (p {R['ols']['coef']['utility']['p']:.2f}); region is not significant.")],size=12,gap=5)
# A3 Monte Carlo
s=blank(p); chrome(s,"Monte Carlo on the layers: reserve covers the modeled ranges, thin against history",eyebrow="Appendix C. Element-level simulation, 20,000 trials",n=n+2)
s.shapes.add_picture(f"{B}/mc_hist.png",Inches(0.5),Inches(1.5),width=Inches(6.4))
s.shapes.add_picture(f"{B}/mc_tornado.png",Inches(0.5),Inches(4.45),width=Inches(6.4))
table(s,7.2,1.55,5.6,2.6,["","Base ranges","Wide ranges"],[["P50 total",f"${MC['total_excl_JK']['50']/1e6:.1f}M",f"${MCW['total_excl_JK']['50']/1e6:.1f}M"],["P80 total",f"${MC['total_excl_JK']['80']/1e6:.1f}M",f"${MCW['total_excl_JK']['80']/1e6:.1f}M"],["Reserve to reach P80",f"${MC['implied_P80_reserve_over_directs']/1e6:.1f}M",f"${MCW['implied_P80_reserve_over_directs']/1e6:.1f}M"],["Carried risk + contingency","$7.6M","$7.6M"],["P(total > $57.2M)",f"{MC['p_exceed_approval_excl_JK']:.0%}",f"{MCW['p_exceed_approval_excl_JK']:.0%}"]],col_w=[2.6,1.5,1.5],size=12,align_right=(1,2))
bullets(s,7.2,4.35,5.6,2.5,[("Distributions ","are PERT ranges on each of the nine Station 360 layers plus Station 496, indirects and AFUDC; risk register and contingency are not stacked on top (they fund the same outcomes)."),("Estimate-to-actual uplift on comparables: ","Fairhaven +64%, Provincetown +9 to +40%, Waena +37%, Regina +31%, Hyde Park Sep cycle +21%. Median about +31%; Rev 3 carries 17.9%."),("Next step: ","replace these ranges with the project team's in a two-hour range-estimating session (AACE 41R-08) before full funding.")],size=12,gap=5)
# move contributions slide (index n-1) to the end
sldIdLst=p.slides._sldIdLst; ids=list(sldIdLst); contrib=ids[n-1]; sldIdLst.remove(contrib); sldIdLst.append(contrib)
# fix page numbers on appendix (they were n, n+1, n+2 = 16,17,18 which is right since contributions becomes 19)
p.save(f"{B}/Hyde_Park_BESS_Cost_Analysis.pptx"); print("appendix added; slides",len(p.slides))
