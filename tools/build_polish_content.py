"""Build country-owned NWW Polish focuses, localization and deterministic programs.

Installed examples and design notes: docs/POL_overhaul.md. Does not edit archives.
"""
import argparse
import json
from pathlib import Path
from hoi4_script import read, one, values, walk, dump, parse

ROOT=Path(__file__).resolve().parents[1]
FOCUSES=[]
LOCALE={}
GROUPS={
 'cop':('POL_cop_program','generic_industrial_concern_1',{
  'construction':('production_speed_buildings_factor','Construction speed','Скорость строительства'),
  'output':('industrial_capacity_factory','Military factory output','Выпуск военных заводов'),
  'efficiency':('production_factory_efficiency_gain_factor','Production efficiency growth','Рост эффективности производства'),
  'energy':('energy_gain_factor','Energy gain','Выработка энергии'),
  'research':('research_speed_factor','Research speed','Скорость исследований')}),
 'army':('POL_army_program','generic_army_war_college',{
  'org':('army_org_factor','Army organisation','Организация армии'),
  'planning':('planning_speed','Planning speed','Скорость планирования'),
  'cavalry':('cavalry_attack_factor','Cavalry attack','Атака кавалерии'),
  'motorized':('motorized_attack_factor','Motorized attack','Атака моторизованной пехоты'),
  'cavalry_speed':('modifier_army_sub_unit_cavalry_speed_factor','Cavalry speed','Скорость кавалерии'),
  'speed':('army_speed_factor','Army speed','Скорость армии'),
  'dig_in':('max_dig_in_factor','Maximum entrenchment','Максимальная укреплённость'),
  'dig_speed':('dig_in_speed_factor','Entrenchment speed','Скорость окапывания'),
  'supply':('supply_consumption_factor','Supply consumption','Потребление снабжения'),
  'training':('training_time_army_factor','Army training time','Время подготовки армии'),
  'defence':('army_core_defence_factor','Defence on core territory','Оборона национальных территорий')}),
 'air':('POL_air_program','generic_air_bonus',{
  'range':('air_range_factor','Air range','Дальность авиации'),
  'efficiency':('air_mission_efficiency','Air mission efficiency','Эффективность авиазаданий'),
  'accidents':('air_accidents_factor','Air accident chance','Вероятность авиапроисшествий')}),
 'state':('POL_state_program','generic_political_support',{
  'stability':('stability_factor','Stability','Стабильность'),
  'power':('political_power_gain','Daily political power','Политическая власть в день'),
  'war_support':('war_support_factor','War support','Поддержка войны'),
  'compliance':('compliance_growth','Compliance growth in our occupied states','Рост подчинения на оккупированных нами территориях'),
  'resistance':('resistance_target','Resistance target in our occupied states','Целевое сопротивление на оккупированных нами территориях')})}

def loc(key,ru,en):LOCALE[key]={'russian':ru,'english':en}
def fid(s):return 'POL_'+s

def add(short,ru,en,ru_desc,en_desc,x,y,parent=None,*,cost=10,branch='economy',bonus=None,reward='',available='',exclusive=(),extra=''):
 node=dict(id=fid(short),ru=ru,en=en,ru_desc=ru_desc,en_desc=en_desc,x=x,y=y,cost=cost,branch=branch,
           parents=[fid(p) for p in ([parent] if isinstance(parent,str) else parent or [])],bonus=bonus or {},
           reward=reward,available=available,exclusive=[fid(p) for p in exclusive],extra=extra)
 FOCUSES.append(node)
 return node

def tech(category,bonus='0.50',uses=1):return f'add_tech_bonus = {{ category = {category} bonus = {bonus} uses = {uses} }}'
def build(kind,n=1,coast=False):
 return f'''random_owned_controlled_state = {{
 limit = {{ {'is_coastal = yes' if coast else 'is_core_of = PREV'} }}
 add_extra_state_shared_building_slots = {n}
 add_building_construction = {{ type = {kind} level = {n} instant_build = yes }}
}}'''
def politics(group):return f'set_politics = {{ ruling_party = {group} elections_allowed = no election_frequency = 48 }}'

