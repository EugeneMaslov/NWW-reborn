"""NWW Austria: five political settlements, Danubian campaigns and crown lands."""
from pathlib import Path
from copy import deepcopy
import json,re
from hoi4_script import read,one,values,walk,parse,dump

ROOT=Path(__file__).resolve().parents[1]
GAME=Path('D:/Steam/steamapps/common/Hearts of Iron IV')
def save(path,doc):
    p=ROOT/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(dump(doc)+'\n',encoding='utf-8',newline='\n')
def put(node,key,value):
    node[:]=[n for n in node if n[0]!=key];node.append((key,value,'='))
def b(text):return parse(text)
LOC={}
def loc(key,ru,en):LOC[key]=(ru,en)
ICONS={'politics':'GFX_focus_generic_support_the_left_right','industry':'GFX_focus_generic_modernize_industry','army':'GFX_focus_generic_army_attack','air':'GFX_focus_generic_pilot_training','navy':'GFX_focus_generic_destroyer','research':'GFX_focus_research','diplomacy':'GFX_focus_generic_diplomatic_treaty'}

def main():
    path='common/national_focus/AUS_focuses.txt';doc=read(ROOT/path);tree=one(doc,'focus_tree')
    # Repeatable builder: only its own new focuses are regenerated. Legacy IDs,
    # hidden DLC compatibility imports and full-conquest rewards remain intact.
    tree[:]=[n for n in tree if not(n[0]=='focus' and one(n[1],'id','').startswith('AUS_nww2_'))]
    fs={one(f,'id'):f for f in values(tree,'focus')}
    def add(token,ru,en,x,y,parent=None,reward='',gate='',kind='politics',cost=10):
        fid='AUS_nww2_'+token
        node=b(f'id = {fid} x = {x} y = {y} cost = {cost} icon = {ICONS[kind]} available_if_capitulated = no completion_reward = {{ {reward} }} ai_will_do = {{ factor = 1 }}')
        if parent:put(node,'prerequisite',b(' '.join('focus = '+p for p in ([parent] if isinstance(parent,str) else parent))))
        if gate:put(node,'available',b(gate));put(node,'cancel_if_invalid','yes');put(node,'continue_if_invalid','no')
        tree.append(('focus',node,'='));fs[fid]=node
        loc(fid,ru,en)
        loc(fid+'_desc',f'{ru}. Программа получает отдельное финансирование и вводится через учреждения коронных земель.',f'{en}. Fund this program through the institutions of the crown lands.')
        return fid
    def move(fid,x,y,parent=None):
        n=fs[fid];put(n,'x',str(x));put(n,'y',str(y));n[:]=[e for e in n if e[0]!='prerequisite']
        if parent:put(n,'prerequisite',b('focus = '+parent))
    move('AUS_nww_rebuild',12,0);move('AUS_political_power',12,1,'AUS_nww_rebuild')
    loc('AUS_nww_rebuild','Дунайская корона в 1936 году','The Danubian Crown in 1936')
    loc('AUS_nww_rebuild_desc','Отто I удерживает венский престол, но прежняя общая монархия распалась. Определим отношения короны, общества и национальностей, прежде чем возвращать утраченные земли.','Otto I holds the Viennese throne, but the common monarchy has fragmented. Settle the relationship between crown, society and nationalities before recovering the lost crown lands.')
    loc('AUS_political_power','Совещание коронного совета','Conference of the Crown Council')
    loc('AUS_political_power_desc','Двор, партии и коронные земли должны получить возможность изложить свои требования. Итоги совещания станут отправной точкой пяти политических проектов.','The court, parties and crown lands must present their demands. This conference opens five competing political projects.')
    routes=[
        ('absolute','AUS_reinstate_the_imperial_council',0,'neutrality','Вся власть кайзеру','All Power to the Kaiser'),
        ('constitutional','AUS_hold_elections',6,'democratic','Кайзер и конституция','The Kaiser and the Constitution'),
        ('fascist','AUS_nww2_fascist_settlement',12,'fascism','Свергнуть Габсбурга: директория','Depose the Habsburg: Directorate'),
        ('communist','AUS_nww2_communist_settlement',18,'communism','Свергнуть Габсбурга: рабочая республика','Depose the Habsburg: Workers Republic'),
        ('alternative','AUS_nww2_alternative_settlement',24,'neutrality','Новая династия Лихтенштейнов','The Liechtenstein Alternative'),
    ]
    institutions={
        'absolute':[('cabinet','Личный кабинет кайзера','The Kaisers Cabinet'),('crown_service','Служба короне','Service to the Crown'),('provincial_diets','Земские сеймы под короной','Crown Provincial Diets'),('loyal_officers','Присяга офицерского корпуса','The Officers Oath'),('imperial_chancery','Имперская канцелярия','Imperial Chancellery'),('crown_law','Основной закон короны','Fundamental Law of the Crown')],
        'constitutional':[('responsible_ministry','Ответственное министерство','Responsible Ministry'),('parliament','Общеимперский парламент','Imperial Parliament'),('rights','Хартия гражданских прав','Charter of Civil Rights'),('coalition','Коалиционный кабинет','Coalition Cabinet'),('federal_court','Федеральный суд','Federal Court'),('constitutional_crown','Корона над партиями','The Crown Above Parties')],
        'fascist':[('directorate','Директория национального возрождения','National Renewal Directorate'),('corporations','Палаты корпораций','Corporate Chambers'),('veterans','Союз национальных добровольцев','Union of National Volunteers'),('propaganda','Дунайская пропагандистская служба','Danubian Information Service'),('security','Государственная охрана','State Security'),('national_state','Государство национальной мобилизации','National Mobilization State')],
        'communist':[('workers_councils','Советы промышленных городов','Industrial Workers Councils'),('land','Земельный закон республики','Republican Land Act'),('unions','Конгресс профсоюзов','Trade Union Congress'),('planning','Дунайская плановая комиссия','Danubian Planning Commission'),('nationalities','Совет национальностей','Council of Nationalities'),('social_republic','Социальная Дунайская республика','Social Danubian Republic')],
        'alternative':[('dynastic_pact','Договор новой династии','New Dynastic Compact'),('landed_elites','Землевладельцы и новая корона','Landowners and the New Crown'),('royal_guard','Гвардия Лихтенштейнов','Liechtenstein Guard'),('court_reform','Реформа двора','Court Reform'),('crown_diplomats','Дипломаты новой короны','Diplomats of the New Crown'),('succession_act','Акт о престолонаследии','Act of Succession')],
    }
    for route,entry,x,party,ru,en in routes:
        prep=add(route+'_debate',{'absolute':'Восстановить авторитет короны','constitutional':'Созвать конституционное совещание','fascist':'Собрать национальные лиги','communist':'Объединить рабочие комитеты','alternative':'Созвать династический конвент'}[route],route.title()+' Preparations',x,2,'AUS_political_power',reward=f'add_popularity = {{ ideology = {party} popularity = 0.10 }} add_political_power = 25',cost=5)
        reward=f'AUS_nww_install_{route} = yes add_ideas = AUS_nww_{route}_settlement add_stability = 0.05'
        if entry not in fs:add(route+'_settlement',ru,en,x,3,prep,reward=reward,gate=f'NOT = {{ {party} < 0.40 }}',cost=5)
        else:
            move(entry,x,3,prep);put(fs[entry],'completion_reward',b(reward));put(fs[entry],'available',b(f'NOT = {{ {party} < 0.40 }}'));loc(entry,ru,en)
            loc(entry+'_desc',f'{ru}. Для нового порядка требуется не менее 40% поддержки его сторонников.',f'{en}. The settlement requires at least 40% party support.')
        put(fs[entry],'mutually_exclusive',b(' '.join('focus = '+other for _,other,_,_,_,_ in routes if other!=entry)))
        previous=entry
        for i,(token,title,english) in enumerate(institutions[route]):
            rewards=['add_political_power = 100','add_stability = 0.05','AUS_nww_reduce_bohemian_tension = yes','add_war_support = 0.05','add_command_power = 30','add_political_power = 100 add_stability = 0.05']
            previous=add(route+'_'+token,title,english,x,4+i,previous,reward=rewards[i],gate=f'has_government = {party}')
    entries=[r[1] for r in routes]
    settled='OR = { '+' '.join('has_completed_focus = '+f for f in entries)+' }'
    # Foreign policy is shared by every political settlement.
    move('AUS_not_germany',42,0);put(fs['AUS_not_germany'],'available',b(settled));put(fs['AUS_not_germany'],'completion_reward',b('add_political_power = 75 add_war_support = 0.05'))
    loc('AUS_not_germany','Самостоятельная политика Вены','An Independent Viennese Policy')
    loc('AUS_not_germany_desc','При любом государственном строе Вена может добиваться объединения Дуная. Подготовим собственную внешнюю политику, сохраняя выбор между иностранными контрактами и самостоятельным курсом.','Every political settlement can pursue Danubian reunification. Prepare an independent foreign policy while retaining access to foreign contracts.')
    move('AUS_join_to_axis',39,1,'AUS_not_germany');move('AUS_help_from_eng',45,1,'AUS_not_germany')
    move('AUS_the_danubian_federation',36,2,'AUS_not_germany');move('AUS_via_danube_to_europe',36,3,'AUS_the_danubian_federation')
    for fid,y,parent in [('AUS_war_with_hun',2,'AUS_not_germany'),('AUS_war_with_croatia',3,'AUS_war_with_hun'),('AUS_reclaiming_yugoslavian_territories',4,'AUS_war_with_croatia'),('NWW_AUS_restore_dual_monarchy',5,'AUS_reclaiming_yugoslavian_territories')]:move(fid,42,y,parent)
    # Remove duplicated helper calls in the archived reward, retaining public IDs.
    for tag,fid in [('HUN','AUS_war_with_hun'),('CRO','AUS_war_with_croatia')]:
        put(fs[fid],'completion_reward',b(f'custom_effect_tooltip = NWW_AUS_{tag}_full_conquest_tt hidden_effect = {{ nww_AUS_prepare_{tag.lower()}_campaign = yes }}'))
    gal=add('galician_ultimatum','Галицийский ультиматум','The Galician Ultimatum',42,6,'NWW_AUS_restore_dual_monarchy',reward='set_country_flag = AUS_nww_galicia_pending POL = { country_event = { id = nww_aus_overhaul.10 days = 1 } }',gate='is_subject = no POL = { exists = yes is_subject = no } NOT = { has_war_with = POL } NOT = { is_ally_with = POL } OR = { 88 = { is_owned_and_controlled_by = POL } 89 = { is_owned_and_controlled_by = POL } 91 = { is_owned_and_controlled_by = POL } }',kind='diplomacy')
    buk=add('bukovina_ultimatum','Буковинский ультиматум','The Bukovinian Ultimatum',42,7,gal,reward='set_country_flag = AUS_nww_bukovina_pending ROM = { country_event = { id = nww_aus_overhaul.11 days = 1 } }',gate='is_subject = no ROM = { exists = yes is_subject = no } 80 = { is_owned_and_controlled_by = ROM } NOT = { has_war_with = ROM } NOT = { is_ally_with = ROM }',kind='diplomacy')
    west=add('german_competition','Оспорить первенство Берлина','Challenge Berlins Primacy',36,8,buk,reward='set_country_flag = AUS_nww_german_competition GER = { add_opinion_modifier = { target = AUS modifier = AUS_nww_rivalry } } add_war_support = 0.10',gate='GER = { exists = yes } NOT = { is_ally_with = GER }',kind='diplomacy')
    league=add('danubian_congress','Созвать Дунайский конгресс','Convene the Danubian Congress',48,8,buk,reward='if = { limit = { is_in_faction = no } create_faction = AUS_nww_danubian_league } add_political_power = 100',gate='is_subject = no OR = { is_in_faction = no is_faction_leader = yes }',kind='diplomacy')
    put(fs[west],'mutually_exclusive',b('focus = '+league));put(fs[league],'mutually_exclusive',b('focus = '+west))
    for i,(token,ru,en,reward) in enumerate([
        ('customs','Дунайский таможенный союз','Danubian Customs Union','add_to_variable = { AUS_economy_consumer_goods_factor = -0.05 }'),
        ('finance','Вена против Берлинской биржи','Vienna Against the Berlin Exchange','add_to_variable = { AUS_economy_industrial_capacity_factory = 0.05 }'),
        ('intelligence','Контрразведка на германской границе','Counterintelligence on the German Border','add_command_power = 40 add_stability = 0.05'),
        ('strategic_reserve','Западный стратегический резерв','Western Strategic Reserve','add_to_variable = { AUS_army_army_org_factor = 0.05 }'),
        ('sovereign_danube','Самостоятельная Дунайская держава','A Sovereign Danubian Power','add_political_power = 150 add_war_support = 0.10'),
        ('equal_empires','Переговоры равных империй','Negotiations Between Equal Empires','GER = { country_event = { id = nww_aus_overhaul.15 days = 1 } }'),
    ]):west=add(token,ru,en,36,9+i,west,reward=reward,kind='diplomacy')
    for i,tag in enumerate(('ROM','BUL','YUG')):
        league=add('invite_'+tag.lower(),'Пригласить '+{'ROM':'Румынию','BUL':'Болгарию','YUG':'Югославию'}[tag],f'Invite {tag} to the Congress',48,9+i,league,reward=f'{tag} = {{ country_event = {{ id = nww_aus_overhaul.12 days = 1 }} }}',gate=f'is_faction_leader = yes {tag} = {{ exists = yes is_subject = no is_in_faction = no }} NOT = {{ has_war_with = {tag} }}',kind='diplomacy')
    league=add('danubian_security','Коллективная безопасность Дуная','Danubian Collective Security',48,12,league,reward='add_war_support = 0.10 add_command_power = 40',kind='diplomacy')
    league=add('danubian_research','Дунайская научная комиссия','Danubian Scientific Commission',48,13,league,reward='add_tech_bonus = { bonus = 0.50 uses = 2 category = industry }',kind='research')
    add('crownland_administration','Администрация возвращённых земель','Administration of Recovered Lands',42,14,[gal,buk],reward='every_owned_state = { limit = { is_controlled_by = ROOT OR = { state = 88 state = 89 state = 91 state = 80 } } add_core_of = ROOT }',gate='OR = { 88 = { is_owned_and_controlled_by = AUS } 89 = { is_owned_and_controlled_by = AUS } 91 = { is_owned_and_controlled_by = AUS } 80 = { is_owned_and_controlled_by = AUS } }',kind='diplomacy')
    # Retain and relocate the industrial/army archive; no long root connectors.
    for fid,x,y,parent in [('AUS_nww_industry',64,0,None),('aus_prom',64,1,'AUS_nww_industry'),('aus_prom_2',64,2,'aus_prom'),('aus_prom_3',64,3,'aus_prom_2'),('aus_prom_4',64,4,'aus_prom_3'),('aus_prom_5',67,4,'aus_prom_3'),('AUS_new_economic',72,1,'AUS_nww_industry'),('AUS_reform_the_economic',72,2,'AUS_new_economic'),('AUS_create_a_new_econimic',72,3,'AUS_reform_the_economic'),('AUS_nww_army',88,0,None),('AUS_army_expierience',88,1,'AUS_nww_army'),('AUS_bring_generals_out_of_retirement',88,2,'AUS_army_expierience'),('AUS_establish_bohme_plan',88,3,'AUS_bring_generals_out_of_retirement')]:move(fid,x,y,parent)
    for root in ('AUS_nww_industry','AUS_nww_army'):put(fs[root],'available',b('has_completed_focus = AUS_nww_rebuild'))
    industry=[
        ('civilian',56,['Городские строительные артели','Жилищный фонд Вены','Земельный банк','Альпийские дороги','Дунайские грузовые пристани','Сельская электрификация','Лёгкая промышленность Моравии','Экспортные кооперативы','Общий гражданский рынок'],['Urban Building Cooperatives','Vienna Housing Fund','Land Bank','Alpine Roads','Danube Cargo Wharves','Rural Electrification','Moravian Light Industry','Export Cooperatives','Common Civilian Market']),
        ('military',62,['Единый оружейный заказ','Лицензии Штайра','Артиллерия Шкоды','Броневые стали','Патронные фабрики','Линии бронетехники','Военные грузовики','Рассеянные арсеналы','Военная промышленная палата'],['Unified Arms Orders','Steyr Licenses','Skoda Artillery','Armor Steel','Ammunition Factories','Armored Vehicle Lines','Military Trucks','Dispersed Arsenals','Military Industrial Chamber']),
        ('technology',78,['Совет технических университетов','Венская политехника','Инженерные стипендии','Лаборатории связи','Метрологические стандарты','Станкостроительные лаборатории','Авиационные материалы','Дунайская академия наук','Исследовательская держава'],['Technical Universities Council','Vienna Polytechnic','Engineering Scholarships','Radio Laboratories','Metrology Standards','Machine Tool Laboratories','Aviation Materials','Danubian Academy of Sciences','A Research Power']),
    ]
    for branch,x,titles,english in industry:
        parent='AUS_nww_industry'
        for i,(ru,en) in enumerate(zip(titles,english)):
            y=i+1 if branch!='military' else i+6
            reward='add_political_power = 50'
            if branch=='civilian':
                if i in (0,1,4,6):reward='AUS_nww_build_civilian = yes'
                elif i in (3,5):reward='every_owned_state = { limit = { is_controlled_by = ROOT is_core_of = ROOT infrastructure < 5 } add_building_construction = { type = infrastructure level = 1 instant_build = yes } }'
                elif i==8:reward='add_to_variable = { AUS_economy_consumer_goods_factor = -0.05 }'
                else:reward='add_to_variable = { AUS_economy_production_speed_buildings_factor = 0.05 }'
            elif branch=='military':
                if i in (0,2,4,6):reward='AUS_nww_build_military = yes'
                elif i in (3,5):reward='add_tech_bonus = { bonus = 0.50 uses = 1 category = armor }'
                elif i==8:reward='set_country_flag = AUS_nww_concerns_advanced add_to_variable = { AUS_economy_production_factory_max_efficiency_factor = 0.05 }'
                else:reward='add_to_variable = { AUS_economy_industrial_capacity_factory = 0.05 }'
            else:
                reward='add_tech_bonus = { bonus = 0.50 uses = 1 category = '+('electronics' if i%2 else 'industry')+' }'
                if i in (1,7):reward='if = { limit = { amount_research_slots < 5 } add_research_slot = 1 } else = { add_tech_bonus = { bonus = 0.50 uses = 2 category = industry } }'
                if i==8:reward='add_to_variable = { AUS_economy_research_speed_factor = 0.05 }'
            parent=add(branch+'_'+str(i+1),ru,en,x,y,parent,reward=reward,kind='research' if branch=='technology' else 'industry')
    army_titles=[['Горная школа Инсбрука','Штурмовые сапёры','Зимнее снабжение','Резерв горных частей','Альпийские укрепления','Щит коронных земель'],['Корпусная реформа Янсы','Штабные радиосети','Моторизованные колонны','Общевойсковые манёвры','Оперативные резервы','Единое сухопутное командование'],['Броневая комиссия','Школа механиков','Танковые радиостанции','Подвижная артиллерия','Складская система','Механизированный кулак']]
    army_stats=[['army_core_defence_factor','dig_in_speed_factor','supply_consumption_factor','army_org_factor','max_planning','army_defence_factor'],['army_org_factor','land_reinforce_rate','army_speed_factor','planning_speed','army_org_regain','army_attack_factor'],['army_armor_attack_factor','attrition','army_org_factor','army_artillery_attack_factor','supply_consumption_factor','breakthrough_factor']]
    army_english=[['Innsbruck Mountain School','Assault Engineers','Winter Supply','Mountain Reserves','Alpine Fortifications','Shield of the Crown Lands'],['Jansas Corps Reform','Staff Radio Networks','Motorized Columns','Combined Arms Exercises','Operational Reserves','Unified Land Command'],['Armor Commission','Mechanics School','Tank Radios','Mobile Artillery','Depot System','Mechanized Spearhead']]
    for col,x in enumerate((84,88,92)):
        parent='AUS_establish_bohme_plan'
        for i,title in enumerate(army_titles[col]):
            stat=army_stats[col][i];value='-0.05' if stat in ('attrition','supply_consumption_factor') else '0.02' if stat=='land_reinforce_rate' else '0.05'
            parent=add(f'army_{col}_{i}',title,army_english[col][i],x,i+4,parent,reward=f'add_to_variable = {{ AUS_army_{stat} = {value} }} army_experience = 15',kind='army')
    for service,x,kind,titles in [('air',104,'air',['Школа лётчиков','Истребительная инспекция','Радиолокационные посты','Перехватчики Альп','Служба воздушного наблюдения','Подготовка авиамехаников','Штурмовая авиация','Взаимодействие с армией','Прифронтовые аэродромы','Бомбардировочная комиссия','Дальняя разведка','Снабжение авиагрупп']),('navy',120,'navy',['Вернуть морской офицерский корпус','Кадетская школа Пулы','Служба корабельного ремонта','Адриатические верфи','Эсминцы сопровождения','Противолодочная подготовка','Морская авиация','Крейсерская доктрина','Адриатические манёвры','Конвойные маршруты','Прибрежные батареи','Объединённый Адриатический флот'])]:
        root=add(service+'_command','Воздушное командование Дуная' if service=='air' else 'Адмиралтейство Дуная','Danubian Air Command' if service=='air' else 'Danubian Admiralty',x,0,reward='add_command_power = 25',gate='has_completed_focus = AUS_nww_rebuild'+(' any_owned_state = { is_coastal = yes }' if service=='navy' else ''),kind=kind,cost=5)
        for col in range(3):
            parent=root
            for i in range(4):
                index=col*4+i
                stat=('air_mission_efficiency','air_accidents_factor','air_cas_efficiency')[col] if service=='air' else ('repair_speed_factor','convoy_escort_efficiency','naval_coordination')[col]
                val='-0.05' if stat=='air_accidents_factor' else '0.05'
                reward=f'add_to_variable = {{ AUS_{service}_{stat} = {val} }} '+('air_experience = 15' if service=='air' else 'navy_experience = 15')
                if service=='navy' and index==3:reward='AUS_nww_build_dockyard = yes'
                english={'air':['Flying School','Fighter Inspectorate','Radar Stations','Alpine Interceptors','Air Observation Service','Aircraft Mechanic Training','Assault Aviation','Army Cooperation','Forward Airfields','Bomber Commission','Long Range Reconnaissance','Air Group Supply'],'navy':['Recall the Naval Officers','Pula Cadet School','Ship Repair Service','Adriatic Shipyards','Escort Destroyers','Anti Submarine Training','Naval Aviation','Cruiser Doctrine','Adriatic Exercises','Convoy Routes','Coastal Batteries','United Adriatic Fleet']}[service][index]
                if service=='air' and index==8:reward+=' 4 = { if = { limit = { is_owned_and_controlled_by = ROOT } add_building_construction = { type = air_base level = 2 instant_build = yes } } }'
                parent=add(f'{service}_{index+1}',titles[index],english,x-4+col*4,i+1,parent,reward=reward,kind=kind)
        if service=='navy':
            one(fs[root],'completion_reward').extend(b('if = { limit = { has_dlc = "Man the Guns" } set_technology = { early_ship_hull_light = 1 basic_battery = 1 basic_torpedo = 1 } } else = { set_technology = { early_destroyer = 1 } }'))
    bohemia=[('language_charter','Языковая хартия Богемии','Bohemian Language Charter'),('prague_conference','Пражская конференция','Prague Conference'),('local_budget','Бюджеты коронных земель','Crown Land Budgets'),('land_compromise','Аграрный компромисс','Agrarian Compromise'),('technical_compact','Пльзеньский промышленный договор','Pilsen Industrial Compact'),('provincial_court','Суд коронных земель','Crown Lands Court'),('representation','Богемские делегаты в Вене','Bohemian Delegates in Vienna'),('crownland_settlement','Договор Богемской короны','Bohemian Crown Settlement')]
    parent=None
    for i,(token,title,english) in enumerate(bohemia):
        reward='AUS_nww_reduce_bohemian_tension = yes add_stability = 0.05'
        if i==7:reward+=' set_country_flag = AUS_nww_bohemia_settled remove_mission = AUS_nww_bohemian_drift'
        parent=add(token,title,english,30,i,parent,reward=reward,gate='9 = { is_owned_and_controlled_by = AUS } NOT = { has_country_flag = AUS_nww_bohemia_seceded }',cost=5 if i<2 else 10)
    modifier_ru={'consumer_goods_factor':'Товары народного потребления','production_speed_buildings_factor':'Скорость строительства','industrial_capacity_factory':'Производительность военных заводов','production_factory_max_efficiency_factor':'Максимальная эффективность производства','research_speed_factor':'Скорость исследований','army_core_defence_factor':'Защита на национальной территории','dig_in_speed_factor':'Скорость укрепления','supply_consumption_factor':'Потребление снабжения','army_org_factor':'Организация дивизий','max_planning':'Максимальный бонус планирования','army_defence_factor':'Защита дивизий','land_reinforce_rate':'Скорость пополнения боевого резерва','army_speed_factor':'Скорость дивизий','planning_speed':'Скорость планирования','army_org_regain':'Восстановление организации','army_attack_factor':'Атака дивизий','army_armor_attack_factor':'Атака бронетехники','attrition':'Потери от истощения','army_artillery_attack_factor':'Атака артиллерии','breakthrough_factor':'Прорыв','air_mission_efficiency':'Эффективность воздушных заданий','air_accidents_factor':'Вероятность авиапроисшествий','air_cas_efficiency':'Эффективность штурмовиков','repair_speed_factor':'Скорость ремонта','convoy_escort_efficiency':'Эффективность сопровождения конвоев','naval_coordination':'Координация флота'}
    for focus in values(tree,'focus'):
        for bonus in values(one(focus,'completion_reward',[]),'add_to_variable'):
            for variable,value,op in bonus[:]:
                if not variable.startswith(('AUS_economy_','AUS_army_','AUS_air_','AUS_navy_')):continue
                stat=re.sub(r'^AUS_(economy|army|air|navy)_','',variable)
                key='AUS_nww_bonus_'+stat+'_'+value.replace('-','minus').replace('.','_')
                put(bonus,'tooltip',key)
                percent=f'{float(value)*100:+.0f}%'
                loc(key,modifier_ru.get(stat,stat)+': '+percent,stat.replace('_',' ').title()+': '+percent)
        fid=one(focus,'id')
        if fid.startswith('AUS_nww2_') and fid in LOC:
            ru,en=LOC[fid];reward=one(focus,'completion_reward',[])
            bonus_keys=[one(n,'tooltip') for n in values(reward,'add_to_variable') if one(n,'tooltip')]
            if bonus_keys:
                loc(fid+'_desc',ru+'. '+ ' '.join(LOC[k][0]+'.' for k in bonus_keys)+' Улучшение становится частью постоянной программы соответствующего ведомства.',en+'. '+' '.join(LOC[k][1]+'.' for k in bonus_keys)+' This improvement becomes part of the permanent service program.')
    put(tree,'continuous_focus_position',b('x = 100 y = 3000'));save(path,doc)
    content(tree,routes)
    manifest_path=ROOT/'docs/legacy_import.json';manifest=json.loads(manifest_path.read_text(encoding='utf-8'))
    entry=manifest['countries']['AUS'];entry['focus_ids']=[one(f,'id') for f in values(tree,'focus')];entry['total']=len(entry['focus_ids'])
    manifest['content_files']=sorted(set(manifest['content_files'])|{
        'common/characters/AUS_nww_characters.txt','common/country_leader/AUS_traits.txt',
        'common/dynamic_modifiers/AUS_modifiers.txt','common/ideas/AUS_overhaul_ideas.txt',
        'common/on_actions/AUS_overhaul_on_actions.txt','common/scripted_effects/AUS_overhaul_effects.txt',
        'events/AUS_overhaul_events.txt','history/countries/AUS - Austria.txt',
        'common/military_industrial_organization/organizations/AUS_nww_organizations.txt',
    })
    manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
    (ROOT/'docs/AUS_overhaul.json').write_text(json.dumps({'playable_focuses':len(values(tree,'focus')),'political_routes':routes,'bohemian_states':[9,69,72,74,75],'galician_states':[88,89,91],'bukovina_state':80,'historical':'Habsburg absolutism; Hungary and Croatia full conquest; crown-land settlement'},ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
    print('Austria playable focuses:',len(values(tree,'focus')))

def content(tree,routes):
    # Implemented below so the tree and its mechanics are emitted together.
    mechanics(tree,routes)
    for lang,index in [('russian',0),('english',1)]:
        path=ROOT/f'localisation/replace/AUS_l_{lang}.yml';text=path.read_text(encoding='utf-8-sig')
        for key,pair in LOC.items():
            text=re.sub(r'^\s+'+re.escape(key)+r':[^\n]*\n','',text,flags=re.M)
            text+=f' {key}:0 "{pair[index]}"\n'
        path.write_text(text,encoding='utf-8-sig',newline='\n')

def mechanics(tree,routes):
    effects=[];initial={};dyn=[]
    # One persistent spirit per service; every completed focus is replayed on
    # migration. Factory rewards and foreign events are never replayed.
    for service in ('economy','army','air','navy'):
        stats={k.removeprefix('AUS_'+service+'_') for f in values(tree,'focus') for key,node,op in walk(one(f,'completion_reward',[])) if key=='add_to_variable' for k,v,o in node if k.startswith('AUS_'+service+'_')}
        defaults={'consumer_goods_factor':0.10,'production_speed_buildings_factor':-0.05,'industrial_capacity_factory':-0.05} if service=='economy' else {}
        stats|=defaults.keys()
        node=b('enable = { always = yes } icon = '+{'economy':'GFX_idea_generic_industrial_concern_1','army':'GFX_idea_generic_army_war_college','air':'GFX_idea_generic_air_bonus','navy':'GFX_idea_generic_navy_bonus'}[service])
        for stat in sorted(stats):
            var='AUS_'+service+'_'+stat;initial[var]=defaults.get(stat,0);node.append((stat,var,'='))
        dyn.append(('AUS_nww_'+service+'_development',node,'='))
        loc('AUS_nww_'+service+'_development',{'economy':'Дунайское промышленное развитие','army':'Имперская армия','air':'Дунайская авиация','navy':'Адриатический флот'}[service],service.title()+' Development')
        loc('AUS_nww_'+service+'_development_desc','Последовательная программа развивается через фокусы, сохраняя достигнутые улучшения.','Focus programs develop this persistent national spirit.')
    rebuild=[]
    for var,val in initial.items():rebuild.extend(b(f'set_variable = {{ {var} = {val:.4f} }}'))
    for f in values(tree,'focus'):
        bonuses=[(key,deepcopy(value),op) for key,value,op in one(f,'completion_reward',[]) if key=='add_to_variable' and any(k in initial for k,v,o in value)]
        if bonuses:rebuild.append(('if',b('limit = { has_completed_focus = '+one(f,'id')+' }')+bonuses,'='))
    for service in ('economy','army','air','navy'):rebuild.extend(b('if = { limit = { NOT = { has_dynamic_modifier = { modifier = AUS_nww_'+service+'_development } } } add_dynamic_modifier = { modifier = AUS_nww_'+service+'_development } }'))
    effects.append(('AUS_nww_rebuild_development',rebuild,'='));save('common/dynamic_modifiers/AUS_modifiers.txt',dyn)
    effects.extend(b('''AUS_nww_reduce_bohemian_tension = {
        subtract_from_variable = { AUS_bohemian_tension = 2 }
        clamp_variable = { var = AUS_bohemian_tension min = 0 max = 10 }
        AUS_nww_update_bohemian_spirit = yes
    }
    AUS_nww_update_bohemian_spirit = {
        set_variable = { AUS_bohemian_stability = AUS_bohemian_tension }
        multiply_variable = { AUS_bohemian_stability = -0.01 }
        set_variable = { AUS_bohemian_output = AUS_bohemian_tension }
        multiply_variable = { AUS_bohemian_output = -0.01 }
    }
    AUS_nww_initialize = {
        if = { limit = { NOT = { has_variable = AUS_bohemian_investments } } set_variable = { AUS_bohemian_investments = 0 } }
        if = { limit = { NOT = { has_country_flag = AUS_nww_overhaul_v1 } }
            AUS_nww_rebuild_development = yes
            if = { limit = { NOT = { has_variable = AUS_bohemian_tension } } set_variable = { AUS_bohemian_tension = 2 } }
            set_country_flag = AUS_nww_overhaul_v1
        }
        AUS_nww_update_bohemian_spirit = yes
        if = { limit = { 9 = { is_owned_by = AUS } NOT = { has_country_flag = AUS_nww_bohemia_settled } NOT = { has_country_flag = AUS_nww_bohemia_seceded } }
            if = { limit = { NOT = { has_active_mission = AUS_nww_bohemian_drift } } activate_mission = AUS_nww_bohemian_drift }
            if = { limit = { NOT = { has_dynamic_modifier = { modifier = AUS_nww_bohemian_question } } } add_dynamic_modifier = { modifier = AUS_nww_bohemian_question } }
        }
        if = { limit = { OR = { has_country_flag = AUS_nww_bohemia_settled has_country_flag = AUS_nww_bohemia_seceded NOT = { 9 = { is_owned_by = AUS } } } }
            remove_mission = AUS_nww_bohemian_drift
            remove_dynamic_modifier = { modifier = AUS_nww_bohemian_question }
        }
    }'''))
    dyn=read(ROOT/'common/dynamic_modifiers/AUS_modifiers.txt')
    dyn.extend(b('AUS_nww_bohemian_question = { enable = { always = yes } icon = GFX_idea_generic_constitutional_guarantees stability_factor = AUS_bohemian_stability industrial_capacity_factory = AUS_bohemian_output }'));save('common/dynamic_modifiers/AUS_modifiers.txt',dyn)
    loc('AUS_nww_bohemian_question','Богемия желает отделиться','Bohemia Demands Independence')
    loc('AUS_nww_bohemian_question_desc','С ростом напряжённости падают стабильность и выпуск заводов. На уровне 10 Богемия выходит из состава государства.','Rising tension reduces stability and factory output. At level 10 Bohemia secedes.')
    for building,token in [('industrial_complex','civilian'),('arms_factory','military'),('dockyard','dockyard')]:
        coast=' is_coastal = yes' if token=='dockyard' else ''
        effects.extend(b(f'AUS_nww_build_{token} = {{ random_owned_controlled_state = {{ limit = {{ is_core_of = PREV {coast} }} add_extra_state_shared_building_slots = 1 add_building_construction = {{ type = {building} level = 1 instant_build = yes }} }} }}'))
    # Otto I inherited the crown after Karl withdrew from public life in 1930;
    # there was no wartime abdication or postwar restoration in NWW.
    portraits={'absolute':'GFX_Portrait_hungary_otto_von_hapsburg','constitutional':'GFX_Portrait_hungary_otto_von_hapsburg','fascist':'GFX_portrait_AUS_ernst_rudiger_starhemberg','communist':'GFX_portrait_AUS_johann_koplenig','alternative':'GFX_portrait_AUS_johannes_von_liechtenstein'}
    leader_names={'absolute':'AUS_nww_otto_i','constitutional':'AUS_nww_otto_i','fascist':'AUS_nww_starhemberg','communist':'AUS_nww_koplenig','alternative':'AUS_nww_johannes_i'}
    for route,entry,x,party,ru,en in routes:
        ideology={'absolute':'despotism','constitutional':'conservatism','fascist':'fascism_ideology','communist':'leninism','alternative':'despotism'}[route]
        effects.extend(b(f'''AUS_nww_install_{route} = {{
            retire_ideology_leader = {party}
            create_country_leader = {{ name = {leader_names[route]} picture = {portraits[route]} ideology = {ideology} traits = {{ AUS_nww_{route}_leader }} }}
            set_politics = {{ ruling_party = {party} elections_allowed = {'yes' if route=='constitutional' else 'no'} }}
            set_country_flag = AUS_nww_political_settlement
        }}'''))
    secession='set_country_flag = AUS_nww_bohemia_seceded remove_mission = AUS_nww_bohemian_drift remove_dynamic_modifier = { modifier = AUS_nww_bohemian_question } '
    for sid in (9,69,72,74,75):secession+=f'if = {{ limit = {{ {sid} = {{ is_owned_and_controlled_by = AUS }} }} {sid} = {{ add_core_of = CZE transfer_state_to = CZE }} }} '
    secession+='CZE = { set_cosmetic_tag = AUS_nww_bohemia set_politics = { ruling_party = democratic elections_allowed = yes } set_stability = 0.60 } add_stability = -0.10'
    effects.append(('AUS_nww_release_bohemia',b(secession),'='));save('common/scripted_effects/AUS_overhaul_effects.txt',effects)
    save('common/on_actions/AUS_overhaul_on_actions.txt',b('''on_actions = {
        on_startup = { effect = { AUS = { if = { limit = { exists = yes has_focus_tree = AUS_focus } AUS_nww_initialize = yes } } } }
        on_daily_AUS = { effect = { if = { limit = { has_focus_tree = AUS_focus } AUS_nww_initialize = yes } } }
    }'''))
    categories=b('''AUS_nww_crown_lands = {
        icon = GFX_decision_category_generic_political_actions allowed = { original_tag = AUS }
        visible = { 9 = { is_owned_by = AUS } NOT = { has_country_flag = AUS_nww_bohemia_settled } NOT = { has_country_flag = AUS_nww_bohemia_seceded } }
    }
    AUS_nww_political_mandate = { icon = GFX_decision_category_generic_political_actions allowed = { original_tag = AUS } visible = { NOT = { has_country_flag = AUS_nww_political_settlement } } }''')
    for key,node,op in read(ROOT/'common/decisions/categories/AUS_categories.txt'):
        if key.startswith('NWW_'):categories.append((key,node,op))
    save('common/decisions/categories/AUS_categories.txt',categories)
    dec=b('''AUS_nww_crown_lands = {
        AUS_nww_bohemian_drift = {
            icon = generic_political_discourse activation = { always = no } available = { always = no }
            selectable_mission = no days_mission_timeout = 60 cancel_if_not_visible = yes
            visible = { 9 = { is_owned_by = AUS } NOT = { has_country_flag = AUS_nww_bohemia_settled } NOT = { has_country_flag = AUS_nww_bohemia_seceded } }
            timeout_effect = {
                if = { limit = { NOT = { has_country_flag = AUS_nww_bohemia_settled } NOT = { has_country_flag = AUS_nww_bohemia_seceded } 9 = { is_owned_by = AUS } }
                    add_to_variable = { AUS_bohemian_tension = 1 }
                    clamp_variable = { var = AUS_bohemian_tension min = 0 max = 10 }
                    AUS_nww_update_bohemian_spirit = yes
                    if = { limit = { check_variable = { var = AUS_bohemian_tension value = 10 compare = greater_than_or_equals } } country_event = { id = nww_aus_overhaul.1 } }
                    else = { remove_mission = AUS_nww_bohemian_drift activate_mission = AUS_nww_bohemian_drift }
                }
            }
        }
        AUS_nww_prague_negotiations = {
            icon = generic_political_discourse cost = 50 days_remove = 20 days_re_enable = 0
            visible = { NOT = { has_country_flag = AUS_nww_bohemia_seceded } NOT = { has_country_flag = AUS_nww_bohemia_settled } }
            available = { 9 = { is_owned_and_controlled_by = AUS } check_variable = { AUS_bohemian_tension > 0 } }
            remove_effect = { if = { limit = { NOT = { has_country_flag = AUS_nww_bohemia_seceded } } AUS_nww_reduce_bohemian_tension = yes } }
            ai_will_do = { base = 1 modifier = { factor = 20 check_variable = { var = AUS_bohemian_tension value = 5 compare = greater_than_or_equals } } }
        }
        AUS_nww_prague_investment = {
            icon = generic_industry cost = 75 days_remove = 35 days_re_enable = 30
            visible = { NOT = { has_country_flag = AUS_nww_bohemia_seceded } NOT = { has_country_flag = AUS_nww_bohemia_settled } }
            available = { 9 = { is_owned_and_controlled_by = AUS } check_variable = { AUS_bohemian_investments < 3 } }
            remove_effect = { if = { limit = { 9 = { is_owned_and_controlled_by = AUS } NOT = { has_country_flag = AUS_nww_bohemia_seceded } }
                AUS_nww_reduce_bohemian_tension = yes
                add_to_variable = { AUS_bohemian_investments = 1 }
                9 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }
            } }
            ai_will_do = { base = 1 }
        }
    }
    AUS_nww_political_mandate = { }''')
    mandates=one(dec,'AUS_nww_political_mandate')
    for party in ('neutrality','democratic','fascism','communism'):
        mandates.extend(b(f'AUS_nww_campaign_{party} = {{ icon = generic_political_discourse cost = 25 days_remove = 20 days_re_enable = 0 available = {{ NOT = {{ has_country_flag = AUS_nww_political_settlement }} }} remove_effect = {{ add_popularity = {{ ideology = {party} popularity = 0.10 }} }} ai_will_do = {{ base = 0 }} }}'))
        loc('AUS_nww_campaign_'+party,{'neutrality':'Кампания сторонников монархии','democratic':'Конституционная кампания','fascism':'Кампания национальных лиг','communism':'Кампания рабочих комитетов'}[party],party.title()+' Campaign')
        loc('AUS_nww_campaign_'+party+'_desc','За 20 дней кампания добавит 10 процентных пунктов поддержки.','After twenty days, gain ten percentage points of party support.')
    for key,node,op in read(ROOT/'common/decisions/AUS_decisions.txt'):
        if key.startswith('NWW_'):dec.append((key,node,op))
    save('common/decisions/AUS_decisions.txt',dec)
    for key,ru,en in [('AUS_nww_crown_lands','Богемия и коронные земли','Bohemia and the Crown Lands'),('AUS_nww_bohemian_drift','Богемия желает отделиться: [?AUS_bohemian_tension|0]/10','Bohemian Separatism: [?AUS_bohemian_tension|0]/10'),('AUS_nww_prague_negotiations','Переговоры с Прагой','Negotiate with Prague'),('AUS_nww_prague_investment','Инвестировать в Богемию','Invest in Bohemia'),('AUS_nww_political_mandate','Борьба за государственный строй','The Political Settlement')]:
        loc(key,ru,en);loc(key+'_desc','Каждые 30 дней напряжённость растёт на 1. При 10 Богемия отделяется. Переговоры снижают её на 2 после 20 дней; инвестиции создают фабрику и снижают напряжённость на 2 после 35 дней.','Every thirty days tension rises by one. At ten Bohemia secedes. Negotiations reduce it by two after twenty days; investment builds a factory and reduces it by two after thirty-five days.')
    events=b('''add_namespace = nww_aus_overhaul
        country_event = { id = nww_aus_overhaul.1 title = nww_aus_overhaul.1.t desc = nww_aus_overhaul.1.d
            picture = GFX_report_event_election_vote is_triggered_only = yes
            trigger = { tag = AUS NOT = { has_country_flag = AUS_nww_bohemia_settled } NOT = { has_country_flag = AUS_nww_bohemia_seceded } check_variable = { var = AUS_bohemian_tension value = 10 compare = greater_than_or_equals } 9 = { is_owned_and_controlled_by = AUS } }
            immediate = { AUS_nww_release_bohemia = yes }
            option = { name = nww_aus_overhaul.1.a add_political_power = -50 }
            option = { name = nww_aus_overhaul.1.b create_wargoal = { type = annex_everything target = CZE } add_war_support = 0.05 }
        }
    ''')
    loc('nww_aus_overhaul.1.t','Богемия объявляет независимость','Bohemia Declares Independence')
    loc('nww_aus_overhaul.1.d','Переговоры сорваны. Пражский сейм отверг власть Вены и провозгласил независимое государство коронных земель.','Negotiations have collapsed. The Prague Diet rejects Viennas authority and proclaims an independent crown-land state.')
    loc('nww_aus_overhaul.1.a','Признать свершившийся факт','Accept the Separation');loc('nww_aus_overhaul.1.b','Подготовить возвращение коронных земель','Prepare to Recover the Crown Lands')
    for num,target,states,flag,title in [(10,'POL',[88,89,91],'galicia','Галиция'),(11,'ROM',[80],'bukovina','Буковина')]:
        owned='OR = { '+' '.join(f'{sid} = {{ is_owned_and_controlled_by = {target} }}' for sid in states)+' }'
        acceptance=' '.join(f'if = {{ limit = {{ {sid} = {{ is_owned_and_controlled_by = ROOT }} }} {sid} = {{ transfer_state_to = AUS add_claim_by = AUS }} }}' for sid in states)
        events.extend(b(f'''country_event = {{ id = nww_aus_overhaul.{num} title = nww_aus_overhaul.{num}.t desc = nww_aus_overhaul.{num}.d
            picture = GFX_report_event_election_vote is_triggered_only = yes
            trigger = {{ tag = {target} AUS = {{ exists = yes is_subject = no has_country_flag = AUS_nww_{flag}_pending }} NOT = {{ has_war_with = AUS }} is_subject = no }}
            option = {{ name = nww_aus_overhaul.{num}.a trigger = {{ {owned} NOT = {{ has_war_with = AUS }} AUS = {{ exists = yes }} }} ai_chance = {{ factor = 25 }}
                {acceptance} AUS = {{ clr_country_flag = AUS_nww_{flag}_pending add_stability = 0.05 }}
            }}
            option = {{ name = nww_aus_overhaul.{num}.b ai_chance = {{ factor = 75 }}
                AUS = {{ clr_country_flag = AUS_nww_{flag}_pending if = {{ limit = {{ NOT = {{ has_war_with = {target} }} NOT = {{ is_ally_with = {target} }} }} create_wargoal = {{ type = take_state target = {target} generator = {{ {' '.join(map(str,states))} }} }} }} }}
            }}
        }}'''))
        loc(f'nww_aus_overhaul.{num}.t',title+': ультиматум Вены','The Viennese Territorial Ultimatum')
        loc(f'nww_aus_overhaul.{num}.d','Вена требует передачи бывших коронных земель. Мы можем принять требование или рискнуть войной; чужие и оккупированные регионы переданы не будут.','Vienna demands the former crown lands. Accept or risk war. Only territory we currently own and control can be ceded.')
        loc(f'nww_aus_overhaul.{num}.a','Уступить требуемые земли','Cede the Requested Territory');loc(f'nww_aus_overhaul.{num}.b','Отклонить ультиматум','Reject the Ultimatum')
    events.extend(b('''country_event = { id = nww_aus_overhaul.12 title = nww_aus_overhaul.12.t desc = nww_aus_overhaul.12.d picture = GFX_report_event_election_vote is_triggered_only = yes
        trigger = { AUS = { exists = yes is_faction_leader = yes } is_subject = no is_in_faction = no NOT = { has_war_with = AUS } }
        option = { name = nww_aus_overhaul.12.a trigger = { is_subject = no is_in_faction = no NOT = { has_war_with = AUS } AUS = { is_faction_leader = yes } } ai_chance = { factor = 60 } AUS = { add_to_faction = ROOT } }
        option = { name = nww_aus_overhaul.12.b ai_chance = { factor = 40 } }
    }
    country_event = { id = nww_aus_overhaul.15 title = nww_aus_overhaul.15.t desc = nww_aus_overhaul.15.d picture = GFX_report_event_election_vote is_triggered_only = yes
        trigger = { tag = GER AUS = { exists = yes } NOT = { has_war_with = AUS } }
        option = { name = nww_aus_overhaul.15.a trigger = { NOT = { has_war_with = AUS } } ai_chance = { factor = 50 } add_stability = 0.05 AUS = { add_stability = 0.05 add_tech_bonus = { bonus = 0.50 uses = 1 category = industry } } }
        option = { name = nww_aus_overhaul.15.b ai_chance = { factor = 50 } AUS = { add_war_support = 0.05 } }
    }'''))
    for num,ru,en,desc in [(12,'Приглашение на Дунайский конгресс','Invitation to the Danubian Congress','Вена предлагает военный союз равных государств. Вступление возможно только с нашего согласия.'),(15,'Вена предлагает договор равных','Vienna Proposes a Treaty of Equals','Австрия предлагает признать два равных центра европейской политики и начать промышленное сотрудничество.')]:
        loc(f'nww_aus_overhaul.{num}.t',ru,en);loc(f'nww_aus_overhaul.{num}.d',desc,'Vienna proposes cooperation between sovereign partners. The recipient can accept or refuse.');loc(f'nww_aus_overhaul.{num}.a','Принять предложение','Accept the Offer');loc(f'nww_aus_overhaul.{num}.b','Отклонить предложение','Decline the Offer')
    save('events/AUS_overhaul_events.txt',events)
    opinion=read(ROOT/'common/opinion_modifiers/AUS_opinions.txt')
    put(one(opinion,'opinion_modifiers'),'AUS_nww_rivalry',b('value = -50'));save('common/opinion_modifiers/AUS_opinions.txt',opinion);loc('AUS_nww_rivalry','Соперничество за Центральную Европу','Central European Rivalry')
    loc('AUS_nww_danubian_league','Дунайская лига','Danubian League');loc('AUS_nww_bohemia','Богемия','Bohemia');loc('AUS_nww_bohemia_DEF','Богемия','Bohemia');loc('AUS_nww_bohemia_ADJ','Богемск.','Bohemian')
    for party,ru,en,long_ru,long_en in [
        ('neutrality','КС','CC','Коронный совет','Crown Council'),
        ('democratic','КБ','CB','Конституционный блок','Constitutional Bloc'),
        ('fascism','НЛ','NL','Национальные лиги Дуная','National Leagues of the Danube'),
        ('communism','СРС','UWC','Союз рабочих советов','Union of Workers Councils'),
    ]:
        loc('AUS_'+party+'_party',ru,en);loc('AUS_'+party+'_party_long',long_ru,long_en)
    leaders={'absolute':'political_power_factor = 0.10','constitutional':'stability_factor = 0.10','fascist':'war_support_factor = 0.10','communist':'industrial_capacity_factory = 0.10','alternative':'political_power_gain = 0.20'}
    traits=b('leader_traits = { '+' '.join(f'AUS_nww_{key}_leader = {{ random = no sprite = 15 {mods} }}' for key,mods in leaders.items())+' }')
    for route,entry,x,party,ru,en in routes:loc('AUS_nww_'+route+'_leader',ru,en)
    save('common/country_leader/AUS_traits.txt',traits)
    ideas=b('ideas = { country = { } industrial_concern = { } }')
    policies={'absolute':'political_power_factor = 0.10 war_support_factor = 0.05 consumer_goods_factor = 0.05','constitutional':'stability_factor = 0.10 consumer_goods_factor = -0.05','fascist':'army_attack_factor = 0.10 stability_factor = -0.05','communist':'industrial_capacity_factory = 0.10 conscription = 0.02','alternative':'political_power_factor = 0.10 trade_opinion_factor = 0.10'}
    for route,mods in policies.items():
        one(one(ideas,'ideas'),'country').extend(b(f'AUS_nww_{route}_settlement = {{ picture = generic_constitutional_guarantees allowed = {{ original_tag = AUS }} removal_cost = -1 modifier = {{ {mods} }} }}'))
        loc('AUS_nww_'+route+'_settlement',{'absolute':'Абсолютная власть Габсбурга','constitutional':'Конституционная монархия','fascist':'Национальная директория','communist':'Дунайская рабочая республика','alternative':'Лихтенштейнская монархия'}[route],route.title()+' Settlement')
        loc('AUS_nww_'+route+'_settlement_desc','Государственный строй определяет соотношение короны, общества и армии.','The political settlement defines the relationship between society, the crown and the armed forces.')
    for token,name,english,focus,mods,category in [
        ('steyr','Штайр','Steyr','AUS_nww2_military_2','industrial_capacity_factory = 0.10 production_factory_max_efficiency_factor = 0.05','infantry_weapons'),
        ('skoda','Шкода','Skoda','AUS_nww2_military_3','production_speed_arms_factory_factor = 0.10','artillery'),
        ('siemens','Австрийская электротехническая сеть','Austrian Electrical Consortium','AUS_nww2_technology_4','production_speed_buildings_factor = 0.10','electronics')]:
        one(one(ideas,'ideas'),'industrial_concern').extend(b(f'AUS_nww_{token}_concern = {{ picture = generic_industrial_concern_1 allowed = {{ original_tag = AUS }} available = {{ has_completed_focus = {focus} }} cost = 150 research_bonus = {{ {category} = 0.15 }} modifier = {{ {mods} }} }}'))
        loc('AUS_nww_'+token+'_concern',name,english)
    save('common/ideas/AUS_overhaul_ideas.txt',ideas)
    mios=[]
    for token,template,focus in [('steyr','generic_infantry_equipment_organization','AUS_nww2_military_2'),('skoda','generic_artillery_organization','AUS_nww2_military_3'),('siemens','generic_general_aircraft_organization','AUS_nww2_technology_4')]:
        mios.extend(b(f'AUS_nww_{token}_organization = {{ include = {template} icon = GFX_idea_generic_industrial_concern_1 allowed = {{ original_tag = AUS }} available = {{ FROM = {{ has_completed_focus = {focus} }} }} initial_trait = {{ name = AUS_nww_{token}_organization_trait organization_modifier = {{ military_industrial_organization_research_bonus = 0.10 }} production_bonus = {{ production_efficiency_cap_factor = 0.05 }} }} add_trait = {{ token = AUS_nww_{token}_advanced name = AUS_nww_{token}_advanced icon = GFX_generic_mio_trait_icon_production_capacity position = {{ x = 13 y = 0 }} special_trait_background = yes available = {{ FROM = {{ has_country_flag = AUS_nww_concerns_advanced }} }} equipment_bonus = {{ reliability = 0.05 }} production_bonus = {{ production_efficiency_cap_factor = 0.05 }} }} }}'))
        loc('AUS_nww_'+token+'_organization',{'steyr':'Вооружение Штайра','skoda':'Артиллерийские заводы Шкоды','siemens':'Дунайская электротехническая сеть'}[token],token.title()+' Organization')
        loc('AUS_nww_'+token+'_organization_trait','Коронный промышленный заказ','Crown Industrial Orders')
        loc('AUS_nww_'+token+'_advanced','Серийный стандарт промышленной палаты','Industrial Chamber Series Standard')
    save('common/military_industrial_organization/organizations/AUS_nww_organizations.txt',mios)
    characters(tree)
    history_path='history/countries/AUS - Austria.txt';history=read(ROOT/history_path)
    # Remove native WUW initialization, retaining equipment and early technology.
    for key,node,op in history[:]:
        if isinstance(node,list) and any(k=='AUS_set_austrofascism_defaults' for k,v,o in walk(node)):
            history.remove((key,node,op))
    history[:]=[n for n in history if n[0] not in ('create_country_leader','AUS_nww_install_absolute')]
    history.extend(b('AUS_nww_install_absolute = yes clr_country_flag = AUS_nww_political_settlement'))
    save(history_path,history)
    # Historical order preserves the Kaiser and prepares the Hungarian campaign.
    path='common/ai_strategy_plans/AUS_historical.txt';plan=read(ROOT/path);node=plan[0][1]
    order=['AUS_nww_rebuild','AUS_political_power','AUS_nww2_absolute_debate','AUS_reinstate_the_imperial_council','AUS_not_germany','AUS_nww_army','AUS_army_expierience','AUS_bring_generals_out_of_retirement','AUS_nww2_language_charter','AUS_nww2_prague_conference','AUS_nww_industry','AUS_war_with_hun','AUS_establish_bohme_plan','AUS_war_with_croatia','AUS_reclaiming_yugoslavian_territories','NWW_AUS_restore_dual_monarchy','AUS_nww2_local_budget','AUS_nww2_land_compromise','AUS_nww2_technical_compact','AUS_nww2_provincial_court','AUS_nww2_representation','AUS_nww2_crownland_settlement','AUS_nww2_galician_ultimatum','AUS_nww2_bukovina_ultimatum','AUS_nww2_german_competition']
    put(node,'ai_national_focuses',b(' '.join(order)));put(node,'focus_factors',b('AUS_the_danubian_federation = 0 AUS_hold_elections = 0 AUS_nww2_fascist_settlement = 0 AUS_nww2_communist_settlement = 0 AUS_nww2_alternative_settlement = 0'));save(path,plan)

def characters(tree):
    chars=[];traits=one(read(ROOT/'common/country_leader/AUS_traits.txt'),'leader_traits')
    gamechars=one(read(GAME/'common/characters/AUS.txt'),'characters')
    roster=[('AUS_alfred_jansa','Альфред Янса','Alfred Jansa','army_chief','army_org_factor = 0.10'),('AUS_franz_bohme','Франц Бёме','Franz Bohme','high_command','army_infantry_attack_factor = 0.10 army_infantry_defence_factor = 0.10'),('AUS_eugen_beyer','Ойген Бейер','Eugen Beyer','high_command','supply_consumption_factor = -0.15'),('AUS_karl_renner','Карл Реннер','Karl Renner','political_advisor','stability_factor = 0.10'),('AUS_julius_raab','Юлиус Рааб','Julius Raab','political_advisor','production_speed_buildings_factor = 0.10'),('AUS_ludwig_von_mises','Людвиг фон Мизес','Ludwig von Mises','political_advisor','consumer_goods_factor = -0.05'),('AUS_johann_koplenig','Иоганн Коплениг','Johann Koplenig','political_advisor','industrial_capacity_factory = 0.10'),('AUS_ernst_rudiger_starhemberg','Эрнст Рюдигер Штаремберг','Ernst Rudiger Starhemberg','political_advisor','war_support_factor = 0.10'),('AUS_alexander_lohr','Александр Лёр','Alexander Lohr','air_chief','air_mission_efficiency = 0.10'),('AUS_marianne_pollak','Марианна Поллак','Marianne Pollak','political_advisor','research_speed_factor = 0.05'),('AUS_alfred_ritter_von_hubicki','Альфред фон Губицки','Alfred von Hubicki','high_command','army_armor_attack_factor = 0.10'),('AUS_gottfried_freiherr_von_banfeld','Готфрид фон Банфильд','Gottfried von Banfield','navy_chief','naval_coordination = 0.10')]
    history_path='history/countries/AUS - Austria.txt';history=read(ROOT/history_path)
    for i,(source,ru,en,slot,mods) in enumerate(roster):
        cid='AUS_nww_staff_'+str(i);trait=cid+'_trait'
        char=b(f'name = {cid}')
        source_node=one(gamechars,source,[])
        portraits=deepcopy(next((v for k,v,o in walk(source_node) if k=='portraits'),[]))
        if not portraits:portraits=b('civilian = { small = GFX_idea_generic_political_advisor_europe_1 }')
        put(char,'portraits',portraits)
        put(char,'advisor',b(f'slot = {slot} idea_token = {cid} cost = 150 allowed = {{ original_tag = AUS }} traits = {{ {trait} }}'))
        if slot=='high_command':put(one(char,'advisor'),'ledger','army')
        if i==0:
            put(char,'field_marshal',b('skill = 5 attack_skill = 3 defense_skill = 5 planning_skill = 5 logistics_skill = 4 traits = { defensive_doctrine organizer }'))
        elif i<3 or i==10:
            put(char,'corps_commander',b('skill = 4 attack_skill = 3 defense_skill = 4 planning_skill = 4 logistics_skill = 3 traits = { infantry_officer hill_fighter }'))
        if i==10:put(one(char,'corps_commander'),'traits',b('panzer_leader organizer'))
        if i==11:put(char,'navy_leader',b('skill = 3 attack_skill = 3 defense_skill = 3 maneuvering_skill = 4 coordination_skill = 4 traits = { spotter superior_tactician } visible = { has_completed_focus = AUS_nww2_navy_command }'))
        chars.append((cid,char,'='));traits.extend(b(f'{trait} = {{ random = no sprite = 15 {mods} }}'))
        if cid not in values(history,'recruit_character'):history.extend(b('recruit_character = '+cid))
        loc(cid,ru,en);loc(trait,{'army_chief':'Начальник имперского штаба','high_command':'Специалист генерального штаба','political_advisor':'Представитель Дунайского кабинета','air_chief':'Руководитель воздушного штаба','navy_chief':'Руководитель Адриатического флота'}[slot],slot.replace('_',' ').title())
    save('common/characters/AUS_nww_characters.txt',[('characters',chars,'=')]);save('common/country_leader/AUS_traits.txt',[('leader_traits',traits,'=')]);save(history_path,history)
    loc('AUS_nww_otto_i','Отто I Габсбург','Otto I von Habsburg');loc('AUS_nww_starhemberg','Эрнст Рюдигер Штаремберг','Ernst Rudiger Starhemberg');loc('AUS_nww_koplenig','Иоганн Коплениг','Johann Koplenig');loc('AUS_nww_johannes_i','Иоганн I Лихтенштейн','Johannes I von Liechtenstein')

if __name__=='__main__':
    main()
    from repair_campaign_order_and_crown import repair_austria
    repair_austria()
