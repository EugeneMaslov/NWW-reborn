"""Replay GER/TUR country readiness rules, target AI policy and recovery callbacks.

Strategy desires are evaluated as policy, not as engine-enforced target bans."""
import argparse
from copy import deepcopy
from pathlib import Path
from hoi4_script import read,one,values,walk,engine_script_errors
from validate_germany_politics import Scenario

ROOT=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('--game',type=Path,required=True);game=p.parse_args().game
class World(Scenario):
    def __init__(self):
        effects={k:v for tag in ('GER','TUR') for k,v,o in read(ROOT/f'common/scripted_effects/{tag}_campaign_safety_effects.txt')}
        super().__init__(effects,{})
        self.ai=True
        self.date="1941.1.1"
        for tag in ('TUR','BUL','GRE','YUG','ALB','ROM','CRO','USA','HOL','BEL','LUX','DEN','NOR','SWE','FIN','SWI','HUN','ITA'):
            self.countries[tag]=deepcopy(self.countries['POL']);self.countries[tag].update(original=tag,tree='turkish_focus' if tag=='TUR' else 'other_tree')
        for tag,data in self.countries.items():
            data.update(strength=100 if tag in ('GER','TUR') else 30,major=tag in ('GER','ENG','FRA','SOV','USA'),stability=0.6,war_support=0.6)
        self.strategies={tag:read(ROOT/f'common/ai_strategy/{tag}_campaign_safety.txt') for tag in ('GER','TUR')}
        self.hooks=[]
        for tag in ('GER','TUR'):
            self.triggers.update({k:v for k,v,o in read(ROOT/f'common/scripted_triggers/{tag}_campaign_safety_triggers.txt')})
            self.hooks.extend(one(read(ROOT/f'common/on_actions/{tag}_campaign_safety_on_actions.txt'),'on_actions'))
        self.hook('on_startup','GER')
        self.days(180)
    def condition(self,node,actor='GER',root=None,stack=()):
        for entry in node:
            if entry[0]=='can_declare_war_on':result=self.permitted(actor,self.target(entry[1],actor,root or actor,stack))
            else:result=super().condition([entry],actor,root,stack)
            if not result:return False
        return True
    def hook(self,name,actor,other='ENG'):
        previous=self.from_country;self.from_country=other
        try:
            for key,body,op in self.hooks:
                if key==name:
                    for effect in values(body,'effect'):self.apply(effect,actor,actor)
        finally:self.from_country=previous
    def days(self,count):
        for _ in range(count):
            for key in list(self.flag_timers):
                self.flag_timers[key]-=1
                if self.flag_timers[key]<=0:
                    actor,flag=key;self.countries[actor]['flags'].discard(flag);del self.flag_timers[key]
            for actor in ('GER','TUR'):self.hook('on_daily_'+actor,actor)
    def permitted(self,actor,target):
        # Refresh the supported country rule, then evaluate source-script strategy policy.
        # A negative AI desire is not an absolute engine prohibition against a particular tag.
        self.apply(self.effects[f'nww_{actor}_ai_refresh_declaration_rule'],actor)
        previous=self.from_country;self.from_country=target
        try:
            rules=self.countries[actor]['rules']
            if target in rules or ('country','can_not_declare_war') in rules:return False
            if self.ai:
                for name,body,op in self.strategies[actor]:
                    if self.condition(one(body,'enable'),actor):
                        if any(one(v,'type')=='declare_war' and one(v,'id')==target and float(one(v,'value'))<0 for v in values(body,'ai_strategy')):return False
            return True
        finally:self.from_country=previous
    def start_war(self,actor,target):
        assert self.permitted(actor,target),(actor,target)
        self.countries[actor]['wars'].add(target);self.countries[target]['wars'].add(actor)
        self.hook('on_war',actor,target)
        self.hook('on_war_relation_added',actor,target)
    def peace(self,actor):
        for target in tuple(self.countries[actor]['wars']):self.countries[target]['wars'].discard(actor)
        self.countries[actor]['wars'].clear();self.countries[actor]['capitulated']=False
        self.hook('on_peaceconference_ended',actor)
    def faction(self,leader,*members):
        people={leader,*members}
        for t in people:self.countries[t]['faction']=leader;self.countries[t]['allies']|=people-{t}

