from patch_mkn_overhaul import ROOT, save, put, block
from hoi4_script import read, one, values, walk, dump

def main():
    path='common/scripted_triggers/MKN_ukr_border_triggers.txt';doc=read(ROOT/path)
    put(doc,'MKN_valid_frontier_target',block('''
        NOT = { state = 202 }
        has_border_war = no
        any_neighbor_state = { is_owned_and_controlled_by = MKN has_border_war = no }
        OR = {
            is_owned_and_controlled_by = UKR
            AND = { is_owned_and_controlled_by = SOV
                OR = { state = 227 state = 221 state = 137 }
                MKN = { has_completed_focus = MKN_donbas_miners_agitation NOT = { is_ally_with = SOV } NOT = { has_non_aggression_pact_with = SOV } }
            }
        }
    '''))
    # Root-country target scopes may be a hostile country; the focus gate uses
    # explicit MKN scope rather than assuming ROOT still denotes the taker.
    save(path,doc)
    path='common/decisions/MKN_ukr_border_decisions.txt';doc=read(ROOT/path)
    category=one(doc,'MKN_ukr_border_category');battle=one(category,'mkn_launch_border_battle')
    put(battle,'target_trigger',block('FROM = { MKN_valid_frontier_target = yes }'))
    available=one(battle,'available')
    put(available,'FROM',block('MKN_valid_frontier_target = yes owner = { check_variable = { num_owned_states > 1 } }'))
    available[:]=[n for n in available if n[0]!='UKR']
    completion=one(battle,'complete_effect')
    # Recheck the offer before starting the battle; ownership can change while
    # the decision window is open. No province/state IDs from the prompt used.
    if not (len(completion)==1 and completion[0][0]=='if' and one(one(completion[0][1],'limit'),'FROM')):
        put(battle,'complete_effect',block('if = { limit = { FROM = { MKN_valid_frontier_target = yes } mkn_ukr_frontier_action_available = yes } '+dump(completion)+' }'))
    drift=one(category,'MKN_passive_escalation_drift')
    # Explicitly remove the expired mission before reactivation: no 31-day gap.
    put(drift,'timeout_effect',block('''if = { limit = { NOT = { has_country_flag = mkn_ukr_frontier_concluded } }
        add_to_variable = { mkn_ukr_escalation_level = 1 }
        clamp_variable = { var = mkn_ukr_escalation_level min = 1 max = 5 }
        mkn_ukr_check_escalation = yes
        remove_mission = MKN_passive_escalation_drift
        activate_mission = MKN_passive_escalation_drift
    }'''))
    save(path,doc)
    path='common/scripted_effects/MKN_ukr_border_effects.txt';doc=read(ROOT/path)
    victory=one(doc,'mkn_ukr_border_victory');cond=one(victory,'if');limit=one(cond,'limit')
    put(limit,'FROM.FROM',block('OR = { tag = UKR tag = SOV }'))
    put(limit,'FROM.FROM.FROM',block('''NOT = { state = 202 }
        OR = {
            AND = { FROM.FROM = { tag = UKR } OR = { is_owned_by = UKR is_owned_by = MKN } }
            AND = { FROM.FROM = { tag = SOV } OR = { is_owned_by = SOV is_owned_by = MKN }
                OR = { state = 227 state = 221 state = 137 }
                MKN = { has_completed_focus = MKN_donbas_miners_agitation }
            }
        }'''))
    defeat=one(doc,'mkn_ukr_border_defeat');cond=one(defeat,'if');put(one(cond,'limit'),'FROM.FROM',block('OR = { tag = UKR tag = SOV }'))
    for k,v,o in list(walk(cond)):
        if isinstance(v,list):
            for i,(key,value,op) in enumerate(v):
                if key=='transfer_state_to':v[i]=(key,'FROM.FROM',op)
    stop=one(doc,'mkn_ukr_stop_border_battle')
    for k,v,o in list(walk(stop)):
        if isinstance(v,list):
            for i,(key,value,op) in enumerate(v):
                if key=='has_border_war_with' and value=='UKR':v[i]=('OR',block('has_border_war_with = UKR has_border_war_with = SOV'),'=')
                if key=='is_owned_by' and value=='UKR':v[i]=('OR',block('is_owned_by = UKR is_owned_by = SOV'),'=')
    put(doc,'MKN_annex_encircled_ukraine',block('''
        UKR = { every_owned_state = { set_state_flag = MKN_kyiv_capitulation_claim } }
        annex_country = { target = UKR transfer_troops = no }
        every_owned_state = { limit = { has_state_flag = MKN_kyiv_capitulation_claim }
            add_core_of = ROOT clr_state_flag = MKN_kyiv_capitulation_claim
        }
        set_country_flag = mkn_ukr_frontier_concluded
        clr_country_flag = mkn_ukr_war_pending
        remove_mission = MKN_passive_escalation_drift
        remove_mission = MKN_frontier_year_countdown_mission
        mkn_ukr_stop_border_battle = yes
    '''))
    save(path,doc)
    path='events/MKN_ukr_border_events.txt';doc=read(ROOT/path)
    if not any(one(e,'id')=='mkn_ukr_border.30' for e in values(doc,'country_event')):
        doc.extend(block('''country_event = {
            id = mkn_ukr_border.30 title = mkn_ukr_border.30.t desc = mkn_ukr_border.30.d
            picture = GFX_report_event_spain_civil_war_soldiers is_triggered_only = yes
            trigger = { original_tag = MKN UKR = { exists = yes } has_war_with = UKR
                202 = { all_neighbor_state = { OR = { is_controlled_by = ROOT NOT = { is_owned_by = UKR } } } }
            }
            immediate = { MKN_annex_encircled_ukraine = yes }
            option = { name = mkn_ukr_border.30.a }
        }'''))
    save(path,doc)
    save('common/on_actions/MKN_kyiv_on_actions.txt',block('''on_actions = {
        on_daily = { effect = { every_country = {
            limit = { original_tag = MKN UKR = { exists = yes } has_war_with = UKR
                202 = { all_neighbor_state = { OR = { is_controlled_by = ROOT NOT = { is_owned_by = UKR } } } }
            }
            country_event = { id = mkn_ukr_border.30 }
        } } }
    }'''))
    path='events/nww_ukr_diplomacy.txt';doc=read(ROOT/path)
    event=next(e for e in values(doc,'country_event') if one(e,'id')=='ukr.50');accept=values(event,'option')[0]
    put(one(accept,'trigger'),'203',block('is_owned_and_controlled_by = UKR'))
    put(accept,'203',block('transfer_state_to = ROOT add_core_of = ROOT set_state_flag = mkn_ukr_integrated_frontier_state'))
    save(path,doc)

if __name__=='__main__':main()
