"""Merge the build-status audit (5 Oct 2026) into bess_projects.csv: columns status, cod_actual, cost_type, status_confidence, status_note.
Built = status begins with 'operating'. Reads every CSV under scratchpad/status_audit/."""
import csv, glob, os
S="/tmp/claude-0/-home-user-BESS/078f934e-4ca0-5169-be3f-cb66ff0e2514/scratchpad"
aud={}
for f in glob.glob(f"{S}/status_audit/*.csv"):
    for r in csv.DictReader(open(f)): aud[r["project"].strip()]=r
rows=list(csv.DictReader(open(f"{S}/bess_projects.csv"))); flds=list(rows[0].keys())
for c in ("status","cod_actual","cost_type","status_confidence","status_note"):
    if c not in flds: flds.append(c)
miss=[]
for r in rows:
    a=aud.get(r["project"].strip())
    if a:
        r["status"]=a.get("status",""); r["cod_actual"]=a.get("cod_actual",""); r["cost_type"]=a.get("cost_type",""); r["status_confidence"]=a.get("status_confidence",""); r["status_note"]=(a.get("note","")+" "+a.get("actual_cost_note","")).strip()
    else:
        r.setdefault("status",""); miss.append(r["project"])
w=csv.DictWriter(open(f"{S}/bess_projects.csv","w",newline=""),fieldnames=flds); w.writeheader(); w.writerows(rows)
print(len(rows),"rows;",len(aud),"audited;",len(miss),"not matched:",miss[:40])