count=0
for actor,first,second in [('GER','AUS','POL'),('TUR','BUL','GRE')]:
    w=World();assert w.permitted(actor,first)
    # Readiness rule and AI target policy also inspect an already-granted objective.
    w.countries[actor]['goals']|={first,second,'ENG','FRA','SOV'}
    w.start_war(actor,first)
    assert not w.permitted(actor,second)
    assert not w.permitted(actor,'ENG')
    assert not w.condition(w.triggers[f'nww_{actor}_ai_can_target_{second}'],actor)
    w.peace(actor);assert not w.permitted(actor,second)
    w.days(179);assert not w.permitted(actor,second)
    w.days(1);assert w.permitted(actor,second)
    count+=6
    # Defeat pending survives war; two years are measured from the final peace.
    w=World();w.start_war(actor,first);w.countries[actor]['capitulated']=True
    w.hook('on_capitulation',actor,first);w.days(20)
    assert not w.permitted(actor,second)
    w.peace(actor)
    assert w.flag_timers[(actor,f'NWW_{actor}_campaign_recovery')]==730
    w.days(729);assert not w.permitted(actor,second)
    w.days(1);assert w.permitted(actor,second)
    count+=4
    # No new conference or flag reset on save load may shorten defeat recovery.
    w=World();w.countries[actor]['flags'].add(f'NWW_{actor}_campaign_defeat_pending')
    w.hook('on_startup',actor)
    assert w.flag_timers[(actor,f'NWW_{actor}_campaign_recovery')]==730
    w.days(100);w.hook('on_startup',actor)
    assert w.flag_timers[(actor,f'NWW_{actor}_campaign_recovery')]==630
    # Guard installation must leave separately owned pre-1939 rules alone.
    w.countries[actor]['rules'].add('LTB')
    before=deepcopy(w.countries[actor]['rules']);w.hook('on_startup',actor)
    assert before==w.countries[actor]['rules']
    count+=3
    for bad in ('capitulated','civil_war','subject','stability','war_support','surrender','enemy','pending','peace_pending'):
        w=World();s=w.countries[actor]
        if bad in ('capitulated','civil_war'):s[bad]=True
        if bad=='subject':s['subject']='ENG'
        if bad=='stability':s['stability']=0.40
        if bad=='war_support':s['war_support']=0.35
        if bad=='surrender':s['surrender']=0.20
        if bad=='enemy':s['wars'].add('ENG')
        if bad=='pending':s['flags'].add(f'NWW_{actor}_campaign_defeat_pending')
        if bad=='peace_pending':s['flags'].add(f'NWW_{actor}_campaign_was_at_war')
        assert not w.permitted(actor,first),bad
        # Player control bypasses only this AI safeguard, not unrelated rules.
        w.ai=False;assert w.permitted(actor,first)
        count+=2
for problem in ('major','subject','faction','minor_guarantee','major_guarantee','weak_army','target_war'):
    w=World();t=w.countries['BUL']
    if problem=='major':t['major']=True
    if problem=='subject':t['subject']='ENG'
    if problem=='faction':w.faction('ENG','BUL')
    if problem=='minor_guarantee':w.countries['GRE']['guarantees']={'BUL'}
    if problem=='major_guarantee':w.countries['ENG']['guarantees']={'BUL'}
    if problem=='weak_army':t['strength']=80
    if problem=='target_war':t['wars'].add('ROM')
    assert not w.permitted('TUR','BUL'),problem
    assert not w.condition(w.triggers['nww_TUR_ai_can_target_BUL'],'TUR'),problem
    count+=2
for problem in ('major_guarantee','faction_guarantor','subject_guarantor','subject','weak_army','two_majors','strong_leader','already_world_war'):
    w=World();t=w.countries['POL']
    if problem=='major_guarantee':w.countries['ENG']['guarantees']={'POL'}
    if problem=='faction_guarantor':w.faction('ENG','GRE');w.countries['GRE']['guarantees']={'POL'}
    if problem=='subject_guarantor':w.countries['GRE']['subject']='ENG';w.countries['GRE']['guarantees']={'POL'}
    if problem=='subject':t['subject']='ENG'
    if problem=='weak_army':t['strength']=85
    if problem=='two_majors':w.faction('ENG','FRA','POL')
    if problem=='strong_leader':w.countries['SOV']['strength']=100;w.faction('SOV','POL')
    if problem=='already_world_war':t['wars'].add('ENG')
    assert not w.permitted('GER','POL'),problem
    count+=1
