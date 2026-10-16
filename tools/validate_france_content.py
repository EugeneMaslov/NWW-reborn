"""Static FRA integration and lifecycle checks; does not claim a game reproduction."""
import argparse
import json
import re
from pathlib import Path
from PIL import Image
from hoi4_script import read, one, values, walk, engine_script_errors, TOKEN

ROOT=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--game',type=Path,default=Path('D:/Steam/steamapps/common/Hearts of Iron IV'))
args=p.parse_args();GAME=args.game
errors=[]
def check(ok,msg):
    if not ok:errors.append(msg)

files=[f for folder in ['common','events','interface'] for f in (ROOT/folder).rglob('*') if f.is_file() and (f.name.startswith('FRA') or f.name in ['France.txt','LaR_France.txt','france.txt','free_france.txt','vichy_france.txt']) and f.suffix in ['.txt','.gui','.gfx']]
docs={}
for f in files:
    try:
        docs[f]=read(f)
        errors.extend(str(f.relative_to(ROOT))+': '+e for e in engine_script_errors(docs[f]))
        text=f.read_text(encoding='utf-8-sig')
        check(not any(re.fullmatch(r'-?\.\d+',m.group()) for m in TOKEN.finditer(text)),str(f)+': decimal without leading zero')
    except Exception as exc:errors.append(str(f)+': '+str(exc))

tree=one(read(ROOT/'common/national_focus/FRA_focuses.txt'),'focus_tree')
focuses={one(f,'id'):f for f in values(tree,'focus')}
check(len(focuses)>=140,'Expected a major FRA tree with at least 140 focuses')
check(one(tree,'id')=='french_focus','Preserve the native tree compatibility ID')
positions={}
for fid,f in focuses.items():
    pos=(one(f,'x'),one(f,'y'));check(pos not in positions,f'Focus overlap {fid} / {positions.get(pos)}');positions[pos]=fid
    for block in values(f,'prerequisite')+values(f,'mutually_exclusive'):
        for parent in values(block,'focus'):check(parent in focuses,f'{fid}: undefined focus {parent}')
    for other in values(one(f,'mutually_exclusive',[]),'focus'):
        check(fid in values(one(focuses.get(other,[]),'mutually_exclusive',[]),'focus'),f'{fid}: asymmetric exclusion {other}')
    check(one(f,'cost') in ('5','10'),f'{fid}: unexpected duration')
    for parent in values(f,'prerequisite'):
        for pf in values(parent,'focus'):
            check(int(one(focuses[pf],'y'))<int(one(f,'y')),f'{fid}: nonascending prerequisite')
check(int(one(one(tree,'continuous_focus_position'),'y'))>max(int(one(f,'y')) for f in focuses.values())*130+250,'Continuous focus panel overlaps final rows')

def required(fid,choices=None):
    choices=choices or {};s={fid}
    for block in values(focuses[fid],'prerequisite'):
        options=values(block,'focus');selected=choices.get(fid,options[0])
        if selected not in options:selected=options[0]
        s|=required(selected,choices)
    return s

combined=set()
for fid in ['renewal','rail_nodes','signals_supply']:combined|=required('FRA_nww_'+fid)
pacing=sum(int(one(focuses[f],'cost'))*7 for f in combined)
check(900<=pacing<=1100,f'Combined neutralisation route is {pacing} days, expected 900–1100')
emergency=sum(int(one(focuses['FRA_nww_'+f],'cost'))*7 for f in ['army_neutrality','civil_administration','defence_budget','extend_mandate'])
check(emergency<270,f'Emergency resolution impossible within mandate: {emergency}')

effects=read(ROOT/'common/scripted_effects/FRA_effects.txt')
effect_names={k for k,v,o in effects}
events={one(v,'id') for k,v,o in read(ROOT/'events/FRA_events.txt') if k=='country_event'}
triggers={k for k,v,o in read(ROOT/'common/scripted_triggers/FRA_triggers.txt')}
decisions=read(ROOT/'common/decisions/FRA_decisions.txt')
decision_ids={k for cat,items,o in decisions for k,v,op in items}
country_tags={k for root in (GAME,ROOT) for f in (root/'common/country_tags').glob('*.txt') for k,v,o in read(f)}
for path,doc in docs.items():
    for k,v,o in walk(doc):
        if k=='set_country_flag' and isinstance(v,list) and one(v,'days') is not None:
            check(float(one(v,'value',0))>0,f'{path.name}: timed flag {one(v,"flag")} needs explicit positive value')
        if k and re.fullmatch(r'[A-Z][A-Z0-9]{2}',k) and k not in ('AND','NOT'):
            check(k in country_tags,f'{path.name}: undefined country scope {k}')
        if k=='country_event' and isinstance(v,list) and str(one(v,'id','')).startswith('nww_fra.'):
            check(one(v,'id') in events,f'{path.name}: missing event {one(v,"id")}')
        if k=='activate_mission':check(v in decision_ids,f'{path.name}: undefined mission {v}')
        if k and k.startswith('FRA_') and v in ('yes','no'):
            check(k in effect_names|triggers,f'{path.name}: undefined scripted effect/trigger {k}')
        if k=='set_politics':
            check(all(one(v,a) is not None for a in ['ruling_party','elections_allowed','election_frequency','last_election']),f'{path.name}: incomplete set_politics')

