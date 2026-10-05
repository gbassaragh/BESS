import json, numpy as np, matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
B="/tmp/claude-0/-home-user-BESS/078f934e-4ca0-5169-be3f-cb66ff0e2514/scratchpad/build"
R=json.load(open(f"{B}/mc_scope_results.json")); NAVY="#001E60";GOLD="#FFC72C";BURG="#6E1F2E";TEAL="#2A8A8C";GRAY="#9AA3B2";INK="#1F2A44";LIGHT="#C9D1E0"
# ---- tornado: opportunities left, threats right, accuracy two-sided, schedule right; top 18 by magnitude ----
rows=R["tornado"][:18][::-1]
fig,ax=plt.subplots(figsize=(7.8,5.6),dpi=220)
for i,r in enumerate(rows):
    lo,hi=r["p10"]/1e6,r["p90"]/1e6; col={"opportunity":TEAL,"threat":BURG,"accuracy":GRAY,"schedule":NAVY}[r["kind"]]
    ax.barh(i,hi-lo,left=lo,color=col,height=0.62,zorder=2)
    ax.plot(r["mean"]/1e6,i,marker="|",color="white" if r["kind"]!="accuracy" else INK,markersize=9,mew=1.6,zorder=3)
    lab=f"{lo:+.1f} to {hi:+.1f}" if abs(hi-lo)>0.05 else f"{lo:+.1f}"
    ax.text((hi+0.15) if hi>0 or r["kind"]=="threat" else (lo-0.15),i,lab,va="center",ha="left" if (hi>0 or r["kind"]=="threat") else "right",fontsize=6.4,color=INK)
ax.set_yticks(range(len(rows))); ax.set_yticklabels([r["driver"] for r in rows],fontsize=6.6)
ax.axvline(0,color=INK,lw=0.8); ax.set_xlabel("Effect on the loaded total, \\$M (P10 to P90 of each driver's own contribution; tick = mean)",fontsize=7)
ax.set_xlim(-3.5,10.5); ax.tick_params(axis="x",labelsize=7); ax.grid(True,axis="x",color="#E5E9F0",lw=.5,zorder=0)
for sp in ("top","right"): ax.spines[sp].set_visible(False)
import matplotlib.patches as mp
ax.legend(handles=[mp.Patch(color=TEAL,label="Opportunity (lever pursued)"),mp.Patch(color=BURG,label="Threat (not in the estimate)"),mp.Patch(color=GRAY,label="Estimate accuracy (two-sided)"),mp.Patch(color=NAVY,label="Schedule slip")],fontsize=6.6,loc="lower right",frameon=False)
ax.set_title("Opportunities and threats on the Hyde Park total",fontsize=8.5,loc="left",color=NAVY,fontweight="bold")
plt.tight_layout(); fig.savefig(f"{B}/mc_scope_tornado.png"); plt.close(fig)
# ---- histogram of the three postures ----
sq=np.load(f"{B}/mc_scope_status_quo.npy")/1e6; mg=np.load(f"{B}/mc_scope_managed.npy")/1e6; ce=np.load(f"{B}/mc_scope_ceiling.npy")/1e6
fig,ax=plt.subplots(figsize=(6.4,3.3),dpi=220)
bins=np.linspace(40,85,91)
for x,col,lab in ((sq,BURG,"Status quo: no lever pursued"),(mg,NAVY,"Managed: levers at assessed odds"),(ce,TEAL,"Ceiling: every lever realized")):
    ax.hist(x,bins=bins,alpha=0.55,color=col,label=f"{lab} (P50 \\${np.percentile(x,50):.1f}M, P80 \\${np.percentile(x,80):.1f}M)")
ax.axvline(R["approval"]/1e6,color=GOLD,lw=1.6,ls="--"); ax.text(R["approval"]/1e6+0.3,ax.get_ylim()[1]*0.93,"Approval \\$57.2M",fontsize=6.5,color=INK)
ax.set_xlabel("Loaded project outcome, \\$M (20,000 trials)",fontsize=7); ax.set_yticks([]); ax.tick_params(axis="x",labelsize=7); ax.legend(fontsize=6.2,frameon=False,loc="upper right")
for sp in ("top","right","left"): ax.spines[sp].set_visible(False)
plt.tight_layout(); fig.savefig(f"{B}/mc_scope_hist.png"); plt.close(fig)
# ---- schedule ----
sl=np.load(f"{B}/mc_scope_slip.npy")
fig,ax=plt.subplots(figsize=(6.4,1.9),dpi=220)
ax.hist(sl,bins=np.arange(-1.5,26.5,1),color=NAVY,alpha=0.8)
for p,c in ((50,GOLD),(80,BURG)): v=np.percentile(sl,p); ax.axvline(v,color=c,lw=1.4,ls="--"); ax.text(v+0.2,ax.get_ylim()[1]*0.85,f"P{p}: +{v:.0f} mo",fontsize=6.5,color=INK)
ax.set_xlabel("Months after the 28 Dec 2028 in-service date (siting chain, long-lead equipment, construction variance; EFSB path 8%)",fontsize=6.5); ax.set_yticks([]); ax.tick_params(axis="x",labelsize=7)
for sp in ("top","right","left"): ax.spines[sp].set_visible(False)
plt.tight_layout(); fig.savefig(f"{B}/mc_scope_sched.png"); plt.close(fig); print("charts saved")
