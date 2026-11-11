import json,re,subprocess,time
a=json.load(open('all.json'))
res={}
try: res=json.load(open('bortle.json'))
except Exception: pass
pts={}
for k,v in a.items():
    pts[k]=(round(v['lat'],2),round(v['lng'],2))
# extra reference points
refs={'REF_Seawall':(44.24,-68.30),'REF_SchoodicPt':(44.33,-68.06),'REF_BarHarborTown':(44.39,-68.21),'REF_Ellsworth':(44.54,-68.42),'REF_Corea':(44.40,-67.98),'REF_SealCove':(44.29,-68.40),'REF_Bernard':(44.24,-68.36)}
pts.update(refs)
cache={}
for k,(la,lo) in pts.items():
    if k in res: continue
    key=f"{la:.2f}/{lo:.2f}"
    if key not in cache:
        t=subprocess.run(['curl','-s','-m','20','-A','Mozilla/5.0',f'https://clearoutside.com/forecast/{key}'],capture_output=True,text=True).stdout
        m=re.search(r'Sky Quality:.*?<strong>([\d.]+)</strong>.*?Class (\d)',re.sub(r'\s+',' ',t))
        m2=re.search(r'Est\. Sky Quality: &nbsp;<strong>([\d.]+)</strong>.*?<strong>Class (\d)</strong>',re.sub(r'\s+',' ',t))
        mm=m or m2
        cache[key]=(float(mm.group(1)),int(mm.group(2))) if mm else None
        if not mm: print('fail',key,len(t))
        time.sleep(1)
    res[k]=cache[key]
    json.dump(res,open('bortle.json','w'))
print(len(res)); print({k:v for k,v in res.items() if k.startswith('REF')})
