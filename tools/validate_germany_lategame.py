"""Replay German reform, guarantees, federation and late-game diplomacy from source.

Uses installed definitions for engine tokens. This does not launch the game.
"""
import argparse
from copy import deepcopy
from pathlib import Path
import re

from hoi4_script import read, one, values, walk, tree_focuses, engine_script_errors
from validate_germany_politics import Scenario


def validate_lategame(root, game, check):
    effects = {k:v for name in ('GER_effects.txt','GER_lategame_effects.txt')
               for k,v,o in read(root/'common/scripted_effects'/name)}
    events = {one(v,'id'):v for k,v,o in read(root/'events/GER_events.txt') if k.endswith('_event')}
    focuses = {one(f,'id'):f for f in values(read(root/'common/national_focus/GER_political.txt'),'shared_focus')}
    ideas = dict((k,v) for k,v,o in one(one(read(root/'common/ideas/GER_ideas.txt'),'ideas'),'country'))
    strategies = dict((k,v) for k,v,o in read(root/'common/ai_strategy/GER_lategame_strategies.txt'))

    class World(Scenario):
        def __init__(self):
            super().__init__(effects,events)
            for tag in ('HOL','BEL','LUX','DEN','NOR','SWE','FIN','SWI'):
                self.countries[tag] = deepcopy(self.countries['POL'])
                self.countries[tag]['original'] = tag
            self.countries['GER'].update(stability=0.6,war_support=0.6,strength=100)
            self.countries['CZE']['exists'] = False
            self.date = '1941.1.1'
            self.revolts = []
        def apply(self,node,actor='GER',root=None,stack=(),character=None):
            root = root or actor
            branch_taken = False
            for key,value,op in node:
                if key in ('if','else_if','else'):
                    if key=='if':branch_taken=False
                    if not branch_taken and (key=='else' or self.condition(one(value,'limit',[]),actor,root,stack)):
                        self.apply([e for e in value if e[0]!='limit'],actor,root,stack,character)
                        branch_taken=True
                elif key == 'every_other_country':
                    for tag,s in list(self.countries.items()):
                        if tag != actor and s['exists'] and self.condition(one(value,'limit',[]),tag,root or actor,(*stack,actor)):
                            self.apply([e for e in value if e[0]!='limit'],tag,root or actor,(*stack,actor))
                elif key == 'start_civil_war':
                    # Record a native civil-war request, not a pretend engine result.
                    self.revolts.append((actor,one(value,'ideology'),float(one(value,'size'))))
                elif key == 'remove_from_faction':
                    self.countries[self.target(value,actor,root or actor,stack)]['faction'] = None
                elif key == 'add_stability':
                    self.countries[actor]['stability'] = self.countries[actor].get('stability',0.5)+float(value)
                elif key in ('add_tech_bonus','set_rule'):
                    self.countries[actor].setdefault(key,[]).append(value)
                else:
                    super().apply([(key,value,op)],actor,root,stack,character)
        def settled(self):
            for tag in ('POL','AUS'): self.countries[tag]['subject']='GER'
        def finish(self,fid):
            self.countries['GER']['focuses'].add(fid)
            self.apply(one(focuses[fid],'completion_reward'))

    assimilation = one(ideas['GER_the_new_reich_integrated'],'modifier')
    check(one(assimilation,'compliance_growth')=='0.10' and one(assimilation,'resistance_target')=='-0.10',
          'GER: assimilation must modify occupier compliance/resistance, not our states occupied by the enemy')
    check(one(assimilation,'compliance_growth_on_our_occupied_states') is None and one(assimilation,'resistance_target_on_our_occupied_states') is None,
          'GER: occupation modifier direction regressed')
    count=0
    # Every reform route and capstone handles both old and new saves without rewards.
    partials=('GER_fund_the_reichswehr','GER_true_constitutional_monarchy','GER_abolish_the_hohenzollerns','GER_german_soviet_republic')
    finals=('GER_gott_mit_uns','GER_arsenal_of_democracy','GER_the_new_reich','GER_workers_militias')
    for fid in partials:
        for spirit in ('GER_imperial_overstretch','GER_imperial_overstretch_2',None):
            w=World();s=w.countries['GER'];s['balance']=0
            if spirit:s['ideas'].add(spirit)
            w.finish(fid)
            check(('GER_imperial_overstretch_2' in s['ideas']) == bool(spirit),f'{fid}: partial reform lost stage')
            before=deepcopy(w.countries);w.apply(effects['GER_nww_repair_army_reform'])
            w.apply(effects['GER_nww_repair_army_reform'])
            check(w.countries==before,f'{fid}: repeated reform repair changes rewards')
            count+=1
    for fid in finals:
        for old in (set(),{'GER_imperial_overstretch'},{'GER_imperial_overstretch_2'},{'GER_imperial_overstretch','GER_imperial_overstretch_2'}):
            w=World();s=w.countries['GER'];s['ideas'] |= old;s['focuses'].add(fid)
            w.apply(effects['GER_nww_repair_army_reform'])
            check(not s['ideas'] & {'GER_imperial_overstretch','GER_imperial_overstretch_2'},f'{fid}: stale debuff retained')
            check(not s['goals'] and s['factories']==0 and s['pp']==200,f'{fid}: save repair repeats rewards')
            w.finish(fid)
            check(not s['ideas'] & {'GER_imperial_overstretch','GER_imperial_overstretch_2'},f'{fid}: capstone retains debuff')
            count+=1
    # Prefer sovereign CZE, otherwise sovereign FRA; never revive a country or guarantee an enemy.
    for eid,fid,gov in [('ger_crisis.10','GER_the_austrian_question','neutrality'),('ger_crisis.40','GER_anschluss_by_force','fascism')]:
        for state,expected in [('CZE','CZE'),('missing_CZE','FRA'),('CZE_subject','FRA'),('CZE_ally','FRA'),('CZE_war','FRA'),('both_absent',None),('FRA_war',None),('FRA_subject',None)]:
            w=World();g=w.countries['GER'];g['government']=gov;g['focuses'].add(fid)
            c,f=w.countries['CZE'],w.countries['FRA']
            c['exists']=state in ('CZE','CZE_subject','CZE_ally','CZE_war')
            if state=='CZE_subject':c['subject']='GER'
            if state=='CZE_ally':c['faction']=g['faction']='GER'
            if state=='CZE_war':c['wars'].add('GER')
            if state=='both_absent':f['exists']=False
            if state=='FRA_war':f['wars'].add('GER')
            if state=='FRA_subject':f['subject']='GER'
            check(w.event(eid,'AUS',1),f'{eid}: valid refusal rejected')
            actual={tag for tag in ('CZE','FRA') if 'AUS' in w.countries[tag]['guarantees']}
            check(actual==({expected} if expected else set()),f'{eid}/{state}: wrong guarantor {actual}')
            check('AUS' in g['goals'],f'{eid}: guarantee preempted the refusal war goal')
            count+=1
    # Refusal guarantees are a real deterrent, not an unconditional permanent lock.
    for mode in ('prepared','early','no_reform','strong_guarantor','other_target','other_guarantor'):
        w=World();w.ai=True;g=w.countries['GER'];g['focuses'].add('GER_gott_mit_uns')
        target='POL' if mode=='other_target' else 'AUS'
        guarantor='ENG' if mode=='other_guarantor' else 'FRA'
        w.countries[guarantor].update(strength=60,major=True,guarantees={target})
        if mode=='early':w.date='1940.12.31'
        if mode=='no_reform':g['focuses'].clear()
        if mode=='strong_guarantor':w.countries[guarantor]['strength']=67
        w.from_country=target
        check(w.condition(w.triggers['nww_GER_ai_unsafe_declaration'])==(mode!='prepared'),f'Austrian deterrent/{mode}: invalid guarantee override')
        count+=1
    # German victories, subjugation or actual wartime capitulation satisfy the eastern gate.
    for target in ('POL','AUS'):
        for mode in ('subject','annexed','capitulated','foreign_subject','foreign_annexation','foreign_capitulation','independent'):
            w=World();w.settled();t=w.countries[target];t['subject']=None
            if mode=='subject':t['subject']='GER'
            if mode=='foreign_subject':t['subject']='SOV'
            if mode in ('annexed','foreign_annexation'):
                t['exists']=False
                if mode=='annexed':w.countries['GER']['owned_states']={'10' if target=='POL' else '4'}
            if mode in ('capitulated','foreign_capitulation'):
                t['capitulated']=True;t['wars'].add('GER' if mode=='capitulated' else 'SOV')
            check(w.condition(w.triggers['GER_nww_eastern_campaigns_settled']) == (mode in ('subject','annexed','capitulated')),f'{target}/{mode}: wrong eastern settlement')
            count+=1
    # Prepared target policy: the Kaiser settles the east; revolution does not require eastern puppets.
    for government,focus in [('neutrality','GER_strike_the_west'),('communism','GER_world_revolution')]:
        for date in ('1940.12.31','1941.1.1','1942.1.1'):
            w=World();w.ai=True;w.date=date;w.settled();g=w.countries['GER']
            g['government']=government;g['focuses'].add(focus)
            w.countries['FRA'].update(strength=100,faction='ENG',major=True)
            w.countries['ENG'].update(strength=100,faction='ENG',major=True)
            w.from_country='FRA'
            check(w.condition(w.triggers['nww_GER_ai_unsafe_declaration'])==(date=='1940.12.31'),f'{focus}/{date}: declaration mandate broken')
            count+=1
        for blocked in ('recovery','war','capitulated','civil_war','weak','unsettled','no_focus','wrong_government','ally','subject'):
            w=World();w.ai=True;w.settled();g=w.countries['GER'];g['government']=government;g['focuses'].add(focus)
            f=w.countries['FRA'];f.update(strength=100,faction='ENG',major=True)
            w.countries['ENG'].update(strength=100,faction='ENG',major=True)
            if blocked=='recovery':g['flags'].add('NWW_GER_campaign_recovery')
            if blocked=='war':g['wars'].add('SOV')
            if blocked=='capitulated':g['capitulated']=True
            if blocked=='civil_war':g['civil_war']=True
            if blocked=='weak':f['strength']=125
            if blocked=='unsettled':w.countries['POL']['subject']=None
            if blocked=='no_focus':g['focuses'].clear()
            if blocked=='wrong_government':g['government']='democratic'
            if blocked=='ally':g['faction']='ENG'
            if blocked=='subject':f['subject']='ENG'
            w.from_country='FRA'
            expected = not (government=='communism' and blocked=='unsettled')
            check(w.condition(w.triggers['nww_GER_ai_unsafe_declaration'])==expected,f'{focus}/{blocked}: safety bypass')
            count+=1
    # Refresh previously blocked/expired goals only after a valid western mandate.
    for fid,expected in [('GER_strike_the_west',{'FRA'}),('GER_the_second_naval_race',{'FRA','ENG'}),('GER_world_revolution',{'FRA','ENG'})]:
        w=World();w.ai=True;w.settled();g=w.countries['GER'];g['government']='communism' if fid=='GER_world_revolution' else 'neutrality'
        g['focuses'].add(fid)
        if fid=='GER_the_second_naval_race':g['focuses'].add('GER_strike_the_west')
        w.date='1940.12.31';w.apply(effects['GER_nww_refresh_western_wargoals']);check(not g['goals'],'Early western repair')
        w.date='1941.1.1';w.apply(effects['GER_nww_refresh_western_wargoals']);check(g['goals']==expected,f'{fid}: missing late goals')
        before=deepcopy(w.countries);w.apply(effects['GER_nww_refresh_western_wargoals']);check(w.countries==before,'Repeated goal reward')
        count+=1
    # Federation membership is a maintained modifier, including entrants and departures.
    w=World();g=w.countries['GER'];g.update(government='democratic',faction='GER')
    g['focuses'].add('GER_european_federation');w.countries['POL']['faction']='GER'
    for tag in ('GER','POL','LTB'):w.apply(effects['GER_nww_refresh_federal_investment'],tag)
    check(all('GER_federal_investment' in w.countries[t]['ideas'] for t in ('GER','POL')),'Federation member lacks bonus')
    check('GER_federal_investment' not in w.countries['LTB']['ideas'],'Nonmember receives federation bonus')
    w.countries['LTB']['faction']='GER';w.apply(effects['GER_nww_refresh_federal_investment'],'LTB')
    check('GER_federal_investment' in w.countries['LTB']['ideas'],'New federation member lacks bonus')
    w.countries['POL']['faction']=None;w.apply(effects['GER_nww_refresh_federal_investment'],'POL')
    check('GER_federal_investment' not in w.countries['POL']['ideas'],'Departed member retains bonus')
    g['government']='fascism'
    for tag in ('GER','LTB'):w.apply(effects['GER_nww_refresh_federal_investment'],tag)
    check(all('GER_federal_investment' not in w.countries[t]['ideas'] for t in ('GER','LTB')),'Federation bonus survives loss of democracy')
    count+=6
    # Political-spirit upgrades retain previous modifiers, using a single stage per branch.
    for fid,old,new in [('GER_the_second_naval_race','GER_gott_mit_uns','GER_gott_mit_uns_naval'),('GER_total_assimilation','GER_the_new_reich','GER_the_new_reich_integrated'),('GER_shield_against_the_reds','GER_arsenal_of_democracy','GER_arsenal_of_democracy_shield'),('GER_nva_mass_mobilization','GER_workers_militias','GER_nva_mass_army')]:
        w=World();g=w.countries['GER'];g['ideas'].add(old);w.finish(fid)
        check(new in g['ideas'] and old not in g['ideas'],f'{fid}: duplicate/lost spirit stage')
        before=dict((k,v) for k,v,o in one(ideas[old],'modifier'));after=dict((k,v) for k,v,o in one(ideas[new],'modifier'))
        check(all(k in after and float(after[k]) >= float(v) for k,v in before.items()),f'{fid}: previous programme benefits lost')
        count+=1
    # Democratic liberation excludes democracies, allies, subjects and absent states.
    for mode in ('valid','democracy','ally','subject','absent','war'):
        w=World();g=w.countries['GER'];g['government']='democratic';f=w.countries['FRA']
        if mode=='democracy':f['government']='democratic'
        if mode=='ally':f['faction']=g['faction']='GER'
        if mode=='subject':f['subject']='SOV'
        if mode=='absent':f['exists']=False
        if mode=='war':g['wars'].add('FRA')
        w.finish('GER_anti_imperialist_crusade')
        check(('FRA' in g['goals'])==(mode=='valid'),f'Liberation/{mode}: invalid target')
        count+=1
    # Moscow split preserves other faction members and does not disband a whole alliance.
    for faction in ('SOV','GER',None):
        w=World();g=w.countries['GER'];g['faction']=faction
        w.countries['SOV']['faction']=faction;w.countries['MKN']['faction']=faction
        w.finish('GER_challenge_moscow')
        check('SOV' in g['goals'] and not w.condition([('is_in_faction_with','SOV','=')]),'Moscow challenge cannot leave alliance')
        check(w.countries['MKN']['faction']==faction,'Moscow split disrupts unrelated allies')
        count+=1
    # Red Rhine uses local readiness and rechecks delayed event replies.
    for support,stability,states,expected in [(0.29,0.5,2,False),(0.30,0.5,2,True),(0.15,0.39,2,True),(0.15,0.40,2,False),(0.40,0.2,1,False)]:
        w=World();g=w.countries['GER'];g['government']='communism';g['focuses'].add('GER_red_rhine')
        w.countries['FRA'].update(communism=support,stability=stability,controlled_states=states)
        check(w.event('ger_crisis.70','FRA',0)==expected,'Red Rhine ignores local readiness')
        check(bool(w.revolts)==expected,'Red Rhine issued incorrect civil-war request')
        count+=1
    for invalid in ('sender_absent','sender_subject','wrong_government','target_subject','target_communist','civil_war'):
        w=World();g=w.countries['GER'];g['government']='communism';g['focuses'].add('GER_red_rhine')
        check(w.event('ger_crisis.70','FRA'), 'Valid agitation not delivered')
        if invalid=='sender_absent':g['exists']=False
        if invalid=='sender_subject':g['subject']='SOV'
        if invalid=='wrong_government':g['government']='democratic'
        if invalid=='target_subject':w.countries['FRA']['subject']='ENG'
        if invalid=='target_communist':w.countries['FRA']['government']='communism'
        if invalid=='civil_war':w.countries['FRA']['civil_war']=True
        before=deepcopy(w.countries)
        for opt in values(events['ger_crisis.70'],'option'):
            w.apply([e for e in opt if e[0] not in ('name','trigger','ai_chance')],'FRA')
        check(w.countries==before and not w.revolts,f'Red Rhine/{invalid}: stale reply executed')
        count+=1
    # Reversed AI strategy: any eligible recipient, not just a fixed European tag list.
    w=World();g=w.countries['GER'];g['government']='democratic';g['focuses'].add('GER_arsenal_of_democracy')
    w.countries['POL']['wars'].add('SOV');w.countries['SOV']['government']='communism'
    aid=strategies['GER_nww_support_threatened_democracies']
    check(one(aid,'reversed')=='yes' and w.condition(one(aid,'enable'),'POL'),'Democratic aid misses a threatened independent state')
    w.countries['POL']['government']='fascism'
    check(not w.condition(one(aid,'enable'),'POL'),'Democratic aid supports fascism')
    count+=2
    # Cross-check every new goal type, technology category and strategy type against native files.
    wargoals={k for k,v,o in one(read(game/'common/wargoals/00_invasion.txt'),'wargoal_types')}
    native_strategy_types=set(re.findall(r'type\s*=\s*(\w+)', '\n'.join(p.read_text(encoding='utf-8-sig') for p in (game/'common/ai_strategy').glob('*.txt'))))
    for name,body in strategies.items():
        check(one(body,'abort_when_not_enabled')=='yes',f'{name}: strategy never aborts')
        for node in values(body,'ai_strategy'):check(one(node,'type') in native_strategy_types,f'{name}: invalid strategy type')
    categories={v for k,v,o in walk(read(game/'common/technology_tags/00_technology.txt')) if k is None}
    for focus in focuses.values():
        for k,v,o in walk(one(focus,'completion_reward',[])):
            if k=='create_wargoal':check(one(v,'type') in wargoals,'Unknown goal type')
            if k=='add_tech_bonus':check(one(v,'category') in categories,'Unknown research category')
    for path in (root/'common/scripted_effects/GER_lategame_effects.txt',root/'common/scripted_triggers/GER_lategame_triggers.txt',root/'common/on_actions/GER_lategame_on_actions.txt'):
        check(not list(engine_script_errors(read(path))),f'{path.name}: invalid engine syntax')
    print(f'PASS: {count} GER late-game reform, guarantor, coalition, old-save, federation, uprising and faction-split cases; native goal/research/AI tokens')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--game',required=True,type=Path)
    args=parser.parse_args();errors=[]
    validate_lategame(Path(__file__).resolve().parents[1],args.game,lambda ok,msg:errors.append(msg) if not ok else None)
    for error in errors:print('ERROR:',error)
    return bool(errors)


if __name__=='__main__':raise SystemExit(main())
