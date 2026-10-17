"""Build France's NWW 1936 content. Source of truth: data below, not vanilla rewards.

Reference files and gameplay contracts are recorded in docs/FRA_overhaul.md.
Only country-owned FRA files and documented native overrides are emitted.
"""
from pathlib import Path
import json
import re
from hoi4_script import parse, read, one, values, walk, dump, TOKEN

ROOT = Path(__file__).resolve().parents[1]
GAME = Path('D:/Steam/steamapps/common/Hearts of Iron IV')
LOC = {}
FOCUSES = []
EFFECTS = []
DECISIONS = {'FRA_nww_mandate_category': [], 'FRA_nww_overseas_category': [], 'FRA_nww_projects_category': [], 'FRA_nww_diplomacy_category': []}
FOCUS_FLAVOUR = {
 'accounts':('Слухи о скрытых обязательствах государства разрушают кредит быстрее банкротств. Опубликуем счета ведомств и дадим Палате возможность спорить о настоящем бюджете.', 'Rumours of hidden state obligations destroy credit faster than bankruptcies. Publish departmental accounts so the Chamber can debate a real budget.'),
 'consultations':('Профсоюзы, предприниматели, муниципалитеты и командование должны назвать условия, на которых готовы поддержать правительство. Одного большинства на день голосования недостаточно.', 'Unions, employers, municipalities and the command must state the terms on which they will support a government. A majority lasting one vote is not enough.'),
 'republic':('Республике не требуется отрекаться от собственного имени. Ей требуется кабинет, способный выполнить обещания, и Палата, готовая отвечать за принятые решения.', 'The republic need not abandon its name. It needs a cabinet able to fulfil its promises and a Chamber prepared to answer for its decisions.'),
 'responsible':('Вотум недоверия должен открывать путь новому кабинету, а не оставлять страну без управления. Большинство, свергающее министров, обязуется представить замену.', 'A vote of no confidence must open the way to a new cabinet rather than leave the country ungoverned. A majority dismissing ministers must present a replacement.'),
 'oversight':('Сильное правительство нуждается в убедительных ограничениях. Постоянные комиссии и публичная отчётность позволят удерживать широкую коалицию без передачи ей неограниченной власти.', 'A strong government needs credible limits. Standing committees and public accounts will sustain a broad coalition without granting unlimited powers.'),
 'renewal':('Комиссии, арбитраж и государственная служба получили постоянные полномочия. Теперь правительство может предлагать стране программу, срок которой превышает жизнь одного кабинета.', 'Audit bodies, arbitration and the civil service have permanent powers. The government can now offer a programme that outlasts a single cabinet.'),
 'right':('Монархические общества и национальные лиги объединяет ненависть к бессилию Палаты. Их согласие пока скрывает главный вопрос: кому достанется власть после победы?', 'Royalist societies and national leagues share their hatred of an impotent Chamber. Their agreement still conceals the central question: who will rule after victory?'),
 'garrisons':('Командование не обязано разделять убеждения комитетов. Но без обещания сохранить порядок и армейскую иерархию гарнизоны не останутся в казармах во время политической развязки.', 'The command need not share the committees\' convictions. Yet without guarantees of order and military hierarchy, garrisons will not remain in barracks during the political reckoning.'),
 'crown_law':('Реставрация должна определить полномочия короны, правительства и представительных учреждений. Без основного закона трон останется заложником тех лиг, которые расчистили к нему дорогу.', 'The restoration must define the powers of crown, government and representative institutions. Without a fundamental law, the throne will remain hostage to the leagues that cleared its path.'),
 'league_state':('Лиги требуют собственной власти, а не места в свите претендента. Национальная директория заменит партийные переговоры единым центром решений и примет ответственность за сопротивление этому порядку.', 'The leagues demand power of their own rather than a place in a pretender\'s entourage. A national directory will replace party bargaining with a single centre of decision and face the resistance it creates.'),
 'front':('Левым необходимо договориться до выборов: о заработной плате, кредите, свободе организаций и судьбе колоний. Без общей программы кабинет станет продолжением межпартийного спора.', 'The left must agree before the election on wages, credit, organisational freedoms and the colonies. Without a common programme, its cabinet will merely continue the party dispute.'),
 'labour_charter':('Коллективные договоры требуют согласованных правил и переходного периода для предприятий. Рабочие должны увидеть гарантии, а заводы — знать, как оплачивать новую организацию труда.', 'Collective bargaining requires common rules and a transition period for businesses. Workers need guarantees and factories need to know how the new organisation of labour will be funded.'),
 'councils':('Трудовые советы предлагают связать политическое представительство с производственными коллективами. Их съезду предстоит установить пределы полномочий центра и самостоятельности предприятий.', 'Labour councils propose linking political representation to workplace communities. Their congress must define the limits of central authority and enterprise autonomy.'),
 'central_plan':('Правительство предлагает сосредоточить кредит и инвестиции в едином плане. Оно получает возможность направлять капитал, но принимает на себя риск ошибок, саботажа и бюрократической неподвижности.', 'The government proposes concentrating credit and investment in a unified plan. It gains the power to direct capital while assuming the risks of mistakes, sabotage and bureaucratic inertia.'),
 'military_cabinet':('Чрезвычайное правительство получает ограниченный срок, а не бессрочную собственность на государство. Армия обещает восстановить гражданское управление или представить законное основание для нового порядка.', 'The emergency government receives a limited term, not permanent ownership of the state. The army promises to restore civilian government or establish a lawful basis for a new order.'),
 'bank_audit':('Сбережения есть, но вкладчики не доверяют балансам, а банки не доверяют будущим доходам предприятий. Проверка задолженности должна вернуть различие между временной нехваткой кредита и настоящим банкротством.', 'Savings exist, but depositors distrust balance sheets and banks distrust future industrial earnings. An audit must distinguish temporary credit shortages from genuine insolvency.'),
 'internal_market':('Жильё, транспорт и устойчивый кредит связывают провинциальное производство с национальным спросом. Хозяйственное восстановление сможет продолжаться и без постоянного роста военных заказов.', 'Housing, transport and reliable credit link provincial production with national demand. Economic recovery can continue without an endless increase in military orders.'),
 'fort_commission':('Довоенная крепостная традиция даёт нам инженеров, но не готовый ответ на будущую войну. Комиссия определит ограниченные участки строительства, подъездные пути и место подвижного резерва.', 'The pre-war fortress tradition provides engineers, not a ready answer to the next war. The commission will define limited construction sites, access routes and the role of mobile reserves.'),
 'research_council':('Университетские школы сохранились, однако их лаборатории живут разными бюджетами. Общий совет свяжет фундаментальную работу, техническое образование и задачи промышленности.', 'University traditions survived, but laboratories live on separate budgets. A common council will connect fundamental research, technical education and industrial needs.'),
 'maneuvers':('Настоящей европейской войны нового масштаба у нашего штаба не было. Большие манёвры должны проверить теории на расстояниях, снабжении и времени, прежде чем их проверит противник.', 'Our staff has never fought a European war on the new scale. Grand manoeuvres must test its theories against distance, supply and time before an enemy does.'),
 'methodical':('Артиллерия, разведка и заранее согласованный манёвр способны лишить наступающего преимущества. Подготовленное сражение потребует крепостей, связи и резерва, способного перейти в контрудар.', 'Artillery, reconnaissance and coordinated manoeuvre can deny an attacker the initiative. A prepared battle requires fortifications, signals and reserves able to counterattack.'),
 'mobile':('Моторизация должна менять устройство командования, а не только способ перевозки пехоты. Опытные группы свяжут танки, связь, разведку и снабжение в самостоятельный оперативный инструмент.', 'Motorisation must change command structures, not merely transport infantry. Experimental groups will combine tanks, signals, reconnaissance and supply into an independent operational instrument.'),
 'air_command':('Армия и флот привыкли распределять самолёты по ведомственным потребностям. Самостоятельное командование позволит согласовать подготовку, закупки и оборону воздушного пространства страны.', 'Army and navy have distributed aircraft according to departmental needs. An independent command will coordinate training, procurement and national air defence.'),
 'fleet_audit':('Атлантические коммуникации и Средиземное море предъявляют разные требования к одному бюджету. Сначала установим, какие корабли стоит модернизировать и какие задачи важнее численности вымпелов.', 'Atlantic communications and the Mediterranean place different demands on one budget. Establish which ships merit reconstruction and which missions matter more than counting hulls.'),
 'overseas_conference':('Париж привык обсуждать колонии как статьи доходов и расходов. Конференция впервые поставит рядом вопрос о том, кто вправе принимать решения от имени их жителей.', 'Paris has treated its colonies as items of revenue and expenditure. The conference will also ask who has the right to speak for their inhabitants.'),
 'selfdetermination':('Отказ от прямого господства требует договориться о собственности, торговле и безопасности. Будущие независимые правительства смогут согласиться на сотрудничество или выбрать другой путь.', 'Ending direct rule requires agreements on property, trade and security. Future independent governments may accept cooperation or choose a different course.'),
 'central_overseas_plan':('Общий хозяйственный план обещает колониальным обществам школы, работу и инфраструктуру. Пока право окончательного решения остаётся в Париже, национальный вопрос этим не исчерпывается.', 'A common economic plan promises schools, work and infrastructure to colonial societies. As long as final authority remains in Paris, the national question remains unresolved.'),
 'continental_accord':('Сходство общественного устройства не отменяет соперничества держав. Соглашение с Берлином и Веной потребует переговоров, взаимного признания интересов и готовности услышать отказ.', 'Similar institutions do not end rivalry between powers. An agreement with Berlin and Vienna requires negotiation, reciprocal recognition of interests and a willingness to hear a refusal.'),
 'rhine_ultimatum':('Националисты готовы подкрепить требования силой. Германия получит возможность заключить договор; отказ откроет военную развязку, за которую Франции придётся отвечать собственной армией.', 'The nationalists are ready to back their demands with force. Germany may conclude a treaty; refusal opens a military confrontation France must fight with its own army.'),
}

def write(path, text, bom=False):
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text.rstrip() + '\n', encoding='utf-8-sig' if bom else 'utf-8', newline='\n')

def label(key, ru, en, desc=None, edesc=None):
    # HOI4's UI font does not contain U+2212: it renders as '?' in the panel.
    LOC[key] = (ru.replace('\u2212','-'), en.replace('\u2212','-'))
    if desc is not None:
        LOC[key + '_desc'] = (desc.replace('\u2212','-'), (edesc or desc).replace('\u2212','-'))

def done(fid):
    return f'OR = {{ has_completed_focus = {fid} has_country_flag = {fid}_done }}'

def var(name, op, value):
    comp = {'>=':'greater_than_or_equals', '<=':'less_than_or_equals', '>':'greater_than', '<':'less_than', '=':'equals'}[op]
    tt=f'FRA_check_{name}_{comp}_{value}_tt'
    ru,en={'mandate':('Мандат кабинета','Cabinet mandate'),'tension':('Уличная напряжённость','Street tension')}.get(name,('Колониальное давление','Colonial pressure'))
    wording={'greater_than_or_equals':('не менее','at least'),'less_than_or_equals':('не более','at most'),'greater_than':('больше','greater than'),'less_than':('меньше','less than'),'equals':('равно','equals')}[comp]
    label(tt,f'{ru}: {wording[0]} {value}.',f'{en}: {wording[1]} {value}.')
    return f'check_variable = {{ var = FRA_{name} value = {value} compare = {comp} tooltip = {tt} }}'

def delta(name, amount):
    direction='gain' if amount>0 else 'loss'
    tt=f'FRA_meter_{name}_{direction}_{abs(amount)}_tt'
    if name=='mandate':ru,en='Мандат кабинета','Cabinet mandate'
    elif name=='tension':ru,en='Уличная напряжённость','Street tension'
    else:
        region=name.removesuffix('_pressure')
        row=next(r for r in REGIONS if r[0]==region)
        ru,en='Давление: '+row[1],'Pressure: '+row[2]
    label(tt,f'{ru}: {amount:+g}.',f'{en}: {amount:+g}.')
    return f'custom_effect_tooltip = {tt} add_to_variable = {{ FRA_{name} = {amount} }}'

def build(kind='industrial_complex', count=1, priorities=()):
    coast = 'is_coastal = yes' if kind == 'dockyard' else ''
    preferred='prioritize = { '+' '.join(str(s) for s in priorities)+' }' if priorities else ''
    return f'''random_owned_controlled_state = {{ limit = {{ is_core_of = ROOT is_on_continent = europe {coast} }} {preferred}
      add_extra_state_shared_building_slots = {count}
      add_building_construction = {{ type = {kind} level = {count} instant_build = yes }} }}'''

def state_build(sid, kind, count=1):
    return f'''if = {{ limit = {{ {sid} = {{ is_owned_and_controlled_by = ROOT }} }}
      {sid} = {{ add_building_construction = {{ type = {kind} level = {count} instant_build = yes }} }} }}'''

def tech(cat, bonus='0.5'):
    return f'add_tech_bonus = {{ name = FRA_nww_research_program bonus = {bonus} uses = 1 category = {cat} }}'

def focus(key, ru, en, x, y, parent=None, reward='', gate='', cost=10, art='republic', desc=None, edesc=None, exclusive=()):
    fid = 'FRA_nww_' + key
    parents = [] if parent is None else ([parent] if isinstance(parent, str) else parent)
    parent_text = ''.join('prerequisite = { ' + ' '.join('focus = FRA_nww_' + p for p in (v if isinstance(v, tuple) else (v,))) + ' }\n' for v in parents)
    excl = 'mutually_exclusive = { ' + ' '.join('focus = FRA_nww_' + p for p in exclusive) + ' }' if exclusive else ''
    # Flag handles the completion callback before the focus is registered; save repair reads both.
    reward += f'\nset_country_flag = {fid}_done\nclr_country_flag = FRA_coalition_promise\nclr_country_flag = FRA_coalition_deadline\n{delta("mandate",1)}\nFRA_update_spirits = yes\nFRA_clamp_meters = yes'
    text = f'''focus = {{ id = {fid} icon = GFX_FRA_nww_{art}
      x = {x} y = {y} cost = {cost} {parent_text} {excl}
      available = {{ has_capitulated = no {gate} }}
      cancel_if_invalid = yes continue_if_invalid = no
      ai_will_do = {{ factor = 1 }}
      completion_reward = {{ {reward} }} }}'''
    FOCUSES.append({'id':fid, 'key':key, 'x':x, 'y':y, 'parents':parents, 'cost':cost, 'art':art, 'text':text})
    flavour=FOCUS_FLAVOUR.get(key,(None,None))
    label(fid, ru, en, desc or flavour[0] or f'{ru}: согласовать полномочия, кадры и финансирование программы. Её результат станет частью постоянных институтов Франции.', edesc or flavour[1] or f'{en}: agree responsibilities, trained staff and funding. The programme will become part of France\'s permanent institutions.')
    return fid

def pair(a, b):
    for f, other in ((a,b),(b,a)):
        item = next(v for v in FOCUSES if v['key']==f)
        item['text'] = item['text'].replace('available = {', f'mutually_exclusive = {{ focus = FRA_nww_{other} }}\navailable = {{', 1)

def chain(rows, x, start_y, parent, art, rewards=None):
    for i, (key, ru, en) in enumerate(rows):
        focus(key,ru,en,x,start_y+i,parent,(rewards or {}).get(key, 'add_political_power = 35'),art=art)
        parent=key
    return parent

def effect(name, body):
    EFFECTS.append(f'{name} = {{\n{body}\n}}')

def decision(cat,key,ru,en,body,desc,edesc):
    art={'FRA_nww_overseas_category':'overseas','FRA_nww_projects_category':'industry','FRA_nww_diplomacy_category':'republic','FRA_nww_mandate_category':'republic'}[cat]
    body=re.sub(r'icon\s*=\s*\w+',f'icon = GFX_FRA_nww_{art}_idea',body,count=1)
    if 'days_mission_timeout' in body:
        # Script-activated timers must neither auto-start nor auto-complete.
        body+='\nactivation = { always = no }\navailable = { always = no }\ncancel_if_not_visible = yes\nfire_only_once = no\n'
    DECISIONS[cat].append(f'{key} = {{\n{body}\n}}')
    label(key,ru,en,desc,edesc)

