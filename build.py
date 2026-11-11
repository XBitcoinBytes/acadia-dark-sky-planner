import json
a=json.load(open('all.json'));d=json.load(open('det.json'));b=json.load(open('bortle.json'))
num=lambda s: float(s.replace('$','').replace(',',''))
meta={
'1196928800896612186':dict(area='Gouldsboro (Schoodic Peninsula)',hot='No',fire='Gas fireplace',game='Garage game room (unheated)',view='Beachfront',winter='Host advertises a winter promo (stay 2 nights, 3rd free); confirm it applies. Game room unheated.'),
'48042667':dict(area='Addison (Downeast inland, ~40 min past Schoodic)',hot='No',fire='Not listed',game='Not listed',view='20 wooded acres',winter='Remote; host warns cell service is limited. Long drive to MDI (~1.5 h).'),
'629677250314896465':dict(area='Gouldsboro (West Bay, Schoodic)',hot='No',fire='Stone fireplace',game='Not listed',view='Waterfront, private peninsula',winter='No winter notes in listing; ask about driveway plowing.'),
'1305300752577177934':dict(area='Gouldsboro (Frenchman Bay shore)',hot='No',fire='Not listed',game='Not listed',view='Ocean view',winter='Duplex (main house + loft apartment); loft stairs narrow and steep. Heated bathroom floor.'),
'979869376223646088':dict(area='Mount Desert (Seal Harbor side, near Jordan Pond Rd)',hot='No',fire='Not listed',game='Not listed',view='5-min walk to trailhead',winter='Baseboard heat plus Generac backup generator. Closest pick to the winter-open Jordan Pond road.'),
'843561346217341307':dict(area='Gouldsboro (Schoodic)',hot='Yes',fire='Propane fireplace (screened gazebo)',game='Game room: arcade, pool table',view='Waterfront compound',winter='Ask if hot tub runs in winter.'),
'51622972':dict(area='Sullivan (inland lake)',hot='No',fire='Gas + stone fireplaces',game='Game room: ping pong, air hockey, foosball',view='Lakefront',winter='Parking for 4 cars plus overflow lot.'),
'1556779144028253495':dict(area='Franklin (inland lake)',hot='Yes',fire='Not listed',game='Theater/game room with pool table',view='Lakefront',winter='Ask if hot tub runs in winter.'),
'39964769':dict(area='Gouldsboro (near Corea)',hot='No',fire='Not listed',game='Not listed',view='Beachfront, 10 acres',winter='Loft sleeps 6; no winter notes.'),
'1635610833138368893':dict(area='Sullivan (Morancy Pond)',hot='Indoor jetted tub only',fire='Not listed',game='Foosball',view='Pondfront',winter='Mini-split heat throughout, marketed for year-round comfort. 9 beds: 1 king, 3 queens, 3 doubles, 2 twins.'),
'52012730':dict(area='Tremont (Bass Harbor)',hot='Indoor Jacuzzi tub only',fire='Fireplace',game='Not listed',view='Log home',winter='Same manager as the other Bass Harbor homes: guests may need to clear light snow; shovel, salt, and sand provided.'),
'1039878328248416312':dict(area='Lamoine',hot='No',fire='Not listed',game='Foosball, air hockey (porch)',view='Panoramic water views',winter='Boiler heat; marketed as "Acadia Four Seasons".'),
'34423277':dict(area='Tremont (near Bass Harbor Light)',hot='No',fire='Not listed',game='Not listed',view='Yard, near lighthouse',winter='Guests may need to clear light snow; outdoor furniture stored Nov–May. Beds: queen; queen + full; king; 2 twins.'),
'556570227801723498':dict(area='Tremont (Bass Harbor)',hot='No',fire='Not listed',game='Not listed',view='New build, fire pit',winter='Guests may need to clear light snow. Beds: king; queen; 2 fulls; full + twin trundle; queen sleeper.'),
'621869887358444638':dict(area='Tremont (Bass Harbor)',hot='No',fire='Not listed',game='Not listed',view='Big lawn, fire pit',winter='Guests may need to clear light snow; long driveway. Beds: king; full + twin trundle; queen; queen; full.'),
'40404479':dict(area='Tremont (abuts Acadia)',hot='No',fire='Fireplace',game='Foosball',view='Abuts park land',winter='"Heat for colder months" listed; guests may need to clear light snow.'),
'852753780325256979':dict(area='Winter Harbor village',hot='No',fire='Not listed',game='Not listed',view='Harbor view (2nd-floor unit)',winter='Second-floor apartment in village; lowest rating in list (4.54).'),
'904507066807073305':dict(area='Mount Desert (Somesville)',hot='No',fire='Not listed',game='Not listed',view='1830s home',winter='Heated bathroom floor.'),
'1664506260570897573':dict(area='Mount Desert (Somesville area)',hot='No',fire='Not listed',game='Not listed',view='EV charger',winter='Mini-split units in bedrooms.'),
'1025695466402390077':dict(area='Tremont (two houses)',hot='No',fire='Not listed',game='Not listed',view='2 min to Acadia',winter='Two separate houses; guests may need to clear light snow.'),
'1174056797624754924':dict(area='Tremont (two houses, back to Acadia)',hot='No',fire='Fireplace',game='Foosball',view='Backs onto park',winter='Two houses; guests may need to clear light snow. Appears to be the same pair Vrbo lists as "Acadia Escape & Blue Lobster" (Vrbo says its hot tub runs only Jul 15–Nov 30).'),
'1549266066852439429':dict(area='Tremont (Duck Cove / lighthouse home)',hot='No',fire='Not listed',game='Not listed',view='Waterfront',winter='Only 3 bedrooms for 16 guests, so mostly shared rooms.'),
'1025698302995362651':dict(area='Tremont (two houses)',hot='No',fire='Not listed',game='Not listed',view='Near water',winter='Two houses; guests may need to clear light snow.'),
'1217472265575202413':dict(area='Mariaville (inland lake, 40 min to MDI)',hot='Yes',fire='Not listed',game='Ping pong, Pop-A-Shot',view='Lakefront',winter='Ask if hot tub runs in winter. Beds include king, queen, bunks, and a daybed with trundle.'),
'48272248':dict(area='Franklin (Taunton Bay)',hot='Indoor jetted tub',fire='Wood-burning stove + fireplace room',game='Pool table, darts',view='Waterfront, "4-season"',winter='Marketed as a 4-season retreat.'),
'1574955649180461943':dict(area='Lamoine',hot='Yes',fire='Propane fireplace',game='Game room: ping pong, Pop-A-Shot, shuffleboard, arcade',view='Oceanfront, 5 acres',winter='Radiant floor heat plus mini-splits; winter photos in listing.'),
'1121257304896908149':dict(area='Mount Desert (Somesville)',hot='Yes (7-person)',fire='Not listed',game='Game room + theater',view='Brookside',winter='Hot tub new in Mar 2024; 3 kings in theater room.'),
'1421065197495083602':dict(area='Hancock (Kilkenny Cove)',hot='Yes',fire='Fireplace not available',game='Ping pong, shuffleboard, arcade',view='Oceanfront',winter='Bookable year-round per host; radiant heat; Starlink internet.'),
'12886133':dict(area='Tremont',hot='Yes',fire='Not listed',game='Game loft: pool, air hockey, shuffleboard',view='Wooded, deck net for stargazing',winter='Host advises 4WD in winter; spotty cell service.'),
'41751559':dict(area='Winter Harbor (½ mi from Schoodic Point)',hot='No',fire='Not listed',game='Not listed',view='Large private yard',winter='Only 1 bathroom for 8 guests.'),
'1187904026331961587':dict(area='Winter Harbor village',hot='No',fire='Not listed',game='Not listed',view='Coastal views to Cadillac',winter='1.5 baths; mentions Bar Harbor ferry, which is summer only.'),
'700192960937194517':dict(area='Southwest Harbor',hot='No',fire='Not listed',game='Game room',view='Wraparound porch',winter='Same Bass Harbor manager: guests may need to clear light snow.'),
'49499575':dict(area='Southwest Harbor (harbor)',hot='No',fire='Not listed',game='Not listed',view='Waterfront, dock',winter='Trundle beds convert twins to kings.'),
'1038535762542430895':dict(area='Ellsworth',hot='Yes (year-round area)',fire='Not listed',game='Arcade room closed Nov–Apr (unheated)',view='Wooded',winter='Advertised as a 4-season home; hot tub area described as year-round.'),
'50053509':dict(area='Bar Harbor (in town)',hot='No',fire='Not listed',game='Game room: ping pong',view='Restored 1908 convent',winter='Brightest skies on the list (in town).'),
'1602603361093266191':dict(area='Bar Harbor (downtown)',hot='No',fire='Not listed',game='Not listed',view='Downtown',winter='Heat pump climate control; in-town light pollution.'),
}
rows=[]
for k,m in meta.items():
    x=a[k]; dd=d[k]; bo=b[k]
    p=num(x['price'])
    bl=x['beds']; g=lambda w: next((s.split()[0] for s in bl if s.split()[-1] in w),'')
    rows.append(dict(id=k,name=x['name'],type=x['title'],area=m['area'],src='Airbnb',guests=dd['cap'],br=g(('bedrooms','bedroom')),beds=g(('beds','bed')),baths=g(('baths','bath')),pre=round(p),nightly=round(p/4),tot=round(p*1.09),pp=round(p*1.09/8),bortle=bo[1],sqm=bo[0],hot=m['hot'],fire=m['fire'],game=m['game'],view=m['view'],winter=m['winter'],rating=x['rating'],url=f'https://www.airbnb.com/rooms/{k}',price='Dated quote'))
