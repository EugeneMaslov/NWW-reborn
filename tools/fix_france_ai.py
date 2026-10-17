"""Apply the France AI lifecycle fixes without regenerating unrelated content/art."""
import json
from pathlib import Path

from hoi4_script import dump, one, parse, read, values

ROOT = Path(__file__).resolve().parents[1]
REGIONS = [item[0] for item in json.loads((ROOT / 'docs/FRA_content.json').read_text(encoding='utf-8'))['regions']]


def save(relative, doc):
    (ROOT / relative).write_text(dump(doc) + '\n', encoding='utf-8', newline='\n')


def setv(node, key, value):
    node[:] = [entry for entry in node if entry[0] != key]
    node.append((key, value, '='))


def modifier(body):
    return ('modifier', parse(body), '=')


def apply_fixes():
    # Prevent the 1937/38 crisis from preceding the AI's first colonial institution.
    path = 'common/ai_strategy_plans/FRA_plans.txt'
    plans = read(ROOT / path)
    colonial = ['overseas_register', 'overseas_conference', 'representation', 'colonial_schools',
                'overseas_credit', 'overseas_compact']
    for name, plan, _ in plans:
        route = name.removeprefix('FRA_nww_plan_')
        selected = ['FRA_nww_' + fid for fid in colonial]
        if route == 'COUNCILS':
            selected[2] = 'FRA_nww_selfdetermination'
        old = [fid for _, fid, _ in one(plan, 'ai_national_focuses') if fid not in
               {'FRA_nww_' + x for x in colonial + ['selfdetermination', 'extraction']}]
        # The common opening stays first. Policy is ready at day 315, schools at 385.
        order = old[:3] + selected[:4] + old[3:]
        order += selected[4:]
        setv(plan, 'ai_national_focuses', [(None, fid, None) for fid in order])
        factors = one(plan, 'focus_factors')
        for fid in ['representation', 'selfdetermination', 'extraction']:
            if 'FRA_nww_' + fid != selected[2]:
                setv(factors, 'FRA_nww_' + fid, '0')
    save(path, plans)

    pending = ' '.join(f'AND = {{ FRA_holds_{r} = yes NOT = {{ has_country_flag = FRA_{r}_represented }} }}'
                       for r in REGIONS)
    triggers = parse(f'''
    FRA_ai_overseas_talks_pending = {{ has_country_flag = FRA_policy_representation OR = {{ {pending} }} }}
    FRA_ai_historical_defensive = {{
      has_game_rule = {{ rule = FRA_ai_behavior option = DEFAULT }} is_historical_focus_on = yes
    }}
    FRA_ai_ready_for_GER = {{
      NOT = {{ FRA_ai_historical_defensive = yes }}
      date > 1939.12.31 has_war = no has_capitulated = no has_civil_war = no is_subject = no
      surrender_progress < 0.05 has_stability > 0.50 has_war_support > 0.50
      has_completed_focus = FRA_nww_signals_supply has_completed_focus = FRA_nww_officer_corps
      has_completed_focus = FRA_nww_rhine_preparations
      GER = {{ exists = yes is_subject = no NOT = {{ is_ally_with = FRA }}
        strength_ratio = {{ tag = FRA ratio < 0.80 }}
        OR = {{ is_in_faction = no NOT = {{ any_other_country = {{ is_in_faction_with = PREV }} }} }}
      }}
      NOT = {{ any_other_country = {{ has_guaranteed = GER OR = {{ is_major = yes is_in_faction = yes is_subject = yes }} }} }}
    }}
    FRA_ai_can_confront_GER = {{ OR = {{ is_ai = no FRA_ai_ready_for_GER = yes }} }}
    FRA_ai_GER_front_advantage = {{
      GER = {{ exists = yes strength_ratio = {{ tag = FRA ratio < 0.80 }} }}
    }}
    FRA_ai_unsafe_GER_declaration = {{
      FRA = {{ is_ai = yes has_focus_tree = french_focus NOT = {{ FRA_ai_ready_for_GER = yes }} }}
      FROM = {{ tag = GER }}
    }}
    ''')
    save('common/scripted_triggers/FRA_ai_triggers.txt', triggers)
    save('common/scripted_effects/FRA_ai_effects.txt', parse('''
    FRA_install_ai_campaign_guard = {
      remove_relation_rule_override = { trigger = FRA_ai_unsafe_GER_declaration can_not_declare_war = yes }
      add_relation_rule_override = { trigger = FRA_ai_unsafe_GER_declaration usage_desc = FRA_ai_GER_restraint_tt can_not_declare_war = yes }
      set_country_flag = FRA_ai_campaign_guard_installed
    }
    '''))
    save('common/on_actions/FRA_ai_on_actions.txt', parse('''
    on_actions = {
      on_startup = { effect = { FRA = { if = { limit = { exists = yes has_focus_tree = french_focus } FRA_install_ai_campaign_guard = yes } } } }
      on_daily_FRA = { effect = { if = { limit = { has_focus_tree = french_focus NOT = { has_country_flag = FRA_ai_campaign_guard_installed } } FRA_install_ai_campaign_guard = yes } } }
    }
    '''))
    save('common/ai_strategy/FRA_nww_strategy.txt', parse('''
    FRA_nww_GER_restraint = {
      allowed = { original_tag = FRA }
      enable = { has_focus_tree = french_focus NOT = { FRA_ai_ready_for_GER = yes } }
      abort_when_not_enabled = yes
      ai_strategy = { type = declare_war id = GER value = -1000 }
      ai_strategy = { type = antagonize id = GER value = -1000 }
    }
    FRA_nww_fund_overseas_settlement = {
      allowed = { original_tag = FRA }
      enable = { has_focus_tree = french_focus FRA_ai_overseas_talks_pending = yes }
      abort_when_not_enabled = yes
      ai_strategy = { type = pp_spend_priority id = decision value = 100 }
      ai_strategy = { type = pp_spend_priority id = idea value = -100 }
      ai_strategy = { type = pp_spend_priority id = relation value = -100 }
    }
    FRA_nww_careful_GER_front = {
      allowed = { original_tag = FRA }
      enable = { is_ai = yes has_focus_tree = french_focus has_war_with = GER NOT = { FRA_ai_GER_front_advantage = yes } }
      abort_when_not_enabled = yes
      ai_strategy = { type = force_concentration_front_factor state = 28 state = 42 state = 51 state = 978 ratio = 0.95 value = -100 }
      ai_strategy = {
        type = front_control state = 28 state = 42 state = 51 state = 978 ratio = 0.8 priority = 100
        ordertype = front execution_type = careful execute_order = no manual_attack = no
      }
    }
    '''))

    path = 'common/decisions/FRA_decisions.txt'
    decisions = read(ROOT / path)
    by_id = {key: body for _, group, _ in decisions for key, body, _ in group}
    # Domestic campaigns must not consume every 35-day negotiation slot forever.
    campaign = {
        'republic': ('democratic', 'OR = { has_country_flag = FRA_ai_REPUBLIC has_country_flag = FRA_ai_SOCIAL }'),
        'royal': ('neutrality', 'has_country_flag = FRA_ai_MONARCHY'),
        'leagues': ('fascism', 'has_country_flag = FRA_ai_LEAGUES'),
        'workers': ('communism', 'OR = { has_country_flag = FRA_ai_COUNCILS has_country_flag = FRA_ai_PLAN }'),
        'army': ('neutrality', 'has_country_flag = FRA_ai_MILITARY'),
    }
    reserve = modifier('factor = 0 FRA_ai_overseas_talks_pending = yes '
                       'check_variable = { var = FRA_mandate value = 25 compare = greater_than_or_equals }')
    for name, body in by_id.items():
        ai = one(body, 'ai_will_do')
        if ai is not None and not name.startswith(('FRA_nww_negotiate_', 'FRA_nww_garrison_')):
            # Replace our own modifier on rerun; preserve other conditions.
            ai[:] = [entry for entry in ai if not (entry[0] == 'modifier' and
                       one(entry[1], 'FRA_ai_overseas_talks_pending') is not None)]
            ai.append(reserve)
    for short, (ideology, route) in campaign.items():
        setv(by_id['FRA_nww_campaign_' + short], 'ai_will_do',
             parse(f'factor = 10 modifier = {{ factor = 0 NOT = {{ {route} }} }} '
                   f'modifier = {{ factor = 0 NOT = {{ {ideology} < 0.40 }} }}') + [reserve])
    for short, threshold in [('coalition', 30), ('inquiry', 45), ('decree', 25)]:
        setv(by_id['FRA_nww_' + short], 'ai_will_do', parse(
            f'factor = {40 if short == "inquiry" else 2} modifier = {{ factor = 0 '
            f'check_variable = {{ var = FRA_mandate value = {threshold} compare = greater_than_or_equals }} }}') + [reserve])
    setv(by_id['FRA_nww_social_arbitration'], 'ai_will_do', parse(
        'factor = 5 modifier = { factor = 0 check_variable = { var = FRA_tension value = 50 compare = less_than } }') + [reserve])
    for index, region in enumerate(REGIONS):
        decision = by_id['FRA_nww_negotiate_' + region]
        setv(decision, 'available', parse('has_capitulated = no NOT = { has_country_flag = FRA_negotiation_busy } '
             'OR = { has_country_flag = FRA_policy_representation has_country_flag = FRA_policy_selfdetermination '
             'has_completed_focus = FRA_nww_overseas_compact }'))
        setv(decision, 'ai_will_do', parse(
            f'factor = 100 modifier = {{ factor = 0 NOT = {{ has_country_flag = FRA_policy_representation }} '
            'NOT = { has_country_flag = FRA_policy_selfdetermination } } '
            f'modifier = {{ factor = 0 has_country_flag = FRA_policy_selfdetermination FRA_can_release_{region} = no }} '
            f'modifier = {{ factor = 0 has_country_flag = FRA_policy_representation '
            f'check_variable = {{ var = FRA_{region}_pressure value = 80 compare = greater_than_or_equals }} '
            'NOT = { has_political_power > 99 } } '
            f'modifier = {{ factor = 0 has_country_flag = FRA_{region}_represented }} '
            f'modifier = {{ factor = 4 has_country_flag = FRA_{region}_crisis }}'))
        # Keep the same lock until the regional reply, not merely until the conference opens.
        setv(decision, 'remove_effect', parse(f'if = {{ limit = {{ FRA_holds_{region} = yes }} '
             f'country_event = {{ id = nww_fra.{100 + index} days = 1 }} }} '
             'else = { clr_country_flag = FRA_negotiation_busy }'))
    save(path, decisions)

    path = 'events/FRA_events.txt'
    events = read(ROOT / path)
    by_event = {one(event, 'id'): event for event in values(events, 'country_event')}
    for index, region in enumerate(REGIONS):
        event = by_event[f'nww_fra.{100 + index}']
        opts = values(event, 'option')
        representation, autonomy, independence, decline = opts
        pressure = f'FRA_{region}_pressure'
        setv(representation, 'trigger', parse(f'has_country_flag = FRA_policy_representation FRA_holds_{region} = yes '
             f'OR = {{ check_variable = {{ var = {pressure} value = 80 compare = less_than '
             f'tooltip = FRA_check_{region}_pressure_less_than_80_tt }} has_political_power > 49 }}'))
        setv(representation, 'ai_chance', parse('factor = 100'))
        guarantee = ('if', parse(f'limit = {{ check_variable = {{ var = {pressure} value = 80 compare = greater_than_or_equals }} }} '
             'custom_effect_tooltip = FRA_emergency_representation_tt add_political_power = -50 '
             f'add_to_variable = {{ {pressure} = -25 }} FRA_clamp_meters = yes'), '=')
        representation[:] = [entry for entry in representation if not (entry[0] == 'if' and
                                one(entry[1], 'custom_effect_tooltip') == 'FRA_emergency_representation_tt')]
        representation.insert(2, guarantee)
        setv(autonomy, 'ai_chance', parse('factor = 25 modifier = { factor = 0 has_country_flag = FRA_policy_representation }'))
        setv(decline, 'ai_chance', parse(f'factor = 1 modifier = {{ factor = 0 has_country_flag = FRA_policy_representation '
             f'FRA_holds_{region} = yes OR = {{ check_variable = {{ var = {pressure} value = 80 compare = less_than }} has_political_power > 49 }} }} '
             f'modifier = {{ factor = 0 has_country_flag = FRA_policy_selfdetermination FRA_can_release_{region} = yes }}'))
        if ('clr_country_flag', 'FRA_negotiation_busy', '=') not in decline:
            decline.append(('clr_country_flag', 'FRA_negotiation_busy', '='))
        reply = one(by_event[f'nww_fra.{140 + index}'], 'option')
        if ('clr_country_flag', 'FRA_negotiation_busy', '=') not in reply:
            reply.append(('clr_country_flag', 'FRA_negotiation_busy', '='))
    refusal = values(by_event['nww_fra.204'], 'option')[1]
    goal = one(refusal, 'FRA')
    condition = one(one(goal, 'if'), 'limit')
    if ('FRA_ai_can_confront_GER', 'yes', '=') not in condition:
        condition.append(('FRA_ai_can_confront_GER', 'yes', '='))
    save(path, events)

    path = 'common/national_focus/FRA_focuses.txt'
    doc = read(ROOT / path)
    focuses = {one(focus, 'id'): focus for focus in values(one(doc, 'focus_tree'), 'focus')}
    available = one(focuses['FRA_nww_rhine_ultimatum'], 'available')
    if ('FRA_ai_can_confront_GER', 'yes', '=') not in available:
        available.append(('FRA_ai_can_confront_GER', 'yes', '='))
    for short in ['rhine_stand', 'rhine_preparations', 'rhine_ultimatum']:
        setv(focuses['FRA_nww_' + short], 'ai_will_do', parse(
            'factor = 1 modifier = { factor = 0 FRA_ai_historical_defensive = yes }'))
    save(path, doc)
    strings = {
        'english': {
            'FRA_ai_GER_restraint_tt': 'France’s historical AI follows a defensive policy. Other AI routes require completed army reforms, preparations, domestic stability and a clear army advantage before declaring war on Germany.',
            'FRA_emergency_representation_tt': 'With regional pressure at 80 or more, emergency budget guarantees cost an additional 50 political power and reduce pressure by 25 before the regional reply.',
        },
        'russian': {
            'FRA_ai_GER_restraint_tt': 'Исторический ИИ Франции придерживается оборонительной политики. На других маршрутах для объявления войны Германии нужны армейские реформы, подготовка, внутренняя стабильность и явное превосходство сухопутных сил.',
            'FRA_emergency_representation_tt': 'При региональном давлении от 80 экстренные бюджетные гарантии стоят ещё 50 политвласти и снижают давление на 25 до ответа представителей.',
        },
    }
    for lang, entries in strings.items():
        path = ROOT / f'localisation/{lang}/FRA_ai_l_{lang}.yml'
        path.write_text('l_' + lang + ':\n' + '\n'.join(f' {k}:0 "{v}"' for k, v in entries.items()) + '\n',
                        encoding='utf-8-sig', newline='\n')
    print('Applied France colonial AI, serialized replies and German declaration safeguards.')


if __name__ == '__main__':
    apply_fixes()
