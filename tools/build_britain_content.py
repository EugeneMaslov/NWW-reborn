"""Build the country-owned ENG package. Run from the repository root.

The manifest is deliberately explicit: focus IDs, rewards and map coordinates
are reviewable here; the emitted game files are committed alongside it.
Native compatibility collects direct focus definitions only.
"""
from pathlib import Path
import json
import re
from hoi4_script import read, one, values, quoted

ROOT = Path(__file__).resolve().parents[1]
GAME = Path('D:/Steam/steamapps/common/Hearts of Iron IV')
P = 'ENG_nww_'
LOCS = {'russian': {}, 'english': {}}
FOCI = []


def write(path, text):
    # HOI4 scripted effects are invoked with = yes. Unlike scripted localization,
    # they do not accept arbitrary AMOUNT blocks: those truncate the native tree.
    text = re.sub(r'(ENG_nww_(?:trust_all|build_\w+))\s*=\s*\{\s*AMOUNT\s*=\s*(-?\d+)\s*\}',
                  lambda m: m[1]+'_'+m[2].replace('-','minus')+' = yes', text)
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text('\n'.join(line.rstrip() for line in text.rstrip().splitlines()) + '\n', encoding='utf-8', newline='\n')


def loc(key, ru, en):
    LOCS['russian'][key] = ru
    LOCS['english'][key] = en
    return key


def focus(key, ru, en, x, y, parent=None, effect='', mods=None,
          available='', exclusive=(), cost=10, group='state', desc=None):
    fid = P + key
    loc(fid, ru, en)
    flavour = {
        'state': ('Устройство власти определит, какие обещания Лондон способен исполнить. Реформа должна опираться на согласованные полномочия и устойчивые учреждения.',
                  'The settlement of power determines which promises London can honour. Reform needs agreed powers and durable institutions.'),
        'economy': ('Защищённые рынки десятилетиями поддерживали наши предприятия. Новая программа потребует оборудования, энергии и труда, чтобы британская промышленность вновь выдерживала мировую конкуренцию.',
                    'Protected markets have sustained our firms for decades. Equipment, energy and labour must now restore their ability to compete.'),
        'science': ('Исследования требуют постоянных вложений и обмена знаниями. Государственное финансирование даст лабораториям время довести работу до практического результата.',
                    'Research needs sustained investment and shared knowledge. Public funding gives laboratories time to turn their work into practical results.'),
        'army': ('Наши офицеры знают дальние гарнизоны и ограниченные экспедиции. Новую армию предстоит подготовить учениями, снабжением и ясным представлением о будущей войне.',
                 'Our officers know distant garrisons and limited expeditions. Exercises, logistics and a clear purpose must prepare the next army.'),
        'air': ('Самостоятельная воздушная служба выросла из наблюдательных, почтовых и колониальных подразделений. Её дальнейшее развитие зависит от подготовленных экипажей и согласованной системы управления.',
                'The independent air service grew from observation, mail and colonial units. Its future depends on trained crews and coordinated command.'),
        'navy': ('Морское могущество измеряется готовностью кораблей и доступностью баз. Адмиралтейство должно соотнести глобальные обязательства с силами, которые действительно может отправить в море.',
                 'Sea power rests on ready ships and accessible bases. The Admiralty must match global commitments to forces it can actually deploy.'),
    }
    loc(fid + '_desc', *(desc or flavour[group]))
    FOCI.append(dict(id=fid, key=key, x=x, y=y, parent=parent,
                     effect=effect, mods=mods or {}, available=available,
                     exclusive=list(exclusive), cost=cost, group=group))
    return key


def chain(rows, x, start, parent=None, group='state', gate=''):
    for i, row in enumerate(rows):
        key, ru, en, effect, mods = row
        focus(key, ru, en, x, start+i, parent, effect, mods,
              available=gate if i == 0 else '', group=group)
        parent = key
    return parent


def build(kind, n=1):
    return f'ENG_nww_build_{kind} = {{ AMOUNT = {n} }}'


def bonus(category, name, uses=1):
    return f'add_tech_bonus = {{ name = {P+name} bonus = 0.5 uses = {uses} category = {category} }}'


def m(group, key, amount):
    return {group + ':' + key: amount}


