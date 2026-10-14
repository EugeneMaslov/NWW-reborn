"""Publish the legacy bootstrap as country-owned files and apply NWW AI/startup rules.

Run after import_legacy_focuses.py --write. This script also supports already split files.
"""
import copy,json,re,shutil
from pathlib import Path
from hoi4_script import read,one,values,walk,parse,dump

ROOT=Path(__file__).resolve().parents[1]
GAME=Path('D:/Steam/steamapps/common/Hearts of Iron IV')
manifest=json.loads((ROOT/'docs/legacy_import.json').read_text(encoding='utf-8'))
TAGS=('TUR','AUS','AFG','GER','HUN')

def save(relative,doc):
    p=ROOT/relative;p.parent.mkdir(parents=True,exist_ok=True)
    if not doc:
        if p.exists():p.unlink()
        return
    p.write_text(dump(doc)+'\n',encoding='utf-8')

def setv(doc,key,value):
    doc[:]=[(k,v,o) for k,v,o in doc if k!=key];doc.append((key,value,'='))

def owner(token):
    upper=token.upper()
    for tag in TAGS:
        if upper.startswith(tag+'_') or upper.startswith('NWW_'+tag+'_') or '_'+tag+'_' in upper:return tag
    return 'AUS'  # Bilateral Danubian definitions are owned by their initiating country.

def remove(relative):
    p=ROOT/relative
    if p.is_file():p.unlink()

trees={}
for tag,c in manifest['countries'].items():
    source=ROOT/c['destination'];tree=one(read(source),'focus_tree')
    target=f'common/national_focus/{tag}_focuses.txt'
    if source!=ROOT/target:
        # These original filenames override installed DLC trees and must remain present.
        if source.name in ('turkey.txt','afghanistan.txt','austria.txt','hungary.txt'):
            source.write_text(f'# NWW tree: {tag}_focuses.txt. Suppress the vanilla tree in this filename.\n',encoding='utf-8')
        else:source.unlink()
    c['destination']=target;trees[tag]=tree
    if tag=='TUR':setv(tree,'id','turkish_focus')  # Native BFTB effects refer to this tree ID.

def reward(tag,fid,script):
    node=next(f for f in values(trees[tag],'focus') if one(f,'id')==fid)
    existing=one(node,'completion_reward',[])
    for k,v,o in parse(script):
        if (k,v,o) not in existing:existing.append((k,v,o))
    setv(node,'completion_reward',existing)

# Austria: separate political choices, diplomatic contacts, army and industrial lanes.
positions={
 'AUS_nww_rebuild':(10,0),'AUS_political_power':(4,1),
 'AUS_reinstate_the_imperial_council':(2,2),'AUS_hold_elections':(6,2),
 'AUS_the_danubian_federation':(2,3),'AUS_via_danube_to_europe':(2,4),
 'AUS_not_germany':(6,3),'AUS_war_with_hun':(6,4),'AUS_war_with_croatia':(6,5),
 'AUS_reclaiming_yugoslavian_territories':(6,6),'AUS_join_to_axis':(10,4),'AUS_help_from_eng':(10,5),
 'AUS_nww_army':(16,1),'AUS_army_expierience':(16,2),'AUS_bring_generals_out_of_retirement':(16,3),'AUS_establish_bohme_plan':(16,4),
 'AUS_nww_industry':(24,1),'aus_prom':(22,2),'aus_prom_2':(22,3),'aus_prom_3':(22,4),'aus_prom_4':(21,5),'aus_prom_5':(23,5),
 'AUS_new_economic':(26,2),'AUS_reform_the_economic':(26,3),'AUS_create_a_new_econimic':(26,4)}
for node in values(trees['AUS'],'focus'):
    x,y=positions[one(node,'id')];setv(node,'x',str(x));setv(node,'y',str(y))
    if one(node,'id')=='AUS_war_with_hun':
        # Historical NWW prepares for a real conquest; it still waits until 1937.
        setv(node,'ai_will_do',parse('factor = 10 modifier = { factor = 10 is_historical_focus_on = yes }'))
    if one(node,'id')=='AUS_the_danubian_federation':
        setv(node,'ai_will_do',parse('factor = 1 modifier = { factor = 0 is_historical_focus_on = yes }'))

