"""Idempotent MKN overhaul; country-local edits, retaining public script IDs."""
from pathlib import Path
from hoi4_script import read, one, values, dump, parse

ROOT = Path(__file__).resolve().parents[1]
def save(path, node):
    (ROOT/path).parent.mkdir(parents=True, exist_ok=True)
    (ROOT/path).write_text(dump(node)+'\n', encoding='utf-8', newline='\n')
def put(node, key, value):
    node[:] = [n for n in node if n[0] != key]
    node.append((key, value, '='))
def block(text):
    return parse(text)

def main():
    path = 'history/countries/MKN - Makhnovists.txt'
    doc = read(ROOT/path)
    put(doc, 'capital', '1082')
    save(path, doc)
    for path, buildings in [('history/states/1082-Huliaipole.txt', {'industrial_complex':'3','arms_factory':'2','infrastructure':'3'}), ('history/states/226-Nikopol.txt', {'arms_factory':'1'})]:
        doc = read(ROOT/path)
        state = one(doc, 'state')
        if '1082' in path:
            # Five factories must actually fit in the state's starting slots.
            put(state, 'state_category', 'town')
        for key, value in buildings.items():
            put(one(one(state, 'history'), 'buildings'), key, value)
        save(path, doc)
    for path in ['common/national_focus/MKN.txt', 'common/national_focus/MKN_frontier_focuses.txt', 'common/national_focus/ukr_focus.txt']:
        doc = read(ROOT/path)
        focuses = values(doc, 'shared_focus') + [f for t in values(doc, 'focus_tree') for f in values(t, 'focus')]
        for focus in focuses:
            put(focus, 'cost', str(max(10, int(one(focus, 'cost','10')))) if 'ukr_focus' in path else '5')
            if one(focus, 'id') == 'MKN_ukrainian_frontier_root':
                put(focus, 'available', block('always = no'))
        save(path, doc)
    path = 'common/decisions/MKN_ukr_border_decisions.txt'
    doc = read(ROOT/path)
    category = one(doc, 'MKN_ukr_border_category')
    decision = one(category, 'mkn_deescalate_pull_back')
    reward = block('''subtract_from_variable = { mkn_ukr_escalation_level = 1 }
        clamp_variable = { var = mkn_ukr_escalation_level min = 1 max = 5 }
        remove_ideas = MKN_border_fury_buff
        add_timed_idea = { idea = MKN_border_relaxation_debuff days = 90 }''')
    put(decision, 'days_remove', '20')
    put(decision, 'days_re_enable', '0')
    put(decision, 'complete_effect', [])
    put(decision, 'remove_effect', block('if = { limit = { NOT = { has_country_flag = mkn_ukr_frontier_concluded } } '+dump(reward)+' }'))
    for key, node, op in category:
        put(node, 'visible', block('NOT = { has_country_flag = mkn_ukr_frontier_concluded }'))
    if not one(category,'MKN_passive_escalation_drift'):
        category.extend(block('''MKN_passive_escalation_drift = {
            icon = frontier_ukr activation = { always = no }
            available = { always = no } selectable_mission = no
            visible = { has_country_flag = mkn_frontier_conflict_active NOT = { has_country_flag = mkn_ukr_frontier_concluded } }
            cancel_if_not_visible = yes days_mission_timeout = 30
            timeout_effect = { if = { limit = { NOT = { has_country_flag = mkn_ukr_frontier_concluded } }
                add_to_variable = { mkn_ukr_escalation_level = 1 }
                clamp_variable = { var = mkn_ukr_escalation_level min = 1 max = 5 }
                mkn_ukr_check_escalation = yes
                country_event = { id = mkn_ukr_border.11 days = 1 }
            } }
        }'''))
    save(path,doc)

    leaders_and_advisors()

