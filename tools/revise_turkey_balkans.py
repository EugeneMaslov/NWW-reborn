"""Extend the adapted Ottoman tree without reimporting or losing archive focuses."""
import json
import re
from pathlib import Path
from hoi4_script import read, parse, one, values, dump

ROOT = Path(__file__).resolve().parents[1]
FOCUS = ROOT / 'common/national_focus/TUR_focuses.txt'
CAMPAIGNS = {
    'BUL': ('TUR_war_with_bulgaria', [48, 184, 211, 212, 801, 1083]),
    'GRE': ('TUR_snova_copi', [47, 182, 185, 186, 187, 731]),
    'YUG': ('NWW_TUR_serbian_campaign', [105, 106, 107, 108, 802, 803, 970]),
    'ALB': ('NWW_TUR_albanian_campaign', [44, 805, 934]),
    'ROM': ('NWW_TUR_romanian_campaign', [46, 77, 78, 79, 80, 81, 766, 971]),
    'CRO': ('NWW_TUR_adriatic_campaign', [103, 104, 109, 163, 804]),
}
ACCORDS = ['NWW_TUR_officer_accord', 'NWW_TUR_ulema_accord', 'NWW_TUR_provincial_accord']
RULE_PATHS = {
    'historical': (['HISTORICAL', 'OTTOMAN'], ['TUR_AI_RANDOM_NEUTRALITY_HISTORICAL', 'TUR_AI_RANDOM_OTTOMAN']),
    'peaceful': (['ALTERNATE_KEMALIST', 'BALKAN_ENTENTE'], ['TUR_AI_RANDOM_ALT_KEMALIST', 'TUR_AI_RANDOM_BALKAN_ENTENTE']),
    'democratic': (['TUR_DEMOCRATIC_KEMALIST', 'TUR_DEMOCRATIC_ALTERNATE'], ['TUR_AI_RANDOM_DEMOCRATIC', 'TUR_AI_RANDOM_DEMOCRATIC_ALTERNATE']),
    'communism': (['COMMUNIST_TUR_AI', 'TUR_COMMUNISM_ALTERNATE'], ['TUR_AI_RANDOM_COMMUNISM', 'TUR_AI_RANDOM_COMMUNISM_ALTERNATE']),
    'fascism': (['FASCISM_TUR_AI', 'TUR_FASCISM_ALTERNATE'], ['TUR_AI_RANDOM_FASCISM', 'TUR_AI_RANDOM_FASCISM_ALTERNATE']),
}

