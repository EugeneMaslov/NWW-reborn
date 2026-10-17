"""Build the NWW German service programmes and two alternative industrial policies.

References: installed common/national_focus/germany.txt (Gotterdammerung),
GER_panzer_troops_school, GER_establish_carrier_groups, GER_the_four_year_plan
and GER_prioritize_economic_growth. No native conquest economy is activated.
"""
import json
from pathlib import Path
from hoi4_script import read, one, values, parse, dump, quoted

ROOT = Path(__file__).resolve().parents[1]
PREFIX = 'GER_nww_'


def write(path, text):
    (ROOT / path).write_text(text.rstrip() + '\n', encoding='utf-8-sig' if path.endswith('.yml') else 'utf-8', newline='\n')


def put(node, key, value):
    node[:] = [e for e in node if e[0] != key]
    node.append((key, value, '='))


def tech(category):
    return f'add_tech_bonus = {{ name = GER_nww_service_research category = {category} bonus = 0.5 uses = 1 }}'


def doctrine(service):
    return f'add_doctrine_cost_reduction = {{ name = GER_nww_{service}_doctrine category = {service}_doctrine cost_reduction = 0.5 uses = 1 }}'


def main():
    doc = read(ROOT / 'common/national_focus/GER_focuses.txt')
    tree = one(doc, 'focus_tree')
    fs = {one(f, 'id'): f for f in values(tree, 'focus')}
    # Keep diplomacy beside the political tree; service branches have their own roots.
    put(fs['GER_prussian_traditions'], 'x', '72')
    put(fs['GER_prussian_traditions'], 'y', '0')
    fs['GER_prussian_traditions'][:] = [e for e in fs['GER_prussian_traditions'] if e[0] != 'prerequisite']
    put(fs['GER_the_fleet_question'], 'x', '100')
    put(fs['GER_the_eastern_question'], 'x', '45')
    put(fs['GER_the_eastern_question'], 'prerequisite', parse('focus = GER_guardians_of_the_reich'))
    available = one(fs['GER_the_eastern_question'], 'available', [])
    if not any(k == 'has_completed_focus' and v == 'GER_prussian_traditions' for k, v, _ in available):
        available.append(('has_completed_focus', 'GER_prussian_traditions', '='))
    put(fs['GER_the_eastern_question'], 'available', available)
    specs = []

    def add(slug, ru, en, x, y, parent, reward='', spirit=None, icon='GFX_goal_generic_army_doctrines', cost=10, exclusive=None, available=''):
        specs.append(dict(id=PREFIX + slug, ru=ru, en=en, x=x, y=y,
                          parent=parent, reward=reward, spirit=spirit or {}, icon=icon,
                          cost=cost, exclusive=exclusive, available=available))

    # Army: common staff and logistics, two mutually exclusive operational schools,
    # parallel equipment/armoured programmes and a common capstone.
    add('general_staff', 'Обновить Большой генеральный штаб', 'Renew the Great General Staff', 72, 1, 'GER_prussian_traditions', 'army_experience = 25', {'army': {'org': 0.05}}, cost=5)
    add('staff_college', 'Штабные академии земель', 'State Staff Colleges', 72, 2, PREFIX+'general_staff', doctrine('land'), {'army': {'planning': 0.10}})
    add('mission_command', 'Самостоятельность командиров', 'Mission Command', 70, 3, PREFIX+'staff_college', 'army_experience = 20', {'army': {'training': -0.10}}, exclusive=PREFIX+'deliberate_battle')
    add('deliberate_battle', 'Методическая подготовка сражения', 'Deliberate Battle', 74, 3, PREFIX+'staff_college', 'army_experience = 20', {'army': {'org': 0.05}}, exclusive=PREFIX+'mission_command')
    add('army_signals', 'Связь общевойсковых соединений', 'Combined Arms Signals', 72, 4, [PREFIX+'mission_command', PREFIX+'deliberate_battle'], tech('electronics'))
    add('infantry_standardisation', 'Единое пехотное вооружение', 'Standard Infantry Armaments', 68, 2, PREFIX+'general_staff', tech('infantry_weapons'), icon='GFX_goal_generic_small_arms')
    add('artillery_directorate', 'Управление полевой артиллерии', 'Field Artillery Directorate', 68, 3, PREFIX+'infantry_standardisation', tech('artillery'), {'army': {'artillery': 0.05}})
    add('combat_engineers', 'Штурмовые сапёры', 'Assault Engineers', 68, 4, PREFIX+'artillery_directorate', tech('support_tech'))
    add('motor_transport', 'Автомобильные колонны', 'Motor Transport Columns', 76, 2, PREFIX+'general_staff', tech('motorized_equipment'))
    add('armour_school', 'Школа бронетанковых войск', 'Armoured Troops School', 76, 3, PREFIX+'motor_transport', doctrine('land'), icon='GFX_goal_generic_army_tanks')
    add('medium_tank_programme', 'Средний танк для имперской армии', 'Imperial Medium Tank Programme', 76, 4, PREFIX+'armour_school', tech('cat_medium_armor'), icon='GFX_goal_generic_army_tanks')
    add('panzergrenadiers', 'Моторизованная пехота сопровождения', 'Panzergrenadiers', 76, 5, PREFIX+'medium_tank_programme', tech('cat_mechanized_equipment'), {'army': {'armour': 0.05}})
    add('army_rail_logistics', 'Железнодорожная служба армии', 'Army Railway Service', 72, 5, PREFIX+'army_signals', 'army_experience = 20', {'army': {'supply': -0.10}})
    add('field_hospitals', 'Военно-медицинская служба', 'Military Medical Service', 68, 5, PREFIX+'combat_engineers', tech('support_tech'))
    add('combined_arms_exercises', 'Большие общевойсковые манёвры', 'Grand Combined Arms Exercises', 72, 6, [PREFIX+'army_rail_logistics', PREFIX+'panzergrenadiers', PREFIX+'field_hospitals'], doctrine('land'), available=f'has_completed_focus = {PREFIX}army_rail_logistics has_completed_focus = {PREFIX}panzergrenadiers has_completed_focus = {PREFIX}field_hospitals')
    add('imperial_army_readiness', 'Готовность имперской армии', 'Imperial Army Readiness', 72, 7, PREFIX+'combined_arms_exercises', 'army_experience = 35', {'army': {'experience': 0.10}})

    add('imperial_air_service', 'Имперская воздушная служба', 'Imperial Air Service', 86, 0, None, 'air_experience = 25', {'air': {'accidents': -0.05}}, icon='GFX_goal_generic_build_airforce', cost=5)
    add('air_academies', 'Авиационные академии', 'Air Academies', 86, 1, PREFIX+'imperial_air_service', doctrine('air'), {'air': {'accidents': -0.05}})
    add('fighter_design', 'Современный истребитель', 'Modern Fighter Design', 82, 2, PREFIX+'air_academies', tech('light_air'), icon='GFX_goal_generic_air_fighter')
    add('interceptor_control', 'Сеть управления перехватом', 'Interceptor Control Network', 82, 3, PREFIX+'fighter_design', tech('radar_tech'), {'air': {'superiority': 0.05}})
    add('night_fighters', 'Эскадрильи ночных истребителей', 'Night Fighter Squadrons', 82, 4, PREFIX+'interceptor_control', tech('light_air'))
    add('battlefield_aviation', 'Авиация поля боя', 'Battlefield Aviation', 86, 2, PREFIX+'air_academies', tech('cas_bomber'), {'air': {'cas': 0.05}})
    add('forward_air_controllers', 'Передовые авианаводчики', 'Forward Air Controllers', 86, 3, PREFIX+'battlefield_aviation', doctrine('air'))
    add('long_range_bombers', 'Дальняя бомбардировочная авиация', 'Long Range Bomber Command', 90, 2, PREFIX+'air_academies', tech('heavy_air'))
    add('air_navigation', 'Радионавигация и метеослужба', 'Air Navigation and Weather Service', 90, 3, PREFIX+'long_range_bombers', tech('electronics'), {'air': {'range': 0.05}})
    add('air_transport', 'Транспортная авиация', 'Air Transport Service', 90, 4, PREFIX+'air_navigation', tech('air_equipment'))
    add('integrated_air_operations', 'Единое управление воздушной войной', 'Integrated Air Operations', 86, 5, [PREFIX+'night_fighters', PREFIX+'forward_air_controllers', PREFIX+'air_transport'], doctrine('air'), {'air': {'mission': 0.05}}, available=f'has_completed_focus = {PREFIX}night_fighters has_completed_focus = {PREFIX}forward_air_controllers has_completed_focus = {PREFIX}air_transport')
    add('aeronautical_institutes', 'Имперские институты аэродинамики', 'Imperial Aeronautical Institutes', 86, 6, PREFIX+'integrated_air_operations', tech('air_equipment')+' air_experience = 35')

    add('admiralty_staff', 'Объединённый штаб адмиралтейства', 'Unified Admiralty Staff', 100, 1, 'GER_the_fleet_question', 'navy_experience = 25', {'navy': {'coordination': 0.05}}, icon='GFX_goal_generic_navy_carrier', cost=5)
    add('imperial_shipyards', 'Верфи Киля и Вильгельмсхафена', 'Kiel and Wilhelmshaven Shipyards', 100, 2, PREFIX+'admiralty_staff', 'GER_nww_build_service_dockyard = yes', {'navy': {'output': 0.05}})
    add('battlefleet_modernisation', 'Модернизация линейного флота', 'Battlefleet Modernisation', 96, 3, PREFIX+'imperial_shipyards', tech('bb_tech'), icon='GFX_goal_generic_navy_battleship')
    add('capital_ship_fire_control', 'Управление огнём тяжёлых кораблей', 'Capital Ship Fire Control', 96, 4, PREFIX+'battlefleet_modernisation', tech('naval_equipment'))
    add('fleet_air_arm', 'Морская авиационная служба', 'Fleet Air Arm', 100, 3, PREFIX+'imperial_shipyards', tech('naval_air'), icon='GFX_goal_generic_air_naval_bomber')
    add('fleet_carriers', 'Программа эскадренных авианосцев', 'Fleet Carrier Programme', 100, 4, PREFIX+'fleet_air_arm', tech('mio_cat_tech_all_carrier_and_modules'), icon='GFX_goal_generic_navy_carrier')
    add('carrier_groups', 'Авианосные ударные соединения', 'Carrier Task Groups', 100, 5, PREFIX+'fleet_carriers', doctrine('naval'), {'navy': {'sortie': 0.10}})
    add('screening_squadrons', 'Эскадры охранения', 'Screening Squadrons', 104, 3, PREFIX+'imperial_shipyards', tech('dd_tech'), {'navy': {'screens': 0.05}})
    add('convoy_escorts', 'Противолодочное сопровождение', 'Anti Submarine Escorts', 104, 4, PREFIX+'screening_squadrons', tech('naval_equipment'))
    add('submarine_patrols', 'Подводные патрули океана', 'Ocean Submarine Patrols', 108, 3, PREFIX+'imperial_shipyards', tech('ss_tech'), icon='GFX_goal_generic_navy_submarine')
    add('ocean_replenishment', 'Океанское снабжение', 'Ocean Replenishment', 108, 4, PREFIX+'submarine_patrols', 'navy_experience = 20', {'navy': {'range': 0.10}})
    add('fleet_repair_bases', 'Базы ремонта и докования', 'Fleet Repair Bases', 104, 5, PREFIX+'convoy_escorts', 'GER_nww_build_service_dockyard = yes', {'navy': {'repair': 0.10}})
    add('joint_naval_exercises', 'Совместные манёвры флота и авиации', 'Joint Fleet and Air Exercises', 100, 6, [PREFIX+'carrier_groups', PREFIX+'capital_ship_fire_control', PREFIX+'fleet_repair_bases'], doctrine('naval'), available=f'has_completed_focus = {PREFIX}carrier_groups has_completed_focus = {PREFIX}capital_ship_fire_control has_completed_focus = {PREFIX}fleet_repair_bases')
    add('high_seas_readiness', 'Боеготовность Флота открытого моря', 'High Seas Fleet Readiness', 100, 7, PREFIX+'joint_naval_exercises', 'navy_experience = 35', {'navy': {'output': 0.05}})

    # Two alternative policies supplement the common energy/technical/trade trunk.
    # Distant policy unlocks use availability gates to avoid connectors through it.
    policies = [
        ('civil_investment', 'Долгосрочные гражданские инвестиции', 'Long Term Civil Investment', 'GER_nww_build_civilian = yes', {'construction': 0.05}),
        ('regional_enterprises', 'Предприятия имперских земель', 'Regional Enterprises', 'GER_nww_build_civilian = yes', {}),
        ('export_machinery', 'Экспорт станков и машин', 'Machinery Exports', tech('industry'), {'research': 0.05}),
        ('consumer_markets', 'Общий потребительский рынок', 'Common Consumer Market', 'add_stability = 0.05', {}),
        ('civil_energy_reserve', 'Резерв гражданской энергетики', 'Civil Energy Reserve', 'GER_nww_build_energy_infrastructure = yes', {'energy': 0.10}),
        ('investment_dividend', 'Дивиденды мирного развития', 'Dividend of Peaceful Development', 'GER_nww_build_civilian = yes', {'construction': 0.05}),
        ('defence_procurement', 'Четырёхлетняя оборонная программа', 'Four Year Defence Programme', 'GER_nww_build_military = yes', {'output': 0.05}),
        ('arsenal_dispersal', 'Рассредоточение арсеналов', 'Disperse the Arsenals', 'GER_nww_build_military = yes', {}),
        ('strategic_reserves', 'Стратегические производственные резервы', 'Strategic Production Reserves', tech('industry'), {'maximum': 0.05}),
        ('defence_standardisation', 'Единые оборонные контракты', 'Standard Defence Contracts', tech('infantry_weapons'), {'efficiency': 0.05}),
        ('defence_energy_reserve', 'Энергетика оборонных производств', 'Defence Energy Reserve', 'GER_nww_build_energy_infrastructure = yes', {'energy': 0.10}),
        ('procurement_continuity', 'Непрерывность оборонных заказов', 'Continuity of Defence Orders', 'GER_nww_build_military = yes', {'output': 0.05}),
    ]
    industrial = {}
    for i, (slug, ru, en, reward, bonuses) in enumerate(policies):
        branch, row = divmod(i, 6)
        previous = None if row == 0 else PREFIX + policies[i-1][0]
        other = PREFIX + ('defence_procurement' if branch == 0 else 'civil_investment') if row == 0 else None
        industrial[PREFIX+slug] = bonuses
        add(slug, ru, en, 61+4*branch, row+2, previous, reward,
            icon='GFX_goal_generic_construct_civ_factory' if branch == 0 else 'GFX_goal_generic_construct_mil_factory',
            exclusive=other, available='has_completed_focus = GER_krupp_and_thyssen' if row == 0 else '')

    mods = {
        'army': {'org': 'army_org_factor', 'planning': 'planning_speed', 'training': 'training_time_army_factor', 'artillery': 'army_artillery_attack_factor', 'armour': 'army_armor_attack_factor', 'supply': 'supply_consumption_factor', 'experience': 'experience_gain_army_factor'},
        'air': {'accidents': 'air_accidents_factor', 'superiority': 'air_superiority_efficiency', 'cas': 'air_cas_efficiency', 'range': 'air_range_factor', 'mission': 'air_mission_efficiency'},
        'navy': {'coordination': 'naval_coordination', 'output': 'industrial_capacity_dockyard', 'sortie': 'sortie_efficiency', 'screens': 'navy_screen_attack_factor', 'range': 'navy_max_range_factor', 'repair': 'repair_speed_factor'},
    }
    loc = {'russian': {}, 'english': {}}
    meta = json.loads((ROOT/'docs/GER_industry_rework.json').read_text(encoding='utf-8'))
    for s in specs:
        reward = s['reward']
        for service, bonuses in s['spirit'].items():
            for key, value in bonuses.items():
                reward += f' add_to_variable = {{ GER_service_{service}_{key} = {value} tooltip = GER_service_{service}_{key}_tt }}'
        if s['id'] in industrial:
            for key, value in industrial[s['id']].items():
                reward += f' add_to_variable = {{ GER_industry_{key} = {value} tooltip = GER_nww_industry_{key}_tt }}'
            meta['persistent_bonuses'][s['id']] = industrial[s['id']]
            if s['id'] not in meta['focuses']: meta['focuses'].append(s['id'])
        reward += ' hidden_effect = { GER_nww_refresh_services = yes GER_nww_refresh_industry = yes }'
        node = parse(f'id = {s["id"]} icon = {s["icon"]} x = {s["x"]} y = {s["y"]} cost = {s["cost"]} available_if_capitulated = no ai_will_do = {{ factor = 2 }}')
        if s['parent']:
            # A single prerequisite block means OR for alternative schools;
            # common capstones explicitly require every service programme above.
            parents = s['parent'] if isinstance(s['parent'], list) else [s['parent']]
            node += parse('prerequisite = { '+ ' '.join('focus = '+p for p in parents) +' }')
        if s['exclusive']: node += parse(f'mutually_exclusive = {{ focus = {s["exclusive"]} }}')
        if s['available']: node += parse('available = { '+s['available']+' }')
        node += parse('completion_reward = { '+reward+' }')
        if s['id'] in fs:
            fs[s['id']][:] = node
        else:
            tree.append(('focus', node, '='))
        for lang, name in [('russian', s['ru']), ('english', s['en'])]:
            loc[lang][s['id']] = name
            purpose = {
                'GER_nww_general_staff': ('Обновим планирование, распределение обязанностей и подготовку офицеров Большого генерального штаба.', 'Renew planning, staff responsibilities and officer training in the Great General Staff.'),
                'GER_nww_mission_command': ('Доверим младшим командирам исполнение общего замысла. Эта школа ускоряет подготовку частей и исключает методическую систему сражения.', 'Delegate execution of the common intent to junior commanders. This training school excludes deliberate battle.'),
                'GER_nww_deliberate_battle': ('Поставим согласование штабов и устойчивость соединений выше самостоятельности отдельных командиров. Этот выбор исключает школу самостоятельного командования.', 'Prioritise staff coordination and formation cohesion. This choice excludes mission command.'),
                'GER_nww_carrier_groups': ('Объединим палубные эскадрильи, авианосцы и корабли охранения в соединения с единым планом воздушных ударов.', 'Unite deck squadrons, carriers and escorts in task groups with a common air strike plan.'),
                'GER_nww_civil_investment': ('Направим сбережения и имперские заказы в гражданские предприятия. Взаимоисключающий выбор: четырёхлетняя оборонная программа станет недоступна.', 'Direct savings and public orders into civilian enterprises. This excludes the four year defence programme.'),
                'GER_nww_defence_procurement': ('Зафиксируем оплаченные оборонные заказы на четыре года. Программа развивает арсеналы без МЕФО, долгов завоевательной экономики и требования захватов; альтернативные гражданские инвестиции станут недоступны.', 'Commit to funded defence orders for four years. Expand arsenals without MEFO, conquest debt or annexation requirements; this excludes the civil investment programme.'),
            }.get(s['id'])
            if purpose:
                description = purpose[0 if lang=='russian' else 1]
            elif s['id'] in industrial:
                description = ('Продолжим выбранную промышленную программу: '+name.lower()+'. Предприятия строятся на контролируемой национальной территории империи.' if lang=='russian' else 'Advance our chosen industrial programme through '+name.lower()+'. New enterprises require controlled imperial core territory.')
            else:
                description = ('Учредим постоянную программу «'+name+'». Военные школы, испытания и совместные учения обеспечат подготовку специалистов и освоение нового вооружения.' if lang=='russian' else 'Establish '+name.lower()+' as a lasting service programme. Schools, trials and joint exercises will train specialists and develop modern equipment.')
            loc[lang][s['id']+'_desc'] = (
                description)
    put(tree, 'continuous_focus_position', parse('x = 150 y = 4200'))
    write('common/national_focus/GER_focuses.txt', dump(doc))

    refresh = []
    dynamic = []
    for service, parameters in mods.items():
        body = []
        for key, modifier in parameters.items():
            var = 'GER_service_'+service+'_'+key
            refresh.append(f'set_variable = {{ {var} = 0 }}')
            body.append(f'{modifier} = {var}')
            labels = {
                'org': ('Организация дивизий','Division organisation'), 'planning': ('Скорость планирования','Planning speed'),
                'training': ('Время подготовки дивизий','Division training time'), 'artillery': ('Атака артиллерии','Artillery attack'),
                'armour': ('Атака бронетехники','Armour attack'), 'supply': ('Расход снабжения','Supply consumption'),
                'experience': ('Прирост армейского опыта','Army experience gain'), 'accidents': ('Вероятность аварий','Air accident chance'),
                'superiority': ('Эффективность превосходства в воздухе','Air superiority efficiency'), 'cas': ('Эффективность штурмовиков','Close air support efficiency'),
                'range': ('Радиус действия','Operational range'), 'mission': ('Эффективность воздушных заданий','Air mission efficiency'),
                'coordination': ('Координация флота','Fleet coordination'), 'output': ('Производительность верфей','Dockyard output'),
                'sortie': ('Эффективность палубных вылетов','Carrier sortie efficiency'), 'screens': ('Атака кораблей охранения','Screen attack'),
                'repair': ('Скорость ремонта','Repair speed'),
            }
            delta = next(s['spirit'][service][key] for s in specs if key in s['spirit'].get(service,{}))
            for lang in loc:
                loc[lang][var+'_tt'] = labels[key][0 if lang=='russian' else 1]+f': §G{delta*100:+.0f}%§!'
        for s in specs:
            if service not in s['spirit']: continue
            increments = ' '.join(f'add_to_variable = {{ GER_service_{service}_{k} = {v} }}' for k,v in s['spirit'][service].items())
            refresh.append(f'if = {{ limit = {{ has_completed_focus = {s["id"]} }} {increments} }}')
        root = {'army':'GER_prussian_traditions','air':PREFIX+'imperial_air_service','navy':'GER_the_fleet_question'}[service]
        refresh.append(f'if = {{ limit = {{ has_completed_focus = {root} NOT = {{ has_dynamic_modifier = {{ modifier = GER_nww_{service}_programme }} }} }} add_dynamic_modifier = {{ modifier = GER_nww_{service}_programme }} }}')
        icon = {'army':'GFX_goal_generic_army_doctrines','air':'GFX_goal_generic_build_airforce','navy':'GFX_idea_GER_generic_navy_1'}[service]
        dynamic.append(f'GER_nww_{service}_programme = {{ icon = {icon} enable = {{ always = yes }} '+' '.join(body)+' }')
        for lang in loc:
            loc[lang]['GER_nww_'+service+'_programme'] = {'russian':{'army':'Имперская армейская программа','air':'Имперская авиационная программа','navy':'Программа Флота открытого моря'},'english':{'army':'Imperial Army Programme','air':'Imperial Air Programme','navy':'High Seas Fleet Programme'}}[lang][service]
            loc[lang]['GER_nww_'+service+'_programme_desc'] = 'Параметры зависят от завершённых реформ.' if lang=='russian' else 'Parameters reflect completed service reforms.'
    effect = 'GER_nww_refresh_services = {\n'+'\n'.join(refresh)+'\n}\n'
    effect += '''GER_nww_build_service_dockyard = {
 random_owned_controlled_state = {
  limit = { is_core_of = PREV is_coastal = yes }
  add_extra_state_shared_building_slots = 1
  add_building_construction = { type = dockyard level = 1 instant_build = yes }
 }
}
'''
    write('common/scripted_effects/GER_services_effects.txt', effect)
    write('common/dynamic_modifiers/GER_services_modifiers.txt', '\n'.join(dynamic))
    write('common/on_actions/GER_services_on_actions.txt', '''on_actions = {
 on_startup = { effect = { every_country = { limit = { original_tag = GER has_focus_tree = GER_focus } GER_nww_refresh_services = yes } } }
 on_daily_GER = { effect = { if = { limit = { has_focus_tree = GER_focus } GER_nww_refresh_services = yes } } }
}
''')
    # Extend the existing single industrial spirit and its exact old-save replay.
    effdoc = read(ROOT/'common/scripted_effects/GER_industry_effects.txt')
    refresh_industry = one(effdoc, 'GER_nww_refresh_industry')
    for fid, bonuses in industrial.items():
        refresh_industry[:] = [e for e in refresh_industry if not (e[0]=='if' and one(one(e[1],'limit',[]),'has_completed_focus')==fid)]
        if bonuses:
            refresh_industry += parse('if = { limit = { has_completed_focus = '+fid+' } '+' '.join(f'add_to_variable = {{ GER_industry_{k} = {v} }}' for k,v in bonuses.items())+' }')
    write('common/scripted_effects/GER_industry_effects.txt', dump(effdoc))
    write('docs/GER_industry_rework.json', json.dumps(meta, ensure_ascii=False, indent=2))
    for lang, entries in loc.items():
        entries['GER_nww_service_research'] = 'Исследования вооружённых сил' if lang=='russian' else 'Armed Forces Research'
        for service in ('land','air','naval'):
            entries[f'GER_nww_{service}_doctrine'] = 'Развитие военной доктрины' if lang=='russian' else 'Military Doctrine Development'
        write(f'localisation/{lang}/GER_services_l_{lang}.yml', 'l_'+lang+':\n'+'\n'.join(' '+k+':0 '+quoted(v) for k,v in entries.items()))
    manifest = {'new_focuses': specs, 'service_modifiers': mods, 'count_added': len(specs), 'total_playable': 76+len(specs)}
    write('docs/GER_services_expansion.json', json.dumps(manifest, ensure_ascii=False, indent=2))
    legacy_path = ROOT/'docs/legacy_import.json'
    legacy = json.loads(legacy_path.read_text(encoding='utf-8-sig'))
    legacy['countries']['GER']['focus_ids'] = [one(f,'id') for f in values(tree,'focus')]
    legacy['countries']['GER']['total'] = len(values(tree,'focus'))
    write('docs/legacy_import.json', json.dumps(legacy, ensure_ascii=False, indent=2))
    print(f'Added {len(specs)} focuses: army, air, navy and two industrial policies.')


if __name__ == '__main__':
    main()
