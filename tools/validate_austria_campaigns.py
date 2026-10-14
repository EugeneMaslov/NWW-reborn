"""Check full Austrian conquest hooks, partial-save repair and ownership-gated formation."""
import itertools,json
from pathlib import Path
from hoi4_script import read,one,values,walk
ROOT=Path(__file__).resolve().parents[1]
report=json.loads((ROOT/'docs/AUS_conquest_objectives.json').read_text(encoding='utf-8'))
errors=[]
def check(ok,message):
    if not ok:errors.append(message)
doc=one(read(ROOT/'common/on_actions/AUS_on_actions.txt'),'on_actions')
cap_rules=values(one(one(doc,'on_capitulation'),'effect'),'if')
check(len(cap_rules)==2,'Expected one capitulation rule for Hungary and one for Croatia')
effects=read(ROOT/'common/scripted_effects/AUS_effects.txt')
ai=one(read(ROOT/'common/peace_conference/ai_peace/AUS_peace.txt'),'peace_ai_desires')
costs=one(read(ROOT/'common/peace_conference/cost_modifiers/AUS_peace.txt'),'peace_action_modifiers')
tree=one(read(ROOT/'common/national_focus/AUS_focuses.txt'),'focus_tree');focuses={one(f,'id'):f for f in values(tree,'focus')}

def condition(node,scope,world):
    answers=[]
    for key,value,op in node:
        if key=='NOT':answers.append(not condition(value,scope,world))
        elif key=='OR':answers.append(any(condition([entry],scope,world) for entry in value))
        elif key=='AND':answers.append(condition(value,scope,world))
        elif key=='FROM':answers.append(condition(value,world['winner'],world))
        elif key in ('HUN','CRO'):answers.append(condition(value,world[key],world))
        elif key and key.isdigit():answers.append(condition(value,world['states'][int(key)],world))
        elif key=='tag':answers.append(scope['tag']==value)
        elif key=='exists':answers.append(scope['exists']==(value=='yes'))
        elif key=='is_subject':answers.append(scope.get('subject',False)==(value=='yes'))
        elif key=='has_completed_focus':answers.append(value in scope.get('focuses',set()))
        elif key=='has_country_flag':answers.append(value in scope.get('flags',set()))
        elif key=='is_owned_and_controlled_by':answers.append(scope['owner']==world['root']['tag'] and scope['controller']==world['root']['tag'])
        else:raise ValueError('Unsupported test trigger '+str(key))
    return all(answers)

scenarios=0
for tag,fid in [('HUN','AUS_war_with_hun'),('CRO','AUS_war_with_croatia')]:
    helper=one(effects,f'nww_AUS_prepare_{tag.lower()}_campaign')
    check(bool(helper),tag+': missing full campaign helper')
    check(not any(k=='annex_country' for k,v,o in walk(helper)),tag+': campaign preparation annexes in peacetime')
    check(any(k=='add_claim_by' and v=='AUS' for k,v,o in walk(helper)),tag+': campaign does not claim the whole target country')
    goals=[v for k,v,o in walk(helper) if k=='create_wargoal']
    check(len(goals)==1 and one(goals[0],'target')==tag and one(goals[0],'type')=='annex_everything' and not values(goals[0],'expire'),tag+': goal is not permanent full annexation')
    check(any(k=='has_wargoal_against' and v==tag for k,v,o in walk(helper)),tag+': renewal can duplicate existing goals')
    check(any(k==f'nww_AUS_prepare_{tag.lower()}_campaign' for k,v,o in walk(one(focuses[fid],'completion_reward'))),tag+': war focus does not start its full campaign')
    for hook in ('on_startup','on_daily_AUS'):
        check(any(k==f'nww_AUS_prepare_{tag.lower()}_campaign' for k,v,o in walk(one(doc,hook))),tag+': unfinished old-save campaign is not repaired')
    rule=next(r for r in cap_rules if one(one(r,'limit'),'tag')==tag)
    annex=one(one(rule,'FROM'),'annex_country')
    check(one(annex,'target')=='ROOT' and one(annex,'transfer_troops')=='no',tag+': annexation has the wrong victor/defeated scope')
    for target,winner,done,restored,exists in itertools.product(('HUN','CRO','GER'),('AUS','GER'),(False,True),(False,True),(False,True)):
        country={'tag':target,'exists':exists}
        victor={'tag':winner,'exists':True,'focuses':{fid} if done else set(),'flags':{'NWW_AUS_dual_monarchy_restored'} if restored else set()}
        actual=condition(one(rule,'limit'),country,{'winner':victor})
        expected=target==tag and winner=='AUS' and done and not restored and exists
        check(actual==expected,f'{tag}: unsafe/missing capitulation path {target,winner,done,restored,exists}');scenarios+=1
    take=one(ai,f'NWW_AUS_{tag}_take_entire_country');other=one(ai,f'NWW_AUS_{tag}_no_fragmentation')
    check(one(take,'peace_action_type')=='take_states' and int(one(take,'ai_desire'))>0,tag+': peace AI does not demand full annexation')
    check(int(one(other,'ai_desire'))<0,tag+': peace AI prefers puppets/releases')
    check(float(one(one(costs,f'NWW_AUS_{tag}_imperial_claims'),'cost_multiplier'))>0,tag+': invalid peace price')
for key in ('on_startup','on_daily_AUS'):
    check(not any(k=='annex_country' for k,v,o in walk(one(doc,key))),'Old-save repair performs a free annexation')

formation=focuses[report['formation_focus']];gate=one(formation,'available')
all_states=set(sum(report['target_states'].values(),[]))
check(len(all_states)==20,'Formation must cover all 15 Hungarian and five Croatian starting states')
world={'root':{'tag':'AUS','exists':True},'winner':{'tag':'AUS'},'HUN':{'tag':'HUN','exists':False},'CRO':{'tag':'CRO','exists':False},'states':{sid:{'owner':'AUS','controller':'AUS'} for sid in all_states|{4}}}
check(condition(gate,world['root'],world),'Complete conquest cannot form Austria-Hungary')
for sid,field in itertools.product(all_states|{4},('owner','controller')):
    world['states'][sid][field]='GER';check(not condition(gate,world['root'],world),f'Formation ignores foreign {field} of {sid}');world['states'][sid][field]='AUS';scenarios+=1
for tag in ('HUN','CRO'):
    world[tag]['exists']=True;check(not condition(gate,world['root'],world),f'Formation ignores surviving {tag}');world[tag]['exists']=False
cores={int(k) for k,v,o in one(formation,'completion_reward') if isinstance(v,list) and one(v,'add_core_of')=='ROOT'}
check(cores==all_states,'Formation grants cores outside the incorporated countries or misses states')
check(one(one(formation,'completion_reward'),'set_cosmetic_tag')=='HUN_EMPIRE','Formation lacks Austria-Hungary name/flag')
check(one(formation,'cancel_if_invalid')=='yes','Formation can finish after losing its required lands')
if errors:
    for error in errors:print('ERROR:',error)
    raise SystemExit(1)
print(f'PASS: {scenarios} conquest/formation scenarios, real-victor scopes, no peacetime annexation, full-country peace priorities, permanent goals, old-save renewal and controlled ownership of all 20 crown-land states')
