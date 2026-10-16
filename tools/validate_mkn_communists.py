"""Execute Revkom branch gates, shared-spirit reconstruction and territorial foes.

Source-script scenarios cannot reproduce engine combat or UI rendering.
"""
from copy import deepcopy
from decimal import Decimal
from itertools import product
import hashlib
import json
import re
from PIL import Image
from hoi4_script import read, one, values, walk, tree_focuses, engine_script_errors
from validate_mkn_free_soviets import SovietWorld
from validate_mkn_military import MilitaryModel


FOCUSES = {
    'MKN_steppe_sovnarkhoz': (94,6,'MKN_embassy_to_kharkov'),
    'MKN_artel_state_farms': (94,7,'MKN_steppe_sovnarkhoz'),
    'MKN_dnieper_five_year_plan': (94,8,'MKN_artel_state_farms'),
    'MKN_political_commissars': (94,9,'MKN_dnieper_five_year_plan'),
    'MKN_red_armored_corps': (94,10,'MKN_political_commissars'),
    'MKN_equal_shield_of_socialism': (94,11,'MKN_the_fatal_plenum'),
    'MKN_industrial_ram_of_comintern': (94,12,'MKN_equal_shield_of_socialism'),
    'MKN_red_brotherhood_in_arms': (94,13,'MKN_industrial_ram_of_comintern'),
    'MKN_true_socialism_against_bureaucrats': (98,11,'MKN_the_fatal_plenum'),
    'MKN_liberation_of_soviet_ukraine': (98,12,'MKN_true_socialism_against_bureaucrats'),
    'MKN_strike_at_the_kremlin': (98,13,'MKN_liberation_of_soviet_ukraine'),
    'MKN_red_beacon_of_the_east': (96,14,None),
}


class RevkomWorld(SovietWorld):
    def __init__(self):
        super().__init__()
        self.countries['MKN'].update(government='communism',focuses={'MKN_the_fatal_plenum'})
        self.countries['SOV']['government']='communism'
        self.wargoals=[]
        self.countries['MKN']['flags']['MKN_communist_progression_v1']=-1

    def test(self, nodes, current='MKN', previous=None):
        for key,val,op in nodes or []:
            c=self.data(current)
            target=self.scope(val,current,previous) if isinstance(val,str) else None
            if key=='any_other_country':
                ok=any(tag!=current and s['exists'] and self.test(val,tag,current) for tag,s in self.countries.items())
            elif key=='hidden_trigger':ok=self.test(val,current,previous)
            elif key=='has_war_together_with':ok=bool(c['wars'] & self.countries[target]['wars'])
            elif key=='is_in_faction_with':ok=c['faction'] is not None and c['faction']==self.countries[target]['faction']
            else:ok=super().test([(key,val,op)],current,previous)
            if not ok:return False
        return True

    def apply(self, nodes, current='MKN', previous=None):
        matched=False
        for key,val,op in nodes or []:
            c=self.data(current)
            if key in {'if','else_if'}:
                if key=='if':matched=False
                if not matched and self.test(one(val,'limit'),current,previous):
                    self.apply([n for n in val if n[0]!='limit'],current,previous);matched=True
            elif key=='else':
                if not matched:self.apply(val,current,previous)
                matched=True
            elif key=='add_offsite_building':
                kind=one(val,'type');offsite=c.setdefault('offsite',{})
                offsite[kind]=offsite.get(kind,0)+int(one(val,'level'))
            elif key=='add_extra_state_shared_building_slots':c['slots']+=int(val)
            elif key=='create_wargoal':self.wargoals.append((current,one(val,'target'),one(val,'type')))
            elif key in {'add_tech_bonus','add_doctrine_cost_reduction'}:
                c.setdefault('coupons',[]).append((key,deepcopy(val)))
            else:super().apply([(key,val,op)],current,previous)

    def war(self, foe, active=True):
        for a,b in (('MKN',foe),(foe,'MKN')):
            (self.countries[a]['wars'].add if active else self.countries[a]['wars'].discard)(b)


