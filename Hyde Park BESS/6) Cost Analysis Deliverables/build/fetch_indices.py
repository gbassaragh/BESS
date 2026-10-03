"""Pull the per-layer escalator series from FRED and BLS once the environment allows those hosts.
Keys are read from the environment: FRED_API_KEY, BLS_API_KEY (never hard-code them).
Hosts to allow in the cloud environment's network policy: api.stlouisfed.org, api.bls.gov.
Writes indices_layers_api.json next to this script; layer_index_model.py prefers it over the
search-excerpt file indices_layers.json when present and complete.
"""
import os, json, sys, urllib.request, urllib.parse
B=os.path.dirname(os.path.abspath(__file__))
FRED={  # series id -> (key used by layer_index_model, label)
 "WPU11740999":("transformer","PPI: power and distribution transformers (BLS, via FRED)"),
 "WPU1175":("switchgear","PPI: switchgear, switchboard, industrial controls (BLS, via FRED)"),
 "PCU541330541330":("engineering","PPI: engineering services (BLS, via FRED)"),
 "CIU2012300000000I":("labor","ECI: total compensation, private, construction (BLS, via FRED)"),
 "WPUIP2311001":("civil","PPI: inputs to construction industries (BLS, via FRED)"),
 "WPU10":("metals","PPI: metals and metal products (BLS, via FRED)"),
}
def fred(sid,key):
    q=urllib.parse.urlencode({"series_id":sid,"api_key":key,"file_type":"json","frequency":"a","aggregation_method":"avg","observation_start":"2014-01-01"})
    with urllib.request.urlopen(f"https://api.stlouisfed.org/fred/series/observations?{q}",timeout=30) as r: j=json.load(r)
    return {o["date"][:4]:float(o["value"]) for o in j["observations"] if o["value"] not in (".","")}
def bls(sids,key):
    body=json.dumps({"seriesid":sids,"startyear":"2014","endyear":"2026","annualaverage":True,"registrationkey":key}).encode()
    req=urllib.request.Request("https://api.bls.gov/publicAPI/v2/timeseries/data/",data=body,headers={"Content-type":"application/json"})
    with urllib.request.urlopen(req,timeout=60) as r: j=json.load(r)
    out={}
    for s in j["Results"]["series"]:
        out[s["seriesID"]]={d["year"]:float(d["value"]) for d in s["data"] if d["period"]=="M13"}  # M13 = annual average
    return out
if __name__=="__main__":
    fk=os.environ.get("FRED_API_KEY"); bk=os.environ.get("BLS_API_KEY"); res={}
    if fk:
        for sid,(k,lab) in FRED.items():
            try: res[k]={"label":lab,"series_id":sid,"source":"FRED API","conf":"High","points":fred(sid,fk)}; print("FRED ok",sid,len(res[k]["points"]))
            except Exception as e: print("FRED fail",sid,e,file=sys.stderr)
    if bk:
        try:
            got=bls(list(FRED),bk)
            for sid,pts in got.items():
                k,lab=FRED[sid]
                if k not in res or len(pts)>len(res[k]["points"]): res[k]={"label":lab.replace("via FRED","BLS API"),"series_id":sid,"source":"BLS API v2","conf":"High","points":pts}
            print("BLS ok",len(got))
        except Exception as e: print("BLS fail",e,file=sys.stderr)
    if res: json.dump(res,open(f"{B}/indices_layers_api.json","w"),indent=1); print("wrote indices_layers_api.json")
    else: print("no keys in environment (FRED_API_KEY / BLS_API_KEY) or no host access; nothing written")