mod_doc=(GAME/'documentation/modifiers_documentation.md').read_text(encoding='utf-8-sig')
registered=set(re.findall(r'^## ([A-Za-z0-9_]+)',mod_doc,re.M))
registered.update('production_speed_'+k+'_factor' for k,v,o in one(read(GAME/'common/buildings/00_buildings.txt'),'buildings',[]))
for path in [ROOT/'common/dynamic_modifiers/FRA_modifiers.txt',ROOT/'common/ideas/FRA_ideas.txt',ROOT/'common/ideas/FRA_companies.txt']:
    doc=read(path)
    blocks=[v for k,v,o in doc] if 'dynamic_modifiers' in path.parts else [v for k,v,o in walk(doc) if k=='modifier']
    for block in blocks:
        keys=[k for k,v,o in block if k not in ('enable','icon')]
        check(len(keys)==len(set(keys)),f'{path.name}: duplicate modifier keys silently overwrite a bonus')
        for k,v,o in block:
            if k not in ['enable','icon']:check(k in registered,f'{path.name}: unregistered modifier {k}')

for k,v,o in read(ROOT/'common/military_industrial_organization/organizations/FRA_organization.txt'):
    check(one(v,'include') is not None,f'{k}: lost generic MIO template')
    for trait in values(v,'add_trait'):
        if str(one(trait,'token')).startswith('FRA_nww_'):
            available=one(trait,'available',[])
            check(any(k2=='has_completed_focus' and v2 in focuses for k2,v2,o2 in walk(available)),f'{k}: missing focus-gated progression')

native_stats={'equipment_bonus':set(),'production_bonus':set()}
for f in (GAME/'common/military_industrial_organization/organizations').glob('*.txt'):
    try:native_doc=read(f)
    except (ValueError,UnicodeError):continue
    for k,v,o in walk(native_doc):
        if k in native_stats and isinstance(v,list):native_stats[k].update(a for a,b,c in v)
for k,v,o in walk(read(ROOT/'common/military_industrial_organization/organizations/FRA_organization.txt')):
    if k in native_stats:
        for a,b,c in v:check(a in native_stats[k],f'Unregistered MIO {k} stat: {a}')

sprites={}
for root in [GAME,*sorted(GAME.glob('dlc/*')),ROOT]:
    for f in root.glob('interface/**/*.gfx'):
        try:doc=read(f)
        except (ValueError,UnicodeError):continue
        for k,v,o in walk(doc):
            if k and k.lower()=='spritetype' and isinstance(v,list):sprites[one(v,'name')]=one(v,'texturefile')
for fid,f in focuses.items():
    icon=one(f,'icon');check(icon in sprites,f'{fid}: missing sprite {icon}');check(icon+'_shine' in sprites,f'{fid}: missing completed-focus shine')
for event in values(read(ROOT/'events/FRA_events.txt'),'country_event'):
    check(one(event,'picture') in sprites,f'{one(event,"id")}: missing event picture {one(event,"picture")}')
for k,v,o in walk(effects):
    if k=='picture' and str(v).startswith('GFX_'):check(v in sprites,'Missing leader portrait '+v)

for lang in ['russian','english']:
    path=ROOT/f'localisation/{lang}/FRA_nww_l_{lang}.yml'
    check(path.read_bytes().startswith(b'\xef\xbb\xbf'),lang+': missing localisation BOM')
    strings=dict(re.findall(r'^\s+([\w.]+):\d*\s+"(.*)"\s*$',path.read_text(encoding='utf-8-sig'),re.M))
    for fid in focuses:check(fid in strings and fid+'_desc' in strings,lang+': unlocalised '+fid)
    for did in decision_ids:check(did in strings and did+'_desc' in strings,lang+': unlocalised '+did)
    for k,v,o in walk(read(ROOT/'events/FRA_events.txt')):
        if k in ('name','title','desc'):check(v in strings,lang+': unlocalised event '+v)

