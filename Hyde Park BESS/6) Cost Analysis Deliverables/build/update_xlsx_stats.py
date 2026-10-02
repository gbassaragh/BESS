import json, openpyxl, pandas as pd
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
B="/tmp/claude-0/-home-user-BESS/078f934e-4ca0-5169-be3f-cb66ff0e2514/scratchpad/build"; S="/tmp/claude-0/-home-user-BESS/078f934e-4ca0-5169-be3f-cb66ff0e2514/scratchpad"
NAVY="001E60"; hdr_font=Font(name="Arial",bold=True,color="FFFFFF",size=10); hdr_fill=PatternFill("solid",fgColor=NAVY)
thin=Side(style="thin",color="BFBFBF"); border=Border(left=thin,right=thin,top=thin,bottom=thin)
base=Font(name="Arial",size=10); bold=Font(name="Arial",size=10,bold=True); blue=Font(name="Arial",size=10,color="0000FF"); title=Font(name="Arial",size=14,bold=True,color=NAVY)
def header(ws,row,cols,widths=None):
    for i,c in enumerate(cols,1):
        cell=ws.cell(row=row,column=i,value=c); cell.font=hdr_font; cell.fill=hdr_fill; cell.alignment=Alignment(wrap_text=True,vertical="center"); cell.border=border
    if widths:
        for i,w in enumerate(widths,1): ws.column_dimensions[get_column_letter(i)].width=w
wb=openpyxl.load_workbook(f"{B}/Hyde_Park_BESS_Cost_Analysis.xlsx")
for n in ("Public Projects","Statistics"):
    if n in wb.sheetnames: del wb[n]
# ---- Public Projects ----
df=pd.read_csv(f"{S}/bess_projects.csv"); R=json.load(open(f"{B}/stats_results.json"))
EXCL={"Nantucket BESS":"cost bundles 15 MW diesel generator and control house","Salem Smart Power Center":"2013 demonstration incl. building and smart-grid controls","Arlington Microgrid":"microgrid incl. solar, building, V2G","Essex Solar + Storage":"bundles 4.9 MW solar","Hot Springs Microgrid":"bundles 2 MW solar; MWh not confirmed","Smarter Network Storage (Leighton Buzzard) [UK]":"R&D demonstration incl. trials","SwRI Solar + Storage (5 MW PV + 10 MW BESS)":"bundles 5 MW solar","Glenarm BESS (for Pasadena Water & Power)":"15-year contract value, not capex","Minnesota utility-owned distribution battery program (200 MW)":"program budget, MWh not stated","Morro Bay BESS (proposed, not built)":"proposed, no COD, developer statement"}
ws=wb.create_sheet("Public Projects",wb.sheetnames.index("Cost Curve")+1)
ws["A1"]="Public project-level BESS costs (75 compiled; 55 used in the regression). Blue = keyed from source; $/kWh, $/kW and duration are formulas."; ws["A1"].font=title
cols=["Project","Owner","Owner type","State","ISO","MW","MWh","COD year","Cost ($)","Cost basis","Scope","Site type","Confidence","Excluded (reason)","Duration (h)","$/kWh","$/kW","Source URL","Notes"]
header(ws,3,cols,[40,22,16,8,8,7,8,8,14,26,34,26,9,30,9,9,9,50,50])
for i,r in enumerate(df.itertuples(index=False),4):
    vals=[r.project,r.owner,r.owner_type,r.state,r.iso,r.mw,r.mwh,r.cod_year,r.cost_usd,r.cost_basis,r.scope,r.site_type,r.confidence,EXCL.get(r.project,"")]
    for j,v in enumerate(vals,1):
        v=None if (isinstance(v,float) and pd.isna(v)) else v
        c=ws.cell(row=i,column=j,value=v); c.font=(blue if j in (6,7,8,9) else base); c.border=border; c.alignment=Alignment(wrap_text=True,vertical="top")
    ws.cell(row=i,column=9).number_format='#,##0'
    ws.cell(row=i,column=15,value=f'=IF(AND(ISNUMBER(F{i}),ISNUMBER(G{i}),F{i}>0),G{i}/F{i},"")').number_format='0.00'
    ws.cell(row=i,column=16,value=f'=IF(AND(ISNUMBER(G{i}),ISNUMBER(I{i}),G{i}>0),I{i}/(G{i}*1000),"")').number_format='#,##0'
    ws.cell(row=i,column=17,value=f'=IF(AND(ISNUMBER(F{i}),ISNUMBER(I{i}),F{i}>0),I{i}/(F{i}*1000),"")').number_format='#,##0'
    for j,v in ((18,r.source_url),(19,r.notes)):
        c=ws.cell(row=i,column=j,value=(None if (isinstance(v,float) and pd.isna(v)) else v)); c.font=Font(name="Arial",size=8); c.border=border; c.alignment=Alignment(wrap_text=True,vertical="top")
    for j in (15,16,17): ws.cell(row=i,column=j).font=base; ws.cell(row=i,column=j).border=border
    ws.row_dimensions[i].height=42
