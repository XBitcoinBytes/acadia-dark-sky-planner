import json,re,sys,base64,html
def parse(fn):
    t=open(fn).read()
    m=re.search(r'<script id="data-deferred-state-0"[^>]*>(.*?)</script>',t,re.S)
    if not m: return None,[]
    d=json.loads(m.group(1))['niobeClientData'][0]
    r=d[1]['data']['presentation']['staysSearch']['results']
    title=None
    try: title=r['sectionConfiguration']['pageTitleSections']['sections'][0]['sectionData']['structuredTitle']
    except Exception: pass
    out=[]
    for it in r['searchResults']:
        dl=it.get('demandStayListing') or {}
        if not dl: continue
        lid=base64.b64decode(dl['id']).decode().split(':')[1]
        pl=[x.get('body') for x in (it.get('structuredContent') or {}).get('primaryLine') or []]
        sp=it.get('structuredDisplayPrice') or {}
        p=sp.get('primaryLine') or {}
        price=p.get('price') or p.get('discountedPrice')
        expl=[]
        try:
            for pd in sp['explanationData']['priceDetails']:
                for i in pd['items']: expl.append((i.get('description'),i.get('priceString')))
        except Exception: pass
        c=dl['location']['coordinate']
        out.append(dict(id=lid,title=it.get('title'),name=it.get('subtitle') or (it.get('nameLocalized') or {}).get('localizedStringWithTranslationPreference'),beds=pl,price=price,qual=p.get('qualifier'),a11y=p.get('accessibilityLabel'),expl=expl,rating=it.get('avgRatingLocalized'),lat=c['latitude'],lng=c['longitude']))
    return title,out
if __name__=='__main__':
    for f in sys.argv[1:]:
        ti,o=parse(f); print(f,ti,len(o))
        for x in o: print(json.dumps(x))