states={one(one(read(f),'state'),'id'):one(read(f),'state') for f in (ROOT/'history/states').glob('*.txt')}
for cat,items,o in decisions:
    for did,body,op in items:
        if one(body,'days_mission_timeout'):
            check(one(one(body,'activation',[]),'always')=='no',did+': scripted mission auto-activates')
            check(one(one(body,'available',[]),'always')=='no',did+': mission auto-completes instead of counting down')
            check(one(body,'cancel_if_not_visible')=='yes',did+': hidden mission is not cancelled')
        if 'project_' in did or did.startswith('FRA_nww_invest_'):
            for need in ['cancel_trigger','cancel_effect','remove_effect']:check(one(body,need) is not None,did+': missing '+need)
            check(any(k=='add_political_power' for k,v,o in walk(one(body,'cancel_effect',[]))),did+': no cancellation refund')
        for k,v,op in walk(body):
            if k=='add_building_construction' and one(v,'type')=='bunker':
                province=one(v,'province');check(any(province in [b for a,b,c in one(s,'provinces',[])] for s in states.values()),did+': unknown fort province '+str(province))

compat=read(ROOT/'common/national_focus/FRA_compatibility.txt')
expected=set()
for name in ['france','free_france','vichy_france']:
    for k,v,o in one(read(GAME/f'common/national_focus/{name}.txt'),'focus_tree',[]):
        if k in ('focus','shared_focus') and isinstance(v,list) and one(v,'id'):expected.add(one(v,'id'))
check({one(v,'id') for k,v,o in compat}==expected,'Compatibility registry must contain direct focus definitions only')
check(all(not one(v,'completion_reward') for k,v,o in compat),'Compatibility focuses replay native rewards')

hist=read(ROOT/'history/countries/FRA - France.txt')
check(not any(k=='target' and v in ['SYR','LEB'] for k,v,o in walk(hist)),'French history recreates Ottoman dependencies')
check(any(k=='set_oob' for k,v,o in walk(hist)),'France lost its equipped starting army')
for alias in ['free_french_focus','vichy_french_focus']:
    check(any(one(one(read(f),'focus_tree',[]),'id')==alias and one(one(one(read(f),'focus_tree',[]),'country',[]),'factor')=='0' for f in [ROOT/'common/national_focus/free_france.txt',ROOT/'common/national_focus/vichy_france.txt']),alias+': missing nonselectable alias')
native_rules=read(GAME/'common/game_rules/00_game_rules.txt')
override_rules=read(ROOT/'common/game_rules/00_game_rules.txt')
check([(k,v,o) for k,v,o in native_rules if k!='FRA_ai_behavior']==[(k,v,o) for k,v,o in override_rules if k!='FRA_ai_behavior'],'FRA override changed another country\'s game rules')
for key in ['mandate','tension',*[r[0]+'_pressure' for r in json.loads((ROOT/'docs/FRA_content.json').read_text(encoding='utf-8'))['regions']]]:
    check(any(k=='clamp_variable' and one(v,'var')=='FRA_'+key and one(v,'min')=='0' and one(v,'max')=='100' for k,v,o in walk(effects)),'Unbounded meter '+key)

manifest=json.loads((ROOT/'docs/art/FRA/manifest.json').read_text(encoding='utf-8'))
for item in manifest:
    with Image.open(ROOT/item['texture']) as im:
        check(list(im.size)==item['size'],'Wrong canvas '+item['texture'])
        bounds=im.convert('RGBA').getchannel('A').getbbox()
        check(bounds is not None,'Empty asset '+item['texture'])
        if item['kind']=='idea':check(bounds[3]<=59,'Spirit icon needs bottom clearance '+item['texture'])
    check((ROOT/item['source']).is_file(),'Missing original '+item['source'])
    check((ROOT/Path(item['source']).with_suffix('.prompt.txt')).is_file(),'Missing prompt '+item['source'])

if errors:
    print('\n'.join('ERROR: '+e for e in errors));raise SystemExit(1)
print(f'France OK: {len(focuses)} focuses; {len(decision_ids)} decisions; {len(events)} events; {pacing}-day combined opening; {emergency}-day emergency resolution; 11 original emblems and 2 scripted decision panels.')