n=3+len(df)
ws.cell(row=n+2,column=1,value="Reference class (utility-owned, <=100 MWh, not excluded): median $/kWh").font=bold
ws.cell(row=3,column=20,value="In reference class? ($/kWh if yes)").font=hdr_font; ws.cell(row=3,column=20).fill=hdr_fill; ws.column_dimensions["T"].width=14
for i in range(4,n+1):
    ws.cell(row=i,column=20,value=f'=IF(AND(N{i}="",ISNUMBER(G{i}),G{i}<=100,ISNUMBER(P{i}),OR(LEFT(C{i},3)="IOU",C{i}="muni/coop",LEFT(C{i},5)="other")),P{i},"")').number_format='#,##0'
    ws.cell(row=i,column=20).font=base; ws.cell(row=i,column=20).border=border
ws.cell(row=n+2,column=16,value=f'=MEDIAN(T4:T{n})').number_format='#,##0'
ws.cell(row=n+2,column=17,value=f'=COUNT(T4:T{n})').number_format='0'
ws.cell(row=n+3,column=1,value="Column T flags the reference class (utility-owned, <= 100 MWh, not excluded); the median and count above are live formulas. The Statistics tab carries the Python run values as of 29 Sep 2026.").font=Font(name="Arial",size=9,italic=True)
ws.freeze_panes="B4"; ws.auto_filter.ref=f"A3:S{n}"
# ---- Statistics ----
st=wb.create_sheet("Statistics",wb.sheetnames.index("2026$ Adjustment")+1 if "2026$ Adjustment" in wb.sheetnames else wb.sheetnames.index("Public Projects")+1)
st["A1"]="Statistical evaluation results (values from stats_model.py and mc_model.py, 29 Sep 2026)"; st["A1"].font=title
P=R["ols_parsimonious"]; RC=R["reference_class"]; MC=json.load(open(f"{B}/mc_results.json")); MCW=json.load(open(f"{B}/mc_results_wide.json"))
r=3
def put(label,val,fmt=None,note=""):
    global r
    st.cell(row=r,column=1,value=label).font=base; c=st.cell(row=r,column=2,value=val); c.font=blue
    if fmt: c.number_format=fmt
    st.cell(row=r,column=3,value=note).font=Font(name="Arial",size=9,color="595959"); r+=1
st.cell(row=r,column=1,value="Reference class: all projects <=100 MWh with an all-in disclosed cost, utility- and developer-owned (redefined 2 Oct 2026)").font=bold; r+=1
put("n utility-owned / developer-owned",f"{RC['n_utility']} / {RC['n_developer']}")
put("n",RC["n"]); put("Median $/kWh",RC["median_kwh"],'#,##0'); put("Q25 $/kWh",RC["q25"],'#,##0'); put("Q75 $/kWh",RC["q75"],'#,##0'); put("Min $/kWh",RC["min"],'#,##0'); put("Max $/kWh",RC["max"],'#,##0')
for k,lab in (("contract","Vendor contract $605"),("b3","Battery installed $833"),("b4","Station complete, direct $1,483"),("b6","Approval level $2,862")): put(f"Hyde Park percentile in class: {lab}",RC["hp_rank"][k],'0%')
RCU=R["reference_class_utility"]
r+=1; st.cell(row=r,column=1,value="Reference class, utility-owned subclass (<=100 MWh)").font=bold; r+=1
put("n",RCU["n"]); put("Median $/kWh",RCU["median_kwh"],'#,##0'); put("Q25 $/kWh",RCU["q25"],'#,##0'); put("Q75 $/kWh",RCU["q75"],'#,##0')
for k,lab in (("b3","Battery installed $833"),("b4","Station complete, direct $1,483"),("b6","Approval level $2,862")): put(f"Hyde Park percentile in subclass: {lab}",RCU["hp_rank"][k],'0%')
r+=1; st.cell(row=r,column=1,value="Regression: ln($/kWh) ~ ln(MWh) + ln(duration) + year (OLS, HC1 errors)").font=bold; r+=1
put("n",P["n"]); put("R-squared",P["r2"],'0.000'); put("Adjusted R-squared",P["adj_r2"],'0.000'); put("Residual SD (log)",P["resid_sd"],'0.000')
for k,lab in (("const","Intercept"),("ln_mwh","Size elasticity (ln MWh)"),("ln_dur","Duration elasticity (ln hours)"),("yr","Year (per year after 2020)")):
    put(f"{lab}: coefficient",P["coef"][k]["b"],'0.000',f"SE {P['coef'][k]['se']:.3f}, p = {P['coef'][k]['p']:.3f}")