def build_focuses():
    focus('session','Открыть парламентскую сессию','Open the Parliamentary Session',0,0,
          reward='add_political_power = 75 country_event = { id = nww_fra.1 days = 1 }',cost=5,
          desc='Франция избежала мировой войны, но не кризиса представительства. Палата должна определить, кто оплатит восстановление хозяйства и подготовку обороны.',
          edesc='France avoided a world war, but not a crisis of representation. The Chamber must decide who will fund economic recovery and national defence.')
    focus('accounts','Опубликовать государственные счета','Publish the Public Accounts',0,1,'session',delta('mandate',10),cost=5)
    focus('consultations','Национальные консультации','National Consultations',0,2,'accounts','set_country_flag = FRA_consultations '+delta('tension',-5),cost=5)
    # Four parent routes, with distinct political mandates even when engine ideologies coincide.
    routes=[('republic','Республика способна управлять','The Republic Can Govern',-9,'democratic','republic'),
            ('right','Соглашение национальных комитетов','National Committees Agreement',-3,'neutrality','crown'),
            ('front','Пакт левых организаций','Pact of the Left',3,'democratic','labour'),
            ('emergency','Подготовить чрезвычайный мандат','Prepare an Emergency Mandate',10,'neutrality','cabinet')]
    for key,ru,en,x,ideology,art in routes:
        others=[r[0] for r in routes if r[0]!=key]
        focus(key,ru,en,x,3,'consultations',f'set_country_flag = FRA_route_{key} add_popularity = {{ ideology = {ideology} popularity = 0.05 }}',cost=5,art=art,exclusive=others)
    focus('commission','Парламентская следственная комиссия','Parliamentary Inquiry',-9,4,'republic',delta('mandate',10)+delta('tension',5),cost=5)
    focus('contracts','Открытые государственные контракты','Transparent Public Contracts',-9,5,'commission','add_stability = 0.05',cost=5)
    focus('responsible','Ответственный кабинет','A Responsible Cabinet',-11,6,'contracts',delta('mandate',15),exclusive=['oversight'])
    focus('oversight','Гарантии парламентского контроля','Guarantees of Parliamentary Oversight',-7,6,'contracts',delta('tension',-15),exclusive=['responsible'])
    focus('arbitration','Арбитраж трудовых конфликтов','Arbitration of Labour Disputes',-9,7,[('responsible','oversight')],delta('tension',-10))
    focus('municipal_credit','Муниципальный кредит','Municipal Credit',-9,8,'arbitration',build(),cost=5)
    focus('audit_court','Независимая счётная палата','Independent Court of Audit',-9,9,'municipal_credit',delta('mandate',10))
    focus('civil_service','Профессиональная государственная служба','Professional Civil Service',-9,10,'audit_court','add_political_power = 75',cost=5)
    focus('renewal','Мандат на обновление','Mandate for Renewal',-9,11,'civil_service','FRA_settle_regime = yes add_stability = 0.05',gate='NOT = { democratic < 0.40 } '+var('mandate','>=',40))
    chain([('rights','Гарантии гражданских прав','Guarantees of Civil Rights'),('republic_institutions','Республика действующих институтов','A Republic of Working Institutions')],-9,12,'renewal','republic',{'rights':delta('tension',-10),'republic_institutions':'add_political_power = 100'})
    focus('leagues_discipline','Дисциплина лиг','Discipline the Leagues',-3,4,'right',delta('tension',-5)+' set_country_flag = FRA_armed_leagues',cost=5,art='leagues')
    focus('garrisons','Нейтралитет гарнизонов','Neutrality of the Garrisons',-3,5,'leagues_discipline',delta('mandate',10),art='cabinet')
    focus('powers_crisis','Кризис полномочий','Crisis of Powers',-3,6,'garrisons',delta('mandate',10),art='leagues')
    focus('orleanists','Соглашение с орлеанистами','Agreement with the Orleanists',-5,7,'powers_crisis','add_popularity = { ideology = neutrality popularity = 0.05 }',cost=5,art='crown',exclusive=['directory'])
    focus('directory','Директория национального спасения','Directory of National Salvation',-1,7,'powers_crisis','add_popularity = { ideology = fascism popularity = 0.10 }',cost=5,art='leagues',exclusive=['orleanists'])
    focus('crown_law','Корона и основной закон','Crown and Fundamental Law',-5,8,'orleanists','FRA_monarchy_transition = yes',gate='NOT = { neutrality < 0.40 } '+var('mandate','>=',40),art='crown')
    focus('league_state','Государство национальных лиг','State of the National Leagues',-1,8,'directory','FRA_league_transition = yes',gate='NOT = { fascism < 0.40 } '+var('mandate','>=',40),art='leagues')
    chain([('royal_cabinet','Королевское правительство','Royal Government'),('royal_charter','Ограниченная королевская хартия','Limited Royal Charter'),('crown_service','Государственная служба короны','Crown Civil Service')],-5,9,'crown_law','crown',{'royal_cabinet':delta('mandate',10),'royal_charter':delta('tension',-15),'crown_service':'FRA_settle_regime = yes'})
    focus('royal_corporate','Корпоративное государство короны','Corporate State of the Crown',-3,10,'royal_cabinet',delta('mandate',10)+delta('tension',5),art='crown')
    pair('royal_charter','royal_corporate')
    crown_service=next(f for f in FOCUSES if f['key']=='crown_service')
    crown_service['text']=crown_service['text'].replace('focus = FRA_nww_royal_charter','focus = FRA_nww_royal_charter focus = FRA_nww_royal_corporate',1)
    crown_service['parents']=[('royal_charter','royal_corporate')]
    chain([('corporate_chamber','Корпоративная палата','Corporate Chamber'),('national_movement','Единое национальное движение','Unified National Movement'),('league_administration','Администрация национального государства','National State Administration')],-1,9,'league_state','leagues',{'corporate_chamber':delta('mandate',10),'national_movement':'add_war_support = 0.10 '+delta('tension',10),'league_administration':'FRA_settle_regime = yes'})
    focus('left_talks','Переговоры с профсоюзами','Talks with the Unions',3,4,'front',delta('tension',-10)+' set_country_flag = FRA_armed_workers',cost=5,art='labour')
    focus('public_works','Общественные работы','Public Works',3,5,'left_talks',build(),art='industry')
    focus('labour_charter','Хартия труда','Charter of Labour',3,6,'public_works','add_timed_idea = { idea = FRA_nww_retooling days = 120 } '+delta('mandate',10),art='labour')
    for key,ru,en,x,ideology in [('social_republic','Социальная республика','Social Republic',1,'democratic'),('councils','Республика трудовых советов','Republic of Labour Councils',3,'communism'),('central_plan','Централизованная социалистическая республика','Centralised Socialist Republic',5,'communism')]:
        focus(key,ru,en,x,7,'labour_charter',f'FRA_{key}_transition = yes',gate=f'NOT = {{ {ideology} < 0.40 }} '+var('mandate','>=',40),art='labour',exclusive=[k for k in ['social_republic','councils','central_plan'] if k!=key])
    chain([('collective_contracts','Коллективные договоры','Collective Bargaining'),('social_insurance','Социальное страхование','Social Insurance'),('social_arbitration','Постоянный социальный арбитраж','Permanent Social Arbitration')],1,8,'social_republic','labour',{'collective_contracts':delta('tension',-10),'social_insurance':'add_stability = 0.05','social_arbitration':'FRA_settle_regime = yes'})
    chain([('cooperatives','Производственные кооперативы','Production Cooperatives'),('elected_boards','Выборные производственные советы','Elected Production Boards'),('councils_congress','Съезд трудовых советов','Congress of Labour Councils')],3,8,'councils','labour',{'cooperatives':tech('industry'),'elected_boards':delta('tension',-10),'councils_congress':'FRA_settle_regime = yes'})
    chain([('national_banks','Национализация банков','Nationalise the Banks'),('investment_plan','Единый инвестиционный план','Unified Investment Plan'),('planning_commission','Постоянная плановая комиссия','Permanent Planning Commission')],5,8,'central_plan','labour',{'national_banks':'add_timed_idea = { idea = FRA_nww_capital_flight days = 180 }','investment_plan':tech('industry'),'planning_commission':'FRA_settle_regime = yes'})
    focus('disarm_militias','Разоружить партийные дружины','Disarm Party Militias',10,4,'emergency',delta('tension',5)+' set_country_flag = FRA_army_mandate',cost=5,art='cabinet')
    focus('emergency_legal','Правовая основа чрезвычайного кабинета','Legal Basis for an Emergency Cabinet',10,5,'disarm_militias',delta('mandate',10),art='cabinet')
    focus('military_cabinet','Кабинет национальной обороны','Cabinet of National Defence',10,6,'emergency_legal','FRA_military_transition = yes',gate='NOT = { neutrality < 0.40 } '+var('mandate','>=',40),art='cabinet')
    focus('army_neutrality','Гарантии армейского нейтралитета','Guarantees of Army Neutrality',10,7,'military_cabinet',delta('tension',-10),cost=5,art='cabinet')
    focus('civil_administration','Гражданская администрация','Civil Administration',10,8,'army_neutrality',delta('mandate',10),cost=5,art='republic')
    focus('defence_budget','Единый оборонный бюджет','Unified Defence Budget',10,9,'civil_administration',tech('industry'),art='industry')
    focus('return_ballot','Вернуться к урнам','Return to the Ballot Box',8,10,'defence_budget','FRA_return_democracy = yes',gate='NOT = { democratic < 0.40 }',art='republic',exclusive=['extend_mandate'])
    focus('extend_mandate','Продлить чрезвычайные полномочия','Extend Emergency Powers',12,10,'defence_budget','FRA_extend_military_rule = yes',gate='NOT = { neutrality < 0.40 } '+var('mandate','>=',50),art='cabinet',exclusive=['return_ballot'])
    # Civil industry: two exclusive financing methods, two territorial strategies.
    focus('bank_audit','Аудит банков','Audit the Banks',20,1,'session','add_political_power = 50',cost=5,art='industry')
    focus('public_bank','Государственный инвестиционный банк','Public Investment Bank',18,2,'bank_audit',delta('mandate',5),art='industry',exclusive=['private_credit'])
    focus('private_credit','Гарантии частному кредиту','Guarantees for Private Credit',22,2,'bank_audit',delta('mandate',5),art='industry',exclusive=['public_bank'])
    focus('housing','Жилищная программа','Housing Programme',20,3,[('public_bank','private_credit')],build(),art='industry')
    focus('municipal_orders','Заказы муниципалитетов','Municipal Orders',20,4,'housing',build(),art='industry')
    rail='if = { limit = { 16 = { is_owned_and_controlled_by = ROOT } 20 = { is_owned_and_controlled_by = ROOT } } build_railway = { level = 2 start_state = 16 target_state = 20 build_only_on_allied = yes controller_priority = { base = -1 modifier = { tag = FRA add = 2 } } } }'
    focus('rail_nodes','Железнодорожные узлы','Railway Junctions',20,5,'municipal_orders',state_build(16,'infrastructure')+state_build(20,'infrastructure')+rail,art='industry')
    focus('coal_basins','Угольные бассейны','Coal Basins',18,6,'rail_nodes','random_owned_controlled_state = { limit = { is_core_of = ROOT } prioritize = { 29 } add_resource = { type = coal amount = 8 } }',art='industry')
    focus('electrification','Электрификация промышленности','Industrial Electrification',22,6,'rail_nodes',state_build(16,'energy_infrastructure'),art='industry')
    focus('concentrate','Сосредоточить капитал','Concentrate Capital',18,7,'coal_basins',build(priorities=(16,29,785)),art='industry',exclusive=['regional'])
    focus('regional','Распределить развитие','Spread Regional Development',22,7,'electrification',build(priorities=(14,31,23)),art='industry',exclusive=['concentrate'])
    focus('west_industry','Индустрия западных департаментов','Industry of the Western Departments',20,8,[('concentrate','regional')],build(priorities=(14,31,15)),art='industry')
    focus('provincial_schools','Технические школы провинции','Provincial Technical Schools',20,9,'west_industry',tech('industry'),art='science')
    # Either upstream territorial strategy already requires coal or electrification.
    # Do not draw a redundant connector through the intervening industrial nodes.
    focus('internal_market','Внутренний рынок Франции','The French Domestic Market',20,10,'provincial_schools',build(),art='industry')
    # Military production and priced fortification projects.
    focus('specifications','Единые спецификации','Unified Specifications',28,1,'session',tech('infantry_weapons'),art='industry')
    chain([('standard_patterns','Сократить число образцов','Reduce the Number of Models'),('state_arsenals','Модернизировать государственные заводы','Modernise State Arsenals'),('private_contracts','Контракты частным предприятиям','Private Industrial Contracts'),('machine_reserve','Резерв станков','Machine Tool Reserve'),('conversion','Планы промышленной конверсии','Industrial Conversion Plans')],28,2,'specifications','industry',{'standard_patterns':tech('industry'),'state_arsenals':build('arms_factory',2),'private_contracts':build('arms_factory',2),'machine_reserve':tech('industry'),'conversion':'add_war_support = 0.05'})
    focus('fort_commission','Комиссия восточных крепостей','Eastern Fortifications Commission',32,2,'specifications','custom_effect_tooltip = FRA_fort_projects_tt',art='army')
    chain([('lorraine','Укреплённые районы Лотарингии','Fortified Districts of Lorraine'),('north_approaches','Северные подступы','The Northern Approaches'),('alpine_passes','Альпийские проходы','Alpine Passes')],32,3,'fort_commission','army',{'lorraine':'custom_effect_tooltip = FRA_fort_projects_tt','north_approaches':'custom_effect_tooltip = FRA_fort_projects_tt','alpine_passes':'custom_effect_tooltip = FRA_fort_projects_tt'})
    focus('arsenal_network','Сеть современных арсеналов','Network of Modern Arsenals',28,7,'conversion',build('arms_factory',2),art='industry')
    # Scientific network.
    focus('research_council','Национальный совет исследований','National Research Council',39,1,'session','add_political_power = 50',art='science')
    chain([('university_contract','Договор университетов и промышленности','University and Industry Compact'),('polytechnics','Региональные политехникумы','Regional Polytechnics'),('fourth_slot','Расширить исследовательские институты','Expand Research Institutes')],39,2,'research_council','science',{'university_contract':tech('industry'),'polytechnics':tech('electronics'),'fourth_slot':'if = { limit = { amount_research_slots < 4 } add_research_slot = 1 }'})
    focus('metallurgy','Металлургия и точное машиностроение','Metallurgy and Precision Engineering',37,5,'fourth_slot',tech('industry'),art='science')
    focus('radio_labs','Радиотехнические лаборатории','Radio Laboratories',41,5,'fourth_slot',tech('electronics'),art='science')
    focus('aerodynamics','Аэродинамические центры','Aerodynamic Centres',39,6,[('metallurgy','radio_labs')],tech('light_air'),art='science')
    focus('science_network','Общая научная сеть','Common Scientific Network',39,7,'aerodynamics','add_to_tech_sharing_group = FRA_nww_science_network',art='science')
    focus('fifth_slot','Постоянный научный бюджет','Permanent Science Budget',39,8,'science_network','if = { limit = { amount_research_slots < 5 } add_research_slot = 1 }',gate='date > 1938.12.31 num_of_factories > 74',art='science')
    # Army. School-specific improvements accumulate in one persistent modifier.
    focus('maneuvers','Большие манёвры','Grand Manoeuvres',47,1,'session','army_experience = 15 add_timed_idea = { idea = FRA_nww_manoeuvres days = 70 }',art='army')
    chain([('staff_college','Реформа штабного образования','Reform Staff Education'),('signals_supply','Стандартизация связи и снабжения','Standardise Signals and Supply')],47,2,'maneuvers','army',{'staff_college':'army_experience = 15','signals_supply':tech('support_tech')})
    focus('methodical','Методическое сражение','Methodical Battle',44,4,'signals_supply','army_experience = 20',art='army',exclusive=['mobile'])
    focus('mobile','Манёвренная армия','Army of Manoeuvre',50,4,'signals_supply','army_experience = 20',art='army',exclusive=['methodical'])
    chain([('artillery_plans','Артиллерийские планы','Artillery Plans'),('mobile_reserve','Подвижные резервы','Mobile Reserves'),('fort_counterattack','Контрудар из укреплённых районов','Counterattack from Fortified Districts'),('methodical_system','Система подготовленного сражения','Prepared Battle System')],44,5,'methodical','army',{'artillery_plans':tech('artillery'),'mobile_reserve':tech('motorized_equipment'),'fort_counterattack':'army_experience = 25','methodical_system':'army_experience = 25'})
    chain([('experimental_groups','Опытные механизированные группы','Experimental Mechanised Groups'),('radio_commands','Радиосвязь в каждом штабе','Radio in Every Headquarters'),('armoured_divisions','Самостоятельные бронетанковые соединения','Independent Armoured Formations'),('mobile_system','Система общевойскового манёвра','Combined Arms Manoeuvre System')],50,5,'mobile','army',{'experimental_groups':tech('armor'),'radio_commands':tech('electronics'),'armoured_divisions':tech('armor'),'mobile_system':'army_experience = 25'})
    focus('officer_corps','Профессиональный офицерский корпус','Professional Officer Corps',47,9,[('methodical_system','mobile_system')],'army_experience = 25',art='army')
    focus('mobilisation_staff','Штаб развёртывания резервов','Reserve Mobilisation Staff',47,10,'officer_corps','add_war_support = 0.05',art='army')
    # Independent aviation, both mission profiles retain ordinary aircraft access.
    focus('air_command','Самостоятельное авиационное командование','Independent Air Command',57,1,'session','air_experience = 15',art='air')
    chain([('flight_schools','Лётные школы','Flight Schools'),('engine_standards','Стандарты авиационных двигателей','Aircraft Engine Standards'),('airfields','Сеть аэродромов','Airfield Network')],57,2,'air_command','air',{'flight_schools':'air_experience = 15','engine_standards':tech('light_air'),'airfields':state_build(16,'air_base',2)+state_build(22,'air_base',2)})
    focus('tactical_air','Офицеры воздушного взаимодействия','Air Liaison Officers',55,5,'airfields',tech('medium_air'),art='air',exclusive=['strategic_air'])
    focus('strategic_air','Доктрина промышленного удара','Doctrine of Industrial Strikes',59,5,'airfields',tech('heavy_air'),art='air',exclusive=['tactical_air'])
    focus('tactical_groups','Тактические авиационные группы','Tactical Air Groups',55,6,'tactical_air','air_experience = 25',art='air')
    focus('navigation','Навигационные школы','Navigation Schools',59,6,'strategic_air','air_experience = 25',art='air')
    focus('air_watch','Служба воздушного наблюдения','Air Observation Service',57,7,[('tactical_groups','navigation')],tech('radar_tech'),art='air')
    focus('interception','Единая система перехвата','Unified Interception System',57,8,'air_watch',tech('light_air'),art='air')
    focus('air_industry','Современные авиационные бюро','Modern Aircraft Design Bureaux',57,9,'interception',build('arms_factory'),art='air')
    # Navy.
    focus('fleet_audit','Ревизия флота','Review the Fleet',67,1,'session','navy_experience = 15',art='navy')
    chain([('training_squadrons','Учебные эскадры','Training Squadrons'),('bases_fuel','Базы и нефтехранилища','Bases and Fuel Storage')],67,2,'fleet_audit','navy',{'training_squadrons':'navy_experience = 15','bases_fuel':state_build(851,'fuel_silo')})
    focus('atlantic','Океанские эскорты','Ocean Escorts',64,4,'bases_fuel',tech('dd_tech'),art='navy',exclusive=['mediterranean'])
    focus('mediterranean','Тулонская программа','Toulon Programme',70,4,'bases_fuel',tech('ca_tech'),art='navy',exclusive=['atlantic'])
    focus('asw','Противолодочные группы','Anti-Submarine Groups',64,5,'atlantic','navy_experience = 25',art='navy')
    focus('fast_squadrons','Быстроходные соединения','Fast Squadrons',70,5,'mediterranean','navy_experience = 25',art='navy')
    focus('naval_yards','Обновить военно-морские верфи','Renew Naval Dockyards',67,6,[('asw','fast_squadrons')],build('dockyard',2),art='navy')
    focus('battlefleet','Реконструкция линейных кораблей','Reconstruct the Battlefleet',65,7,'naval_yards',tech('bb_tech'),art='navy',exclusive=['carrier_trials'])
    focus('carrier_trials','Палубные испытания','Deck Aviation Trials',69,7,'naval_yards',tech('cv_tech'),art='navy',exclusive=['battlefleet'])
    focus('fire_control','Современное управление огнём','Modern Fire Control',65,8,'battlefleet',tech('naval_equipment'),art='navy')
    focus('carrier_group','Океанское авианосное соединение','Ocean Carrier Group',69,8,'carrier_trials',tech('naval_air'),art='navy')
    focus('two_seas','Два моря — один флот','Two Seas, One Fleet',67,9,[('fire_control','carrier_group')],build('dockyard'),art='navy')
    # Overseas and diplomatic frames; actual treaties are recipient-consent events.
    focus('overseas_register','Ревизия заморского управления','Review Overseas Administration',77,1,'session','add_political_power = 50',art='overseas')
    focus('overseas_conference','Заморская конференция','Overseas Conference',77,2,'overseas_register',delta('tension',-5),art='overseas')
    for key,ru,en,x in [('extraction','Порядок и концессии','Order and Concessions',73),('representation','Инвестиции и представительство','Investment and Representation',77),('selfdetermination','Самоопределение по соглашению','Negotiated Self-Determination',81)]:
        focus(key,ru,en,x,3,'overseas_conference',f'set_country_flag = FRA_policy_{key}',art='overseas',exclusive=[k for k in ['extraction','representation','selfdetermination'] if k!=key])
    focus('colonial_schools','Школы и местные администрации','Schools and Local Administration',77,4,[('extraction','representation','selfdetermination')],'custom_effect_tooltip = FRA_colonial_projects_tt',art='overseas')
    focus('overseas_credit','Банк заморского развития','Overseas Development Bank',77,5,'colonial_schools','add_political_power = 50',art='overseas')
    focus('central_overseas_plan','Единый план метрополии и колоний','Unified Metropolitan and Colonial Plan',81,5,'colonial_schools','set_country_flag = FRA_central_overseas_plan add_political_power = 50',gate='has_government = communism NOT = { has_country_flag = FRA_policy_selfdetermination }',art='labour')
    focus('overseas_compact','Заморский договор','The Overseas Compact',77,6,'overseas_credit','set_country_flag = FRA_overseas_compact',art='overseas')
    focus('common_markets','Общие рынки по договору','Treaty-Based Common Markets',77,7,'overseas_compact','custom_effect_tooltip = FRA_treaty_consent_tt',art='overseas')
    focus('foreign_review','Пересмотреть внешнюю политику','Review Foreign Policy',87,1,'session','add_political_power = 50',art='republic')
    focus('western_security','Западная система безопасности','Western Security System',85,2,'foreign_review','set_country_flag = FRA_western_diplomacy',art='republic',gate='OR = { has_government = democratic has_country_flag = FRA_regime_military }')
    focus('latin_accord','Латинское согласие','Latin Accord',87,3,'foreign_review','set_country_flag = FRA_latin_diplomacy',art='crown',gate='OR = { has_government = fascism has_country_flag = FRA_regime_monarchy }',exclusive=['continental_accord','rhine_stand'])
    focus('continental_accord','Континентальное соглашение','Continental Agreement',89,3,'foreign_review','set_country_flag = FRA_continental_diplomacy',art='crown',gate='OR = { has_government = fascism has_country_flag = FRA_regime_monarchy }',exclusive=['latin_accord','rhine_stand'])
    focus('rhine_stand','Никакого примирения на Рейне','No Accommodation on the Rhine',91,3,'foreign_review','add_war_support = 0.05 set_country_flag = FRA_rhine_diplomacy',art='army',gate='OR = { has_government = fascism has_country_flag = FRA_regime_monarchy }',exclusive=['latin_accord','continental_accord'])
    focus('workers_diplomacy','Дипломатия трудовых республик','Diplomacy of Labour Republics',93,2,'foreign_review','set_country_flag = FRA_workers_diplomacy',art='labour',gate='OR = { has_government = communism has_country_flag = FRA_route_front }')
    focus('independent_course','Самостоятельный европейский курс','Independent European Policy',95,3,['foreign_review'],'add_political_power = 75',art='republic')
    focus('rhine_preparations','Подготовить рейнскую кампанию','Prepare the Rhine Campaign',91,4,'rhine_stand','army_experience = 25',gate='date > 1938.12.31',art='army')
    focus('rhine_ultimatum','Рейнский ультиматум','The Rhine Ultimatum',91,5,'rhine_preparations','GER = { country_event = { id = nww_fra.204 days = 1 } }',gate='date > 1939.12.31 GER = { exists = yes } NOT = { has_war_with = GER }',art='army')
    unlocks={
      'extraction':('Заморские концессии: +10% к добыче ресурсов и +5 давления каждые 30 дней в управляемых колониях. Открывает усиление гарнизонов.', 'Overseas concessions: +10% resource gain and +5 pressure every 30 days in administered colonies. Unlocks garrison reinforcement.'),
      'representation':('На региональных конференциях становится доступно предложение представительства и местного бюджета.', 'Regional conferences can offer representation and a local budget.'),
      'selfdetermination':('На региональных конференциях становится доступно предложение независимости. Дальнейшие договоры требуют согласия получателя.', 'Regional conferences can offer independence. Subsequent treaties require recipient consent.'),
      'overseas_compact':('Открывает предложения автономного соглашения на региональных конференциях.', 'Unlocks autonomy offers at regional conferences.'),
      'western_security':('Открывает переговоры о договоре с демократическими Британией, Бельгией и LTB.', 'Unlocks treaty negotiations with democratic Britain, Belgium and LTB.'),
      'latin_accord':('Открывает переговоры с совместимыми правыми правительствами Италии и Испании.', 'Unlocks negotiations with compatible right-wing governments in Italy and Spain.'),
      'continental_accord':('Открывает переговоры с нейтральными правительствами Германии и Австрии.', 'Unlocks negotiations with non-aligned governments in Germany and Austria.'),
      'workers_diplomacy':('Открывает переговоры с совместимыми правительствами SOV, UKR и MKN. Каждое государство вправе отказаться.', 'Unlocks negotiations with compatible governments in SOV, UKR and MKN. Each recipient may refuse.'),
      'common_markets':('После принятия договора независимым заморским партнёром становится доступен постоянный бонус к торговым отношениям. Сам фокус не принуждает партнёра к соглашению.', 'A treaty accepted by an independent overseas partner enables a permanent trade-opinion bonus. The focus does not compel the partner to agree.'),
    }
    for key,(ru,en) in unlocks.items():
        tt='FRA_nww_'+key+'_unlock_tt';label(tt,ru,en)
        item=next(f for f in FOCUSES if f['key']==key)
        item['text']=item['text'].replace('completion_reward = {',f'completion_reward = {{ custom_effect_tooltip = {tt}',1)


