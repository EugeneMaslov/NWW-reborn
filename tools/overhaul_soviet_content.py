"""Build NWW Soviet reconstruction and diplomacy; retain original NWW focus IDs."""
import json
import re
import copy
from datetime import date, timedelta
from pathlib import Path
from hoi4_script import read, parse, one, values, walk, dump, TOKEN

ROOT = Path(__file__).resolve().parents[1]
GAME = Path('D:/Steam/steamapps/common/Hearts of Iron IV')
LEGACY = '''SOV_the_revolution_endures SOV_russian_socialism SOV_the_new_constitution
SOV_brotherhood_of_peoples SOV_second_five_year_plan SOV_magnitogorsk SOV_urals_industry
SOV_deep_battle SOV_red_artillery SOV_workers_and_peasants_army SOV_red_wings
SOV_ilya_muromets_spirit SOV_red_banner_fleet SOV_comintern_calls'''.split()
STAGES = {
    'state': ['SOV_the_new_constitution', 'SOV_brotherhood_of_peoples', 'NWW_SOV_civil_peace'],
    'economy': ['SOV_magnitogorsk', 'SOV_urals_industry', 'NWW_SOV_plan_fulfilled'],
    'army': ['NWW_SOV_unified_command', 'NWW_SOV_professional_officers', 'NWW_SOV_army_maneuvers'],
}
LABELS = {}
FILES = []
DESCRIPTIONS_EN = {
    'SOV_the_revolution_endures': 'Land disputes, hungry cities and failing authority broke the empire during 1918–1922. The soviets retained its industrial heartland, but the civil-war settlement has yet to become a durable state.',
    'SOV_russian_socialism': 'Before new campaigns, restore taxation, city supplies and trust in public institutions. The revolution must demonstrate that it can govern.',
    'SOV_the_new_constitution': 'Define central and republican powers. Rights and budget obligations will replace the temporary orders of the civil war.',
    'SOV_brotherhood_of_peoples': 'National councils gain permanent representation. Kharkiv, Riga and Tallinn remain negotiating partners rather than territories annexed by decree.',
    'NWW_SOV_union_congress': 'Agree on common supplies, military coordination and revenue. The allied republics retain their own governments.',
    'NWW_SOV_party_coordination': 'Use coordinated party institutions to reconcile central and local decisions. This excludes the alternative republican charter model.',
    'NWW_SOV_republican_charters': 'Use negotiated republican charters to reconcile central and local decisions. This excludes the alternative party coordination model.',
    'NWW_SOV_budget_accountability': 'A common budget and enforceable responsibilities will replace overlapping emergency commissions with a permanent civil service.',
    'NWW_SOV_civil_peace': 'Complete the civil settlement through functioning institutions and common rules. Disputes over the Union Treaty will cease to paralyse government.',
    'SOV_second_five_year_plan': 'Transport, grain supplies and machinery lag behind heavy industry. Revise the plan to correct these imbalances.',
    'NWW_SOV_industrial_survey': 'Audit machinery, fuel and freight. Production targets must reflect actual capacity.',
    'NWW_SOV_agricultural_credit': 'Tractors, credit and predictable purchase prices will restore rural supplies. A new civilian factory provides the necessary workshops.',
    'SOV_magnitogorsk': 'Connect metallurgy with machinery production. Two civilian factories and coordinated deliveries improve the economic plan.',
    'SOV_urals_industry': 'Ural manufacturers receive actual military contracts and new capacity. Two armaments plants reduce reliance on improvised workshops.',
    'NWW_SOV_railway_bottlenecks': 'Coordinate freight schedules and expand infrastructure in our industrial heartland.',
    'NWW_SOV_power_stations': 'Expand civilian capacity and coordinate the electricity supply of industrial districts.',
    'NWW_SOV_standardized_armaments': 'Common drawings and acceptance standards simplify repairs and raise armaments output.',
    'NWW_SOV_plan_fulfilled': 'Civilian capacity, military contracts and transport now form a working plan. The final starting economic penalties become lasting advantages.',
    'NWW_SOV_scientific_network': 'Restore engineering education and laboratory networks while retaining experienced research teams.',
    'NWW_SOV_technical_colleges': 'Train the technicians and engineers needed by modern industry.',
    'NWW_SOV_research_council': 'Connect universities, factory laboratories and proving grounds. Research slots remain capped at five.',
    'NWW_SOV_atomic_laboratories': 'A long-term physics programme requires functioning institutions and laboratories.',
    'NWW_SOV_rocket_bureau': 'Test stands and engineering teams will begin developing rocket technology.',
    'SOV_deep_battle': 'Examine mobile fronts, armoured trains and rival headquarters. Civil-war experience requires a new military organisation.',
    'NWW_SOV_unified_command': 'Replace competing headquarters with common operational rules and a professional chain of command.',
    'SOV_workers_and_peasants_army': 'Introduce common establishments and training programmes. A manpower reserve cannot substitute for trained formations.',
    'SOV_red_artillery': 'Train observers and gun crews, and organise the supply of artillery formations.',
    'NWW_SOV_professional_officers': 'Military colleges, staff training and promotion by qualification replace improvisation. Mass purges are not part of this programme.',
    'NWW_SOV_mechanized_reserve': 'Concentrate modern equipment in properly supplied reserve formations.',
    'NWW_SOV_field_radios': 'Give headquarters, artillery observers and supply services a common communications network.',
    'NWW_SOV_motorized_columns': 'Motor vehicles give reserve formations the mobility required for modern operations.',
    'NWW_SOV_army_logistics': 'Make supply, repair and route preparation integral parts of operational planning.',
    'NWW_SOV_army_maneuvers': 'Test unified command, artillery and logistics together. The final penalties of the Civil War Army will be removed.',
    'NWW_SOV_regular_army': 'Consolidate officer training and establish a sustainable mobilisation reserve.',
    'SOV_red_wings': 'An aviation school will coordinate the training of crews and technical services.',
    'NWW_SOV_fighter_schools': 'Organise fighter pilot training and aircraft testing.',
    'NWW_SOV_ground_support': 'Develop coordination between aviation and ground headquarters.',
    'SOV_ilya_muromets_spirit': 'Experienced heavy-aircraft designers will support a new long-range bomber programme.',
    'NWW_SOV_air_service': 'Unify aircraft repair, crew training and airfield preparation.',
    'SOV_red_banner_fleet': 'Restore naval training and the administration of maritime bases.',
    'NWW_SOV_baltic_bases': 'Develop shipbuilding on our own coastline.',
    'NWW_SOV_black_sea_bases': 'New dockyards and coastal supplies will support the southern squadron.',
    'NWW_SOV_escort_fleet': 'Light ships, cruisers and anti-submarine training will protect maritime communications.',
    'NWW_SOV_coastal_submarines': 'Train submarine crews and develop new underwater equipment.',
    'NWW_SOV_fleet_readiness': 'Joint exercises will test the command of escort and submarine formations.',
    'SOV_comintern_calls': 'Coordinate the foreign policy of the Soviet republics. External demands must follow domestic reconstruction.',
    'NWW_SOV_strategic_pause': 'The army, economy and Union institutions must be ready before an external crisis.',
    'NWW_SOV_frontier_review': 'Prepare political and military demands towards the buffer states. A calendar date cannot replace domestic reforms.',
    'NWW_SOV_western_command': 'Prepare operational objectives and supplies for the western front.',
    'NWW_SOV_litbel_ultimatum': 'Request military access and neutrality guarantees. The Union decides whether to accept our terms or resist.',
    'NWW_SOV_litbel_campaign': 'After refusal, the prepared headquarters receives a permanent war goal. Allies and states that accepted a peaceful settlement are excluded.',
    'NWW_SOV_steppe_conference': 'Offer the Free Territory equipment and grain exchange and a non-aggression pact. Existing recognition of equal autonomy and alliances remain in force.',
    'NWW_SOV_steppe_campaign': 'War requires refusal, a prepared regular army and the absence of alliance commitments. Recognized equal autonomy prevents this campaign.',
}