def leaders_and_advisors():
    traits = {
        'mkn_iron_warlord': 'army_attack_factor = 0.15 war_support_factor = 0.15 stability_factor = -0.15',
        'mkn_idealist_philosopher': 'stability_factor = 0.25 political_power_gain = 0.30 war_support_factor = -0.10',
        'mkn_granary_overseer': 'local_building_slots_factor = 0.20 army_defence_factor = 0.20 trade_opinion_factor = -0.20',
        'mkn_paralyzed_committee': 'political_power_gain = -0.10',
        'mkn_syndicalist_organizer': 'industrial_capacity_factory = 0.10 army_org_factor = 0.10',
        'mkn_batko_advisor': 'army_org_factor = 0.25 org_loss_when_moving = -0.20 planning_speed = 0.20',
        'mkn_infantry_specialist': 'army_infantry_attack_factor = 0.10 army_infantry_defence_factor = 0.10',
        'mkn_tachanka_expert': 'army_speed_factor = 0.15 modifier_army_sub_unit_cavalry_attack_factor = 0.10 motorized_attack_factor = 0.10',
        'mkn_armored_train_commander': 'railway_gun_bombardment_factor = 0.20',
        'mkn_steppe_logistics_officer': 'supply_consumption_factor = -0.15',
        'mkn_entrenchment_specialist': 'dig_in_speed_factor = 0.15',
    }
    advisor_groups = {
        'fascism': [('weapons_broker','production_speed_arms_factory_factor = 0.10'),('recruiting_commissar','conscription = 0.02'),('military_orator','war_support_factor = 0.10'),('frontline_delegate','army_org_factor = 0.05'),('arsenal_coordinator','industrial_capacity_factory = 0.10'),('veterans_organizer','experience_gain_army_factor = 0.10')],
        'democratic': [('education_delegate','research_speed_factor = 0.05'),('commune_secretary','political_power_gain = 0.20'),('anti_statist_theorist','stability_factor = 0.10'),('cooperative_treasurer','consumer_goods_factor = -0.05'),('literacy_organizer','industry_research = 0.10'),('free_press_editor','democratic_drift = 0.05')],
        'neutrality': [('grain_distributor','supply_consumption_factor = -0.10'),('rural_defender','army_core_defence_factor = 0.10'),('militia_delegate','conscription = 0.02'),('agronomist','production_speed_infrastructure_factor = 0.10'),('village_mediator','stability_factor = 0.10'),('market_keeper','trade_opinion_factor = 0.10')],
        'communism': [('industrial_organizer','industrial_capacity_factory = 0.10'),('rail_dispatcher','production_speed_rail_way_factor = 0.15'),('union_secretary','political_power_gain = 0.20'),('workshop_engineer','production_factory_max_efficiency_factor = 0.05'),('labor_delegate','production_speed_buildings_factor = 0.10'),('syndicalist_theorist','communism_drift = 0.05')],
    }
    names = {
        'fascism': ['Semen Karetnyk','Petro Havrylenko','Mykhailo Kalashnykov','Oleksii Marchenko','Hryhorii Vasylivskyi','Ivan Liutyi'],
        'democratic': ['Vsevolod Volin','Petro Arshinov','Mark Mratchnyi','Aaron Baron','Olha Taratuta','Anatolii Horelik'],
        'neutrality': ['Fedot Kozubenko','Hanna Kravchenko','Stepan Tkachenko','Maria Hordiienko','Mykhailo Petrenko','Ivan Sytnyk'],
        'communism': ['Osyp Tsebriy','Danylo Bondarenko','Kateryna Melnyk','Mykola Savchenko','Olena Kovalenko','Andrii Romanenko'],
    }
    doc = read(ROOT/'common/characters/nww_MKN.txt')
    characters = one(doc,'characters')
    # Preserve original generals, chiefs and monarch portraits; replace only the
    # political-advisor roster with the requested six representatives per party.
    for name, char, op in characters:
        char[:] = [entry for entry in char if not(entry[0]=='advisor' and one(entry[1],'slot')=='political_advisor')]
    makhno = one(characters,'NWW_MKN_makhno')
    for role in values(makhno,'advisor'):
        put(role,'traits',block('mkn_batko_advisor'))
    fm = one(makhno,'field_marshal')
    for key,value in {'skill':'6','attack_skill':'6','defense_skill':'5','planning_skill':'5','logistics_skill':'5'}.items():
        put(fm,key,value)
    put(fm,'traits',block('trickster cavalry_officer skirmisher mkn_batko_legend'))
    # A distinct general role does not alter the preserved monarch role.
    put(makhno,'corps_commander',block('skill = 6 attack_skill = 6 defense_skill = 5 planning_skill = 5 logistics_skill = 5 traits = { trickster cavalry_officer skirmisher mkn_batko_legend }'))
    history_path='history/countries/MKN - Makhnovists.txt'
    history=read(ROOT/history_path)
    loc_en={}; loc_ru={}
    for ideology, entries in advisor_groups.items():
        for index,(token, modifiers) in enumerate(entries):
            tid='mkn_'+token
            traits[tid]=modifiers
            cid='MKN_advisor_'+token
            char=block(f'''name = {cid}
                portraits = {{ civilian = {{ small = GFX_idea_generic_political_advisor_europe_{1 + index%2} }} }}
                advisor = {{ slot = political_advisor idea_token = {cid} cost = 150
                    allowed = {{ original_tag = MKN }} available = {{ has_government = {ideology} }}
                    traits = {{ {tid} }}
                }}''')
            put(characters,cid,char)
            if cid not in values(history,'recruit_character'):
                history.extend(block(f'recruit_character = {cid}'))
            loc_en[cid]=names[ideology][index]
            loc_ru[cid]=names[ideology][index]
            loc_en[tid]=token.replace('_',' ').title()
            loc_ru[tid]=token.replace('_',' ').title()
    # Upgrade five existing staff members, keeping their established portraits.
    for cid,tid in [('NWW_MKN_andrii_dorosh','mkn_infantry_specialist'),('NWW_MKN_fedir_shchus','mkn_tachanka_expert'),('NWW_MKN_roman_danylenko','mkn_armored_train_commander'),('NWW_MKN_olena_hrytsenko','mkn_steppe_logistics_officer'),('NWW_MKN_oleksandr_hordiienko','mkn_entrenchment_specialist')]:
        char=one(characters,cid)
        staff=next((r for r in values(char,'advisor') if one(r,'slot')=='high_command'),None)
        if staff is None:
            staff=block(f'slot = high_command idea_token = {cid}_high_command cost = 150 allowed = {{ original_tag = MKN }} ledger = army')
            char.append(('advisor',staff,'='))
        put(staff,'traits',block(tid))
    save('common/characters/nww_MKN.txt',doc)
    save(history_path,history)
    save('common/country_leader/MKN_overhaul_traits.txt',block('leader_traits = { '+ ' '.join(f'{k} = {{ sprite = 15 random = no {v} }}' for k,v in traits.items())+' }'))
    save('common/unit_leader/MKN_traits.txt',block('''leader_traits = {
        mkn_batko_legend = { type = all trait_type = personality_trait gain_xp = { always = no }
            modifier = { army_speed_factor = 0.25 modifier_army_sub_unit_cavalry_attack_factor = 0.25 motorized_attack_factor = 0.25 breakthrough_factor = 0.20 }
        }
    }'''))
    path='common/scripted_effects/MKN_effects.txt'
    doc=read(ROOT/path)
    for ideology, trait in [('fascism','mkn_iron_warlord'),('democratic','mkn_idealist_philosopher'),('neutrality','mkn_granary_overseer'),('communism','mkn_paralyzed_committee')]:
        effect=one(doc,'MKN_install_'+ideology+'_successor')
        put(one(effect,'create_country_leader'),'traits',block(trait))
        if ideology=='communism' and not values(effect,'add_ideas'):
            effect.extend(block('add_ideas = MKN_revkom_terror'))
    put(doc,'MKN_install_tsebriy',block('''retire_ideology_leader = communism
        create_country_leader = { name = MKN_osyp_tsebriy picture = GFX_Portrait_MKN_osyp_tsebriy ideology = leninism traits = { mkn_syndicalist_organizer } }
        remove_ideas = MKN_revkom_terror'''))
    save(path,doc)
    path='common/national_focus/MKN.txt'
    doc=read(ROOT/path)
    focus=next(f for f in values(one(doc,'focus_tree'),'focus') if one(f,'id')=='MKN_purge_irreconcilables')
    if not values(one(focus,'completion_reward'),'MKN_install_tsebriy'):
        one(focus,'completion_reward').extend(block('MKN_install_tsebriy = yes'))
    save(path,doc)
    path='common/ideas/MKN_ideas.txt'
    doc=read(ROOT/path)
    put(one(one(doc,'ideas'),'country'),'MKN_revkom_terror',block('picture = MKN_revkom allowed = { original_tag = MKN } removal_cost = -1 modifier = { stability_factor = -0.35 consumer_goods_factor = 0.15 industrial_capacity_factory = -0.25 political_power_gain = -0.40 }'))
    save(path,doc)
    for folder in ('common/ideas','common/bop','common/national_focus'):
        for path in (ROOT/folder).glob('*MKN*.txt'):
            text=path.read_text(encoding='utf-8-sig')
            import re
            text=re.sub(r'recruitable_population_factor\s*=\s*[-\d.]+','conscription = 0.02',text)
            path.write_text(text,encoding='utf-8',newline='\n')
    loc_en.update({k:k.removeprefix('mkn_').replace('_',' ').title() for k in traits if k not in loc_en})
    loc_ru.update({k:k.removeprefix('mkn_').replace('_',' ').title() for k in traits if k not in loc_ru})
    loc_en.update({'mkn_batko_legend':'The Legend of Batko','MKN_osyp_tsebriy':'Osyp Tsebriy','MKN_revkom_terror':'Revkom Terror','MKN_passive_escalation_drift':'Mounting Frontier Tension'})
    loc_ru.update({'mkn_batko_legend':'Легенда о Батьке','MKN_osyp_tsebriy':'Осип Цебрий','MKN_revkom_terror':'Террор ревкома','MKN_passive_escalation_drift':'Нарастание напряжённости на границе'})
    for lang, loc in [('english',loc_en),('russian',loc_ru)]:
        p=ROOT/f'localisation/{lang}/MKN_overhaul_l_{lang}.yml'
        p.write_text('l_'+lang+':\n'+''.join(f' {k}:0 "{v}"\n' for k,v in loc.items()),encoding='utf-8-sig',newline='\n')
    path = 'events/MKN_ukr_border_events.txt'
    doc = read(ROOT/path)
    incident = next(e for e in values(doc,'country_event') if one(e,'id') == 'mkn_ukr_border.10')
    immediate = one(incident,'immediate')
    if not values(immediate,'complete_national_focus'):
        immediate.extend(block('complete_national_focus = MKN_ukrainian_frontier_root'))
    active = one(immediate,'if')
    if not values(active,'activate_mission').count('MKN_passive_escalation_drift'):
        active.extend(block('activate_mission = MKN_passive_escalation_drift'))
    if not any(one(e,'id') == 'mkn_ukr_border.11' for e in values(doc,'country_event')):
        doc.extend(block('''country_event = { id = mkn_ukr_border.11 hidden = yes is_triggered_only = yes
            trigger = { tag = MKN has_country_flag = mkn_frontier_conflict_active NOT = { has_country_flag = mkn_ukr_frontier_concluded } }
            immediate = { if = { limit = { NOT = { has_active_mission = MKN_passive_escalation_drift } } activate_mission = MKN_passive_escalation_drift } }
        }'''))
    save(path,doc)
    path = 'common/scripted_effects/MKN_ukr_border_effects.txt'
    doc = read(ROOT/path)
    initialize = one(doc,'mkn_ukr_initialize_frontier')
    for cond in values(initialize,'if'):
        if one(one(cond,'limit'),'has_completed_focus') == 'MKN_ukrainian_frontier_root':
            one(cond,'limit').extend(block('NOT = { has_country_flag = mkn_ukr_frontier_concluded }'))
    daily = one(doc,'mkn_ukr_frontier_daily')
    if not any(k == 'remove_mission' and v == 'MKN_passive_escalation_drift' for c in values(daily,'if') for k,v,o in c):
        daily.extend(block('''if = { limit = { has_country_flag = mkn_ukr_frontier_concluded }
            remove_mission = MKN_passive_escalation_drift clr_country_flag = mkn_ukr_frontier_unlocked
            clr_country_flag = mkn_frontier_conflict_active
        }'''))
    save(path,doc)

if __name__ == '__main__':
    main()