SPIRITS = {
 'state': ('republic','Республика непрочных кабинетов','Republic of Fragile Cabinets', {'political_power_factor':-0.15,'stability_factor':-0.10}),
 'economy': ('industry','Экономика отложенных решений','Economy of Deferred Decisions',{'production_speed_buildings_factor':-0.10,'industrial_capacity_factory':-0.05,'energy_gain_factor':0,'production_factory_efficiency_gain_factor':0,'production_factory_max_efficiency_factor':0}),
 'army': ('army','Генеральный штаб без согласия','A Divided General Staff',{'land_doctrine_cost_factor':0.10,'planning_speed':-0.10,'army_org_factor':0,'army_speed_factor':0,'max_planning':0}),
 'air': ('air','Авиация ведомственных границ','Aviation Divided by Ministries',{'air_mission_efficiency':-0.10,'air_doctrine_cost_factor':0,'air_intercept_efficiency':0,'air_cas_efficiency':0,'air_strategic_bomber_bombing_factor':0}),
 'navy': ('navy','Флот двух морей','Fleet of Two Seas',{'industrial_capacity_dockyard':-0.10,'naval_doctrine_cost_factor':0,'convoy_escort_efficiency':0,'naval_speed_factor':0}),
 'science': ('science','Сохранившиеся научные школы','Preserved Scientific Schools',{'research_speed_factor':0.05}),
}

def build_spirits():
    defs=[]; update=[]
    for key,(art,ru,en,mods) in SPIRITS.items():
        defs.append(f'FRA_nww_{key} = {{ enable = {{ always = yes }} icon = GFX_FRA_nww_{art}_idea '+ ' '.join(f'{m} = FRA_{key}_{m}' for m in mods)+' }')
        update.extend(f'set_variable = {{ FRA_{key}_{m} = {value} }}' for m,value in mods.items())
        update.append(f'if = {{ limit = {{ NOT = {{ has_dynamic_modifier = {{ modifier = FRA_nww_{key} }} }} }} add_dynamic_modifier = {{ modifier = FRA_nww_{key} }} }}')
        label('FRA_nww_'+key,ru,en, 'Постоянная система: завершённые реформы последовательно меняют её параметры. Программы взаимоисключающих школ развивают этот же дух.', 'A permanent system: completed reforms change its parameters. Mutually exclusive programmes develop this same spirit.')
    changes={
      'contracts': [('state','political_power_factor',-0.10)],
      'arbitration': [('state','stability_factor',-0.05)],
      'civil_service':[('state','political_power_factor',-0.05)],
      'housing':[('economy','production_speed_buildings_factor',-0.05)],
      'municipal_orders':[('economy','industrial_capacity_factory',0)],
      'rail_nodes':[('economy','production_speed_buildings_factor',0)],
      'internal_market':[('economy','production_speed_buildings_factor',0.10),('economy','industrial_capacity_factory',0.05)],
      'electrification':[('economy','energy_gain_factor',0.10)],
      'standard_patterns':[('economy','industrial_capacity_factory',0.05)],
      'arsenal_network':[('economy','industrial_capacity_factory',0.10)],
      'staff_college':[('army','land_doctrine_cost_factor',0.05)],
      'signals_supply':[('army','planning_speed',0),('army','land_doctrine_cost_factor',0)],
      'methodical':[('army','max_planning',0.10)],
      'artillery_plans':[('army','planning_speed',0.10)],
      'methodical_system':[('army','army_org_factor',0.05)],
      'experimental_groups':[('army','army_speed_factor',0.05)],
      'radio_commands':[('army','planning_speed',0.10)],
      'mobile_system':[('army','army_org_factor',0.05),('army','army_speed_factor',0.10)],
      'officer_corps':[('army','land_doctrine_cost_factor',-0.10)],
      'air_command':[('air','air_mission_efficiency',-0.05)],
      'flight_schools':[('air','air_mission_efficiency',0)],
      'engine_standards':[('air','air_doctrine_cost_factor',-0.10)],
      'tactical_groups':[('air','air_cas_efficiency',0.10)],
      'navigation':[('air','air_strategic_bomber_bombing_factor',0.10)],
      'interception':[('air','air_intercept_efficiency',0.10)],
      'air_industry':[('air','air_mission_efficiency',0.10)],
      'training_squadrons':[('navy','naval_doctrine_cost_factor',-0.10)],
      'bases_fuel':[('navy','industrial_capacity_dockyard',-0.05)],
      'asw':[('navy','convoy_escort_efficiency',0.10)],
      'fast_squadrons':[('navy','naval_speed_factor',0.05)],
      'naval_yards':[('navy','industrial_capacity_dockyard',0)],
      'two_seas':[('navy','industrial_capacity_dockyard',0.10)],
      'fifth_slot':[('science','research_speed_factor',0.10)],
      'elected_boards':[('economy','production_factory_efficiency_gain_factor',0.10)],
      'investment_plan':[('economy','production_factory_max_efficiency_factor',0.10)],
      'central_overseas_plan':[('economy','production_factory_efficiency_gain_factor',0.10)],
    }
    modifier_labels={
      'political_power_factor':('Прирост политической власти','Political power gain'),
      'stability_factor':('Стабильность','Stability'),
      'production_speed_buildings_factor':('Скорость строительства','Construction speed'),
      'industrial_capacity_factory':('Выпуск военных заводов','Military factory output'),
      'energy_gain_factor':('Выработка энергии','Energy gain'),
      'land_doctrine_cost_factor':('Стоимость сухопутной доктрины','Land doctrine cost'),
      'planning_speed':('Скорость планирования','Planning speed'),
      'max_planning':('Максимальное планирование','Maximum planning'),
      'army_org_factor':('Организация армии','Army organisation'),
      'army_speed_factor':('Скорость армии','Army speed'),
      'air_mission_efficiency':('Эффективность воздушных заданий','Air mission efficiency'),
      'air_doctrine_cost_factor':('Стоимость воздушной доктрины','Air doctrine cost'),
      'air_cas_efficiency':('Эффективность непосредственной поддержки','Close air support efficiency'),
      'air_strategic_bomber_bombing_factor':('Стратегические бомбардировки','Strategic bombing'),
      'air_intercept_efficiency':('Эффективность перехвата','Interception efficiency'),
      'naval_doctrine_cost_factor':('Стоимость морской доктрины','Naval doctrine cost'),
      'industrial_capacity_dockyard':('Выпуск верфей','Dockyard output'),
      'convoy_escort_efficiency':('Эффективность сопровождения конвоев','Convoy escort efficiency'),
      'naval_speed_factor':('Скорость флота','Naval speed'),
      'research_speed_factor':('Скорость исследований','Research speed'),
      'production_factory_efficiency_gain_factor':('Рост эффективности производства','Production efficiency growth'),
      'production_factory_max_efficiency_factor':('Предел эффективности производства','Production efficiency cap'),
    }
    for fid,mods in changes.items():
        update.append('if = { limit = { '+done('FRA_nww_'+fid)+' } '+' '.join(f'set_variable = {{ FRA_{key}_{m} = {v} }}' for key,m,v in mods)+' }')
        tt='FRA_nww_'+fid+'_progress_tt'
        label(tt,'После реформы соответствующий национальный дух даёт:\n'+'\n'.join(f'{modifier_labels[m][0]}: {v*100:+.0f}%' for key,m,v in mods),
              'After this reform the corresponding national spirit provides:\n'+'\n'.join(f'{modifier_labels[m][1]}: {v*100:+.0f}%' for key,m,v in mods))
        item=next(f for f in FOCUSES if f['key']==fid)
        item['text']=item['text'].replace('completion_reward = {',f'completion_reward = {{ custom_effect_tooltip = {tt}',1)
    update.append('if = { limit = { has_country_flag = FRA_regime_settled } set_variable = { FRA_state_political_power_factor = 0.05 } set_variable = { FRA_state_stability_factor = 0.05 } }')
    for f,m,v in [('responsible','political_power_factor',0.10),('oversight','stability_factor',0.10),('royal_charter','stability_factor',0.10),('royal_corporate','political_power_factor',0.10),('social_insurance','stability_factor',0.10)]:
        update.append(f'if = {{ limit = {{ has_country_flag = FRA_regime_settled {done("FRA_nww_"+f)} }} set_variable = {{ FRA_state_{m} = {v} }} }}')
    effect('FRA_update_spirits','\n'.join(update))
    write('common/dynamic_modifiers/FRA_modifiers.txt','\n'.join(defs))
    ideas=[]
    for key,ru,en,art,mods in [
      ('retooling','Перестройка трудовых отношений','Restructuring Labour Relations','labour','industrial_capacity_factory = -0.05'),
      ('capital_flight','Отток капитала','Capital Flight','industry','production_speed_buildings_factor = -0.10 research_speed_factor = -0.05'),
      ('manoeuvres','Расходы больших манёвров','Grand Manoeuvres Expenditure','army','army_fuel_consumption_factor = 0.10'),
      ('overseas_network','Заморская административная сеть','Overseas Administrative Network','overseas','local_resources_factor = 0.05'),
      ('coercion','Государство чрезвычайных мер','State of Emergency Measures','cabinet','political_power_factor = 0.10 stability_factor = -0.05'),
      ('colonial_extraction','Заморские концессии','Overseas Concessions','overseas','local_resources_factor = 0.10 resistance_growth = 0.10'),
      ('project_commitment','Финансирование государственной программы','Public Programme Funding','industry','civilian_factory_use = 3'),
      ('trade_compact','Заморский торговый договор','Overseas Trade Compact','overseas','trade_opinion_factor = 0.10'),
    ]:
        ideas.append(f'FRA_nww_{key} = {{ picture = FRA_nww_{art} allowed = {{ original_tag = FRA }} allowed_civil_war = {{ always = no }} removal_cost = -1 modifier = {{ {mods} }} }}')
        label('FRA_nww_'+key,ru,en,'Последствия текущей государственной политики. Сроки временных мер и условия программ указаны в решениях.','The effects of current state policy. Decisions explain the duration of temporary measures and the conditions of public programmes.')
    for key in ['state','economy','army']:
        art,ru,en,mods=SPIRITS[key]
        preview='FRA_nww_preview_'+key
        ideas.append(f'{preview} = {{ picture = FRA_nww_{art} allowed = {{ always = no }} removal_cost = -1 modifier = {{ '+ ' '.join(f'{m} = {v}' for m,v in mods.items())+' } }')
        label(preview,ru,en,'Стартовое состояние Франции. Реформы последовательно меняют параметры постоянного духа.','France\'s starting condition. Reforms progressively change the parameters of the permanent spirit.')
    write('common/ideas/FRA_ideas.txt','ideas = { country = {\n'+'\n'.join(ideas)+'\n} }')