def write(relative, node):
    def normalize(entries):
        result = []
        for key, value, op in entries:
            if key == 'check_variable' and isinstance(value, list):
                operands = [(k, v, o) for k, v, o in value if k not in ('tooltip', 'compare')]
                if one(value, 'var') is None and len(operands) == 1 and (one(value, 'compare') or operands[0][2] in ('>=', '<=', '!=', '==')):
                    name, amount, compare = operands[0]
                    mapping = {'>=': 'greater_than_or_equals', '<=': 'less_than_or_equals',
                               '!=': 'not_equals', '==': 'equals', '=': 'equals', '<': 'less_than', '>': 'greater_than'}
                    selected = one(value, 'compare', mapping[compare])
                    value = [('var', name, '='), ('value', amount, '='), ('compare', selected, '=')]
            if key == 'remove_dynamic_modifier' and isinstance(value, str):
                value = [('modifier', value, '=')]
            if isinstance(value, list):
                value = normalize(value)
            if op in ('>=', '<=', '!='):
                reverse = {'>=': '<', '<=': '>', '!=': '='}[op]
                result.append(('NOT', [(key, value, reverse)], '='))
            else:
                result.append((key, value, '=' if op == '==' else op))
        return result
    node = normalize(node)
    path = ROOT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(dump(node) + '\n', encoding='utf-8', newline='\n')
    FILES.append(relative)


def comment(relative, text):
    path = ROOT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text('# ' + text + '\n', encoding='utf-8', newline='\n')
    FILES.append(relative)


def field(node, key, value):
    node[:] = [(k, v, o) for k, v, o in node if k != key]
    node.append((key, value, '='))


def label(key, ru, en, ru_desc=None, en_desc=None):
    LABELS[key] = (ru, en)
    if ru_desc is not None:
        LABELS[key + '_desc'] = (ru_desc, en_desc)


def factory(kind='industrial_complex', count=1):
    coastal = 'is_coastal = yes' if kind == 'dockyard' else ''
    return f'''random_owned_controlled_state = {{ limit = {{ is_core_of = PREV {coastal} }}
        add_extra_state_shared_building_slots = {count}
        add_building_construction = {{ type = {kind} level = {count} instant_build = yes }} }}'''


def tech(category, uses=1):
    return f'add_tech_bonus = {{ category = {category} uses = {uses} bonus = 0.5 }}'


def doctrine(category):
    return f'add_doctrine_cost_reduction = {{ name = NWW_SOV_doctrine_bonus category = {category} uses = 1 cost_reduction = 0.5 }}'