def validate_territorial_penalties(root, check):
    cases=0
    configs=(
        ('communism','MKN_true_socialism_against_bureaucrats',None,'MKN_sync_revkom_combat',
         'MKN_revkom_enemy_disorganization','common/dynamic_modifiers/MKN_communist_modifiers.txt',False),
        ('democratic','MKN_subversion_of_enemy_ranks','MKN_enemy_subversion_idea','MKN_sync_people_defense',
         'MKN_people_defense_subversion','common/dynamic_modifiers/MKN_soviet_modifiers.txt',True),
    )
    for gov,focus,idea,sync,modifier,path,needs_core in configs:
        definition=one(read(root/path),modifier)
        check(not any(k=='SOV' for k,v,o in walk(one(definition,'enable'))),modifier+': fixed Soviet restriction remains')
        # Three simultaneous enemies, plus an allied country and a neutral one.
        w=RevkomWorld();c=w.countries['MKN'];c['government']=gov;c['focuses'].add(focus)
        if idea:c['ideas'].add(idea)
        c['faction']=w.countries['LTB']['faction']='MKN'
        for foe in ('SOV','GER','UKR'):w.war(foe)
        w.states['9000'].update(owner='MKN',controller='MKN',cores={'MKN'})
        w.run(sync);w.run(sync)
        for sid,s in w.states.items():
            expected=s['owner']==s['controller']=='MKN' and (not needs_core or 'MKN' in s['cores'])
            targets={country for (token,country),expiry in s.get('dynamic',{}).items() if token==modifier and expiry>w.day}
            check(targets==({'SOV','GER','UKR'} if expected else set()),modifier+': wrong targets/territory '+sid)
            cases+=1
        # Peace with the USSR must preserve penalties against other enemies.
        w.war('SOV',False);w.run(sync)
        pairs=w.states['9000']['dynamic']
        check((modifier,'SOV') not in pairs and all((modifier,t) in pairs for t in ('GER','UKR')),modifier+': Soviet peace clears other enemies or leaves a stale penalty')
        cases+=1
        # Another opponent enters the war later, without relying on a country list.
        w.war('AUS');w.run(sync)
        check((modifier,'AUS') in w.states['9000']['dynamic'],modifier+': newly hostile country is omitted')
        cases+=1
        w.war('GER',False);w.countries['GER']['faction']='MKN';w.run(sync)
        check((modifier,'GER') not in w.states['9000']['dynamic'],modifier+': former enemy/ally retains penalty')
        cases+=1
        for owned,controlled,core,government in product((False,True),(False,True),(False,True),(gov,'fascism')):
            w.states['9000'].update(owner='MKN' if owned else 'GER',controller='MKN' if controlled else 'GER',cores={'MKN'} if core else set())
            c['government']=government
            check(w.test(one(definition,'enable'),'9000')==(owned and controlled and (core or not needs_core) and government==gov),modifier+': territorial enable escapes ownership/control/government')
            cases+=1
        w.states['9000'].update(owner='MKN',controller='MKN',cores={'MKN'});c['government']=gov
        w.run(sync);w.states['9000']['owner']='GER';w.day+=2
        check(not w.test([('has_dynamic_modifier',[('modifier',modifier,'='),('scope','AUS','=')],'=')],'9000'),modifier+': lost-state penalty has no expiry')
        cases+=1
        for foe in tuple(c['wars']):w.war(foe,False)
        w.run(sync)
        check(not any(k[0]==modifier and expiry>w.day for s in w.states.values() if s['owner']=='MKN' for k,expiry in s.get('dynamic',{}).items()),modifier+': penalty survives peace')
        cases+=1
    # These are native enemy-relative fields, not a restriction to any named foe.
    traps=one(read(root/'common/dynamic_modifiers/MKN_agrarian_modifiers.txt'),'MKN_agrarian_trapped_roads')
    check(one(traps,'enemy_army_speed_factor')=='-0.30','MKN traps: wrong native enemy-speed penalty')
    check(not any(k in {'SOV','GER','UKR'} for k,v,o in walk(traps)),'MKN traps: fixed target country')
    for file,iid,amount in (
        ('MKN_agrarian_ideas','MKN_empty_field_idea','0.35'),
        ('MKN_soviet_ideas','MKN_enemy_subversion_idea','0.40'),
    ):
        idea=one(one(one(read(root/f'common/ideas/{file}.txt'),'ideas'),'country'),iid)
        check(one(one(idea,'modifier'),'enemy_attrition')==amount and not values(idea,'targeted_modifier'),iid+': enemy attrition is narrowed to a fixed country')
    print(f'PASS: MKN territorial penalties: {cases} source-script scenarios; multiple enemies, non-Soviet war, allies/neutrals, peace, ownership/control and expiry')


