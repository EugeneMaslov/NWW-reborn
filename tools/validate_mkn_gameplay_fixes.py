"""Regressions for issues observed during the user's MKN campaign.

Runs source scripts and native-token checks; does not reproduce engine UI/combat.
"""
from copy import deepcopy
from itertools import product
import json
from PIL import Image
from hoi4_script import read,one,values,walk,tree_focuses,engine_script_errors
from validate_mkn_communists import RevkomWorld
from validate_mkn_military import MilitaryModel


class GameplayWorld(RevkomWorld):
    def run(self, token, current='MKN'):
        self.apply(self.effects[token],current)

    def __init__(self,root):
        super().__init__()
        self.root_path=root
        self.definitions={k:v for p in (root/'common/ideas').glob('MKN*.txt') for k,v,o in one(one(read(p),'ideas',[]),'country',[])}
        self.operatives={}
        for c in self.countries.values():c['operatives']=[]

    def data(self,scope):
        return self.operatives[scope] if scope in getattr(self,'operatives',{}) else super().data(scope)

    def test(self,nodes,current='MKN',previous=None):
        for k,v,o in nodes or []:
            c=self.data(current)
            if k=='has_dlc':ok=v=='La Resistance'
            elif k=='has_trait':ok=v in c['traits']
            elif k=='has_war_with_major':ok=bool(c['wars'] & {'GER','SOV'})==(v=='yes')
            else:ok=super().test([(k,v,o)],current,previous)
            if not ok:return False
        return True

    def apply(self,nodes,current='MKN',previous=None):
        matched=False
        for k,v,o in nodes or []:
            c=self.data(current)
            if k in {'if','else_if'}:
                if k=='if':matched=False
                if not matched and self.test(one(v,'limit'),current,previous):
                    self.apply([n for n in v if n[0]!='limit'],current,previous);matched=True
            elif k=='else':
                if not matched:self.apply(v,current,previous)
                matched=True
            elif k=='add_ideas':
                if v not in c['ideas']:
                    c['ideas'].add(v);self.apply(one(self.definitions[v],'on_add',[]),current,previous)
            elif k=='remove_ideas':
                if v in c['ideas']:
                    c['ideas'].remove(v);self.timed.pop((current,v),None)
                    self.apply(one(self.definitions[v],'on_remove',[]),current,previous)
            elif k=='add_timed_idea':
                iid=one(v,'idea');self.apply([('add_ideas',iid,'=')],current,previous)
                self.timed[(current,iid)]=self.day+int(one(v,'days'))
            elif k=='swap_ideas':
                old,new=one(v,'remove_idea'),one(v,'add_idea');deadline=self.timed.get((current,old))
                self.apply([('remove_ideas',old,'='),('add_ideas',new,'=')],current,previous)
                if deadline is not None:self.timed[(current,new)]=deadline
            elif k=='load_focus_tree':
                assert one(v,'keep_completed')=='yes'
                c['tree']=one(v,'tree')
            elif k=='every_operative':
                for token in c['operatives']:
                    if self.test(one(v,'limit',[]),token,current):self.apply([n for n in v if n[0]!='limit'],token,current)
            elif k=='remove_unit_leader_trait':c['traits'].discard(v)
            elif k=='remove_core_of':c['cores'].discard(self.scope(v,current,previous) or v)
            elif k=='annex_country':
                target=self.scope(one(v,'target'),current,previous) or one(v,'target')
                super().apply([(k,[(key,target if key=='target' else value,op) for key,value,op in v],o)],current,previous)
            else:super().apply([(k,v,o)],current,previous)

    def advance(self,days):
        self.day+=days
        for (tag,iid),deadline in list(self.timed.items()):
            if deadline<=self.day:self.apply([('remove_ideas',iid,'=')],tag)


