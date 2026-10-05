"""Dumbbell chart: each reference-class project, nominal vs 2026$ (installed index, 40% share)."""
import json, numpy as np, matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
B="/tmp/claude-0/-home-user-BESS/078f934e-4ca0-5169-be3f-cb66ff0e2514/scratchpad/build"
A=json.load(open(f"{B}/adjust_results.json")); P=sorted(A["projects"],key=lambda r:r["nominal"])
NAVY="#001E60";GOLD="#FFC72C";BURG="#6E1F2E";GRAY="#9AA3B2";INK="#1F2A44"
fig,ax=plt.subplots(figsize=(7.6,5.4),dpi=220)
ys=np.arange(len(P))
for i,r in enumerate(P):
    ax.plot([r["nominal"],r["adj_installed"]],[i,i],color="#C9D1E0",lw=1.1,zorder=1)
    ax.scatter(r["nominal"],i,s=12,color=GRAY,zorder=2,edgecolor="white",linewidth=.4)
    ax.scatter(r["adj_installed"],i,s=14,color=NAVY if r.get("utility")==1 else "#2A8A8C",zorder=3,edgecolor="white",linewidth=.4)
    ax.text(max(r["nominal"],r["adj_installed"])*1.03,i,f"${r['adj_installed']:,.0f}",fontsize=4.8,va="center",color=INK)
ax.set_yticks(ys); ax.set_yticklabels([f"{r['project'][:34]} ({int(r['mw'])} MW/{int(round(r['mwh']))} MWh, {r['cod_year']})" for r in P],fontsize=4.9)
for v,c,l in ((A["hp"]["installed"],GOLD,"HP installed $833"),(A["hp"]["station_direct"],BURG,"HP station direct $1,483"),(A["hp"]["approval"],BURG,"HP approval $2,862")):
    ax.axvline(v,color=c,lw=1.3,ls="--",zorder=0); ax.text(v*1.02,-0.55,l,rotation=90,fontsize=5.6,va="bottom",ha="left",color=c)
ax.set_xscale("log"); ax.set_xlabel("Dollars per kWh, log scale.  Gray = nominal as reported; filled = 2026 dollars (installed-cost index, 40% battery share)\nNavy = utility-owned, teal = developer-owned",fontsize=6.2)
ax.tick_params(axis="x",labelsize=6.5); ax.set_xticks([300,500,1000,2000,3000]); ax.get_xaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v,_:"$"+f"{v:,.0f}")); ax.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
ax.grid(True,axis="x",color="#E5E9F0",lw=.5); ax.set_ylim(-0.7,len(P)-0.3)
for sp in ("top","right"): ax.spines[sp].set_visible(False)
ax.set_title(f"Reference class, {len(P)} projects at or below 100 MWh: nominal vs 2026$",fontsize=8,loc="left",color=NAVY,fontweight="bold")
plt.tight_layout(); fig.savefig(f"{B}/adjust_dumbbell.png"); plt.close(fig); print("dumbbell saved", len(P))