NEW_LABELS = {
    'NWW_TUR_sultans_shadow': (
        'Авторитет султана и халифа', 'Authority of the Sultan and Caliph',
        'Султанат пережил десятилетия реформ, но двор, улемы и армия по-разному понимают его будущее. Признаем духовный авторитет султана, сохранив профессиональные военные и гражданские учреждения.',
        'The empire has survived decades of reform, but the palace, ulema and army disagree over its future. Recognize the Sultan\'s spiritual authority while preserving professional military and civil institutions.'),
    'NWW_TUR_ottoman_bourgeoisie': (
        'Османская буржуазия', 'The Ottoman Bourgeoisie',
        'Меджлис закрепит единые правила торговли и собственности для всех общин. Капитал Стамбула послужит развитию городов, а не новым завоеваниям.',
        'The Majlis will establish common trade and property rights for every community. Constantinople\'s capital will develop our cities.'),
    'NWW_TUR_agrarian_reform': (
        'Аграрная реформа', 'Agrarian Reform',
        'Земельные комитеты перераспределят крупные поместья и обеспечат крестьян кредитом и техникой. Рабочая федерация должна опираться и на Анатолию, и на провинции.',
        'Land committees will redistribute large estates and provide credit and machinery to farmers. The workers\' federation must represent Anatolia and the provinces alike.'),
    'NWW_TUR_rumelian_logistics': (
        'Снабжение Румелийского фронта', 'Supply the Rumelian Front',
        'Расширим склады, дороги и аэродромы Восточной Фракии. Балканская кампания требует надёжного снабжения, а не одних имперских лозунгов.',
        'Expand depots, roads and airfields in Eastern Thrace. A Balkan campaign requires reliable supplies.'),
    'NWW_TUR_war_industry_program': (
        'Имперская программа вооружений', 'Imperial Armaments Programme',
        'Государственные заказы и долгосрочные соглашения с промышленниками дадут армии современное оружие. Новый арсенал и военная промышленная программа поддержат подготовку кампании.',
        'State contracts and long-term agreements with manufacturers will supply modern weapons. A new arsenal and military production programme will sustain our campaign.'),
    'NWW_TUR_greek_settlement': (
        'Греческое урегулирование', 'The Greek Settlement',
        'После завоевания Греции восстановим порты и местное управление. Провинции получат гражданские гарантии; местная администрация и гарнизоны по-прежнему необходимы.',
        'After conquering Greece, restore the ports and local administration. Civil guarantees improve compliance without turning occupied provinces into Ottoman cores.'),
    'NWW_TUR_balkan_mandate': (
        'Османская балканская доктрина', 'The Ottoman Balkan Doctrine',
        'Болгарская и греческая кампании открыли путь на север и запад. Порта предъявит претензии на балканские земли; отдельные решения Генерального штаба позволят перейти к новым войнам. Мирное исчезновение соседнего государства не передаёт нам его земли.',
        'The Bulgarian and Greek campaigns have opened the routes north and west. The Porte will assert Balkan claims; separate military plans authorize further wars. A neighbour\'s disappearance does not transfer its territory to us.'),
    'NWW_TUR_serbian_campaign': (
        'На Белград', 'March on Belgrade',
        'Сербское королевство перекрывает дорогу к Дунаю. Подготовим самостоятельную кампанию за его полное подчинение. Союзников империи эта программа не затрагивает.',
        'The Serbian kingdom blocks the road to the Danube. Prepare a campaign to conquer it in full, provided it is not our ally.'),
    'NWW_TUR_albanian_campaign': (
        'Албанский плацдарм', 'The Albanian Bridgehead',
        'Албанские порты дадут империи выход к Адриатике. Генеральный штаб разработает план их захвата и полного присоединения Албании.',
        'Albanian ports provide access to the Adriatic. The General Staff will prepare the conquest and annexation of Albania.'),
    'NWW_TUR_romanian_campaign': (
        'К нижнему Дунаю', 'Towards the Lower Danube',
        'Плодородные земли, нефть и дунайские переправы Румынии имеют стратегическое значение. После побед на юге мы можем начать новую северную кампанию.',
        'Romania\'s farmland, oil and Danube crossings are strategic objectives. Victories in the south allow a new northern campaign.'),
    'NWW_TUR_adriatic_campaign': (
        'Босния и Адриатика', 'Bosnia and the Adriatic',
        'Предъявим хорватскому государству имперские претензии на Боснию и адриатическое побережье. Если эти земли уже захватила другая держава, претензии балканской доктрины сохраняются, но этот фокус не начинает войну с новым владельцем автоматически.',
        'Press imperial claims against Croatia over Bosnia and the Adriatic coast. If another power has already conquered these lands, our Balkan claims remain; this focus does not automatically declare war on their new owner.'),
    'NWW_TUR_rumelian_governorates': (
        'Румелийские генерал-губернаторства', 'The Rumelian Governorates',
        'Создадим постоянную гражданскую администрацию балканских провинций, согласуем местные хартии и снабжение гарнизонов. Сопротивление снизится, а подчинение будет расти; провинции не получат национальный статус одним указом.',
        'Establish permanent civil administration, provincial charters and garrison supply in the Balkans. Resistance falls and compliance grows without automatic core status.'),
}
OLD_LABELS = {
    'TUR_political_rw': ('Империя на перепутье', 'The Empire at a Crossroads',
        'Двор, армия, улемы и провинциальные представители требуют обновления государства. Выберем политический курс и откроем переговоры об общем устройстве империи.',
        'The palace, army, ulema and provincial representatives demand reform. Choose a political course and negotiate the institutions that will sustain it.'),
    'TUR_not_fascism': ('Опора на династию', 'Stand with the Dynasty',
        'Сохраним султанат и османское единство. Сильная власть должна договориться с армией и провинциями, прежде чем начинать новую балканскую политику.',
        'Preserve the Sultanate and Ottoman unity. Strong government must reach an agreement with the army and provinces before a new Balkan policy.'),
    'tur_bred': ('Провинциальные хартии', 'Provincial Charters',
        'Защитим языки общин, местное представительство и равный доступ к службе. Имперская солидарность должна подкрепляться правами, а не только лояльностью двору.',
        'Protect community languages, local representation and equal access to public service. Imperial solidarity requires rights as well as loyalty to the palace.'),
    'tur_polos': ('Совещательный меджлис', 'The Consultative Majlis',
        'Представители провинций получат постоянный совещательный орган при султане. Он согласует бюджет и хартии, сохраняя верховную власть династии.',
        'Provincial representatives will form a permanent consultative body under the Sultan, coordinating budgets and charters while retaining dynastic sovereignty.'),
    'TUR_proper_stoper': ('Самостоятельная имперская политика', 'An Independent Imperial Policy',
        'После внутреннего соглашения империя сможет проводить самостоятельную внешнюю политику. Выбор этого курса закрывает европейские дипломатические миссии.',
        'The internal compact enables an independent foreign policy. Choosing this course excludes the European diplomatic missions.'),
    'TUR_kosa_smerti': ('Балканское военное министерство', 'The Balkan War Ministry',
        'Реформированный Генеральный штаб согласует мобилизацию и оперативные планы для Балкан. Необходимо завершить объединение армейского командования и внутреннее соглашение.',
        'The reformed General Staff will coordinate mobilisation and Balkan operations. Unified army command and the internal compact must be completed first.'),
    'TUR_war_with_bulgaria': ('Болгарская кампания', 'The Bulgarian Campaign',
        'Начнём исторический для нашего мира путь имперской экспансии. После внутренних и военных реформ предъявим Болгарии претензии и получим бессрочную цель войны за полное завоевание. Следующий этап требует реальной победы.',
        'Begin this world\'s historical imperial expansion. Internal and military reforms unlock a permanent goal to conquer Bulgaria in full. The next stage requires an actual victory.'),
    'afg_bolgi': ('Болгарское урегулирование', 'The Bulgarian Settlement',
        'Закрепим управление всей завоёванной Болгарией и восстановим промышленность Софии. Гражданские гарантии повышают подчинение, но не превращают провинции в национальные территории.',
        'Consolidate administration across conquered Bulgaria and restore Sofia\'s industry. Civil guarantees improve compliance without granting Ottoman cores.'),
    'TUR_snova_copi': ('Греческая кампания', 'The Greek Campaign',
        'После полного болгарского урегулирования империя может повернуть к Греции. Бессрочная цель войны охватывает всю страну; балканская доктрина станет доступна после завоевания и устройства её провинций.',
        'The Bulgarian settlement allows an advance into Greece. A permanent war goal covers the entire country; the wider Balkan doctrine requires conquest and provincial administration.'),
}