def content():
    focus('report', 'Доклад о состоянии Империи', 'The State of the Empire', 0, 0,
          effect='add_political_power = 35', cost=5,
          desc=('Июльский кризис 1914 года завершился переговорами. Британская империя сохранила флот, рынки и престиж, но избежавшая мировой войны Европа продолжала меняться. Доклад кабинету должен показать цену каждого обязательства.',
                'The July Crisis of 1914 ended at the negotiating table. Britain retained her fleet, markets and prestige, but Europe kept changing. The cabinet must learn the price of every commitment.'))
    focus('session', 'Открыть парламентскую сессию', 'Open the Parliamentary Session', 0, 1, 'report',
          'add_political_power = 35', cost=5)
    focus('budget', 'Бюджет короны и обязательств', 'The Crown and Commitments Budget', 0, 2, 'session',
          'country_event = { id = nww_eng.1 days = 1 }', cost=5)
    roots = ['continuity', 'federal', 'emergency', 'labour', 'island']
    titles = [('Конституционная преемственность','Constitutional Continuity'),
              ('Разделить имперский суверенитет','Share Imperial Sovereignty'),
              ('Комитет национального восстановления','National Recovery Committee'),
              ('Мандат трудящейся Британии','A Mandate for Working Britain'),
              ('Остров прежде Империи','The Island before the Empire')]
    for key, names, x in zip(roots, titles, [-16,-8,0,8,16]):
        effect = 'add_political_power = 50'
        if key == 'labour': effect += ' set_country_flag = ENG_nww_labour_campaign'
        focus(key, *names, x, 4, 'budget', effect,
              exclusive=[k for k in roots if k != key], cost=5)
    chain([
        ('majority','Кабинет ответственного большинства','A Responsible Majority','add_stability = 0.05',m('state','political_power_factor',0.05)),
        ('civil_service','Обновить колониальную службу','Reform the Colonial Service','add_political_power = 50',{}),
        ('premiers','Совет премьер-министров','Council of Prime Ministers','set_country_flag = ENG_nww_conferences_unlocked',{}),
        ('local_parliaments','Гарантии местных парламентов','Guarantees for Local Parliaments','ENG_nww_trust_all = { AMOUNT = 10 }',{}),
        ('commonwealth_budget','Совместные оборонные сметы','Joint Defence Estimates','navy_experience = 20',m('state','political_power_factor',0.05)),
        ('commonwealth_charter','Хартия Содружества','The Commonwealth Charter','set_country_flag = ENG_nww_commonwealth_settlement',m('state','stability_factor',0.05)),
        ('cabinet_accountability','Ответственность кабинета','Cabinet Accountability','add_political_power = 75',m('state','political_power_factor',0.05)),
        ('treaty_diplomacy','Договорная дипломатия','Diplomacy by Treaty','set_country_flag = ENG_nww_diplomacy_unlocked',{}),
        ('constitutional_crown','Корона конституционного согласия','A Crown of Constitutional Consent','add_stability = 0.05',m('state','stability_factor',0.05)),
    ], -16, 5, 'continuity')
    chain([
        ('conference','Созвать Имперскую конференцию','Convene the Imperial Conference','set_country_flag = ENG_nww_conferences_unlocked',{}),
        ('federal_defence','Разделить оборонные обязательства','Share Defence Obligations','navy_experience = 20',{}),
        ('federal_budget','Согласовать федеральный бюджет','Agree the Federal Budget','add_political_power = 50',m('state','political_power_factor',0.05)),
        ('representation','Хартия представительства','Charter of Representation','ENG_nww_trust_all = { AMOUNT = 10 }',{}),
        ('two_chambers','Две палаты союза','Two Chambers of the Union','add_stability = 0.05',{}),
        ('ratification','Вынести договор на ратификацию','Submit the Treaty for Ratification','set_country_flag = ENG_nww_ratification_unlocked',{}),
        ('federal_parliament','Открыть Имперский парламент','Open the Imperial Parliament','set_country_flag = ENG_nww_federation_settlement',m('state','stability_factor',0.10)),
        ('federal_treasury','Федеральное казначейство','Federal Treasury','add_political_power = 75',m('state','political_power_factor',0.10)),
        ('federal_command','Общий совет обороны','Federal Defence Council','army_experience = 25 air_experience = 25 navy_experience = 25',{}),
        ('equal_union','Союз равных парламентов','A Union of Equal Parliaments','ENG_nww_trust_all = { AMOUNT = 10 }',m('state','stability_factor',0.05)),
    ], -8, 5, 'federal')
    FOCI[-4]['available'] = 'date > 1938.1.1 check_variable = { var = ENG_nww_federal_count value = 2 compare = greater_than_or_equals }'
    chain([
        ('emergency_powers','Чрезвычайные полномочия кабинета','Emergency Cabinet Powers','add_political_power = 50 add_stability = -0.05',{}),
        ('national_press','Национальная печать','The National Press','set_country_flag = ENG_nww_right_campaign',{}),
        ('officers_council','Поддержка командования','Support of the High Command','add_command_power = 20',{}),
    ], 0, 5, 'emergency')
    focus('blackshirts','Британский союз фашистов','British Union of Fascists',-2,8,'officers_council',
          'ENG_nww_fascist_transition = yes',available='NOT = { fascism < 0.40 }',exclusive=['directory'])
    focus('directory','Консервативная директория','Conservative Directorate',2,8,'officers_council',
          'ENG_nww_directory_transition = yes',available='NOT = { neutrality < 0.40 }',exclusive=['blackshirts'])
    chain([
        ('corporate_chambers','Корпоративные палаты','Corporate Chambers','add_political_power = 50',m('state','political_power_factor',0.10)),
        ('party_police','Государственная милиция','State Militia','add_stability = -0.05',m('state','stability_factor',0.05)),
        ('labour_charter','Государственная хартия труда','State Labour Charter','remove_ideas = ENG_nww_strikes',m('economy','industrial_capacity_factory',0.05)),
        ('imperial_discipline','Имперская дисциплина','Imperial Discipline','set_country_flag = ENG_nww_coercive_settlement',m('state','political_power_factor',0.05)),
    ], -2, 9, 'blackshirts')
    chain([
        ('defence_council','Совет национальной обороны','Council of National Defence','add_command_power = 25',m('state','political_power_factor',0.10)),
        ('administrative_order','Приказ и администрация','Order and Administration','add_stability = 0.05',{}),
        ('labour_arbitration','Обязательный трудовой арбитраж','Compulsory Labour Arbitration','remove_ideas = ENG_nww_strikes',m('economy','production_factory_efficiency_gain_factor',0.05)),
        ('crown_directory','Корона и директория','The Crown and the Directorate','set_country_flag = ENG_nww_coercive_settlement',m('state','stability_factor',0.05)),
    ], 2, 9, 'directory')
    chain([
        ('public_works','Программа общественных работ','Public Works Programme',build('civilian'),{}),
        ('union_agreement','Соглашение с профсоюзами','Agreement with the Trade Unions','remove_ideas = ENG_nww_strikes add_stability = 0.05',{}),
        ('labour_election','Парламентский мандат реформ','A Parliamentary Mandate for Reform','ENG_nww_labour_transition = yes',m('state','political_power_factor',0.05)),
        ('public_energy','Национальная энергетическая программа','National Energy Programme','',m('economy','energy_gain_factor',0.10)),
        ('public_railways','Общественные железные дороги','Public Railways',build('infrastructure',2),{}),
        ('colonial_review','Пересмотреть колониальный договор','Review the Colonial Treaty','set_country_flag = ENG_nww_decolonisation_unlocked',{}),
    ],8,5,'labour')
    FOCI[-4]['available'] = 'check_variable = { var = ENG_nww_labour_mandate value = 40 compare = greater_than_or_equals } NOT = { democratic < 0.40 }'
    focus('parliamentary_socialism','Парламентский социализм','Parliamentary Socialism',6,11,'colonial_review',
          'set_country_flag = ENG_nww_social_settlement add_stability = 0.05',exclusive=['social_republic'])
    focus('social_republic','Социалистическая республика','Socialist Republic',10,11,'colonial_review',
          'ENG_nww_socialist_transition = yes',available='NOT = { communism < 0.40 }',exclusive=['parliamentary_socialism'])
    for x, parent, suffix in [(6,'parliamentary_socialism','parliament'),(10,'social_republic','republic')]:
        chain([
            ('housing_'+suffix,'Достойное жильё','Decent Housing',build('civilian'),m('state','stability_factor',0.05)),
            ('welfare_'+suffix,'Гарантии социального государства','Guarantees of the Welfare State','add_stability = 0.05',m('state','political_power_factor',0.05)),
        ],x,12,parent)
    chain([
        ('price_presence','Цена мирового присутствия','The Price of Global Presence','add_political_power = 50',{}),
        ('regional_defence','Передать региональную оборону','Devolve Regional Defence','ENG_nww_trust_all = { AMOUNT = -5 }',{}),
        ('island_treaties','Договоры вместо гарнизонов','Treaties instead of Garrisons','set_country_flag = ENG_nww_decolonisation_unlocked',{}),
        ('home_ports','Порты метрополии','Home Ports',build('dockyard'),{}),
        ('coastal_watch','Береговая стража','Coastal Watch','air_experience = 20',m('air','air_intercept_efficiency',0.10)),
        ('island_fortress','Крепость Британских островов','Fortress Britain','set_country_flag = ENG_nww_island_settlement',m('state','political_power_factor',0.10)),
        ('island_housing','Средства для британских городов','Funds for British Cities',build('civilian',2),{}),
        ('armed_neutrality','Вооружённый нейтралитет','Armed Neutrality','add_war_support = 0.05 if = { limit = { is_in_faction = yes } remove_from_faction = ENG }',m('army','army_core_defence_factor',0.10)),
        ('home_charter','Хартия островного государства','Charter of the Island State','add_stability = 0.05',m('state','stability_factor',0.05)),
    ],16,5,'island')
    FOCI[-2]['available'] = 'has_war = no NOT = { any_subject_country = { exists = yes } }'
    focus('irish_report','Незавершённый ирландский договор','The Unfinished Irish Treaty',24,0,
          effect='set_country_flag = ENG_nww_irish_unlocked',cost=5,
          desc=('Независимость Ирландии стала итогом довоенного конституционного противостояния. В Ольстере сохраняются британская администрация и соперничающие национальные проекты. Пограничные инциденты угрожают обоим правительствам.',
                'Irish independence followed a pre-war constitutional struggle. British administration and rival national projects coexist in Ulster. Border incidents threaten both governments.'))
    chain([
        ('border_inquiry','Расследовать пограничные инциденты','Investigate the Border Incidents','add_to_variable = { ENG_nww_irish_pressure = -10 }',{}),
        ('irish_talks','Открыть переговоры с Дублином','Open Talks with Dublin','set_country_flag = ENG_nww_irish_talks_ready',{}),
    ],24,1,'irish_report')
    focus('belfast','Белфастское соглашение','The Belfast Agreement',22,3,'irish_talks',
          'country_event = { id = nww_eng.20 days = 1 }',exclusive=['irish_emergency'])
    focus('irish_emergency','Чрезвычайная администрация Ольстера','Emergency Administration in Ulster',26,3,'irish_talks',
          'set_country_flag = ENG_nww_irish_coercion add_to_variable = { ENG_nww_irish_pressure = -10 } add_timed_idea = { idea = ENG_nww_ulster_garrison days = 365 }',exclusive=['belfast'])
    chain([
        ('community_rights','Гарантии обеим общинам','Guarantees for Both Communities','add_stability = 0.05',{}),
        ('irish_commission','Совместная пограничная комиссия','Joint Border Commission','set_country_flag = ENG_nww_irish_final',m('state','stability_factor',0.05)),
    ],22,4,'belfast',gate='has_country_flag = ENG_nww_irish_agreement')
    chain([
        ('ulster_police','Реформа ольстерской полиции','Reform the Ulster Police','add_to_variable = { ENG_nww_irish_pressure = -15 }',{}),
        ('ulster_review','Возвращение к гражданской власти','Return to Civilian Government','clr_country_flag = ENG_nww_irish_coercion remove_ideas = ENG_nww_ulster_garrison set_country_flag = ENG_nww_irish_talks_ready',{}),
    ],26,4,'irish_emergency')
    focus('irish_future','Договор о будущем острова','A Treaty on the Future of the Island',24,7,
          effect='set_country_flag = ENG_nww_border_vote_unlocked',
          available='has_country_flag = ENG_nww_irish_agreement has_completed_focus = ENG_nww_budget')
    # Civil industry, war industry and science are independent, country-owned branches.
    chain([
        ('industrial_survey','Обследование старых предприятий','Survey the Old Industries','add_political_power = 35',{}),
        ('coalfields','Обновить угольные бассейны','Modernise the Coalfields','ENG_nww_coal_project = yes',{}),
        ('machine_tools','Новые станки Мидлендса','New Machine Tools for the Midlands','',m('economy','production_factory_efficiency_gain_factor',0.05)),
        ('electric_grid','Объединить электрические сети','Connect the Electricity Grid','',m('economy','energy_gain_factor',0.10)),
        ('northern_cities','Возрождение северных городов','Revive the Northern Cities',build('civilian',2),{}),
        ('freight_routes','Грузовые магистрали','Freight Corridors',build('infrastructure',2),{}),
        ('industrial_standards','Общие промышленные стандарты','Common Industrial Standards','',m('economy','production_speed_buildings_factor',0.05)),
    ],34,0,group='economy')
    focus('free_trade','Имперская зона свободной торговли','Imperial Free Trade Area',32,7,'industrial_standards',
          'set_country_flag = ENG_nww_trade_unlocked',m('economy','industrial_capacity_factory',0.05),exclusive=['protection'],group='economy')
    focus('protection','Защищённый британский рынок','A Protected British Market',36,7,'industrial_standards',
          'ENG_nww_trust_all = { AMOUNT = -5 }',m('economy','production_factory_max_efficiency_factor',0.10),exclusive=['free_trade'],group='economy')
    chain([
        ('civil_reconstruction','Завершить промышленную реконструкцию','Complete Industrial Reconstruction',build('civilian'),m('economy','production_speed_buildings_factor',0.05)),
        ('imperial_investment','Имперский инвестиционный банк','Imperial Investment Bank','set_country_flag = ENG_nww_investment_unlocked',{}),
        ('canadian_corridors','Канадские транспортные коридоры','Canadian Transport Corridors','ENG_nww_offer_canadian_project = yes',{}),
        ('indian_electricity','Индийская электрификация','Indian Electrification','ENG_nww_offer_indian_project = yes',{}),
        ('commercial_ports','Порты мировой торговли','Ports of World Trade',build('dockyard'),{}),
    ],34,9,group='economy',gate='OR = { has_completed_focus = ENG_nww_free_trade has_completed_focus = ENG_nww_protection }')
    chain([
        ('armament_board','Совет военных заказов','Armaments Board','add_political_power = 35',{}),
        ('ordnance','Предприятия Royal Ordnance','Royal Ordnance Factories',build('military'),{}),
        ('steel_contracts','Стальные контракты','Steel Contracts','ENG_nww_steel_project = yes',{}),
        ('admiralty_yards','Верфи Адмиралтейства','Admiralty Shipyards',build('dockyard',2),{}),
        ('shadow_factories','Резервные авиационные заводы','Reserve Aircraft Factories',build('military'),{}),
        ('engine_plants','Авиационное моторостроение','Aircraft Engine Plants',bonus('air_equipment','engine_plants'),{}),
    ],40,0,group='economy')
    focus('quality','Стандарты качественного вооружения','Quality Armament Standards',38,6,'engine_plants',
          'set_country_flag = ENG_nww_quality_program',m('economy','production_factory_max_efficiency_factor',0.05),exclusive=['mass_contracts'],group='economy')
    focus('mass_contracts','Мобилизационные контракты','Mobilisation Contracts',42,6,'engine_plants',
          'add_timed_idea = { idea = ENG_nww_retooling days = 180 }',m('economy','industrial_capacity_factory',0.10),exclusive=['quality'],group='economy')
    chain([
        ('vickers','Опытные мастерские Vickers-Armstrong','Vickers-Armstrong Workshops',bonus('armor','vickers'),{}),
        ('standard_ammunition','Стандартизация боеприпасов','Standardise Ammunition','',m('economy','production_factory_efficiency_gain_factor',0.05)),
        ('production_inspection','Военная приёмка','Military Acceptance Boards','',m('economy','production_factory_max_efficiency_factor',0.05)),
        ('strategic_reserves','Стратегические производственные резервы','Strategic Production Reserves',build('military'),{}),
    ],40,8,group='economy',gate='OR = { has_completed_focus = ENG_nww_quality has_completed_focus = ENG_nww_mass_contracts }')
    chain([
        ('university_grants','Университетские гранты','University Grants',bonus('electronics','university_grants'),{}),
        ('research_council','Национальный научный совет','National Research Council','',m('science','research_speed_factor',0.05)),
        ('scientific_exchange','Имперский научный совет','Imperial Scientific Council','set_country_flag = ENG_nww_science_unlocked add_to_tech_sharing_group = ENG_nww_research',{}),
        ('radar_network','Цепь прибрежного обнаружения','The Coastal Detection Chain','ENG_nww_radar_project = yes',{}),
        ('computing','Вычислительные лаборатории','Computing Laboratories',bonus('electronics','computing'),{}),
        ('research_capacity','Расширить исследовательские институты','Expand the Research Institutes','add_research_slot = 1',{}),
        ('jet_research','Газотурбинная программа','Gas Turbine Programme','add_breakthrough_progress = { specialization = specialization_air value = 0.25 }',{}),
        ('closed_laboratories','Закрытые исследовательские центры','Restricted Research Centres','ENG_nww_research_facility = yes',{}),
        ('nuclear_committee','Комитет ядерных исследований','Nuclear Research Committee',bonus('nuclear','nuclear_committee'),{}),
        ('scientific_service','Государственная научная служба','Public Scientific Service','',m('science','research_speed_factor',0.05)),
    ],46,0,group='science')
    FOCI[-5]['available'] = 'date > 1938.1.1 amount_research_slots < 6'
    FOCI[-2]['available'] = 'date > 1940.1.1'
    chain([
        ('naval_review','Проверка готовности флота','Review Fleet Readiness','navy_experience = 25',{}),
        ('repair_bases','Обновить ремонтные базы','Modernise Repair Bases',build('dockyard'),{}),
        ('naval_planning','Объединённое морское планирование','Joint Naval Planning','set_country_flag = ENG_nww_routes_unlocked',{}),
    ],54,0,group='navy')
    focus('escort','Щит торговых путей','Shield of the Trade Routes',52,3,'naval_planning',
          'navy_experience = 20',m('navy','convoy_escort_efficiency',0.10),exclusive=['strike'],group='navy')
    focus('strike','Сосредоточенный морской удар','Concentrated Naval Strike',56,3,'naval_planning',
          'navy_experience = 20',m('navy','navy_capital_ship_attack_factor',0.10),exclusive=['escort'],group='navy')
    chain([
        ('escort_groups','Постоянные эскортные группы','Permanent Escort Groups','',m('navy','naval_detection',0.10)),
        ('asw_schools','Школы противолодочной борьбы','Anti-Submarine Schools',bonus('dd_tech','asw_schools'),{}),
        ('convoy_reserve','Транспортный резерв','Convoy Reserve','add_equipment_to_stockpile = { type = convoy amount = 50 producer = ENG }',{}),
        ('ocean_watch','Океанская охрана','Ocean Watch','',m('navy','convoy_escort_efficiency',0.10)),
    ],52,4,'escort',group='navy')
    chain([
        ('carrier_operations','Опыт палубных операций','Carrier Operations',bonus('cv_tech','carrier_operations'),{}),
        ('carrier_airgroups','Обновить авиагруппы','Modernise Carrier Air Groups',bonus('naval_air','carrier_airgroups'),{}),
        ('ocean_carrier','Авианосец океанской службы','Ocean Service Carrier',bonus('cv_tech','ocean_carrier'),{}),
        ('naval_strike_control','Управление морским ударом','Naval Strike Control','',m('navy','navy_capital_ship_attack_factor',0.05)),
    ],56,4,'strike',group='navy')
    chain([
        ('cape_route','Запасной маршрут вокруг Африки','The Cape Alternative','set_country_flag = ENG_nww_cape_ready',{}),
        ('naval_supply','Служба флотского снабжения','Fleet Supply Service','navy_experience = 25',{}),
        ('two_ocean_fleet','Обязательства двух океанов','Two-Ocean Commitments','',m('navy','industrial_capacity_dockyard',0.10)),
    ],54,9,group='navy',gate='OR = { has_completed_focus = ENG_nww_ocean_watch has_completed_focus = ENG_nww_naval_strike_control }')
    chain([
        ('air_service','Устав Королевских ВВС','Royal Air Force Charter','air_experience = 25',{}),
        ('pilot_reserve','Резерв лётных экипажей','Aircrew Reserve','air_experience = 25',{}),
    ],62,0,group='air')
    focus('fighter_command','Истребительное командование','Fighter Command',60,2,'pilot_reserve',
          '',m('air','air_intercept_efficiency',0.10),exclusive=['bomber_command'],group='air')
    focus('bomber_command','Бомбардировочное командование','Bomber Command',64,2,'pilot_reserve',
          '',m('air','air_strategic_bomber_bombing_factor',0.10),exclusive=['fighter_command'],group='air')
    chain([
        ('sector_hq','Секторные штабы','Sector Headquarters','',m('air','air_mission_efficiency',0.05)),
        ('supermarine','Программа Supermarine','Supermarine Programme',bonus('light_fighter','supermarine'),{}),
        ('home_air_shield','Воздушный щит метрополии','Home Air Shield','',m('air','air_intercept_efficiency',0.10)),
    ],60,3,'fighter_command',group='air')
    chain([
        ('navigation','Дальняя навигация','Long-Range Navigation','',m('air','air_mission_efficiency',0.05)),
        ('heavy_airgroups','Тяжёлые авиагруппы','Heavy Bomber Groups',bonus('cat_strategic_bomber','heavy_airgroups'),{}),
        ('strategic_campaign','План воздушной кампании','Strategic Air Campaign','',m('air','air_strategic_bomber_bombing_factor',0.10)),
    ],64,3,'bomber_command',group='air')
    chain([
        ('coastal_command','Береговое командование','Coastal Command',bonus('naval_air','coastal_command'),{}),
        ('fairey','Морская авиация Fairey','Fairey Naval Aviation','air_experience = 25',{}),
        ('air_ground_liaison','Армейские авианаводчики','Army Air Liaison','',m('air','air_cas_efficiency',0.10)),
        ('air_logistics','Передовые аэродромы','Forward Airfields',build('airbase',2),{}),
    ],62,7,group='air',gate='OR = { has_completed_focus = ENG_nww_home_air_shield has_completed_focus = ENG_nww_strategic_campaign }')
    chain([
        ('army_review','Инспекция Британской армии','Inspect the British Army','army_experience = 25',{}),
        ('staff_college','Штабной колледж','Staff College','army_experience = 25',m('army','planning_speed',0.10)),
    ],70,0,group='army')
    focus('expeditionary','Профессиональная экспедиционная армия','Professional Expeditionary Army',68,2,'staff_college',
          '',m('army','army_org_factor',0.05),exclusive=['continental'],group='army')
    focus('continental','Континентальная механизированная армия','Continental Mechanised Army',72,2,'staff_college',
          'add_war_support = 0.05',m('army','army_org_factor',0.05),exclusive=['expeditionary'],group='army')
    chain([
        ('overseas_supply','Снабжение дальних гарнизонов','Overseas Supply','',m('army','supply_consumption_factor',-0.10)),
        ('expedition_engineers','Экспедиционные инженеры','Expeditionary Engineers',bonus('support_tech','expedition_engineers'),{}),
        ('professional_rotations','Ротация кадровых частей','Professional Rotations','',m('army','army_org_regain',0.10)),
        ('rapid_expedition','Силы быстрого развёртывания','Rapid Deployment Force','',m('army','army_speed_factor',0.05)),
    ],68,3,'expeditionary',group='army')
    chain([
        ('reserve_act','Закон о подготовленном резерве','Trained Reserve Act','add_war_support = 0.05',m('army','training_time_army_factor',-0.10)),
        ('tank_trials','Испытания бронетанковых соединений','Armoured Formation Trials',bonus('armor','tank_trials'),{}),
        ('combined_arms','Взаимодействие родов войск','Combined Arms','',m('army','max_planning',0.10)),
        ('mechanised_logistics','Механизированное снабжение','Mechanised Logistics','',m('army','army_speed_factor',0.05)),
    ],72,3,'continental',group='army')
    chain([
        ('army_signals','Общая система армейской связи','Army Signals System',bonus('support_tech','army_signals'),{}),
        ('artillery_board','Артиллерийский комитет','Artillery Board',bonus('artillery','artillery_board'),{}),
        ('army_exercises','Большие штабные учения','Large Staff Exercises','army_experience = 40',{}),
        ('army_readiness','Армия нового десятилетия','Army of the New Decade','',m('army','army_org_factor',0.05)),
    ],70,8,group='army',gate='OR = { has_completed_focus = ENG_nww_rapid_expedition has_completed_focus = ENG_nww_mechanised_logistics }')
    # Administrative work takes 35 days; material programmes and constitutional
    # settlements take 70. Negotiation decisions have their own paid clock.
    short={
        'civil_service','premiers','local_parliaments','commonwealth_budget',
        'cabinet_accountability','treaty_diplomacy','federal_defence','federal_budget',
        'two_chambers','officers_council','national_press','irish_talks',
        'community_rights','irish_commission','ulster_police','ulster_review',
        'industrial_survey','freight_routes','armament_board','university_grants',
        'scientific_exchange','naval_review','naval_planning','carrier_operations',
        'naval_supply','air_service','pilot_reserve','sector_hq','navigation',
        'coastal_command','fairey','air_ground_liaison','army_review','staff_college',
        'army_signals','artillery_board','army_exercises',
    }
    for f in FOCI:
        if f['key'] in short:f['cost']=5
    prose={
        'continuity':('Британская конституция держится на признанных пределах власти. Кабинет сохранит ответственность перед Палатой общин, а перемены начнутся с пересмотра обязательств, которые Лондон больше не может исполнять в одиночку.',
                      'The constitution rests on accepted limits to power. The cabinet will remain responsible to the Commons while reviewing obligations London can no longer meet alone.'),
        'federal':('Федерация потребует уступок самой метрополии. Общая оборона и казна станут устойчивыми лишь тогда, когда решения перестанут быть исключительной привилегией Вестминстера.',
                   'Federation demands concessions from Britain itself. Common defence and finance can endure only when Westminster gives up its exclusive right to decide.'),
        'emergency':('Радикалы обещают избавить страну от бесконечных парламентских отсрочек. Промышленники и офицеры готовы их выслушать, но чрезвычайные полномочия неизбежно поставят вопрос о том, кто контролирует правительство.',
                     'Radicals promise an end to parliamentary delay. Industrialists and officers are listening, but emergency powers will inevitably raise the question of who controls the government.'),
        'labour':('Угольные районы и рабочие кварталы требуют, чтобы богатство Империи наконец служило их нуждам. Для устойчивых реформ лейбористам понадобится собственный общественный мандат внутри демократического большинства.',
                  'Mining districts and working-class neighbourhoods demand a share of imperial wealth. Labour needs a programme mandate within the democratic majority to make reform endure.'),
        'island':('Далёкие базы приносят влияние и постоянные счета. Сторонники островного курса предлагают договориться о передаче обязательств и направить высвободившиеся средства на безопасность и благосостояние метрополии.',
                  'Distant bases bring influence and permanent bills. The island programme offers a negotiated transfer of commitments and investment in security and welfare at home.'),
        'premiers':('Премьер-министры доминионов должны обсуждать общие обязательства до их объявления. Совет откроет путь к оплачиваемым конференциям, на которых каждый участник сможет принять или отвергнуть предложение.',
                    'Dominion prime ministers must discuss common commitments before they are announced. The council opens paid conferences where each participant may accept or reject an offer.'),
        'conference':('Канадцы требуют гарантий своих законов, австралийцы — безопасности Тихого океана, а Индия — ответственного правительства. Конференция даст им место за столом; содержание будущего договора ещё предстоит согласовать.',
                      'Canada seeks legal guarantees, Australia Pacific security, and India responsible government. The conference gives them a seat at the table; the treaty still has to be negotiated.'),
        'representation':('Палата населения без индийского представительства станет обещанием с оговоркой. Палата участников без гарантий малым странам вызовет их сопротивление. Хартия должна определить полномочия обеих.',
                          'A population chamber excluding India would be a qualified promise. A chamber of participants without safeguards for smaller countries would invite resistance. The charter must define both.'),
        'ratification':('Делегаты могут согласовать текст, но решение принадлежит местным парламентам. После подготовки каждый участник получит отдельное предложение о ратификации. Лондон обязан принять возможность отказа.',
                        'Delegates may agree a text, but local parliaments decide. Each participant receives a separate ratification proposal after preparation. London must accept the possibility of refusal.'),
        'federal_parliament':('Не менее двух правительств должны добровольно ратифицировать федеральный договор. Новый парламент начнёт работу в согласованном составе, сохранив страны-участницы, их армии и местные учреждения.',
                              'At least two governments must freely ratify the federal treaty. Parliament will open with the agreed membership, preserving participating countries, their armies and local institutions.'),
        'blackshirts':('Мосли построил своё движение на промышленном недовольстве и обещании возродить имперскую дисциплину. Передача власти потребует сорока процентов поддержки и готовой организационной сети. Низкая стабильность грозит гражданской войной.',
                       'Mosley built his movement on industrial discontent and promises of imperial discipline. Taking power requires forty percent support and an organised movement. Low stability risks civil war.'),
        'directory':('Часть консерваторов предлагает передать руководство государством Совету национальной обороны. Поддержка офицеров должна быть дополнена общественным мандатом; парламентская оппозиция не обязана признать новый порядок.',
                     'Some Conservatives propose handing executive authority to a National Defence Council. Officer backing must be accompanied by public support; parliamentary opponents may refuse to recognise the new order.'),
        'labour_election':('Поддержка демократии сама по себе не означает согласия с национализацией и социальными расходами. Лейбористы должны провести кампанию за собственную программу, прежде чем сформировать кабинет Эттли.',
                           'Support for democracy does not automatically endorse nationalisation and welfare spending. Labour must campaign for its own programme before forming an Attlee cabinet.'),
        'colonial_review':('Передача административных полномочий требует подготовки местных учреждений и переговоров с их представителями. Каждому реально зависимому правительству будет предложен отдельный договор о суверенитете.',
                           'Transferring administrative powers requires prepared local institutions and negotiations with their representatives. Each actual dependency will receive a separate sovereignty treaty.'),
        'social_republic':('Республиканское крыло требует завершить разрыв с наследственной властью. Только подготовленное движение с сорока процентами поддержки сможет попытаться изменить государственный строй; расколотая страна может ответить оружием.',
                           'Republicans demand a final break with hereditary power. An organised movement with forty percent support may attempt constitutional change; a divided country may answer with arms.'),
        'armed_neutrality':('Нейтралитет требует завершить передачу зависимых правительств и выйти из прежней системы союзных обязательств. Британия сможет сосредоточить военное планирование на защите собственных берегов.',
                            'Neutrality requires completing transfers to dependent governments and leaving the old alliance structure. Britain can then concentrate military planning on its own shores.'),
        'belfast':('Совместная комиссия, представительство общин и юридические гарантии могут остановить приграничную эскалацию. Дублин получит проект соглашения и право отказаться; в таком случае потребуется новое посредничество.',
                   'A joint commission, community representation and legal guarantees may stop border escalation. Dublin receives the draft and may decline, requiring fresh mediation.'),
        'irish_emergency':('Чрезвычайная администрация способна временно восстановить порядок. Дополнительные гарнизоны потребуют политических расходов, а нерешённые требования общин продолжат увеличивать напряжённость.',
                           'Emergency administration can temporarily restore order. Additional garrisons impose political costs while unresolved community demands continue to increase tension.'),
        'irish_future':('Согласие Дублина на Белфастское соглашение позволяет обсуждать будущее острова. Любое изменение границы потребует отдельного договора, мирных условий и фактического британского контроля над передаваемой территорией.',
                        'Dublin’s agreement to the Belfast settlement permits discussion of the island’s future. Any border change requires a separate treaty, peace, and actual British control over the territory transferred.'),
        'coalfields':('Мировое господство британского угля осталось в отчётах прежнего поколения. Новые выработки и оборудование должны обеспечить действующую энергетику сырьём, прежде чем возрастёт промышленное потребление.',
                      'British coal supremacy survives in the reports of an earlier generation. New workings and machinery must supply the energy system before industrial demand rises.'),
        'electric_grid':('Разрозненные сети и устаревшие станции делают расширение производства дороже. Объединённая система распределения позволит лучше использовать энергетическую базу страны.',
                         'Fragmented grids and obsolete stations make industrial expansion costly. An integrated distribution system will improve use of the country’s energy base.'),
        'free_trade':('Общий рынок может сохранить британское влияние после пересмотра политического подчинения. Для этого закупки, стандарты и доступ к рынкам должны стать предметом взаимных соглашений.',
                      'A common market may preserve British influence as political dependency changes. Procurement, standards and market access must become reciprocal agreements.'),
        'protection':('Пошлины и закупки защитят предприятия метрополии от внешней конкуренции. Доминионы воспримут эту программу как напоминание о том, чьи интересы Лондон ставит первыми.',
                      'Tariffs and procurement will shelter metropolitan firms from foreign competition. Dominions will see a reminder of whose interests London places first.'),
        'canadian_corridors':('Канадским предприятиям нужны надёжные связи между внутренними районами и портами. Фокус подготовит кредитную программу; деньги и строительные мощности будут выделены отдельным решением после согласия Оттавы.',
                              'Canadian industry needs reliable links between the interior and ports. This focus prepares a credit programme; funds and construction capacity require a separate decision and Ottawa’s consent.'),
        'indian_electricity':('Индийская промышленность должна получать энергию и собственные производственные возможности. Проект откроет оплачиваемые инвестиции, но не заменит переговоры об ответственном правительстве.',
                             'Indian industry needs power and productive capacity of its own. This programme opens paid investment without replacing negotiations on responsible government.'),
        'quality':('Военная приёмка будет добиваться устойчивых характеристик и воспроизводимого качества. Предприятиям понадобится время, чтобы поднять предел эффективности своих производственных линий.',
                   'Acceptance boards will demand consistent specifications and reproducible quality. Firms need time to raise the efficiency ceiling of their production lines.'),
        'mass_contracts':('Упрощённые заказы позволят быстрее расширить выпуск. Начальная перестройка линий временно снизит производство, прежде чем массовые контракты принесут результат.',
                          'Simplified orders allow output to expand faster. Initial retooling will temporarily reduce production before mass contracts deliver results.'),
        'radar_network':('Радиолокационный принцип уже доказал работоспособность. Теперь станции, связь и секторные штабы должны образовать действующую сеть раннего предупреждения.',
                         'Radar has already proved workable. Stations, communications and sector headquarters must now become an operational early-warning network.'),
        'escort':('Имперские договоры теряют смысл, когда транспорт не достигает портов. Постоянные эскорты и согласованные маршруты станут первым приоритетом Адмиралтейства.',
                  'Imperial treaties mean little when transports fail to reach port. Permanent escorts and coordinated routes will become the Admiralty’s first priority.'),
        'strike':('Сосредоточенное соединение способно изменить морское равновесие в решающем районе. Его создание потребует принять риск более слабого прикрытия второстепенных коммуникаций.',
                  'A concentrated force can change the naval balance in a decisive theatre. Building it means accepting thinner protection on secondary routes.'),
        'cape_route':('Доступ к базам Южной Африки позволит подготовить запасной путь при закрытии Суэца. Само решение Лондона не заменяет фактический доступ к Кейптауну и достаточный транспортный резерв.',
                      'Access to South African bases permits an alternative route if Suez closes. London’s decision cannot replace actual Cape Town access and adequate transport reserves.'),
        'fighter_command':('Промышленные районы нуждаются в системе, которая обнаружит налёт и направит перехватчики вовремя. Истребительное командование получит приоритет в развитии воздушной службы.',
                           'Industrial districts need a system that detects raids and directs interceptors in time. Fighter Command will receive priority in air-service development.'),
        'bomber_command':('Дальняя авиация должна заставить противника считаться с угрозой его промышленности. Подготовка экипажей, навигация и тяжёлые самолёты потребуют отдельной программы.',
                          'Long-range aviation must threaten an opponent’s industry. Crew preparation, navigation and heavy aircraft require a dedicated programme.'),
        'expeditionary':('Небольшие профессиональные силы должны быстро прибывать туда, где решается судьба британских обязательств. Их преимуществами станут подготовка, снабжение и ограниченная потребность в людях.',
                         'Small professional forces must arrive quickly wherever British commitments are tested. Training, logistics and limited manpower demands will be their strengths.'),
        'continental':('Возможная большая война потребует резерва, бронетанковых соединений и штабов, способных ими управлять. Армия начнёт готовиться к масштабу, которого не знала её служба в заморских гарнизонах.',
                        'A possible major war requires reserves, armoured formations and staffs able to command them. The army must prepare for a scale unfamiliar to its overseas garrisons.'),
    }
    for key,description in prose.items():loc(P+key+'_desc',*description)
    # Coercion halts dependency drift only while bearing a permanent political
    # upkeep, expressed through the existing state spirit rather than a new stack.
    next(f for f in FOCI if f['key']=='imperial_discipline')['mods']['state:political_power_factor']=-0.05
    next(f for f in FOCI if f['key']=='crown_directory')['mods']['state:political_power_factor']=-0.10
    for gate,organization in [('vickers','ENG_vickers_armstrong_eng_organization'),
                              ('standard_ammunition','ENG_rsaf_enfield_organization'),
                              ('supermarine','ENG_supermarine_organization'),
                              ('engine_plants','ENG_hawker_organization'),
                              ('fairey','ENG_fairey_aviation_organization')]:
        f=next(f for f in FOCI if f['key']==gate)
        token=P+organization+'_programme'
        f['effect']+=f' if = {{ limit = {{ has_dlc = "Arms Against Tyranny" }} mio:{organization} = {{ add_mio_size = 1 unlock_mio_trait_tooltip = {token} }} }}'
    # Absolute coordinates stay positive so the leftmost political branch is
    # reachable even before the tree has been scrolled or centred by the UI.
    for f in FOCI:
        f['x']+=18