def build_political_effects():
    effect('FRA_restore_tree','if = { limit = { OR = { has_focus_tree = free_french_focus has_focus_tree = vichy_french_focus } } load_focus_tree = { tree = french_focus keep_completed = yes } }')
    effect('FRA_clamp_meters','\n'.join(f'clamp_variable = {{ var = FRA_{v} min = 0 max = 100 }}' for v in ['mandate','tension',*[r[0]+'_pressure' for r in REGIONS]]))
    effect('FRA_settle_regime','set_country_flag = FRA_regime_settled '+delta('mandate',15)+delta('tension',-10)+' FRA_update_spirits = yes')
    effect('FRA_political_advisor_reaction',delta('tension',5)+' FRA_clamp_meters = yes')
    transitions=[
      ('monarchy','neutrality','moderatism','FRA_nww_jean_iii','GFX_portrait_fra_jean_duke_of_guise','no'),
      ('league','fascism','fascism_ideology','FRA_nww_national_directory','GFX_portrait_fra_pierre_laval','no'),
      ('social_republic','democratic','socialism','FRA_nww_social_cabinet','GFX_portrait_fra_leon_blum','yes'),
      ('councils','communism','anarchist_communism','FRA_nww_labour_congress','GFX_portrait_fra_leon_blum','no'),
      ('central_plan','communism','marxism','FRA_nww_planning_cabinet','GFX_portrait_fra_maurice_thorez','no'),
      ('military','neutrality','despotism','FRA_nww_military_directory','GFX_portrait_FRA_maurice_gamelin','no'),
    ]
    for key,ideology,sub,name,portrait,elections in transitions:
        # Composite councils use a representative portrait, not a fictitious personal biography.
        extra = ''
        if key in ('league','central_plan'): extra='add_timed_idea = { idea = FRA_nww_capital_flight days = 180 } '+delta('tension',10)
        if key=='military': extra='activate_mission = FRA_nww_emergency_mandate'
        body=f'''set_country_flag = FRA_regime_{key}
          create_country_leader = {{ name = {name} desc = FRA_nww_regime_description picture = {portrait} ideology = {sub} expire = "1965.1.1" }}
          set_politics = {{ ruling_party = {ideology} elections_allowed = {elections} election_frequency = 48 last_election = "1936.5.1" }}
          set_party_name = {{ ideology = {ideology} name = FRA_nww_party_{key} long_name = FRA_nww_party_{key}_long }}
          {delta('mandate',10)} {extra}'''
        effect('FRA_'+key+'_transition',body)
    for key,ru,en in [
      ('monarchy','Королевский союз','Royal Union'),('league','Национальные лиги','National Leagues'),
      ('social_republic','Народный фронт','Popular Front'),('councils','Конгресс трудовых советов','Congress of Labour Councils'),
      ('central_plan','Социалистический государственный союз','Socialist State Union'),('military','Кабинет национальной обороны','Cabinet of National Defence'),
    ]:
        label('FRA_nww_party_'+key,ru,en);label('FRA_nww_party_'+key+'_long',ru,en)
    effect('FRA_return_democracy','set_country_flag = FRA_emergency_resolved set_politics = { ruling_party = democratic elections_allowed = yes election_frequency = 48 last_election = "1936.5.1" } FRA_settle_regime = yes')
    effect('FRA_extend_military_rule','set_country_flag = FRA_emergency_resolved add_ideas = FRA_nww_coercion '+delta('tension',15)+' FRA_settle_regime = yes')
    label('FRA_nww_jean_iii','Жан III','Jean III')
    label('FRA_nww_national_directory','Национальная директория','National Directory')
    label('FRA_nww_social_cabinet','Социальный кабинет','Social Cabinet')
    label('FRA_nww_labour_congress','Конгресс трудовых советов','Congress of Labour Councils')
    label('FRA_nww_planning_cabinet','Центральный плановый кабинет','Central Planning Cabinet')
    label('FRA_nww_military_directory','Военный кабинет','Military Cabinet')
    label('FRA_nww_regime_description','Государственные институты Франции перестроены после кризиса представительства. Их прочность зависит от выполненных обязательств.','French institutions were rebuilt after the crisis of representation. Their strength rests on honouring their commitments.')
    cleanup='\n'.join('remove_ideas = '+v for v in ['FRA_disjointed_government','FRA_protected_by_the_maginot_line','FRA_full_employment','FRA_worker_shortage','FRA_political_violence','FRA_inefficient_economy_1','FRA_inefficient_economy_2','FRA_matignon_agreements'])
    effect('FRA_suspend_native_systems',cleanup)
    repair=''
    for route,key in [('republic','republic'),('right','right'),('front','front'),('emergency','emergency')]:
        repair+=f'if = {{ limit = {{ has_completed_focus = FRA_nww_{key} }} set_country_flag = FRA_route_{route} }}\n'
    for regime,key in [('monarchy','crown_law'),('league','league_state'),('social_republic','social_republic'),('councils','councils'),('central_plan','central_plan'),('military','military_cabinet')]:
        repair+=f'if = {{ limit = {{ has_completed_focus = FRA_nww_{key} }} set_country_flag = FRA_regime_{regime} }}\n'
    settled=' '.join('has_completed_focus = FRA_nww_'+f for f in ['renewal','crown_service','league_administration','social_arbitration','councils_congress','planning_commission','return_ballot','extend_mandate'])
    repair+=f'if = {{ limit = {{ OR = {{ {settled} }} }} set_country_flag = FRA_regime_settled }}'
    repair+=' if = { limit = { OR = { has_completed_focus = FRA_nww_return_ballot has_completed_focus = FRA_nww_extend_mandate } } set_country_flag = FRA_emergency_resolved }'
    repair+=' if = { limit = { has_completed_focus = FRA_nww_science_network } every_other_country = { limit = { has_country_flag = FRA_security_partner NOT = { has_country_flag = FRA_science_joined } NOT = { has_war_with = FRA } } add_to_tech_sharing_group = FRA_nww_science_network set_country_flag = FRA_science_joined } }'
    effect('FRA_repair_reform_stages',repair)
    # Migration is deliberately restricted to the distinctive early-game corruption:
    # all six pressures at 100, mandate at zero, before normal crises are possible.
    # Never replay factories, politics, PP, decisions, or arbitrary late-save counters.
    bad=' '.join(var(r[0]+'_pressure','>=',100) for r in REGIONS)
    migration=f'''if = {{ limit = {{ NOT = {{ has_country_flag = FRA_runtime_v2 }} }}
      if = {{ limit = {{ date < 1936.4.1 {var('mandate','=',0)} {bad}
        NOT = {{ has_country_flag = FRA_regime_settled }}
        NOT = {{ has_country_flag = FRA_negotiation_busy }} NOT = {{ has_country_flag = FRA_coalition_promise }}
        NOT = {{ has_country_flag = FRA_project_busy }} }}
        set_variable = {{ FRA_mandate = 35 }}
        {' '.join('set_variable = { FRA_'+r[0]+'_pressure = 35 }' for r in REGIONS)}
        if = {{ limit = {{ date > 1936.2.29 }} add_to_variable = {{ FRA_mandate = -4 }}
          {' '.join('add_to_variable = { FRA_'+r[0]+'_pressure = 4 }' for r in REGIONS)} }}
        else_if = {{ limit = {{ date > 1936.1.30 }} add_to_variable = {{ FRA_mandate = -2 }}
          {' '.join('add_to_variable = { FRA_'+r[0]+'_pressure = 2 }' for r in REGIONS)} }}
    '''
    for f in FOCUSES:
        reward=one(parse(f['text'])[0][1],'completion_reward')
        gain=sum(float(one(v,'FRA_mandate',0)) for k,v,o in walk(reward) if k=='add_to_variable')
        if gain:migration+=f'if = {{ limit = {{ has_completed_focus = {f["id"]} }} add_to_variable = {{ FRA_mandate = {gain:g} }} }}\n'
    migration+='set_country_flag = FRA_early_meters_repaired }\n'
    for mid in ['confidence_vote','emergency_mandate',*[r[0]+'_ultimatum' for r in REGIONS]]:
        migration+='remove_mission = FRA_nww_'+mid+'\n'
    migration+='clr_country_flag = FRA_confidence_active\n'
    migration+=' '.join('clr_country_flag = FRA_'+r[0]+'_crisis' for r in REGIONS)
    migration+=' set_country_flag = { flag = FRA_tick_cooldown value = 1 days = 30 } set_country_flag = FRA_runtime_v2\n'
    migration+=' if = { limit = { has_country_flag = FRA_regime_military NOT = { has_country_flag = FRA_emergency_resolved } } activate_mission = FRA_nww_emergency_mandate } }'
    effect('FRA_repair_runtime_v2',migration)
    effect('FRA_initialize',f'''if = {{ limit = {{ NOT = {{ has_country_flag = FRA_nww_initialized }} }}
      set_country_flag = FRA_nww_initialized
      set_variable = {{ FRA_mandate = 35 }} set_variable = {{ FRA_tension = 40 }}
      {' '.join(f'set_variable = {{ FRA_{r[0]}_pressure = 35 }}' for r in REGIONS)}
      add_ideas = FRA_nww_overseas_network
      set_country_flag = {{ flag = FRA_tick_cooldown value = 1 days = 30 }}
      if = {{ limit = {{ is_ai = yes }} FRA_select_ai_route = yes }}
      }} FRA_repair_runtime_v2 = yes FRA_repair_reform_stages = yes FRA_suspend_native_systems = yes FRA_update_spirits = yes FRA_clamp_meters = yes''')
    # A missing initialization flag never replays a completed focus reward or changes borders.
    effect('FRA_daily', '''FRA_initialize = yes
      if = { limit = { has_country_flag = FRA_coalition_promise NOT = { has_country_flag = FRA_coalition_deadline } }
        '''+delta('mandate',-5)+delta('tension',5)+''' clr_country_flag = FRA_coalition_promise }
      if = { limit = { NOT = { has_country_flag = FRA_tick_cooldown } }
        set_country_flag = { flag = FRA_tick_cooldown value = 1 days = 30 } FRA_monthly_tick = yes }
      if = { limit = { has_completed_focus = FRA_nww_session NOT = { has_country_flag = FRA_confidence_cooldown } NOT = { has_country_flag = FRA_confidence_active } '''+var('mandate','<',25)+''' }
        set_country_flag = FRA_confidence_active activate_mission = FRA_nww_confidence_vote }
      FRA_update_spirits = yes FRA_clamp_meters = yes''')
    monthly='''if = { limit = { NOT = { has_country_flag = FRA_regime_settled } } '''+delta('mandate',-2)+''' }
      if = { limit = { has_country_flag = FRA_regime_settled } '''+delta('tension',-2)+''' }
      if = { limit = { is_ai = yes NOT = { has_country_flag = FRA_regime_settled } } FRA_ai_campaign = yes }
      if = { limit = { has_completed_focus = FRA_nww_common_markets any_other_country = { has_country_flag = FRA_compact_partner has_country_flag = FRA_security_partner exists = yes NOT = { has_war_with = FRA } } } add_ideas = FRA_nww_trade_compact }
    '''
    monthly+=' if = { limit = { OR = { '+' '.join('FRA_holds_'+r[0]+' = yes' for r in REGIONS)+' } } add_ideas = FRA_nww_overseas_network if = { limit = { has_country_flag = FRA_policy_extraction } add_ideas = FRA_nww_colonial_extraction } } else = { remove_ideas = FRA_nww_overseas_network remove_ideas = FRA_nww_colonial_extraction }'
    for region,ru,en,tags in REGIONS:
        label('FRA_'+region+'_treaty','Ратифицирован договор: '+ru,'Treaty ratified: '+en)
        monthly+=f'''if = {{ limit = {{ FRA_holds_{region} = yes }}
          if = {{ limit = {{ has_country_flag = FRA_{region}_represented }} {delta(region+'_pressure',-1)} }}
          else_if = {{ limit = {{ has_country_flag = FRA_policy_extraction }} {delta(region+'_pressure',5)} }}
          else_if = {{ limit = {{ has_country_flag = FRA_{region}_investment }} {delta(region+'_pressure',-3)} }}
          else = {{ {delta(region+'_pressure',2)} }}
          if = {{ limit = {{ {var(region+'_pressure','>=',80)} NOT = {{ has_country_flag = FRA_{region}_crisis }} NOT = {{ has_country_flag = FRA_{region}_cooldown }} }}
            set_country_flag = FRA_{region}_crisis activate_mission = FRA_nww_{region}_ultimatum }} }}'''
    effect('FRA_monthly_tick',monthly+' FRA_clamp_meters = yes')