def validate_gameplay_fixes(root,game,check,localized):
    fs={one(f,'id'):f for f in tree_focuses(one(read(root/'common/national_focus/MKN.txt'),'focus_tree'),root/'common/national_focus')}
    registry=json.loads((root/'docs/MKN_party_progression.json').read_text())
    parties=('fascism','democratic','neutrality','communism')
    cases=0
    check(len(registry['focus_parties'])==79,'MKN parties: missing political branch ownership')
    # All completed policies remain earned while exactly one party's spirits act.
    w=GameplayWorld(root);c=w.countries['MKN'];c['focuses']=set(registry['focus_parties']);c['flags']['MKN_party_reforms_enabled']=-1
    c['flags']['mkn_batko_departed']=-1
    for gov in (*parties,*reversed(parties)):
        c['government']=gov
        before=(c['pp'],c['manpower'] if 'manpower' in c else 0,deepcopy(w.states),set(c['focuses']))
        w.run('MKN_sync_party_spirits');w.run('MKN_sync_party_spirits')
        for iid,item in registry['ideas'].items():
            eligible=item['party']==gov and bool(item['focuses'])
            if iid=='MKN_field_counter_intelligence_reserve_idea':eligible=False
            if iid=='MKN_field_counter_intelligence_idea':eligible=gov=='fascism'
            check((iid in c['ideas'])==eligible,'MKN party switch: inactive/unearned spirit '+iid+' at '+gov)
        check(before==(c['pp'],c.get('manpower',0),w.states,set(c['focuses'])),'MKN party switch: repeats a physical focus reward or clears progress')
        cases+=1
    for gov,entry in ((g,f) for f,g in registry['entries'].items()):
        w=GameplayWorld(root);c=w.countries['MKN'];c.update(government=gov,tree='generic_focus',subject=True)
        c['flags']['MKN_crisis_legacy_settled']=-1;c['focuses']={'MKN_congress_1936','MKN_question_of_supply',*registry['entries']}
        c['popularity']={g:0.10 for g in parties}
        before=set(c['focuses']);w.run('MKN_prepare_party_revival');w.run('MKN_prepare_party_revival')
        check(c['tree']=='MKN_focus' and before<=c['focuses'] and 'MKN_departure_of_batko' in c['focuses'],'MKN release: lost completed focuses or retains generic/locked tree')
        for fid,party in registry['entries'].items():
            check(w.test(one(fs[fid],'available'))==(party==gov),'MKN release: current-party entry inaccessible or permits another imposed switch')
        cases+=1
    for gov,entry in ((g,f) for f,g in registry['entries'].items()):
        w=GameplayWorld(root);c=w.countries['MKN'];c.update(government=gov,subject=False)
        c['focuses']={'MKN_congress_1936','MKN_question_of_supply'}
        for popularity in (0.39,0.40):
            c['popularity'][gov]=popularity
            check(w.test(one(fs[entry],'available'))==(popularity>=0.40),'MKN initial transition: 40% mandate removed')
            cases+=1
    # Temporary effects preserve absolute expiry, including the leased factory.
    for iid,gov in (('MKN_voucher_transition_idea','democratic'),('MKN_betrayed_twice','communism'),('MKN_grain_barter_factory_idea','neutrality')):
        w=GameplayWorld(root);c=w.countries['MKN'];c['government']=gov
        w.apply([('add_timed_idea',[('idea',iid,'='),('days','180','=')],'=')]);w.advance(30)
        c['government']='fascism';w.run('MKN_sync_party_timed_spirits')
        check(iid not in c['ideas'] and w.timed.get(('MKN',iid+'_inactive'))==180,'MKN temporary party spirit: old effect remains active or expiry resets')
        if gov=='neutrality':check(c['offsite']['industrial_complex']==0,'MKN inactive grain contract leaves its factory')
        w.advance(30);c['government']=gov;w.run('MKN_sync_party_timed_spirits')
        check(iid in c['ideas'] and w.timed[('MKN',iid)]==180,'MKN restored temporary spirit: remaining time not preserved')
        if gov=='neutrality':check(c['offsite']['industrial_complex']==1,'MKN grain contract fails to restore its leased factory')
        w.advance(120);check(iid not in c['ideas'],'MKN temporary effect survives its original expiry')
        if gov=='neutrality':check(c['offsite']['industrial_complex']==0,'MKN grain lease leaves a permanent factory')
        cases+=1
    effects={k:v for p in (root/'common/scripted_effects').glob('*.txt') if 'mkn' in p.name.lower() for k,v,o in read(p)}
    for gov in parties:
        actual=MilitaryModel(effects,set(registry['focus_parties']));actual.government=gov
        expected=MilitaryModel(effects,{f for f,g in registry['focus_parties'].items() if g==gov});expected.government=gov
        for m in (actual,expected):m.apply(effects['nww_mkn_rebuild_industry']);m.rebuild()
        check(dict(actual.variables)==dict(expected.variables),'MKN shared spirits: modifiers of former parties remain active at '+gov)
        before=dict(actual.variables);actual.apply(effects['nww_mkn_rebuild_industry']);actual.rebuild()
        check(before==dict(actual.variables) and not actual.oneoffs,'MKN shared spirit rebuild stacks or replays factories/XP')
        cases+=1
    # One focus from the emergency branch is enough for the post-war event.
    for focus in ('MKN_death_or_freedom','MKN_hide_the_machines','MKN_marusya_womens_battalions','MKN_evacuation_soviets','MKN_shadows_in_the_forests','MKN_black_vengeance'):
        reward=one(fs[focus],'completion_reward');check(one(reward,'MKN_begin_desperate_defense')=='yes',focus+': partial branch use is not recorded')
    for used in (False,True):
        w=GameplayWorld(root);c=w.countries['MKN'];c['flags']['MKN_desperate_defense_migration_v1']=-1
        w.war('GER')
        if used:
            w.run('MKN_begin_desperate_defense')
            for iid in ('MKN_hidden_workshops','MKN_evacuation_columns','MKN_black_vengeance_spirit'):w.apply([('add_ideas',iid,'=')])
        w.run('MKN_cleanup_desperate_defense')
        check(('MKN_hidden_workshops' in c['ideas'])==used,'MKN defense: stripped during ongoing war')
        w.war('GER',False)
        # Shared parameter reconstruction is tested above and by validate_horizons.
        w.effects['nww_mkn_rebuild_services']=[]
        w.run('MKN_cleanup_desperate_defense');w.run('MKN_cleanup_desperate_defense')
        check(not {'MKN_hidden_workshops','MKN_evacuation_columns','MKN_black_vengeance_spirit'} & c['ideas'],'MKN defense: wartime spirits survive peace')
        check(c.get('offsite',{}).get('arms_factory',0)==0,'MKN defense: concealed workshops survive peace')
        check(sum(e[1]=='mkn_gameplay.1' for e in w.events)==int(used),'MKN defense: missing/repeated/unearned celebration')
        cases+=1
    # Every possible real capitulation winner, including an unrelated invader.
    for loser,winner,capitulated in product(('MKN','UKR'),('MKN','UKR','SOV'),(False,True)):
        if loser==winner:continue
        w=GameplayWorld(root);w.root=loser;w.froms=(winner,winner,winner);w.countries[loser]['capitulated']=capitulated
        before=deepcopy(w.states);w.run('UKR_MKN_settle_actual_capitulation')
        should=capitulated and {winner,loser}=={'MKN','UKR'}
        check(w.countries[loser]['exists']!=should,'MKN–UKR settlement annexes an unrelated or undefeated country')
        for sid,s in w.states.items():
            if should and before[sid]['owner']==loser:check(s['owner']==winner and winner in s['cores'],'MKN–UKR victor lacks annexation/core '+sid)
            else:check(s==before[sid],'MKN–UKR settlement changes unrelated land '+sid)
        cases+=1
    # Timeline gates and actual-war-length policy, without destroying alliances.
    ukrfs={one(f,'id'):f for f in values(one(read(root/'common/national_focus/ukr_focus.txt'),'focus_tree'),'focus')}
    for date,question,compact in (('1938.12.31',False,False),('1939.1.1',True,False),('1939.5.31',True,False),('1939.6.1',True,True)):
        w=GameplayWorld(root);w.date=date
        check(w.test(one(ukrfs['UKR_the_makhno_question'],'available'),'UKR')==question,'UKR Makhno question has wrong date')
        check(w.test(one(ukrfs['UKR_border_compact'],'available'),'UKR')==compact,'UKR compact has wrong date')
        cases+=1
    for date,refused,allied in product(('1939.8.31','1939.9.1','1939.11.30','1939.12.1'),(False,True),(False,True)):
        w=GameplayWorld(root);w.date=date;c=w.countries['UKR'];c['ai']=True;c['focuses'].add('UKR_border_compact')
        if refused:c['flags']['UKR_MKN_border_settled_rejected']=-1
        if allied:w.faction('SOV','MKN','UKR')
        w.run('UKR_MKN_autumn_ultimatum_war','UKR')
        expected=refused and not allied and date in ('1939.9.1','1939.11.30')
        check(bool(w.declarations)==expected,'UKR autumn war: wrong date/refusal/alliance boundary')
        cases+=1
    for months in (0,11,12,24):
        w=GameplayWorld(root);w.faction('SOV','MKN');w.countries['UKR']['faction']='GER';w.war('UKR')
        for tag,target in (('MKN','UKR'),('UKR','MKN')):w.countries[tag]['war_months']={target:months}
        before={t:c['faction'] for t,c in w.countries.items()};w.run('UKR_MKN_begin_local_war_year','UKR')
        for tag in ('MKN','UKR'):check(w.test([('MKN_UKR_in_first_war_year','yes','=')],tag)==(months<12),'MKN–UKR restriction ignores real war age on reload')
        check(before=={t:c['faction'] for t,c in w.countries.items()},'MKN–UKR local war changes alliances')
        cases+=1
    # Existing agent contamination is removed in all countries, not just MKN.
    for tag in ('MKN','UKR','SOV'):
        w=GameplayWorld(root);token='agent';w.operatives[token]={'traits':{'mkn_batko_legend','mkn_eugen_under_fire','linguist'}};w.countries[tag]['operatives']=[token]
        w.run('MKN_cleanup_unique_operative_traits',tag)
        check(w.operatives[token]['traits']=={'linguist'},'MKN unique-trait cleanup removes legitimate spy traits or misses an agent')
        cases+=1
    for file,token in (('MKN_traits','mkn_batko_legend'),('MKN_eugen_traits','mkn_eugen_under_fire')):
        trait=one(one(read(root/f'common/unit_leader/{file}.txt'),'leader_traits'),token)
        check(one(trait,'type')=='land' and one(one(trait,'new_commander_weight'),'factor')=='0','MKN unique trait still belongs to random operative pool')
    check(one(read(root/'history/countries/MKN - Makhnovists.txt'),'set_convoys')=='60','MKN does not start with exactly 60 convoys')
    for sid in ('196','200','226','1082'):
        p=next(p for p in (root/'history/states').glob('*.txt') if one(one(read(p),'state'),'id')==sid)
        check(values(one(one(read(p),'state'),'history'),'add_core_of')==['MKN'],'MKN starting state retains a foreign core '+sid)
    project=one(one(read(root/'common/decisions/MKN_economic_decisions.txt'),'MKN_economic_projects_category'),'MKN_project_dnieper_waterways')
    check(not any(k=='type' and v=='naval_base' for k,v,o in walk(one(project,'remove_effect'))),'MKN inland Dnieper project still creates a naval base')
    operation=one(read(root/'common/operations/MKN_operations.txt'),'mkn_expropriate_funds_operation')
    aftermath=one(one(one(read(root/'common/ideas/MKN_gameplay_ideas.txt'),'ideas'),'country'),'MKN_bank_raid_aftermath')
    check(dict((k,float(v)) for k,v,o in one(aftermath,'modifier'))=={'consumer_goods_factor':0.20,'industrial_capacity_factory':-0.20,'political_power_gain':-0.30},'MKN bank victim penalty differs from agreed values')
    check(one(one(operation,'visible'),'MKN_valid_expropriation_target')=='yes' and not any(k=='while' for k,v,o in walk(read(root/'common/scripted_effects/MKN_international_effects.txt'))),'MKN bank operation remains visible on used targets or cleanup uses unsupported while')
    icons=json.loads((root/'docs/MKN_mio_icon_bounds.json').read_text());check(len(icons)==7,'MKN MIO icon set is incomplete')
    for a in icons:
        with Image.open(root/a['texture']) as im:
            b=im.getchannel('A').getbbox();check(im.size==(65,67) and b[0]>=6 and b[1]>=2 and b[2]<=59 and b[3]<=61,'MKN MIO artwork exceeds card bounds '+a['key'])
    for p in (*root.glob('common/**/MKN_gameplay*.txt'),*root.glob('common/**/MKN_party*.txt')):check(not list(engine_script_errors(read(p))),str(p)+': engine syntax error')
    for iid,node,o in one(one(read(root/'common/ideas/MKN_gameplay_ideas.txt'),'ideas'),'country'):localized(iid,iid);localized(iid+'_desc',iid)
    print(f'PASS: MKN campaign fixes: {cases} party/release/timed-spirit/peace/capitulation/1939/operative source-script scenarios, native bank cleanup, inland construction, 60 convoys and seven bounded MIO logos; no runtime claim')