ideas_doc=ROOT/'common/ideas/nww_legacy_ideas.txt'
ideas=one(one(read(ideas_doc),'ideas'),'country') if ideas_doc.exists() else [item for tag in TAGS for item in one(one(read(ROOT/f'common/ideas/{tag}_ideas.txt'),'ideas'),'country',[])]
extra=parse('''NWW_AUS_officer_corps = { picture = generic_army_war_college removal_cost = -1 modifier = { army_org_factor = 0.10 planning_speed = 0.10 } }
NWW_AFG_frontier_army = { picture = generic_army_europe_1 removal_cost = -1 modifier = { army_org_factor = 0.10 army_attack_factor = 0.05 } }
NWW_AFG_court_industry = { picture = generic_industrial_concern_1 removal_cost = -1 modifier = { production_speed_buildings_factor = 0.10 production_factory_efficiency_gain_factor = 0.10 } }''')
ids={k for k,v,o in ideas};ideas += [item for item in extra if item[0] not in ids]
for token,node,o in ideas:
    if token=='NWW_AUS_officer_corps':setv(node,'picture','generic_army_war_college')
    if token=='NWW_AFG_frontier_army':setv(node,'picture','generic_army_europe_1')
reward('AUS','AUS_army_expierience','add_ideas = NWW_AUS_officer_corps')
reward('AFG','AFG_ready_the_army','add_ideas = NWW_AFG_frontier_army')
reward('AFG','afg_anon_ussr','add_ideas = NWW_AFG_court_industry')
reward('AUS','AUS_war_with_hun','add_ai_strategy = { type = conquer id = HUN value = 200 }')
for tag in TAGS:save(f'common/ideas/{tag}_ideas.txt',[('ideas',[('country',[item for item in ideas if owner(item[0])==tag],'=')],'=')])
remove('common/ideas/nww_legacy_ideas.txt')

effects_doc=ROOT/'common/scripted_effects/nww_legacy_effects.txt'
effects=read(effects_doc) if effects_doc.exists() else [item for tag in TAGS if (ROOT/f'common/scripted_effects/{tag}_effects.txt').exists() for item in read(ROOT/f'common/scripted_effects/{tag}_effects.txt')]
for tag in TAGS:save(f'common/scripted_effects/{tag}_effects.txt',[item for item in effects if owner(item[0])==tag])
remove('common/scripted_effects/nww_legacy_effects.txt')

# Separate event namespaces per initiator; replies stay in the originating namespace.
template_path=ROOT/'events/nww_legacy_diplomacy.txt'
template=read(template_path) if template_path.exists() else read(ROOT/'events/AUS_events.txt')
def namespace(doc,tag):
    result=[]
    for k,v,o in doc:
        if isinstance(v,list):v=namespace(v,tag)
        elif isinstance(v,str):
            v=re.sub(r'nww_(?:legacy|tur_diplomacy|aus_diplomacy)\.',f'nww_{tag.lower()}_diplomacy.',v)
            if k=='add_namespace':v=f'nww_{tag.lower()}_diplomacy'
        result.append((k,v,o))
    return result
for tag in TAGS:
    trees[tag]=namespace(trees[tag],tag)
    if tag!='GER':
        events=namespace(copy.deepcopy(template),tag)
        if tag in ('TUR','AFG'):events=[(k,v,o) for k,v,o in events if k!='country_event' or one(v,'id').rsplit('.',1)[1] not in ('3','5')]
        save(f'events/{tag}_events.txt',events)
remove('events/nww_legacy_diplomacy.txt')

for directory,original,suffix in [('common/decisions','nww_legacy_campaigns.txt','decisions'),('common/decisions/categories','nww_legacy_categories.txt','categories')]:
    p=ROOT/directory/original
    items=read(p) if p.exists() else [i for tag in TAGS if (ROOT/f'{directory}/{tag}_{suffix}.txt').exists() for i in read(ROOT/f'{directory}/{tag}_{suffix}.txt')]
    for tag in TAGS:save(f'{directory}/{tag}_{suffix}.txt',[item for item in items if owner(item[0])==tag])
    remove(f'{directory}/{original}')
for directory,original,new in [('common/opinion_modifiers','nww_legacy_opinions.txt','AUS_opinions.txt'),('common/technology_sharing','nww_legacy_research.txt','AUS_research.txt')]:
    if (ROOT/directory/original).exists():
        save(f'{directory}/{new}',read(ROOT/directory/original));remove(f'{directory}/{original}')

# Archive leaders and modern advisor/commander roles share the native TUR override.
if (ROOT/'common/characters/nww_legacy_TUR.txt').exists():
    doc=read(ROOT/'common/characters/TUR.txt');chars=one(doc,'characters')
    known={k for k,v,o in chars}
    chars += [i for i in one(read(ROOT/'common/characters/nww_legacy_TUR.txt'),'characters') if i[0] not in known]
    save('common/characters/TUR.txt',doc);remove('common/characters/nww_legacy_TUR.txt')
if (ROOT/'interface/nww_legacy.gfx').exists():
    save('interface/TUR_ideas.gfx',read(ROOT/'interface/nww_legacy.gfx'));remove('interface/nww_legacy.gfx')
