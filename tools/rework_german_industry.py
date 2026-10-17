"""Build NWW German industry without changing legacy focus IDs or political graph."""
from pathlib import Path
import json,re
from hoi4_script import read,one,values,parse,dump

ROOT=Path(__file__).resolve().parents[1]
def save(path,node):
    Path(path).write_text(dump(node)+'\n',encoding='utf-8',newline='\n')
def block(s):return parse(s)
def put(node,key,value):
    node[:]=[n for n in node if n[0]!=key];node.append((key,value,'='))
def write(path,s):
    p=ROOT/path;p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(s,encoding='utf-8-sig' if path.endswith('.yml') else 'utf-8',newline='\n')
BONUSES={}
def bonus(fid,**kwargs):
    BONUSES[fid]=kwargs
    return '\n'.join(f'add_to_variable = {{ GER_industry_{k} = {v} tooltip = GER_nww_industry_{k}_tt }}' for k,v in kwargs.items())
def factory(kind):return f'GER_nww_build_{kind} = yes'
def tech(category):return f'add_tech_bonus = {{ category = {category} uses = 1 bonus = 0.5 }}'

def main():
    doc=read(ROOT/'common/national_focus/GER_focuses.txt');tree=one(doc,'focus_tree')
    nodes={one(f,'id'):f for f in values(tree,'focus')}
    specs=[]
    def add(fid,ru,en,x,y,parents,icon,reward,description,cost=10):
        specs.append((fid,ru,en,x,y,parents,icon,reward,description,cost))
    add('GER_krupp_and_thyssen','Имперский промышленный совет','Imperial Industrial Council',51,0,[], 'industrialists',bonus('GER_krupp_and_thyssen',construction=0.05)+'\n'+tech('industry'),'Крупп, Тиссен, электротехнические концерны и земли согласуют программу инвестиций. Это начало развития единого промышленного комплекса, а не схема долгов ради завоеваний.')
    add('GER_1','Модернизировать Рурский бассейн','Modernize the Ruhr Basin',49,1,['GER_krupp_and_thyssen'],'coal_mining','42 = { if = { limit = { is_owned_and_controlled_by = ROOT } add_resource = { type = coal amount = 8 } } }','Новые шахтные стволы и обогатительные установки увеличат добычу рурского угля. Рост промышленности должен опираться на реальную энергетическую базу.')
    add('GER_nww_electrical_grid','Соединить региональные энергосистемы','Connect Regional Power Grids',49,2,['GER_1'],'electrification',bonus('GER_nww_electrical_grid',energy=0.10),'Объединим региональные электростанции и промышленные сети. Уголь и генерация останутся основой энергетики, а единая сеть уменьшит потери.')
    add('GER_nww_silesian_steel','Силезская металлургия','Silesian Steelworks',49,3,['GER_nww_electrical_grid'],'steel_mill','67 = { if = { limit = { is_owned_and_controlled_by = ROOT } add_resource = { type = steel amount = 8 } } }','Модернизация силезских домен даст сталь для станков, рельсов и вооружения. Награда предоставляется только при нашем владении и контроле над Силезией.')
    add('GER_3','Восточные промышленные заказы','Eastern Industrial Orders',49,4,['GER_nww_silesian_steel'],'military_industry',factory('military'),'Государственные заказы поддержат оборонные предприятия германских земель. Заводы строятся на собственных контролируемых национальных территориях.')
    add('GER_nww_arsenal_contracts','Долгосрочные контракты арсеналов','Long-Term Arsenal Contracts',49,5,['GER_3'],'arms_trade',bonus('GER_nww_arsenal_contracts',output=0.05),'Вместо чрезвычайных займов арсеналы получат предсказуемые многолетние заказы. Это повышает выпуск уже существующих военных заводов.')
    add('GER_4','Единые стандарты вооружения','Common Armament Standards',49,6,['GER_nww_arsenal_contracts'],'GFX_goal_generic_small_arms',tech('infantry_weapons')+'\n'+bonus('GER_4',efficiency=0.05),'Единые допуски и взаимозаменяемые детали ускорят освоение серийного оружия. Военные технологии опираются на развитие станочного производства.')
    add('GER_5','Рейнские инвестиционные банки','Rhineland Investment Banks',53,1,['GER_krupp_and_thyssen'],'industry_investment',factory('civilian'),'Привлечём долгосрочные вложения к рейнским и общегерманским предприятиям. Производственные мощности растут без МЕФО и завоевательной долговой экономики.')
    add('GER_6','Промышленные облигации земель','State Industrial Bonds',53,2,['GER_5'],'stockpile_currency',bonus('GER_6',construction=0.05),'Добровольные облигации земель направят сбережения в оборудование, коммуникации и новые корпуса. Неограниченных денежных или фабричных наград эта программа не даёт.')
    add('GER_7','Культура точного производства','Precision Manufacturing',53,3,['GER_6'],'industrial_experts',bonus('GER_7',maximum=0.05),'Обучение мастеров и контроль качества дадут устойчивый рост производственной эффективности. Программа развивает общий промышленный дух.')
    add('GER_nww_machine_tools','Станкостроительная кооперация','Machine Tool Cooperation',53,4,['GER_7'],'mass_production',tech('industry')+'\n'+bonus('GER_nww_machine_tools',efficiency=0.05),'Машиностроительные фирмы согласуют выпуск станков, оснастки и запасных частей. Это ускорит развёртывание новых производственных линий.')
    add('GER_nww_industrial_standards','Общегерманские технические нормы','National Technical Standards',53,5,['GER_nww_machine_tools'],'improve_the_administration_2',bonus('GER_nww_industrial_standards',maximum=0.05),'Унификация деталей и производственных норм позволит совместить разработки частных фирм с государственными заказами.')
    add('GER_nww_technical_colleges','Технические училища земель','State Technical Colleges',53,6,['GER_nww_industrial_standards'],'education',bonus('GER_nww_technical_colleges',research=0.05),'Инженерные школы подготовят специалистов для заводов и лабораторий. Их постоянный вклад выражается в общем промышленном духе.')
    add('GER_mitteleuropa_trade','Торговые палаты Миттельевропы','Mitteleuropa Chambers of Commerce',57,1,['GER_krupp_and_thyssen'],'GFX_goal_generic_trade',factory('civilian'),'Договоры поставок и торговые палаты расширят гражданское производство. Экономическое сотрудничество само по себе не подчиняет соседей.')
    add('GER_2','Концессии заморских предприятий','Overseas Enterprise Concessions',57,2,['GER_mitteleuropa_trade'],'resource_extraction','546 = { if = { limit = { is_owned_and_controlled_by = ROOT } add_resource = { type = rubber amount = 8 } } }\n541 = { if = { limit = { is_owned_and_controlled_by = ROOT } add_resource = { type = chromium amount = 6 } } }','Вложения в заморские предприятия увеличат добычу только в принадлежащих нам и контролируемых регионах. Коренное население сохраняет национальные территории; германские колониальные коры не добавляются.')
    add('GER_nww_freight_corridors','Грузовые коридоры империи','Imperial Freight Corridors',57,3,['GER_2'],'railroad','GER_nww_improve_infrastructure = yes','Улучшим инфраструктуру двух собственных германских промышленных регионов. Заводы должны получать уголь и комплектующие до начала новой гонки вооружений.')
    add('GER_nww_merchant_contracts','Контракты торгового флота','Merchant Shipping Contracts',57,4,['GER_nww_freight_corridors'],'merchant_fleet','add_equipment_to_stockpile = { type = convoy amount = 20 producer = GER }','Долгосрочные контракты дадут торговому флоту транспорты для устойчивых поставок между метрополией и заморскими владениями.')
    add('GER_nww_export_credit','Экспортное кредитование','Export Credit',57,5,['GER_nww_merchant_contracts'],'GFX_goal_generic_positive_trade_relations',factory('civilian'),'Государственные гарантии экспортных контрактов поддержат гражданские предприятия. Торговля станет подготовкой к переговорам, а не поводом для немедленной войны.')
    add('GER_nww_investment_guarantees','Гарантии долгосрочных вложений','Long-Term Investment Guarantees',57,6,['GER_nww_export_credit'],'currency_reforms',bonus('GER_nww_investment_guarantees',construction=0.05),'Прозрачные гарантии заказов завершают инвестиционную программу земель. Рост строительства не требует запуска ванильной экономики завоеваний.')
    add('GER_8','Согласовать промышленную программу','Coordinate the Industrial Program',51,7,['GER_4','GER_nww_technical_colleges'],'GFX_focus_research2','if = { limit = { amount_research_slots < 5 } add_research_slot = 1 }','Военная стандартизация и гражданские технические школы должны сойтись в общей исследовательской программе. Дополнительная ячейка предоставляется только до пяти исследовательских ячеек.')
    add('GER_9','Арсеналы нового поколения','Next-Generation Arsenals',49,8,['GER_8'],'tank_production',factory('military')+'\n'+bonus('GER_9',output=0.05),'Новые военные предприятия опираются на уже подготовленную производственную и инженерную базу. Это завершение подготовки, а не ранний скачок к массовой агрессии.')
    add('GER_10','Автоматизация оружейных линий','Automated Armament Lines',53,8,['GER_8'],'GFX_goal_generic_production2',tech('infantry_weapons'),'Внедрим автоматическую оснастку в оружейное производство. Бонус исследований не выдаёт технологии другой эпохи напрямую.')
    add('GER_nww_industrial_research','Имперское исследовательское объединение','Imperial Research Association',51,9,['GER_9','GER_10'],'university_3',bonus('GER_nww_industrial_research',research=0.05),'Университеты, арсеналы и частные лаборатории объединят прикладные программы. Результат сохраняется в общем промышленном духе.')
    add('GER_nww_balanced_orders','Сбалансированная система заказов','Balanced Procurement',49,10,['GER_nww_industrial_research'],'reorient_production',factory('civilian')+'\n'+factory('military'),'Гражданские и военные предприятия получают сбалансированную программу заказов. Имперская промышленность должна выдержать длительное напряжение без долговых миссий.')
    add('GER_nww_synthetic_fuels','Синтетическое топливо из угля','Coal-Based Synthetic Fuels',57,7,['GER_nww_investment_guarantees'],'GFX_goal_generic_oil_refinery','GER_nww_build_refinery = yes','Разовьём синтетическую переработку в собственном промышленном регионе. Топливная безопасность дополняет, но не заменяет энергетическую систему угля и сетей.')
    add('GER_nww_colonial_ports','Складские узлы заморских портов','Overseas Port Warehouses',57,8,['GER_nww_synthetic_fuels'],'GFX_goal_generic_construction',factory('civilian'),'Складские и перерабатывающие мощности поддержат заморские перевозки. Программа не передаёт чужие территории и не создаёт германские колониальные коры.')
    add('GER_nww_energy_keystones','Энергетическая инфраструктура Рура','Ruhr Energy Infrastructure',47,3,['GER_nww_electrical_grid'],'energy','GER_nww_build_energy_infrastructure = yes','Построим энергетическую инфраструктуру в собственном контролируемом регионе, где её ещё нет. Используется инфраструктурный объект установленной версии игры.')
    add('GER_nww_worker_housing','Жильё для промышленных рабочих','Industrial Workers Housing',55,2,['GER_5'],'low_cost_housing','add_stability = 0.05','Жилищные программы снизят напряжённость в растущих промышленных городах. Развитие производственной базы должно сопровождаться улучшением быта.')
    add('GER_nww_electromechanical_labs','Электромеханические лаборатории','Electromechanical Laboratories',55,5,['GER_nww_machine_tools'],'GFX_goal_generic_radar',tech('electronics'),'Электромеханика и связь дадут основу для следующего поколения промышленного оборудования. Гражданское применение технологий предшествует массовому перевооружению.')
    add('GER_nww_supply_resilience','Устойчивые цепочки поставок','Resilient Supply Chains',55,9,['GER_nww_colonial_ports'],'supply_line','add_equipment_to_stockpile = { type = train_equipment_1 amount = 20 producer = GER }','Резерв локомотивов и согласованные контракты укрепят снабжение. Программа создаёт реальный транспорт, не заменяя его абстрактной наградой людскими ресурсами.')
    add('GER_nww_prague_network','Связи с богемскими автономистами','Contacts with Bohemian Autonomists',45,3,['GER_guardians_of_the_reich'],'secret_agent_operative','add_political_power = 50\ncustom_effect_tooltip = GER_nww_bohemian_operation_unlock_tt','Разведка установит контакты с богемскими автономистами. При наличии La Résistance в агентстве откроется операция против Австрии: каждое завершение даёт +2 к напряжённости и учитывается как немецкий вклад.',cost=5)
    for fid,ru,en,x,y,parents,icon,reward,desc,cost in specs:
        node=nodes.get(fid)
        if node is None:
            node=block(f'id = {fid}');tree.append(('focus',node,'='));nodes[fid]=node
        for key,value in [('x',str(x)),('y',str(y)),('cost',str(cost)),('icon',icon if icon.startswith('GFX_') else 'GFX_focus_generic_'+icon)]:put(node,key,value)
        node[:]=[n for n in node if n[0] not in ('prerequisite','completion_reward','search_filters','ai_will_do','available_if_capitulated')]
        for parent in parents:node.append(('prerequisite',block('focus = '+parent),'='))
        node.extend(block('available_if_capitulated = no\nsearch_filters = { FOCUS_FILTER_INDUSTRY }'))
        node.append(('completion_reward',block(reward+'\nhidden_effect = { GER_nww_refresh_industry = yes }'),'='))
        node.append(('ai_will_do',block('factor = 1'),'='))
    put(tree,'continuous_focus_position',block('x = 100 y = 3000'))
    save(ROOT/'common/national_focus/GER_focuses.txt',doc)
    # Replay only persistent parameters; never one-off factories, resources or slots.
    variables={'construction':'production_speed_buildings_factor','output':'industrial_capacity_factory','efficiency':'production_factory_efficiency_gain_factor','maximum':'production_factory_max_efficiency_factor','research':'research_speed_factor','energy':'energy_gain_factor'}
    effects='GER_nww_refresh_industry = {\n'
    for k in variables:effects+=f' set_variable = {{ GER_industry_{k} = 0 }}\n'
    for fid,bonuses in BONUSES.items():
        effects+=f' if = {{ limit = {{ has_completed_focus = {fid} }}\n'
        effects+='\n'.join(f'  add_to_variable = {{ GER_industry_{k} = {v} }}' for k,v in bonuses.items())+'\n }\n'
    effects+=''' if = { limit = { has_completed_focus = GER_7 has_idea = NWW_GER_quality } remove_ideas = NWW_GER_quality }
 if = { limit = { has_completed_focus = GER_krupp_and_thyssen NOT = { has_dynamic_modifier = { modifier = GER_nww_industrial_program } } } add_dynamic_modifier = { modifier = GER_nww_industrial_program } }
}
'''
    for kind,building in [('civilian','industrial_complex'),('military','arms_factory'),('refinery','synthetic_refinery')]:
        effects+=f'''GER_nww_build_{kind} = {{
 random_owned_controlled_state = {{
  limit = {{ is_core_of = PREV }}
  add_extra_state_shared_building_slots = 1
  add_building_construction = {{ type = {building} level = 1 instant_build = yes }}
 }}
}}
'''
    effects+='''GER_nww_improve_infrastructure = {
 random_owned_controlled_state = { limit = { is_core_of = PREV infrastructure < 5 } add_building_construction = { type = infrastructure level = 1 instant_build = yes } }
 random_owned_controlled_state = { limit = { is_core_of = PREV infrastructure < 5 } add_building_construction = { type = infrastructure level = 1 instant_build = yes } }
}
GER_nww_build_energy_infrastructure = {
 random_owned_controlled_state = {
  limit = { is_core_of = PREV energy_infrastructure < 1 free_building_slots = { building = energy_infrastructure size > 0 include_locked = yes } }
  prioritize = { 42 }
  add_extra_state_shared_building_slots = 1
  add_building_construction = { type = energy_infrastructure level = 1 instant_build = yes }
 }
}
'''
    write('common/scripted_effects/GER_industry_effects.txt',effects)
    write('common/dynamic_modifiers/GER_industry_modifiers.txt','GER_nww_industrial_program = {\n enable = { always = yes }\n icon = GFX_idea_generic_industrial_concern_1\n'+''.join(f' {mod} = GER_industry_{key}\n' for key,mod in variables.items())+'}\n')
    write('common/on_actions/GER_industry_on_actions.txt','''on_actions = {
 on_startup = { effect = { every_country = { limit = { original_tag = GER has_focus_tree = GER_focus } GER_nww_refresh_industry = yes } } }
 on_daily_GER = { effect = { if = { limit = { has_focus_tree = GER_focus } GER_nww_refresh_industry = yes } } }
}
''')
    for lang in ['russian','english']:
        entries={}
        english_descriptions=[
            'Krupp, Thyssen, electrical firms and the states coordinate investment. Industrial research and construction improve through a lasting program financed without conquest debt.',
            'Modern shafts and processing plants expand Ruhr coal extraction. The resource investment requires ownership and control of the Ruhr.',
            'Link regional generating stations and industrial grids to improve energy supply. Coal extraction and efficient distribution must support new factories.',
            'Modernize Silesian furnaces to supply steel for machinery, railways and armaments. The steel is added only while we own and control the region.',
            'State orders support new military production on owned and controlled German core territory.',
            'Give arsenals predictable long-term contracts, improving the output of existing military factories.',
            'Common tolerances and interchangeable parts improve production efficiency growth and support infantry weapon research.',
            'Long-term investment supports a new civilian enterprise on owned and controlled German core territory.',
            'Voluntary state industrial bonds direct savings into equipment and construction, permanently improving the industrial program.',
            'Train master craftsmen and strengthen quality control to raise the production efficiency cap.',
            'Coordinate machine tools, fixtures and spare parts to speed the development of new production lines and industrial technology.',
            'Common technical standards integrate private designs with public orders, raising the production efficiency cap.',
            'Technical colleges train engineers and laboratory staff, providing a lasting research bonus.',
            'Supply contracts and chambers of commerce expand civilian production. Economic cooperation does not itself subjugate neighboring states.',
            'Develop overseas rubber and chromium enterprises only in regions we actually own and control. Indigenous claims remain intact.',
            'Improve infrastructure twice in eligible owned and controlled German core regions so industry can receive coal and components.',
            'Long-term shipping contracts supply twenty convoys for trade between the metropole and overseas possessions.',
            'Export guarantees support another civilian enterprise. Trade prepares the ground for diplomacy rather than an immediate war.',
            'Predictable procurement completes the states investment program and permanently improves construction speed.',
            'Bring military standardization and technical education together. An additional research slot is granted only below five slots.',
            'New military factories and improved output build on the completed industrial and engineering program.',
            'Automatic tooling supports infantry weapon research without directly granting technologies from a later era.',
            'Unite universities, arsenals and private laboratories in applied research, improving the lasting industrial program.',
            'Balance civilian and military orders by building one enterprise of each kind on owned and controlled German core territory.',
            'Build a synthetic refinery in an eligible domestic core region. Fuel security complements coal extraction and the electrical grid.',
            'Expand civilian storage and processing capacity for overseas shipping without transferring territory or creating colonial cores.',
            'Build an energy-infrastructure installation, prioritizing the Ruhr when eligible. The project requires an owned and controlled core region with room for the building.',
            'Housing programs reduce tensions in growing industrial towns and improve national stability.',
            'Electromechanical laboratories support electronics research and the development of industrial communications.',
            'Provide twenty locomotives to support resilient supply chains and reliable freight transport.',
            'Intelligence contacts with Bohemian autonomists unlock an agency operation against Austria with La Resistance. Each completion adds two tension and counts toward German influence.'
        ]
        assert len(english_descriptions)==len(specs)
        for index,(fid,ru,en,x,y,parents,icon,reward,desc,cost) in enumerate(specs):
            entries[fid]=ru if lang=='russian' else en
            entries[fid+'_desc']=desc if lang=='russian' else english_descriptions[index]
        path=ROOT/f'localisation/replace/GER_l_{lang}.yml'
        text=path.read_text(encoding='utf-8-sig')
        for key,value in entries.items():
            line=f' {key}:0 "{value}"'
            if re.search(r'^ '+key+r':',text,re.M):text=re.sub(r'^ '+key+r':[^\n]*',lambda m:line,text,flags=re.M)
            else:text+=line+'\n'
        write(str(path.relative_to(ROOT)),text)
    write('docs/GER_industry_rework.json',json.dumps({'focuses':[s[0] for s in specs],'persistent_bonuses':BONUSES,'modifiers':variables},indent=2)+'\n')
    manifest=json.loads((ROOT/'docs/legacy_import.json').read_text(encoding='utf-8-sig'))
    manifest['countries']['GER']['focus_ids']=[one(f,'id') for f in values(tree,'focus')]
    manifest['countries']['GER']['total']=len(values(tree,'focus'))
    write('docs/legacy_import.json',json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    print(f'Built {len(specs)} German industrial/intelligence focuses, preserving all original IDs')

if __name__=='__main__':
    main()
    from expand_german_services import main as expand_services
    from update_german_service_plans import main as update_service_plans
    expand_services()
    update_service_plans()
