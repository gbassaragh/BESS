"""Reference-class and regression analysis of public BESS project costs vs Hyde Park boundaries.
Input: scratchpad/bess_projects.csv (from research agent). Outputs: stats_results.json, PNG charts."""
import json, numpy as np, pandas as pd, statsmodels.api as sm
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
B="/tmp/claude-0/-home-user-BESS/078f934e-4ca0-5169-be3f-cb66ff0e2514/scratchpad/build"
S="/tmp/claude-0/-home-user-BESS/078f934e-4ca0-5169-be3f-cb66ff0e2514/scratchpad"
df=pd.read_csv(f"{S}/bess_projects.csv")
for c in ("mw","mwh","cod_year","cost_usd"): df[c]=pd.to_numeric(df[c],errors="coerce")
df["raw_n"]=len(df)
EXCL={"Nantucket BESS":"cost bundles 15 MW diesel generator and control house","Salem Smart Power Center":"2013 demonstration incl. building and smart-grid controls","Arlington Microgrid":"microgrid incl. solar, building, V2G","Essex Solar + Storage":"bundles 4.9 MW solar","Hot Springs Microgrid":"bundles 2 MW solar; MWh not confirmed","Smarter Network Storage (Leighton Buzzard) [UK]":"R&D demonstration incl. trials","SwRI Solar + Storage (5 MW PV + 10 MW BESS)":"bundles 5 MW solar","Glenarm BESS (for Pasadena Water & Power)":"15-year contract value, not capex","Minnesota utility-owned distribution battery program (200 MW)":"program budget, MWh not stated","Morro Bay BESS (proposed, not built)":"proposed, no COD, developer statement","NineDot Seneca Lake / Boston Rd BESS (Bronx)":"low-confidence cost (conflicting excerpts $25.7M vs $227.8M)","Soltage McDonald BESS (46th St Maspeth)":"probable notice error (>$3,000/kWh; same notice lists Brigis 1A at $16.1M)","Con Edison Storage on Demand mobile BESS (with NRG)":"mobile REV demonstration incl. demo overheads","East Hampton Energy Storage Center (NextEra for LIPA)":"contract value to LIPA, not capex","Boston Medical Center BTM BESS":"behind-the-meter sub-MW customer system","Kapolei Energy Storage":"low-confidence estimate; developer declined to confirm final cost","Weadock BESS (Consumers Energy)":"low-confidence local-press figure"}
df["excluded"]=df.project.map(EXCL)
df=df[df.excluded.isna()]
df=df.dropna(subset=["mwh","cost_usd","cod_year","mw"]); df=df[(df.mwh>0)&(df.cost_usd>0)&(df.mw>0)]
df["dur"]=df.mwh/df.mw; df["kwh"]=df.cost_usd/(df.mwh*1000); df["kw"]=df.cost_usd/(df.mw*1000)
df["utility"]=df.owner_type.str.lower().str.contains("iou|muni|coop|utility|authority|public power|crown",regex=True).astype(int)
df["ne"]=df.state.isin(["MA","CT","NH","RI","VT","ME","NY"]).astype(int)
df["island"]=df.site_type.fillna("").str.lower().str.contains("island|microgrid").astype(int)
df["allin"]=df.scope.fillna("").str.lower().str.contains("all-in|rate base|approved|final|total|incl",regex=True).astype(int)
df["ln_kwh"]=np.log(df.kwh); df["ln_mwh"]=np.log(df.mwh); df["ln_dur"]=np.log(df.dur); df["yr"]=df.cod_year-2020
HP={"b3":832.9,"b4":1483.3,"b6":2862.4,"contract":605.3}
res={"n_total":int(len(df)),"projects_used":df[["project","state","owner_type","mw","mwh","cod_year","cost_usd","kwh","cost_basis","confidence"]].to_dict("records")}
# ---- reference class: distribution-scale (<=100 MWh), any owner with an all-in disclosed cost; utility-only subclass kept for continuity ----
def pct_rank(series,x): return float((series<x).mean())
def rc_block(rc):
    return {"n":int(len(rc)),"median_kwh":float(rc.kwh.median()),"q25":float(rc.kwh.quantile(.25)),"q75":float(rc.kwh.quantile(.75)),"min":float(rc.kwh.min()),"max":float(rc.kwh.max()),
      "n_utility":int(rc.utility.sum()),"n_developer":int((rc.utility==0).sum()),
      "hp_rank":{k:pct_rank(rc.kwh,v) for k,v in HP.items()},"projects":rc[["project","state","owner_type","utility","mw","mwh","cod_year","kwh","cost_basis","confidence"]].sort_values("kwh").to_dict("records")}