def main():
    tree = parse('''id = SOV_focus default = no
        country = { factor = 0 modifier = { add = 100 tag = SOV } }
        continuous_focus_position = { x = 100 y = 2500 }''')
    by_id = {}

    def focus(fid, x, y, ru, en, desc, reward='', parents=(), cost=10,
              icon='GFX_goal_generic_political_pressure', gate=None, en_desc=None):
        node = parse(f'id = {fid} x = {x} y = {y} cost = {cost} icon = {icon}')
        for parent in parents:
            choices = parent if isinstance(parent, tuple) else (parent,)
            node.append(('prerequisite', parse(' '.join('focus = ' + p for p in choices)), '='))
        if gate:
            node.append(('available', parse(gate), '='))
            node.extend(parse('cancel_if_invalid = yes continue_if_invalid = no'))
        # The stage updater counts completed milestones; this reward also works
        # when the completion callback precedes registering its own focus ID.
        if any(fid in milestones for milestones in STAGES.values()):
            reward += f'\nset_country_flag = {fid}_reform_done\nnww_SOV_update_reconstruction = yes'
        node.append(('completion_reward', parse(reward), '='))
        tree.append(('focus', node, '='))
        by_id[fid] = node
        label(fid, ru, en, desc, en_desc or DESCRIPTIONS_EN[fid])

    # Constitutional reconstruction and a genuine institutional choice.
    focus('SOV_the_revolution_endures', 8, 0, 'После Великой смуты', 'After the Great Tumult',
          'В 1918–1922 годах империю разрушили земельный вопрос, голодные города и распад власти. Советы удержали промышленный центр, но мир гражданской войны ещё не стал устойчивым государством.',
          'add_political_power = 100 country_event = { id = nww_sov.1 days = 1 }',
          icon='GFX_goal_support_communism')
    focus('SOV_russian_socialism', 6, 1, 'Сначала восстановить республику', 'Rebuild the Republic First',
          'Прежде новых походов восстановим налоговую систему, снабжение городов и доверие к учреждениям. Революция должна доказать, что умеет управлять.',
          'add_political_power = 75 add_stability = 0.05', ['SOV_the_revolution_endures'], cost=5)
    focus('SOV_the_new_constitution', 10, 1, 'Конституция советских республик', 'Constitution of the Soviet Republics',
          'Определим полномочия центра и республиканских органов. Права и бюджетные обязательства заменят временные распоряжения гражданской войны.',
          'add_stability = 0.05', ['SOV_the_revolution_endures'], icon='GFX_goal_generic_national_unity')
    focus('SOV_brotherhood_of_peoples', 10, 2, 'Представительство республик', 'Representation of the Republics',
          'Национальные советы получат постоянное представительство в общих учреждениях. Харьков, Рига и Таллин остаются участниками переговоров, а не территориями для бесплатного присоединения.',
          'add_political_power = 50', ['SOV_the_new_constitution'], icon='GFX_goal_generic_improve_relations')
    focus('NWW_SOV_union_congress', 8, 3, 'Съезд союзного договора', 'Congress of the Union Treaty',
          'Согласуем общее снабжение, военную координацию и распределение доходов. Собственные правительства союзных республик сохраняются.',
          'add_stability = 0.05', ['SOV_russian_socialism', 'SOV_brotherhood_of_peoples'], cost=5)
    for fid, x, ru, en, reward in [
        ('NWW_SOV_party_coordination', 6, 'Партийная координация', 'Party Coordination', 'add_ideas = NWW_SOV_party_coordination_idea'),
        ('NWW_SOV_republican_charters', 10, 'Хартии республик', 'Republican Charters', 'add_ideas = NWW_SOV_republican_charters_idea')]:
        focus(fid, x, 4, ru, en, 'Выберем постоянный способ согласования решений центра и местных советов. Этот институциональный выбор исключает противоположный вариант.',
              reward, ['NWW_SOV_union_congress'], cost=5, icon='GFX_focus_generic_diplomatic_treaty')
    field(by_id['NWW_SOV_party_coordination'], 'mutually_exclusive', parse('focus = NWW_SOV_republican_charters'))
    field(by_id['NWW_SOV_republican_charters'], 'mutually_exclusive', parse('focus = NWW_SOV_party_coordination'))
    focus('NWW_SOV_budget_accountability', 8, 5, 'Ответственность комиссариатов', 'Accountability of the Commissariats',
          'Единый бюджет и проверка исполнения решений сократят дублирование аппарата. Заменим чрезвычайные комиссии постоянной государственной службой.',
          'add_political_power = 75', [('NWW_SOV_party_coordination', 'NWW_SOV_republican_charters')], cost=5)
    focus('NWW_SOV_civil_peace', 8, 6, 'Завершить гражданское урегулирование', 'Complete the Civil Settlement',
          'Гражданское урегулирование заканчивается действующими учреждениями и общими правилами. Противоречия союзного договора больше не парализуют государство.',
          'add_stability = 0.05', ['NWW_SOV_budget_accountability'], icon='GFX_goal_generic_national_unity')

    # Real buildings and a gradually repaired economic spirit.
    industry_icon = 'GFX_goal_generic_construct_civ_factory'
    focus('SOV_second_five_year_plan', 22, 0, 'Пересмотр хозяйственного плана', 'Revise the Economic Plan',
          'Транспорт, хлебозаготовки и выпуск оборудования отстают от тяжёлой промышленности. Новая программа исправит эти диспропорции.',
          tech('industry', 2), icon=industry_icon)
    focus('NWW_SOV_industrial_survey', 22, 1, 'Учёт заводов и поставок', 'Survey Factories and Deliveries',
          'Составим проверяемый баланс оборудования, топлива и перевозок. Плановые задания будут опираться на реальные мощности.',
          'add_political_power = 50', ['SOV_second_five_year_plan'], cost=5, icon=industry_icon)
    focus('NWW_SOV_agricultural_credit', 22, 2, 'Сельский кредит и машинные станции', 'Rural Credit and Machine Stations',
          'Тракторы и предсказуемые закупочные цены восстановят сельское снабжение городов. Новая гражданская фабрика даст мастерские для этой программы.',
          factory(), ['NWW_SOV_industrial_survey'], icon=industry_icon)
    focus('SOV_magnitogorsk', 20, 3, 'Магнитогорский промышленный узел', 'The Magnitogorsk Industrial Hub',
          'Свяжем металлургию с выпуском оборудования. Два гражданских предприятия и сбалансированные поставки улучшат состояние хозяйственного плана.',
          factory(count=2), ['NWW_SOV_agricultural_credit'], icon=industry_icon)
    focus('SOV_urals_industry', 24, 3, 'Уральские оружейные заводы', 'Ural Armaments Plants',
          'Уральские предприятия получат реальные военные заказы и новые мощности. Производство перестанет зависеть от импровизированных мастерских.',
          factory('arms_factory', 2), ['NWW_SOV_agricultural_credit'], icon='GFX_goal_generic_construct_mil_factory')
    focus('NWW_SOV_railway_bottlenecks', 22, 4, 'Устранить железнодорожные узкие места', 'Clear Railway Bottlenecks',
          'Согласуем графики грузов и расширим инфраструктуру центральных промышленных областей.',
          'random_owned_controlled_state = { limit = { is_core_of = PREV } add_building_construction = { type = infrastructure level = 1 instant_build = yes } }',
          ['SOV_magnitogorsk', 'SOV_urals_industry'], icon='GFX_goal_generic_construct_infrastructure')
    focus('NWW_SOV_power_stations', 20, 5, 'Электрификация промышленных районов', 'Electrify the Industrial Districts',
          'Увеличим мощность гражданских предприятий и согласуем энергоснабжение заводов.', factory(), ['NWW_SOV_railway_bottlenecks'], icon=industry_icon)
    focus('NWW_SOV_standardized_armaments', 24, 5, 'Стандарты вооружения', 'Standardize Armaments',
          'Общие чертежи и нормы приёмки позволят ремонтировать технику и наращивать выпуск.',
          factory('arms_factory') + ' ' + tech('industry'), ['NWW_SOV_railway_bottlenecks'], icon='GFX_goal_generic_construct_mil_factory')
    focus('NWW_SOV_plan_fulfilled', 22, 6, 'Сбалансированная хозяйственная программа', 'A Balanced Economic Programme',
          'Гражданские мощности, военные заказы и транспорт теперь связаны одним действующим планом. Последние стартовые хозяйственные штрафы сменятся преимуществами.',
          'add_stability = 0.05', ['NWW_SOV_power_stations', 'NWW_SOV_standardized_armaments'], icon=industry_icon)

    focus('NWW_SOV_scientific_network', 32, 0, 'Сеть научных институтов', 'Network of Scientific Institutes',
          'Восстановим подготовку инженеров и сеть лабораторий, сохранив исследовательские коллективы.', tech('electronics'), icon='GFX_goal_generic_scientific_exchange')
    focus('NWW_SOV_technical_colleges', 32, 1, 'Технические училища', 'Technical Colleges',
          'Промышленности нужны подготовленные мастера и инженеры.', tech('industry'), ['NWW_SOV_scientific_network'], icon='GFX_goal_generic_scientific_exchange')
    focus('NWW_SOV_research_council', 32, 2, 'Совет прикладных исследований', 'Council of Applied Research',
          'Соединим университеты, заводские лаборатории и испытательные полигоны. Число исследовательских ячеек ограничено пятью.',
          'if = { limit = { amount_research_slots < 5 } add_research_slot = 1 }', ['NWW_SOV_technical_colleges'], icon='GFX_goal_generic_scientific_exchange')
    focus('NWW_SOV_atomic_laboratories', 30, 3, 'Лаборатории атомной физики', 'Atomic Physics Laboratories',
          'Долгосрочная программа физики требует действующих институтов, а не разовых обещаний.',
          tech('nuclear'), ['NWW_SOV_research_council'], icon='GFX_goal_generic_scientific_exchange', gate='date > 1938.1.1')
    focus('NWW_SOV_rocket_bureau', 34, 3, 'Ракетное конструкторское бюро', 'Rocket Design Bureau',
          'Испытательные стенды и инженерные коллективы начнут исследование ракетной техники.',
          tech('rocketry'), ['NWW_SOV_research_council'], icon='GFX_goal_generic_scientific_exchange')

    # Red Army rebuilt from civil-war formations, with no purges.
    army_icon = 'GFX_goal_generic_army_doctrines'
    focus('SOV_deep_battle', 42, 0, 'Уроки гражданской войны', 'Lessons of the Civil War',
          'Разберём опыт манёвренных фронтов, бронепоездов и разрозненных штабов. Боевой опыт гражданской войны требует новой организации.',
          doctrine('land_doctrine') + ' army_experience = 15', icon=army_icon)
    focus('NWW_SOV_unified_command', 42, 1, 'Единое оперативное командование', 'Unified Operational Command',
          'Устраним конкурирующие штабы и установим общие оперативные правила. Командование больше не зависит от личных связей гражданской войны.',
          'add_command_power = 20', ['SOV_deep_battle'], icon=army_icon)
    focus('SOV_workers_and_peasants_army', 42, 2, 'Регулярная рабоче-крестьянская армия', 'A Regular Workers and Peasants Army',
          'Воинские части получат общие штаты и учебные программы. Мобилизационный резерв не заменяет подготовленные подразделения.',
          'add_manpower = 100000 army_experience = 15', ['NWW_SOV_unified_command'], icon='GFX_goal_generic_allies_build_infantry')
    focus('SOV_red_artillery', 40, 3, 'Красная артиллерия', 'Red Artillery',
          'Подготовим наблюдателей, расчёты и снабжение артиллерии.', tech('artillery', 2) + ' army_experience = 15',
          ['SOV_workers_and_peasants_army'], cost=5, icon='GFX_goal_generic_army_artillery')
    focus('NWW_SOV_professional_officers', 42, 3, 'Профессиональный офицерский корпус', 'Professional Officer Corps',
          'Военные училища, штабная подготовка и продвижение по квалификации заменят военную импровизацию. Массовые чистки не являются частью этой программы.',
          'army_experience = 20', ['SOV_workers_and_peasants_army'], icon=army_icon)
    focus('NWW_SOV_mechanized_reserve', 46, 3, 'Механизированный резерв', 'Mechanized Reserve',
          'Сосредоточим современную технику в оснащённых резервных частях.', tech('armor'), ['SOV_workers_and_peasants_army'], icon='GFX_goal_generic_army_tanks')
    focus('NWW_SOV_field_radios', 42, 4, 'Радиосвязь полевых штабов', 'Field Headquarters Radio',
          'Свяжем штабы, артиллерию и службы снабжения общими средствами связи.', tech('electronics'), ['NWW_SOV_professional_officers'], cost=5, icon=army_icon)
    focus('NWW_SOV_motorized_columns', 46, 4, 'Моторизованные колонны', 'Motorized Columns',
          'Автомобильные подразделения дадут резервам необходимую подвижность.', tech('motorized_equipment'), ['NWW_SOV_mechanized_reserve'], icon='GFX_goal_generic_army_motorized')
    focus('NWW_SOV_army_logistics', 42, 5, 'Тыл регулярной армии', 'Logistics of the Regular Army',
          'Снабжение, ремонт и подготовка маршрутов станут частью оперативного плана.',
          'add_ideas = NWW_SOV_regular_logistics', ['NWW_SOV_field_radios'], icon='GFX_goal_generic_construct_infrastructure')
    focus('NWW_SOV_army_maneuvers', 42, 6, 'Общевойсковые манёвры', 'Combined Arms Manoeuvres',
          'Проверим единое командование, работу артиллерии и тыла в общих манёврах. Последние штрафы армии гражданской войны будут устранены.',
          'army_experience = 25', ['NWW_SOV_army_logistics', 'SOV_red_artillery'], icon=army_icon)
    focus('NWW_SOV_regular_army', 42, 7, 'Армия нового государства', 'Army of the New State',
          'Закрепим подготовку кадров и сформируем устойчивый мобилизационный резерв.',
          doctrine('land_doctrine') + ' add_war_support = 0.05', ['NWW_SOV_army_maneuvers'], icon=army_icon)

    focus('SOV_red_wings', 54, 0, 'Красные крылья', 'Red Wings',
          'Авиационная школа объединит подготовку экипажей и технических служб.', doctrine('air_doctrine') + ' air_experience = 15', icon='GFX_goal_generic_build_airforce')
    focus('NWW_SOV_fighter_schools', 54, 1, 'Истребительные школы', 'Fighter Schools',
          'Организуем подготовку истребительных экипажей и испытание самолётов.', tech('light_air'), ['SOV_red_wings'], icon='GFX_goal_generic_air_fighter')
    focus('NWW_SOV_ground_support', 52, 2, 'Авиация поля боя', 'Battlefield Aviation',
          'Разработаем взаимодействие авиации и наземных штабов.', tech('cas_bomber'), ['NWW_SOV_fighter_schools'], icon='GFX_goal_generic_CAS')
    focus('SOV_ilya_muromets_spirit', 56, 2, 'Дальний бомбардировочный корпус', 'Long Range Bomber Corps',
          'Опыт конструкторов тяжёлых самолётов послужит новой программе дальних машин.', tech('heavy_air'), ['NWW_SOV_fighter_schools'], icon='GFX_goal_generic_air_bomber')
    focus('NWW_SOV_air_service', 54, 3, 'Единая авиационная служба', 'Unified Air Service',
          'Объединим ремонт, обучение и подготовку аэродромов.', 'add_ideas = NWW_SOV_air_service_idea air_experience = 20',
          ['NWW_SOV_ground_support', 'SOV_ilya_muromets_spirit'], icon='GFX_goal_generic_build_airforce')

    focus('SOV_red_banner_fleet', 64, 0, 'Краснознамённый флот', 'Red Banner Fleet',
          'Восстановим кадровую подготовку флота и управление морскими базами.', doctrine('naval_doctrine') + ' navy_experience = 15', icon='GFX_goal_generic_build_navy')
    focus('NWW_SOV_baltic_bases', 62, 1, 'Балтийские базы', 'Baltic Bases',
          'Развиваем судостроение на собственном побережье.', factory('dockyard'), ['SOV_red_banner_fleet'], icon='GFX_goal_generic_construct_naval_dockyard')
    focus('NWW_SOV_black_sea_bases', 66, 1, 'Черноморская программа', 'Black Sea Programme',
          'Новые верфи и береговое снабжение поддержат южную эскадру.', factory('dockyard'), ['SOV_red_banner_fleet'], icon='GFX_goal_generic_construct_naval_dockyard')
    focus('NWW_SOV_escort_fleet', 62, 2, 'Эскортные соединения', 'Escort Groups',
          'Крейсеры, лёгкие корабли и противолодочная подготовка защитят морские коммуникации.', tech('naval_equipment'), ['NWW_SOV_baltic_bases'], icon='GFX_goal_generic_build_navy')
    focus('NWW_SOV_coastal_submarines', 66, 2, 'Подводные силы', 'Submarine Force',
          'Готовим экипажи и новую подводную технику.', tech('naval_equipment'), ['NWW_SOV_black_sea_bases'], icon='GFX_goal_generic_navy_submarine')
    focus('NWW_SOV_fleet_readiness', 64, 3, 'Готовность флота', 'Fleet Readiness',
          'Общие учения проверят управление эскортами и подводными соединениями.',
          doctrine('naval_doctrine') + ' navy_experience = 25', ['NWW_SOV_escort_fleet', 'NWW_SOV_coastal_submarines'], icon='GFX_goal_generic_build_navy')

    # Distant domestic requirements are availability gates, not cross-tree lines.
    reform_gate = '''custom_trigger_tooltip = { tooltip = NWW_SOV_reconstruction_ready_tt
        has_completed_focus = NWW_SOV_union_congress
        has_completed_focus = SOV_magnitogorsk has_completed_focus = SOV_urals_industry
        has_completed_focus = NWW_SOV_professional_officers }'''
    war_gate = '''is_subject = no has_government = communism
        custom_trigger_tooltip = { tooltip = NWW_SOV_campaign_ready_tt
            has_completed_focus = NWW_SOV_civil_peace has_completed_focus = NWW_SOV_army_maneuvers }'''
    focus('SOV_comintern_calls', 76, 0, 'Общий революционный фронт', 'A Common Revolutionary Front',
          'Согласуем общую политику советских республик. Внешние требования станут продолжением подготовки государства, а не заменой реформам.',
          'add_political_power = 50', cost=5, gate='has_completed_focus = SOV_russian_socialism', icon='GFX_focus_generic_diplomatic_treaty')
    focus('NWW_SOV_strategic_pause', 76, 1, 'Реконструкция перед экспансией', 'Reconstruction before Expansion',
          'Армия, экономика и союзные учреждения должны быть готовы к внешнему кризису.',
          'add_war_support = 0.05', ['SOV_comintern_calls'], cost=5, gate=reform_gate, icon='GFX_goal_generic_position_armies')
    focus('NWW_SOV_frontier_review', 76, 2, 'Пересмотр западной границы', 'Review the Western Frontier',
          'Подготовим политические и военные требования к буферным государствам. Дата сама по себе не заменяет внутренних реформ.',
          'add_command_power = 15', ['NWW_SOV_strategic_pause'], cost=5, gate='date > 1938.1.1', icon='GFX_goal_generic_demand_territory')
    focus('NWW_SOV_western_command', 76, 3, 'Западное оперативное командование', 'Western Operational Command',
          'Разработаем ограниченные оперативные задачи и снабжение западного фронта.',
          'army_experience = 20', ['NWW_SOV_frontier_review'], cost=5, gate=war_gate, icon='GFX_goal_generic_position_armies')
    focus('NWW_SOV_litbel_ultimatum', 74, 4, 'Требования к Литовско-Белорусскому Союзу', 'Demands to the Lithuanian Belarusian Union',
          'Предложим Союзу военный доступ и внешнеполитические гарантии. Его правительство самостоятельно решит, принять требования или готовиться к сопротивлению.',
          'LTB = { country_event = { id = nww_sov.10 days = 1 } }', ['NWW_SOV_western_command'],
          gate='''date > 1939.1.1 is_subject = no LTB = { exists = yes is_subject = no }
            NOT = { is_ally_with = LTB } NOT = { has_war_with = LTB }''', icon='GFX_goal_generic_demand_territory')
    focus('NWW_SOV_litbel_campaign', 74, 5, 'Западная кампания', 'The Western Campaign',
          'После отказа Союза подготовленный штаб получает бессрочную цель войны. Союзники и добровольно заключившие урегулирование государства исключены из кампании.',
          'custom_effect_tooltip = NWW_SOV_litbel_war_tt hidden_effect = { nww_SOV_prepare_litbel_campaign = yes }',
          ['NWW_SOV_litbel_ultimatum'], gate=war_gate + ''' date > 1939.6.1 has_war_support > 0.30
            has_country_flag = NWW_SOV_LTB_rejected NOT = { has_country_flag = NWW_SOV_LTB_settlement }
            LTB = { exists = yes } NOT = { is_ally_with = LTB } NOT = { has_war_with = LTB }''',
          icon='GFX_goal_generic_major_war')
    field(by_id['NWW_SOV_litbel_campaign'], 'bypass', parse('OR = { is_ally_with = LTB has_country_flag = NWW_SOV_LTB_settlement LTB = { exists = no } }'))
    focus('NWW_SOV_steppe_conference', 80, 3, 'Переговоры с вольной степью', 'Negotiations with the Free Steppe',
          'Съезд вольной территории получит предложение о хозяйственном обмене и ненападении. Признанные договоры равноправия и существующие союзы сохраняются.',
          'MKN = { country_event = { id = nww_sov.20 days = 1 } }', ['NWW_SOV_frontier_review'],
          gate='''date > 1939.1.1 is_subject = no MKN = { exists = yes is_subject = no }
            NOT = { has_war_with = MKN } NOT = { has_country_flag = NWW_SOV_MKN_settlement }''', icon='GFX_focus_generic_diplomatic_treaty')
    focus('NWW_SOV_steppe_campaign', 80, 4, 'Разрешить степной конфликт', 'Resolve the Steppe Conflict',
          'Война возможна после отказа от протокола, при готовности регулярной армии и отсутствии союзных обязательств. Новая ветка не отменяет признанное равноправие махновских советов.',
          'custom_effect_tooltip = NWW_SOV_steppe_war_tt hidden_effect = { nww_SOV_prepare_steppe_campaign = yes }',
          ['NWW_SOV_steppe_conference'], gate=war_gate + ''' date > 1940.1.1 has_war_support > 0.30
            has_country_flag = NWW_SOV_MKN_rejected NOT = { has_country_flag = NWW_SOV_MKN_settlement }
            MKN = { exists = yes NOT = { has_country_flag = MKN_equal_autonomy } }
            NOT = { is_ally_with = MKN } NOT = { has_war_with = MKN }''', icon='GFX_goal_generic_major_war')
    field(by_id['NWW_SOV_steppe_campaign'], 'bypass', parse('''OR = { is_ally_with = MKN
        has_country_flag = NWW_SOV_MKN_settlement MKN = { exists = no }
        MKN = { has_country_flag = MKN_equal_autonomy } }'''))

    # Keep native references registered, while making their focuses inaccessible.
    native_tree = one(read(GAME / 'common/national_focus/soviet.txt'), 'focus_tree')
    compatibility = []
    for f in values(native_tree, 'focus'):
        fid = one(f, 'id')
        if fid in by_id:
            continue
        shared = parse(f'id = {fid} icon = {one(f, "icon")} cost = 5 allow_branch = {{ always = no }} completion_reward = {{ }}')
        compatibility.append(('shared_focus', shared, '='))
        tree.append(('shared_focus', fid, '='))
    write('common/national_focus/SOV_focuses.txt', [('focus_tree', tree, '=')])
    write('common/national_focus/SOV_compatibility.txt', compatibility)
    comment('common/national_focus/sov_focus.txt', 'Country content moved to SOV_focuses.txt; original NWW IDs retained.')
    comment('common/national_focus/soviet.txt', 'NWW Soviet tree lives in SOV_focuses.txt; native IDs registered as hidden compatibility focuses.')

    # One spirit per reform area; no repeated grants when loading a save.
    spirit_stats = {
        'state': [(-0.10, -0.15), (-0.05, -0.10), (0, -0.05), (0.05, 0.10)],
        'economy': [(-0.15, -0.15, 0.05), (-0.10, -0.10, 0.05), (-0.05, -0.05, 0), (0.05, 0.05, 0)],
        'army': [(-0.15, -0.10, -0.05), (-0.10, -0.05, -0.05), (-0.05, 0, 0), (0.05, 0.05, 0.05)],
    }
    areas = {
        'state': ('Незавершённый союзный договор', 'The Unfinished Union Treaty', 'generic_political_support', ['stability_factor', 'political_power_gain']),
        'economy': ('Диспропорции хозяйственного плана', 'Imbalances in the Economic Plan', 'generic_industrial_concern_1', ['industrial_capacity_factory', 'production_speed_buildings_factor', 'consumer_goods_factor']),
        'army': ('Армия гражданской войны', 'The Civil War Army', 'generic_communist_army', ['army_org_factor', 'planning_speed', 'army_attack_factor']),
    }
    ideas = []
    effects = []
    for area, stages in spirit_stats.items():
        ru, en, picture, keys = areas[area]
        for level, stats in enumerate(stages):
            token = f'NWW_SOV_{area}_{level}'
            node = parse(f'picture = {picture} removal_cost = -1 allowed = {{ original_tag = SOV }}')
            node.append(('modifier', [(key, str(value), '=') for key, value in zip(keys, stats) if value], '='))
            ideas.append((token, node, '='))
            label(token, ru if level < 3 else {'state': 'Действующий союзный договор', 'economy': 'Сбалансированный хозяйственный план', 'army': 'Регулярная Красная армия'}[area],
                  en if level < 3 else {'state': 'A Working Union Treaty', 'economy': 'A Balanced Economic Plan', 'army': 'The Regular Red Army'}[area],
                  f'Этап {level + 1} из 4. Реформы последовательно меняют этот дух; случайные чистки и паранойя не используются.',
                  f'Stage {level + 1} of 4. Reconstruction progressively changes this spirit. Random purges and paranoia are not used.')
        milestones = STAGES[area]
        update = []
        # Each milestone gets an exact boolean derived from focus completion,
        # or from its own completion callback's marker.
        condition = lambda fid: f'OR = {{ has_completed_focus = {fid} has_country_flag = {fid}_reform_done }}'
        combos = [
            ' '.join(condition(fid) for fid in milestones),
            'OR = { ' + ' '.join('AND = { ' + condition(milestones[a]) + ' ' + condition(milestones[b]) + ' }' for a, b in [(0, 1), (0, 2), (1, 2)]) + ' }',
            'OR = { ' + ' '.join(condition(fid) for fid in milestones) + ' }',
        ]
        for index, stage in enumerate([3, 2, 1, 0]):
            remove = ' '.join(f'if = {{ limit = {{ has_idea = NWW_SOV_{area}_{other} }} remove_ideas = NWW_SOV_{area}_{other} }}' for other in range(4) if other != stage)
            body = parse(remove + f' if = {{ limit = {{ NOT = {{ has_idea = NWW_SOV_{area}_{stage} }} }} add_ideas = NWW_SOV_{area}_{stage} }}')
            if stage:
                body.insert(0, ('limit', parse(combos[index]), '='))
            update.append(('if' if index == 0 else ('else' if stage == 0 else 'else_if'), body, '='))
        effects.append((f'nww_SOV_update_{area}', update, '='))
    effects += parse('nww_SOV_update_reconstruction = { nww_SOV_update_state = yes nww_SOV_update_economy = yes nww_SOV_update_army = yes }')
    for token, ru, en, picture, mods in [
        ('NWW_SOV_party_coordination_idea', 'Партийная координация', 'Party Coordination', 'generic_political_support', 'political_power_gain = 0.10 war_support_factor = 0.05'),
        ('NWW_SOV_republican_charters_idea', 'Хартии республик', 'Republican Charters', 'generic_political_support', 'stability_factor = 0.10 resistance_target = -0.05'),
        ('NWW_SOV_regular_logistics', 'Тыл регулярной армии', 'Regular Army Logistics', 'generic_communist_army', 'supply_consumption_factor = -0.10'),
        ('NWW_SOV_air_service_idea', 'Единая авиационная служба', 'Unified Air Service', 'generic_aircraft_support', 'air_accidents_factor = -0.10 air_training_xp_gain_factor = 0.10'),
        ('NWW_SOV_steppe_exchange', 'Гуляйпольский хозяйственный протокол', 'Huliaipole Economic Protocol', 'generic_industrial_concern_1', 'research_speed_factor = 0.05 industrial_capacity_factory = 0.05')]:
        ideas.append((token, parse(f'picture = {picture} removal_cost = -1 allowed = {{ always = yes }} modifier = {{ {mods} }}'), '='))
        label(token, ru, en, 'Постоянная программа, созданная реальными решениями и договорённостями нового государства.', 'A lasting programme established by actual reforms and agreements of the new state.')
    write('common/ideas/SOV_ideas.txt', [('ideas', [('country', ideas, '=')], '=')])

    # Preserve the native registry and designers, but disable native spirits in NWW.
    text = (GAME / 'common/ideas/SOV.txt').read_text(encoding='utf-8-sig')
    missing = sum(m.group() == '{' for m in TOKEN.finditer(text)) - sum(m.group() == '}' for m in TOKEN.finditer(text))
    native_ideas_doc = parse(text + '}' * max(0, missing))
    native_country = one(one(native_ideas_doc, 'ideas'), 'country')
    native_ids = [k for k, v, o in native_country]
    for token, node, op in native_country:
        allowed = one(node, 'allowed')
        if allowed is None:
            node.append(('allowed', parse('NOT = { has_focus_tree = SOV_focus }'), '='))
        else:
            allowed.extend(parse('NOT = { has_focus_tree = SOV_focus }'))
    write('common/ideas/SOV.txt', native_ideas_doc)
    dynamic_ids = [k for k, v, o in read(GAME / 'common/dynamic_modifiers/0_dynamic_modifiers.txt') if k.startswith('SOV_')]
    cleanup = parse('''clr_country_flag = SOV_paranoia_system_active_flag
        clr_country_flag = SOV_paranoia_modifier_active_flag
        clr_country_flag = SOV_great_purge_active_flag
        clr_country_flag = SOV_propaganda_campaigns_active_flag
        set_variable = { SOV_paranoia = 0 } set_variable = { SOV_paranoia_weekly_bucket = 0 }
        set_variable = { SOV_paranoia_modifier_increase = 0 }
        set_variable = { SOV_paranoia_weekly_modifiers_amount = 0 }''')
    for token in native_ids + ['SOV_genrikh_yagoda', 'SOV_nikolay_yezhov', 'SOV_lavrenty_beriya', 'SOV_vsevolod_merkulov']:
        cleanup += parse(f'if = {{ limit = {{ has_idea = {token} }} remove_ideas = {token} }}')
    for token in dynamic_ids:
        cleanup += parse(f'if = {{ limit = {{ has_dynamic_modifier = {{ modifier = {token} }} }} remove_dynamic_modifier = {token} }}')
    inactive_decisions = []
    mission_ids = []
    for category, node, op in read(GAME / 'common/decisions/SOV.txt'):
        if isinstance(node, list):
            for token, decision, op in node:
                if not isinstance(decision, list) or not token.startswith('SOV_'):
                    continue
                inactive = parse('allowed = { always = no } visible = { always = no } available = { always = no }')
                if one(decision, 'days_mission_timeout') is not None:
                    inactive += parse('activation = { always = no } days_mission_timeout = 1 timeout_effect = { }')
                    mission_ids.append(token)
                    cleanup += parse(f'if = {{ limit = {{ has_active_mission = {token} }} remove_mission = {token} }}')
                else:
                    inactive += parse('complete_effect = { }')
                inactive_decisions.append((token, inactive, '='))
    write('common/decisions/SOV_compatibility.txt', [('NWW_SOV_disabled_subsystems', inactive_decisions, '=')])
    write('common/decisions/categories/SOV_categories.txt', parse('''NWW_SOV_disabled_subsystems = {
        icon = generic_political_actions visible = { always = no } }'''))
    label('NWW_SOV_disabled_subsystems', 'Недействующие подсистемы совместимости', 'Inactive Compatibility Subsystems')
    cleanup += parse('''if = { limit = { has_country_leader = { character = SOV_iosif_stalin }
        NOT = { has_country_leader_with_trait = NWW_SOV_general_secretary } }
        remove_country_leader_trait = stalin_heart_of_steel
        add_country_leader_trait = NWW_SOV_general_secretary }''')
    cleanup += parse('''every_army_leader = { limit = { has_trait = trait_SOV_cowed_by_stalin_army }
        remove_unit_leader_trait = trait_SOV_cowed_by_stalin_army }
        every_navy_leader = { limit = { has_trait = trait_SOV_cowed_by_stalin_navy }
        remove_unit_leader_trait = trait_SOV_cowed_by_stalin_navy }''')
    effects.append(('nww_SOV_suspend_detached_purges', cleanup, '='))

    # No native decision or GUI can activate a detached Soviet subsystem.
    for relative in ['common/decisions/SOV.txt', 'common/decisions/categories/SOV_decision_categories.txt',
                     'common/scripted_guis/SOV_paranoia_system_scripted_gui.txt',
                     'common/scripted_guis/SOV_propaganda_campaigns_scripted_gui.txt',
                     'common/ai_strategy_plans/SOV_historical_strategy_plan.txt',
                     'common/ai_strategy_plans/SOV_alternate_strategy_plan.txt']:
        comment(relative, 'NWW Soviet reconstruction replaces the native Soviet subsystem; see docs/SOV_lore_and_design.md.')
    blocked_events = 0
    for name in ['NSB_Soviet.txt', 'SovietUnion.txt', 'WTT_Soviet.txt']:
        doc = read(GAME / 'events' / name)
        for kind, event, op in doc:
            if kind not in ('country_event', 'news_event'):
                continue
            gate = one(event, 'trigger')
            if gate is None:
                gate = []
                event.append(('trigger', gate, '='))
            gate.extend(parse('NOT = { AND = { tag = SOV has_focus_tree = SOV_focus } }'))
            blocked_events += 1
        write('events/' + name, doc)

    # Adapt advisors without duplicating commanders or replacing portraits.
    characters_doc = read(GAME / 'common/characters/SOV.txt')
    characters = one(characters_doc, 'characters')
    advisor_count = 0
    nkvd = {'SOV_genrikh_yagoda', 'SOV_nikolay_yezhov', 'SOV_lavrenty_beriya', 'SOV_vsevolod_merkulov'}
    for cid, character, op in characters:
        for advisor in values(character, 'advisor'):
            if cid in nkvd:
                field(advisor, 'visible', parse('always = no'))
                field(advisor, 'available', parse('always = no'))
                continue
            slot = one(advisor, 'slot')
            required = ('NWW_SOV_unified_command' if slot in ('army_chief', 'high_command')
                        else 'SOV_red_wings' if slot == 'air_chief'
                        else 'SOV_red_banner_fleet' if slot == 'navy_chief'
                        else 'SOV_the_new_constitution')
            field(advisor, 'visible', parse(f'has_focus_tree = SOV_focus {cid} = {{ NOT = {{ has_character_flag = SOV_exiled_flag }} }}'))
            field(advisor, 'available', parse(f'has_completed_focus = {required}'))
            advisor_count += 1
    write('common/characters/SOV.txt', characters_doc)
    write('common/country_leader/SOV_traits.txt', parse('''leader_traits = {
        NWW_SOV_general_secretary = { random = no political_power_gain = 0.10 }
    }'''))
    label('NWW_SOV_general_secretary', 'Генеральный секретарь восстановленной республики', 'General Secretary of the Reconstructed Republic')

    # Strip native initialization from history, retaining equipment and the map.
    history_path = ROOT / 'history/countries/SOV - Soviet union.txt'
    history = read(history_path)
    def clean(node):
        result = []
        for k, v, op in node:
            if k and (k.startswith('1939.') or k.startswith('SOV_paranoia') or k == 'SOV_remove_paranoia_effect'):
                continue
            if k in ('set_variable', 'add_to_variable', 'multiply_variable', 'subtract_from_variable', 'clamp_variable', 'set_temp_variable', 'add_to_array', 'clear_array'):
                names = [n for n, value, operator in v] if isinstance(v, list) else [v]
                if any(str(n).startswith('SOV_') for n in names):
                    continue
                if k == 'set_temp_variable' and names == ['i']:
                    continue
            if k == 'add_dynamic_modifier' and one(v, 'modifier', '').startswith('SOV_'):
                continue
            if k == 'country_event' and one(v, 'id', '').startswith(('NSB_', 'soviet.')):
                continue
            if k == 'set_country_flag' and ('paranoia' in v or 'purge' in v or v == 'SOV_TEST_REMOVE_VANILLA_ADVISORS_flag'):
                continue
            if k == 'set_character_flag' and any(s in v for s in ('purge', 'imprisoned', 'opposition')):
                continue
            if k == 'add_ideas':
                v = [(n, value, operator) for n, value, operator in v if value not in set(native_ids) | nkvd]
            elif isinstance(v, list):
                v = clean(v)
            if k == 'while_loop_effect' and not any(name in ('country_event', 'add_to_array', 'random_army_leader', 'random_navy_leader', 'add_ideas') for name, value, operator in walk(v)):
                continue
            if isinstance(v, list) and not v:
                continue
            result.append((k, v, op))
        return result
    history = clean(history)
    history = [(k, v, o) for k, v, o in history if k != 'nww_SOV_update_reconstruction' and k != 'nww_SOV_suspend_detached_purges']
    history += parse('nww_SOV_suspend_detached_purges = yes nww_SOV_update_reconstruction = yes')
    write('history/countries/SOV - Soviet union.txt', history)

    # Foreign demands resolve through recipient choices, not instant annexation.
    for target, key, fid, earliest in [('LTB', 'litbel', 'NWW_SOV_litbel_campaign', '1939.6.1'), ('MKN', 'steppe', 'NWW_SOV_steppe_campaign', '1940.1.1')]:
        guards = f'''tag = SOV has_focus_tree = SOV_focus is_subject = no has_government = communism
            has_completed_focus = NWW_SOV_civil_peace has_completed_focus = NWW_SOV_army_maneuvers
            date > {earliest} {target} = {{ exists = yes }} NOT = {{ is_ally_with = {target} }}
            NOT = {{ has_country_flag = NWW_SOV_{target}_settlement }} has_country_flag = NWW_SOV_{target}_rejected'''
        if target == 'MKN':
            guards += ' MKN = { NOT = { has_country_flag = MKN_equal_autonomy } }'
        effects += parse(f'''nww_SOV_prepare_{key}_campaign = {{ if = {{ limit = {{ {guards} }}
            {target} = {{ every_owned_state = {{ add_claim_by = SOV }} }}
            if = {{ limit = {{ NOT = {{ has_war_with = {target} }} NOT = {{ has_wargoal_against = {target} }} }}
                create_wargoal = {{ type = annex_everything target = {target} }} }} }} }}''')
    write('common/scripted_effects/SOV_effects.txt', effects)
    repair = parse('''if = { limit = { has_focus_tree = SOV_focus }
        nww_SOV_suspend_detached_purges = yes nww_SOV_update_reconstruction = yes
        if = { limit = { has_completed_focus = NWW_SOV_litbel_campaign } nww_SOV_prepare_litbel_campaign = yes }
        if = { limit = { has_completed_focus = NWW_SOV_steppe_campaign } nww_SOV_prepare_steppe_campaign = yes }
    }''')
    write('common/on_actions/SOV_on_actions.txt', [('on_actions', [
        ('on_startup', [('effect', [('SOV', repair, '=')], '=')], '='),
        ('on_daily_SOV', [('effect', repair, '=')], '=')], '=')])

    events = parse('add_namespace = nww_sov')
    def event(eid, ru, en, rd, ed, body):
        node = parse(f'''id = {eid} title = {eid}.t desc = {eid}.d
            picture = GFX_report_event_election_vote is_triggered_only = yes {body}''')
        if eid in ('nww_sov.10', 'nww_sov.20'):
            live = one(node, 'trigger')
            for index, option in enumerate(values(node, 'option')):
                metadata = [(k, v, o) for k, v, o in option if k in ('name', 'ai_chance')]
                actions = [(k, v, o) for k, v, o in option if k not in ('name', 'ai_chance')]
                if index == 0:
                    metadata.append(('trigger', copy.deepcopy(live), '='))
                metadata.append(('if', [('limit', copy.deepcopy(live), '=')] + actions, '='))
                option[:] = metadata
        events.append(('country_event', node, '='))
        label(eid + '.t', ru, en)
        label(eid + '.d', rd, ed)
    event('nww_sov.1', 'Республика после Смуты', 'The Republic after the Tumult',
          'Мировой войны не было, но мира оказалось недостаточно. Земельный кризис, продовольственные перебои и стачки разрушили империю в 1918–1922 годах. Советы удержали промышленные узлы, однако западные окраины стали независимыми, а украинская степь отвергла власть центра. Теперь республика должна согласовать полномочия, исправить хозяйственный план и превратить армию гражданской войны в регулярную. Только после этого Москва сможет предъявить новые требования соседям.',
          'There was no world war, yet peace was insufficient. Land disputes, food shortages and strikes broke the empire during 1918–1922. The soviets held the industrial centres, but the western borderlands became independent and the Ukrainian steppe rejected central authority. The republic must now settle powers, balance its economic plan and turn civil-war formations into a regular army before pressing new demands abroad.',
          'trigger = { tag = SOV has_focus_tree = SOV_focus } option = { name = nww_sov.1.a }')
    label('nww_sov.1.a', 'Построить государство, способное пережить революцию.', 'Build a state that can survive its revolution.')
    event('nww_sov.10', 'Советские требования к Союзу', 'Soviet Demands to the Union',
          'Москва требует военного доступа и гарантий нейтралитета Литовско-Белорусского Союза. Согласие сохранит наше правительство и границы, но даст советским войскам доступ. Отказ позволит Москве открыть военную кампанию после необходимой подготовки. Компромисс между народами Союза остаётся нашим внутренним делом.',
          'Moscow demands military access and neutrality guarantees from the Lithuanian Belarusian Union. Acceptance preserves our government and borders but admits Soviet forces. Refusal permits a prepared Soviet campaign. Our internal federal compromise remains our own affair.', '''
          trigger = { tag = LTB exists = yes is_subject = no SOV = { exists = yes is_subject = no }
              NOT = { has_war_with = SOV } NOT = { is_ally_with = SOV } }
          option = { name = nww_sov.10.a ai_chance = { factor = 5 modifier = { factor = 8 has_government = communism } }
              set_country_flag = NWW_SOV_LTB_settlement give_military_access = SOV
              diplomatic_relation = { country = SOV relation = non_aggression_pact active = yes }
              SOV = { set_country_flag = NWW_SOV_LTB_settlement clr_country_flag = NWW_SOV_LTB_rejected } }
          option = { name = nww_sov.10.b ai_chance = { factor = 95 }
              add_war_support = 0.05 SOV = { set_country_flag = NWW_SOV_LTB_rejected }
              diplomatic_relation = { country = SOV relation = non_aggression_pact active = no } }
          ''')
    label('nww_sov.10.a', 'Принять гарантии, сохранив самостоятельность.', 'Accept the guarantees and retain independence.')
    label('nww_sov.10.b', 'Союз сам определяет свою политику.', 'The Union determines its own policy.')
    event('nww_sov.20', 'Предложение Москве и вольной степи', 'Moscow and the Free Steppe',
          'Советская делегация предлагает обмен оборудованием и зерном, доступ к техническим разработкам и договор о ненападении. Протокол не меняет наше правительство и не превращает общины в советскую провинцию. Отказ оставит конфликт открытым; уже признанное равноправие и союз Москва не отменяет этим предложением.',
          'The Soviet delegation proposes machinery and grain exchange, access to technical work and a non-aggression pact. The protocol changes neither our government nor our sovereignty. Refusal leaves the dispute open; existing recognition and alliances are retained.', '''
          trigger = { tag = MKN exists = yes is_subject = no SOV = { exists = yes is_subject = no }
              NOT = { has_war_with = SOV } }
          option = { name = nww_sov.20.a ai_chance = { factor = 35 modifier = { factor = 4 has_government = communism } }
              set_country_flag = NWW_SOV_MKN_settlement add_ideas = NWW_SOV_steppe_exchange
              diplomatic_relation = { country = SOV relation = non_aggression_pact active = yes }
              SOV = { set_country_flag = NWW_SOV_MKN_settlement clr_country_flag = NWW_SOV_MKN_rejected add_ideas = NWW_SOV_steppe_exchange } }
          option = { name = nww_sov.20.b ai_chance = { factor = 65 }
              SOV = { set_country_flag = NWW_SOV_MKN_rejected } }
          ''')
    label('nww_sov.20.a', 'Сотрудничать на основе самостоятельности советов.', 'Cooperate while preserving independent councils.')
    label('nww_sov.20.b', 'Не связывать степь московским договором.', 'Do not bind the steppe to Moscow\'s agreement.')
    write('events/SOV_events.txt', events)

    order = ['SOV_the_revolution_endures', 'SOV_russian_socialism', 'SOV_the_new_constitution',
        'SOV_brotherhood_of_peoples', 'NWW_SOV_union_congress', 'NWW_SOV_party_coordination',
        'SOV_second_five_year_plan', 'NWW_SOV_industrial_survey', 'NWW_SOV_agricultural_credit',
        'SOV_magnitogorsk', 'SOV_urals_industry', 'SOV_deep_battle', 'NWW_SOV_unified_command',
        'SOV_workers_and_peasants_army', 'NWW_SOV_professional_officers', 'SOV_red_artillery',
        'NWW_SOV_field_radios', 'NWW_SOV_army_logistics', 'NWW_SOV_army_maneuvers',
        'NWW_SOV_budget_accountability', 'NWW_SOV_civil_peace', 'SOV_comintern_calls',
        'NWW_SOV_strategic_pause', 'NWW_SOV_frontier_review', 'NWW_SOV_western_command',
        'NWW_SOV_litbel_ultimatum', 'NWW_SOV_litbel_campaign', 'NWW_SOV_steppe_conference',
        'NWW_SOV_steppe_campaign', 'NWW_SOV_railway_bottlenecks', 'NWW_SOV_power_stations',
        'NWW_SOV_standardized_armaments', 'NWW_SOV_plan_fulfilled', 'NWW_SOV_scientific_network',
        'SOV_red_wings', 'SOV_red_banner_fleet']
    write('common/ai_strategy_plans/SOV_historical.txt', parse(f'''NWW_SOV_historical = {{
        name = "NWW Soviet Reconstruction" desc = "" allowed = {{ original_tag = SOV has_focus_tree = SOV_focus }}
        enable = {{ has_focus_tree = SOV_focus }} abort = {{ is_subject = yes }}
        ai_national_focuses = {{ {' '.join(order)} }} weight = {{ factor = 100 }}
        focus_factors = {{ NWW_SOV_republican_charters = 0 }} }}'''))
    strategies = []
    peace = []
    for target, key, fid in [('LTB', 'litbel', 'NWW_SOV_litbel_campaign'), ('MKN', 'steppe', 'NWW_SOV_steppe_campaign')]:
        extra = 'MKN = { NOT = { has_country_flag = MKN_equal_autonomy } }' if target == 'MKN' else ''
        strategies += parse(f'''NWW_SOV_{key}_attack = {{ enable = {{ tag = SOV has_focus_tree = SOV_focus
            is_subject = no has_completed_focus = {fid} {target} = {{ exists = yes }}
            NOT = {{ is_ally_with = {target} }} NOT = {{ has_war_with = {target} }} {extra}
            NOT = {{ has_country_flag = NWW_SOV_{target}_settlement }}
            has_wargoal_against = {target} can_declare_war_on = {target} }} abort_when_not_enabled = yes
            ai_strategy = {{ type = prepare_for_war id = {target} value = 200 }}
            ai_strategy = {{ type = declare_war id = {target} value = 300 }}
            ai_strategy = {{ type = conquer id = {target} value = 300 }} }}''')
        peace += parse(f'''NWW_SOV_{key}_peace = {{ peace_action_type = take_states
            enable = {{ ROOT = {{ tag = SOV has_completed_focus = {fid} }} FROM = {{ tag = SOV }}
                FROM.FROM = {{ original_tag = {target} }} }} ai_desire = 300 }}''')
        earliest = '1939.6.2' if target == 'LTB' else '1940.1.2'
        autonomy = 'MKN = { has_country_flag = MKN_equal_autonomy }' if target == 'MKN' else ''
        strategies += parse(f'''NWW_SOV_{key}_restraint = {{
            enable = {{ tag = SOV has_focus_tree = SOV_focus {target} = {{ exists = yes }}
                OR = {{ date < {earliest} is_ally_with = {target}
                    has_country_flag = NWW_SOV_{target}_settlement {autonomy} }} }}
            abort_when_not_enabled = yes
            ai_strategy = {{ type = declare_war id = {target} value = -1000 }}
        }}''')
    write('common/ai_strategy/SOV_campaigns.txt', strategies)
    write('common/peace_conference/ai_peace/SOV_peace.txt', [('peace_ai_desires', peace, '=')])

    label('NWW_SOV_doctrine_bonus', 'Советская программа доктрин', 'Soviet Doctrine Programme')
    label('NWW_SOV_reconstruction_ready_tt', 'Согласован союзный договор, развиты Магнитогорск и Урал, подготовлен профессиональный офицерский корпус.', 'The Union Treaty, Magnitogorsk, Ural industry and professional officer corps are ready.')
    label('NWW_SOV_campaign_ready_tt', 'Завершены гражданское урегулирование и общевойсковые манёвры.', 'The civil settlement and combined arms manoeuvres are complete.')
    label('NWW_SOV_LTB_rejected', 'Союз отклонил советские требования', 'The Union rejected Soviet demands')
    label('NWW_SOV_MKN_rejected', 'Махновский съезд отклонил хозяйственный протокол', 'The Makhnovist Congress rejected the economic protocol')
    label('NWW_SOV_LTB_settlement', 'Заключено мирное урегулирование с Союзом', 'A peaceful settlement with the Union is in force')
    label('NWW_SOV_MKN_settlement', 'Заключён Гуляйпольский хозяйственный протокол', 'The Huliaipole economic protocol is in force')
    label('NWW_SOV_litbel_war_tt', 'Получить претензии и бессрочную цель войны против Литвы-Беларуси после её отказа. Мирное согласие и действующий союз исключают награду.', 'Gain claims and a permanent war goal against Lithuania-Belarus after its refusal. A peaceful settlement or alliance prevents the reward.')
    label('NWW_SOV_steppe_war_tt', 'Получить претензии и бессрочную цель войны против Махновщины после отказа, с 1940 года. Признанное равноправие и союз исключают награду.', 'Gain claims and a permanent war goal against Makhnovshchina after refusal, from 1940. Recognized autonomy and an alliance prevent the reward.')
    for lang, index in [('russian', 0), ('english', 1)]:
        path = ROOT / f'localisation/replace/SOV_l_{lang}.yml'
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text('\n'.join([f'l_{lang}:'] + [f' {key}:0 "{entry[index]}"' for key, entry in LABELS.items()]) + '\n', encoding='utf-8-sig', newline='\n')
        FILES.append(str(path.relative_to(ROOT)).replace('\\', '/'))
    assert set(LEGACY) <= by_id.keys()
    duration = sum(int(one(by_id[fid], 'cost')) * 7 for fid in order[:order.index('NWW_SOV_litbel_campaign') + 1])
    report = {'focus_count': len(by_id), 'focus_ids': list(by_id), 'preserved_focus_ids': LEGACY,
              'native_spirits': native_ids, 'native_dynamic_modifiers': dynamic_ids,
              'blocked_native_events': blocked_events, 'adapted_advisors': advisor_count,
              'inactive_native_decisions': [k for k, v, o in inactive_decisions], 'inactive_native_missions': mission_ids,
              'stage_milestones': STAGES, 'historical_first_campaign_focus_days': duration,
              'uninterrupted_historical_war_goal_date': str(date(1936, 1, 1) + timedelta(days=duration)),
              'native_idea_source_missing_closures': missing, 'files': sorted(set(FILES))}
    (ROOT / 'docs/SOV_overhaul.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(f'SOV: {len(by_id)} focuses; all14 NWW IDs retained; {len(native_ids)} native spirits/{len(dynamic_ids)} modifiers replaced; {blocked_events} guarded events.')
    print('Historical first war-goal route:', report['uninterrupted_historical_war_goal_date'])


if __name__ == '__main__':
    main()