# vrbo
rows.append(dict(id='v5170049',name='Roxaboxen – designer waterfront cottage on Duck Cove',type='Vrbo house in Bernard',area='Bernard (Tremont)',src='Vrbo',guests=10,br='4',beds='8+',baths='4.5',pre=None,nightly=None,tot=None,pp=None,bortle=b['REF_Bernard'][1],sqm=b['REF_Bernard'][0],hot='No',fire='Not listed',game='Ping pong game room, telescope loft',view='Oceanfront, west-facing',winter='"Now booking year-round". Base rate covers 6 adults; extra guests $100/person/night, so +$800 for 8 adults over 4 nights. Bunk room: 5 XL twins + queen.',rating='10/10 (Vrbo)',url='https://www.vrbo.com/5170049',price='Not verified'))
rows.append(dict(id='v2365038',name='Captain Nehemiah Young House – Corea harborside',type='Vrbo house in Corea',area='Corea (Gouldsboro, Schoodic)',src='Vrbo / owner',guests=10,br='4',beds='?',baths='2.5',pre=None,nightly=None,tot=None,pp=None,bortle=b['REF_Corea'][1],sqm=b['REF_Corea'][0],hot='No',fire='Electric fireplace',game='Not listed',view='Harbor view deck',winter='Operator (Starlight Lodge) says it offers stays year-round; sleeps 8–10; dog-friendly; cleaning fee extra. Book by phone 207-236-3276 or Vrbo.',rating='9.6/10 (Vrbo)',url='https://www.vrbo.com/2365038',price='Not verified'))
fac={2:1.0,3:1.2,4:1.4,5:1.6}
for r in rows:
    if r['pp'] is None: r['score']=None; continue
    s=r['pp']*fac[r['bortle']]
    try:
        if int(r['beds'])<6: s*=1.1
    except: pass
    r['score']=round(s)
dark=[r for r in rows if r['bortle']<=3 and r['score']]
dark.sort(key=lambda r:r['score'])
for i,r in enumerate(dark): r['rank']=i+1
for r in rows:
    r.setdefault('rank',None)
json.dump(rows,open('rows.json','w'),indent=0)
for r in sorted(rows,key=lambda r:(r['rank'] or 99)):
    print(r['rank'],r['score'],r['pp'],r['bortle'],r['area'],r['guests'],r['br'],r['beds'],r['tot'],r['hot'],r['name'])
print(len(rows))
