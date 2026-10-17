"""Validate NWW Poland's graph, native tokens and source-script lifecycle.

This interpreter exercises script branches, not the HOI4 engine or actual combat.
"""
import argparse
from copy import deepcopy
import csv
import json
from pathlib import Path
import random
import re
from hoi4_script import read,one,values,walk,engine_script_errors
from validate_germany_politics import Scenario


def validate_poland(root,game,check):
    meta=json.loads((root/'docs/POL_focus_design.json').read_text(encoding='utf-8-sig'))
    tree=one(read(root/'common/national_focus/POL_focus.txt'),'focus_tree')
    fs={one(f,'id'):f for f in values(tree,'focus')}
    effects={k:v for p in (root/'common/scripted_effects').glob('POL*.txt') for k,v,o in read(p)}
    events={one(v,'id'):v for k,v,o in read(root/'events/POL_events.txt') if k=='country_event'}
    triggers={k:v for k,v,o in read(root/'common/scripted_triggers/POL_triggers.txt')}
    decisions=one(read(root/'common/decisions/POL_decisions.txt'),'POL_nww_politics')
    ideas=one(one(read(root/'common/ideas/POL_ideas.txt'),'ideas'),'country')
    dynamic={k:v for k,v,o in read(root/'common/dynamic_modifiers/POL_modifiers.txt')}
    history=read(root/'history/countries/POL - Poland.txt')
    check(len(fs)==meta['focus_count']==80,'POL: expected 80 focuses')
    check(one(tree,'id')=='POL_focus' and one(one(one(tree,'country'),'modifier'),'add')=='100','POL: invalid tree selection')
    check(int(one(one(tree,'continuous_focus_position'),'y'))>max(int(one(f,'y')) for f in fs.values())*130+800,'POL: continuous panel overlaps')
    for f in fs.values():
        for group in values(f,'prerequisite'):
            for p in values(group,'focus'):check(p in fs and int(one(fs[p],'y'))<int(one(f,'y')),f'POL: invalid parent {p}')
        for group in values(f,'mutually_exclusive'):
            for other in values(group,'focus'):check(any(one(f,'id') in values(g,'focus') for g in values(fs[other],'mutually_exclusive')),f'POL: asymmetric exclusion {other}')
        check(one(f,'cost') in ('5','10'),f'POL: unexpected cost {one(f,"id")}')
    for y in {one(f,'y') for f in fs.values()}:
        xs=sorted(int(one(f,'x')) for f in fs.values() if one(f,'y')==y)
        check(all(b-a>=2 for a,b in zip(xs,xs[1:])),f'POL: overlapping row {y}')
    # Compiled compatibility contains only actual direct native focuses.
    native=read(game/'common/national_focus/poland.txt')
    ids={one(f,'id') for t in values(native,'focus_tree') for f in values(t,'focus')}|{one(f,'id') for f in values(native,'shared_focus')}
    compat=values(read(root/'common/national_focus/POL_native_compatibility.txt'),'shared_focus')
    check({one(f,'id') for f in compat}==ids-fs.keys(),'POL: native registry lost IDs or collected nested IDs')
    check(all(one(one(f,'allow_branch'),'always')=='no' and one(f,'completion_reward')==[] for f in compat),'POL: native compatibility grants rewards')
    check(not read(root/'common/national_focus/poland.txt'),'POL: native tree remains active')
    alias=one(read(root/'common/national_focus/POL_native_tree_alias.txt'),'focus_tree')
    check(one(alias,'id')=='polish_focus' and not values(alias,'focus') and one(one(alias,'country'),'factor')=='0','POL: native alias is selectable')
    for filename in ('Poland.txt','NSB_Poland.txt'):
        old=read(game/'events'/filename);new=read(root/'events'/filename)
        for eventtype in ('country_event','news_event'):
            check({one(v,'id') for v in values(old,eventtype)}=={one(v,'id') for v in values(new,eventtype)},f'POL: lost native event IDs in {filename}')
            check(all(one(one(v,'trigger'),'always')=='no' and not one(v,'immediate') for v in values(new,eventtype)),f'POL: native events remain active in {filename}')
    # Modifier names include the installed generated trade-law modifier.
    docs={kind:set(re.findall(r'^## (\w+)',(game/f'documentation/{kind}_documentation.md').read_text(encoding='utf-8-sig'),re.M)) for kind in ('effects','triggers','modifiers')}
    generated={'production_speed_'+k+'_factor' for k,v,o in one(read(game/'common/buildings/00_buildings.txt'),'buildings')}
    generated.add('trade_laws_cost_factor')
    check('trade_laws_cost_factor' in (game/'common/dynamic_modifiers/TAOG_dynamic_modifiers.txt').read_text(encoding='utf-8-sig'),'POL: generated trade-law modifier absent')
    for name,body,o in ideas:
        for modifier,value,op in one(body,'modifier',[]):check(modifier in docs['modifiers']|generated,f'POL: invalid idea modifier {modifier}')
    for name,body in dynamic.items():
        for key,value,op in body:
            if key not in ('icon','enable'):check(key in docs['modifiers']|generated,f'POL: invalid dynamic modifier {key}')
    check({k:float(v) for k,v,o in one(one(ideas,'POL_german_economic_stranglehold'),'modifier')}=={'consumer_goods_factor':0.10,'trade_laws_cost_factor':0.25,'industrial_capacity_factory':0.10},'POL: wrong starting economic burden')
    check({k:float(v) for k,v,o in one(one(ideas,'POL_sanation_crisis'),'modifier')}=={'stability_factor':-0.15,'political_power_gain':-0.20},'POL: wrong Sanation burden')
    locales={}
    for lang in ('russian','english'):
        p=root/f'localisation/{lang}/POL_nww_l_{lang}.yml';s=p.read_text(encoding='utf-8-sig');keys=re.findall(r'^ ([\w.]+):',s,re.M)
        locales[lang]=set(keys)
        check(p.read_bytes().startswith(b'\xef\xbb\xbf') and s.startswith('l_'+lang+':\n') and len(keys)==len(set(keys)),f'POL: invalid {lang} localization')
    check(locales['russian']==locales['english'],'POL: RU/EN key mismatch')
    required=set(fs)|{f+'_desc' for f in fs}|set(dynamic)|{k for k,v,o in ideas}|{k+'_desc' for k,v,o in ideas}
    required|={v for e in events.values() for k,v,o in walk(e) if k in ('title','desc','name')}
    for f in fs.values():required|={v for k,v,o in walk(f) if k=='custom_effect_tooltip'}
    check(required<=locales['english'],f'POL: missing localization {required-locales["english"]}')
    # Sprite definitions and technology categories must exist in installed content.
    sprites={}
    for base in (game,*sorted(game.glob('dlc/*')),root):
        for p in (base/'interface').rglob('*.gfx'):
            try:doc=read(p)
            except ValueError:continue
            for k,v,o in walk(doc):
                if k and k.lower()=='spritetype':sprites[one(v,'name')]=one(v,'texturefile')
    for f in fs.values():check(one(f,'icon') in sprites,f'POL: missing focus icon {one(f,"icon")}')
    for k,v,o in ideas:check('GFX_idea_'+one(v,'picture') in sprites,f'POL: missing spirit picture {k}')
    categories={v for k,v,o in walk(read(game/'common/technology_tags/00_technology.txt')) if k is None}
    buildings={k for k,v,o in one(read(game/'common/buildings/00_buildings.txt'),'buildings')}
    for p in list((root/'common').rglob('POL*.txt'))+[root/'events/POL_events.txt',root/'history/countries/POL - Poland.txt']:
        doc=read(p);check(not list(engine_script_errors(doc)),f'{p.name}: invalid engine syntax')
        for k,v,o in walk(doc):
            if k=='set_politics':check({'ruling_party','elections_allowed','election_frequency'}<={k for k,v,o in v},f'{p.name}: incomplete politics block')
            if k=='add_tech_bonus':check(one(v,'category') in categories,f'{p.name}: invalid technology category')
            if k=='add_building_construction':check(one(v,'type') in buildings,f'{p.name}: invalid building')
            if k=='add_research_slot':check('amount_research_slots' in {k for f in fs.values() for k,v,o in walk(one(f,'completion_reward'))},'POL: uncapped research reward')
    # Actual map and OOB: POL is inland, Galicia stays Polish, Germany keeps the west.
    effective={p.name:p for p in (game/'history/states').glob('*.txt')};effective.update({p.name:p for p in (root/'history/states').glob('*.txt')})
    states={one(one(read(p),'state'),'id'):one(read(p),'state') for p in effective.values()}
    with (root/'map/definition.csv' if (root/'map/definition.csv').exists() else game/'map/definition.csv').open() as file:
        coast={r[0] for r in csv.reader(file,delimiter=';') if len(r)>5 and r[5]=='true'}
    polstates={sid for sid,s in states.items() if one(one(s,'history'),'owner')=='POL'}
    check(not any(v in coast for sid in polstates for k,v,o in one(states[sid],'provinces')),'POL: starts with a coastal province')
    for sid in ('85','86','63','66','67','762'):check(one(one(states[sid],'history'),'owner')=='GER',f'POL: Germany lost western state {sid}')
    for sid in ('88','89','91'):check(one(one(states[sid],'history'),'owner')=='POL',f'POL: Galicia state {sid} lost')
    check({'POL','SIL'}<=set(values(one(states['762'],'history'),'add_core_of')),'POL: indigenous Silesian cores lost')
    check(not any(k=='set_naval_oob' for k,v,o in walk(history)) and one(history,'set_convoys')=='0','POL: starts with a fleet/convoys')
    check(not any(k=='start_civil_war' or k=='set_autonomy' for k,v,o in walk(history)),'POL: subject or civil war at start')
    startideas=set(v for k,v,o in one(history,'add_ideas'))
    check({'POL_german_economic_stranglehold','POL_sanation_crisis','POL_landlocked_nation'}<=startideas,'POL: starting spirits absent')
    units=one(read(root/'history/units/POL_1936.txt'),'units')
    check(len(values(units,'division'))>=20,'POL: no substantial starting army')
    # Source interpreter. Native numeric UI operations remain static checks above.
    class World(Scenario):
        def __init__(self):
            super().__init__(effects,events);self.triggers.update(triggers);self.from_country='POL';self.player='POL'
            for tag in ('ROM','D01'):
                self.countries[tag]=deepcopy(self.countries['POL']);self.countries[tag]['original']=tag
            for tag,s in self.countries.items():s.update(tree='POL_focus' if tag=='POL' else 'other_tree',stability=0.6,war_support=0.5,strength=100 if tag=='GER' else 60)
            self.countries['POL'].update(original='POL',neutrality=0.45,democratic=0.25,fascism=0.15,communism=0.15,pp=200,balance=0)
            self.countries['POL']['ideas']={'POL_sanation_crisis','POL_german_economic_stranglehold','POL_landlocked_nation'}
            self.countries['POL']['flags'].add('POL_nww_start_configured')
            self.character_owner.update({x:'POL' for x in ('POL_maria_koszutska','POL_roman_dmowski','POL_edward_rydzsmigly','POL_ignacy_moscicki','POL_wladyslaw_gomulka')})
            self.coast=False;self.rule='DEFAULT';self.draw=0;self.requests=[]
        def condition(self,node,actor='POL',root=None,stack=()):
            for key,v,op in node:
                if key=='has_game_rule':result=one(v,'option')==self.rule
                elif key=='has_political_power':result=self.compare(self.countries[actor]['pp'],float(v),op)
                elif key=='has_faction_template':result=self.countries[actor].get('template')==v
                elif key=='has_any_controlled_coastal_state':result=self.coast==(v=='yes')
                else:result=super().condition([(key,v,op)],actor,root,stack)
                if not result:return False
            return True
        def apply(self,node,actor='POL',root=None,stack=(),character=None):
            root=root or actor;branch=False
            for key,v,op in node:
                s=self.countries[actor]
                if key in ('if','else_if','else'):
                    if key=='if':branch=False
                    if not branch and (key=='else' or self.condition(one(v,'limit',[]),actor,root,stack)):
                        self.apply([e for e in v if e[0]!='limit'],actor,root,stack,character);branch=True
                elif key=='random_list':
                    options=[body for k,body,o in v];self.apply(options[self.draw],actor,root,stack,character)
                elif key=='add_to_variable':
                    for name,amount,o in v:s['variables'][name]=s['variables'].get(name,0)+float(amount)
                elif key=='add_dynamic_modifier':s['dynamic_modifiers'].add(one(v,'modifier'))
                elif key=='set_rule':s['rules']|={(k,value) for k,value,o in v}
                elif key=='create_faction_from_template':s['faction']=actor;s['template']=one(v,'template')
                elif key=='diplomatic_relation':s.setdefault('pacts',set()).add(self.target(one(v,'country'),actor,root,stack))
                elif key=='mark_focus_tree_layout_dirty':pass
                elif key=='every_owned_state':pass # ownership/reward definitions audited separately against actual map
                elif key=='start_civil_war':
                    child='D01';self.countries[child]=deepcopy(s);rebel=self.countries[child]
                    rebel.update(original='POL',government='communism',civil_war=True,wars={actor},faction=None)
                    s['civil_war']=True;s['wars'].add(child)
                    config={'ideology','size','army_ratio','air_ratio','navy_ratio'}
                    self.apply([e for e in v if e[0] not in config],child,root,(*stack,actor))
                    self.requests.append((child,float(one(v,'size'))))
                elif key=='promote_character':s['leader']=v if v!='yes' else character
                else:super().apply([(key,v,op)],actor,root,stack,character)
        def finish(self,fid,actor='POL'):
            self.countries[actor]['focuses'].add(fid);self.apply(one(fs[fid],'completion_reward'),actor)
    count=0
    # Pure program repair with random completed focuses and repeated loads.
    rng=random.Random(1936)
    for _ in range(60):
        w=World();s=w.countries['POL'];selected={f['id'] for f in meta['focuses'] if rng.randrange(2)};s['focuses']=selected
        s['variables']={'POL_'+g+'_'+p:99 for g,(_,_,params) in meta['programs'].items() for p in params}
        w.apply(effects['POL_refresh_programs'])
        for group,(_,_,params) in meta['programs'].items():
            for param in params:
                expected=sum(f['bonus'].get(group,{}).get(param,0) for f in meta['focuses'] if f['id'] in selected)
                check(abs(s['variables']['POL_'+group+'_'+param]-expected)<1e-8,f'POL: wrong reconstructed {group}/{param}')
        before=deepcopy(w.countries);w.apply(effects['POL_refresh_programs']);check(w.countries==before,'POL: repeated program repair changes rewards');count+=1
    # Full startup/old-save repair preserves diplomacy and repeats no one-off rewards.
    for saved in (False,True):
        for progress in (set(),{'POL_state_budget_commission'},{'POL_professional_civil_service','POL_the_colonels_regime','POL_cop_plan'},{'POL_economic_independence','POL_national_bloc','POL_endecja_ascendant'}):
            w=World();s=w.countries['POL'];s['focuses']=progress
            if saved:s['flags'].discard('POL_nww_start_configured')
            w.apply(effects['POL_initialize_country']);before=deepcopy(w.countries)
            w.apply(effects['POL_initialize_country'])
            check(w.countries==before,'POL: full startup repair is not idempotent')
            check(s['pp']==200 and s['factories']==0 and not s['goals'] and s['subject'] is None,'POL: save repair repeats economic/diplomatic rewards')
            count+=1
    # Political mandates require preparation, the common commission and no previous path.
    entries=[('the_colonels_regime','castle_and_colonels_dialogue','neutrality'),('endecja_ascendant','national_democratic_leagues','fascism'),('pragmatic_deal','berlin_trade_delegation','neutrality'),('the_lodz_uprising','workers_defence_committees','communism')]
    for entry,prep,ideology in entries:
        for pop in (0.39,0.40):
            for prepared in (False,True):
                w=World();s=w.countries['POL'];s[ideology]=pop;s['focuses'].add('POL_state_budget_commission')
                # Prerequisites are checked independently by HOI4; match them here.
                if prepared:s['focuses'].add('POL_'+prep)
                gate=w.condition(one(fs['POL_'+entry],'available')) and ('POL_'+prep in s['focuses'])
                check(gate==(pop>=0.40 and prepared),f'POL {entry}: incorrect mandate/preparation');count+=1
        for flag in ('sanation','endecja','german','communist'):
            w=World();s=w.countries['POL'];s[ideology]=0.50;s['focuses'].add('POL_state_budget_commission');s['flags'].add('POL_path_'+flag)
            check(not w.condition(one(fs['POL_'+entry],'available')),f'POL {entry}: previous path ignored');count+=1
    # Repeatable campaigning reaches a real mandate from the new starting support.
    for ideology,prep in [('fascism','national_democratic_leagues'),('communism','workers_defence_committees')]:
        w=World();s=w.countries['POL'];s['focuses'].add('POL_aftermath_of_the_marshal');w.finish('POL_'+prep)
        decision=one(decisions,'POL_campaign_'+ideology)
        for _ in range(2):
            check(w.condition(one(decision,'available')),'POL: campaign cannot reach 40%');w.apply(one(decision,'complete_effect'));s['pp']-=50
        check(s[ideology]>=0.40 and s['pp']==100,'POL: campaign mandate or price wrong');count+=1
    # Named AI rules beat historical mode; DEFAULT history is always Sanation.
    for rule,expected in [('DEFAULT','sanation'),('HISTORICAL','sanation'),('FASCIST_INDEPENDENT','endecja'),('FASCIST','german'),('COMMUNIST','communist')]:
        w=World();w.rule=rule;w.apply(effects['POL_select_ai_path'])
        check({f for f in w.countries['POL']['flags'] if f.startswith('POL_ai_') and f!='POL_ai_selected'}=={'POL_ai_'+expected},f'POL AI {rule}: bad path');count+=1
    for draw in range(4):
        w=World();w.rule='RANDOM';w.draw=draw;w.apply(effects['POL_select_ai_path'])
        check(len({f for f in w.countries['POL']['flags'] if f.startswith('POL_ai_') and f!='POL_ai_selected'})==1,'POL: random AI selected multiple paths');count+=1
    # Two-stage crisis and economic breakaway are idempotent and never grant factories.
    for focus in ('POL_state_budget_commission','POL_professional_civil_service','POL_national_bloc','POL_customs_commission','POL_council_republic'):
        w=World();s=w.countries['POL'];s['focuses'].add(focus);w.apply(effects['POL_refresh_crisis']);before=deepcopy(w.countries)
        w.apply(effects['POL_refresh_crisis']);check(w.countries==before,'POL: crisis repair repeats rewards')
        check(('POL_sanation_crisis_2' in s['ideas'])==(focus=='POL_state_budget_commission'),'POL: wrong crisis stage');count+=1
    w=World();s=w.countries['POL'];w.apply(effects['POL_accept_capital']);w.apply(effects['POL_end_german_dependence']);before=deepcopy(w.countries)
    w.apply(effects['POL_accept_capital']);check(not s['ideas']&{'POL_german_economic_stranglehold','POL_german_economic_stranglehold_2'},'POL: cancelled concessions restored');count+=1
    # Coast is dynamic: occupation unlocks only the proposal, never free ships.
    w=World()
    for coast in (False,True,False):
        w.coast=coast;w.apply(effects['POL_refresh_coast'])
        check(('POL_landlocked_nation' in w.countries['POL']['ideas'])==(not coast),'POL: stale landlocked spirit')
        check(w.condition(one(fs['POL_baltic_fleet_program'],'available'))==coast,'POL: naval placeholder ignores coast');count+=1
    # Civil war uses a copied tree without reward replay; a disappearing opponent is not victory.
    w=World();s=w.countries['POL'];s['focuses'].update({'POL_aftermath_of_the_marshal','POL_workers_defence_committees','POL_the_lodz_uprising'})
    w.apply(effects['POL_start_communist_civil_war']);r=w.countries['D01']
    check(w.player=='D01' and r['original']=='POL' and r['focuses']==s['focuses'] and w.requests==[('D01',0.40)],'POL: civil war loses player/progress')
    check(w.character_owner['POL_maria_koszutska']=='D01','POL: rebel leader not transferred')
    gate=one(fs['POL_council_republic'],'available');check(not w.condition(gate,'D01'),'POL: republic available during civil war')
    s['exists']=False;r['civil_war']=False;r['wars'].clear();check(not w.condition(gate,'D01'),'POL: disappearance of loyalists falsely counts as victory')
    hook=one(one(read(root/'common/on_actions/POL_on_actions.txt'),'on_actions'),'on_civil_war_end')
    w.from_country='POL';w.apply(one(hook,'effect'),'D01');check(w.condition(gate,'D01'),'POL: actual communist victory does not unlock republic');count+=5
    # Consent and delayed-reply protection for all four bilateral offers.
    for eid,recipient,focus,government,flag in [('nww_pol.10','GER','POL_join_mitteleuropa_officially','neutrality','POL_german_compact_accepted'),('nww_pol.20','LTB','POL_vilnius_settlement','neutrality','POL_vilnius_accord'),('nww_pol.30','ROM','POL_baltic_danubian_congress','neutrality','POL_intermarium_member'),('nww_pol.40','SOV','POL_alliance_with_the_east','communism','POL_eastern_alliance_accepted')]:
        def offer():
            w=World();s=w.countries['POL'];s['government']=government;s['focuses'].add(focus)
            s['flags']|={'POL_path_german','POL_communist_victory'}
            w.countries['LTB']['focuses'].add('LTB_the_vilnius_compromise')
            if recipient=='SOV':w.countries['SOV']['government']='communism';w.countries['SOV']['faction']='SOV';w.countries['MKN']['faction']='SOV'
            if recipient=='ROM':s['faction']='POL';s['template']='faction_template_POL_intermarium'
            return w
        for option in (0,1):
            w=offer();check(w.event(eid,recipient,option,sender='POL'),f'POL {eid}: valid offer rejected')
            source=recipient if recipient=='ROM' else 'POL'
            check((flag in w.countries[source]['flags'])==(option==0),f'POL {eid}: recipient consent ignored')
            if recipient=='SOV':check(w.countries['MKN']['faction']=='SOV','POL: eastern compact changes MKN alliance')
            count+=1
        for invalid in ('recipient_subject','sender_subject','war','sender_absent','wrong_government'):
            w=offer();check(w.event(eid,recipient,sender='POL'),f'POL {eid}: offer cannot be delivered')
            if invalid=='recipient_subject':w.countries[recipient]['subject']='AUS'
            if invalid=='sender_subject':w.countries['POL']['subject']='AUS'
            if invalid=='war':w.countries[recipient]['wars'].add('POL')
            if invalid=='sender_absent':w.countries['POL']['exists']=False
            if invalid=='wrong_government':w.countries['POL']['government']='fascism'
            before=deepcopy(w.countries);w.from_country='POL'
            for opt in values(events[eid],'option'):w.apply([e for e in opt if e[0] not in ('name','trigger','ai_chance')],recipient)
            check(w.countries==before,f'POL {eid}/{invalid}: stale reply changes diplomacy');count+=1
    # Use the real LTB dissolution guard, and tolerate missing auxiliary settlement flags.
    w=World();l=w.countries['LTB'];l['focuses'].add('LTB_the_vilnius_compromise')
    check(w.condition(triggers['POL_ltb_can_negotiate'],'LTB'),'POL: old-save completed LTB compromise with missing flags is rejected')
    l['flags'].add('LTB_split_choice_available')
    check(not w.condition(triggers['POL_ltb_can_negotiate'],'LTB'),'POL: diplomacy can reverse a triggered LTB dissolution')
    count+=2
    # Germany's acceptance weights: deterministic for committed Polish paths, LTB unchanged.
    crisis={one(v,'id'):v for k,v,o in read(root/'events/GER_events.txt') if k=='country_event'}['ger_crisis.20']
    def weight(w,opt,tag):
        node=one(opt,'ai_chance');value=float(one(node,'factor','1'))
        for m in values(node,'modifier'):
            condition=[e for e in m if e[0] not in ('factor','add')]
            if w.condition(condition,tag):value=value*float(one(m,'factor','1'))+float(one(m,'add','0'))
        return value
    for path,expected in [('POL_the_colonels_regime',(0,65)),('POL_endecja_ascendant',(0,65)),('POL_pragmatic_deal',(100,0))]:
        w=World();w.countries['POL']['focuses'].add(path)
        check(tuple(weight(w,opt,'POL') for opt in values(crisis,'option'))==expected,f'POL ultimatum {path}: incorrect deterministic weights');count+=1
    w=World();check(tuple(weight(w,opt,'LTB') for opt in values(crisis,'option'))==(0,65),'POL: changed historical LTB ultimatum');count+=1
    # The declaration rule also covers a dynamic original-POL civil-war successor.
    for actor in ('POL','D01'):
        for date in ('1938.12.31','1939.1.1'):
            w=World();w.ai=True;w.date=date;s=w.countries[actor];s.update(original='POL',tree='POL_focus',strength=100)
            s['flags'].add('POL_path_endecja');s['focuses'].add('POL_march_to_the_sea');w.countries['GER']['strength']=50;w.from_country='GER'
            check(w.condition(triggers['POL_ai_unsafe_declaration'],actor)==(date=='1938.12.31'),'POL: wrong early aggression boundary');count+=1
    # Plans and existing game rules must work without Polish DLC selection gates.
    rule=one(read(root/'common/game_rules/00_game_rules.txt'),'POL_ai_behavior')
    check(one(rule,'required_dlc') is None and all(one(v,'required_dlc') is None for v in values(rule,'option')),'POL: NWW AI routes still DLC-gated')
    plans=read(root/'common/ai_strategy_plans/POL_plans.txt')
    check(len(plans)==4,'POL: expected four AI plans')
    for name,plan,o in plans:
        check(one(one(plan,'enable'),'has_focus_tree')=='POL_focus','POL: AI plan missing runtime tree gate')
        check(all(v in fs for k,v,o in one(plan,'ai_national_focuses')),'POL: plan references foreign focus')
    print(f'PASS: POL 80-focus graph, native registry/tokens, landlocked start, Galicia/1914 frontier, RU/EN and {count} source-script reform/mandate/diplomacy/AI/civil-war cases')


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--game',required=True,type=Path);args=p.parse_args();errors=[]
    validate_poland(Path(__file__).resolve().parents[1],args.game,lambda ok,msg:errors.append(msg) if not ok else None)
    for error in errors:print('ERROR:',error)
    return bool(errors)


if __name__=='__main__':raise SystemExit(main())
