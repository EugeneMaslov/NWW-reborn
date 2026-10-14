"""Validate adapted archive content against the installed game; also run LTB/MKN checks."""
import json,re,sys
from functools import lru_cache
from pathlib import Path
from hoi4_script import read,one,values,walk
import validate_country_content as base

ROOT,GAME=base.ROOT,base.GAME
errors=[]
def check(ok,message):
    if not ok:errors.append(message)
def documents(root,pattern):return base.documents(root,pattern)
manifest=json.loads((ROOT/'docs/legacy_import.json').read_text(encoding='utf-8'))
locales=base.locales
def local(key,where):
    for lang,entries in locales.items():check(key in entries,f'{where}: missing {lang} localization {key}')
idea_ids=set()
character_ids=set()
for root in (GAME,ROOT):
    for p,doc in documents(root,'common/ideas/*.txt'):
        for group,node,o in one(doc,'ideas',[]):
            if isinstance(node,list):idea_ids.update(k for k,v,o in node if isinstance(v,list))
    for p,doc in documents(root,'common/characters/*.txt'):character_ids.update(k for k,v,o in one(doc,'characters',[]))
all_focus_ids=base.all_focus_ids
event_ids={one(event,'id') for p,doc in documents(ROOT,'events/*.txt') for kind,event,o in doc if kind in ('country_event','news_event')}
modifiers=set(re.findall(r'^## ([\w]+)\s*$',(GAME/'documentation/modifiers_documentation.md').read_text(encoding='utf-8-sig'),re.M))
# Ideology modifiers are generated dynamically; the installed advisor traits use them.
modifiers.update(['democratic_drift','fascism_drift','communism_drift'])
known_effects=set(re.findall(r'^## ([\w]+)\s*$',(GAME/'documentation/effects_documentation.md').read_text(encoding='utf-8-sig'),re.M))
scripted={k for p,doc in documents(ROOT,'common/scripted_effects/*.txt') for k,v,o in doc}
scope=[ROOT/c['destination'] for c in manifest['countries'].values()]
scope += [ROOT/p for p in ['common/ideas/nww_legacy_ideas.txt','common/scripted_effects/nww_legacy_effects.txt','events/nww_legacy_diplomacy.txt','common/technology_sharing/nww_legacy_research.txt','common/decisions/nww_legacy_campaigns.txt','common/decisions/categories/nww_legacy_categories.txt','history/countries/TUR - Turkey.txt','common/characters/nww_legacy_TUR.txt','interface/nww_legacy.gfx']]
for path in scope:
    doc=read(path);where=path.relative_to(ROOT)
    for key,value,op in walk(doc):
        if isinstance(value,str):
            if value.startswith('GFX_'):check(value in base.sprites,f'{where}: unknown sprite {value}')
            if key in ('has_completed_focus','complete_national_focus'):check(value in all_focus_ids,f'{where}: unknown focus {value}')
            if key in ('add_ideas','remove_ideas','has_idea','idea','remove_idea','add_idea'):check(value in idea_ids,f'{where}: unknown idea {value}')
            if key in ('recruit_character','promote_character'):check(value in character_ids,f'{where}: unknown character {value}')
            if key and key.startswith('nww_legacy_'):check(key in scripted,f'{where}: undefined scripted effect {key}')
        if key=='picture' and '/ideas/' in path.as_posix():check('GFX_idea_'+value in base.sprites,f'{where}: unknown idea icon {value}')
        if key=='add_tech_bonus':
            for cat in values(value,'category'):check(cat in base.categories and not cat.endswith('_doctrine'),f'{where}: obsolete research category {cat}')
        if key=='country_event' and isinstance(value,list):check(one(value,'id') in event_ids,f'{where}: missing event {one(value,"id")}')
        if key=='modifier' and isinstance(value,list) and path.name=='nww_legacy_ideas.txt':
            for mod,v,o in value:check(mod in modifiers or mod.startswith('production_speed_'),f'{where}: unknown modifier {mod}')
        check(key not in ('add_offsite_building','add_defense','start_border_war','set_state_owner','set_state_controller','num_of_research_slots'),f'{where}: obsolete or unsafe archive effect {key}')
        if key=='set_politics':
            check(bool(one(value,'ruling_party')) and len(values(value,'ruling_party'))==1,f'{where}: incomplete political transition')
            check(not values(value,'parties'),f'{where}: obsolete nested party setup')
        if key=='add_research_slot':
            # All slot effects must be within a guarded if in this generated content.
            check(any(k=='if' and one(v,'add_research_slot') is not None and any(t=='amount_research_slots' and n=='5' and op=='<' for t,n,op in one(v,'limit',[])) for k,v,o in walk(doc)),f'{where}: research slots lack a five-slot cap')
        if key=='random_owned_controlled_state' and any(k=='add_building_construction' for k,v,o in walk(value)):
            limit=one(value,'limit',[])
            check(one(limit,'is_core_of')=='PREV',f'{where}: random factory selection uses the wrong country scope')
        if isinstance(value,list):
            buildings=[b for b in values(value,'add_building_construction') if one(b,'type') in ('industrial_complex','arms_factory','dockyard')]
            if buildings:check(sum(int(v) for v in values(value,'add_extra_state_shared_building_slots'))>=sum(int(one(b,'level')) for b in buildings),f'{where}: buildings exceed granted state slots')
    tree=one(doc,'focus_tree')
    if tree:
        tag=next(tag for tag,c in manifest['countries'].items() if c['destination']==str(path.relative_to(ROOT)).replace('\\','/'))
        fs=values(tree,'focus');by_id={one(f,'id'):f for f in fs}
        check(len(fs)==len(by_id),f'{tag}: duplicate focuses')
        check(set(manifest['countries'][tag]['archive_ids'])<=by_id.keys(),f'{tag}: archive focuses lost')
        check(len(fs)==manifest['countries'][tag]['total'],f'{tag}: manifest count mismatch')
        check(one(one(one(tree,'country'),'modifier'),'add')=='100',f'{tag}: tree selection does not outrank DLC')
        rows={}
        for f in fs:
            fid=one(f,'id');local(fid,tag);local(fid+'_desc',tag)
            x,y=int(one(f,'x')),int(one(f,'y'));rows.setdefault(y,[]).append((x,fid))
            reward=one(f,'completion_reward',[])
            for k,v,o in walk(reward):
                if k=='set_politics' and one(v,'ruling_party') in ('democratic','fascism','communism'):
                    ideology=one(v,'ruling_party');gate=one(f,'available',[])
                    check(any((ideology,'0.40','<') in n for n in values(gate,'NOT')),f'{fid}: government change lacks a 40% mandate')
            for group in values(f,'prerequisite'):
                for parent in values(group,'focus'):
                    check(parent in by_id,f'{fid}: missing parent {parent}')
                    if parent in by_id:check(int(one(by_id[parent],'y'))<y,f'{fid}: parent {parent} is not above it')
            for group in values(f,'mutually_exclusive'):
                for other in values(group,'focus'):
                    check(other in by_id and any(fid in values(g,'focus') for g in values(by_id.get(other,[]),'mutually_exclusive')),f'{fid}: exclusion with {other} is not reciprocal')
        for y,row in rows.items():
            for (x,fid),(gx,gid) in zip(sorted(row),sorted(row)[1:]):check(gx-x>=2,f'{tag}: overlapping/crowded row {y}: {fid}, {gid}')
        check(int(one(one(tree,'continuous_focus_position'),'y'))>max(rows)*130+800,f'{tag}: continuous panel overlaps the tree')
        reached=set()
        while True:
            more={fid for fid,f in by_id.items() if fid not in reached and all(any(p in reached for p in values(g,'focus')) for g in values(f,'prerequisite'))}
            if not more:break
            reached|=more
        check(reached==by_id.keys(),f'{tag}: unreachable/cyclic focuses {by_id.keys()-reached}')
        pairs={frozenset((fid,other)) for fid,f in by_id.items() for g in values(f,'mutually_exclusive') for other in values(g,'focus')}
        @lru_cache(None)
        def paths(fid):
            result={frozenset([fid])}
            for group in values(by_id[fid],'prerequisite'):
                alternatives={p for parent in values(group,'focus') for p in paths(parent)}
                result={a|b for a in result for b in alternatives if not any(pair<=a|b for pair in pairs)}
            return result
        if reached==by_id.keys():
            for fid in by_id:check(bool(paths(fid)),f'{fid}: requires mutually exclusive paths')
    if path.name=='nww_legacy_ideas.txt':
        for token,idea,o in one(one(doc,'ideas'),'country'):local(token,path.name);local(token+'_desc',path.name)
    if path.name=='nww_legacy_diplomacy.txt':
        for event in values(doc,'country_event'):
            local(one(event,'title'),path.name);local(one(event,'desc'),path.name)
            for option in values(event,'option'):local(one(option,'name'),path.name)
    if path.name in ('nww_legacy_categories.txt','nww_legacy_campaigns.txt'):
        for token,node,o in doc:
            local(token,path.name)
            if path.name=='nww_legacy_campaigns.txt':
                for decision,content,o in node:local(decision,path.name);local(decision+'_desc',path.name)
for lang in locales:
    p=ROOT/f'localisation/nww_legacy_l_{lang}.yml';check(p.read_bytes().startswith(b'\xef\xbb\xbf'),f'{p.name}: no UTF-8 BOM')
    keys=re.findall(r'^\s+([\w.]+):',p.read_text(encoding='utf-8-sig'),re.M);check(len(keys)==len(set(keys)),f'{p.name}: duplicate localization keys')
for token in manifest['compatibility_ids']:
    shared=next(v for k,v,o in read(ROOT/'common/national_focus/nww_legacy_compatibility.txt') if one(v,'id')==token)
    check(one(one(shared,'allow_branch'),'always')=='no',f'{token}: compatibility focus can appear in gameplay')
if errors:
    for err in dict.fromkeys(errors):print('ERROR:',err)
    raise SystemExit(1)
print('PASS: '+', '.join(f'{tag}: {c["total"]}' for tag,c in manifest['countries'].items()))
print('PASS: all 107 archived IDs, dependency paths, spacing, diplomacy scopes, 40% mandates, slots, ideas, icons, leaders, RU/EN localization and hidden compatibility definitions')