rc=df[df.mwh<=100]; rcu=df[(df.utility==1)&(df.mwh<=100)]
res["reference_class"]=rc_block(rc); res["reference_class_utility"]=rc_block(rcu)
# ---- regression ----
y=df.ln_kwh
m0=sm.OLS(y,sm.add_constant(df[["ln_mwh","ln_dur","yr"]])).fit(cov_type="HC1")
res["ols_parsimonious"]={"n":int(m0.nobs),"r2":float(m0.rsquared),"adj_r2":float(m0.rsquared_adj),"resid_sd":float(np.sqrt(m0.scale)),"coef":{k:{"b":float(m0.params[k]),"se":float(m0.bse[k]),"p":float(m0.pvalues[k])} for k in m0.params.index}}
X=df[["ln_mwh","ln_dur","yr","utility","ne"]]; X=sm.add_constant(X)
m=sm.OLS(y,X).fit(cov_type="HC1")
res["ols"]={"n":int(m.nobs),"r2":float(m.rsquared),"adj_r2":float(m.rsquared_adj),"resid_sd":float(np.sqrt(m.scale)),
  "coef":{k:{"b":float(m.params[k]),"se":float(m.bse[k]),"p":float(m.pvalues[k])} for k in m.params.index}}
xh=pd.DataFrame([{"const":1,"ln_mwh":np.log(20),"ln_dur":np.log(2),"yr":8,"utility":1,"ne":1}])
pr=m.get_prediction(xh); sf=pr.summary_frame(alpha=0.2)
pred=float(np.exp(sf["mean"].iloc[0])); lo=float(np.exp(sf["obs_ci_lower"].iloc[0])); hi=float(np.exp(sf["obs_ci_upper"].iloc[0]))
res["ols"]["hp_pred_kwh"]={"p50":pred,"pi80_lo":lo,"pi80_hi":hi}
# percentile of HP boundaries within predictive distribution (lognormal approx with resid sd + param var)
from scipy.stats import norm
mu=float(sf["mean"].iloc[0]); sd=float((sf["obs_ci_upper"].iloc[0]-sf["obs_ci_lower"].iloc[0])/(2*1.2816))
xh0=pd.DataFrame([{"const":1,"ln_mwh":np.log(20),"ln_dur":np.log(2),"yr":8}]); sf0=m0.get_prediction(xh0).summary_frame(alpha=0.2)
mu0=float(sf0["mean"].iloc[0]); sd0=float((sf0["obs_ci_upper"].iloc[0]-sf0["obs_ci_lower"].iloc[0])/(2*1.2816))
res["ols_parsimonious"]["hp_pred_kwh"]={"p50":float(np.exp(mu0)),"pi80_lo":float(np.exp(sf0["obs_ci_lower"].iloc[0])),"pi80_hi":float(np.exp(sf0["obs_ci_upper"].iloc[0]))}
res["ols_parsimonious"]["hp_percentile"]={k:float(norm.cdf((np.log(v)-mu0)/sd0)) for k,v in HP.items()}
res["ols"]["hp_percentile"]={k:float(norm.cdf((np.log(v)-mu)/sd)) for k,v in HP.items()}
# size elasticity check on utility-only subsample
u=df[df.utility==1]
if len(u)>=8:
    Xu=sm.add_constant(u[["ln_mwh","ln_dur","yr"]]); mu2=sm.OLS(u.ln_kwh,Xu).fit(cov_type="HC1")
    res["ols_utility_only"]={"n":int(mu2.nobs),"r2":float(mu2.rsquared),"coef":{k:{"b":float(mu2.params[k]),"p":float(mu2.pvalues[k])} for k in mu2.params.index}}