REGIONS = [
 ('algeria','Алжир','Algeria',['ALG']),
 ('maghreb','Магрибские протектораты','Maghreb Protectorates',['MOR','TUN']),
 ('west_africa','Западная Африка','West Africa',['SEN','MLI','IVO','GNA','DAH','NGR','VOL','MRT']),
 ('equatorial','Экваториальная Африка','Equatorial Africa',['GAB','RCG','CHA','CAR']),
 ('indochina','Индокитай','Indochina',['VIN','CAM','LAO']),
 ('islands','Островные владения','Island Possessions',['MAD','TAH']),
]

def build_mandate_decisions():
    cat='FRA_nww_mandate_category'
    base='allowed = { original_tag = FRA } icon = generic_political_discourse available = { has_capitulated = no NOT = { has_country_flag = FRA_negotiation_busy } }'
    for key,ru,en,price,days,body in [
      ('coalition','Коалиционное соглашение','Coalition Agreement',50,35,delta('mandate',15)+' set_country_flag = FRA_coalition_promise set_country_flag = { flag = FRA_coalition_deadline value = 1 days = 30 }'),
      ('social_arbitration','Социальный арбитраж','Social Arbitration',50,35,delta('tension',-15)),
      ('inquiry','Опубликовать результаты расследования','Publish Inquiry Findings',35,35,delta('mandate',10)),
      ('decree','Чрезвычайный декрет','Emergency Decree',75,14,delta('mandate',10)+delta('tension',10)),
    ]:
        decision(cat,'FRA_nww_'+key,ru,en,base+f''' visible = {{ has_completed_focus = FRA_nww_session }} cost = {price} days_remove = {days} days_re_enable = 60
          complete_effect = {{ set_country_flag = FRA_negotiation_busy }}
          cancel_trigger = {{ has_capitulated = yes }} cancel_effect = {{ clr_country_flag = FRA_negotiation_busy add_political_power = {price} }}
          remove_effect = {{ clr_country_flag = FRA_negotiation_busy {body} FRA_clamp_meters = yes }}
          ai_will_do = {{ factor = 2 }}''',
          'Переговоры оплачиваются заранее и идут последовательно. Результат выдаётся после завершения; при капитуляции политвласть возвращается. Коалиционное соглашение требует завершить фокус в течение следующих 30 дней.',
          'Negotiations are paid in advance and run one at a time. Effects apply on completion; capitulation refunds political power. A coalition agreement requires completing a focus within the following 30 days.')
    for key,ideology,ru,en,gate in [
      ('republic','democratic','Республиканская кампания','Republican Campaign','OR = { has_country_flag = FRA_route_republic has_country_flag = FRA_route_front has_country_flag = FRA_regime_military }'),
      ('royal','neutrality','Кампания монархических комитетов','Monarchist Committee Campaign','has_country_flag = FRA_route_right NOT = { has_completed_focus = FRA_nww_directory }'),
      ('leagues','fascism','Кампания национальных лиг','National League Campaign','has_completed_focus = FRA_nww_directory'),
      ('workers','communism','Рабочие собрания','Workers Assemblies','has_country_flag = FRA_route_front'),
      ('army','neutrality','Кампания чрезвычайного мандата','Emergency Mandate Campaign','has_country_flag = FRA_route_emergency'),
    ]:
        decision(cat,'FRA_nww_campaign_'+key,ru,en,base+f''' visible = {{ {gate} }} cost = 40 days_remove = 35 days_re_enable = 7
          complete_effect = {{ set_country_flag = FRA_negotiation_busy }}
          cancel_trigger = {{ has_capitulated = yes }} cancel_effect = {{ clr_country_flag = FRA_negotiation_busy add_political_power = 40 }}
          remove_effect = {{ clr_country_flag = FRA_negotiation_busy add_popularity = {{ ideology = {ideology} popularity = 0.05 }} {delta('mandate',5)} FRA_clamp_meters = yes }}
          ai_will_do = {{ factor = 10 }}''',
          '35 дней организационной работы: +5 процентных пунктов поддержки и +5 мандата. Для смены режима нужны подготовительные фокусы и не менее 40% поддержки.',
          '35 days of organisation: +5 percentage points of support and +5 mandate. A regime transition requires preparatory focuses and at least 40% support.')
    decision(cat,'FRA_nww_confidence_vote','Вотум доверия: 90 дней','Vote of Confidence: 90 Days',f'''icon = generic_political_discourse allowed = {{ original_tag = FRA }}
      visible = {{ has_country_flag = FRA_confidence_active }} selectable_mission = no is_good = no days_mission_timeout = 90
      cancel_trigger = {{ OR = {{ {var('mandate','>=',40)} has_capitulated = yes }} }}
      cancel_effect = {{ clr_country_flag = FRA_confidence_active set_country_flag = {{ flag = FRA_confidence_cooldown value = 1 days = 90 }} }}
      timeout_effect = {{ clr_country_flag = FRA_confidence_active set_country_flag = {{ flag = FRA_confidence_cooldown value = 1 days = 90 }} country_event = {{ id = nww_fra.2 days = 1 }} }}''',
      'Поднимите мандат до 40. Провал означает отставку кабинета. Вооружённое столкновение возможно лишь при напряжённости от 80 и организованных противниках.',
      'Restore mandate to 40. Failure means cabinet resignation. Armed conflict is possible only with tension of at least 80 and organised opponents.')
    decision(cat,'FRA_nww_emergency_mandate','Срок чрезвычайного мандата','Emergency Mandate Deadline','''icon = generic_political_discourse allowed = { original_tag = FRA }
      visible = { has_country_flag = FRA_regime_military NOT = { has_country_flag = FRA_emergency_resolved } }
      selectable_mission = no is_good = no days_mission_timeout = 270
      cancel_trigger = { OR = { has_country_flag = FRA_emergency_resolved has_capitulated = yes } }
      timeout_effect = { country_event = { id = nww_fra.3 days = 1 } }''',
      'За 270 дней подготовьте возвращение к выборам или законное продление чрезвычайных полномочий. При провале предстоит политическая развязка.',
      'Within 270 days prepare elections or a legal extension of emergency powers. Failure forces a political reckoning.')

def build_overseas():
    triggers=[]
    for region,ru,en,tags in REGIONS:
        cores='OR = { '+' '.join('is_core_of = '+t for t in tags)+' }'
        held=f'any_owned_state = {{ is_controlled_by = ROOT {cores} }}'
        triggers.append(f'FRA_holds_{region} = {{ {held} }}')
        triggers.append(f'FRA_can_release_{region} = {{ OR = {{ '+ ' '.join(f'AND = {{ {tag} = {{ exists = no }} any_owned_state = {{ is_controlled_by = ROOT is_core_of = {tag} }} }}' for tag in tags)+' } }')
        # All releases are restricted to land actually owned/controlled by France.
        # Existing sovereign recipients cannot be puppeted by a French decision.
        release='';autonomy='';war_release=''
        for tag in tags:
            test=f'any_owned_state = {{ is_controlled_by = ROOT is_core_of = {tag} }} {tag} = {{ exists = no }}'
            transfer=f'every_owned_state = {{ limit = {{ is_controlled_by = ROOT is_core_of = {tag} }} transfer_state_to = {tag} }}'
            release+=f'if = {{ limit = {{ {test} }} {transfer} {tag} = {{ set_country_flag = FRA_compact_partner }} }}\n'
            war_release+=f'if = {{ limit = {{ {test} }} {transfer} declare_war_on = {{ target = {tag} type = annex_everything }} }}\n'
            autonomy+=f'''if = {{ limit = {{ {test} }}
              {transfer}
              if = {{ limit = {{ OR = {{ has_dlc = "Together for Victory" has_dlc = "Man the Guns" }} }}
                set_autonomy = {{ target = {tag} autonomous_state = autonomy_dominion freedom_level = 0.8 }} }}
              else = {{ puppet = {tag} }}
              {tag} = {{ set_country_flag = FRA_compact_partner }} }}'''
        effect('FRA_release_'+region,release+f'set_country_flag = FRA_{region}_independent set_variable = {{ FRA_{region}_pressure = 0 }}')
        effect('FRA_war_release_'+region,war_release+f'set_country_flag = FRA_{region}_independent set_variable = {{ FRA_{region}_pressure = 0 }}')
        effect('FRA_autonomy_'+region,autonomy+f'set_country_flag = FRA_{region}_autonomous set_variable = {{ FRA_{region}_pressure = 0 }}')
        decision('FRA_nww_overseas_category','FRA_nww_invest_'+region,'Инвестиции: '+ru,'Investment: '+en,f'''icon = decision_generic_construction allowed = {{ original_tag = FRA }}
          visible = {{ has_completed_focus = FRA_nww_colonial_schools FRA_holds_{region} = yes NOT = {{ has_country_flag = FRA_{region}_investment }} }}
          available = {{ has_capitulated = no NOT = {{ has_country_flag = FRA_project_busy }} }}
          cost = 50 days_remove = 70
          complete_effect = {{ set_country_flag = FRA_project_busy add_ideas = FRA_nww_project_commitment }}
          cancel_trigger = {{ OR = {{ has_capitulated = yes NOT = {{ FRA_holds_{region} = yes }} }} }}
          cancel_effect = {{ clr_country_flag = FRA_project_busy remove_ideas = FRA_nww_project_commitment add_political_power = 50 }}
          remove_effect = {{ clr_country_flag = FRA_project_busy remove_ideas = FRA_nww_project_commitment
            if = {{ limit = {{ FRA_holds_{region} = yes }} set_country_flag = FRA_{region}_investment {delta(region+'_pressure',-20)}
              random_owned_controlled_state = {{ limit = {{ {cores} }} add_extra_state_shared_building_slots = 1 add_building_construction = {{ type = industrial_complex level = 1 instant_build = yes }} }} }} FRA_clamp_meters = yes }}
          ai_will_do = {{ factor = 5 }}''',
          '70 дней, 50 политвласти и 3 гражданских завода на время работ. После завершения: один местный завод, −20 давления, далее −3 давления за 30 дней. При отмене политвласть возвращается.',
          '70 days, 50 political power and 3 civilian factories while work proceeds. Completion adds one local factory, reduces pressure by 20 and then by 3 every 30 days. Cancellation refunds political power.')
        decision('FRA_nww_overseas_category','FRA_nww_negotiate_'+region,'Переговоры: '+ru,'Negotiations: '+en,f'''icon = generic_political_discourse allowed = {{ original_tag = FRA }}
          visible = {{ has_completed_focus = FRA_nww_overseas_conference FRA_holds_{region} = yes NOT = {{ has_country_flag = FRA_{region}_treaty }} }}
          available = {{ has_capitulated = no NOT = {{ has_country_flag = FRA_negotiation_busy }} }} cost = 50 days_remove = 35
          complete_effect = {{ set_country_flag = FRA_negotiation_busy }}
          cancel_trigger = {{ OR = {{ has_capitulated = yes NOT = {{ FRA_holds_{region} = yes }} }} }}
          cancel_effect = {{ clr_country_flag = FRA_negotiation_busy add_political_power = 50 }}
          remove_effect = {{ clr_country_flag = FRA_negotiation_busy if = {{ limit = {{ FRA_holds_{region} = yes }} country_event = {{ id = nww_fra.{100+REGIONS.index((region,ru,en,tags))} days = 1 }} }} }}
          ai_will_do = {{ factor = 3 }}''',
          'Оплаченные последовательные переговоры откроют конференцию представителей. Можно предложить представительство, автономию или независимость. Передачи чужих территорий не происходит.',
          'Paid, serialised talks open a representatives conference. Offer representation, autonomy or independence. Foreign-owned territory is never transferred.')
        decision('FRA_nww_overseas_category','FRA_nww_garrison_'+region,'Усилить гарнизоны: '+ru,'Reinforce Garrisons: '+en,f'''icon = generic_prepare_civil_war allowed = {{ original_tag = FRA }}
          visible = {{ has_country_flag = FRA_policy_extraction FRA_holds_{region} = yes }}
          available = {{ has_equipment = {{ infantry_equipment > 499 }} }} cost = 35 days_remove = 30 days_re_enable = 90
          complete_effect = {{ add_equipment_to_stockpile = {{ type = infantry_equipment amount = -500 }} }}
          remove_effect = {{ {delta(region+'_pressure',-10)} FRA_clamp_meters = yes }}
          ai_will_do = {{ factor = 1 }}''',
          'Расход 500 единиц пехотного снаряжения и 35 политвласти. Через 30 дней давление снижается на 10; причины роста сохраняются.',
          'Costs 500 infantry equipment and 35 political power. After 30 days pressure falls by 10; its underlying causes remain.')
        decision('FRA_nww_overseas_category','FRA_nww_'+region+'_ultimatum','Кризис: '+ru,'Crisis: '+en,f'''icon = generic_prepare_civil_war allowed = {{ original_tag = FRA }}
          visible = {{ has_country_flag = FRA_{region}_crisis }} selectable_mission = no is_good = no days_mission_timeout = 120
          cancel_trigger = {{ OR = {{ NOT = {{ FRA_holds_{region} = yes }} {var(region+'_pressure','<',60)} has_country_flag = FRA_{region}_treaty has_capitulated = yes }} }}
          cancel_effect = {{ clr_country_flag = FRA_{region}_crisis set_country_flag = {{ flag = FRA_{region}_cooldown value = 1 days = 180 }} }}
          timeout_effect = {{ clr_country_flag = FRA_{region}_crisis set_country_flag = {{ flag = FRA_{region}_cooldown value = 1 days = 180 }} country_event = {{ id = nww_fra.{120+REGIONS.index((region,ru,en,tags))} days = 1 }} }}''',
          '120 дней на соглашение или снижение давления ниже 60. По истечении срока будет предложен выбор между уходом и региональной войной.',
          '120 days to reach an agreement or reduce pressure below 60. Expiry forces a choice between withdrawal and a regional war.')
    write('common/scripted_triggers/FRA_triggers.txt','\n'.join(triggers))

def build_projects():
    # One project at a time. Ownership/control checked at start and completion.
    for key,ru,en,gate,sid,kind,count in [
      ('eastern_forts','Восточные укрепления','Eastern Fortifications','lorraine',18,'bunker',2),
      ('northern_forts','Северные укрепления','Northern Fortifications','north_approaches',29,'bunker',2),
      ('alpine_forts','Альпийские укрепления','Alpine Fortifications','alpine_passes',735,'bunker',2),
      ('civil_programme','Долгосрочное гражданское строительство','Long-Term Civil Construction','internal_market',None,'industrial_complex',2),
      ('mobilisation_conversion','Мобилизационная конверсия','Mobilisation Conversion','conversion',None,'arms_factory',2),
    ]:
        held=f'{sid} = {{ is_owned_and_controlled_by = ROOT }}' if sid else 'any_owned_state = { is_core_of = ROOT is_on_continent = europe is_controlled_by = ROOT }'
        work=state_build(sid,kind,count) if sid else build(kind,count)
        if kind=='bunker':
            provinces={18:[5291,3560],29:[575,11483],735:[764,9909]}[sid]
            work=f'{sid} = {{ '+ ' '.join(f'add_building_construction = {{ type = bunker level = {count} province = {p} instant_build = yes }}' for p in provinces)+' }'
        decision('FRA_nww_projects_category','FRA_nww_project_'+key,ru,en,f'''icon = decision_generic_construction allowed = {{ original_tag = FRA }}
          visible = {{ has_completed_focus = FRA_nww_{gate} NOT = {{ has_country_flag = FRA_project_{key}_done }} }}
          available = {{ has_capitulated = no {held} NOT = {{ has_country_flag = FRA_project_busy }} {'has_war = yes' if key=='mobilisation_conversion' else ''} }}
          cost = 50 days_remove = 120
          complete_effect = {{ set_country_flag = FRA_project_busy add_ideas = FRA_nww_project_commitment }}
          cancel_trigger = {{ OR = {{ has_capitulated = yes NOT = {{ {held} }} }} }}
          cancel_effect = {{ clr_country_flag = FRA_project_busy remove_ideas = FRA_nww_project_commitment add_political_power = 50 }}
          remove_effect = {{ clr_country_flag = FRA_project_busy remove_ideas = FRA_nww_project_commitment
            if = {{ limit = {{ {held} NOT = {{ has_country_flag = FRA_project_{key}_done }} }} {work} set_country_flag = FRA_project_{key}_done }} }}
          ai_will_do = {{ factor = 2 }}''',
          '120 дней, 50 политвласти и 3 гражданских завода на время программы. Награда выдаётся один раз после завершения. Нужны собственные контролируемые территории; отмена возвращает политвласть.',
          '120 days, 50 political power and 3 civilian factories committed during the programme. The reward is granted once on completion. Requires owned, controlled territory; cancellation refunds political power.')