def emit_tree():
    native = read(GAME/'common/national_focus/uk.txt')
    old = sorted({one(f,'id') for k,v,o in native for f in
                  (values(v,'focus') if k == 'focus_tree' else [v] if k == 'shared_focus' else []) if one(f,'id')})
    write('common/national_focus/uk.txt', '# Native filename override. Playable content: ENG_focuses.txt.\nfocus_tree = { id = british_focus default = no country = { factor = 0 } }')
    write('common/national_focus/ENG_compatibility.txt',
          '# Owner: ENG. Direct native focus IDs only; inert callbacks, no rewards.\n' + '\n'.join(
          f'shared_focus = {{ id = {fid} icon = GFX_goal_generic_political_pressure x = 0 y = 0 cost = 5 allow_branch = {{ always = no }} available = {{ always = no }} completion_reward = {{ }} }}' for fid in old))
    from britain_focus_icons import ICONS,icon_for
    assert {f['key'] for f in FOCI}==set(ICONS),'Every playable focus needs an explicit themed icon'
    out = ['# Owner: ENG. Generated by tools/build_britain_content.py.',
           'focus_tree = { id = ENG_nww_focus default = no country = { factor = 0 modifier = { add = 200 tag = ENG } }',
           'initial_show_position = { x = 18 y = 0 } continuous_focus_position = { x = 100 y = 2600 }']
    out.extend('shared_focus = '+fid for fid in old)
    for f in FOCI:
        fid=f['id']
        out.append(f"focus = {{ id = {fid} icon = {icon_for(f['key'])} x = {f['x']} y = {f['y']} cost = {f['cost']}")
        if f['parent']: out.append(f"prerequisite = {{ focus = {P+f['parent']} }}")
        if f['exclusive']: out.append('mutually_exclusive = { '+' '.join('focus = '+P+k for k in f['exclusive'])+' }')
        out.append('available = { has_capitulated = no '+f['available']+' }')
        out.append('cancel_if_invalid = yes continue_if_invalid = no')
        if f['key']=='research_capacity': out.append('bypass = { amount_research_slots > 5 }')
        weight = 8 if f['group'] in ('economy','navy') else 3
        if f['key'] in ('report','session','budget','irish_report','border_inquiry','irish_talks','belfast'): weight=30
        out.append(f'ai_will_do = {{ factor = {weight}')
        if f['key'] in ('continuity','federal','emergency','labour','island'):
            plan={'continuity':'continuity','federal':'federal','emergency':'right','labour':'labour','island':'island'}[f['key']]
            out.append(f'modifier = {{ factor = 0 NOT = {{ has_country_flag = ENG_nww_plan_{plan} }} }}')
        for key,flag in [('blackshirts','fascist'),('directory','directory'),('social_republic','republic'),('parliamentary_socialism','social')]:
            if f['key']==key: out.append(f'modifier = {{ factor = 0 NOT = {{ has_country_flag = ENG_nww_plan_{flag} }} }}')
        out.append('}')
        out.append('completion_reward = { '+f['effect'])
        from britain_reward_tooltips import focus_reward_tooltips
        out.extend('custom_effect_tooltip = '+tip for tip in focus_reward_tooltips(f,loc))
        for mod,amount in f['mods'].items():
            tip = P+'bonus_'+mod.replace(':','_')+'_'+str(amount).replace('-','minus').replace('.','_')
            label = mod.split(':')[1]
            label = {'industrial_capacity_factory':'MODIFIER_INDUSTRIAL_CAPACITY_FACTOR',
                     'industrial_capacity_dockyard':'MODIFIER_INDUSTRIAL_CAPACITY_DOCKYARD_FACTOR',
                     'army_core_defence_factor':'MODIFIERS_ARMY_CORE_DEFENCE_FACTOR',
                     'convoy_escort_efficiency':'MODIFIER_MISSION_CONVOY_ESCORT_EFFICIENCY',
                     'air_strategic_bomber_bombing_factor':'MODIFIER_STRATEGIC_BOMBER_BOMBING_FACTOR'}.get(label,'MODIFIER_'+label.upper())
            loc(tip, f'Изменение постоянного духа: ${label}$: {amount:+.0%}.', f'Persistent spirit change: ${label}$: {amount:+.0%}.')
            out.append('custom_effect_tooltip = '+tip)
        out.append('hidden_effect = { set_country_flag = ENG_nww_spirit_refresh_pending ENG_nww_clamp = yes ENG_nww_rebuild_spirits = yes } } }')
    out.append('}')
    write('common/national_focus/ENG_focuses.txt','\n'.join(out))
    write('docs/ENG_focus_manifest.json',json.dumps(FOCI,ensure_ascii=False,indent=2))
    return old