put("Prediction for 20 MWh, 2-h, 2028: P50 $/kWh",P["hp_pred_kwh"]["p50"],'#,##0'); put("80% prediction interval, low",P["hp_pred_kwh"]["pi80_lo"],'#,##0'); put("80% prediction interval, high",P["hp_pred_kwh"]["pi80_hi"],'#,##0')
for k,lab in (("contract","Vendor contract"),("b3","Battery installed"),("b4","Station complete, direct"),("b6","Approval level")): put(f"Hyde Park percentile of predictive distribution: {lab}",P["hp_percentile"][k],'0%')
r+=1; st.cell(row=r,column=1,value="Monte Carlo on cost layers (20,000 trials; risk register and contingency not added on top)").font=bold; r+=1
for lab,src in (("Base ranges",MC),("Wide (Class 5-like) ranges",MCW)):
    for p in ("10","50","80","90"): put(f"{lab}: P{p} total ($)",src["total_excl_JK"][p],'#,##0')
    put(f"{lab}: reserve to reach P80 above deterministic base ($)",src["implied_P80_reserve_over_directs"],'#,##0',"carried risk + contingency = $7,583,517")
    put(f"{lab}: probability total exceeds $57.2M approval level",src["p_exceed_approval_excl_JK"],'0.0%')
    put(f"{lab}: battery contract share, P50",src["battery_share"]["50"],'0.0%')
r+=1; st.cell(row=r,column=1,value="Layer standard deviation, $ (base / wide)").font=bold; r+=1
for k in "ABCDEFGHI": put(f"Layer {k}",MC["contributions"][k],'#,##0',f"wide: {MCW['contributions'][k]:,.0f}")
st.column_dimensions["A"].width=70; st.column_dimensions["B"].width=16; st.column_dimensions["C"].width=44
# ISO interconnection refs onto Benchmarks tab
bm=wb["Benchmarks"]; last=bm.max_row+2
bm.cell(row=last,column=1,value="ISO interconnection cost references (LBNL series; ISO-NE Transitional Cluster Study interim, Jun 2026)").font=bold
refs=[("LBNL ISO-NE interconnection brief",2023,"Storage median, studies 2018-21",148,"$/kW","n/a","real (2022$ likely)","POI + network upgrades from ISO studies; all-status storage mean ~ $230/kW","High","https://emp.lbl.gov/publications/interconnection-cost-analysis-iso-new"),
("ISO-NE Transitional Cluster Study interim",2026,"Average interconnection cost, 23 transmission-connected projects (~$3.2B / 4.8 GW)",664,"$/kW","n/a","2026 nominal","System network upgrades ~ $2.5B; WCMA > $1,000/kW, SEMA ~ $177/kW; 21 of 26 requests are BESS","High (totals) / Medium (zonal)","https://www.mass.gov/doc/letter-to-iso-ne-on-transitional-cluster-study-interim-results-june-25-2026/download"),
("LBNL NYISO interconnection brief",2023,"Storage, 1-50 MW requests (vs $32/kW above 250 MW)",76,"$/kW","n/a","real","Only ISO-level storage cost by size","High","https://emp.lbl.gov/publications/interconnection-cost-analysis-nyiso"),
("LBNL PJM interconnection brief",2023,"Storage mean, all statuses",335,"$/kW","n/a","real","Median $63/kW; complete storage ~ $4/kW","High","https://emp.lbl.gov/publications/interconnection-cost-analysis-pjm"),
("LBNL MISO interconnection brief",2022,"Storage potential cost, 2018-21",248,"$/kW","n/a","real","","High","https://emp.lbl.gov/publications/generator-interconnection-cost"),
("NYSERDA State of Storage",2025,"Bulk (>5 MW) average installed cost",524,"$/kWh","n/a","2025 nominal","Retail front-of-meter standalone $666/kWh","High","https://www.nyserda.ny.gov/"),
("Modo Energy global capex survey",2026,"Median 2-h system capex (4-h: $201/kWh)",325,"$/kWh","2-h","2026 nominal","Doubling duration cuts ~38%/MWh","Medium","https://modoenergy.com/research/en/global-battery-capex-september-2026-research")]
for i,rr in enumerate(refs,last+1):
    for j,v in enumerate(rr,1):
        c=bm.cell(row=i,column=j,value=v); c.font=base; c.border=border; c.alignment=Alignment(wrap_text=True,vertical="top")
    bm.cell(row=i,column=4).font=blue; bm.row_dimensions[i].height=45
# README rows
rd=wb["README"]; rr=rd.max_row+1
for k,v in (("Tab: Public Projects","75 public project costs compiled 29 Sep 2026 and 2 Oct 2026 (55 used in the regression; exclusions and reasons in column N). $/kWh, $/kW and duration are formulas."),("Tab: Statistics","Reference-class, regression and Monte Carlo results as values, with the model parameters. See the Statistical Benchmarking Memo for method and limits.")):
    rd.cell(row=rr,column=1,value=k).font=bold; c=rd.cell(row=rr,column=2,value=v); c.font=base; c.alignment=Alignment(wrap_text=True,vertical="top"); rr+=1
from openpyxl.workbook.properties import CalcProperties
wb.calculation=CalcProperties(fullCalcOnLoad=True)
wb.save(f"{B}/Hyde_Park_BESS_Cost_Analysis.xlsx"); print("workbook updated")