def validate_communists(root, game, check, localized):
    fs={one(f,'id'):f for f in tree_focuses(one(read(root/'common/national_focus/MKN.txt'),'focus_tree'),root/'common/national_focus')}
    for fid,(x,y,parent) in FOCUSES.items():
        f=fs[fid]
        check((one(f,'x'),one(f,'y'),one(f,'cost'))==(str(x),str(y),'5'),fid+': incorrect coordinates/duration')
        check(one(one(f,'available'),'has_government')=='communism',fid+': missing communism gate')
        if parent:check(values(one(f,'prerequisite'),'focus')==[parent],fid+': wrong prerequisite')
        localized(fid,fid);localized(fid+'_desc',fid)
    check(set(values(one(fs['MKN_red_beacon_of_the_east'],'prerequisite'),'focus'))=={'MKN_red_brotherhood_in_arms','MKN_strike_at_the_kremlin'},'MKN beacon: finale is not reachable from either route')
    for fid,parent in (('MKN_political_commissars','MKN_red_military_specialists'),('MKN_red_armored_corps','MKN_tractors_for_grain')):
        check(one(one(fs[fid],'available'),'has_completed_focus')==parent,fid+': cross-branch gate lost')
    native=set(re.findall(r'^## (\w+)',(game/'documentation/modifiers_documentation.md').read_text(),re.M))
    native.update('production_speed_'+k+'_factor' for k,v,o in one(read(game/'common/buildings/00_buildings.txt'),'buildings'))
    categories=set(v for k,v,o in one(read(game/'common/technology_tags/00_technology.txt'),'technology_categories') if k is None)
    ideas=one(one(read(root/'common/ideas/MKN_communist_ideas.txt'),'ideas'),'country')
    for iid,node,o in ideas:
        localized(iid,iid);localized(iid+'_desc',iid)
        for key,val,op in one(node,'modifier',[]):check(key in native,iid+': unknown modifier '+str(key))
        for key,val,op in one(node,'research_bonus',[]):check(key in categories,iid+': undefined research category '+str(key))
        for targeted in values(node,'targeted_modifier'):
            check(all(k=='tag' or k in native for k,v,o in targeted),iid+': invalid targeted modifier')
    for path in root.glob('common/**/MKN_communist*.txt'):
        check(not list(engine_script_errors(read(path))),str(path)+': invalid engine syntax')
    beacon=one(ideas,'MKN_red_beacon_idea')
    check(not one(one(beacon,'modifier'),'research_speed_factor') and dict((k,v) for k,v,o in one(beacon,'research_bonus'))=={'industry':'0.20','electronics':'0.20'},'MKN beacon: research bonus leaks outside industry/electronics')
    cases=0
    for equal,betrayed,protected,plenum,gov in product((False,True),(False,True),(False,True),(False,True),('communism','democratic')):
        w=RevkomWorld();c=w.countries['MKN'];c['government']=gov
        if not plenum:c['focuses'].clear()
        for flag,present in (('MKN_equal_autonomy',equal),('MKN_soviet_betrayal',betrayed)):
            if present:c['flags'][flag]=-1
        if protected:w.countries['SOV']['flags']['NWW_SOV_MKN_settlement']=-1
        w.run('MKN_repair_communist_progression')
        a=w.test(one(fs['MKN_equal_shield_of_socialism'],'available'))
        b=w.test(one(fs['MKN_true_socialism_against_bureaucrats'],'available'))
        check(a==(gov=='communism' and plenum and equal),'MKN plenum: equal autonomy route is lost')
        check(b==(gov=='communism' and plenum and betrayed and not equal and not protected),'MKN plenum: betrayal bypasses an accepted charter')
        check(not(a and b),'MKN plenum: both routes open')
        cases+=1
    for allied,war,exists,gov in product((False,True),(False,True),(False,True),('communism','democratic')):
        w=RevkomWorld();c=w.countries['MKN'];c['focuses'].add('MKN_equal_shield_of_socialism');c['flags']['MKN_equal_autonomy']=-1
        if allied:w.faction('SOV','MKN')
        if war:w.war('SOV')
        w.countries['SOV'].update(exists=exists,government=gov)
        for tag,idea in (('MKN','MKN_equal_shield_trade_idea'),('SOV','MKN_equal_shield_partner_idea')):w.countries[tag]['ideas'].add(idea)
        w.run('MKN_sync_revkom_trade');w.run('MKN_sync_revkom_trade')
        check(all((iid in w.countries[tag]['ideas'])==(allied and not war and exists and gov=='communism') for tag,iid in (('MKN','MKN_equal_shield_trade_idea'),('SOV','MKN_equal_shield_partner_idea'))),'MKN pact: trade survives loss of eligibility or is one-sided')
        cases+=1
    for allied,joint,own_war in product((False,True),repeat=3):
        w=RevkomWorld();c=w.countries['MKN'];c['focuses'].add('MKN_red_brotherhood_in_arms');c['flags']['MKN_equal_autonomy']=-1
        if allied:w.faction('SOV','MKN')
        if own_war:w.war('GER')
        if joint:w.countries['SOV']['wars'].add('GER')
        w.run('MKN_sync_revkom_combat');w.run('MKN_sync_revkom_combat')
        check(('MKN_red_brotherhood_idea' in c['ideas'])==(allied and joint and own_war),'MKN brotherhood: peacetime or separate wars grant attack')
        cases+=1
    plan=one(fs['MKN_dnieper_five_year_plan'],'completion_reward')
    for owned,controlled in product((False,True),repeat=2):
        w=RevkomWorld();s=w.states['226'];s.update(owner='MKN' if owned else 'GER',controller='MKN' if controlled else 'GER')
        before=deepcopy(s['buildings']);slots=s['slots'];w.apply(plan);w.apply(plan)
        gains={k:s['buildings'][k]-before.get(k,0) for k in ('industrial_complex','arms_factory')}
        check(gains==dict(industrial_complex=4 if owned and controlled else 0,arms_factory=4 if owned and controlled else 0) and s['slots']-slots==(8 if owned and controlled else 0),'MKN Nikopol: repeated/foreign construction or insufficient guaranteed slots')
        cases+=1
    w=RevkomWorld();reward=one(fs['MKN_equal_shield_of_socialism'],'completion_reward');w.apply(reward);w.apply(reward)
    check(w.countries['MKN']['offsite']=={'industrial_complex':6},'MKN shield: off-map reward repeated or not doubled');cases+=1
    w=RevkomWorld();before={k:(s['owner'],s['controller'],set(s['cores'])) for k,s in w.states.items()}
    w.apply(one(fs['MKN_liberation_of_soviet_ukraine'],'completion_reward'))
    expected={'192','197','202','225','259'}
    for sid,s in w.states.items():
        check((s['owner'],s['controller'])==before[sid][:2] and s['cores']==before[sid][2]|({'MKN'} if sid in expected else set()),'MKN liberation: steals territory or cores an unintended state')
    check(w.countries['MKN']['war_support']==0.90,'MKN liberation: war support not doubled');cases+=1
    for war,ally,equal,protected,exists in product((False,True),repeat=5):
        w=RevkomWorld();c=w.countries['MKN'];c['flags']['MKN_soviet_betrayal']=-1
        if war:w.war('SOV')
        if ally:w.faction('SOV','MKN')
        if equal:c['flags']['MKN_equal_autonomy']=-1
        if protected:w.countries['SOV']['flags']['NWW_SOV_MKN_settlement']=-1
        w.countries['SOV']['exists']=exists
        w.apply(one(fs['MKN_strike_at_the_kremlin'],'completion_reward'))
        check(bool(w.wargoals)==(exists and not(war or ally or equal or protected)),'MKN Kremlin: war goal targets an ally/protected settlement or duplicates a war')
        check(not w.declarations,'MKN Kremlin: focus declares war instead of granting a goal');cases+=1
    effects={k:v for name in ('nww_mkn_progression','MKN_horizons_effects','MKN_militarist_effects','MKN_soviet_effects','MKN_communist_effects') for k,v,o in read(root/f'common/scripted_effects/{name}.txt')}
    def rebuild(done):
        model=MilitaryModel(effects,done);model.apply(effects['nww_mkn_rebuild_industry']);model.rebuild();return model
    baseline=rebuild(set())
    for plan,armour,defense,strike in product((False,True),repeat=4):
        done={fid for fid,active in zip(('MKN_dnieper_five_year_plan','MKN_red_armored_corps','MKN_true_socialism_against_bureaucrats','MKN_strike_at_the_kremlin'),(plan,armour,defense,strike)) if active}
        m=rebuild(done)
        for var,delta in (
            ('MKN_unified_industrial_capacity_factory',Decimal('0.20')*plan),('MKN_unified_consumer_goods_factor',Decimal('0.15')*plan),
            ('MKN_army_army_armor_attack_factor',Decimal('0.20')*armour),('MKN_army_army_armor_speed_factor',Decimal('0.20')*armour),
            ('MKN_army_army_core_defence_factor',Decimal('0.40')*defense),('MKN_army_army_speed_factor',Decimal('0.30')*strike)):
            check(m.variables[var]-baseline.variables[var]==delta,'MKN communist save replay: lost/scaled modifier '+var)
        before=(dict(m.variables),deepcopy(m.oneoffs));m.apply(effects['nww_mkn_rebuild_industry']);m.rebuild()
        check(before==(dict(m.variables),m.oneoffs),'MKN communist save replay: stacking or repeated physical rewards');cases+=1
    art=json.loads((root/'docs/art/mkn_communist_expansion/assets.json').read_text())
    sprites={one(s,'name'):s for s in values(one(read(root/art['sprite_file']),'spriteTypes'),'spriteType')}
    check(len(art['assets'])==12 and len(sprites)==24,'MKN Revkom artwork: incomplete set')
    hashes=set()
    for a in art['assets']:
        h=hashlib.sha256((root/a['source']).read_bytes()).hexdigest();hashes.add(h)
        check(h==a['source_sha256'] and (root/a['prompt']).is_file(),a['focus']+': missing imagegen source/prompt')
        check(hashlib.sha256((root/a['texture']).read_bytes()).hexdigest()==a['texture_sha256'],a['focus']+': unexpected DDS modification')
        check(one(fs[a['focus']],'icon')==a['sprite'],a['focus']+': artwork not connected')
        for token in (a['sprite'],a['sprite']+'_shine'):
            check(one(sprites[token],'texturefile')==a['texture'],a['focus']+': incorrect sprite')
        for animation in values(sprites[a['sprite']+'_shine'],'animation'):
            check(one(animation,'animationmaskfile')==a['texture'],a['focus']+': incorrect highlight mask')
        with Image.open(root/a['texture']) as im:
            check(im.size==(96,96) and im.mode=='RGBA',a['focus']+': invalid texture canvas')
            b=im.getchannel('A').getbbox()
            check(list(b)==a['occupied_alpha_bounds'] and b[0]>=6 and b[1]>=6 and b[2]<=90 and b[3]<=90,a['focus']+': insufficient alpha clearance')
    check(len(hashes)==12,'MKN Revkom artwork: duplicate source')
    validate_territorial_penalties(root,check)
    print(f'PASS: MKN communists: 12 focuses, 12 imagegen icons, x2 modifiers/x3 consumer goods, {cases} source-script route/trade/war/reconstruction scenarios; no runtime claim')