def localize():
    for lang, title_index, desc_index in [('russian', 0, 2), ('english', 1, 3)]:
        path = ROOT / f'localisation/replace/TUR_l_{lang}.yml'
        text = path.read_text(encoding='utf-8-sig')
        for fid, entry in OLD_LABELS.items():
            for key, value in [(fid, entry[title_index]), (fid + '_desc', entry[desc_index])]:
                text = re.sub(r'^\s+' + re.escape(key) + r':\d*\s+".*"\s*$',
                              lambda _: f' {key}:0 "{value}"', text, flags=re.M)
        path.write_text(text.rstrip() + '\n', encoding='utf-8-sig')
        lines = [f'l_{lang}:']
        for fid, entry in NEW_LABELS.items():
            lines += [f' {fid}:0 "{entry[title_index]}"', f' {fid}_desc:0 "{entry[desc_index]}"']
        tt = ('Завершён фокус «Турецкая армия».'
              if lang == 'russian' else 'The Turkish Army focus has been completed.')
        lines.append(f' NWW_TUR_modern_war_ministry_tt:0 "{tt}"')
        targets = {'BUL': ('Болгарии', 'Bulgaria'), 'GRE': ('Греции', 'Greece'),
                   'YUG': ('Сербии', 'Serbia'), 'ALB': ('Албании', 'Albania'),
                   'ROM': ('Румынии', 'Romania'), 'CRO': ('Хорватии', 'Croatia')}
        for tag, names in targets.items():
            tooltip = (f'Получить претензии на земли {names[0]} и бессрочную цель войны за полное завоевание. '
                       'При капитуляции этой страны перед османами после данного фокуса она будет полностью присоединена. '
                       'Победа другой державы не передаёт нам её земли.' if lang == 'russian' else
                       f'Gain claims and a permanent war goal to conquer {names[1]}. '
                       'Its capitulation to the Ottomans after this focus fully annexes the country. '
                       'Victory by another power does not transfer its land to us.')
            lines.append(f' NWW_TUR_{tag}_campaign_tt:0 "{tooltip}"')
        (ROOT / f'localisation/nww_tur_balkans_l_{lang}.yml').write_text('\n'.join(lines) + '\n', encoding='utf-8-sig')


def write(relative, node):
    path = ROOT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(dump(node) + '\n', encoding='utf-8')


def field(node, key, value):
    node[:] = [(k, v, op) for k, v, op in node if k != key]
    node.append((key, value, '='))


