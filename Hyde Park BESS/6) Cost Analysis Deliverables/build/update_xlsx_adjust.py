import json, openpyxl
from openpyxl.styles import Font, PatternFill, Alignment
B="/tmp/claude-0/-home-user-BESS/078f934e-4ca0-5169-be3f-cb66ff0e2514/scratchpad/build"
AJ=json.load(open(f"{B}/adjust_results.json")); NY=json.load(open(f"{B}/ny_cohort.json"))
wb=openpyxl.load_workbook(f"{B}/Hyde_Park_BESS_Cost_Analysis.xlsx")
if "2026$ Adjustment" in wb.sheetnames: del wb["2026$ Adjustment"]
ws=wb.create_sheet("2026$ Adjustment", index=wb.sheetnames.index("Public Projects")+1)
NAVY="001E60"; hdr=Font(bold=True,color="FFFFFF",name="Calibri",size=10); hfill=PatternFill("solid",fgColor=NAVY)
base=Font(name="Calibri",size=10); blue=Font(name="Calibri",size=10,color="0000FF"); bold=Font(name="Calibri",size=10,bold=True); title=Font(name="Georgia",size=14,bold=True,color=NAVY); note=Font(name="Calibri",size=9,italic=True,color="6B7280")
def H(r,c,vals):
    for j,v in enumerate(vals):
        cell=ws.cell(row=r,column=c+j,value=v); cell.font=hdr; cell.fill=hfill; cell.alignment=Alignment(wrap_text=True,vertical="center")
ws["A1"]="Dollar-year adjustment of the public comparables to 2026 (deck slides 12-13)"; ws["A1"].font=title
ws["A2"]="cost_2026 = cost_nominal x [ s x I(2026)/I(y) + (1 - s) x (1 + g)^(2026 - y) ]   s = battery share of the comparable, I = battery index, g = non-battery construction escalation. Blue = inputs."; ws["A2"].font=note
ws["A4"]="Battery share s"; ws["B4"]=AJ["share"]; ws["B4"].font=blue; ws["A5"]="Construction escalation g (used only if B7 = 0)"; ws["B5"]=AJ["g"]; ws["B5"].font=blue; ws["B5"].number_format="0.0%"; ws["A7"]="Non-battery escalator: 1 = Handy-Whitman index (column G), 0 = flat g"; ws["B7"]=1; ws["B7"].font=blue
ws["A6"]="Index selector (1 installed, 2 pack, 3 LCOS, 4 turnkey, 5 NREL)"; ws["B6"]=1; ws["B6"].font=blue
# index table
r=8; ws.cell(row=r,column=1,value="A. Battery indices as published ($/kWh; LCOS $/MWh)").font=bold; r+=1
H(r,1,["Year","Installed all-in (EIA-860, LBNL)","BNEF pack (real)","Lazard LCOS midpoint","BNEF turnkey","NREL base year","Handy-Whitman NA production plant","Note"]); r+=1
import numpy as np
IXJ=json.load(open(f"{B}/indices.json")); P_=IXJ["indices"]
tod=lambda pts:{int(k):v for k,v in pts.items()}
inst=tod(P_["installed"]["points"]); pack=tod(P_["pack"]["points"]); lcos=tod(P_["lcos"]["points"]); turn=tod(P_["turnkey"]["points"]); nrel=tod(P_["nrel"]["points"]); hw=tod(IXJ["construction_index"]["points"])
def ip(d,y): xs=sorted(d); return float(np.interp(y,xs,[d[x] for x in xs]))
t0=r
for y in range(2015,2027):
    ws.cell(row=r,column=1,value=y).font=base
    for c,d in ((2,inst),(3,pack),(4,lcos),(5,turn),(6,nrel),(7,hw)):
        cell=ws.cell(row=r,column=c,value=round(ip(d,y),1)); cell.font=blue if y in d else base
    ws.cell(row=r,column=8,value=("published (blue)" if any(y in d for d in (inst,pack,lcos,turn,nrel,hw)) else "interpolated")).font=note; r+=1
t1=r-1
ws.cell(row=r,column=1,value=IXJ["note"]+" Handy-Whitman: "+IXJ["construction_index"]["source"]).font=note
r+=2; ws.cell(row=r,column=1,value=f"B. Reference class ({len(AJ['projects'])} comparables at or below 100 MWh, utility- and developer-owned; redefined 2 Oct 2026)").font=bold; r+=1
H(r,1,["Project","COD year","Nominal $/kWh","Index at COD","Index 2026","Factor","2026$ $/kWh","Naive (whole cost deflated)","Owner"]); r+=1
p0=r
col=f"CHOOSE($B$6,B,C,D)"
for p in sorted(AJ["projects"],key=lambda x:x["nominal"]):
    ws.cell(row=r,column=1,value=p["project"]).font=base; ws.cell(row=r,column=2,value=p["cod_year"]).font=blue; c=ws.cell(row=r,column=3,value=round(p["nominal"],1)); c.font=blue; c.number_format='"$"#,##0'
    ws.cell(row=r,column=4,value=f"=INDEX(CHOOSE($B$6,$B${t0}:$B${t1},$C${t0}:$C${t1},$D${t0}:$D${t1},$E${t0}:$E${t1},$F${t0}:$F${t1}),MATCH(MIN(B{r},2026),$A${t0}:$A${t1},0))").font=base
    ws.cell(row=r,column=5,value=f"=INDEX(CHOOSE($B$6,$B${t0}:$B${t1},$C${t0}:$C${t1},$D${t0}:$D${t1},$E${t0}:$E${t1},$F${t0}:$F${t1}),MATCH(2026,$A${t0}:$A${t1},0))").font=base
    f=ws.cell(row=r,column=6,value=f"=$B$4*E{r}/D{r}+(1-$B$4)*IF($B$7=1,INDEX($G${t0}:$G${t1},MATCH(2026,$A${t0}:$A${t1},0))/INDEX($G${t0}:$G${t1},MATCH(MIN(B{r},2026),$A${t0}:$A${t1},0)),(1+$B$5)^(2026-MIN(B{r},2026)))"); f.font=base; f.number_format="0.00"
    a=ws.cell(row=r,column=7,value=f"=C{r}*F{r}"); a.font=base; a.number_format='"$"#,##0'
    nv=ws.cell(row=r,column=8,value=f"=C{r}*E{r}/D{r}"); nv.font=base; nv.number_format='"$"#,##0'; ws.cell(row=r,column=9,value=("utility" if p.get("utility")==1 else "developer")).font=base; r+=1
