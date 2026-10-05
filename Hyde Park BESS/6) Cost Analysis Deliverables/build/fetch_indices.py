"""Pull the per-layer escalator series from FRED and BLS.
Keyless path: FRED's fredgraph.csv endpoint (no key) and the BLS v2 API (no key: 25 series per query, 10 years per query).
Keyed path (optional): FRED_API_KEY and BLS_API_KEY in the environment raise the BLS limits and use the FRED JSON API.
Hosts: fred.stlouisfed.org, api.stlouisfed.org, api.bls.gov. Writes indices_layers_api.json; layer_index_model.py prefers it over
the search-excerpt values in indices_layers.json when a series has 8 or more annual points.
"""
import os, json, sys, csv, io, urllib.request, urllib.parse, collections
B=os.path.dirname(os.path.abspath(__file__))
SERIES={  # FRED id -> (key in layer_index_model, label)
 "WPU117409":("transformer","PPI commodity: power and distribution transformers, except parts (WPU117409, Dec 1999 = 100), annual average"),
 "WPU11740999":("transformer_item","PPI commodity: power and distribution transformers, 8-digit item (WPU11740999, Dec 1999 = 100), annual average"),
 "WPU1175":("switchgear","PPI commodity: switchgear, switchboard, industrial controls (WPU1175, 1982 = 100), annual average"),
 "WPU4532":("engineering","PPI commodity: engineering services (WPU4532, Mar 2009 = 100), annual average"),
 "PCU541330541330":("engineering_industry","PPI industry: engineering services (PCU541330541330, Dec 1996 = 100), annual average"),
 "CIU2012300000000I":("eci_construction","ECI: total compensation, private industry, construction (CIU2012300000000I, Dec 2005 = 100), annual average of quarters"),
 "WPUIP2300001":("construction_inputs","PPI: net inputs to construction industries, goods (WPUIP2300001, Jun 1986 = 100), annual average"),
 "WPU117":("electrical_equipment","PPI commodity: electrical machinery and equipment (WPU117, 1982 = 100), annual average"),
 "WPUSI012011":("construction_materials","PPI special index: construction materials (WPUSI012011, 1982 = 100), annual average"),
 "PCU335313335313":("switchgear_industry","PPI industry: switchgear and switchboard apparatus mfg (PCU335313335313, Jun 1985 = 100), annual average"),
}
def fred_csv(sid):
    with urllib.request.urlopen(f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={sid}",timeout=30) as r: txt=r.read().decode()
    rows=list(csv.reader(io.StringIO(txt))); hdr=rows[0]; acc=collections.defaultdict(list)
    for d,v in rows[1:]:
        if v not in (".",""): acc[d[:4]].append(float(v))
    return {y:round(sum(v)/len(v),3) for y,v in acc.items() if int(y)>=2014}, {y:len(v) for y,v in acc.items() if int(y)>=2014}
def fred_api(sid,key):
    q=urllib.parse.urlencode({"series_id":sid,"api_key":key,"file_type":"json","frequency":"a","aggregation_method":"avg","observation_start":"2014-01-01"})
    with urllib.request.urlopen(f"https://api.stlouisfed.org/fred/series/observations?{q}",timeout=30) as j: d=json.load(j)
    return {o["date"][:4]:float(o["value"]) for o in d["observations"] if o["value"] not in (".","")}
def bls(sids,key=None,start=2014,end=2026):
    body={"seriesid":sids,"startyear":str(start),"endyear":str(end),"annualaverage":True}
    if key: body["registrationkey"]=key
    req=urllib.request.Request("https://api.bls.gov/publicAPI/v2/timeseries/data/",data=json.dumps(body).encode(),headers={"Content-type":"application/json"})
    with urllib.request.urlopen(req,timeout=60) as r: j=json.load(r)
    out={}
    for s in j.get("Results",{}).get("series",[]):
        ann={d["year"]:float(d["value"]) for d in s["data"] if d["period"]=="M13"}
        months=collections.defaultdict(list)
        for d in s["data"]:
            if d["period"].startswith("M") and d["period"]!="M13": months[d["year"]].append(float(d["value"]))
        for y,v in months.items(): ann.setdefault(y,round(sum(v)/len(v),3))   # partial year: average of months published so far
        out[s["seriesID"]]={"annual":ann,"months":{y:len(v) for y,v in months.items()},"messages":j.get("message",[])}
    return out
if __name__=="__main__":
    fk=os.environ.get("FRED_API_KEY"); bk=os.environ.get("BLS_API_KEY"); res={}
    for sid,(k,lab) in SERIES.items():
        try:
            pts,nobs=(fred_api(sid,fk),{}) if fk else fred_csv(sid)
            res[k]={"label":lab,"series_id":sid,"source":"FRED "+("API" if fk else "fredgraph.csv")+" (BLS data), retrieved "+__import__("datetime").date.today().isoformat(),"conf":"High (published observations; the latest year is a partial-year average)","points":pts,"obs_per_year":nobs}
            print("FRED ok",sid,min(pts),"-",max(pts),"last",pts[max(pts)])
        except Exception as e: print("FRED fail",sid,e,file=sys.stderr)
    try:
        got=bls(list(SERIES),bk,2017,2026)   # keyless limit: 10 years per query
        for sid,d in got.items():
            k,lab=SERIES[sid]; cur=res.get(k)
            if cur is None or (d["annual"] and max(d["annual"])>max(cur["points"])):
                res[k]={"label":lab,"series_id":sid,"source":"BLS API v2, retrieved "+__import__("datetime").date.today().isoformat(),"conf":"High","points":{**(cur["points"] if cur else {}),**d["annual"]},"obs_per_year":d["months"]}
            elif cur: cur["bls_check"]={y:v for y,v in d["annual"].items()}
        print("BLS ok",len(got),"series; messages:",got[list(got)[0]]["messages"] if got else None)
    except Exception as e: print("BLS fail",e,file=sys.stderr)
    if res: json.dump(res,open(f"{B}/indices_layers_api.json","w"),indent=1); print("wrote indices_layers_api.json")