def block(text):
    return parse(text)


def owned(states):
    return ' '.join(f'{sid} = {{ is_owned_and_controlled_by = ROOT }}' for sid in states)


def guarded_factory(sid, kind):
    return f'''{sid} = {{ if = {{ limit = {{ is_owned_and_controlled_by = ROOT }}
        add_extra_state_shared_building_slots = 1
        add_building_construction = {{ type = {kind} level = 1 instant_build = yes }}
    }} }}'''


def main():
    document = read(FOCUS)
    tree = one(document, 'focus_tree')
    by_id = {one(f, 'id'): f for f in values(tree, 'focus')}

    def update(fid, **fields):
        for name, value in fields.items():
            field(by_id[fid], name, block(value) if name in ('available', 'bypass', 'completion_reward') else value)

    def parents(fid, *groups):
        by_id[fid][:] = [(k, v, o) for k, v, o in by_id[fid] if k != 'prerequisite']
        for group in groups:
            by_id[fid].append(('prerequisite', block(' '.join('focus = ' + p for p in group)), '='))

    def add(fid, x, y, icon, parent, reward, available=None, cost=5):
        node = block(f'id = {fid} x = {x} y = {y} icon = {icon} cost = {cost}')
        node.append(('completion_reward', block(reward), '='))
        if available:
            node.extend(block('cancel_if_invalid = yes continue_if_invalid = no'))
            node.append(('available', block(available), '='))
        if fid in by_id:
            by_id[fid][:] = node
        else:
            tree.append(('focus', node, '='))
            by_id[fid] = node
        parents(fid, [parent])

    # The dynasty survives in this universe. Consultation is not republican elections.
    add('NWW_TUR_sultans_shadow', 6, 2, 'GFX_focus_TUR_loosen_the_laws_on_secularism',
        'TUR_not_fascism', 'add_stability = 0.05 add_war_support = 0.05')
    update('TUR_not_fascism', icon='GFX_focus_TUR_pivot_to_the_past')
    update('tur_bred', y='3')
    parents('tur_bred', ['NWW_TUR_sultans_shadow'])
    update('tur_polos', y='4', completion_reward='''
        set_politics = { ruling_party = neutrality elections_allowed = no }
        add_stability = 0.05 add_political_power = 50''')

    add('NWW_TUR_ottoman_bourgeoisie', 10, 4, 'GFX_goal_generic_consumer_goods',
        'NWW_TUR_federal_charter', guarded_factory(49, 'industrial_complex') + '\nadd_stability = 0.05')
    add('NWW_TUR_agrarian_reform', 14, 4, 'GFX_goal_generic_construct_civ_factory',
        'NWW_TUR_workers_union', 'nww_legacy_TUR_industry_step = yes add_stability = 0.05')
    add('NWW_TUR_imperial_compact', 8, 5, 'GFX_focus_TUR_pivot_to_the_past',
        'tur_polos', '''
        set_country_flag = NWW_TUR_council_settled
        nww_TUR_update_imperial_crisis = yes
        add_political_power = 50
        country_event = { id = nww_tur_council.4 days = 1 }''',
        'is_subject = no NOT = { has_country_flag = NWW_TUR_council_negotiation_active } '
        + ' '.join(f'custom_trigger_tooltip = {{ tooltip = {flag} has_country_flag = {flag} }}' for flag in ACCORDS))
    parents('NWW_TUR_imperial_compact', ['tur_polos', 'TUR_dux_national',
            'NWW_TUR_ottoman_bourgeoisie', 'NWW_TUR_agrarian_reform'])
    update('TUR_proper_stoper', x='6', y='6')
    parents('TUR_proper_stoper', ['TUR_dux_national', 'tur_polos'], ['NWW_TUR_imperial_compact'])
    update('TUR_store_eng', x='4', y='6')
    update('TUR_kosa_smerti', x='6', y='7', icon='GFX_focus_TUR_reconfigure_turkish_foreign_policy',
           available='''is_subject = no
            custom_trigger_tooltip = { tooltip = NWW_TUR_modern_war_ministry_tt
                has_completed_focus = TUR_Army_3 }''',
           completion_reward='army_experience = 20 add_war_support = 0.05')
    parents('TUR_kosa_smerti', ['TUR_proper_stoper'])
    field(by_id['TUR_kosa_smerti'], 'cancel_if_invalid', 'yes')
    field(by_id['TUR_kosa_smerti'], 'continue_if_invalid', 'no')
    add('NWW_TUR_rumelian_logistics', 4, 7, 'GFX_goal_generic_construct_infrastructure',
        'TUR_proper_stoper', '''
        797 = { if = { limit = { is_owned_and_controlled_by = ROOT }
            add_building_construction = { type = infrastructure level = 1 instant_build = yes }
            add_building_construction = { type = air_base level = 1 instant_build = yes }
        } }
        add_ideas = TUR_supply_reform army_experience = 10''')
    add('NWW_TUR_war_industry_program', 8, 7, 'GFX_goal_generic_construct_mil_factory',
        'TUR_proper_stoper', guarded_factory(49, 'arms_factory') + '\nadd_ideas = NWW_TUR_war_industry')

    update('TUR_war_with_bulgaria', x='6', y='8')
    parents('TUR_war_with_bulgaria', ['TUR_kosa_smerti'], ['NWW_TUR_rumelian_logistics'])
    update('afg_bolgi', x='6', y='9', icon='GFX_focus_BUL_bulgarian_administration_of_the_balkans',
           available=owned(CAMPAIGNS['BUL'][1]), completion_reward=guarded_factory(48, 'industrial_complex') + '''
            set_country_flag = NWW_TUR_bulgaria_settled
            ''' + ' '.join(f'{sid} = {{ add_compliance = 10 }}' for sid in CAMPAIGNS['BUL'][1]))
    update('TUR_snova_copi', x='6', y='10')
    add('NWW_TUR_greek_settlement', 6, 11, 'GFX_focus_BUL_bulgarian_administration_of_the_balkans',
        'TUR_snova_copi', '''set_country_flag = NWW_TUR_greece_settled add_stability = 0.05
            ''' + ' '.join(f'{sid} = {{ add_compliance = 10 }}' for sid in CAMPAIGNS['GRE'][1]),
        owned(CAMPAIGNS['GRE'][1]))
    all_balkans = sorted({sid for _, states in CAMPAIGNS.values() for sid in states})
    add('NWW_TUR_balkan_mandate', 6, 12, 'GFX_focus_generic_balkans_focus',
        'NWW_TUR_greek_settlement', '''add_war_support = 0.05 add_command_power = 20
        ''' + ' '.join(f'add_state_claim = {sid}' for sid in all_balkans),
        'is_subject = no ' + owned(CAMPAIGNS['BUL'][1] + CAMPAIGNS['GRE'][1]))
    for tag, x, icon in [('YUG', 2, 'GFX_focus_generic_balkans_focus'),
                         ('ALB', 6, 'GFX_focus_generic_balkan_diplomacy'),
                         ('ROM', 10, 'GFX_focus_generic_attack_romania'),
                         ('CRO', 14, 'GFX_focus_generic_balkans_focus')]:
        add(CAMPAIGNS[tag][0], x, 13, icon, 'NWW_TUR_balkan_mandate', '')
    add('NWW_TUR_rumelian_governorates', 6, 14,
        'GFX_focus_BUL_bulgarian_administration_of_the_balkans', 'NWW_TUR_balkan_mandate',
        'add_ideas = NWW_TUR_balkan_administration add_stability = 0.05',
        owned(CAMPAIGNS['BUL'][1] + CAMPAIGNS['GRE'][1]))

    for tag, (fid, states) in CAMPAIGNS.items():
        update(fid, available=f'''is_subject = no {tag} = {{ exists = yes }}
            NOT = {{ is_ally_with = {tag} }} NOT = {{ has_war_with = {tag} }}
            has_war_support > 0.30 date > 1937.1.1''',
            bypass=owned(states), completion_reward=f'''
            custom_effect_tooltip = NWW_TUR_{tag}_campaign_tt
            hidden_effect = {{ nww_TUR_prepare_{tag.lower()}_campaign = yes }}''')
        field(by_id[fid], 'cancel_if_invalid', 'yes')
        field(by_id[fid], 'continue_if_invalid', 'no')
    update('TUR_war_with_bulgaria', icon='GFX_focus_generic_attack_bulgaria')
    update('TUR_snova_copi', icon='GFX_focus_generic_attack_greece')
    field(one(tree, 'continuous_focus_position'), 'y', '2800')
    write('common/national_focus/TUR_focuses.txt', document)

    # Keep the original army/industry helpers intact. One crisis spirit changes tier.
    effect_path = ROOT / 'common/scripted_effects/TUR_effects.txt'
    owned_helpers = {'nww_TUR_update_imperial_crisis', 'nww_TUR_select_ai_path'} | {
        f'nww_TUR_prepare_{tag.lower()}_campaign' for tag in CAMPAIGNS}
    effects = [(k, v, o) for k, v, o in read(effect_path) if k not in owned_helpers]
    crises = ['NWW_TUR_imperial_crisis', 'NWW_TUR_imperial_crisis_1', 'NWW_TUR_imperial_crisis_2']
    remove = ' '.join(f'if = {{ limit = {{ has_idea = {idea} }} remove_ideas = {idea} }}' for idea in crises)
    two_of_three = 'OR = { ' + ' '.join('AND = { ' + ' '.join('has_country_flag = ' + f for f in pair) + ' }'
                        for pair in ((ACCORDS[0], ACCORDS[1]), (ACCORDS[0], ACCORDS[2]), (ACCORDS[1], ACCORDS[2]))) + ' }'
    at_least_one = 'OR = { ' + ' '.join('has_country_flag = ' + f for f in ACCORDS) + ' }'
    effects += block(f'''nww_TUR_update_imperial_crisis = {{
        if = {{ limit = {{ has_country_flag = NWW_TUR_council_settled }}
            {remove}
            if = {{ limit = {{ NOT = {{ has_idea = NWW_TUR_imperial_compact }} }} add_ideas = NWW_TUR_imperial_compact }}
        }}
        else_if = {{ limit = {{ {two_of_three} NOT = {{ has_idea = NWW_TUR_imperial_crisis_2 }} }}
            {remove} add_ideas = NWW_TUR_imperial_crisis_2 }}
        else_if = {{ limit = {{ {at_least_one} NOT = {{ {two_of_three} }} NOT = {{ has_idea = NWW_TUR_imperial_crisis_1 }} }}
            {remove} add_ideas = NWW_TUR_imperial_crisis_1 }}
        else_if = {{ limit = {{ NOT = {{ {at_least_one} }} NOT = {{ has_idea = NWW_TUR_imperial_crisis }} }}
            {remove} add_ideas = NWW_TUR_imperial_crisis }}
    }}''')
    for tag, (fid, states) in CAMPAIGNS.items():
        effects += block(f'''nww_TUR_prepare_{tag.lower()}_campaign = {{
            if = {{ limit = {{ tag = TUR is_subject = no {tag} = {{ exists = yes }} NOT = {{ is_ally_with = {tag} }} }}
                {' '.join('add_state_claim = ' + str(sid) for sid in states)}
                {tag} = {{ every_owned_state = {{ add_claim_by = ROOT }} }}
                if = {{ limit = {{ NOT = {{ has_war_with = {tag} }} NOT = {{ has_wargoal_against = {tag} }} }}
                    create_wargoal = {{ type = annex_everything target = {tag} }} }}
            }}
        }}''')
    random_flags = [flag for _, flags in RULE_PATHS.values() for flag in flags]
    effects += block('''nww_TUR_select_ai_path = { if = { limit = {
        is_ai = yes nww_TUR_random_ai_mode = yes NOT = { OR = {
        ''' + ' '.join('has_country_flag = ' + flag for flag in random_flags) + ''' } } }
        random_list = {
            25 = { set_country_flag = TUR_AI_RANDOM_OTTOMAN }
            15 = { set_country_flag = TUR_AI_RANDOM_ALT_KEMALIST }
            20 = { set_country_flag = TUR_AI_RANDOM_DEMOCRATIC }
            20 = { set_country_flag = TUR_AI_RANDOM_COMMUNISM }
            20 = { set_country_flag = TUR_AI_RANDOM_FASCISM }
        }
    } }''')
    write('common/scripted_effects/TUR_effects.txt', effects)

    rules = lambda options: ' '.join(f'has_game_rule = {{ rule = TUR_ai_behavior option = {option} }}' for option in options)
    explicit_options = [option for options, _ in RULE_PATHS.values() for option in options]
    triggers = block('''nww_TUR_random_ai_mode = { OR = {
        has_game_rule = { rule = TUR_ai_behavior option = RANDOM }
        AND = { is_historical_focus_on = no NOT = { OR = { ''' + rules(explicit_options) + ''' } } }
    } }''')
    for path, (options, flags) in RULE_PATHS.items():
        default_historical = ('''AND = { is_historical_focus_on = yes NOT = { OR = {
            ''' + rules(explicit_options + ['RANDOM']) + ''' } } }''') if path == 'historical' else ''
        triggers += block(f'''nww_TUR_ai_{path}_path = {{ OR = {{
            {rules(options)} {default_historical}
            AND = {{ nww_TUR_random_ai_mode = yes OR = {{
                {' '.join('has_country_flag = ' + flag for flag in flags)} }} }}
        }} }}''')
    triggers += block('''nww_TUR_ai_neutrality_path = { OR = {
        nww_TUR_ai_historical_path = yes nww_TUR_ai_peaceful_path = yes } }''')
    write('common/scripted_triggers/TUR_triggers.txt', triggers)

    # Only actual Ottoman victories can annex opponents; startup never annexes.
    capitulations = []
    renewals = []
    for tag, (fid, _) in CAMPAIGNS.items():
        capitulations += block(f'''if = {{ limit = {{ tag = {tag} exists = yes
            FROM = {{ tag = TUR has_focus_tree = turkish_focus has_completed_focus = {fid} }} }}
            FROM = {{ annex_country = {{ target = ROOT transfer_troops = no }} }} }}''')
        renewals += block(f'''if = {{ limit = {{ has_completed_focus = {fid} }} nww_TUR_prepare_{tag.lower()}_campaign = yes }}''')
    maintenance = block('''if = { limit = { has_focus_tree = turkish_focus }
        nww_TUR_select_ai_path = yes nww_TUR_update_imperial_crisis = yes }''')
    # Read/rebuild the maintenance block once rather than running new history effects in saves.
    maintenance[0][1].extend(renewals)
    write('common/on_actions/TUR_on_actions.txt', [('on_actions', [
        ('on_capitulation', [('effect', capitulations, '=')], '='),
        ('on_startup', [('effect', [('TUR', maintenance, '=')], '=')], '='),
        ('on_daily_TUR', [('effect', maintenance, '=')], '=')], '=')])
    history_path = ROOT / 'history/countries/TUR - Turkey.txt'
    history = read(history_path)
    if not any(v == 'NWW_TUR_imperial_crisis' for group in values(history, 'add_ideas') for k, v, o in group):
        history.append(('add_ideas', [(None, 'NWW_TUR_imperial_crisis', None)], '='))
    write('history/countries/TUR - Turkey.txt', history)

    # Native Kemalist/WWI scripts point at hidden compatibility focuses in NWW.
    for native in ('TUR_historical_strategy_plan.txt', 'TUR_alternate_strategy_plan.txt'):
        (ROOT / 'common/ai_strategy_plans' / native).write_text(
            '# NWW Ottoman plans are defined in TUR_historical.txt and TUR_alternatives.txt.\n', encoding='utf-8')
    history_order = ['TUR_political_rw', 'TUR_not_fascism', 'NWW_TUR_sultans_shadow',
        'TUR_reform_the_army', 'TUR_prom', 'tur_bred', 'TUR_Army_1', 'TUR_Army_3',
        'tur_polos', 'TUR_new_economic', 'NWW_TUR_imperial_compact', 'TUR_proper_stoper',
        'TUR_Infantry_1', 'TUR_Doctrine_1', 'TUR_Artillery_1', 'TUR_kosa_smerti',
        'NWW_TUR_rumelian_logistics', 'NWW_TUR_war_industry_program', 'TUR_war_with_bulgaria',
        'afg_bolgi', 'TUR_snova_copi', 'NWW_TUR_greek_settlement', 'NWW_TUR_balkan_mandate',
        'NWW_TUR_albanian_campaign', 'NWW_TUR_serbian_campaign', 'NWW_TUR_romanian_campaign',
        'NWW_TUR_adriatic_campaign', 'NWW_TUR_rumelian_governorates']
    plan = f'''NWW_TUR_historical = {{ name = "NWW Ottoman historical plan" desc = ""
        allowed = {{ original_tag = TUR has_focus_tree = turkish_focus }}
        enable = {{ nww_TUR_ai_historical_path = yes }}
        abort = {{ is_subject = yes }}
        ai_national_focuses = {{ {' '.join(history_order)} }}
        weight = {{ factor = 100 }}
        focus_factors = {{ TUR_new_fascism = 0 TUR_new_dem = 0 TUR_new_communism = 0 TUR_store_eng = 0 TUR_Army_2 = 0 }}
    }}'''
    write('common/ai_strategy_plans/TUR_historical.txt', block(plan))
    alternatives = []
    for ideology, options, order in [
        ('democratic', ['TUR_DEMOCRATIC_KEMALIST', 'TUR_DEMOCRATIC_ALTERNATE'],
         ['TUR_political_rw', 'TUR_prom', 'TUR_new_dem', 'NWW_TUR_civil_assembly', 'NWW_TUR_federal_charter', 'NWW_TUR_ottoman_bourgeoisie', 'NWW_TUR_imperial_compact']),
        ('communism', ['COMMUNIST_TUR_AI', 'TUR_COMMUNISM_ALTERNATE'],
         ['TUR_political_rw', 'TUR_prom', 'TUR_new_communism', 'NWW_TUR_workers_congress', 'NWW_TUR_workers_union', 'NWW_TUR_agrarian_reform', 'NWW_TUR_imperial_compact']),
        ('fascism', ['FASCISM_TUR_AI', 'TUR_FASCISM_ALTERNATE'],
         ['TUR_political_rw', 'TUR_prom', 'TUR_new_fascism', 'TUR_set_capital', 'TUR_dux_national', 'NWW_TUR_imperial_compact', 'TUR_reform_the_army', 'TUR_Army_1', 'TUR_Army_3', 'TUR_proper_stoper', 'TUR_kosa_smerti', 'NWW_TUR_rumelian_logistics', 'TUR_war_with_bulgaria', 'afg_bolgi', 'TUR_snova_copi']),
        ('neutrality', ['ALTERNATE_KEMALIST', 'BALKAN_ENTENTE'],
         ['TUR_political_rw', 'TUR_not_fascism', 'NWW_TUR_sultans_shadow', 'tur_bred', 'tur_polos', 'NWW_TUR_imperial_compact', 'TUR_store_eng'])]:
        path = 'peaceful' if ideology == 'neutrality' else ideology
        others = [fid for fid in ('TUR_new_fascism', 'TUR_new_dem', 'TUR_new_communism', 'TUR_not_fascism')
                  if fid != {'democratic': 'TUR_new_dem', 'communism': 'TUR_new_communism',
                             'fascism': 'TUR_new_fascism', 'neutrality': 'TUR_not_fascism'}[ideology]]
        alternatives += block(f'''NWW_TUR_{ideology}_alternative = {{ name = "NWW TUR {ideology}" desc = ""
            allowed = {{ original_tag = TUR has_focus_tree = turkish_focus }}
            enable = {{ nww_TUR_ai_{path}_path = yes }} abort = {{ is_subject = yes }}
            ai_national_focuses = {{ {' '.join(order)} }} weight = {{ factor = 100 }}
            focus_factors = {{ {' '.join(fid + ' = 0' for fid in others)} }}
        }}''')
    write('common/ai_strategy_plans/TUR_alternatives.txt', alternatives)
    strategies = []
    peace = []
    for tag, (fid, _) in CAMPAIGNS.items():
        strategies += block(f'''NWW_TUR_{tag}_campaign = {{
            enable = {{ tag = TUR has_focus_tree = turkish_focus is_subject = no
                has_completed_focus = {fid} {tag} = {{ exists = yes }}
                NOT = {{ is_ally_with = {tag} }} NOT = {{ has_war_with = {tag} }}
                has_wargoal_against = {tag} can_declare_war_on = {tag} }}
            abort_when_not_enabled = yes
            ai_strategy = {{ type = prepare_for_war id = {tag} value = 200 }}
            ai_strategy = {{ type = conquer id = {tag} value = 300 }}
            ai_strategy = {{ type = declare_war id = {tag} value = 300 }}
        }}''')
        peace += block(f'''NWW_TUR_{tag}_full_conquest = {{ peace_action_type = take_states
            enable = {{ ROOT = {{ tag = TUR has_completed_focus = {fid} }}
                FROM = {{ tag = TUR }} FROM.FROM = {{ original_tag = {tag} }} }} ai_desire = 1000 }}''')
    write('common/ai_strategy/TUR_balkans.txt', strategies)
    write('common/peace_conference/ai_peace/TUR_peace.txt', [('peace_ai_desires', peace, '=')])

    manifest_path = ROOT / 'docs/legacy_import.json'
    manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
    manifest['countries']['TUR']['focus_ids'] = list(by_id)
    manifest['countries']['TUR']['total'] = len(by_id)
    added = ['common/on_actions/TUR_on_actions.txt', 'common/ai_strategy/TUR_balkans.txt',
             'common/ai_strategy_plans/TUR_historical.txt', 'common/ai_strategy_plans/TUR_alternatives.txt',
             'common/scripted_triggers/TUR_triggers.txt',
             'common/peace_conference/ai_peace/TUR_peace.txt']
    manifest['content_files'] = sorted(set(manifest['content_files'] + added))
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    (ROOT / 'docs/TUR_balkan_objectives.json').write_text(json.dumps(CAMPAIGNS, indent=2) + '\n', encoding='utf-8')
    localize()
    print(f'TUR: {len(by_id)} focuses; six staged Balkan campaigns; council and historical AI wired.')


if __name__ == '__main__':
    main()