# ---- charts ----
NAVY="#001E60";GOLD="#FFC72C";BURG="#6E1F2E";TEAL="#2A8A8C";GRAY="#94A3B8"
fig,ax=plt.subplots(figsize=(7.6,4.4),dpi=200)
for ut,col,lab in ((0,GRAY,"Developer / IPP"),(1,NAVY,"Utility-owned")):
    s=df[df.utility==ut]; ax.scatter(s.mwh,s.kwh,s=28,c=col,alpha=.8,label=lab,edgecolor="white",linewidth=.4)
xs=np.logspace(np.log10(max(df.mwh.min(),1)),np.log10(df.mwh.max()),50)
for dur,ls in ((2,"-"),(4,"--")):
    yy=np.exp(m.params["const"]+m.params["ln_mwh"]*np.log(xs)+m.params["ln_dur"]*np.log(dur)+m.params["yr"]*8+m.params["utility"]*1+m.params["ne"]*1)
    ax.plot(xs,yy,ls=ls,color=TEAL,lw=1.4,label=f"Fit: utility, NE, 2028, {dur}-h")
for k,v,c in (("contract",HP["contract"],GOLD),("b3",HP["b3"],GOLD),("b4",HP["b4"],BURG),("b6",HP["b6"],BURG)):
    ax.scatter([20],[v],s=70,marker="D",c=c,edgecolor=NAVY,zorder=5)
    ax.annotate({"contract":"HP vendor contract","b3":"HP battery installed","b4":"HP station complete, direct","b6":"HP approval level"}[k],(20,v),xytext=(6,0),textcoords="offset points",fontsize=7,va="center",color="#1F2A44")
ax.set_xscale("log"); ax.set_yscale("log"); ax.set_xlabel("Energy capacity (MWh), log scale",fontsize=8); ax.set_ylabel("$ per kWh (nominal), log scale",fontsize=8)
ax.tick_params(labelsize=7); ax.grid(True,which="both",color="#E5E9F0",lw=.5); ax.legend(fontsize=7,frameon=False)
for sp in ("top","right"): ax.spines[sp].set_visible(False)
ax.set_title("Public BESS project costs vs size, with Hyde Park boundaries",fontsize=9,loc="left",color=NAVY,fontweight="bold")
plt.tight_layout(); fig.savefig(f"{B}/stats_scatter.png"); plt.close(fig)
# reference class strip chart
fig,ax=plt.subplots(figsize=(7.6,5.4 if len(rc)>20 else 2.6),dpi=220)
rcs=rc.sort_values("kwh")
ax.barh(range(len(rcs)),rcs.kwh,color=[NAVY if u==1 else GRAY for u in rcs.utility],height=.7)
from matplotlib.patches import Patch; ax.legend(handles=[Patch(color=NAVY,label="Utility-owned"),Patch(color=GRAY,label="Developer-owned")],fontsize=6,frameon=False,loc="lower right")
ax.set_yticks(range(len(rcs))); ax.set_yticklabels([f"{p[:34]} ({int(mw)} MW/{int(mwh)} MWh, {int(y)})" for p,mw,mwh,y in zip(rcs.project,rcs.mw,rcs.mwh,rcs.cod_year)],fontsize=(4.9 if len(rcs)>20 else 6))
for v,c,l in ((HP["b3"],GOLD,"HP battery installed $833"),(HP["b4"],BURG,"HP station complete $1,483"),(HP["b6"],BURG,"HP approval $2,862")):
    ax.axvline(v,color=c,lw=1.4,ls="--"); ax.text(v,len(rcs)-0.3,l,rotation=90,fontsize=6,va="top",ha="right",color=c)
ax.set_xlabel("$ per kWh (nominal)",fontsize=8); ax.tick_params(axis="x",labelsize=7)
for sp in ("top","right"): ax.spines[sp].set_visible(False)
ax.set_title(f"Reference class: {len(rc)} projects at or below 100 MWh",fontsize=9,loc="left",color=NAVY,fontweight="bold")
plt.tight_layout(); fig.savefig(f"{B}/stats_refclass.png"); plt.close(fig)
json.dump(res,open(f"{B}/stats_results.json","w"),indent=1,default=str)
print(json.dumps({k:v for k,v in res.items() if k!="reference_class"},indent=1)); print("refclass_utility n",res["reference_class_utility"]["n"],"median",res["reference_class_utility"]["median_kwh"]); print("refclass n",res["reference_class"]["n"],"median",res["reference_class"]["median_kwh"],"hp_rank",res["reference_class"]["hp_rank"])
