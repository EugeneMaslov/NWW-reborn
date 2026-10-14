"""Replace four-way succession collapse with one strongest-opposition duel."""
from patch_mkn_overhaul import ROOT, save, put, block
from hoi4_script import read, one, values, dump

PARTIES = {'fascism':'MKN_military_takes_charge','democratic':'MKN_triumph_of_free_soviets','neutrality':'MKN_peasant_delegates','communism':'MKN_emergency_revkom'}

def main():
    path='common/scripted_effects/MKN_effects.txt'
    doc=read(ROOT/path)
    script='''
        set_country_flag = MKN_collapse_started
        set_country_flag = mkn_collapsed
        set_country_flag = MKN_duel_participant
        set_country_flag = MKN_collapse_participant
        set_country_flag = MKN_crisis_enabled
        set_country_flag = mkn_ukr_frontier_concluded
        set_country_flag = mkn_ukr_frontier_aborted
        clr_country_flag = mkn_frontier_year_running
        clr_country_flag = mkn_ukr_border_battle_active
        remove_mission = MKN_passive_escalation_drift
        remove_mission = MKN_frontier_year_countdown_mission
        remove_mission = MKN_civil_war_timer_mission
        clr_country_flag = MKN_crisis_active
        clr_country_flag = mkn_ukr_war_pending
        clr_country_flag = mkn_ukr_pact_pending
        mkn_ukr_stop_border_battle = yes
        MKN_dismantle_bop = yes
        save_global_event_target_as = MKN_duel_incumbent
        set_variable = { MKN_duel_best_support = -1 }
    '''
    # Strict > makes ties deterministic in declared party order. Ruling party
    # cannot challenge itself, including when its support is below opposition.
    for index,party in enumerate(PARTIES):
        script+=f'''if = {{ limit = {{ NOT = {{ has_government = {party} }}
            check_variable = {{ var = party_popularity@{party} value = MKN_duel_best_support compare = greater_than }} }}
            set_variable = {{ MKN_duel_best_support = party_popularity@{party} }}
            set_variable = {{ MKN_duel_challenger = {index} }}
        }}'''
    for index,party in enumerate(PARTIES):
        script+=f'''if = {{ limit = {{ check_variable = {{ MKN_duel_challenger = {index} }} }}
            start_civil_war = {{ ideology = {party} size = 0.50 keep_all_characters = yes
                set_country_flag = MKN_crisis_enabled
                set_country_flag = MKN_collapse_started
                set_country_flag = mkn_collapsed
                set_country_flag = MKN_duel_participant
                set_country_flag = MKN_collapse_participant
                set_country_flag = mkn_ukr_frontier_concluded
                load_focus_tree = {{ tree = MKN_focus keep_completed = yes }}
                MKN_install_{party}_successor = yes
                set_politics = {{ ruling_party = {party} elections_allowed = no }}
                save_global_event_target_as = MKN_duel_challenger
            }}
        }}'''
    script+='''if = { limit = { is_ai = no } set_country_flag = MKN_duel_choice_pending }
        set_country_flag = MKN_duel_started'''
    # Preserve public helper ID used by events and old saves.
    put(doc,'MKN_execute_four_way_collapse',block(script))
    recovery='''set_country_flag = MKN_duel_recovered
        clr_country_flag = mkn_collapsed
        clr_country_flag = MKN_collapse_started
        clr_country_flag = MKN_duel_choice_pending
        clr_country_flag = MKN_collapse_participant
        clr_country_flag = MKN_crisis_legacy_settled
        remove_mission = MKN_soviet_intervention_mission
        MKN_resolve_succession_crisis = yes
        set_country_flag = MKN_crisis_enabled
        set_global_flag = MKN_collapse_reunified
        load_focus_tree = { tree = MKN_focus keep_completed = yes }
    '''
    for party,fid in PARTIES.items():
        pops=' '.join(f'{p} = {100 if p == party else 0}' for p in PARTIES)
        reset=' '.join(f'uncomplete_national_focus = {{ focus = {other} uncomplete_children = yes refund_political_power = no }}' for p,other in PARTIES.items() if p != party)
        recovery+=f'''if = {{ limit = {{ has_government = {party} }}
            {reset}
            set_popularities = {{ {pops} }}
            if = {{ limit = {{ NOT = {{ has_completed_focus = MKN_departure_of_batko }} }} complete_national_focus = MKN_departure_of_batko }}
            if = {{ limit = {{ NOT = {{ has_completed_focus = {fid} }} }} complete_national_focus = {fid} }}
        }}'''
    recovery+='nww_mkn_rebuild_industry = yes nww_mkn_rebuild_services = yes mark_focus_tree_layout_dirty = yes'
    put(doc,'MKN_recover_duel_winner',block(recovery))
    save(path,doc)
    save('common/decisions/categories/MKN_duel_categories.txt',block('''MKN_duel_category = {
        icon = GFX_decision_category_SOV_civil_war allowed = { original_tag = MKN }
        visible = { has_country_flag = MKN_duel_choice_pending NOT = { has_country_flag = MKN_duel_recovered } }
    }'''))
    save('common/decisions/MKN_duel_decisions.txt',block('''MKN_duel_category = {
        MKN_support_established_order = {
            icon = generic_army_support cost = 0 fire_only_once = yes
            visible = { has_country_flag = MKN_duel_choice_pending }
            available = { has_country_flag = MKN_duel_choice_pending }
            complete_effect = { clr_country_flag = MKN_duel_choice_pending set_country_flag = MKN_duel_support_incumbent }
            ai_will_do = { base = 0 }
        }
        MKN_rally_to_challenger = {
            icon = generic_army_support cost = 0 fire_only_once = yes
            visible = { has_country_flag = MKN_duel_choice_pending }
            available = { has_country_flag = MKN_duel_choice_pending event_target:MKN_duel_challenger = { exists = yes has_country_flag = MKN_duel_participant } }
            complete_effect = {
                clr_country_flag = MKN_duel_choice_pending set_country_flag = MKN_duel_support_rebels
                event_target:MKN_duel_challenger = { change_tag_from = ROOT }
            }
            ai_will_do = { base = 0 }
        }
    }'''))
    save('common/on_actions/MKN_duel_on_actions.txt',block('''on_actions = {
        on_daily = { effect = { every_country = {
            limit = { original_tag = MKN has_country_flag = MKN_duel_participant
                NOT = { has_country_flag = MKN_duel_recovered }
                check_variable = { num_owned_states > 0 }
                NOT = { any_other_country = { original_tag = MKN has_country_flag = MKN_duel_participant check_variable = { num_owned_states > 0 } } }
                NOT = { has_civil_war = yes }
            }
            MKN_recover_duel_winner = yes
        } } }
    }'''))
    # Old four-way intervention maintenance is retained for old saves only.
    path='common/on_actions/MKN_intervention_on_actions.txt'
    doc=read(ROOT/path)
    limit=one(one(one(one(one(doc,'on_actions'),'on_daily'),'effect'),'every_country'),'limit')
    if not any(one(v,'has_country_flag')=='MKN_duel_participant' for v in values(limit,'NOT')):
        limit.extend(block('NOT = { has_country_flag = MKN_duel_participant }'))
    save(path,doc)

if __name__=='__main__':
    main()