EVENTS=[]
def event(eid,ru,en,desc,edesc,options,picture='GFX_report_event_generic_parliament'):
    name=f'nww_fra.{eid}'
    label(name+'.t',ru,en);label(name+'.d',desc,edesc)
    chunks=[]
    for i,(oru,oen,body) in enumerate(options):
        key=name+f'.{chr(97+i)}';label(key,oru,oen)
        chunks.append(f'option = {{ name = {key} {body} }}')
    EVENTS.append(f'country_event = {{ id = {name} title = {name}.t desc = {name}.d picture = {picture} is_triggered_only = yes '+'\n'.join(chunks)+' }')

def build_events():
    event(1,'Республика на распутье','Republic at the Crossroads',
      'Великая война не состоялась. Но заводы работают неполную неделю, парламентские кабинеты живут от голосования до голосования, а улица перестаёт верить обещаниям. Наши люди и предприятия сохранились. Предстоит вернуть государству способность действовать.',
      'The Great War never came. Yet factories work short weeks, cabinets survive vote by vote and the streets lose faith in promises. Our people and industry survived. We must restore the state\'s ability to act.',
      [('Открыть работу Палаты.','Let the Chamber begin its work.','add_stability = 0.05')])
    event(2,'Кабинет утратил доверие','The Cabinet Loses Confidence',
      'Палата отказала правительству в поддержке. Новая коалиция может получить временный кредит доверия. Если вооружённые организации готовы к столкновению, остаётся последняя возможность созвать согласительную конференцию.',
      'The Chamber has denied the government its support. A new coalition may gain temporary confidence. If armed organisations are ready for conflict, a reconciliation conference remains the last opportunity.',[
      ('Сформировать новый кабинет.','Form a new cabinet.','ai_chance = { factor = 90 } add_stability = -0.05 set_variable = { FRA_mandate = 35 } '+delta('tension',5)),
      ('Созвать оплачиваемую согласительную конференцию.','Fund a reconciliation conference.','trigger = { has_political_power > 74 } ai_chance = { factor = 10 } add_political_power = -75 set_variable = { FRA_mandate = 40 } '+delta('tension',-15)),
      ('Противостояние выходит из-под контроля.','The confrontation spirals out of control.',f'''trigger = {{ {var('tension','>=',80)} OR = {{ has_country_flag = FRA_armed_leagues has_country_flag = FRA_armed_workers }} NOT = {{ has_country_flag = FRA_civil_war_started }} }}
        ai_chance = {{ factor = 0 }} set_country_flag = FRA_civil_war_started
        if = {{ limit = {{ has_government = communism }} start_civil_war = {{ ideology = fascism size = 0.35 }} }}
        else = {{ start_civil_war = {{ ideology = communism size = 0.35 }} }}''')])
    event(3,'Полномочия военного кабинета истекли','The Military Cabinet Mandate Expires',
      'Обещанный срок чрезвычайного управления истёк. Продление без нового законного основания разрушит доверие к командованию.',
      'The promised period of emergency rule has expired. An extension without a new legal basis will destroy confidence in the command.',[
      ('Вернуть власть гражданскому кабинету.','Return power to a civilian cabinet.','trigger = { NOT = { democratic < 0.40 } } ai_chance = { factor = 90 } FRA_return_democracy = yes add_stability = -0.05'),
      ('Удержать власть чрезвычайным декретом.','Retain power by emergency decree.','ai_chance = { factor = 10 } set_country_flag = FRA_emergency_resolved add_ideas = FRA_nww_coercion add_stability = -0.10 '+delta('tension',25)+delta('mandate',-15))])
    for idx,(region,ru,en,tags) in enumerate(REGIONS):
        event(100+idx,'Заморская конференция: '+ru,'Overseas Conference: '+en,
          'Делегаты требуют определённого статуса, бюджета местного управления и гарантий исполнения. Соглашение должно учитывать выбранный Парижем курс. Предложение ещё предстоит утвердить представителям территории.',
          'Delegates demand a defined status, funding for local government and guarantees of implementation. The agreement must reflect the course chosen in Paris. Territorial representatives must still ratify the offer.',[
          ('Предложить представительство и местный бюджет.','Offer representation and a local budget.',f'''trigger = {{ has_country_flag = FRA_policy_representation }} ai_chance = {{ factor = 60 }}
            set_country_flag = FRA_{region}_offer_representation country_event = {{ id = nww_fra.{140+idx} days = 7 }}'''),
          ('Предложить автономное соглашение.','Offer an autonomy agreement.',f'''trigger = {{ has_completed_focus = FRA_nww_overseas_compact FRA_can_release_{region} = yes }} ai_chance = {{ factor = 25 }}
            set_country_flag = FRA_{region}_offer_autonomy country_event = {{ id = nww_fra.{140+idx} days = 7 }}'''),
          ('Предложить согласованную независимость.','Offer negotiated independence.',f'''trigger = {{ has_country_flag = FRA_policy_selfdetermination FRA_can_release_{region} = yes }} ai_chance = {{ factor = 60 }}
            set_country_flag = FRA_{region}_offer_independence country_event = {{ id = nww_fra.{140+idx} days = 7 }}'''),
          ('Продолжить обсуждение без соглашения.','Continue talks without an agreement.',delta(region+'_pressure',5)+' add_political_power = 25')])
        # Acceptance is a separate delegation outcome, not a unilateral annexation/puppet effect.
        ratify=f'''if = {{ limit = {{ FRA_holds_{region} = yes }}
          if = {{ limit = {{ {var(region+'_pressure','<',80)} }}
            set_country_flag = FRA_{region}_treaty
            if = {{ limit = {{ has_country_flag = FRA_{region}_offer_independence }} FRA_release_{region} = yes }}
            else_if = {{ limit = {{ has_country_flag = FRA_{region}_offer_autonomy }} FRA_autonomy_{region} = yes }}
            else = {{ set_country_flag = FRA_{region}_represented {delta(region+'_pressure',-25)} }}
          }} else = {{ {delta(region+'_pressure',5)} add_political_power = 25 }}
          }} if = {{ limit = {{ FRA_holds_{region} = yes NOT = {{ has_country_flag = FRA_{region}_represented }} }} clr_country_flag = FRA_{region}_treaty }}
          clr_country_flag = FRA_{region}_offer_representation clr_country_flag = FRA_{region}_offer_autonomy clr_country_flag = FRA_{region}_offer_independence FRA_clamp_meters = yes'''
        event(140+idx,'Ответ представителей: '+ru,'Delegates Reply: '+en,
          'Представители рассмотрели предложение. При давлении ниже 80 соглашение утверждается; на пороге восстания делегация уже не может гарантировать его исполнение. Сначала потребуется снизить напряжение.',
          'Representatives have reviewed the offer. They ratify it if pressure is below 80; on the brink of revolt the delegation can no longer guarantee implementation. Pressure must first be reduced.',[
          ('Огласить решение делегации.','Announce the delegation decision.',ratify)])
        event(120+idx,'Заморское урегулирование сорвано: '+ru,'Overseas Settlement Fails: '+en,
          'Истёк срок переговоров. Местные организации объявляют разрыв с Парижем. Правительство должно признать выход или начать открытую военную кампанию; одной полицейской мерой конфликт уже не решить.',
          'Negotiations have expired. Local organisations announce their break with Paris. The government must recognise their departure or begin an open military campaign; policing can no longer resolve the conflict.',[
          ('Признать выход и избежать войны.','Recognise departure and avoid war.',f'ai_chance = {{ factor = 80 }} if = {{ limit = {{ FRA_holds_{region} = yes }} FRA_release_{region} = yes }}'),
          ('Начать региональную кампанию.','Begin a regional campaign.',f'ai_chance = {{ factor = 20 }} if = {{ limit = {{ FRA_holds_{region} = yes }} FRA_war_release_{region} = yes }} '+delta('tension',10))])

def build_diplomacy():
    eligible='''OR = {
      AND = { ROOT = { has_country_flag = FRA_western_diplomacy } OR = { tag = ENG tag = BEL tag = LTB } has_government = democratic }
      AND = { ROOT = { has_country_flag = FRA_latin_diplomacy } OR = { tag = ITA tag = SPR } OR = { has_government = fascism has_government = neutrality } }
      AND = { ROOT = { has_country_flag = FRA_continental_diplomacy } OR = { tag = GER tag = AUS } has_government = neutrality }
      AND = { ROOT = { has_country_flag = FRA_workers_diplomacy } OR = { tag = SOV tag = UKR tag = MKN } OR = { has_government = communism has_government = democratic } }
      has_country_flag = FRA_compact_partner
    }'''
    decision('FRA_nww_diplomacy_category','FRA_nww_security_offer','Предложить договор: [FROM.GetName]','Offer a Treaty: [FROM.GetName]',f'''icon = generic_improve_relations allowed = {{ original_tag = FRA }}
      target_root_trigger = {{ has_completed_focus = FRA_nww_foreign_review }}
      target_trigger = {{ exists = yes NOT = {{ original_tag = FRA }} is_subject = no NOT = {{ has_war_with = ROOT }} {eligible} }}
      visible = {{ NOT = {{ FROM = {{ has_country_flag = FRA_security_answered }} }} }}
      available = {{ has_capitulated = no NOT = {{ has_country_flag = FRA_negotiation_busy }} }}
      cost = 50 days_remove = 35
      complete_effect = {{ set_country_flag = FRA_negotiation_busy }}
      cancel_trigger = {{ OR = {{ has_capitulated = yes FROM = {{ exists = no }} has_war_with = FROM }} }}
      cancel_effect = {{ clr_country_flag = FRA_negotiation_busy add_political_power = 50 }}
      remove_effect = {{ clr_country_flag = FRA_negotiation_busy if = {{ limit = {{ FROM = {{ exists = yes }} NOT = {{ has_war_with = FROM }} }} FROM = {{ country_event = {{ id = nww_fra.200 days = 1 }} }} }} }}
      ai_will_do = {{ factor = 3 }}''',
      '35-дневные переговоры о ненападении и научном сотрудничестве. Получатель самостоятельно принимает или отклоняет предложение; членство в союзе не меняется.',
      '35-day talks on non-aggression and scientific cooperation. The recipient accepts or refuses independently; faction membership remains unchanged.')
    event(200,'Предложение Парижа','An Offer from Paris',
      'Франция предлагает договор о ненападении и, при готовности её научной сети, участие в совместных исследованиях. Мы сохраняем собственное правительство и внешнеполитические обязательства.',
      'France offers a non-aggression pact and, once its scientific network is ready, participation in joint research. Our government and existing foreign commitments are retained.',[
      ('Принять договор.','Accept the treaty.','''trigger = { FRA = { exists = yes } NOT = { has_war_with = FRA } } ai_chance = { factor = 65 }
        set_country_flag = FRA_security_answered set_country_flag = FRA_security_partner
        diplomatic_relation = { country = FRA relation = non_aggression_pact active = yes }
        if = { limit = { FRA = { has_completed_focus = FRA_nww_science_network } } add_to_tech_sharing_group = FRA_nww_science_network }
        FRA = { country_event = { id = nww_fra.201 days = 1 } }'''),
      ('Отклонить предложение.','Decline the offer.','ai_chance = { factor = 35 } set_country_flag = FRA_security_answered FRA = { country_event = { id = nww_fra.202 days = 1 } }')])
    event(201,'Договор принят','Treaty Accepted','Наше предложение принято. Договор не передаёт Франции территории или право распоряжаться армией партнёра.','Our offer has been accepted. The treaty transfers neither territory nor command over the partner\'s army to France.',[('Сотрудничество начинается.','Cooperation begins.','add_political_power = 25')])
    event(202,'Предложение отклонено','Offer Declined','Переговоры не дали соглашения. Отказ не создаёт повода к войне.','The talks produced no agreement. A refusal does not create a war goal.',[('Принять к сведению.','Take note.','add_political_power = 25')])
    # Alliance is a second, separately consented step; existing alliances are respected.
    decision('FRA_nww_diplomacy_category','FRA_nww_alliance_offer','Предложить оборонный союз: [FROM.GetName]','Offer a Defensive Alliance: [FROM.GetName]','''icon = generic_improve_relations allowed = { original_tag = FRA }
      target_root_trigger = { has_country_flag = FRA_regime_settled OR = { is_in_faction = no is_faction_leader = yes } }
      target_trigger = { exists = yes has_country_flag = FRA_security_partner is_subject = no is_in_faction = no NOT = { has_war_with = ROOT } }
      visible = { NOT = { FROM = { has_country_flag = FRA_alliance_answered } } }
      available = { has_capitulated = no } cost = 75 days_re_enable = 90
      complete_effect = { FROM = { country_event = { id = nww_fra.203 days = 1 } } }
      ai_will_do = { factor = 2 }''',
      'Партнёр должен отдельно одобрить оборонный союз. Франция должна возглавлять свой союз или не состоять в другом. Существующие союзы получателя сохраняются.',
      'The partner must separately approve a defensive alliance. France must lead its faction or belong to none. Existing recipient alliances are respected.')
    event(203,'Оборонный союз с Францией','Defensive Alliance with France','Париж предлагает перейти от договора к общему оборонному союзу. Это отдельное решение нашего правительства.','Paris proposes moving from a treaty to a joint defensive alliance. This is a separate decision for our government.',[
      ('Вступить в союз.','Join the alliance.','''trigger = { is_in_faction = no is_subject = no FRA = { exists = yes OR = { is_in_faction = no is_faction_leader = yes } } NOT = { has_war_with = FRA } }
        ai_chance = { factor = 55 } set_country_flag = FRA_alliance_answered FRA = { if = { limit = { is_in_faction = no } create_faction = FRA_nww_defensive_accord } add_to_faction = ROOT }'''),
      ('Сохранить самостоятельность.','Retain our independence.','ai_chance = { factor = 45 } set_country_flag = FRA_alliance_answered')])
    event(204,'Французский ультиматум на Рейне','The French Rhine Ultimatum','Париж требует отказаться от давления на соседей и заключить договор о ненападении. Французские националисты готовы использовать отказ как основание для войны. Уступка не передаёт территории.','Paris demands an end to pressure on its neighbours and a non-aggression treaty. French nationalists are prepared to use refusal as grounds for war. Acceptance transfers no territory.',[
      ('Заключить договор.','Conclude the treaty.','ai_chance = { factor = 10 } diplomatic_relation = { country = FRA relation = non_aggression_pact active = yes }'),
      ('Отвергнуть ультиматум.','Reject the ultimatum.','ai_chance = { factor = 90 } FRA = { if = { limit = { has_completed_focus = FRA_nww_rhine_ultimatum NOT = { has_war_with = GER } } create_wargoal = { type = annex_everything target = GER expire = 365 } } }')])
    label('FRA_nww_defensive_accord','Парижское оборонное соглашение','Paris Defensive Accord')
    write('common/technology_sharing/FRA_research.txt','''technology_sharing_group = {
      id = FRA_nww_science_network name = FRA_nww_science_network_name desc = FRA_nww_science_network_desc
      picture = GFX_technology_sharing_default research_sharing_per_country_bonus = 0.05
      available = { FRA = { exists = yes has_completed_focus = FRA_nww_science_network } NOT = { has_war_with = FRA } }
    }''')
    label('FRA_nww_science_network_name','Парижская научная сеть','Paris Scientific Network','Исследовательский обмен с согласившимися участниками.','Research exchange among consenting participants.')
    LOC['FRA_nww_science_network_desc']=LOC.pop('FRA_nww_science_network_name_desc')

