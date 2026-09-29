import json, numpy as np
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
B="/tmp/claude-0/-home-user-BESS/078f934e-4ca0-5169-be3f-cb66ff0e2514/scratchpad/build"
NAVY="#001E60";GOLD="#FFC72C";BURG="#6E1F2E";TEAL="#2A8A8C";GRAY="#94A3B8"
base=np.load(f"{B}/mc_total_excl_JK.npy")/1e6; wide=np.load(f"{B}/mc_total_excl_JK_wide.npy")/1e6
r=json.load(open(f"{B}/mc_results.json")); rw=json.load(open(f"{B}/mc_results_wide.json"))
fig,ax=plt.subplots(figsize=(7.6,3.4),dpi=200)
ax.hist(base,bins=80,color=NAVY,alpha=.85,label="Base element ranges"); ax.hist(wide,bins=80,color=TEAL,alpha=.55,label="Wide (Class 5-like) ranges")
ax.axvline(57.2473,color=BURG,lw=1.6,ls="--"); ax.text(57.35,ax.get_ylim()[1]*.92,"Approval level $57.2M\n(incl. $7.6M risk + contingency)",fontsize=7,color=BURG)
det=(r["det_by_layer"]["A"]+r["det_by_layer"]["B"]+r["det_by_layer"]["C"]+r["det_by_layer"]["D"]+r["det_by_layer"]["E"]+r["det_by_layer"]["G"]+r["det_by_layer"]["H"]+r["det_by_layer"]["I"]+r["det_by_layer"]["F"]+8064672+4680899)/1e6
ax.axvline(det,color=GOLD,lw=1.6); ax.text(det-0.2,ax.get_ylim()[1]*.92,f"Deterministic, no risk/contingency\n${det:.1f}M",fontsize=7,color="#7a5b00",ha="right")
for p,c in ((50,NAVY),(80,NAVY)):
    v=r["total_excl_JK"][str(p)]/1e6; ax.axvline(v,color=c,lw=.8,ls=":"); ax.text(v,ax.get_ylim()[1]*.6,f"P{p} ${v:.1f}M",fontsize=6.5,rotation=90,va="top",ha="right",color=c)
ax.set_xlabel("Project 21334 total, $M (element uncertainty, no separate risk/contingency lines)",fontsize=8); ax.set_yticks([]); ax.tick_params(labelsize=7); ax.legend(fontsize=7,frameon=False,loc="center right")
for sp in ("top","right","left"): ax.spines[sp].set_visible(False)
ax.set_title("Monte Carlo on the thirteen layers: where the risk and contingency reserve lands",fontsize=9,loc="left",color=NAVY,fontweight="bold")
plt.tight_layout(); fig.savefig(f"{B}/mc_hist.png"); plt.close(fig)
# tornado: std by layer, base and wide
names={"A":"A Battery contract (change orders)","B":"B Battery install labor basis","C":"C GSUs / EMS / aux power","D":"D Station 360 switching","E":"E Landfill site platform","F":"F Station 496 protection","G":"G Testing & commissioning","H":"H Engineering, siting, PM","I":"I Taxes, CWIP, BAR"}
ks=sorted(r["contributions"],key=lambda k:r["contributions"][k])
fig,ax=plt.subplots(figsize=(7.6,3.0),dpi=200)
ax.barh([names[k] for k in ks],[rw["contributions"][k]/1e6 for k in ks],color=TEAL,alpha=.5,label="Wide ranges")
ax.barh([names[k] for k in ks],[r["contributions"][k]/1e6 for k in ks],color=NAVY,label="Base ranges")
ax.set_xlabel("Standard deviation of layer cost, $M",fontsize=8); ax.tick_params(labelsize=7); ax.legend(fontsize=7,frameon=False,loc="lower right")
for sp in ("top","right"): ax.spines[sp].set_visible(False)
ax.set_title("Which layers drive the uncertainty",fontsize=9,loc="left",color=NAVY,fontweight="bold")
plt.tight_layout(); fig.savefig(f"{B}/mc_tornado.png"); plt.close(fig); print("charts ok, det",det)