# A lone weaker major and a weaker coalition with one major remain possible for Germany.
w=World();assert w.permitted('GER','SOV');w.faction('SOV','POL');assert w.permitted('GER','POL')
# Army comparisons must establish their own live actor/target scope. An event's
# ROOT may be the recipient, and the original German tag may no longer exist.
for caller in ('GER','AUS','POL'):
    w=World()
    assert w.condition(w.triggers['nww_GER_ai_target_safe'],'POL',caller)
    w.faction('SOV','POL')
    assert w.condition(w.triggers['nww_GER_ai_target_safe'],'POL',caller)
    w.countries['SOV']['strength']=100
    assert not w.condition(w.triggers['nww_GER_ai_target_safe'],'POL',caller)
    count+=3
w=World();w.countries['GER']['exists']=False
assert not w.condition(w.triggers['nww_GER_ai_target_safe'],'POL','POL')
w.countries['D01']=deepcopy(w.countries['GER'])
w.countries['D01'].update(exists=True,original='GER',tree='GER_focus',strength=100)
assert w.condition(w.triggers['nww_GER_ai_target_safe'],'POL','POL')
w.faction('SOV','POL')
assert w.condition(w.triggers['nww_GER_ai_target_safe'],'POL','POL')
count+=3
# Diplomacy changed AFTER the objective was granted: evaluate at actual declaration.
w=World();w.countries['TUR']['goals'].add('BUL');assert w.permitted('TUR','BUL')
w.countries['ENG']['guarantees'].add('BUL');assert not w.permitted('TUR','BUL')
w.countries['GER']['goals'].add('POL');assert w.permitted('GER','POL')
w.faction('ENG','FRA','POL');assert not w.permitted('GER','POL')
# All focus/reply/repair goal awards must sit inside their matching AI target check.
awards=0
def audit(node,tag,guards=()):
    global awards
    for key,value,operator in node:
        if key=='create_wargoal':
            target=one(value,'target');assert f'nww_{tag}_ai_can_target_{target}' in guards,(tag,target)
            awards+=1
        if isinstance(value,list):
            extra=tuple(k for k,v,o in walk(one(value,'limit',[])) if k and k.startswith(f'nww_{tag}_ai_can_target_')) if key=='if' else ()
            audit(value,tag,guards+extra)
for tag in ('TUR','GER'):audit(read(ROOT/f'common/scripted_effects/{tag}_effects.txt'),tag)
audit(read(ROOT/'events/GER_events.txt'),'GER')
for tag in ('GER','TUR'):
    hook=one(read(ROOT/f'common/on_actions/{tag}_campaign_safety_on_actions.txt'),'on_actions')
    assert {'on_startup','on_war','on_war_relation_added','on_capitulation','on_peaceconference_ended','on_daily_'+tag}<={k for k,v,o in hook}
    for name in ('scripted_effects','scripted_triggers','on_actions'):
        for path in (ROOT/'common'/name).glob(f'{tag}_campaign_safety*.txt'):assert not list(engine_script_errors(read(path))),path
    text=(ROOT/f'common/scripted_effects/{tag}_campaign_safety_effects.txt').read_text()
    assert 'relation_rule_override' not in text
    assert 'set_rule = { can_not_declare_war = yes }' in text
    assert 'clear_rule = { can_not_declare_war = yes }' in text
    assert f'NWW_{tag}_declaration_rule_owned' in text
docs=(game/'documentation/effects_documentation.md').read_text(encoding='utf-8-sig')
assert 'trigger = is_democratic_country' in docs
# Documentation advertises negative relation overrides, but the observed 1.19.3 log rejects them.
assert 'clear_rule' in docs
print(f'PASS: {count} AI readiness/recovery/coalition policy cases; supported country rule and war callbacks, 180/730-day peace recovery, save reload, human control and {awards} guarded goal awards')