def build_gui():
    categories=[('mandate','Мандат Республики','Mandate of the Republic'),('overseas','Заморский договор','Overseas Compact'),('projects','Государственные программы','Public Programmes'),('diplomacy','Французские соглашения','French Agreements')]
    blocks=[]
    for key,ru,en in categories:
        name='FRA_nww_'+key+'_category'
        label(name,ru,en,'Порядок проведения программ и текущие показатели показаны на панели.','The panel shows programme procedures and current values.')
        gui=f'scripted_gui = FRA_{key}_ui' if key in ('mandate','overseas') else ''
        blocks.append(f'{name} = {{ icon = GFX_FRA_nww_{"overseas" if key=="overseas" else "republic"} allowed = {{ original_tag = FRA }} visible = {{ has_focus_tree = french_focus }} {gui} }}')
    write('common/decisions/categories/FRA_categories.txt','\n'.join(blocks))
    gui=['guiTypes = {']; scripted=['scripted_gui = {']
    for panel,height in [('mandate',240),('overseas',410)]:
        gui.append(f'containerWindowType = {{ name = "FRA_{panel}_window" position = {{ x = 0 y = 0 }} size = {{ width = 100% height = {height} }}')
        gui.append(f'iconType = {{ name = "FRA_{panel}_background" spriteType = "GFX_FRA_{panel}_panel" orientation = center_up position = {{ x = -220 y = 0 }} }}')
        scripted.append(f'FRA_{panel}_ui = {{ context_type = decision_category window_name = FRA_{panel}_window visible = {{ original_tag = FRA }} triggers = {{')
        def text_box(name,y,text,help,width=408):
            gui.append(f'instantTextBoxType = {{ name = "{name}" orientation = center_up position = {{ x = -204 y = {y} }} font = "hoi_16mbs" text = "{text}" format = center maxWidth = {width} maxHeight = 30 pdx_tooltip = {help} }}')
        text_box('FRA_'+panel+'_title',14,'FRA_panel_'+panel+'_title','FRA_'+panel+'_help')
        meters=[('mandate',62),('tension',139)] if panel=='mandate' else [(r[0]+'_pressure',54+i*54) for i,r in enumerate(REGIONS)]
        for meter,y in meters:
            text_box('FRA_'+meter+'_value',y,'FRA_panel_'+meter,'FRA_'+panel+'_help')
            for i in range(10):
                x=-190+i*38
                gui.append(f'iconType = {{ name = "FRA_{meter}_socket_{i}" spriteType = "GFX_FRA_meter_socket" orientation = center_up position = {{ x = {x} y = {y+27} }} }}')
                gui.append(f'iconType = {{ name = "FRA_{meter}_fill_{i}" spriteType = "GFX_FRA_meter_{"red" if meter=="tension" else "gold"}" orientation = center_up position = {{ x = {x} y = {y+27} }} pdx_tooltip = FRA_{panel}_help }}')
                scripted.append(f'FRA_{meter}_fill_{i}_visible = {{ {var(meter,">=",(i+1)*10)} }}')
        if panel=='mandate': text_box('FRA_mandate_forecast',203,'FRA_panel_forecast','FRA_mandate_help')
        else: text_box('FRA_overseas_forecast',383,'FRA_panel_overseas_forecast','FRA_overseas_help')
        gui.append('}');scripted.append('} }')
    gui.append('}');scripted.append('}')
    write('interface/FRA_decisions.gui','\n'.join(gui));write('common/scripted_guis/FRA_gui.txt','\n'.join(scripted))
    label('FRA_panel_mandate_title','ПАЛАТА И УЛИЦА','THE CHAMBER AND THE STREETS')
    label('FRA_panel_overseas_title','ЗАМОРСКИЙ ДОГОВОР','THE OVERSEAS COMPACT')
    label('FRA_panel_mandate','Мандат кабинета: [?FRA_mandate|0]/100','Cabinet mandate: [?FRA_mandate|0]/100')
    label('FRA_panel_tension','Уличная напряжённость: [?FRA_tension|0]/100','Street tension: [?FRA_tension|0]/100')
    label('FRA_panel_forecast','[FRA.GetFRARegimeStatus]','[FRA.GetFRARegimeStatus]')
    label('FRA_panel_overseas_forecast','[FRA.GetFRAOverseasForecast]','[FRA.GetFRAOverseasForecast]')
    custom=['defined_text = { name = GetFRARegimeStatus text = { trigger = { has_country_flag = FRA_regime_settled } localization_key = FRA_status_settled } text = { localization_key = FRA_status_unsettled } }',
            'defined_text = { name = GetFRAOverseasForecast text = { trigger = { has_country_flag = FRA_policy_extraction } localization_key = FRA_forecast_extraction } text = { localization_key = FRA_forecast_default } }']
    spirit_names={
      'state':('has_country_flag = FRA_regime_settled','Институты национального согласия','Institutions of National Agreement'),
      'economy':('has_completed_focus = FRA_nww_internal_market','Модернизированная французская экономика','Modernised French Economy'),
      'army':('has_completed_focus = FRA_nww_signals_supply','Обновлённая система сухопутных войск','Reformed Army System'),
      'air':('has_completed_focus = FRA_nww_air_command','Самостоятельные военно-воздушные силы','Independent Air Force'),
      'navy':('has_completed_focus = FRA_nww_two_seas','Обновлённый флот двух морей','Modernised Fleet of Two Seas'),
    }
    for key,(condition,ru,en) in spirit_names.items():
        getter='GetFRASpirit'+key.title()
        label('FRA_spirit_'+key+'_initial',*LOC['FRA_nww_'+key]);label('FRA_spirit_'+key+'_reformed',ru,en)
        LOC['FRA_nww_'+key]=(f'[FRA.{getter}]',f'[FRA.{getter}]')
        custom.append(f'defined_text = {{ name = {getter} text = {{ trigger = {{ {condition} }} localization_key = FRA_spirit_{key}_reformed }} text = {{ localization_key = FRA_spirit_{key}_initial }} }}')
    label('FRA_status_settled','Институты закреплены: напряжённость −2 за 30 дней','Institutions settled: tension −2 every 30 days')
    label('FRA_status_unsettled','До урегулирования: мандат −2 за 30 дней','Before settlement: mandate −2 every 30 days')
    label('FRA_forecast_extraction','Концессии: давление +5 за 30 дней','Concessions: pressure +5 every 30 days')
    label('FRA_forecast_default','Без вложений +2; после вложений −3 за 30 дней','Without investment +2; after investment −3 per 30 days')
    for region,ru,en,tags in REGIONS:
        getter='GetFRA'+''.join(w.title() for w in region.split('_'))+'Status'
        custom.append(f'''defined_text = {{ name = {getter}
          text = {{ trigger = {{ FRA_holds_{region} = yes OR = {{ has_country_flag = FRA_{region}_independent has_country_flag = FRA_{region}_autonomous }} }} localization_key = FRA_status_partial }}
          text = {{ trigger = {{ has_country_flag = FRA_{region}_independent }} localization_key = FRA_status_independent }}
          text = {{ trigger = {{ has_country_flag = FRA_{region}_autonomous }} localization_key = FRA_status_autonomous }}
          text = {{ trigger = {{ has_country_flag = FRA_{region}_represented }} localization_key = FRA_status_represented }}
          text = {{ trigger = {{ FRA_holds_{region} = no }} localization_key = FRA_status_no_control }}
          text = {{ localization_key = FRA_status_direct }} }}''')
        label('FRA_panel_'+region+'_pressure',ru+': [?FRA_'+region+'_pressure|0] — [FRA.'+getter+']',en+': [?FRA_'+region+'_pressure|0] — [FRA.'+getter+']')
    for key,ru,en in [('partial','частичное урегулирование','partial settlement'),('independent','независимость','independent'),('autonomous','автономия','autonomy'),('represented','представительство','representation'),('no_control','нет управления','no administration'),('direct','прямое управление','direct administration')]: label('FRA_status_'+key,ru,en)
    write('common/scripted_localisation/FRA_localization.txt','\n'.join(custom))
    label('FRA_mandate_help','Мандат ниже 25 открывает 90-дневный вотум доверия: восстановите его до 40. Без урегулирования −2 мандата за 30 дней. Каждый завершённый фокус даёт +1 и исполняет коалиционное обещание. Невыполненное обещание: −5 мандата и +5 напряжённости. Гражданская война требует напряжённости от 80, вооружённых организаций и провала урегулирования.','Mandate below 25 opens a 90-day confidence vote: restore it to 40. Before settlement lose 2 mandate per 30 days. Each completed focus adds 1 and fulfils a coalition promise. A broken promise costs 5 mandate and adds 5 tension. Civil war requires tension of at least 80, armed organisations and failed reconciliation.')
    label('FRA_overseas_help','Проверка каждые 30 дней. Без вложений давление +2; после вложений −3; при концессиях +5. От 80 начинается кризис на 120 дней: заключите договор или снизьте давление ниже 60. Инвестиции требуют 70 дней, 50 политвласти и 3 гражданских завода. Территории передаются только из фактически управляемых французских владений.','Checked every 30 days. Pressure: +2 without investment, −3 after investment, +5 under concessions. At 80 a 120-day crisis begins: negotiate a treaty or reduce pressure below 60. Investment takes 70 days, 50 political power and 3 civilian factories. Only actually administered French possessions may be transferred.')

AI_ROUTES=['REPUBLIC','MONARCHY','LEAGUES','SOCIAL','COUNCILS','PLAN','MILITARY']

def build_ai():
    rules='FRA_ai_behavior = { name = FRA_AI_BEHAVIOR group = RULE_GROUP_AI_BEHAVIOR default = { name = DEFAULT text = RULE_OPTION_DEFAULT desc = FRA_AI_DEFAULT_DESC }\n'
    label('FRA_AI_BEHAVIOR','Франция: политический курс','France: Political Course')
    label('FRA_AI_DEFAULT_DESC','Исторический ИИ NWW реформирует республику; неисторический выбирает связный альтернативный план.','NWW historical AI reforms the republic; nonhistorical AI chooses a coherent alternative plan.')
    for route in ['RANDOM',*AI_ROUTES]:
        rules+=f'option = {{ name = {route} text = FRA_AI_{route} desc = FRA_AI_{route}_DESC }}\n'
        ru,en={
          'RANDOM':('Случайный связный курс','Random Coherent Course'),
          'REPUBLIC':('Реформированная республика','Reformed Republic'),
          'MONARCHY':('Орлеанская монархия','Orleanist Monarchy'),
          'LEAGUES':('Национальные лиги','National Leagues'),
          'SOCIAL':('Социальная республика','Social Republic'),
          'COUNCILS':('Трудовые советы','Labour Councils'),
          'PLAN':('Централизованный социализм','Centralised Socialism'),
          'MILITARY':('Военный кабинет','Military Cabinet'),
        }[route]
        label('FRA_AI_'+route,ru,en);label('FRA_AI_'+route+'_DESC','Последовательный курс: '+ru+'. Явное правило имеет приоритет над историческим режимом.','Coherent course: '+en+'. Explicit rules override historical mode.')
    rules+='}'
    # Avoid duplicate game-rule IDs: preserve the native registry and replace
    # its direct FRA entry only. All French content remains country-owned.
    native_rules=read(GAME/'common/game_rules/00_game_rules.txt')
    replacement=parse(rules)[0]
    native_rules=[replacement if k=='FRA_ai_behavior' else (k,v,o) for k,v,o in native_rules]
    write('common/game_rules/00_game_rules.txt','# Only FRA_ai_behavior is replaced; country implementation: FRA_focuses.txt and FRA_plans.txt.\n'+dump(native_rules))
    write('common/game_rules/FRA_rules.txt','# FRA rule is defined exactly once in the native registry override 00_game_rules.txt.')
    selection=''
    for i,route in enumerate(AI_ROUTES):
        selection+=f'{"if" if i==0 else "else_if"} = {{ limit = {{ has_game_rule = {{ rule = FRA_ai_behavior option = {route} }} }} set_country_flag = FRA_ai_{route} }}\n'
    selection+='''else_if = { limit = { has_game_rule = { rule = FRA_ai_behavior option = DEFAULT } is_historical_focus_on = yes } set_country_flag = FRA_ai_REPUBLIC }
      else = { random_list = { '''+' '.join(f'20 = {{ set_country_flag = FRA_ai_{r} }}' for r in AI_ROUTES)+' } }'
    # Actual game trigger spelling is is_historical_focus_on in decisions; plans use same documented spelling.
    selection=selection.replace('is_historical_focus_on','is_historical_focus_on')
    effect('FRA_select_ai_route',selection)
    campaign=''
    for i,(route,ideology) in enumerate([('REPUBLIC','democratic'),('MONARCHY','neutrality'),('LEAGUES','fascism'),('SOCIAL','democratic'),('COUNCILS','communism'),('PLAN','communism'),('MILITARY','neutrality')]):
        campaign+=f'''{"if" if i==0 else "else_if"} = {{ limit = {{ has_country_flag = FRA_ai_{route} {ideology} < 0.40 has_political_power > 39 NOT = {{ has_country_flag = FRA_negotiation_busy }} }}
          add_political_power = -40 add_popularity = {{ ideology = {ideology} popularity = 0.05 }} {delta('mandate',5)} }}'''
    effect('FRA_ai_campaign',campaign)
    opening=['session','accounts','consultations']
    paths={
      'REPUBLIC':['republic','commission','contracts','responsible','arbitration','municipal_credit','audit_court','civil_service','renewal','rights','republic_institutions'],
      'MONARCHY':['right','leagues_discipline','garrisons','powers_crisis','orleanists','crown_law','royal_cabinet','royal_charter','crown_service'],
      'LEAGUES':['right','leagues_discipline','garrisons','powers_crisis','directory','league_state','corporate_chamber','national_movement','league_administration'],
      'SOCIAL':['front','left_talks','public_works','labour_charter','social_republic','collective_contracts','social_insurance','social_arbitration'],
      'COUNCILS':['front','left_talks','public_works','labour_charter','councils','cooperatives','elected_boards','councils_congress'],
      'PLAN':['front','left_talks','public_works','labour_charter','central_plan','national_banks','investment_plan','planning_commission'],
      'MILITARY':['emergency','disarm_militias','emergency_legal','military_cabinet','army_neutrality','civil_administration','defence_budget','extend_mandate'],
    }
    economy=['bank_audit','public_bank','housing','municipal_orders','rail_nodes','coal_basins','electrification','regional','west_industry','provincial_schools','internal_market']
    military=['maneuvers','staff_college','signals_supply','methodical','artillery_plans','mobile_reserve','fort_counterattack','methodical_system','officer_corps']
    plans=[]
    for route,path in paths.items():
        order=opening+path+economy+['research_council','university_contract','polytechnics','fourth_slot']+military+['air_command','flight_schools','engine_standards','airfields','tactical_air','tactical_groups','air_watch','interception','fleet_audit','training_squadrons','bases_fuel','atlantic','asw']
        opposite=[p[0] for r,p in paths.items() if r!=route and p[0]!=path[0]]
        factors=' '.join('FRA_nww_'+k+' = 0' for k in set(opposite))
        plans.append(f'''FRA_nww_plan_{route} = {{ name = "NWW France {route}" desc = "" allowed = {{ original_tag = FRA }}
          enable = {{ has_focus_tree = french_focus has_country_flag = FRA_ai_{route} }} abort = {{ is_subject = yes }}
          ai_national_focuses = {{ {' '.join('FRA_nww_'+k for k in order)} }}
          weight = {{ factor = 100 }} focus_factors = {{ {factors} }} }}''')
    write('common/ai_strategy_plans/FRA_plans.txt','\n'.join(plans))
    for name in ['FRA_historical_strategy_plan.txt','FRA_alternate_strategy_plan.txt']:
        write('common/ai_strategy_plans/'+name,'# Native plans replaced by FRA_plans.txt for the NWW setting.')