def definitions():
 # Economy: 14 focuses, with a real mutually exclusive financing choice.
 add('cop_plan','План ЦИО','The COP Plan','Сосредоточим ограниченные средства на внутреннем промышленном округе, вдали от германских заводов.','Concentrate scarce funds on an inland industrial district beyond German industrial ownership.',6,0,cost=5,bonus={'cop':{'construction':0.05}})
 add('industrial_census','Промышленная перепись','Industrial Census','Учтём мощности и транзитные обязательства прежде, чем выдавать новые концессии.','Audit capacity and transit obligations before granting new concessions.',6,1,'cop_plan',cost=5,reward='add_political_power = 40')
 add('accept_german_capital','Принять германский капитал','Accept German Capital','Две гражданские фабрики достанутся нам ценой более тяжёлых потребительских и торговых обязательств.','Two civilian factories come with heavier consumer-goods and trade obligations.',4,2,'industrial_census',reward='POL_accept_capital = yes\n'+build('industrial_complex',2),exclusive=['economic_independence'],available='GER = { exists = yes } NOT = { has_war_with = GER } NOT = { has_completed_focus = POL_nationalize_german_assets }')
 add('economic_independence','Экономическая независимость','Economic Independence','Выкупим зависимые предприятия за 100 политической власти. Германские инвестиционные льготы исчезнут вместе с удавкой.','Buy out dependent enterprises for 100 political power. German investment benefits end with the stranglehold.',8,2,'industrial_census',reward='add_political_power = -100\nPOL_end_german_dependence = yes',bonus={'cop':{'construction':0.10}},available='has_political_power > 99 NOT = { is_subject_of = GER } NOT = { has_completed_focus = POL_pragmatic_deal }',exclusive=['accept_german_capital'])
 n=add('public_works_board','Управление общественных работ','Public Works Board','Объединим ведомственные заказы и перестанем строить конкурирующие объекты в одних городах.','Coordinate departmental orders rather than building competing facilities in the same towns.',6,3,['accept_german_capital','economic_independence'],bonus={'cop':{'construction':0.05}});n['or_parents']=True
 add('vistula_rail_corridor','Вислинский железнодорожный коридор','Vistula Rail Corridor','Улучшим внутренние перевозки между Варшавой и промышленными областями.','Improve inland transport between Warsaw and the industrial districts.',6,4,'public_works_board',reward='POL_improve_inland_transport = yes')
 add('southern_workshops','Южные машиностроительные мастерские','Southern Engineering Workshops','Построим военный завод на собственной территории, а не на обещанной карте.','Build a military factory on territory we actually own and control.',2,5,'vistula_rail_corridor',reward=build('arms_factory'))
 add('rural_electrification','Электрификация села','Rural Electrification','Энергоснабжение отстаёт от промышленного плана; расширим собственную генерацию.','Power supply lags behind the industrial plan; expand domestic generation.',10,5,'vistula_rail_corridor',bonus={'cop':{'energy':0.10}},reward='POL_build_power = yes')
 add('domestic_coal_survey','Разведка внутренних угольных пластов','Domestic Coal Survey','Разработаем собственные залежи, не рассчитывая на германскую Верхнюю Силезию.','Develop domestic deposits rather than relying on German Upper Silesia.',10,6,'rural_electrification',reward='random_owned_controlled_state = { limit = { is_core_of = PREV } add_resource = { type = coal amount = 8 } }')
 add('lublin_arsenals','Люблинские арсеналы','Lublin Arsenals','Расширим мощности военного округа ещё одним заводом.','Add another factory to the inland armaments district.',2,6,'southern_workshops',reward=build('arms_factory'))
 add('precision_machine_tools','Точное станкостроение','Precision Machine Tools','Поднимем качество серийного производства и освоим современные станки.','Improve series production and master modern machine tools.',6,7,['lublin_arsenals','domestic_coal_survey'],bonus={'cop':{'efficiency':0.10}},reward=tech('industry'))
 add('university_consortium','Университетский консорциум','University Consortium','Свяжем университеты и заводские лаборатории: ещё одна исследовательская ячейка, до общего предела в пять.','Connect universities and factory laboratories: one research slot, up to a total of five.',4,8,'precision_machine_tools',reward='if = { limit = { amount_research_slots < 5 } add_research_slot = 1 }')
 add('export_diversification','Диверсификация заказов','Diversify Industrial Orders','Освоим альтернативные комплектующие и повысим выпуск военных заводов. Сухопутная торговля всё ещё требует реального маршрута.','Develop alternative components and improve military output. Land trade still requires a real route.',8,8,'precision_machine_tools',bonus={'cop':{'output':0.05}},reward=tech('electronics'))
 add('four_year_balance_sheet','Итоги четырёхлетнего плана','Four-Year Balance Sheet','Закрепим производственную кооперацию и техническое образование.','Consolidate industrial cooperation and technical education.',6,9,['university_consortium','export_diversification'],bonus={'cop':{'output':0.05,'research':0.05}})
 # Army: 12 focuses, developing one persistent program.
 add('modernize_the_army','Модернизировать армию','Modernize the Army','Армии нужны обученные штабы и снабжение, а не новая легенда о кавалерии.','The army needs trained staffs and supplies rather than another cavalry legend.',20,0,cost=5,branch='army',bonus={'army':{'planning':0.05}},reward='army_experience = 15')
 add('officer_academy','Высшая военная школа','Officer Academy','Согласуем подготовку офицеров и управление соединениями.','Coordinate officer training and formation command.',20,1,'modernize_the_army',branch='army',bonus={'army':{'org':0.05}},reward=tech('infantry_weapons'))
 add('cavalry_traditions','Кавалерийские традиции','Cavalry Traditions','Сохраним разведывательную и манёвренную роль конницы, готовя её сотрудничество с моторизованной пехотой.','Keep cavalry in reconnaissance and manoeuvre roles while preparing cooperation with motorized infantry.',16,2,'officer_academy',branch='army',exclusive=['defend_the_wisla'],bonus={'army':{'cavalry':0.10,'cavalry_speed':0.10}})
 add('defend_the_wisla','Защитить Вислу','Defend the Vistula','Укрепим национальные пограничные области и улучшим организацию и окапывание сухопутных войск.','Fortify our controlled core border states and improve army organisation and entrenchment.',24,2,'officer_academy',branch='army',exclusive=['cavalry_traditions'],bonus={'army':{'org':0.05,'dig_in':0.10}},reward='POL_build_border_forts = yes')
 add('motorized_columns','Моторизованные колонны','Motorized Columns','Дадим подвижным частям грузовики и стандарты взаимодействия с кавалерией.','Supply mobile formations with trucks and common operating standards.',16,3,'cavalry_traditions',branch='army',bonus={'army':{'motorized':0.10,'speed':0.05}},reward='add_equipment_to_stockpile = { type = motorized_equipment_1 amount = 200 producer = ROOT }')
 add('mobile_signals','Связь подвижных соединений','Mobile Signals','Ускорим передачу приказов в манёвренной армии.','Speed up orders within the mobile army.',16,4,'motorized_columns',branch='army',bonus={'army':{'planning':0.10}},reward=tech('support_tech'))
 add('fortress_engineers','Крепостные инженеры','Fortress Engineers','Инженерные команды подготовят укрепления и полевые позиции.','Engineer teams will prepare fortifications and field positions.',24,3,'defend_the_wisla',branch='army',bonus={'army':{'dig_speed':0.10}},reward=tech('support_tech'))
 add('vistula_reserve_battalions','Вислинские резервные батальоны','Vistula Reserve Battalions','Организуем сменные части для обороны национальной территории.','Organize replacement battalions for homeland defence.',24,4,'fortress_engineers',branch='army',bonus={'army':{'defence':0.10}})
 n=add('unified_general_staff','Единый генеральный штаб','Unified General Staff','Подчиним выбранную доктрину единой системе планирования.','Place the chosen doctrine within a unified planning system.',20,5,['mobile_signals','vistula_reserve_battalions'],branch='army',bonus={'army':{'planning':0.05}},reward='army_experience = 20');n['or_parents']=True
 add('quartermaster_service','Интендантская служба','Quartermaster Service','Сократим потери снабжения при внутренних перевозках.','Reduce supply waste in inland transport.',20,6,'unified_general_staff',branch='army',bonus={'army':{'supply':-0.10}})
 add('reserve_officer_network','Сеть офицеров запаса','Reserve Officer Network','Подготовленные инструкторы ускорят обучение пополнений.','Trained instructors will accelerate replacement training.',20,7,'quartermaster_service',branch='army',bonus={'army':{'training':-0.10}})
 add('national_manoeuvres','Общенациональные манёвры','National Manoeuvres','Проверим реформы в учениях и закрепим управляемость армии.','Test the reforms in exercises and consolidate army cohesion.',20,8,'reserve_officer_network',branch='army',bonus={'army':{'org':0.05}},reward='army_experience = 25')
 # Air force: 6 focuses. No inherited naval branch at the 1936 start.
 add('pzl_research_bureau','Конструкторское бюро PZL','PZL Design Bureau','Разовьём авиационные проекты собственного производства.','Develop domestic aircraft designs.',32,0,cost=5,branch='air',reward=tech('air_equipment'))
 add('air_training_schools','Лётные училища','Flying Schools','Единая программа подготовки снизит аварийность.','A common training syllabus will reduce accidents.',32,1,'pzl_research_bureau',branch='air',bonus={'air':{'accidents':-0.10}})
 add('defence_of_the_skies','Защита польского неба','Defence of Polish Skies','Подготовим истребительную авиацию к обороне внутренних промышленных районов.','Prepare fighters to defend inland industrial districts.',30,2,'air_training_schools',branch='air',bonus={'air':{'range':0.10}},reward=tech('light_air'))
 add('army_air_liaison','Связь авиации с армией','Army-Air Liaison','Наладим обмен разведданными и вызов поддержки.','Coordinate reconnaissance and requests for air support.',34,2,'air_training_schools',branch='air',bonus={'air':{'efficiency':0.05}},reward=tech('cas_bomber'))
 add('dispersed_air_workshops','Рассредоточенные авиамастерские','Dispersed Air Workshops','Построим ещё один военный завод и защищённую внутреннюю авиабазу.','Build another military factory and an inland air base.',32,3,['defence_of_the_skies','army_air_liaison'],branch='air',reward=build('arms_factory')+'\nPOL_build_air_base = yes')
 add('integrated_air_command','Объединённое командование ВВС','Integrated Air Command','Закрепим взаимодействие воздушных округов.','Consolidate cooperation between air districts.',32,4,'dispersed_air_workshops',branch='air',bonus={'air':{'efficiency':0.05}},reward='air_experience = 25')
 add('baltic_fleet_program','Программа Балтийского флота','Baltic Fleet Programme','Пока мы не контролируем побережье, это лишь проект будущего флота. Этот фокус сам не создаёт кораблей.','Until we control a coastline this remains a future proposal. This focus creates no ships.',80,0,cost=5,branch='navy',available='has_any_controlled_coastal_state = yes',extra='allow_branch = { has_any_controlled_coastal_state = yes }\nai_will_do = { factor = 1 }')
 add('first_coastal_dockyard','Первая прибрежная верфь','First Coastal Dockyard','Перейдём от проекта к одной верфи в собственной контролируемой прибрежной области.','Move from plans to one dockyard in an owned, controlled coastal state.',80,1,'baltic_fleet_program',branch='navy',available='any_owned_state = { is_controlled_by = ROOT is_coastal = yes }',reward=build('dockyard',1,True)+'\n'+tech('naval_equipment'))
 # Shared political preparation: 6 focuses, with repeatable paid campaigning.
 add('aftermath_of_the_marshal','Смерть Маршала','After the Marshal','Пилсудский умер. Независимость, добытая в годы Великой смуты, переживёт его лишь при новом государственном компромиссе.','Pilsudski is dead. Independence won during the Great Tumult will outlive him only through a new political settlement.',56,0,cost=5,branch='politics',reward='add_political_power = 50')
 add('castle_and_colonels_dialogue','Диалог Замка и полковников','Castle-Colonels Dialogue','Подготовим соглашение гражданского и военного крыла Санации.','Prepare an agreement between Sanation’s civilian and military wings.',44,1,'aftermath_of_the_marshal',cost=5,branch='politics',reward='add_popularity = { ideology = neutrality popularity = 0.10 }')
 add('national_democratic_leagues','Национал-демократические союзы','National Democratic Leagues','Эндеция создаёт политическую организацию; одной уличной агитации для смены власти недостаточно.','Endecja builds an organization; street agitation alone cannot justify a change of government.',52,1,'aftermath_of_the_marshal',cost=5,branch='politics',reward='add_popularity = { ideology = fascism popularity = 0.10 }')
 add('berlin_trade_delegation','Торговая делегация в Берлин','Trade Delegation to Berlin','Подготовим внутреннюю коалицию сторонников прагматической сделки с Германией.','Prepare a domestic coalition for a pragmatic agreement with Germany.',60,1,'aftermath_of_the_marshal',cost=5,branch='politics',reward='add_popularity = { ideology = neutrality popularity = 0.05 }')
 add('workers_defence_committees','Комитеты защиты рабочих','Workers Defence Committees','Создадим рабочую организацию Лодзи, способную добиваться массовой поддержки.','Build a Lodz workers’ organization capable of winning mass support.',68,1,'aftermath_of_the_marshal',cost=5,branch='politics',reward='add_popularity = { ideology = communism popularity = 0.10 }')
 add('state_budget_commission','Комиссия государственного бюджета','State Budget Commission','Уменьшим остроту кризиса Санации, но окончательные институты ещё предстоит создать.','Ease the Sanation crisis, while leaving its final institutional settlement unfinished.',56,2,'aftermath_of_the_marshal',cost=5,branch='politics',reward='set_country_flag = POL_budget_commission_done\nPOL_refresh_crisis = yes')
 # Four mutually exclusive political paths, 10 focuses each.
 paths=['the_colonels_regime','endecja_ascendant','pragmatic_deal','the_lodz_uprising']
 entry=[('the_colonels_regime','Режим полковников','The Colonels’ Regime','Сохраним независимость и власть Санации при мандате не менее 40%.','Preserve independence and Sanation rule with at least 40% support.',44,'castle_and_colonels_dialogue','neutrality','POL_establish_sanation = yes','sanation'),('endecja_ascendant','Триумф Эндеции','Endecja Ascendant','Национал-демократы сменят режим при поддержке не менее 40% и подготовленном политическом движении.','The National Democrats replace the regime with at least 40% support and a prepared political movement.',52,'national_democratic_leagues','fascism','POL_establish_endecja = yes','endecja'),('pragmatic_deal','Прагматическая сделка','A Pragmatic Deal','Выберем переговоры с Берлином; политический союз всё ещё потребует согласия Германии.','Choose negotiations with Berlin; a political alliance still requires German consent.',60,'berlin_trade_delegation','neutrality','set_country_flag = POL_path_german','german'),('the_lodz_uprising','Лодзинское восстание','The Lodz Uprising','При поддержке коммунистов не менее 40% рабочее движение бросит вооружённый вызов режиму.','With at least 40% communist support, the workers’ movement launches an armed challenge to the regime.',68,'workers_defence_committees','communism','custom_effect_tooltip = POL_civil_war_tt\nhidden_effect = { POL_start_communist_civil_war = yes }','communist')]
 for short,ru,en,rd,ed,x,prep,ideology,reward,path in entry:
  gate=f'POL_no_political_path = yes\nis_subject = no\nhas_civil_war = no\nhas_completed_focus = POL_state_budget_commission\nNOT = {{ {ideology} < 0.40 }}'
  if path=='german':gate+='\nGER = { exists = yes }\nNOT = { has_war_with = GER }\nNOT = { has_completed_focus = POL_economic_independence }'
  add(short,ru,en,rd,ed,x,3,prep,branch=path,reward=reward,available=gate,exclusive=[p for p in paths if p!=short],bonus={} if path in ('german','communist') else {'state':{'stability':0.05}},extra=f'ai_will_do = {{ factor = 1 modifier = {{ factor = 0 is_ai = yes NOT = {{ has_country_flag = POL_ai_{path} }} }} }}')
 # Sanation: independent defensive bloc and negotiated reconciliation.
 san=[('castle_compact','Соглашение с Замком','Compact with the Castle','Уточним пределы власти президента и генерального инспектора.','Define the powers of the president and the inspector-general.',{'state':{'power':0.10}},''),('professional_civil_service','Профессиональная администрация','Professional Civil Service','Закончим кризис разделённого управления и закрепим бюджетную ответственность.','End divided administration and establish budgetary accountability.',{'state':{'stability':0.05}},'POL_finish_crisis = yes'),('fortify_the_borders','Укрепить границы','Fortify the Borders','Подготовим реальные национальные пограничные области к обороне.','Prepare our actual controlled core border states for defence.',{'army':{'defence':0.05}},'POL_build_border_forts = yes'),('intermarium_concept','Концепция Междуморья','The Intermarium Concept','Создадим собственный оборонительный альянс; соседи смогут принять или отклонить приглашение.','Create a defensive alliance of our own; neighbours may accept or reject an invitation.',{},'POL_create_intermarium = yes'),('vilnius_settlement','Виленское урегулирование','The Vilnius Settlement','Предложим ЛитБелу взаимный отказ от пограничных претензий без автоматической передачи областей.','Offer Lithuania-Belarus mutual renunciation of border claims without automatic state transfers.',{},'POL_offer_vilnius_settlement = yes'),('baltic_danubian_congress','Балтийско-Дунайский конгресс','Baltic-Danubian Congress','Пригласим Румынию и, после урегулирования спора, ЛитБел в Междуморье.','Invite Romania and, after settling the dispute, Lithuania-Belarus into the Intermarium.',{},'POL_offer_intermarium_membership = yes'),('agrarian_conciliation','Соглашение с деревней','Agrarian Conciliation','Крестьянское представительство укрепит устойчивость независимой республики.','Rural representation strengthens the independent republic.',{'state':{'stability':0.05}},''),('national_defence_fund_nww','Национальный фонд обороны','National Defence Fund','Профинансируем ещё один собственный военный завод.','Finance another domestic military factory.',{},build('arms_factory')),('republic_survives','Республика выстояла','The Republic Endures','После 1941 года закрепим институты независимой оборонительной республики.','After 1941, consolidate the institutions of an independent defensive republic.',{'state':{'power':0.10},'army':{'defence':0.05}},'')]
 for i,(s,r,e,rd,ed,b,reward) in enumerate(san):
  a='has_government = neutrality is_subject = no'
  if s=='intermarium_concept':a+=' OR = { is_in_faction = no is_faction_leader = yes }'
  if s=='republic_survives':a+=' date > 1940.12.31'
  add(s,r,e,rd,ed,44,4+i,'the_colonels_regime' if i==0 else san[i-1][0],branch='sanation',bonus=b,reward=reward,available=a)
 # Endecja: expensive preparation, specific western claims and a real war.
 end=[('national_bloc','Национальный блок','National Bloc','Укрепим политическую организацию национального правительства.','Consolidate the nationalist government’s political organization.',{'state':{'war_support':0.10}},'POL_finish_crisis = yes'),('radical_polonization','Радикальная полонизация','Radical Polonization','Принудительная администрация ускорит подчинение оккупированных земель, но усилит сопротивление.','Coercive administration accelerates occupied-territory compliance but increases resistance.',{'state':{'compliance':0.05,'resistance':0.10}},''),('western_claims_dossier','Досье западных претензий','Western Claims Dossier','Сформулируем претензии на Познань, Померанию, Данциг и Верхнюю Силезию, не объявляя эти области своими владениями.','Formulate claims to Poznan, Pomerelia, Danzig and Upper Silesia without treating them as already owned.',{},'POL_add_western_claims = yes'),('march_to_the_sea','Марш к морю','March to the Sea','С 1939 года подготовим ограниченную цель войны против Германии за западные области. ИИ должен дождаться уязвимости противника.','From 1939 prepare a limited war goal against Germany for the western states. The AI must wait until Germany is vulnerable.',{},'POL_prepare_western_war = yes'),('secure_the_corridor','Закрепить коридор','Secure the Corridor','Восстановим управление только после фактического владения и контроля западных областей.','Rebuild administration only after actually owning and controlling western territory.',{'state':{'stability':0.05}},'POL_rebuild_western_regions = yes'),('wartime_conversion','Военная конверсия','Wartime Conversion','Переориентируем промышленные заказы и окончательно расторгнем германские концессии.','Redirect industrial orders and terminate German concessions.',{'cop':{'output':0.10}},'POL_end_german_dependence = yes'),('silesian_reconstruction','Силезская реконструкция','Silesian Reconstruction','Промышленные вложения поступят лишь в действительно возвращённые области.','Industrial investment goes only to genuinely recovered states.',{},'POL_rebuild_silesia = yes'),('continental_army','Континентальная армия','Continental Army','Закрепим организацию и снабжение армии после западной кампании.','Consolidate army organization and supplies after the western campaign.',{'army':{'org':0.05,'supply':-0.05}},''),('sovereign_national_state','Суверенное национальное государство','A Sovereign National State','Закрепим институты государства, отказавшегося от германского протектората.','Consolidate the institutions of a state that rejected a German protectorate.',{'state':{'power':0.10,'war_support':0.05}},'')]
 end.insert(3,end.pop(5))
 for i,(s,r,e,rd,ed,b,reward) in enumerate(end):
  a='has_government = fascism is_subject = no'
  if s=='march_to_the_sea':a+=' date > 1938.12.31 POL_can_prepare_western_war = yes'
  if s=='secure_the_corridor':a+=' POL_controls_western_recovery_area = yes'
  if s=='silesian_reconstruction':a+=' 762 = { is_owned_and_controlled_by = ROOT }'
  add(s,r,e,rd,ed,52,4+i,'endecja_ascendant' if i==0 else end[i-1][0],branch='endecja',bonus=b,reward=reward,available=a)
 # German compact: consent, a 40% mandate for the actual German ideology, no automatic puppet.
 ger=[('customs_commission','Таможенная комиссия','Customs Commission','Подготовим условия транзита и промышленного кредита.','Prepare terms for transit and industrial credit.',{'cop':{'efficiency':0.05}},'POL_finish_crisis = yes'),('guaranteed_transit','Гарантированный транзит','Guaranteed Transit','Согласуем процедуры перевозок. Фокус не создаёт морских портов или несуществующих торговых маршрутов.','Agree transport procedures. This focus creates neither ports nor imaginary trade routes.',{'cop':{'output':0.05}},tech('industry')),('join_mitteleuropa_officially','Официально войти в Миттельевропу','Officially Join Mitteleuropa','При мандате 40% для идеологии Германии примем соответствующий режим и запросим у Берлина союз и гарантию. Германия может отказать.','With 40% support for Germany’s ideology, align our government and request Berlin’s alliance and guarantee. Germany may refuse.',{},'POL_align_with_germany = yes\nPOL_offer_german_compact = yes'),('licensed_machine_tools','Лицензионное станкостроение','Licensed Machine Tools','Сохраним польское производство на базе согласованных технических лицензий.','Maintain Polish production through agreed technical licences.',{'cop':{'efficiency':0.05}},tech('industry')),('staff_exchange','Обмен штабными миссиями','Staff Exchange','Обучим офицеров работе с партнёрами, сохранив собственные соединения.','Train officers to cooperate with partners while retaining Polish formations.',{'army':{'planning':0.10}},'army_experience = 20'),('recognize_the_western_frontier','Признать западную границу','Recognize the Western Frontier','Откажемся от политических претензий на германские западные области; чужая территория не будет передана автоматически.','Renounce political claims to German western states; no foreign territory is transferred automatically.',{},'POL_renounce_western_claims = yes'),('galician_assurances','Галицийские гарантии','Galician Assurances','Укрепим собственную оборону юга; союз с Германией не аннексирует Австрию.','Strengthen our own southern defence; an alliance with Germany does not annex Austria.',{'army':{'defence':0.05}},'POL_build_southern_forts = yes'),('joint_armament_contracts','Совместные оружейные контракты','Joint Armament Contracts','Расширим военное производство одной собственной фабрикой.','Expand armaments production with one domestic factory.',{},build('arms_factory')),('polish_institutions_in_mitteleuropa','Польские институты в Миттельевропе','Polish Institutions in Mitteleuropa','Закрепим административную устойчивость внутри германской системы.','Consolidate administrative stability within the German system.',{'state':{'stability':0.10,'power':0.10}},'')]
 for i,(s,r,e,rd,ed,b,reward) in enumerate(ger):
  a='POL_german_path_active = yes'
  if s=='join_mitteleuropa_officially':a+=' POL_german_ideology_mandate = yes'
  if s in ('licensed_machine_tools','staff_exchange','recognize_the_western_frontier','galician_assurances','joint_armament_contracts','polish_institutions_in_mitteleuropa'):a+=' has_country_flag = POL_german_compact_accepted'
  add(s,r,e,rd,ed,60,4+i,'pragmatic_deal' if i==0 else ger[i-1][0],branch='german',bonus=b,reward=reward,available=a)
 # Communist path: genuine civil-war victory, consent-based eastern alliance.
 com=[('council_republic','Республика советов','Council Republic','Только победа восставших в гражданской войне позволяет учредить новое государство.','Only an actual rebel victory in the civil war permits the new state to be constituted.',{'state':{'stability':0.05}},'POL_finish_crisis = yes'),('land_and_food_committees','Земельные и продовольственные комитеты','Land and Food Committees','Организуем снабжение городов и представительство деревни.','Organize urban food supply and rural representation.',{'state':{'stability':0.05}},''),('nationalize_german_assets','Национализировать германские активы','Nationalize German Assets','Ликвидируем зависимость от германских концессий вместе с инвестиционными преимуществами.','End German concession dependence together with its investment benefits.',{'cop':{'construction':0.05}},'POL_end_german_dependence = yes'),('workers_militias_nww','Рабочие ополчения','Workers Militias','Сформируем систему военной подготовки рабочих без бесплатного создания дивизий.','Build a workers’ military training system without conjuring free divisions.',{'army':{'training':-0.10,'defence':0.05}},'army_experience = 20'),('alliance_with_the_east','Союз с Востоком','Alliance with the East','Предложим союз коммунистической России либо ЛитБелу. Получатель сохраняет право отказа.','Offer an alliance to communist Russia or Lithuania-Belarus. The recipient retains the right to refuse.',{},'POL_offer_eastern_alliance = yes'),('socialist_constitution','Социалистическая конституция','Socialist Constitution','Определим пределы центральной власти и полномочия местных советов.','Define central authority and the powers of local councils.',{'state':{'power':0.10}},''),('eastern_trade_protocols','Восточные торговые протоколы','Eastern Trade Protocols','Согласуем контракты с принявшим союз партнёром.','Agree industrial contracts with the partner that accepted our alliance.',{'cop':{'output':0.05}},tech('industry')),('red_logistics_service','Красная служба снабжения','Red Logistics Service','Согласуем железнодорожные поставки и армейские склады.','Coordinate rail deliveries and army depots.',{'army':{'supply':-0.10}},''),('red_wisla','Красная Висла','The Red Vistula','Завершим восстановление институтов и обороны польской советской республики.','Complete institutional reconstruction and the defence of the Polish council republic.',{'state':{'stability':0.05},'army':{'org':0.05}},'')]
 for i,(s,r,e,rd,ed,b,reward) in enumerate(com):
  a='has_government = communism has_country_flag = POL_communist_victory has_civil_war = no'
  if s=='eastern_trade_protocols':a+=' has_country_flag = POL_eastern_alliance_accepted'
  n=add(s,r,e,rd,ed,68,4+i,'the_lodz_uprising' if i==0 else com[i-1][0],branch='communist',bonus=b,reward=reward,available=a)
  if s=='eastern_trade_protocols':n.update(x=70,y=10,parents=['POL_socialist_constitution'])
  if s=='red_logistics_service':n.update(x=66,y=10,parents=['POL_socialist_constitution'])
  if s=='red_wisla':n.update(x=68,y=11,parents=['POL_eastern_trade_protocols','POL_red_logistics_service'],or_parents=True)
 assert len(FOCUSES)==80,len(FOCUSES)


