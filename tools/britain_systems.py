"""Emit Britain's negotiated imperial settlement and persistent country systems."""
from collections import defaultdict
from hoi4_script import read, one, quoted

P='ENG_nww_'
PARTNERS=[('CAN','Канада','Canada'),('AST','Австралия','Australia'),
          ('SAF','Южная Африка','South Africa'),('NZL','Новая Зеландия','New Zealand'),
          ('RAJ','Индия','India')]


def emit_systems(write,loc,foci,game):
    effects=[]
    decisions=defaultdict(list)
    events=['# Owner: ENG, including all bilateral offers below.','add_namespace = nww_eng']
    def effect(key,body):
        effects.append(P+key+' = {\n'+body+'\n}')
    def event(num,ru,en,rd,ed,options,immediate='',hidden=False):
        eid='nww_eng.'+str(num)
        loc(eid+'.t',ru,en); loc(eid+'.d',rd,ed)
        head=f'country_event = {{ id = {eid} is_triggered_only = yes '
        head+=('hidden = yes' if hidden else f'title = {eid}.t desc = {eid}.d picture = GFX_report_event_generic_conference')
        if immediate: head+='\nimmediate = { '+immediate+' }'
        for i,opt in enumerate(options):
            # (Russian label, English label, effects, trigger, AI weight)
            r,e,body,trigger,ai=opt
            name=eid+'.'+chr(97+i);loc(name,r,e)
            head+='\noption = { name = '+name+' '
            if trigger: head+='trigger = { '+trigger+' } '
            head+='ai_chance = { factor = '+str(ai)+' } '+body+' }'
        events.append(head+'\n}')
    def decision(cat,key,ru,en,rd,ed,body):
        loc(P+key,ru,en);loc(P+key+'_desc',rd,ed)
        decisions[cat].append(P+key+' = { '+body+' }')
    def ck(var,value,compare='greater_than_or_equals'):
        return f'check_variable = {{ var = {P+var} value = {value} compare = {compare} }}'
    def F(key): return 'has_completed_focus = '+P+key
    peace='has_capitulated = no has_war = no has_civil_war = no'
    open_country='exists = yes has_capitulated = no NOT = { has_war_with = ENG } OR = { is_subject = no is_subject_of = ENG }'

    # Rebuild derived values from actual completed reforms. Never repeat rewards.
    defaults={
        'state':{'political_power_factor':-0.20,'stability_factor':-0.05},
        'economy':{'production_speed_buildings_factor':-0.10,'production_factory_efficiency_gain_factor':-0.05,
                   'industrial_capacity_factory':0,'production_factory_max_efficiency_factor':0,'energy_gain_factor':0},
        'army':{'army_org_factor':0.05,'training_time_army_factor':0.10,'planning_speed':0,
                'supply_consumption_factor':0,'army_org_regain':0,'army_speed_factor':0,'max_planning':0,'army_core_defence_factor':0},
        'air':{'air_mission_efficiency':0,'air_intercept_efficiency':0,'air_strategic_bomber_bombing_factor':0,'air_cas_efficiency':0},
        'navy':{'industrial_capacity_dockyard':0,'convoy_escort_efficiency':0,'naval_detection':0,'navy_capital_ship_attack_factor':0},
        'science':{'research_speed_factor':0},
    }
    icons={group:P+group for group in defaults}
    # Country artwork is registered in interface/ENG_icons.gfx.
    from pathlib import Path
    import re
    dynamic=[];rebuild=[]
    names={
        'state':('Корона и имперское бремя','The Crown and the Imperial Burden'),
        'economy':('Промышленность метрополии','Metropolitan Industry'),
        'army':('Профессионалы малых войн','Professionals of Small Wars'),
        'air':('Королевские военно-воздушные силы','Royal Air Force'),
        'navy':('Королевский военно-морской флот','Royal Navy'),
        'science':('Британская научная служба','British Scientific Service'),
    }
    for group,params in defaults.items():
        name=P+group
        loc(name,*names[group])
        loc(name+'_desc','Параметры этого постоянного духа меняются по мере завершения реформ соответствующей ветки.',
            'This persistent spirit changes as reforms in its branch are completed.')
        dynamic.append(name+' = { enable = { always = yes } icon = GFX_idea_'+icons[group]+' '+
                       ' '.join(k+' = '+P+group+'_'+k for k in params)+' }')
        rebuild.extend(f'set_variable = {{ {P+group}_{key} = {value:.2f} }}' for key,value in params.items())
        rebuild.append(f'if = {{ limit = {{ NOT = {{ has_dynamic_modifier = {{ modifier = {name} }} }} }} add_dynamic_modifier = {{ modifier = {name} }} }}')
    for f in foci:
        for key,amount in f['mods'].items():
            group,key=key.split(':')
            assert key in defaults[group],key
            rebuild.append(f'if = {{ limit = {{ {F(f["key"])} }} add_to_variable = {{ {P+group}_{key} = {amount:.2f} }} }}')
    rebuild.append('if = { limit = { has_country_flag = ENG_nww_social_settlement } add_to_variable = { ENG_nww_state_stability_factor = 0.05 } }')
    effect('rebuild_spirits','\n'.join(rebuild))
    write('common/dynamic_modifiers/ENG_modifiers.txt','\n'.join(dynamic))
    # Temporary burdens stay separate from persistent branch spirits.
    ideas=[]
    for key,ru,en,mod,desc_ru,desc_en in [
        ('markets','Заморские рынки','Overseas Markets','industrial_capacity_factory = 0.05','Имперские заказы поддерживают британское производство. После пересмотра зависимых отношений их заменяют согласованные торговые договоры.','Imperial orders sustain British production. Negotiated trade must replace them as dependent relationships change.'),
        ('finance','Мировой клиринговый центр','World Clearing Centre','trade_opinion_factor = 0.10','Лондонские банки и страховые общества связывают мировые рынки.','London banks and insurers connect world markets.'),
        ('project_cost','Имперская проектная смета','Imperial Project Commitment','civilian_factory_use = 2','Две гражданские фабрики выделены на действующий проект до его окончания или отмены.','Two civilian factories are committed until the current project finishes or is cancelled.'),
        ('strikes','Промышленные забастовки','Industrial Strikes','industrial_capacity_factory = -0.10','Принуждение обострило трудовой конфликт. Арбитраж и соглашение о труде способны устранить его причины.','Coercion has deepened the labour dispute. Arbitration and a labour settlement can address its causes.'),
        ('ulster_garrison','Чрезвычайный гарнизон Ольстера','Ulster Emergency Garrison','political_power_factor = -0.10','Содержание чрезвычайной администрации требует постоянных расходов.','Emergency administration imposes continuing costs.'),
        ('retooling','Перестройка производственных линий','Retooling Production Lines','industrial_capacity_factory = -0.05','Новые массовые контракты требуют временной остановки части линий.','Mass contracts require some lines to stop temporarily.'),
        ('sea_delay','Задержки имперских проектов','Imperial Project Delays','political_power_factor = -0.05','Потеря доступа к морским базам осложняет исполнение договоров. Потери конвоев и снабжения рассчитываются самой игрой.','Loss of access to naval bases complicates treaty commitments. Convoy and supply losses remain governed by the game.'),
        ('trade_partner','Договор с британским рынком','British Market Compact','production_factory_efficiency_gain_factor = 0.05','Участник ратифицировал взаимные закупки и общие стандарты.','This participant ratified reciprocal procurement and common standards.'),
        ('federal_partner','Федеральные оборонные соглашения','Federal Defence Agreements','research_speed_factor = 0.05','Совместные институты опираются на ратифицированный договор. Участник сохраняет свою территорию и армию.','Joint institutions rest on a ratified treaty. The participant retains its territory and army.'),
        ('pacifism','Мандат мирных преобразований','Mandate for Peaceful Reform','war_support_factor = -0.10','Общество поддержало социальные реформы и ограничение военных обязательств. Оборонный мандат требует новой кампании.','The public endorsed social reform and limited commitments. A defence mandate requires a new campaign.'),
    ]:
        loc(P+key,ru,en);loc(P+key+'_desc',desc_ru,desc_en)
        ideas.append(f'{P+key} = {{ picture = {P+key} allowed = {{ always = yes }} allowed_civil_war = {{ always = no }} removal_cost = -1 modifier = {{ {mod} }} }}')
    write('common/ideas/ENG_ideas.txt','ideas = { country = {\n'+'\n'.join(ideas)+'\n} }')

    # Construction is always on an owned and controlled metropolitan core.
    for kind,building in [('civilian','industrial_complex'),('military','arms_factory'),('dockyard','dockyard'),('infrastructure','infrastructure'),('airbase','air_base')]:
        limit='is_core_of = ENG is_controlled_by = ENG'
        if kind=='dockyard': limit+=' is_coastal = yes'
        if kind in ('infrastructure','airbase'):
            limit+=f' {building} < {4 if kind=="infrastructure" else 9}'
        for amount in range(1,6):
            effect('build_'+kind+'_'+str(amount),f'random_owned_controlled_state = {{ limit = {{ {limit} }} '+
                   (f'add_extra_state_shared_building_slots = {amount} ' if kind in ('civilian','military','dockyard') else '')+
                   f'add_building_construction = {{ type = {building} level = {amount} instant_build = yes }} }}')
    for key,resource,amount in [('coal','coal',6),('steel','steel',4)]:
        effect(key+'_project',f'random_owned_controlled_state = {{ limit = {{ is_core_of = ENG }} add_resource = {{ type = {resource} amount = {amount} }} }}')
    effect('radar_project','random_owned_controlled_state = { limit = { is_core_of = ENG radar_station < 5 } add_building_construction = { type = radar_station level = 2 instant_build = yes } }')
    effect('research_facility','random_owned_controlled_state = { limit = { is_core_of = ENG air_facility < 1 } add_building_construction = { type = air_facility level = 1 instant_build = yes } }')
    for amount in [-15,-10,-5,5,10]:
        tip=P+'trust_change_'+str(amount).replace('-','minus')+'_tt'
        loc(tip,f'Доверие Канады, Австралии, Южной Африки, Новой Зеландии и Индии к Лондону: {amount:+d} пунктов (в пределах 0–100).',
            f'Trust in London in Canada, Australia, South Africa, New Zealand and India: {amount:+d} points (bounded to 0–100).')
        effect('trust_all_'+str(amount).replace('-','minus'),'custom_effect_tooltip = '+tip+'\n'+'\n'.join(f'add_to_variable = {{ {P}trust_{tag} = {amount} }} clamp_variable = {{ var = {P}trust_{tag} min = 0 max = 100 }}' for tag,_,_ in PARTNERS))

    # Country initialization: one-time state only, then idempotent spirit repair.
    init=['if = { limit = { NOT = { has_country_flag = ENG_nww_initialized } }',
          'set_country_flag = ENG_nww_initialized',
          'set_variable = { ENG_nww_labour_mandate = 10 } set_variable = { ENG_nww_irish_pressure = 30 }',
          'add_ideas = { ENG_nww_markets ENG_nww_finance }',
          'remove_ideas = stiff_upper_lip',
          'remove_from_tech_sharing_group = commonwealth_research',
          'clr_country_flag = ENG_nww_project_busy']
    for tag,_,_ in PARTNERS:
        init.append(f'set_variable = {{ {P}trust_{tag} = {45 if tag in ("SAF","RAJ") else 55} }}')
    init.append('ENG_nww_choose_ai_plan = yes } ENG_nww_rebuild_spirits = yes ENG_nww_recount_partners = yes ENG_nww_update_routes = yes')
    effect('initialize','\n'.join(init))
    plans=[('DEMOCRATIC_HISTORICAL','continuity'),('DEMOCRATIC_ALTERNATE','federal'),('FASCIST','fascist'),('NEUTRALITY','directory'),('COMMUNIST','republic'),('SOCIALIST','social'),('ISOLATION','island')]
    ai=[]
    for i,(option,plan) in enumerate(plans):
        ai.append(('if' if i==0 else 'else_if')+f' = {{ limit = {{ has_game_rule = {{ rule = ENG_ai_behavior option = {option} }} }} set_country_flag = ENG_nww_plan_{plan} }}')
    ai.append('else_if = { limit = { is_historical_focus_on = yes has_game_rule = { rule = ENG_ai_behavior option = DEFAULT } } set_country_flag = ENG_nww_plan_continuity }')
    ai.append('else = { random_list = { 30 = { set_country_flag = ENG_nww_plan_continuity } 25 = { set_country_flag = ENG_nww_plan_federal } 15 = { set_country_flag = ENG_nww_plan_fascist } 10 = { set_country_flag = ENG_nww_plan_directory } 15 = { set_country_flag = ENG_nww_plan_social } 5 = { set_country_flag = ENG_nww_plan_island } } }')
    ai.append('if = { limit = { OR = { has_country_flag = ENG_nww_plan_fascist has_country_flag = ENG_nww_plan_directory } } set_country_flag = ENG_nww_plan_right }')
    ai.append('if = { limit = { OR = { has_country_flag = ENG_nww_plan_social has_country_flag = ENG_nww_plan_republic } } set_country_flag = ENG_nww_plan_labour }')
    effect('choose_ai_plan','\n'.join(ai))
    # Replace only ENG's existing entry, preserving the shared registry and all
    # other countries' rules. Every NWW route works without Man the Guns.
    rules_path=Path(__file__).resolve().parents[1]/'common/game_rules/00_game_rules.txt'
    rules_text=rules_path.read_text(encoding='utf-8-sig')
    start=rules_text.index('ENG_ai_behavior = {');brace=rules_text.index('{',start)
    depth=1;end=brace+1
    while depth:
        depth+=(rules_text[end]=='{')-(rules_text[end]=='}');end+=1
    rules=['ENG_ai_behavior = { name = ENG_AI_BEHAVIOR group = RULE_GROUP_AI_BEHAVIOR',
           'default = { name = DEFAULT text = RULE_OPTION_DEFAULT desc = RULE_OPTION_DEFAULT_AI_DESC }']
    for option,key,ru,en in [
        ('DEMOCRATIC_HISTORICAL','continuity','Обновлённое Содружество','A Renewed Commonwealth'),
        ('DEMOCRATIC_ALTERNATE','federal','Имперская федерация','Imperial Federation'),
        ('FASCIST','fascist','Британский союз фашистов','British Union of Fascists'),
        ('NEUTRALITY','directory','Консервативная директория','Conservative Directorate'),
        ('COMMUNIST','republic','Социалистическая республика','Socialist Republic'),
        ('SOCIALIST','social','Парламентский социализм','Parliamentary Socialism'),
        ('ISOLATION','island','Островной изоляционизм','Island Isolationism'),
        ('RANDOM','random','Случайный курс NWW','Random NWW Programme'),
    ]:
        name=P+'rule_'+key;loc(name,ru,en)
        loc(name+'_desc','Британский ИИ выберет этот политический курс. Мандаты, подготовка и право партнёров на отказ сохраняются. Явное правило имеет приоритет над историческим режимом.',
            'British AI selects this programme. Mandates, preparation and partner refusal remain in force. An explicit rule takes precedence over historical mode.')
        rules.append(f'option = {{ name = {option} text = {name} desc = {name}_desc }}')
    rules.append('}')
    write('common/game_rules/00_game_rules.txt',rules_text[:start]+'\n'.join(rules)+rules_text[end:])
    recount=['set_variable = { ENG_nww_federal_count = 0 } set_variable = { ENG_nww_compact_count = 0 }']
    recount.extend(f'if = {{ limit = {{ {tag} = {{ {open_country} }} has_country_flag = {P}{kind}_{tag} }} add_to_variable = {{ {P}{kind}_count = 1 }} }}' for tag,_,_ in PARTNERS for kind in ('federal','compact'))
    recount.append('if = { limit = { OR = { has_country_flag = ENG_nww_social_settlement has_country_flag = ENG_nww_island_settlement } } remove_ideas = ENG_nww_markets }')
    recount.append('if = { limit = { has_country_flag = ENG_nww_island_settlement } remove_ideas = ENG_nww_finance }')
    recount.append('if = { limit = { check_variable = { var = ENG_nww_compact_count value = 1 compare = greater_than_or_equals } } if = { limit = { NOT = { has_idea = ENG_nww_trade_partner } } add_ideas = ENG_nww_trade_partner } } else = { remove_ideas = ENG_nww_trade_partner }')
    effect('recount_partners','\n'.join(recount))
    effect('release_project','clr_country_flag = ENG_nww_project_busy remove_ideas = ENG_nww_project_cost')

    for key,party,ru,en in [('fascist','fascism','Освальд Мосли','Oswald Mosley'),('directory','neutrality','Совет национальной обороны','Council of National Defence'),('socialist','communism','Социалистический исполнительный совет','Socialist Executive Council')]:
        body=''
        if key=='fascist': body+='promote_character = ENG_oswald_mosley '
        elif key=='directory': body+='create_country_leader = { name = ENG_nww_directory_leader ideology = despotism expire = "1965.1.1" } '
        else: body+='promote_character = ENG_harry_pollitt set_country_flag = ENG_nww_social_settlement remove_ideas = george_v remove_ideas = ENG_king_edward remove_ideas = ENG_george_vi '
        body+=f'set_politics = {{ ruling_party = {party} elections_allowed = no }} add_stability = -0.10 ENG_nww_trust_all = {{ AMOUNT = -15 }} '
        if key!='socialist': body+='add_timed_idea = { idea = ENG_nww_strikes days = 365 } '
        body+='if = { limit = { has_stability < 0.40 has_civil_war = no } country_event = { id = nww_eng.4 days = 1 } }'
        effect(key+'_transition',body)
    loc('ENG_nww_directory_leader','Совет национальной обороны','Council of National Defence')
    effect('labour_transition','recruit_character = ENG_nww_attlee promote_character = ENG_nww_attlee set_politics = { ruling_party = democratic elections_allowed = yes election_frequency = 48 } add_ideas = ENG_nww_pacifism')
    effect('offer_canadian_project','set_country_flag = ENG_nww_canada_project_unlocked')
    effect('offer_indian_project','set_country_flag = ENG_nww_india_project_unlocked')
    # Attlee uses an existing large portrait, separate from his advisor card.
    loc('ENG_nww_attlee','Клемент Эттли','Clement Attlee')
    write('common/characters/ENG_characters.txt','characters = { ENG_nww_attlee = { name = ENG_nww_attlee portraits = { civilian = { large = "gfx/leaders/Europe/Portrait_Europe_Generic_1.dds" } } country_leader = { ideology = socialism traits = { } expire = "1965.1.1" } } }')

    # Three decision categories; read-only dashboards are emitted by britain_gui.
    loc(P+'imperial_category','Имперский договор','The Imperial Treaty')
    loc(P+'imperial_category_desc',
        'Доверие к Лондону: Канада [?ENG_nww_trust_CAN|0], Австралия [?ENG_nww_trust_AST|0], Южная Африка [?ENG_nww_trust_SAF|0], Новая Зеландия [?ENG_nww_trust_NZL|0], Индия [?ENG_nww_trust_RAJ|0].\\nТорговых договоров: [?ENG_nww_compact_count|0]. Ратификаций федерации: [?ENG_nww_federal_count|0].\\nПереговоры проводятся последовательно. Доверие облегчает согласие, но не отменяет права отказа.',
        'Trust in London: Canada [?ENG_nww_trust_CAN|0], Australia [?ENG_nww_trust_AST|0], South Africa [?ENG_nww_trust_SAF|0], New Zealand [?ENG_nww_trust_NZL|0], India [?ENG_nww_trust_RAJ|0].\\nTrade compacts: [?ENG_nww_compact_count|0]. Federal ratifications: [?ENG_nww_federal_count|0].\\nNegotiations are serialised. Trust helps secure consent; it never removes the right to refuse.')
    loc(P+'cabinet_category','Вестминстер: мандат и обязательства','Westminster: Mandates and Commitments')
    loc(P+'cabinet_category_desc','Поддержка лейбористской программы: [?ENG_nww_labour_mandate|0]/100.\\nНапряжённость в Ольстере: [?ENG_nww_irish_pressure|0]/100. Рост напряжённости приводит к требованиям и ограниченному сроку урегулирования.',
        'Labour programme mandate: [?ENG_nww_labour_mandate|0]/100.\\nUlster tension: [?ENG_nww_irish_pressure|0]/100. Rising tension brings demands and a timed settlement crisis.')
    loc(P+'routes_category','Морские артерии Империи','Imperial Sea Arteries')
    loc(P+'routes_category_desc','Доступных направлений: [?ENG_nww_open_routes|0]/4.\\nСеверная Атлантика: [?ENG_nww_route_atlantic|0] • Средиземноморье: [?ENG_nww_route_suez|0] • маршрут вокруг Африки: [?ENG_nww_route_cape|0] • Индийский океан: [?ENG_nww_route_indian|0].\\n1 — есть доступ к ключевой базе и транспортный резерв; 0 — направление нарушено. При недоступности двух направлений новые заморские проекты приостанавливаются. Боевые потери транспорта обрабатывает игра.',
        'Open routes: [?ENG_nww_open_routes|0]/4.\\nNorth Atlantic: [?ENG_nww_route_atlantic|0] • Mediterranean: [?ENG_nww_route_suez|0] • Cape route: [?ENG_nww_route_cape|0] • Indian Ocean: [?ENG_nww_route_indian|0].\\n1 means key base access and transport reserves; 0 means disruption. Losing two routes suspends new overseas projects. Transport combat losses remain governed by the game.')
    cats=[]
    for cat in ('imperial','cabinet','routes'):
        cats.append(f'{P+cat}_category = {{ icon = GFX_decision_category_{P+cat} scripted_gui = {P+cat}_ui visible_when_empty = yes allowed = {{ original_tag = ENG }} visible = {{ tag = ENG has_focus_tree = ENG_nww_focus }} }}')
    write('common/decisions/categories/ENG_categories.txt','\n'.join(cats))

    decision('imperial','hold_conference','Открыть сессию Имперской конференции','Open an Imperial Conference Session',
        '50 политической власти; 90 дней. Доступ к торговым переговорам. Подписанные договоры сохраняются после окончания сессии.',
        '50 political power; 90 days. Opens trade negotiations. Signed compacts survive the end of the session.',
        'visible = { has_country_flag = ENG_nww_conferences_unlocked } available = { '+peace+' NOT = { has_country_flag = ENG_nww_conference_active } } cost = 50 days_remove = 90 days_re_enable = 90 complete_effect = { set_country_flag = ENG_nww_conference_active } remove_effect = { clr_country_flag = ENG_nww_conference_active } cancel_trigger = { OR = { has_capitulated = yes has_civil_war = yes } } cancel_effect = { clr_country_flag = ENG_nww_conference_active add_political_power = 50 } ai_will_do = { factor = 4 }')
    # Negotiations use a single paid project slot; recipients get a genuine choice.
    for index,(tag,ru,en) in enumerate(PARTNERS):
        modes=[('compact',14,25),('federal',35,50),('independence',35,50),('investment',35,50)]
        if tag=='RAJ': modes.append(('government',35,50))
        for mode,days,cost in modes:
            key=f'{mode}_{tag}';req=P+'request_'+key;done=P+key
            num=100+index*10+['compact','federal','independence','investment','government'].index(mode)
            vis={
                'compact':'has_country_flag = ENG_nww_conferences_unlocked',
                'federal':'has_country_flag = ENG_nww_ratification_unlocked',
                'independence':'has_country_flag = ENG_nww_decolonisation_unlocked',
                'investment':('has_country_flag = ENG_nww_canada_project_unlocked' if tag=='CAN' else 'has_country_flag = ENG_nww_india_project_unlocked' if tag=='RAJ' else 'has_country_flag = ENG_nww_investment_unlocked'),
                'government':'OR = { has_completed_focus = ENG_nww_representation has_completed_focus = ENG_nww_colonial_review has_completed_focus = ENG_nww_local_parliaments }',
            }[mode]
            gate=(f'has_country_flag = ENG_nww_conference_active {ck("trust_"+tag,40)}' if mode=='compact' else
                  f'has_country_flag = ENG_nww_compact_{tag} {ck("trust_"+tag,65)} date > 1938.1.1' if mode=='federal' else
                  f'{tag} = {{ is_subject_of = ENG }}' if mode=='independence' else
                  f'{tag} = {{ is_subject_of = ENG }} {ck("trust_"+tag,45)}' if mode=='government' else '')
            if mode=='federal' and tag=='RAJ': gate+=' has_country_flag = ENG_nww_indian_government'
            # Projects may be suspended at sea but a settled partner can still negotiate freedom.
            sea_gate=ck('open_routes',3) if mode=='investment' else ''
            available=f'{peace} num_of_available_civilian_factories > 1 {tag} = {{ {open_country} }} NOT = {{ has_country_flag = ENG_nww_project_busy }} NOT = {{ has_country_flag = {req} }} {gate} {sea_gate}'
            cancel=f'OR = {{ has_war = yes has_capitulated = yes has_civil_war = yes {tag} = {{ OR = {{ exists = no has_capitulated = yes has_war_with = ENG AND = {{ is_subject = yes NOT = {{ is_subject_of = ENG }} }} }} }} }}'
            if mode=='compact': cancel=f'OR = {{ NOT = {{ has_country_flag = ENG_nww_conference_active }} {cancel} }}'
            label={
                'compact':('Торговый договор','Trade compact'),
                'federal':('Ратификация федерации','Federal ratification'),
                'independence':('Передача суверенитета','Transfer of sovereignty'),
                'investment':('Инфраструктурный кредит','Infrastructure credit'),
                'government':('Ответственное индийское правительство','Responsible Indian Government'),
            }[mode]
            decision('imperial',key,label[0]+': '+ru,label[1]+': '+en,
                f'{cost} политической власти, две гражданские фабрики на {days} дней. Получатель может согласиться или отказаться. При отмене до отправки предложения стоимость возвращается.',
                f'{cost} political power and two civilian factories for {days} days. The recipient may accept or refuse. Cancellation before dispatch refunds the cost.',
                f'visible = {{ {vis} {tag} = {{ exists = yes }} NOT = {{ has_country_flag = {done} }} }} available = {{ {available} }} cost = {cost} days_remove = {days} days_re_enable = 90 '
                f'complete_effect = {{ set_country_flag = ENG_nww_project_busy add_ideas = ENG_nww_project_cost }} '
                f'cancel_trigger = {{ {cancel} }} cancel_effect = {{ ENG_nww_release_project = yes add_political_power = {cost} }} '
                f'remove_effect = {{ ENG_nww_release_project = yes set_country_flag = {{ flag = {req} days = 90 }} {tag} = {{ country_event = {{ id = nww_eng.{num} days = 1 }} }} }} ai_will_do = {{ factor = {4 if mode=="compact" else 2} }}')
            valid=f'ENG = {{ exists = yes has_focus_tree = ENG_nww_focus has_country_flag = {req} NOT = {{ has_war_with = ROOT }} has_capitulated = no }} {open_country}'
            accept=f'ENG = {{ clr_country_flag = {req} set_country_flag = {done} add_to_variable = {{ ENG_nww_trust_{tag} = 10 }} }} '
            if mode=='compact':
                accept+='add_ideas = ENG_nww_trade_partner '
                accept+='if = { limit = { ENG = { has_country_flag = ENG_nww_science_unlocked } } add_to_tech_sharing_group = ENG_nww_research } '
            elif mode=='federal':
                accept+='add_ideas = ENG_nww_federal_partner add_to_tech_sharing_group = ENG_nww_research '
            elif mode=='independence':
                accept+=f'if = {{ limit = {{ is_subject_of = ENG }} ENG = {{ set_autonomy = {{ target = {tag} autonomy_state = autonomy_free end_wars = no end_civil_wars = no }} }} }} '
            elif mode=='investment':
                accept+='random_owned_controlled_state = { limit = { is_core_of = ROOT } add_extra_state_shared_building_slots = 1 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } } '
            if mode=='government':
                accept+='ENG = { set_country_flag = ENG_nww_indian_government if = { limit = { OR = { has_dlc = "Together for Victory" has_dlc = "Man the Guns" } RAJ = { is_subject_of = ENG } } set_autonomy = { target = RAJ autonomy_state = autonomy_dominion end_wars = no end_civil_wars = no } } } '
            accept+='ENG = { ENG_nww_clamp = yes ENG_nww_recount_partners = yes country_event = { id = nww_eng.10 days = 1 } }'
            refusal=f'ENG = {{ clr_country_flag = {req} add_to_variable = {{ ENG_nww_trust_{tag} = -5 }} ENG_nww_clamp = yes country_event = {{ id = nww_eng.11 days = 1 }} }}'
            event(num,'Предложение из Лондона: '+label[0], 'An Offer from London: '+label[1],
                  'Британский кабинет завершил подготовку предложения. Договор требует нашей ратификации; отказ не даёт Лондону права менять наше правительство, границы или международный статус. Мы можем принять согласованные обязательства либо оставить прежние отношения.',
                  'The British cabinet has prepared its proposal. It requires our ratification; refusal gives London no right to change our government, borders or international status. We may accept the agreed obligations or keep existing relations.',
                  [('Ратифицировать предложение','Ratify the proposal',accept,valid,80 if mode!='federal' else 65),
                   ('Сохранить прежние отношения','Keep existing relations',refusal,'',20 if mode!='federal' else 35)])

    # Political campaigns provide every transition with an attainable mandate.
    for key,ru,en,gate,body,condition in [
        ('labour_campaign','Кампания за лейбористскую программу','Campaign for Labour Reform',F('labour'),'add_to_variable = { ENG_nww_labour_mandate = 10 }',ck('labour_mandate',40,'less_than')),
        ('fascist_campaign','Националистические собрания','Nationalist Meetings','has_country_flag = ENG_nww_right_campaign','add_popularity = { ideology = fascism popularity = 0.10 }','fascism < 0.40'),
        ('directory_campaign','Союз сторонников порядка','Alliance for Order','has_country_flag = ENG_nww_right_campaign','add_popularity = { ideology = neutrality popularity = 0.10 }','neutrality < 0.40'),
        ('socialist_campaign','Социалистические комитеты','Socialist Committees',F('colonial_review'),'add_popularity = { ideology = communism popularity = 0.10 }','communism < 0.40'),
    ]:
        plan={'labour_campaign':'labour','fascist_campaign':'fascist','directory_campaign':'directory','socialist_campaign':'republic'}[key]
        decision('cabinet',key,ru,en,'35 политической власти; 35 дней подготовки. Даёт 10 пунктов программного мандата либо 10 процентных пунктов поддержки партии.',
                 '35 political power; 35 days. Adds 10 programme mandate or 10 percentage points of party support.',
                 f'visible = {{ {gate} {condition} }} available = {{ has_capitulated = no NOT = {{ has_country_flag = ENG_nww_campaign_busy }} }} cost = 35 days_remove = 35 days_re_enable = 5 '
                 f'complete_effect = {{ set_country_flag = ENG_nww_campaign_busy }} remove_effect = {{ clr_country_flag = ENG_nww_campaign_busy {body} ENG_nww_clamp = yes }} cancel_trigger = {{ has_capitulated = yes }} cancel_effect = {{ clr_country_flag = ENG_nww_campaign_busy add_political_power = 35 }} '
                 f'ai_will_do = {{ factor = 5 modifier = {{ factor = 0 NOT = {{ has_country_flag = ENG_nww_plan_{plan} }} }} }}')
    decision('cabinet','defence_mandate','Защитить социальные преобразования','Defend Social Reform',
             'При внешней угрозе провести 35-дневную кампанию за оборонный мандат. Снимает пацифистское ограничение.',
             'A 35-day campaign for a defence mandate under external threat removes the pacifist constraint.',
             'visible = { has_idea = ENG_nww_pacifism } available = { OR = { has_war = yes threat > 0.40 } has_capitulated = no } cost = 50 days_remove = 35 remove_effect = { remove_ideas = ENG_nww_pacifism add_war_support = 0.10 } ai_will_do = { factor = 4 }')

    # Irish settlement: refusal unlocks a paid retry, not automatic war.
    for key,ru,en,body,cost in [
        ('irish_mediation','Посредничество между общинами','Intercommunal Mediation','add_to_variable = { ENG_nww_irish_pressure = -15 }',35),
        ('irish_retry','Вернуться к переговорам с Дублином','Return to Talks with Dublin','country_event = { id = nww_eng.20 days = 1 }',50),
    ]:
        gate=('has_country_flag = ENG_nww_irish_talks_ready NOT = { has_country_flag = ENG_nww_irish_agreement }' if key=='irish_retry' else '')
        decision('cabinet',key,ru,en,'Переговоры требуют 35 дней. При потере Северной Ирландии незавершённая процедура отменяется с возвратом стоимости.',
                 'Negotiations take 35 days. Losing Northern Ireland cancels an unfinished procedure and refunds its cost.',
                 f'visible = {{ has_country_flag = ENG_nww_irish_unlocked NOT = {{ has_country_flag = ENG_nww_irish_final }} }} available = {{ {peace} 119 = {{ is_owned_and_controlled_by = ENG }} NOT = {{ has_country_flag = ENG_nww_irish_busy }} {gate} }} cost = {cost} days_remove = 35 days_re_enable = 60 '
                 f'complete_effect = {{ set_country_flag = ENG_nww_irish_busy }} cancel_trigger = {{ OR = {{ has_capitulated = yes NOT = {{ 119 = {{ is_owned_and_controlled_by = ENG }} }} }} }} cancel_effect = {{ clr_country_flag = ENG_nww_irish_busy add_political_power = {cost} }} remove_effect = {{ clr_country_flag = ENG_nww_irish_busy {body} ENG_nww_clamp = yes }} ai_will_do = {{ factor = 5 }}')
    decision('cabinet','irish_deadline','Ольстер требует урегулирования','Ulster Demands a Settlement',
             '180 дней на снижение напряжённости ниже 50 или заключение соглашения. Провал обострит кризис кабинета и откроет вооружённую развязку.',
             '180 days to reduce tension below 50 or conclude an agreement. Failure deepens the cabinet crisis and opens an armed outcome.',
             'visible = { has_country_flag = ENG_nww_irish_deadline_active } activation = { has_country_flag = ENG_nww_irish_deadline_active } is_good = no days_mission_timeout = 180 '
             'available = { OR = { check_variable = { var = ENG_nww_irish_pressure value = 50 compare = less_than } has_country_flag = ENG_nww_irish_agreement } } complete_effect = { clr_country_flag = ENG_nww_irish_deadline_active } '
             'timeout_effect = { clr_country_flag = ENG_nww_irish_deadline_active set_country_flag = ENG_nww_irish_failed country_event = { id = nww_eng.23 days = 1 } } cancel_trigger = { OR = { has_war = yes has_country_flag = ENG_nww_irish_final NOT = { 119 = { is_owned_by = ENG } } } } cancel_effect = { clr_country_flag = ENG_nww_irish_deadline_active }')
    decision('cabinet','border_referendum','Согласовать изменение статуса Ольстера','Negotiate a Change in Ulster Status',
             'После взаимных гарантий предложить Дублину договор о передаче Северной Ирландии. Требуются согласие Ирландии и фактическое владение и контроль территории.',
             'After mutual guarantees, offer Dublin a treaty transferring Northern Ireland. Requires Irish consent and actual ownership and control.',
             'visible = { has_country_flag = ENG_nww_border_vote_unlocked NOT = { has_country_flag = ENG_nww_border_transferred } } available = { '+peace+' 119 = { is_owned_and_controlled_by = ENG } IRE = { exists = yes has_war = no is_subject = no } } cost = 75 days_remove = 70 days_re_enable = 180 remove_effect = { country_event = { id = nww_eng.24 days = 1 } } ai_will_do = { factor = 0 }')
    # Real access, convoys, ownership and control; no fabricated trade revenue.
    bases={
        'atlantic':(132,'Северная Атлантика','North Atlantic'),
        'suez':(453,'Суэц','Suez'),
        'cape':(681,'Мыс Доброй Надежды','Cape of Good Hope'),
        'indian':(336,'Сингапур','Singapore'),
    }
    route_effect=['set_variable = { ENG_nww_open_routes = 0 }']
    for route,(sid,ru,en) in bases.items():
        # Friendly access requires both a friendly controller and legal access.
        access=f'{sid} = {{ OR = {{ is_controlled_by = ENG controller = {{ is_in_faction_with = ENG NOT = {{ has_war_with = ENG }} }} controller = {{ gives_military_access_to = ENG NOT = {{ has_war_with = ENG }} }} }} }}'
        if route=='cape': access='has_country_flag = ENG_nww_cape_ready '+access
        condition='has_navy_size = { size > 99 type = convoy } '+access
        route_effect.append(f'set_variable = {{ {P}route_{route} = 0 }} if = {{ limit = {{ {condition} }} set_variable = {{ {P}route_{route} = 1 }} add_to_variable = {{ {P}open_routes = 1 }} }}')
    route_effect.append('if = { limit = { has_country_flag = ENG_nww_routes_unlocked check_variable = { var = ENG_nww_open_routes value = 3 compare = less_than } } if = { limit = { NOT = { has_idea = ENG_nww_sea_delay } } add_ideas = ENG_nww_sea_delay } } else = { remove_ideas = ENG_nww_sea_delay }')
    effect('update_routes','\n'.join(route_effect))
    decision('routes','transport_reserve','Заказать резерв транспортов','Order Reserve Transports',
             '50 политической власти и две гражданские фабрики на 70 дней: 40 конвоев. Использует общий слот проектов.',
             '50 political power and two civilian factories for 70 days: 40 convoys. Uses the shared project slot.',
             'visible = { has_country_flag = ENG_nww_routes_unlocked } available = { has_capitulated = no NOT = { has_country_flag = ENG_nww_project_busy } } cost = 50 days_remove = 70 days_re_enable = 90 complete_effect = { set_country_flag = ENG_nww_project_busy add_ideas = ENG_nww_project_cost } remove_effect = { ENG_nww_release_project = yes add_equipment_to_stockpile = { type = convoy amount = 40 producer = ENG } } cancel_trigger = { has_capitulated = yes } cancel_effect = { ENG_nww_release_project = yes add_political_power = 50 } ai_will_do = { factor = 3 modifier = { factor = 0 has_navy_size = { size > 299 type = convoy } } }')

    event(1,'Цена короны','The Price of the Crown',
          'За кабинетом стоят крупнейшие рынки мира, но казна не способна одновременно оплатить все требования. Канцлер предлагает определить первый приоритет. Это решение задаст начало программы, сохранив последующий выбор устройства государства.',
          'The cabinet commands vast markets, but the Treasury cannot meet every demand at once. The Chancellor asks for an initial priority. It will launch a programme while leaving the constitutional choice open.',
          [('Восстановление метрополии','Metropolitan recovery','ENG_nww_build_civilian = { AMOUNT = 1 }','',45),
           ('Подготовка имперских переговоров','Prepare imperial negotiations','ENG_nww_trust_all = { AMOUNT = 5 } add_political_power = 35','',40),
           ('Перевооружение','Rearmament','ENG_nww_build_military = { AMOUNT = 1 } add_war_support = 0.05','',15)])
    event(4,'Крах конституционного согласия','Constitutional Consent Breaks Down',
          'Противники нового режима отказались признать чрезвычайную передачу власти. Часть гарнизонов поддержала парламент. Кабинету предстоит удержать государство в гражданской войне.',
          'Opponents reject the emergency transfer of power. Some garrisons have rallied to Parliament. The cabinet must now hold the state together in a civil war.',
          [('Собрать верные части','Rally loyal forces','start_civil_war = { ideology = democratic size = 0.35 }','has_civil_war = no NOT = { has_government = democratic }',100),
           ('Кризис уже разрешён','The crisis has already passed','','OR = { has_civil_war = yes has_government = democratic }',100)])
    event(10,'Договор ратифицирован','Treaty Ratified',
          'Правительство партнёра ратифицировало предложение. Новые обязательства вступают в силу в согласованном объёме; местные учреждения и вооружённые силы сохраняются.',
          'The partner government has ratified the proposal. Its agreed obligations enter into force; local institutions and armed forces remain in place.',
          [('Соблюдать договор','Honour the treaty','','',100)])
    event(11,'Предложение отклонено','Proposal Declined',
          'Правительство партнёра отказалось от предложения. Прежний статус сохраняется. Кабинет сможет вернуться к переговорам после подготовки нового проекта.',
          'The partner government declined the proposal. Existing status is preserved. The cabinet may prepare a new proposal after the negotiation cooldown.',
          [('Принять ответ','Accept the reply','','',100)])
    event(20,'Приглашение ирландской делегации','Invite the Irish Delegation',
          'Проект Белфастского соглашения предусматривает местное представительство, гарантии обеим общинам и совместное расследование пограничных инцидентов. Его необходимо направить правительству Ирландии.',
          'The Belfast draft provides local representation, guarantees to both communities and joint investigation of border incidents. It must be submitted to the Irish government.',
          [('Направить проект в Дублин','Send the draft to Dublin',
            'set_country_flag = { flag = ENG_nww_irish_offer days = 90 } IRE = { country_event = { id = nww_eng.21 days = 1 } }',
            'IRE = { exists = yes has_war = no is_subject = no } has_war = no 119 = { is_owned_and_controlled_by = ENG }',100),
           ('Пока нет условий для переговоров','Conditions do not permit talks','','NOT = { AND = { IRE = { exists = yes has_war = no is_subject = no } has_war = no 119 = { is_owned_and_controlled_by = ENG } } }',100)])
    event(21,'Белфастский проект','The Belfast Draft',
          'Лондон предлагает международные гарантии общинам Северной Ирландии и постоянную пограничную комиссию. Договор не меняет суверенитет над Ольстером; дальнейшие изменения потребуют нового согласия.',
          'London offers international guarantees for the communities of Northern Ireland and a permanent border commission. The treaty does not change Ulster sovereignty; any later change requires fresh consent.',
          [('Подписать соглашение','Sign the agreement','ENG = { clr_country_flag = ENG_nww_irish_offer set_country_flag = ENG_nww_irish_agreement set_country_flag = ENG_nww_irish_final clr_country_flag = ENG_nww_irish_coercion set_variable = { ENG_nww_irish_pressure = 0 } remove_ideas = ENG_nww_ulster_garrison add_stability = 0.05 ENG_nww_trust_all = { AMOUNT = 5 } }',
            'ENG = { has_country_flag = ENG_nww_irish_offer has_war = no } has_war = no 119 = { is_owned_and_controlled_by = ENG }',85),
           ('Отказаться от проекта','Decline the draft','ENG = { clr_country_flag = ENG_nww_irish_offer add_to_variable = { ENG_nww_irish_pressure = 10 } ENG_nww_clamp = yes }','',15)])
    event(23,'Кабинет перед ирландским кризисом','The Cabinet Faces the Irish Crisis',
          'Срок урегулирования истёк. Чрезвычайные меры подорвали доверие, а в Ольстере формируются вооружённые группы. Парламент требует отставки министров или нового соглашения.',
          'The settlement deadline has expired. Emergency measures have damaged trust and armed groups are forming in Ulster. Parliament demands ministerial resignations or a new settlement.',
          [('Отставка министров и новое посредничество','Ministerial resignations and fresh mediation','add_political_power = -100 add_stability = -0.10 set_variable = { ENG_nww_irish_pressure = 40 } set_country_flag = ENG_nww_irish_talks_ready clr_country_flag = ENG_nww_irish_failed','',85),
           ('Подавить вооружённые группы','Suppress the armed groups','add_stability = -0.10 ENG_nww_trust_all = { AMOUNT = -10 } if = { limit = { NIR = { exists = no } 119 = { is_owned_and_controlled_by = ENG } has_war = no } 119 = { transfer_state_to = NIR } NIR = { set_politics = { ruling_party = neutrality elections_allowed = no } load_oob = ENG_nww_ulster_revolt } declare_war_on = { target = NIR type = annex_everything } }',
            'has_war = no has_civil_war = no 119 = { is_owned_and_controlled_by = ENG } NIR = { exists = no }',15)])
    event(24,'Будущий статус Ольстера','Ulster’s Future Status',
          'После местных консультаций кабинет готов предложить передачу Северной Ирландии под власть Дублина при сохранении гражданских и религиозных гарантий. Окончательное решение требует согласия ирландского правительства.',
          'Following local consultations, the cabinet offers to transfer Northern Ireland to Dublin with civil and religious guarantees. Final agreement requires Irish government consent.',
          [('Передать проект договора','Submit the treaty draft','set_country_flag = { flag = ENG_nww_border_offer days = 90 } IRE = { country_event = { id = nww_eng.25 days = 1 } }',
            'has_war = no 119 = { is_owned_and_controlled_by = ENG } IRE = { exists = yes has_war = no is_subject = no }',100),
           ('Отложить до восстановления мира','Postpone until peace returns','','NOT = { AND = { has_war = no 119 = { is_owned_and_controlled_by = ENG } IRE = { exists = yes has_war = no is_subject = no } } }',100)])
    event(25,'Предложение об объединении острова','An Offer to Unite the Island',
          'Лондон предлагает согласованную передачу Северной Ирландии с гарантиями общинам. Принятие договора завершит территориальный спор, сохранив отдельное британское государство.',
          'London offers an agreed transfer of Northern Ireland with guarantees to its communities. Acceptance settles the territorial dispute while preserving the separate British state.',
          [('Ратифицировать передачу','Ratify the transfer','119 = { transfer_state_to = IRE } ENG = { clr_country_flag = ENG_nww_border_offer set_country_flag = ENG_nww_border_transferred set_country_flag = ENG_nww_irish_final set_variable = { ENG_nww_irish_pressure = 0 } }',
            'has_war = no is_subject = no ENG = { has_country_flag = ENG_nww_border_offer has_war = no } 119 = { is_owned_and_controlled_by = ENG }',90),
           ('Сохранить существующий договор','Keep the existing treaty','ENG = { clr_country_flag = ENG_nww_border_offer }','',10)])

    # An unsettled dependency gets a warning and a timed diplomatic exit.
    # It never vanishes just because a trust counter crosses a threshold.
    crisis_monthly=[]
    for i,(tag,ru,en) in enumerate(PARTNERS):
        active=P+'crisis_'+tag
        crisis_monthly.append(f'if = {{ limit = {{ has_war = no {tag} = {{ exists = yes is_subject_of = ENG has_capitulated = no }} {ck("trust_"+tag,25,"less_than")} NOT = {{ has_country_flag = {active} }} NOT = {{ has_country_flag = {P}crisis_settled_{tag} }} NOT = {{ has_country_flag = {P}coercive_settlement }} }} set_country_flag = {active} activate_mission = {P}deadline_{tag} }}')
        decision('imperial','deadline_'+tag,'Пересмотр обязательств: '+ru,'Review of Obligations: '+en,
                 '180 дней: поднять доверие до 40 или заключить договор. При провале зависимое правительство потребует суверенитета. Во время внешней войны миссия отменяется и может возобновиться после мира.',
                 '180 days: raise trust to 40 or sign a compact. Failure brings a demand for sovereignty. External war cancels the mission; it can restart after peace.',
                 f'visible = {{ has_country_flag = {active} }} activation = {{ has_country_flag = {active} }} is_good = no days_mission_timeout = 180 available = {{ OR = {{ {ck("trust_"+tag,40)} has_country_flag = {P}compact_{tag} }} }} complete_effect = {{ clr_country_flag = {active} set_country_flag = {P}crisis_settled_{tag} }} '
                 f'cancel_trigger = {{ OR = {{ has_war = yes {tag} = {{ exists = no NOT = {{ is_subject_of = ENG }} }} }} }} cancel_effect = {{ clr_country_flag = {active} }} '
                 f'timeout_effect = {{ clr_country_flag = {active} set_country_flag = {P}crisis_settled_{tag} {tag} = {{ country_event = {{ id = nww_eng.{300+i} days = 1 }} }} }}')
        decision('imperial','assurances_'+tag,'Гарантии местному парламенту: '+ru,'Assurances to the Local Parliament: '+en,
                 '35 политической власти и 35 дней: +15 доверия. Использует общий слот переговоров. Военные или административные препятствия отменяют процедуру с возвратом стоимости.',
                 '35 political power and 35 days: +15 trust. Uses the shared negotiation slot. War or administrative obstacles cancel the procedure and refund its cost.',
                 f'visible = {{ {tag} = {{ exists = yes }} {ck("trust_"+tag,80,"less_than")} }} available = {{ {peace} {tag} = {{ {open_country} }} NOT = {{ has_country_flag = ENG_nww_project_busy }} }} cost = 35 days_remove = 35 days_re_enable = 90 '
                 f'complete_effect = {{ set_country_flag = ENG_nww_project_busy }} remove_effect = {{ ENG_nww_release_project = yes add_to_variable = {{ {P}trust_{tag} = 15 }} ENG_nww_clamp = yes }} '
                 f'cancel_trigger = {{ OR = {{ has_war = yes has_capitulated = yes {tag} = {{ OR = {{ exists = no has_war_with = ENG AND = {{ is_subject = yes NOT = {{ is_subject_of = ENG }} }} }} }} }} }} '
                 'cancel_effect = { ENG_nww_release_project = yes add_political_power = 35 } ai_will_do = { factor = 2 }')
        event(300+i,'Требование пересмотреть имперский договор','A Demand to Review the Imperial Treaty',
              'Лондон не смог урегулировать наши разногласия в установленный срок. Правительство может потребовать полного суверенитета либо согласиться на новый период переговоров. Британия не получает права отменить наш выбор.',
              'London failed to settle our differences before the deadline. The government may demand full sovereignty or agree to another round of talks. Britain cannot overturn our choice.',
              [('Провозгласить суверенитет','Assert sovereignty',f'ENG = {{ set_autonomy = {{ target = {tag} autonomy_state = autonomy_free end_wars = no end_civil_wars = no }} set_country_flag = {P}independence_{tag} }}',
                'has_war = no is_subject_of = ENG ENG = { has_war = no }',70),
               ('Дать переговорам ещё один шанс','Give negotiations another chance',f'ENG = {{ set_variable = {{ {P}trust_{tag} = 35 }} }}','',30)])

    # The crown has its own NWW succession rather than immortal vanilla spirits.
    event(30,'Корона переходит к наследнику','The Crown Passes to the Heir',
          'Георг V скончался. Наследник принимает корону государства, которое избежало мировой войны, но не избежало споров о границах монаршей власти. Кабинет ожидает подтверждения конституционных обязательств.',
          'George V has died. His heir inherits a state that avoided world war but not arguments over royal power. The cabinet awaits confirmation of constitutional commitments.',
          [('Признать Эдуарда VIII','Recognise Edward VIII','remove_ideas = george_v add_ideas = ENG_king_edward set_country_flag = ENG_nww_succession_done','',100)])
    # Convert this one event to a normal date-triggered event.
    events[-1]=events[-1].replace('is_triggered_only = yes', 'fire_only_once = yes trigger = { tag = ENG has_focus_tree = ENG_nww_focus date > 1936.1.19 has_idea = george_v NOT = { has_government = communism } } mean_time_to_happen = { days = 1 }',1)
    event(31,'Корона перед парламентом','The Crown before Parliament',
          'Новый монарх требует определить границы его участия в политике. Кабинет предлагает подтвердить парламентскую ответственность правительства. Король может принять это условие либо уступить престол брату.',
          'The new monarch seeks to define his political role. The cabinet proposes reaffirming parliamentary responsibility. The King may accept or yield the throne to his brother.',
          [('Подтвердить конституционный порядок','Reaffirm constitutional government','add_stability = 0.05','',65),
           ('Принять отречение','Accept the abdication','remove_ideas = ENG_king_edward add_ideas = ENG_george_vi add_stability = 0.05','',35)])
    events[-1]=events[-1].replace('is_triggered_only = yes','fire_only_once = yes trigger = { tag = ENG has_focus_tree = ENG_nww_focus date > 1936.12.1 has_idea = ENG_king_edward has_government = democratic } mean_time_to_happen = { days = 7 }',1)
    event(32,'Передача руководства кабинетом','A New Head of the Cabinet',
          'Болдуин готов оставить руководство правительством. Парламентское большинство обсуждает кандидатуру Чемберлена, сторонника упорядоченных смет и переговоров, и Черчилля, настаивающего на более решительном перевооружении. Выбор нового премьера сохраняет конституционный порядок.',
          'Baldwin is ready to leave office. The parliamentary majority considers Chamberlain, an advocate of orderly budgets and negotiation, and Churchill, who argues for more determined rearmament. Choosing a new premier preserves constitutional government.',
          [('Кабинет Чемберлена','A Chamberlain cabinet','recruit_character = ENG_neville_chamberlain promote_character = ENG_neville_chamberlain','',85),
           ('Поручить кабинет Черчиллю','Ask Churchill to form a cabinet','promote_character = ENG_winston_churchill add_war_support = 0.05','',15)])
    events[-1]=events[-1].replace('is_triggered_only = yes','fire_only_once = yes trigger = { tag = ENG has_focus_tree = ENG_nww_focus date > 1937.5.27 has_government = democratic has_country_leader = { character = ENG_stanley_baldwin ruling_only = yes } } mean_time_to_happen = { days = 7 }',1)

    # Remaining actual dependencies receive the same consent-based exit.
    # This never releases Ottoman Palestine/Jordan or recreates British Kuwait.
    for i,(tag,ru,en) in enumerate([('MAL','Малайя','Malaya'),('BRM','Бирма','Burma'),('OMA','Оман','Oman'),('EGY','Египет','Egypt'),('PAL','Палестина','Palestine'),('JOR','Иордания','Jordan')]):
        key='colonial_exit_'+tag
        decision('imperial',key,'Соглашение о суверенитете: '+ru,'Sovereignty Agreement: '+en,
                 '50 политической власти, две гражданские фабрики и 35 дней переговоров. Предложение направляется только реально зависимому правительству; оно может отказаться.',
                 '50 political power, two civilian factories and 35 days. The offer is sent only to an actual dependency; its government may decline.',
                 f'visible = {{ has_country_flag = ENG_nww_decolonisation_unlocked {tag} = {{ exists = yes is_subject_of = ENG }} NOT = {{ has_country_flag = {P+key} }} }} '
                 f'available = {{ {peace} num_of_available_civilian_factories > 1 NOT = {{ has_country_flag = ENG_nww_project_busy }} }} cost = 50 days_remove = 35 days_re_enable = 90 '
                 'complete_effect = { set_country_flag = ENG_nww_project_busy add_ideas = ENG_nww_project_cost } '
                 f'cancel_trigger = {{ OR = {{ has_war = yes has_capitulated = yes {tag} = {{ NOT = {{ is_subject_of = ENG }} }} }} }} '
                 f'cancel_effect = {{ ENG_nww_release_project = yes add_political_power = 50 }} remove_effect = {{ ENG_nww_release_project = yes set_country_flag = {{ flag = {P}offer_{key} days = 90 }} {tag} = {{ country_event = {{ id = nww_eng.{400+i} days = 1 }} }} }} ai_will_do = {{ factor = 3 }}')
        event(400+i,'Договор о передаче суверенитета','Treaty on the Transfer of Sovereignty',
              'Лондон подготовил передачу административных полномочий нашему правительству. Мы можем принять независимость без территориальных уступок или пока сохранить прежний статус. Торговые и оборонные соглашения потребуют отдельного согласия.',
              'London has prepared to transfer administrative powers to our government. We may accept independence without territorial concessions or retain existing status. Trade and defence agreements require separate consent.',
              [('Принять передачу полномочий','Accept the transfer of powers',f'ENG = {{ clr_country_flag = {P}offer_{key} set_country_flag = {P+key} set_autonomy = {{ target = {tag} autonomy_state = autonomy_free end_wars = no end_civil_wars = no }} }}',
                f'is_subject_of = ENG has_war = no ENG = {{ has_war = no has_country_flag = {P}offer_{key} }}',90),
               ('Сохранить прежний статус','Retain the existing status',f'ENG = {{ clr_country_flag = {P}offer_{key} }}','',10)])

    # Existing British organizations keep every native generic template and trait.
    def dump(doc,depth=0):
        lines=[]
        for k,v,op in doc:
            prefix=('\t'*depth)+(str(k)+' '+op+' ' if k is not None else '')
            if isinstance(v,list): lines.append(prefix+'{\n'+dump(v,depth+1)+'\n'+'\t'*depth+'}')
            else:
                val=v if re.fullmatch(r'[\w.\-:@]+',v) else quoted(v)
                lines.append(prefix+val)
        return '\n'.join(lines)
    from hoi4_script import parse
    mio_doc=read(game/'common/military_industrial_organization/organizations/ENG_organization.txt')
    designer_groups=defaultdict(list)
    companies=[
        ('ENG_vickers_armstrong_eng_organization','vickers','Vickers-Armstrong','tank_manufacturer','armor','medium_tank_manufacturer','reliability',0.05),
        ('ENG_rsaf_enfield_organization','standard_ammunition','Royal Small Arms Factory','materiel_manufacturer','infantry_weapons','infantry_equipment_manufacturer','soft_attack',0.05),
        ('ENG_supermarine_organization','supermarine','Supermarine','aircraft_manufacturer','light_fighter','light_aircraft_manufacturer','air_defence',0.05),
        ('ENG_hawker_organization','engine_plants','Hawker','aircraft_manufacturer','cas_bomber','CAS_manufacturer','air_attack',0.05),
        ('ENG_fairey_aviation_organization','fairey','Fairey Aviation','aircraft_manufacturer','naval_air','naval_aircraft_manufacturer','naval_strike_attack',0.05),
    ]
    for organization,gate,name,slot,category,trait,stat,amount in companies:
        token=P+organization+'_programme'
        loc(token,name+': государственная программа',name+': Public Programme')
        node=next(v for k,v,o in mio_doc if k==organization)
        node.extend(parse(f'add_trait = {{ token = {token} name = {token} icon = GFX_generic_mio_trait_icon_production_capacity position = {{ x = 20 y = 0 }} special_trait_background = yes available = {{ FROM = {{ {F(gate)} }} }} equipment_bonus = {{ {stat} = {amount} }} }}'))
        designer=P+gate+'_designer';loc(designer,name+': государственная программа',name+': Public Programme')
        loc(designer+'_desc','Специализированная программа предприятия, открытая национальными фокусами.','A specialised enterprise programme unlocked through national focuses.')
        designer_groups[slot].append(f'{designer} = {{ picture = generic_economic_recovery cost = 150 allowed = {{ original_tag = ENG NOT = {{ has_dlc = "Arms Against Tyranny" }} }} available = {{ {F(gate)} }} research_bonus = {{ {category} = 0.20 }} traits = {{ {trait} }} }}')
    write('common/military_industrial_organization/organizations/ENG_organization.txt','# Owner: ENG. Native organizations preserved; focus-gated NWW traits appended.\n'+dump(mio_doc))
    write('common/ideas/ENG_designers.txt','ideas = {\n'+'\n'.join(slot+' = { designer = yes\n'+'\n'.join(rows)+'\n}' for slot,rows in designer_groups.items())+'\n}')

    clamp=['clamp_variable = { var = ENG_nww_irish_pressure min = 0 max = 100 } clamp_variable = { var = ENG_nww_labour_mandate min = 0 max = 100 }']
    clamp.extend(f'clamp_variable = {{ var = {P}trust_{tag} min = 0 max = 100 }}' for tag,_,_ in PARTNERS)
    effect('clamp','\n'.join(clamp))
    # Settled relationships stop generating automatic pressure. War pauses the clock.
    monthly=['ENG_nww_clamp = yes ENG_nww_recount_partners = yes ENG_nww_update_routes = yes',
             'if = { limit = { 119 = { is_owned_by = ENG } NOT = { has_country_flag = ENG_nww_irish_final } has_war = no has_capitulated = no } add_to_variable = { ENG_nww_irish_pressure = 3 } if = { limit = { has_country_flag = ENG_nww_irish_coercion } add_to_variable = { ENG_nww_irish_pressure = 3 } } }',
             'if = { limit = { check_variable = { var = ENG_nww_irish_pressure value = 70 compare = greater_than_or_equals } NOT = { has_country_flag = ENG_nww_irish_final } NOT = { has_country_flag = ENG_nww_irish_deadline_active } NOT = { has_country_flag = ENG_nww_irish_failed } has_war = no 119 = { is_owned_by = ENG } } set_country_flag = ENG_nww_irish_deadline_active activate_mission = ENG_nww_irish_deadline }']
    for tag,_,_ in PARTNERS:
        monthly.append(f'if = {{ limit = {{ {tag} = {{ exists = yes is_subject_of = ENG }} NOT = {{ has_country_flag = ENG_nww_compact_{tag} }} NOT = {{ has_country_flag = ENG_nww_federal_{tag} }} NOT = {{ has_country_flag = ENG_nww_independence_{tag} }} NOT = {{ has_country_flag = ENG_nww_coercive_settlement }} has_war = no }} add_to_variable = {{ ENG_nww_trust_{tag} = -1 }} }}')
    monthly.append('ENG_nww_clamp = yes')
    monthly.extend(crisis_monthly)
    effect('monthly','\n'.join(monthly))
    # Daily repair grants no PP, factories, ships, territory, elections or treaty votes.
    daily=['if = { limit = { NOT = { has_focus_tree = ENG_nww_focus } has_civil_war = no } load_focus_tree = { tree = ENG_nww_focus keep_completed = yes } }',
           'if = { limit = { NOT = { has_country_flag = ENG_nww_initialized } } ENG_nww_initialize = yes }',
           'if = { limit = { OR = { has_country_flag = ENG_nww_spirit_refresh_pending NOT = { has_dynamic_modifier = { modifier = ENG_nww_state } } NOT = { has_dynamic_modifier = { modifier = ENG_nww_economy } } NOT = { has_dynamic_modifier = { modifier = ENG_nww_army } } NOT = { has_dynamic_modifier = { modifier = ENG_nww_air } } NOT = { has_dynamic_modifier = { modifier = ENG_nww_navy } } NOT = { has_dynamic_modifier = { modifier = ENG_nww_science } } } } ENG_nww_rebuild_spirits = yes clr_country_flag = ENG_nww_spirit_refresh_pending }',
           'if = { limit = { has_completed_focus = ENG_nww_belfast has_country_flag = ENG_nww_irish_agreement } set_country_flag = ENG_nww_irish_final }',
           'ENG_nww_clamp = yes ENG_nww_recount_partners = yes ENG_nww_update_routes = yes']
    # Synchronize treaty benefits and unlocks from the actual settlement. Repeated
    # repair must not replay a factory grant, a vote, an election or an annexation.
    for tag,_,_ in PARTNERS:
        daily.append(f'if = {{ limit = {{ {tag} = {{ {open_country} }} }} '
                     f'if = {{ limit = {{ has_country_flag = {P}compact_{tag} }} {tag} = {{ if = {{ limit = {{ NOT = {{ has_idea = ENG_nww_trade_partner }} }} add_ideas = ENG_nww_trade_partner }} }} }} '
                     f'if = {{ limit = {{ has_country_flag = {P}federal_{tag} }} {tag} = {{ if = {{ limit = {{ NOT = {{ has_idea = ENG_nww_federal_partner }} }} add_ideas = ENG_nww_federal_partner }} }} }} '
                     f'}} else = {{ {tag} = {{ remove_ideas = ENG_nww_trade_partner remove_ideas = ENG_nww_federal_partner }} }}')
        daily.append(f'if = {{ limit = {{ has_country_flag = ENG_nww_science_unlocked has_country_flag = {P}compact_{tag} NOT = {{ has_country_flag = {P}research_joined_{tag} }} {tag} = {{ {open_country} }} }} set_country_flag = {P}research_joined_{tag} {tag} = {{ add_to_tech_sharing_group = ENG_nww_research }} }}')
    for key,flag in [('premiers','conferences_unlocked'),('conference','conferences_unlocked'),('ratification','ratification_unlocked'),('colonial_review','decolonisation_unlocked'),('island_treaties','decolonisation_unlocked'),('imperial_investment','investment_unlocked'),('canadian_corridors','canada_project_unlocked'),('indian_electricity','india_project_unlocked'),('scientific_exchange','science_unlocked'),('naval_planning','routes_unlocked'),('cape_route','cape_ready'),('irish_report','irish_unlocked'),('irish_talks','irish_talks_ready')]:
        daily.append(f'if = {{ limit = {{ {F(key)} }} set_country_flag = {P+flag} }}')
    effect('daily','\n'.join(daily))
    write('common/on_actions/ENG_on_actions.txt','''on_actions = {
on_startup = { effect = { ENG = { if = { limit = { exists = yes } ENG_nww_daily = yes ENG_nww_rebuild_spirits = yes } } } }
on_daily_ENG = { effect = { ENG_nww_daily = yes } }
on_monthly_ENG = { effect = { if = { limit = { exists = yes has_focus_tree = ENG_nww_focus } ENG_nww_monthly = yes } } }
}''')

    # Bilateral diplomacy is consent-based and does not force alliances or wars.
    for i,(tag,ru,en) in enumerate([('GER','Берлин','Berlin'),('USA','Вашингтон','Washington'),('TUR','Константинополь','Constantinople')]):
        eid=200+i
        decision('imperial','diplomacy_'+tag,'Переговоры: '+ru,'Talks with '+en,
                 'Предложить торговое и дипломатическое сближение за 50 политической власти. Получатель принимает решение самостоятельно.',
                 'Offer trade and diplomatic rapprochement for 50 political power. The recipient decides independently.',
                 f'visible = {{ has_country_flag = ENG_nww_diplomacy_unlocked NOT = {{ has_country_flag = ENG_nww_diplomacy_{tag} }} }} available = {{ {peace} {tag} = {{ exists = yes has_war = no }} }} cost = 50 days_re_enable = 180 complete_effect = {{ set_country_flag = {{ flag = ENG_nww_dip_offer_{tag} days = 90 }} {tag} = {{ country_event = {{ id = nww_eng.{eid} days = 1 }} }} }} ai_will_do = {{ factor = 2 }}')
        event(eid,'Дипломатическая миссия из Лондона','A Diplomatic Mission from London',
              'Британия предлагает урегулировать торговые разногласия и поддерживать постоянные консультации. Соглашение не содержит территориальных уступок и не обязывает участвовать в войне.',
              'Britain proposes settling trade disputes and maintaining regular consultations. The agreement contains no territorial concessions and no obligation to enter a war.',
              [('Принять предложение','Accept the offer',f'add_opinion_modifier = {{ target = ENG modifier = ENG_nww_rapprochement }} ENG = {{ clr_country_flag = ENG_nww_dip_offer_{tag} set_country_flag = ENG_nww_diplomacy_{tag} add_opinion_modifier = {{ target = {tag} modifier = ENG_nww_rapprochement }} }}',f'has_war = no ENG = {{ has_war = no has_country_flag = ENG_nww_dip_offer_{tag} }}',60),
               ('Отклонить предложение','Decline the offer',f'ENG = {{ clr_country_flag = ENG_nww_dip_offer_{tag} }}','',40)])
    loc('ENG_nww_rapprochement','Дипломатическое сближение','Diplomatic Rapprochement')
    write('common/opinion_modifiers/ENG_opinions.txt','opinion_modifiers = { ENG_nww_rapprochement = { value = 25 decay = 0.5 } }')
    write('common/technology_sharing/ENG_research.txt','technology_sharing_group = { id = ENG_nww_research name = ENG_nww_research desc = ENG_nww_research_desc picture = GFX_commonwealth_research research_sharing_per_country_bonus = 0.05 available = { OR = { tag = ENG has_idea = ENG_nww_trade_partner has_idea = ENG_nww_federal_partner } NOT = { has_war_with = ENG } } }')
    loc('ENG_nww_research','Научное сотрудничество Содружества','Commonwealth Scientific Cooperation')
    loc('ENG_nww_research_desc','Добровольный обмен результатами исследований в рамках ратифицированных соглашений.','Voluntary research exchange under ratified agreements.')
    write('common/scripted_effects/ENG_effects.txt','\n\n'.join(effects))
    write('common/decisions/ENG_decisions.txt','\n\n'.join(P+cat+'_category = {\n'+'\n'.join(ds)+'\n}' for cat,ds in decisions.items()))
    write('events/ENG_events.txt','\n\n'.join(events))
    # Real, modest rebel force; no peacetime annexation or foreign-victory shortcut.
    write('history/units/ENG_nww_ulster_revolt.txt','''division_template = {
name = "Ulster Volunteers"
regiments = { infantry = { x = 0 y = 0 } infantry = { x = 0 y = 1 } infantry = { x = 0 y = 2 } }
}
units = {
division = { name = "Ulster Volunteer Brigade" location = 3379 division_template = "Ulster Volunteers" start_experience_factor = 0.1 start_equipment_factor = 0.7 }
}
''')
    # Historical and explicit-rule plans use only playable NWW focuses.
    historical=['report','session','budget','continuity','irish_report','border_inquiry','irish_talks','belfast','majority','industrial_survey','coalfields','machine_tools','civil_service','premiers','local_parliaments','electric_grid','naval_review','repair_bases','naval_planning','escort','commonwealth_budget','commonwealth_charter','armament_board','ordnance','air_service','pilot_reserve','fighter_command','staff_college']
    write('common/ai_strategy_plans/ENG_nww_plans.txt','ENG_nww_historical = { name = "NWW Britain constitutional programme" desc = "A negotiated Commonwealth" allowed = { original_tag = ENG } enable = { has_country_flag = ENG_nww_plan_continuity } abort = { NOT = { has_country_flag = ENG_nww_plan_continuity } } ai_national_focuses = { '+' '.join(P+k for k in historical)+' } }')
