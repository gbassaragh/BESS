import json, os, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, matplotlib.patches as mp
B=os.path.dirname(os.path.abspath(__file__)); R=json.load(open(f"{B}/mc_scope_results.json"))
NAVY="#001E60"; GOLD="#FFC72C"; BURG="#6E1F2E"; TEAL="#2A8A8C"; GRAY="#9AA3B2"; INK="#1F2A44"
rows=sorted(R["tornado"],key=lambda r:-(r["p90"]-r["p10"]))[:10]
SHORT={"T1":"Haugland reconciliation (threat)","Sc":"Siting and schedule slip","B2":"B2 Two-feeder topology","A4":"A4 E&S overhead basis","A1":"A1 Battery escalation","A2":"A2 Risk lines duplicating escalation","B1":"B1 Relay program at benchmark","T6":"T6 GSU count: twelve, not four","B4":"B4 Install crew build-up","B3":"B3 Civil after geotech"}
def lab(r):
    d=r["driver"]; k=d[:2]
    if d.startswith("Accuracy"): return d.replace("Accuracy: ","Estimate accuracy, ").split(" (")[0]
    return SHORT.get(k,d)
fig,ax=plt.subplots(figsize=(7.0,4.6),dpi=220)
for i,r in enumerate(rows):
    lo,hi=r["p10"]/1e6,r["p90"]/1e6; col={"threat":BURG,"opportunity":TEAL,"accuracy":GRAY,"schedule":NAVY}[r["kind"]]
    ax.barh(i,hi-lo,left=lo,color=col,height=0.64,zorder=2)
    ax.plot(r["mean"]/1e6,i,marker="|",color="white" if r["kind"]!="accuracy" else INK,markersize=11,mew=1.8,zorder=3)
    t=f"{lo:+.1f} to {hi:+.1f}"
    ax.text(max(hi,0)+0.15,i,t,va="center",ha="left",fontsize=8.5,color=INK)
ax.set_yticks(range(len(rows))); ax.set_yticklabels([lab(r) for r in rows],fontsize=9); ax.invert_yaxis()
ax.axvline(0,color=INK,lw=0.8); ax.set_xlabel("Effect on the loaded total, \\$M (P10 to P90; tick = mean)",fontsize=8.5)
ax.set_xlim(-2.6,11.8); ax.tick_params(axis="x",labelsize=8.5); ax.grid(True,axis="x",color="#E5E9F0",lw=.5,zorder=0)
for sp in ("top","right"): ax.spines[sp].set_visible(False)
ax.legend(handles=[mp.Patch(color=BURG,label="Threat not in the estimate"),mp.Patch(color=NAVY,label="Schedule slip"),mp.Patch(color=GRAY,label="Estimate accuracy (two-sided)"),mp.Patch(color=TEAL,label="Opportunity if pursued")],fontsize=8,loc="lower right",frameon=False)
ax.set_title("Ten largest drivers, 20,000 trials",fontsize=10,loc="left",color=NAVY,fontweight="bold")
plt.tight_layout(); fig.savefig(f"{B}/mc_lead_tornado.png"); print("saved")