portrait='gfx/leaders/TUR/portrait_tur_nihal_atsiz.dds'
(ROOT/portrait).parent.mkdir(parents=True,exist_ok=True)
shutil.copyfile(GAME/'dlc/dlc031_battle_for_the_bosporus'/portrait,ROOT/portrait)
gfx=read(ROOT/'interface/TUR_ideas.gfx');sprites=one(gfx,'spriteTypes')
if not any(one(node,'name')=='GFX_portrait_tur_nihal_atsiz' for node in values(sprites,'spriteType')):
    sprites.extend(parse(f'spriteType = {{ name = GFX_portrait_tur_nihal_atsiz texturefile = "{portrait}" }}'))
save('interface/TUR_ideas.gfx',gfx)

# Register real focus definitions only. Attach hidden shared definitions to initialize their icons.
compat_path=ROOT/'common/national_focus/nww_legacy_compatibility.txt'
compat=read(compat_path) if compat_path.exists() else [i for tag in TAGS if (ROOT/f'common/national_focus/{tag}_compatibility.txt').exists() for i in read(ROOT/f'common/national_focus/{tag}_compatibility.txt')]
actual=set()
for name in ('austria.txt','hungary.txt','hungary_wuw.txt','turkey.txt','afghanistan.txt'):
    d=read(GAME/'common/national_focus'/name)
    actual.update(one(f,'id') for f in values(d,'shared_focus'))
    actual.update(one(f,'id') for t in values(d,'focus_tree') for f in values(t,'focus'))
compat=[item for item in compat if one(item[1],'id') in actual]
manifest['compatibility_ids']=[one(node,'id') for k,node,o in compat]
manifest['compatibility_files']=[]
for tag in TAGS:
    subset=[i for i in compat if owner(one(i[1],'id'))==tag]
    if subset:
        path=f'common/national_focus/{tag}_compatibility.txt';save(path,subset);manifest['compatibility_files'].append(path)
        tree=trees[tag]
        refs={v for k,v,o in tree if k=='shared_focus'}
        tree += [('shared_focus',one(node,'id'),'=') for k,node,o in subset if one(node,'id') not in refs]
remove('common/national_focus/nww_legacy_compatibility.txt')
for tag,tree in trees.items():save(manifest['countries'][tag]['destination'],[('focus_tree',tree,'=')])
(ROOT/'common/national_focus/hungary_wuw.txt').write_text('# NWW: Gotterdammerung Hungarian tree disabled; see HUN_focuses.txt.\n',encoding='utf-8')

# Six native Austrian divisions, properly equipped, plus six infantry divisions.
oob=read(GAME/'history/units/AUS_1936.txt')
units=one(oob,'units');divisions=values(units,'division')
for node in divisions:setv(node,'start_equipment_factor','1');setv(node,'start_experience_factor','0.20')
for i,location in enumerate([11666,3700,9648,9665,11666,3700],7):
    units.extend(parse(f'division = {{ name = "{i}. Infanterie Division" location = {location} division_template = "Infanterie Division" start_experience_factor = 0.20 start_equipment_factor = 1 }}'))
save('history/units/AUS_1936_nww.txt',oob)
history=read(ROOT/'history/countries/AUS - Austria.txt')
history[:]=[(k,v,o) for k,v,o in history if not (k and k.lower()=='if' and any(key=='set_oob' for key,value,op in walk(v))) and k!='set_oob']
history.insert(1,('set_oob','AUS_1936_nww','='));setv(history,'set_war_support','0.40')
setv(history,'set_popularities',parse('neutrality = 60 fascism = 25 democratic = 10 communism = 5'))
save('history/countries/AUS - Austria.txt',history)

# Historical lists follow the DLC strategy-plan format. Focus gates enforce their opening order.
def plan(tag,name,focuses,extras=''):
    save(f'common/ai_strategy_plans/{tag}_historical.txt',parse(f'''{name} = {{ name = "NWW {tag} historical plan" desc = ""
allowed = {{ original_tag = {tag} }} enable = {{ is_historical_focus_on = yes }} abort = {{ is_subject = yes }}
ai_national_focuses = {{ {' '.join(focuses)} }} weight = {{ factor = 100 }} {extras} }}'''))
plan('LTB','NWW_LTB_historical',['LTB_consolidate_the_union','LTB_the_vilnius_compromise','LTB_belarusian_schools','LTB_land_for_the_tillers','LTB_the_union_endures','LTB_union_general_staff'],
     'focus_factors = { LTB_kaunas_first = 0 LTB_face_the_crisis = 0 }')