def write(path,text,bom=False):
 p=ROOT/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text.rstrip()+'\n',encoding='utf-8-sig' if bom else 'utf-8')


def generate(game):
 definitions()
 from polish_presentation import enhance_focuses
 enhance_focuses(FOCUSES)
 out=['# Owner: POL. Generated by tools/build_polish_content.py; see docs/POL_overhaul.md.','focus_tree = {','id = POL_focus','default = no','country = { factor = 0 modifier = { add = 100 tag = POL } }','initial_show_position = { focus = POL_aftermath_of_the_marshal }','continuous_focus_position = { x = 100 y = 3000 }']
 previous=None
 for f in FOCUSES:
  if f['branch']!=previous:out.append('# '+f['branch'].upper());previous=f['branch']
  loc(f['id'],f['ru'],f['en']);loc(f['id']+'_desc',f['ru_desc'],f['en_desc'])
  icons={'economy':'GFX_goal_generic_construct_civ_factory','army':'GFX_goal_generic_army_doctrines','air':'GFX_goal_generic_air_fighter','navy':'GFX_goal_generic_navy_doctrines_tactics','politics':'GFX_goal_generic_political_pressure','sanation':'GFX_goal_generic_neutrality_focus','endecja':'GFX_goal_support_fascism','german':'GFX_goal_generic_alliance','communist':'GFX_goal_support_communism'}
  a=['focus = {',f'id = {f["id"]}',f'icon = {f.get("icon", icons[f["branch"]])}',f'x = {f["x"]}',f'y = {f["y"]}',f'cost = {f["cost"]}','available_if_capitulated = no']
  if f.get('or_parents'):a.append('prerequisite = { '+' '.join('focus = '+p for p in f['parents'])+' }')
  else:a += [f'prerequisite = {{ focus = {p} }}' for p in f['parents']]
  if f['exclusive']:a.append('mutually_exclusive = { '+' '.join('focus = '+p for p in f['exclusive'])+' }')
  if f['available']:a.append('available = { '+f['available']+' }')
  reward=f['reward']
  if f.get('reward_note'):
   key=f['id']+'_reward_tt';loc(key,*f['reward_note']);reward+='\ncustom_effect_tooltip = '+key
  if f['bonus']:
   lines={'russian':[],'english':[]}
   for group,bonuses in f['bonus'].items():
    for param,value in bonuses.items():
     _,en,ru=GROUPS[group][2][param]
     amount=f'{value:+.2f}' if param=='power' else f'{value*100:+g}%'
     for lang,label in [('russian',ru),('english',en)]:lines[lang].append(label+': '+amount)
   for lang in ('russian','english'):
    LOCALE[f['id']+'_desc'][lang]+='\\n\\n'+('Изменение постоянной программы: ' if lang=='russian' else 'Persistent programme change: ')+'; '.join(lines[lang])+'.'
   key=f['id']+'_bonus_tt';loc(key,'; '.join(lines['russian'])+'.','; '.join(lines['english'])+'.')
   reward+='\ncustom_effect_tooltip = '+key+'\nhidden_effect = { set_country_flag = '+f['id']+'_reform_done POL_refresh_programs = yes }'
  a += ['completion_reward = { '+reward+' }']
  if f['extra']:a.append(f['extra'])
  else:a.append('ai_will_do = { factor = 1 }')
  a.append('}');out.extend(a)
 out.append('}')
 # Format generated data using the project's Clausewitz writer, preserving direct definitions.
 formatted=dump(parse('\n'.join(out)))
 for group,title in [('economy','ECONOMY: Central Industrial District and financing'),('army','ARMY: mobile or Vistula doctrine'),('air','AIR FORCE: domestic aviation'),('navy','NAVY: hidden until a controlled coastline exists'),('politics','POLITICS: common crisis preparation'),('sanation','SANATION: independent defensive republic'),('endecja','ENDECJA: prepared western campaign'),('german','GERMAN COMPACT: consent and ideological mandate'),('communist','COMMUNISTS: civil war and council republic')]:
  group_ids={f['id'] for f in FOCUSES if f['branch']==group}
  for ident in group_ids:
   needle='\tfocus = {\n\t\tid = '+ident+'\n'
   # Every focus begins with a small owner/branch label; scripts remain readable.
   formatted=formatted.replace(needle,'\t# '+title+'\n'+needle)
 write('common/national_focus/POL_focus.txt','# Owner: POL. NWW design: docs/POL_overhaul.md.\n'+formatted)
 # Replayable programs: pure reconstruction from focus progress, with no factory/PP rewards.
 effects=['# Owner: POL. Pure program reconstruction; one dynamic spirit per service.','POL_refresh_programs = {']
 dm=[]
 for group,(name,picture,params) in GROUPS.items():
  dm += [name+' = {','enable = { always = yes }','icon = GFX_idea_'+picture]
  for param,(modifier,en,ru) in params.items():
   var='POL_'+group+'_'+param;dm.append(modifier+' = '+var);effects.append(f'set_variable = {{ {var} = 0 }}')
  groupf=[f for f in FOCUSES if group in f['bonus']]
  for f in groupf:
   effects.append('if = { limit = { OR = { has_completed_focus = '+f['id']+' has_country_flag = '+f['id']+'_reform_done } }')
   for param,value in f['bonus'][group].items():effects.append(f'add_to_variable = {{ POL_{group}_{param} = {value:.2f} }}')
   effects.append('}')
  effects.append('if = { limit = { OR = { '+' '.join('has_completed_focus = '+f['id']+' has_country_flag = '+f['id']+'_reform_done' for f in groupf)+' } NOT = { has_dynamic_modifier = { modifier = '+name+' } } } add_dynamic_modifier = { modifier = '+name+' } }')
  dm.append('}')
 effects.append('POL_apply_policy_bonuses = yes')
 effects.append('}')
 write('common/scripted_effects/POL_program_effects.txt','# Owner: POL. Deterministic program repair.\n'+dump(parse('\n'.join(effects))))
 write('common/dynamic_modifiers/POL_modifiers.txt','# Owner: POL. Values are reconstructed from completed focuses.\n'+dump(parse('\n'.join(dm))))
 for name,ru,en,rd,ed in [('POL_cop_program','Центральный индустриальный округ','Central Industrial District','Единая промышленная программа на основе выбранного финансирования.','One industrial programme based on the chosen financing.'),('POL_army_program','Программа Войска Польского','Polish Army Programme','Постоянная программа выбранной доктрины и общего военного управления.','A persistent programme for the chosen doctrine and common military administration.'),('POL_air_program','Программа польской авиации','Polish Aviation Programme','Общие стандарты подготовки, связи и управления авиацией.','Common standards for air training, communications and command.'),('POL_state_program','Государственное устройство Польши','Polish State Institutions','Учреждения и политические решения избранного пути.','Institutions and policy choices of the selected path.')]:
  loc(name,ru,en);loc(name+'_desc',rd,ed)
 # Native focus registry: direct focus/shared_focus definitions only.
 native=read(game/'common/national_focus/poland.txt')
 ids={one(f,'id') for t in values(native,'focus_tree') for f in values(t,'focus')}
 ids|={one(f,'id') for f in values(native,'shared_focus')}
 ids-={f['id'] for f in FOCUSES}
 write('common/national_focus/POL_native_compatibility.txt','# Owner: POL. Detached direct native IDs, never nested event/province IDs.\n'+'\n'.join(f'shared_focus = {{ id = {i} cost = 10 allow_branch = {{ always = no }} available = {{ always = no }} completion_reward = {{ }} }}' for i in sorted(ids)))
 write('common/national_focus/poland.txt','# Owner: POL. Playable tree: POL_focus.txt. Native IDs: POL_native_compatibility.txt.')
 write('common/national_focus/POL_native_tree_alias.txt','# Owner: POL. Non-selectable alias for native compiled references.\nfocus_tree = { id = polish_focus country = { factor = 0 } default = no }')
 # Isolate native automatic strike/sanation/revolution chains while retaining event IDs.
 for filename in ('Poland.txt','NSB_Poland.txt'):
  doc=read(game/'events'/filename);out=[]
  for k,v,o in doc:
   if k=='add_namespace':out.append(f'add_namespace = {v}')
   elif k in ('country_event','news_event'):
    eid=one(v,'id');out.append(f'{k} = {{ id = {eid} is_triggered_only = yes hidden = yes trigger = {{ always = no }} option = {{ name = POL_native_event_disabled }} }}')
  write('events/'+filename,'# Owner: POL. Native event registry only; gameplay: POL_events.txt.\n'+'\n'.join(out))
 for path in ('common/ai_strategy/POL.txt','common/ai_strategy_plans/POL_historical_strategy_plan.txt','common/ai_strategy_plans/POL_alternate_strategy_plan.txt'):
  write(path,'# Owner: POL. Detached native subsystem; country-owned NWW definitions use the POL_ prefix.')
 # Native decisions remain inert but keep IDs used by cached missions and compiled effects.
 registry=[]
 category_fields={'allowed','visible','available','icon','priority','on_map_mode','scripted_gui','picture','highlight_states','state_target'}
 for category,body,op in read(game/'common/decisions/POL.txt'):
  if not isinstance(body,list):continue
  children=[]
  for name,decision,operator in body:
   if not isinstance(decision,list) or name in category_fields:continue
   definition='allowed = { always = no } visible = { always = no } available = { always = no } complete_effect = { } remove_effect = { }'
   if one(decision,'days_mission_timeout') is not None:definition+=' days_mission_timeout = 1 cancel_trigger = { always = yes }'
   else:definition+=' fire_only_once = yes'
   children.append(name+' = { '+definition+' }')
  if children:registry.append(category+' = { '+' '.join(children)+' }')
 write('common/decisions/POL.txt','# Owner: POL. Inert native decision/mission registry. Gameplay: POL_decisions.txt.\n'+dump(parse('\n'.join(registry))))
 # Country history: retain native equipment, DLC technology and named officers;
 # omit dated vanilla progression, indigenous sanation initialization and the navy.
 native=read(game/'history/countries/POL - Poland.txt');history=[]
 chars={'POL_ignacy_moscicki','POL_edward_rydzsmigly','POL_roman_dmowski','POL_maria_koszutska','POL_wladyslaw_gomulka','POL_wladyslaw_sikorski','POL_kazimierz_sosnkowski','POL_tadeusz_kutrzeba','POL_wladyslaw_anders','POL_stanislav_maczek','POL_jozef_zajac','POL_ludomil_rayski','POL_eugeniusz_kwiatkowiski','POL_marian_rejewski','POL_jozef_beck'}
 for k,v,o in native:
  if k=='if':
   if any(key=='has_dlc' and value=='Man the Guns' for key,value,operator in walk(one(v,'limit',[]))):continue
   keys={k for k,v,o in walk(v)}
   if keys & {'set_naval_oob','set_variable','add_ideas','recruit_character'}:continue
  elif k=='recruit_character':
   if v not in chars:continue
  elif k not in ('capital','oob','set_research_slots','set_technology','set_grand_doctrine','set_fuel_ratio','set_stability','set_war_support','create_equipment_variant'):continue
  history.append((k,v,o))
 history+=parse('''set_convoys = 0
set_politics = { ruling_party = neutrality elections_allowed = no election_frequency = 48 last_election = 1935.9.8 }
set_popularities = { neutrality = 45 democratic = 25 fascism = 15 communism = 15 }
set_stability = 0.55
set_war_support = 0.40
add_ideas = { limited_conscription limited_exports civilian_economy POL_german_economic_stranglehold POL_sanation_crisis POL_landlocked_nation }
set_country_flag = POL_nww_start_configured
''')
 write('history/countries/POL - Poland.txt','# Owner: POL. Independent, landlocked NWW republic; military technology/variants follow installed DLC.\n'+dump(history))
 # Silesia remains German in the NWW 1914 western border; retain indigenous cores.
 p=game/'history/states/762-Katowice.txt';doc=read(p);h=one(one(doc,'state'),'history')
 h[:]=[(k,'GER' if k=='owner' else v,o) for k,v,o in h];h.append(('add_core_of','GER','='))
 write('history/states/762-Katowice.txt','# Owner: POL/GER border setup. German 1914 sovereignty; Polish and Silesian cores retained.\n'+dump(doc))
 # Save the design manifest for graph, pricing, reward and repair validation.
 write('docs/POL_focus_design.json',json.dumps({'focus_count':len(FOCUSES),'focuses':FOCUSES,'programs':GROUPS},ensure_ascii=False,indent=2))
 # Hand-owned diplomacy, ideas and decisions have a separate localization dictionary.
 extra=ROOT/'tools/POL_localization.json'
 if extra.exists():LOCALE.update(json.loads(extra.read_text()))
 for lang in ('russian','english'):
  write(f'localisation/{lang}/POL_nww_l_{lang}.yml','l_'+lang+':\n'+'\n'.join(' '+k+':0 '+json.dumps(v[lang],ensure_ascii=False).replace('\\\\n','\\n') for k,v in LOCALE.items()),True)
 print(f'Built {len(FOCUSES)} POL focuses; {len(ids)} detached native focus IDs; deterministic programs and RU/EN localization')


if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--game',type=Path,default=Path.home()/'.local/share/Steam/steamapps/common/Hearts of Iron IV');generate(p.parse_args().game)