def build_companies():
    # Preserve native template traits and foreign invitations; remap French focus gates.
    doc=read(GAME/'common/military_industrial_organization/organizations/FRA_organization.txt')
    maps={'FRA_form_the_state_arsenals':'FRA_nww_state_arsenals','FRA_form_the_national_research_center':'FRA_nww_research_council'}
    def remap(node):
        for i,(k,v,o) in enumerate(node):
            if isinstance(v,list): remap(v)
            elif k=='has_completed_focus' and str(v).startswith('FRA_'): node[i]=(k,maps.get(v,'FRA_nww_specifications'),o)
    remap(doc)
    enterprises=[
      ('renault','standard_patterns','Надёжные пехотные машины','Reliable Infantry Tanks','reliability = 0.10','production_efficiency_cap_factor = 0.05'),
      ('hotchkiss','experimental_groups','Манёвренные танковые группы','Mobile Tank Groups','maximum_speed = 0.10',''),
      ('apx','metallurgy','Точная механика вооружения','Precision Armament Engineering','reliability = 0.10',''),
      ('amx','armoured_divisions','Самостоятельные бронетанковые части','Independent Armoured Units','breakthrough = 0.10',''),
      ('somua','mobile_reserve','Моторизованные резервы','Motorised Reserves','reliability = 0.10',''),
      ('panhard','signals_supply','Штабная разведка','Staff Reconnaissance','maximum_speed = 0.10',''),
      ('schneider','artillery_plans','Единые артиллерийские стандарты','Unified Artillery Standards','soft_attack = 0.05','production_efficiency_cap_factor = 0.05'),
      ('mas','standard_patterns','Серийное пехотное вооружение','Standard Infantry Weapons','reliability = 0.10','production_efficiency_cap_factor = 0.05'),
      ('morane_saulnier','interception','Перехватчики метрополии','Metropolitan Interceptors','air_agility = 0.10',''),
      ('bloch','tactical_groups','Тактическое взаимодействие','Tactical Coordination','air_ground_attack = 0.10',''),
      ('amiot','navigation','Дальняя навигация','Long-Range Navigation','air_range = 0.10',''),
      ('levasseur','carrier_group','Палубное оборудование','Deck Equipment','reliability = 0.10',''),
      ('fcm','asw','Серийные океанские эскорты','Standard Ocean Escorts','reliability = 0.10',''),
      ('aeb','fast_squadrons','Быстроходные соединения','Fast Squadrons','naval_speed = 0.10',''),
      ('acl','fire_control','Современное управление огнём','Modern Fire Control','lg_attack = 0.10',''),
      ('acf','bases_fuel','Дальнее патрулирование','Long-Range Patrol','naval_range = 0.10',''),
      ('alsthom','rail_nodes','Государственный железнодорожный заказ','State Railway Orders','reliability = 0.10','production_efficiency_cap_factor = 0.05'),
    ]
    ideas=[]
    for company,gate,ru,en,eq,prod in enterprises:
        name='FRA_'+company+'_organization'
        org=next((v for k,v,o in doc if k==name),None)
        if org is None: raise ValueError('Missing native MIO '+name)
        token='FRA_nww_'+company+'_programme'
        org.append(('add_trait',parse(f'''token = {token} name = {token} icon = GFX_generic_mio_trait_icon_production_capacity special_trait_background = yes
          position = {{ x = 13 y = 0 }} available = {{ FROM = {{ has_completed_focus = FRA_nww_{gate} }} }}
          equipment_bonus = {{ {eq} }} production_bonus = {{ {prod} }}'''),'='))
        label(token,ru,en)
        label('FRA_nww_designer_'+company,company.replace('_',' ').title(),company.replace('_',' ').title(),ru,en)
        # Useful non-AAT concerns; specialising a company costs a normal advisor slot.
        slot='aircraft_manufacturer' if company in ['morane_saulnier','bloch','amiot','levasseur'] else ('naval_manufacturer' if company in ['fcm','aeb','acl','acf'] else ('tank_manufacturer' if company in ['renault','hotchkiss','apx','amx'] else 'industrial_concern'))
        modifier={'aircraft_manufacturer':'air_doctrine_cost_factor = -0.10','naval_manufacturer':'industrial_capacity_dockyard = 0.10','tank_manufacturer':'land_doctrine_cost_factor = -0.10','industrial_concern':'production_factory_efficiency_gain_factor = 0.10'}[slot]
        # Distinct alternatives supplement category benefits.
        extras={'morane_saulnier':'air_intercept_efficiency = 0.05','bloch':'air_cas_efficiency = 0.05','amiot':'air_strategic_bomber_bombing_factor = 0.05','levasseur':'navy_carrier_air_attack_factor = 0.05','renault':'army_org_factor = 0.05','hotchkiss':'army_speed_factor = 0.05','apx':'research_speed_factor = 0.05','amx':'army_armor_attack_factor = 0.05','somua':'army_speed_factor = 0.05','panhard':'recon_factor = 0.10','schneider':'production_factory_max_efficiency_factor = 0.05','mas':'production_factory_efficiency_gain_factor = 0.05','fcm':'convoy_escort_efficiency = 0.05','aeb':'naval_speed_factor = 0.05','acl':'naval_hit_chance = 0.05','acf':'convoy_retreat_speed = 0.10','alsthom':'production_speed_rail_way_factor = 0.10'}
        merged={}
        for m,value,op in parse(modifier+' '+extras[company]):merged[m]=merged.get(m,0)+float(value)
        modifier=' '.join(f'{m} = {value:g}' for m,value in merged.items())
        ideas.append((slot,f'''FRA_nww_designer_{company} = {{ picture = FRA_nww_industry allowed = {{ original_tag = FRA NOT = {{ has_dlc = "Arms Against Tyranny" }} }}
          available = {{ has_completed_focus = FRA_nww_{gate} }} cost = 150 modifier = {{ {modifier} }} }}'''))
        tt='FRA_nww_unlock_'+company+'_tt'
        label(tt,'Развитие '+company.replace('_',' ').title()+': открывает особую черту «'+ru+'» для MIO; без AAT становится доступен профильный концерн.',
              company.replace('_',' ').title()+' development: unlocks the MIO trait '+en+'; without AAT, unlocks a specialised concern.')
        item=next(f for f in FOCUSES if f['key']==gate)
        item['text']=item['text'].replace('completion_reward = {',f'completion_reward = {{ custom_effect_tooltip = {tt}',1)
    write('common/military_industrial_organization/organizations/FRA_organization.txt',dump(doc))
    write('common/ideas/FRA_companies.txt','ideas = {\n'+'\n'.join(slot+' = {\n'+'\n'.join(t for s,t in ideas if s==slot)+'\n}' for slot in sorted({s for s,t in ideas}))+'\n}')

def isolate_native():
    # Collect direct focus definitions only. Event/province IDs are not focus tokens.
    ids=set()
    for name in ['france','free_france','vichy_france']:
        source=one(read(GAME/f'common/national_focus/{name}.txt'),'focus_tree',[])
        ids.update(one(v,'id') for k,v,o in source if k in ('focus','shared_focus') and isinstance(v,list) and one(v,'id'))
        alias='' if name=='france' else f'\nfocus_tree = {{ id = {one(source,"id")} default = no country = {{ factor = 0 }} }}'
        write(f'common/national_focus/{name}.txt','# France content is owned by FRA_focuses.txt. Nonselectable tree aliases retain native literal references.'+alias)
    compat='\n'.join(f'shared_focus = {{ id = {fid} icon = GFX_goal_generic_political_pressure x = 0 y = 0 cost = 5 allow_branch = {{ always = no }} available = {{ always = no }} completion_reward = {{ }} }}' for fid in sorted(ids))
    write('common/national_focus/FRA_compatibility.txt','# Hidden compatibility definitions; no narrative or rewards.\n'+compat)
    for name in ['France','LaR_France']:
        native=read(GAME/f'events/{name}.txt')
        native_events=[(k,one(v,'id')) for k,v,o in native if k in ('country_event','news_event') and isinstance(v,list) and one(v,'id')]
        event_ids=[eid for kind,eid in native_events]
        namespaces=sorted({e.rsplit('.',1)[0] for e in event_ids})
        inert='\n'.join('add_namespace = '+n for n in namespaces)+'\n'
        inert+='\n'.join(f'{kind} = {{ id = {eid} hidden = yes is_triggered_only = yes immediate = {{ }} }}' for kind,eid in native_events)
        write(f'events/{name}.txt','# Native French event IDs retained as inert compatibility callbacks. See FRA_events.txt.\n'+inert)
    native_decisions=read(GAME/'common/decisions/FRA.txt')
    compat_decisions=[]
    for cat,items,o in native_decisions:
        if not isinstance(items,list):continue
        entries=[]
        for did,body,op in items:
            if isinstance(body,list):entries.append(f'{did} = {{ icon = GFX_FRA_nww_republic_idea allowed = {{ always = no }} visible = {{ always = no }} complete_effect = {{ }} }}')
        compat_decisions.append(cat+' = { '+' '.join(entries)+' }')
    write('common/decisions/FRA.txt','# Inert native decision IDs. Active content is owned by FRA_decisions.txt.\n'+'\n'.join(compat_decisions))
    cats=read(GAME/'common/decisions/categories/FRA_decision_categories.txt')
    write('common/decisions/categories/FRA_decision_categories.txt','# Hidden native category aliases; active interface: FRA_categories.txt.\n'+'\n'.join(f'{cat} = {{ icon = GFX_FRA_nww_republic allowed = {{ always = no }} visible = {{ always = no }} }}' for cat,v,o in cats))
    # Advisor availability must refer to working NWW institutions, not hidden legacy focuses.
    chars=read(GAME/'common/characters/FRA.txt')
    maps={'FRA_leftist_rhetoric':'FRA_nww_left_talks','FRA_invite_communist_ministers':'FRA_nww_councils','FRA_right_wing_rhetoric':'FRA_nww_right','FRA_utilize_the_leagues':'FRA_nww_leagues_discipline','FRA_repeal_the_law_of_exile':'FRA_nww_orleanists','FRA_review_foreign_policy':'FRA_nww_foreign_review','FRA_form_the_popular_front':'FRA_nww_front','FRA_form_the_state_arsenals':'FRA_nww_state_arsenals'}
    def fix(node):
        for i,(k,v,o) in enumerate(node):
            if isinstance(v,list): fix(v)
            elif k=='has_completed_focus' and str(v).startswith('FRA_'): node[i]=(k,maps.get(v,'FRA_nww_session'),o)
            elif k=='FRA_right_wing_riot_effect':node[i]=('FRA_political_advisor_reaction',v,o)
        # Character callback tooltips evaluate in character scope; effects belong to its owner.
        for i,(k,v,o) in enumerate(node):
            if k=='on_add' and isinstance(v,list) and any(a=='FRA_political_advisor_reaction' for a,b,c in v):node[i]=(k,[('ROOT',v,'=')],o)
    fix(chars)
    write('common/characters/FRA.txt',dump(chars))
    return sorted(ids)

def history_setup():
    p=ROOT/'history/countries/FRA - France.txt'
    text=p.read_text(encoding='utf-8-sig')
    tokens=[m for m in TOKEN.finditer(text) if not m.group().isspace() and not m.group().startswith('#')]
    depth=0;start=None;spans=[]
    for i,t in enumerate(tokens):
        if t.group()=='{':
            if depth==0:start=tokens[i-2].start()
            depth+=1
        elif t.group()=='}':
            depth-=1
            if depth==0:
                segment=text[start:t.end()]
                if re.search(r'target\s*=\s*(SYR|LEB)',segment):spans.append((start,t.end()))
    for a,b in reversed(spans):text=text[:a]+text[b:]
    # Remove the entire native Syrian/Lebanese subject initializer, including its else branch.
    text=re.sub(r'set_popularities\s*=\s*\{[^}]*\}', 'set_popularities = {\n\tdemocratic = 50\n\tfascism = 10\n\tneutrality = 15\n\tcommunism = 25\n}',text,count=1)
    text=re.sub(r'^\s*(FRA_disjointed_government|FRA_protected_by_the_maginot_line|FRA_full_employment|FRA_political_violence|FRA_inefficient_economy_2)\s*$', '',text,flags=re.M)
    if not re.search(r'^FRA_initialize\s*=',text,re.M): text+='\n# NWW institutions replace the native French crisis; no border changes.\nFRA_initialize = yes\n'
    write('history/countries/FRA - France.txt',text)

def bookmark_setup():
    p=ROOT/'common/bookmarks/nww_1936.txt'
    text=p.read_text(encoding='utf-8-sig')
    replacements={'FRA_victors_of_wwi':'FRA_nww_preview_state','FRA_disjointed_government':'FRA_nww_preview_economy','FRA_protected_by_the_maginot_line':'FRA_nww_preview_army','FRA_form_the_popular_front':'FRA_nww_front','FRA_revive_the_national_bloc':'FRA_nww_right','FRA_france_leads':'FRA_nww_republic'}
    for old,new in replacements.items():text=re.sub(r'\b'+old+r'\b',new,text)
    write('common/bookmarks/nww_1936.txt',text)
    ru='Франция избежала мировой войны и сохранила людей, предприятия и научные школы. Но Третья республика погрязла в кабинетных кризисах, депрессия расколола общество, а заморские территории требуют нового договора. Реформировать парламент, вернуть корону, передать власть трудовым организациям или доверить страну военному кабинету — выбор определит, какую Францию встретит следующий европейский конфликт.'
    en='France avoided a world war and preserved its people, industry and scientific schools. Yet the Third Republic is mired in cabinet crises, the depression has divided society and overseas territories demand a new settlement. Reform parliament, restore the crown, empower labour organisations or entrust the country to a military cabinet: the choice determines which France will face the next European conflict.'
    # Keep this pre-existing shared key in its original owner; do not create duplicate localisation.
    for lang,desc in [('russian',ru),('english',en)]:
        path=ROOT/f'localisation/mod_countries_l_{lang}.yml'
        content=path.read_text(encoding='utf-8-sig')
        content=re.sub(r'^ NWW_FRA_DESC:.*$',lambda _:f' NWW_FRA_DESC: "{desc}"',content,flags=re.M)
        write(str(path.relative_to(ROOT)),content,True)

def main():
    build_focuses();build_spirits();build_political_effects();build_mandate_decisions()
    build_overseas();build_projects();build_events();build_diplomacy();build_gui();build_ai();build_companies()
    ids=isolate_native()
    tree='''focus_tree = { id = french_focus default = no country = { factor = 0 modifier = { add = 100 tag = FRA } }
      initial_show_position = { x = 0 y = 0 } continuous_focus_position = { x = 100 y = 2200 }
    '''+'\n'.join('shared_focus = '+fid for fid in ids)+'\n'+'\n'.join(f['text'] for f in FOCUSES)+'\n}'
    write('common/national_focus/FRA_focuses.txt',dump(parse(tree)))
    write('common/scripted_effects/FRA_effects.txt',dump(parse('\n'.join(EFFECTS))))
    write('common/decisions/FRA_decisions.txt',dump(parse('\n'.join(k+' = {\n'+'\n'.join(v)+'\n}' for k,v in DECISIONS.items()))))
    write('events/FRA_events.txt',dump(parse('add_namespace = nww_fra\n'+'\n'.join(EVENTS))))
    write('common/on_actions/FRA_on_actions.txt','''on_actions = {
      on_startup = { effect = { FRA = { if = { limit = { exists = yes } FRA_restore_tree = yes FRA_initialize = yes } } } }
      on_daily_FRA = { effect = { FRA_restore_tree = yes if = { limit = { has_focus_tree = french_focus } FRA_daily = yes } } }
    }''')
    for k,ru,en in [
      ('FRA_nww_research_program','Французская исследовательская программа','French Research Programme'),
      ('FRA_fort_projects_tt','Открывает оплачиваемые проекты укреплений в решениях.','Unlocks paid fortification projects in decisions.'),
      ('FRA_colonial_projects_tt','Открывает региональные инвестиции: 70 дней, 50 политвласти и 3 гражданских завода на время работ.','Unlocks regional investment: 70 days, 50 political power and 3 civilian factories while work proceeds.'),
      ('FRA_treaty_consent_tt','Открывает переговоры с независимыми партнёрами; каждый получатель вправе отказаться.','Opens talks with independent partners; each recipient may refuse.'),
    ]: label(k,ru,en)
    for lang,index in [('russian',0),('english',1)]:
        def esc(s): return s.replace('\\','\\\\').replace('"','\\"').replace('\n','\\n')
        write(f'localisation/{lang}/FRA_nww_l_{lang}.yml','l_'+lang+':\n'+'\n'.join(f' {k}:0 "{esc(v[index])}"' for k,v in LOC.items()),True)
    manifest={'focus_count':len(FOCUSES),'focuses':[{k:v for k,v in f.items() if k!='text'} for f in FOCUSES], 'regions':REGIONS,'compatibility_ids':ids}
    write('docs/FRA_content.json',json.dumps(manifest,ensure_ascii=False,indent=2))
    history_setup();bookmark_setup()
    print(f'France built: {len(FOCUSES)} focuses, {sum(len(v) for v in DECISIONS.values())} decisions, {len(EVENTS)} events, {len(ids)} direct compatibility focus IDs.')

if __name__=='__main__': main()