p1=r-1
ws.cell(row=r,column=1,value="Median").font=bold; m=ws.cell(row=r,column=3,value=f"=MEDIAN(C{p0}:C{p1})"); m.font=bold; m.number_format='"$"#,##0'; m2=ws.cell(row=r,column=7,value=f"=MEDIAN(G{p0}:G{p1})"); m2.font=bold; m2.number_format='"$"#,##0'; m3=ws.cell(row=r,column=8,value=f"=MEDIAN(H{p0}:H{p1})"); m3.font=bold; m3.number_format='"$"#,##0'; r+=1
for lab,v in (("Hyde Park installed $833, percentile",833),("Hyde Park station complete direct $1,483, percentile",1483),("Hyde Park approval $2,862, percentile",2862)):
    ws.cell(row=r,column=1,value=lab).font=base; c1=ws.cell(row=r,column=3,value=f"=COUNTIF(C{p0}:C{p1},\"<\"&{v})/COUNT(C{p0}:C{p1})"); c1.number_format="0%"; c2=ws.cell(row=r,column=7,value=f"=COUNTIF(G{p0}:G{p1},\"<\"&{v})/COUNT(G{p0}:G{p1})"); c2.number_format="0%"; r+=1
r+=1; ws.cell(row=r,column=1,value="C. New York distribution-scale cohort (not in the regression; nominal dollars of the year shown)").font=bold; r+=1
H(r,1,["Project","Owner","MW","MWh","COD year","Cost $","$/kWh","$/kW","Hours","Cost basis","Confidence","Source"]); r+=1
for p in NY["projects"]:
    vals=[p["project"],p["owner"],p["mw"],p["mwh"],p["cod_year"],p["cost_usd"],f"=F{r}/D{r}/1000",f"=F{r}/C{r}/1000",f"=D{r}/C{r}",p["cost_basis"],p["confidence"],p["url"]]
    for j,v in enumerate(vals,1):
        c=ws.cell(row=r,column=j,value=v); c.font=blue if j in (3,4,5,6) else base
        if j in (6,7,8): c.number_format='"$"#,##0'
        if j==9: c.number_format="0.0"
    r+=1
for ix in NY["indices"]:
    ws.cell(row=r,column=1,value=ix["name"]).font=base; ws.cell(row=r,column=2,value="NYSERDA program average").font=base; ws.cell(row=r,column=5,value=ix["year"]).font=blue; c=ws.cell(row=r,column=7,value=ix["kwh"]); c.font=blue; c.number_format='"$"#,##0'; ws.cell(row=r,column=10,value=ix["source"]).font=base; ws.cell(row=r,column=11,value=ix["confidence"]).font=base; ws.cell(row=r,column=12,value=ix["url"]).font=base; r+=1
ic=NY["interconnection"]; ws.cell(row=r,column=1,value="Con Edison two-part test (CESIR), NY-BEST / NYSEIA filing 11 Mar 2026, Case 24-E-0621").font=base; ws.cell(row=r,column=3,value=ic["mw"]).font=blue; ws.cell(row=r,column=6,value=ic["avg_upgrade_usd"]).font=blue; ws.cell(row=r,column=6).number_format='"$"#,##0'; ws.cell(row=r,column=10,value=f"average interconnection upgrade cost per project across {ic['projects']} projects after the test; about $4,400/kW").font=base; ws.cell(row=r,column=11,value=ic["confidence"]).font=base; ws.cell(row=r,column=12,value=ic["url"]).font=base; r+=1
ws.cell(row=r,column=1,value=NY["note"]).font=note
for col,wdt in zip("ABCDEFGHIJKL",(46,26,12,14,12,16,12,12,8,48,16,60)): ws.column_dimensions[col].width=wdt
ws.freeze_panes="A4"
rd=wb["README"]; lastr=max(c.row for row in rd.iter_rows() for c in row if c.value is not None)
rd.cell(row=lastr+1,column=1,value="2026$ Adjustment").font=bold
rd.cell(row=lastr+1,column=2,value="Dollar-year adjustment of the reference-class comparables to 2026 under five battery indices (selector in B6) with Handy-Whitman or flat non-battery escalation (B7), battery-share input, medians and Hyde Park percentiles; New York distribution-scale cohort summary. Deck slides 12-14. Added 2 Oct 2026.").font=base
wb.save(f"{B}/Hyde_Park_BESS_Cost_Analysis.xlsx"); print("saved", wb.sheetnames)