def emit_native_isolation():
    # Native Britain chains are replaced completely, while their IDs remain valid.
    for name in ('Britain.txt','MTG_Britain.txt','WTT_Britain.txt'):
        doc = read(GAME/'events'/name)
        out=['# Owner: ENG. Native callbacks retired; see ENG_events.txt.']
        for k,v,o in doc:
            if k=='add_namespace': out.append('add_namespace = '+v)
            elif k in ('country_event','news_event'):
                out.append(f'{k} = {{ id = {one(v,"id")} hidden = yes is_triggered_only = yes immediate = {{ }} }}')
        write('events/'+name,'\n'.join(out))
    write('common/decisions/ENG.txt','# Native ENG decisions replaced by ENG_decisions.txt. Owner: ENG.\n# Keep the ID referenced by the installed native Mosley category.\nENG_nww_cabinet_category = { ENG_the_mosley_plan = { visible = { always = no } available = { always = no } } }')
    for name in ('ENG_historical_strategy_plan.txt','ENG_alternate_strategy_plan.txt'):
        write('common/ai_strategy_plans/'+name,'# Native ENG AI retired. See ENG_nww_plans.txt.')


if __name__ == '__main__':
    content()
    emit_tree()
    emit_native_isolation()
    # Remaining country systems are emitted by the companion module.
    from britain_systems import emit_systems
    emit_systems(write,loc,FOCI,GAME)
    from britain_gui import emit_gui
    emit_gui(write,loc)
    for lang, entries in LOCS.items():
        path=ROOT/f'localisation/{lang}/ENG_nww_l_{lang}.yml'
        path.parent.mkdir(parents=True,exist_ok=True)
        path.write_text('l_'+lang+':\n'+'\n'.join(' '+k+':0 '+quoted(v) for k,v in entries.items())+'\n',encoding='utf-8-sig',newline='\n')
    print(f'Generated {len(FOCI)} ENG focuses and {len(LOCS["russian"])} bilingual localization keys.')
    from repair_campaign_order_and_crown import repair_crown
    repair_crown()