ltb_path=ROOT/'common/national_focus/ltb_focus.txt';ltb=read(ltb_path)
for node in values(one(ltb,'focus_tree'),'focus'):
    fid=one(node,'id')
    if fid in ('LTB_consolidate_the_union','LTB_the_vilnius_compromise'):
        setv(node,'ai_will_do',parse('factor = 1 modifier = { factor = 1000 is_historical_focus_on = yes }'))
    else:
        weights=one(node,'ai_will_do',parse('factor = 1'))
        gate=parse('modifier = { factor = 0 is_historical_focus_on = yes NOT = { has_completed_focus = LTB_the_vilnius_compromise } }')[0]
        if gate not in weights:weights.append(gate)
        if fid=='LTB_kaunas_first':
            block=parse('modifier = { factor = 0 is_historical_focus_on = yes }')[0]
            if block not in weights:weights.append(block)
        setv(node,'ai_will_do',weights)
save('common/national_focus/ltb_focus.txt',ltb)
plan('AUS','NWW_AUS_historical',['AUS_nww_rebuild','AUS_political_power','AUS_reinstate_the_imperial_council','AUS_not_germany','AUS_nww_army','AUS_army_expierience','AUS_nww_industry','aus_prom','aus_prom_2','AUS_bring_generals_out_of_retirement','AUS_war_with_hun','AUS_establish_bohme_plan','aus_prom_3','aus_prom_4','AUS_war_with_croatia'],
     'focus_factors = { AUS_the_danubian_federation = 0 AUS_hold_elections = 0 } ai_strategy = { type = conquer id = HUN value = 200 }')
# Prevent the original DLC plan competing for incompatible focuses.
(ROOT/'common/ai_strategy_plans/AUS_historical_strategy_plan.txt').write_text('# Replaced by AUS_historical.txt for the NWW timeline.\n',encoding='utf-8')

extra_loc={
 'NWW_AUS_officer_corps':('Австрийский офицерский корпус','Austrian officer corps'),
 'NWW_AUS_officer_corps_desc':('Училища готовят командиров для наступательной армии: +10% к организации и скорости планирования.','Officer schools prepare an offensive army: +10% organisation and planning speed.'),
 'NWW_AFG_frontier_army':('Афганская пограничная армия','Afghan frontier army'),
 'NWW_AFG_frontier_army_desc':('Реформа командования даёт +10% организации и +5% атаки дивизий.','Command reform grants +10% organisation and +5% division attack.'),
 'NWW_AFG_court_industry':('Королевская промышленная программа','Royal industrial programme'),
 'NWW_AFG_court_industry_desc':('Производственная программа даёт +10% скорости строительства и роста эффективности производства.','The programme grants +10% construction speed and production efficiency growth.')}
for lang,idx in [('russian',0),('english',1)]:
    old=ROOT/f'localisation/nww_legacy_l_{lang}.yml'
    entries=dict(re.findall(r'^\s+([\w.]+):\d*\s+"(.*)"\s*$',old.read_text(encoding='utf-8-sig'),re.M)) if old.exists() else {}
    entries.update({k:v[idx] for k,v in extra_loc.items()})
    event_texts={k:v for k,v in entries.items() if k.startswith('nww_legacy.')}
    for tag in TAGS:
        target=ROOT/f'localisation/replace/{tag}_l_{lang}.yml';target.parent.mkdir(parents=True,exist_ok=True)
        selected={k:v for k,v in entries.items() if not k.startswith('nww_legacy.') and owner(k)==tag}
        if tag!='GER':selected.update({k.replace('nww_legacy.',f'nww_{tag.lower()}_diplomacy.'):v for k,v in event_texts.items()})
        # Re-running the finalizer retains previously split country text.
        if target.exists() and not old.exists():selected={**dict(re.findall(r'^\s+([\w.]+):\d*\s+"(.*)"\s*$',target.read_text(encoding='utf-8-sig'),re.M)),**selected}
        target.write_text('l_'+lang+':\n'+''.join(f' {k}:0 "{v}"\n' for k,v in selected.items()),encoding='utf-8-sig')
    remove(f'localisation/nww_legacy_l_{lang}.yml')
manifest['content_files']=sorted({str(p.relative_to(ROOT)).replace('\\','/') for folder in ('common/ideas','common/scripted_effects','common/decisions','common/decisions/categories','common/opinion_modifiers','common/technology_sharing','common/characters','events','interface') for tag in TAGS for p in (ROOT/folder).glob(tag+'_*.txt')} | {'common/characters/TUR.txt','interface/TUR_ideas.gfx','history/countries/TUR - Turkey.txt','history/countries/AUS - Austria.txt','history/units/AUS_1936_nww.txt'})
(ROOT/'docs/legacy_import.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Country files published; historical LTB compromise / Austrian conquest; Austria starts with 12 equipped divisions.')
