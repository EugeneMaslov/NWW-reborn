# MKN: готовые блоки файлов Вольных советов

Код уже применён к проекту. Ниже приведены полные новые определения и точные вставки в существующие файлы. Повторно вставлять их в текущую рабочую копию не нужно. Числовые эффекты уже усилены ×2; фактор ТНП дополнительно увеличен ×3: −15% → −45% (×9 от исходного задания).

Механики, адаптации, конкретные образцы DLC и ограничения статической проверки: [MKN_free_soviets.md](MKN_free_soviets.md).

## common/national_focus/MKN.txt — 12 новых фокусов

Вставить внутрь существующего `focus_tree`. У выборных инструкторов требование исходного фокуса находится в `available`, чтобы соединитель не пересекал научную подветку.

```pdx
focus = {
    id = MKN_ferrer_modern_schools
    icon = GFX_focus_MKN_ferrer_modern_schools
    x = 82
    y = 5
    cost = 5
    prerequisite = {
        focus = MKN_pact_of_free_communes
    }
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    available = {
        has_government = democratic
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    completion_reward = {
        add_ideas = MKN_ferrer_schools_idea
        if = {
            limit = {
                amount_research_slots < 4
            }
            add_research_slot = 2
        }
        else_if = {
            limit = {
                amount_research_slots < 5
            }
            add_research_slot = 1
        }
    }
    ai_will_do = {
        factor = 2
    }
}
focus = {
    id = MKN_sanctuary_of_free_thought
    icon = GFX_focus_MKN_sanctuary_of_free_thought
    x = 82
    y = 6
    cost = 5
    prerequisite = {
        focus = MKN_ferrer_modern_schools
    }
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    available = {
        has_government = democratic
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    completion_reward = {
        add_tech_bonus = {
            name = MKN_free_thought_research
            bonus = 1.0
            uses = 2
            category = electronics
            category = industry
        }
        every_country = {
            limit = {
                exists = yes
                NOT = {
                    tag = ROOT
                }
                OR = {
                    has_government = fascism
                    has_government = neutrality
                }
                capital_scope = {
                    is_on_continent = europe
                }
            }
            add_opinion_modifier = {
                target = ROOT
                modifier = MKN_sanctuary_hostility
            }
        }
    }
    ai_will_do = {
        factor = 2
    }
}
focus = {
    id = MKN_eradication_of_wage_labor
    icon = GFX_focus_MKN_eradication_of_wage_labor
    x = 82
    y = 7
    cost = 5
    prerequisite = {
        focus = MKN_sanctuary_of_free_thought
    }
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    available = {
        has_government = democratic
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    completion_reward = {
        add_ideas = MKN_labor_vouchers_idea
        add_timed_idea = {
            idea = MKN_voucher_transition_idea
            days = 120
        }
    }
    ai_will_do = {
        factor = 2
    }
}
focus = {
    id = MKN_imperative_mandate
    icon = GFX_focus_MKN_imperative_mandate
    x = 86
    y = 6
    cost = 5
    prerequisite = {
        focus = MKN_abolish_general_staff
    }
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    available = {
        has_government = democratic
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    completion_reward = {
        add_ideas = MKN_imperative_mandate_idea
    }
    ai_will_do = {
        factor = 2
    }
}
focus = {
    id = MKN_syndicalist_work_ethic
    icon = GFX_focus_MKN_syndicalist_work_ethic
    x = 86
    y = 7
    cost = 5
    prerequisite = {
        focus = MKN_imperative_mandate
    }
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    available = {
        has_government = democratic
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    completion_reward = {
        add_ideas = MKN_syndicalist_work_ethic_idea
    }
    ai_will_do = {
        factor = 2
    }
}
focus = {
    id = MKN_consumer_autonomy
    icon = GFX_focus_MKN_consumer_autonomy
    x = 86
    y = 8
    cost = 5
    prerequisite = {
        focus = MKN_syndicalist_work_ethic
    }
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    available = {
        has_government = democratic
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    completion_reward = {
        add_to_variable = {
            MKN_unified_supply_consumption_factor = -0.20
            tooltip = MKN_unified_supply_consumption_factor_tt
        }
        add_ideas = MKN_consumer_autonomy_idea
    }
    ai_will_do = {
        factor = 2
    }
}
focus = {
    id = MKN_elected_instructor_collegiums
    icon = GFX_focus_MKN_elected_instructor_collegiums
    x = 82
    y = 8
    cost = 5
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    available = {
        has_government = democratic
        has_completed_focus = MKN_arms_to_the_people
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    completion_reward = {
        add_ideas = MKN_elected_instructors_idea
    }
    ai_will_do = {
        factor = 2
    }
}
focus = {
    id = MKN_volost_signal_chains
    icon = GFX_focus_MKN_volost_signal_chains
    x = 82
    y = 9
    cost = 5
    prerequisite = {
        focus = MKN_elected_instructor_collegiums
    }
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    available = {
        has_government = democratic
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    completion_reward = {
        add_to_variable = {
            MKN_army_land_reinforce_rate = 0.10
            tooltip = MKN_army_land_reinforce_rate_tt
        }
        custom_effect_tooltip = MKN_people_signals_tt
        hidden_effect = {
            MKN_sync_people_defense = yes
        }
    }
    ai_will_do = {
        factor = 2
    }
}
focus = {
    id = MKN_hearth_defense_doctrine
    icon = GFX_focus_MKN_hearth_defense_doctrine
    x = 82
    y = 10
    cost = 5
    prerequisite = {
        focus = MKN_volost_signal_chains
    }
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    available = {
        has_government = democratic
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    completion_reward = {
        add_ideas = MKN_hearth_defense_idea
    }
    ai_will_do = {
        factor = 2
    }
}
focus = {
    id = MKN_subversion_of_enemy_ranks
    icon = GFX_focus_MKN_subversion_of_enemy_ranks
    x = 84
    y = 10
    cost = 5
    prerequisite = {
        focus = MKN_beacon_of_statelessness
    }
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    available = {
        has_government = democratic
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    completion_reward = {
        add_ideas = MKN_enemy_subversion_idea
        hidden_effect = {
            MKN_sync_people_defense = yes
        }
    }
    ai_will_do = {
        factor = 2
    }
}
focus = {
    id = MKN_autonomous_free_communes
    icon = GFX_focus_MKN_autonomous_free_communes
    x = 84
    y = 11
    cost = 5
    prerequisite = {
        focus = MKN_subversion_of_enemy_ranks
    }
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    available = {
        has_government = democratic
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    completion_reward = {
        add_ideas = MKN_free_communes_idea
        set_rule = {
            can_create_factions = yes
        }
        custom_effect_tooltip = MKN_free_communes_unlock_tt
    }
    ai_will_do = {
        factor = 2
    }
}
focus = {
    id = MKN_world_federation_of_labor
    icon = GFX_focus_MKN_world_federation_of_labor
    x = 84
    y = 12
    cost = 5
    prerequisite = {
        focus = MKN_autonomous_free_communes
    }
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    available = {
        has_government = democratic
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    completion_reward = {
        add_ideas = MKN_world_federation_idea
        custom_effect_tooltip = MKN_federation_influence_tt
        hidden_effect = {
            MKN_sync_federation_influence = yes
        }
    }
    ai_will_do = {
        factor = 2
    }
}
```

## common/national_focus/MKN.txt — три перенесённых фокуса Тратишова

Заменить существующие определения этих трёх ID целиком; не дублировать их. Изменена только колонка X=82 → X=80 для освобождения координат Волина.

```pdx
focus = {
    id = MKN_labor_armies
    icon = GFX_focus_MKN_labor_armies
    x = 80
    y = 8
    cost = 5
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    prerequisite = {
        focus = MKN_standardize_workshops
    }
    available = {
        has_government = fascism
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    completion_reward = {
        add_ideas = MKN_labor_armies_idea
        custom_effect_tooltip = MKN_labor_armies_lock_tt
    }
    ai_will_do = {
        factor = 2
    }
}
focus = {
    id = MKN_schools_of_young_insurgents
    icon = GFX_focus_MKN_schools_of_young_insurgents
    x = 80
    y = 9
    cost = 5
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    prerequisite = {
        focus = MKN_labor_armies
    }
    available = {
        has_government = fascism
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    completion_reward = {
        add_to_variable = {
            MKN_army_conscription = 0.06
            tooltip = MKN_army_conscription_tt
        }
        add_to_variable = {
            MKN_unified_training_time_army_factor = -0.20
            tooltip = MKN_unified_training_time_army_factor_tt
        }
        add_to_variable = {
            MKN_unified_research_speed_factor = -0.16
            tooltip = MKN_unified_research_speed_factor_tt
        }
    }
    ai_will_do = {
        factor = 2
    }
}
focus = {
    id = MKN_cult_of_fallen_atamans
    icon = GFX_focus_MKN_cult_of_fallen_atamans
    x = 80
    y = 10
    cost = 5
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    prerequisite = {
        focus = MKN_schools_of_young_insurgents
    }
    available = {
        has_government = fascism
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    completion_reward = {
        add_war_support = 0.20
        add_to_variable = {
            MKN_army_casualty_trickleback = 0.10
            tooltip = MKN_army_casualty_trickleback_tt
        }
    }
    ai_will_do = {
        factor = 2
    }
}
```

## common/ideas/MKN_soviet_ideas.txt

Новый файл целиком. Название soviet обозначает советы MKN; файл не принадлежит SOV.

```pdx
# Owner: MKN (Volin's democratic Free Soviets, not SOV).
# Values include x2 balance; consumer goods x3 twice (x9 from the initial prompt).
ideas = {
	country = {
		MKN_ferrer_schools_idea = {
			picture = generic_industrial_concern_1
			allowed = { original_tag = MKN }
			removal_cost = -1
			modifier = { research_speed_factor = 0.14 conscription = -0.02 }
		}
		MKN_labor_vouchers_idea = {
			picture = generic_industrial_concern_1
			allowed = { original_tag = MKN }
			removal_cost = -1
			modifier = { consumer_goods_factor = -0.45 }
		}
		MKN_voucher_transition_idea = {
			picture = generic_industrial_concern_1
			allowed = { original_tag = MKN }
			removal_cost = -1
			modifier = { production_factory_efficiency_gain_factor = -0.20 }
		}
		MKN_imperative_mandate_idea = {
			picture = generic_democratic_reformer_eastern_european_2d
			allowed = { original_tag = MKN }
			removal_cost = -1
			modifier = { stability_factor = 0.20 drift_defence_factor = 0.60 political_power_gain = -0.30 }
		}
		MKN_syndicalist_work_ethic_idea = {
			picture = generic_industrial_concern_1
			allowed = { original_tag = MKN }
			removal_cost = -1
			modifier = { production_factory_max_efficiency_factor = 0.30 repair_speed_factor = 0.40 }
		}
		MKN_consumer_autonomy_idea = {
			picture = generic_industrial_concern_1
			allowed = { original_tag = MKN }
			removal_cost = -1
			modifier = { conversion_cost_civ_to_mil_factor = 1.0 }
		}
		MKN_elected_instructors_idea = {
			picture = generic_army_war_college
			allowed = { original_tag = MKN }
			removal_cost = -1
			modifier = {
				army_morale_factor = 0.30
				experience_gain_army = 0.10
				max_planning = -0.40
				planning_speed = -0.50
			}
		}
		MKN_hearth_defense_idea = {
			picture = generic_army_war_college
			allowed = { original_tag = MKN }
			removal_cost = -1
			modifier = {
				army_core_defence_factor = 0.50
				dig_in_speed_factor = 0.50
				army_non_core_attack_factor = -0.50
			}
		}
		MKN_enemy_subversion_idea = {
			picture = generic_army_war_college
			allowed = { original_tag = MKN }
			removal_cost = -1
			modifier = { enemy_attrition = 0.40 custom_modifier_tooltip = MKN_people_subversion_tt }
		}
		MKN_free_communes_idea = {
			picture = generic_democratic_reformer_eastern_european_2d
			allowed = { original_tag = MKN }
			removal_cost = -1
			modifier = { generate_wargoal_tension = 0.40 }
		}
		MKN_world_federation_idea = {
			picture = generic_democratic_reformer_eastern_european_2d
			allowed = { original_tag = MKN }
			removal_cost = -1
			modifier = { stability_factor = 0.40 political_power_gain = 0.20 faction_trade_opinion_factor = 0.40 }
		}
		MKN_federation_influence_idea = {
			picture = generic_democratic_reformer_eastern_european_2d
			allowed = { always = yes }
			removal_cost = -1
			modifier = { democratic_drift = 0.10 }
		}
	}
}
```

## common/dynamic_modifiers/MKN_soviet_modifiers.txt

Новый файл целиком. Название soviet обозначает советы MKN; файл не принадлежит SOV.

```pdx
# Native NSB pattern: country-targeted state modifiers (SOV coastal batteries).
MKN_people_defense_signals = {
	enable = {
		is_owned_and_controlled_by = MKN
		is_core_of = MKN
		MKN = { has_government = democratic has_completed_focus = MKN_volost_signal_chains }
	}
	icon = GFX_modifiers_SOV_armored_battery
	army_org_regain = 0.20
}
MKN_people_defense_subversion = {
	enable = {
		is_owned_and_controlled_by = MKN
		is_core_of = MKN
		MKN = { has_government = democratic has_idea = MKN_enemy_subversion_idea }
	}
	icon = GFX_modifiers_SOV_armored_battery
	# Applied to hostile countries, not to MKN: this is damage TAKEN.
	org_damage_multiplier = 0.20
}
```

## common/opinion_modifiers/MKN_soviet_opinions.txt

Новый файл целиком. Название soviet обозначает советы MKN; файл не принадлежит SOV.

```pdx
opinion_modifiers = {
	MKN_sanctuary_hostility = { value = -40 }
}
```

## common/scripted_effects/MKN_soviet_effects.txt

Новый файл целиком. Название soviet обозначает советы MKN; файл не принадлежит SOV.

```pdx
# Deterministic shared-spirit reconstruction, never replay one-off rewards.
MKN_rebuild_soviet_industry_stats = {
	if = {
		limit = { has_completed_focus = MKN_consumer_autonomy }
		add_to_variable = { MKN_unified_supply_consumption_factor = -0.20 }
	}
}
MKN_rebuild_soviet_army_stats = {
	if = {
		limit = { has_completed_focus = MKN_volost_signal_chains }
		add_to_variable = { MKN_army_land_reinforce_rate = 0.10 }
	}
}
MKN_repair_soviet_progression = {
	if = {
		limit = { NOT = { has_country_flag = MKN_soviet_progression_v1 } }
		nww_mkn_rebuild_industry = yes
		nww_mkn_rebuild_services = yes
		set_country_flag = MKN_soviet_progression_v1
	}
}
MKN_sync_people_defense = {
	if = {
		limit = { has_completed_focus = MKN_volost_signal_chains }
		every_owned_state = {
			limit = {
				is_core_of = MKN
				NOT = { has_dynamic_modifier = { modifier = MKN_people_defense_signals scope = MKN } }
			}
			add_dynamic_modifier = { modifier = MKN_people_defense_signals scope = MKN }
		}
	}
	# Only current/previous enemies are processed after the propaganda unlock.
	if = {
		limit = { has_completed_focus = MKN_subversion_of_enemy_ranks }
		every_country = {
			limit = { OR = { has_war_with = MKN has_country_flag = MKN_people_subversion_active } }
			save_event_target_as = MKN_people_defense_enemy
			MKN = {
				every_owned_state = {
					if = {
						limit = { has_dynamic_modifier = { modifier = MKN_people_defense_subversion scope = event_target:MKN_people_defense_enemy } }
						remove_dynamic_modifier = { modifier = MKN_people_defense_subversion scope = event_target:MKN_people_defense_enemy }
					}
					if = {
						limit = {
							is_owned_and_controlled_by = MKN
							is_core_of = MKN
							MKN = { has_government = democratic has_idea = MKN_enemy_subversion_idea }
							event_target:MKN_people_defense_enemy = { has_war_with = MKN }
						}
						# Short expiry also cleans modifiers on land no longer owned by MKN.
						add_dynamic_modifier = { modifier = MKN_people_defense_subversion scope = event_target:MKN_people_defense_enemy days = 2 }
					}
				}
			}
			if = {
				limit = { has_war_with = MKN }
				set_country_flag = MKN_people_subversion_active
			}
			else = { clr_country_flag = MKN_people_subversion_active }
		}
	}
}
MKN_sync_federation_influence = {
	every_country = {
		limit = {
			OR = { is_neighbor_of = MKN has_idea = MKN_federation_influence_idea }
		}
		if = {
			limit = {
				is_neighbor_of = MKN
				NOT = { has_war_with = MKN }
				MKN = { exists = yes has_government = democratic has_idea = MKN_world_federation_idea }
			}
			if = {
				limit = { NOT = { has_idea = MKN_federation_influence_idea } }
				add_ideas = MKN_federation_influence_idea
			}
		}
		else = { remove_ideas = MKN_federation_influence_idea }
	}
}
```

## common/scripted_triggers/MKN_soviet_triggers.txt

Новый файл целиком. Название soviet обозначает советы MKN; файл не принадлежит SOV.

```pdx
# Owner: MKN; decision ROOT is MKN and FROM is the selected nation.
MKN_can_release_free_commune = {
	original_tag = MKN
	has_completed_focus = MKN_autonomous_free_communes
	has_government = democratic
	is_subject = no
	has_war = no
	has_capitulated = no
	OR = { is_in_faction = no is_faction_leader = yes }
	FROM = {
		exists = no
		any_core_state = { is_owned_and_controlled_by = ROOT NOT = { is_core_of = ROOT } }
		# release uses all owned cores: forbid any shared MKN core or occupied owned core.
		NOT = {
			any_core_state = {
				is_owned_by = ROOT
				OR = { is_core_of = ROOT NOT = { is_fully_controlled_by = ROOT } }
			}
		}
	}
}
# Recipient-scoped; checked both in the event trigger and before joining.
MKN_can_accept_commune_invitation = {
	exists = yes
	has_country_flag = MKN_free_commune_invitation_pending
	has_government = democratic
	is_subject = no
	is_in_faction = no
	has_capitulated = no
	has_war = no
	MKN = {
		exists = yes
		has_government = democratic
		has_completed_focus = MKN_autonomous_free_communes
		is_subject = no
		has_capitulated = no
		has_war = no
		OR = { is_in_faction = no is_faction_leader = yes }
	}
}
```

## common/decisions/categories/MKN_soviet_categories.txt

Новый файл целиком. Название soviet обозначает советы MKN; файл не принадлежит SOV.

```pdx
MKN_free_communes_category = {
	icon = military_operation
	allowed = { original_tag = MKN }
	visible = { has_completed_focus = MKN_autonomous_free_communes }
}
```

## common/decisions/MKN_soviet_decisions.txt

Новый файл целиком. Название soviet обозначает советы MKN; файл не принадлежит SOV.

```pdx
# Owner: MKN. Release only absent nations, at peace, without shared MKN cores.
MKN_free_communes_category = {
	MKN_release_free_commune = {
		icon = generic_political_actions
		allowed = { original_tag = MKN }
		target_non_existing = yes
		target_root_trigger = { original_tag = MKN has_completed_focus = MKN_autonomous_free_communes }
		target_trigger = {
			FROM = {
				exists = no
				any_core_state = { is_owned_and_controlled_by = ROOT NOT = { is_core_of = ROOT } }
			}
		}
		visible = { has_completed_focus = MKN_autonomous_free_communes }
		available = { MKN_can_release_free_commune = yes }
		cost = 0
		complete_effect = {
			if = {
				limit = { MKN_can_release_free_commune = yes }
				release = FROM
				if = {
					limit = { FROM = { is_subject_of = ROOT } }
					set_autonomy = { target = FROM autonomy_state = autonomy_free end_wars = no end_civil_wars = no }
				}
				# A release may inherit a faction: return the decision to the recipient.
				if = {
					limit = { FROM = { is_in_faction_with = ROOT } }
					remove_from_faction = FROM
				}
				FROM = {
					set_popularities = { democratic = 80 neutrality = 20 fascism = 0 communism = 0 }
					set_politics = { ruling_party = democratic elections_allowed = no }
					set_country_flag = { flag = MKN_free_commune_invitation_pending days = 30 }
					country_event = { id = mkn_free_soviets.1 days = 1 }
				}
			}
		}
		# Territorial releases require a deliberate player choice.
		ai_will_do = { factor = 0 }
	}
	MKN_invite_free_commune = {
		icon = generic_political_actions
		allowed = { original_tag = MKN }
		target_root_trigger = { original_tag = MKN has_completed_focus = MKN_autonomous_free_communes }
		target_trigger = {
			FROM = {
				exists = yes
				NOT = { tag = ROOT }
				has_government = democratic
				is_subject = no
				is_in_faction = no
			}
		}
		visible = { has_completed_focus = MKN_autonomous_free_communes }
		available = {
			has_government = democratic
			is_subject = no
			has_capitulated = no
			has_war = no
			OR = { is_in_faction = no is_faction_leader = yes }
			FROM = {
				exists = yes
				has_government = democratic
				is_subject = no
				is_in_faction = no
				has_capitulated = no
				has_war = no
				NOT = { has_country_flag = MKN_free_commune_invitation_pending }
			}
		}
		cost = 25
		days_re_enable = 90
		complete_effect = {
			FROM = {
				set_country_flag = { flag = MKN_free_commune_invitation_pending days = 30 }
				country_event = { id = mkn_free_soviets.1 days = 1 }
			}
		}
		ai_will_do = { factor = 1 }
	}
}
```

## common/on_actions/MKN_soviet_on_actions.txt

Новый файл целиком. Название soviet обозначает советы MKN; файл не принадлежит SOV.

```pdx
on_actions = {
	on_startup = {
		effect = {
			MKN = {
				if = {
					limit = { exists = yes }
					MKN_repair_soviet_progression = yes
					MKN_repair_research_capacity = yes
					MKN_sync_people_defense = yes
				}
				MKN_sync_federation_influence = yes
			}
		}
	}
	on_daily_MKN = {
		effect = {
			MKN_repair_soviet_progression = yes
			MKN_sync_people_defense = yes
		}
	}
	on_weekly = {
		effect = {
			if = { limit = { tag = MKN } MKN_sync_federation_influence = yes }
			if = {
				limit = { has_idea = MKN_federation_influence_idea MKN = { exists = no } }
				remove_ideas = MKN_federation_influence_idea
			}
		}
	}
}
```

## events/MKN_soviet_events.txt

Новый файл целиком. Название soviet обозначает советы MKN; файл не принадлежит SOV.

```pdx
# Owner: MKN. A liberated nation remains sovereign if it refuses the offer.
add_namespace = mkn_free_soviets
country_event = {
	id = mkn_free_soviets.1
	title = mkn_free_soviets.1.t
	desc = mkn_free_soviets.1.d
	picture = GFX_report_event_generic_factory
	is_triggered_only = yes
	option = {
		name = mkn_free_soviets.1.a
		trigger = { MKN_can_accept_commune_invitation = yes }
		ai_chance = { factor = 70 }
		if = {
			limit = { MKN_can_accept_commune_invitation = yes }
			MKN = {
				if = {
					limit = { is_in_faction = no }
					create_faction = MKN_free_labor_federation
				}
				add_to_faction = ROOT
			}
		}
		clr_country_flag = MKN_free_commune_invitation_pending
	}
	option = {
		name = mkn_free_soviets.1.b
		ai_chance = { factor = 30 }
		clr_country_flag = MKN_free_commune_invitation_pending
	}
}
```

## common/scripted_effects/MKN_research_effects.txt

Заменить существующее определение целиком. В нём сохранены условия прежних научных институтов и Киева.

```pdx
# Owner: MKN. Capacity floors only: never replay focus rewards or reduce
# research slots already earned in an older save.
MKN_repair_research_capacity = {
	if = {
		limit = { has_completed_focus = MKN_ferrer_modern_schools amount_research_slots < 5 }
		set_research_slots = 5
	}
	if = {
		limit = {
			has_completed_focus = MKN_communal_research_network
			has_completed_focus = MKN_free_science_network
			amount_research_slots < 5
		}
		set_research_slots = 5
	}
	if = {
		limit = {
			has_completed_focus = MKN_communal_research_network
			has_completed_focus = MKN_free_science_network
			has_completed_focus = MKN_kyiv_scientific_exchange
			amount_research_slots < 6
		}
		set_research_slots = 6
	}
}
```

## common/scripted_effects/nww_mkn_progression.txt — подключение экономики

В конце существующего `nww_mkn_rebuild_industry`, после имеющегося вызова пересчёта Тратишова, добавить пересчёт Вольных советов. Конец блока должен содержать:

```pdx
MKN_rebuild_militarist_industry_stats = yes
MKN_rebuild_soviet_industry_stats = yes
set_country_flag = MKN_industry_integration_v4
```

## common/scripted_effects/nww_mkn_progression.txt — подключение армии

Внутри существующего `nww_mkn_rebuild_services`, после уже имеющихся вызовов поздних веток и Тратишова, добавить пересчёт Вольных советов:

```pdx
MKN_rebuild_horizons_service_stats = yes
MKN_rebuild_militarist_army_stats = yes
MKN_rebuild_soviet_army_stats = yes
```

Остальные сбросы переменных, условия, награды и версии миграции существующих эффектов сохранить. Это вставки внутрь эффектов, а не дополнительные одноимённые определения.

## localisation/russian/MKN_soviet_l_russian.yml

Новый файл целиком. Сохранить как UTF-8 с BOM.

```yaml
l_russian:
 MKN_ferrer_modern_schools:0 "Свободные школы Феррера"
 MKN_ferrer_modern_schools_desc:0 "Ребёнок должен учиться задавать вопросы, а не маршировать по звонку. Школы Феррера откроют лаборатории и мастерские для всех коммун. У науки появится будущее, но меньше молодых людей выберут казарму."
 MKN_sanctuary_of_free_thought:0 "Убежище мировой мысли"
 MKN_sanctuary_of_free_thought_desc:0 "Учёный, изгнанный королём или вождём, найдёт у нас стол, книги и право спорить. Его знания послужат людям. Европейские дворы и фашистские канцелярии увидят в наших университетах пристанище своих врагов."
 MKN_eradication_of_wage_labor:0 "Ликвидация наёмного труда"
 MKN_eradication_of_wage_labor_desc:0 "Человек больше не продаёт хозяину часы своей жизни. Трудовой чек даёт право на долю общего продукта. Пока артели учатся согласовывать новые расчёты, производство будет буксовать; свободу придётся осваивать на практике."
 MKN_imperative_mandate:0 "Императивный мандат"
 MKN_imperative_mandate_desc:0 "Делегат — лишь голос своей коммуны, лишённый права подменять её наказ личным мнением. Нарушивший поручение отзывается без промедления. Демократия не терпит политиканов, даже если согласование решений отнимает недели."
 MKN_syndicalist_work_ethic:0 "Синдикалистская этика труда"
 MKN_syndicalist_work_ethic_desc:0 "Станок принадлежит тем, кто знает каждый его звук. Синдикаты будут передавать опыт между мастерскими, беречь инструмент и восстанавливать разрушенные цеха. Общий труд требует мастерства, а не надсмотрщика."
 MKN_consumer_autonomy:0 "Всеобщая потребительская автономия"
 MKN_consumer_autonomy_desc:0 "Потребительские союзы распределяют хлеб, одежду и армейское снабжение через местные склады. Обозы станут легче, но ни один съезд не сможет одним приказом превратить гражданский завод в оружейный."
 MKN_elected_instructor_collegiums:0 "Выборные инструкторские коллегии"
 MKN_elected_instructor_collegiums_desc:0 "Генералы ведут людей на убой ради звёзд на погонах. Наши командиры избираются бойцами и сменяются по их воле. У нас нет штабных карт и длинных диспозиций, но есть братство, не знающее паники. За эту свободу мы платим медленным и несовершенным планированием."
 MKN_volost_signal_chains:0 "Сигнальные цепочки волостей"
 MKN_volost_signal_chains_desc:0 "Телефонисты, железнодорожники и сельские связные соединят разрозненные отряды. На своей земле ополчение быстрее соберётся у места прорыва и восстановит порядок после боя. Каждая волость станет узлом Народной обороны."
 MKN_hearth_defense_doctrine:0 "Доктрина защиты родного очага"
 MKN_hearth_defense_doctrine_desc:0 "Свободный хлебороб не пойдёт с ружьём на чужие поля и не станет навязывать революцию силой. Но за свой хутор, за детскую школу и за вольный колодец он превратит степь в пылающий ад для любого оккупанта."
 MKN_subversion_of_enemy_ranks:0 "Разложение вражеских армий"
 MKN_subversion_of_enemy_ranks_desc:0 "За вражеской шинелью стоит такой же рабочий или крестьянин. Наши листовки и голоса перебежчиков заставят его усомниться в приказах. На земле коммун оккупант встретит не только винтовки, но и вопрос: за чьи интересы он умирает?"
 MKN_autonomous_free_communes:0 "Свободные коммуны"
 MKN_autonomous_free_communes_desc:0 "Освобождённый народ не должен менять чужого господина на нашего коменданта. Мы предложим независимость и демократическое самоуправление народам принадлежащих нам земель. Союз возможен лишь с их согласия; отказ не отменяет свободу."
 MKN_world_federation_of_labor:0 "Всемирная федерация трудящихся"
 MKN_world_federation_of_labor_desc:0 "Через границы идут книги, инструменты и письма рабочих союзов. Федерация живёт свободным согласием, общим трудом и взаимной помощью. Её пример убедит соседей сильнее оккупационной армии, если мы сумеем пережить натиск империй."
 MKN_ferrer_schools_idea:0 "Свободные школы Феррера"
 MKN_ferrer_schools_idea_desc:0 "Свободное образование ускоряет научный поиск. Молодёжь предпочитает лаборатории военному ремеслу, сокращая доступный призыв."
 MKN_labor_vouchers_idea:0 "Трудовые чеки"
 MKN_labor_vouchers_idea_desc:0 "Общий продукт распределяется без торговой наценки и прибыли хозяина. Потребительские союзы уменьшают нагрузку повседневного снабжения на промышленность."
 MKN_voucher_transition_idea:0 "Переход к трудовым чекам"
 MKN_voucher_transition_idea_desc:0 "Новая система расчётов ещё не налажена. В течение 120 дней перебои учёта замедляют рост эффективности производства."
 MKN_imperative_mandate_idea:0 "Императивный мандат"
 MKN_imperative_mandate_idea_desc:0 "Доверие к советам защищает общество от чужой пропаганды. Но постоянные отзывы и согласования отнимают время и политические силы."
 MKN_syndicalist_work_ethic_idea:0 "Синдикалистская этика труда"
 MKN_syndicalist_work_ethic_idea_desc:0 "Опыт остаётся у мастеров и передаётся всему синдикату. Рабочие повышают предел эффективности и быстро возвращают повреждённые предприятия к жизни."
 MKN_consumer_autonomy_idea:0 "Автономия потребительских союзов"
 MKN_consumer_autonomy_idea_desc:0 "Завод меняет назначение только после согласия его коллектива. Переоборудование гражданских предприятий в военные требует длительных и дорогих переговоров."
 MKN_elected_instructors_idea:0 "Выборные инструкторы"
 MKN_elected_instructors_idea_desc:0 "Братство и взаимное обучение помогают людям вернуться в строй. Штабная школа распущена: замыслы наступлений созревают медленно, а подробные планы редко выдерживают обсуждение."
 MKN_hearth_defense_idea:0 "Защита родного очага"
 MKN_hearth_defense_idea_desc:0 "Защитники коммун быстро роют окопы и стойко держатся на своей земле. За её пределами их решимость идти в атаку резко падает."
 MKN_enemy_subversion_idea:0 "Солдатская солидарность"
 MKN_enemy_subversion_idea_desc:0 "Изнурённые вражеские части теряют людей и веру в приказы. На территории Народной обороны пропаганда усиливает получаемый ими урон организации."
 MKN_free_communes_idea:0 "Свобода без завоевания"
 MKN_free_communes_idea_desc:0 "Коммуны требуют серьёзных оснований для войны. Право народа на независимость важнее удобства военных планов."
 MKN_world_federation_idea:0 "Всемирная федерация трудящихся"
 MKN_world_federation_idea_desc:0 "Взаимопомощь укрепляет общество и политическую инициативу. Торговля внутри союза опирается на доверие, а соседям доступен пример свободного самоуправления."
 MKN_federation_influence_idea:0 "Пример вольных коммун"
 MKN_federation_influence_idea_desc:0 "Открытая граница с Махновщиной несёт книги и рассказы о низовом самоуправлении. Популярность демократических идей растёт, пока сохраняются мирное соседство и сама федерация."
 MKN_people_defense_signals:0 "Народная оборона: связь волостей"
 MKN_people_defense_signals_desc:0 "Сеть местных связных помогает нашим войскам восстанавливать организацию в принадлежащей нам и контролируемой коренной области."
 MKN_people_defense_subversion:0 "Народная оборона: братание"
 MKN_people_defense_subversion_desc:0 "Войска противника получают больше урона организации при боях на территории Народной обороны. Модификатор не применяется к войскам MKN."
 MKN_people_signals_tt:0 "§YНародная оборона§!: восстановление организации армии §G+20%§! в собственных контролируемых коренных областях."
 MKN_people_subversion_tt:0 "§YНародная оборона§!: враги получают §G+20%§! урона организации при боях в принадлежащих нам и контролируемых коренных областях."
 MKN_free_thought_research:0 "Мастерские свободной мысли"
 MKN_free_communes_unlock_tt:0 "Открывает мирное освобождение независимых демократических коммун и приглашения в добровольный союз. Коренные области MKN не передаются; вступление требует согласия адресата."
 MKN_federation_influence_tt:0 "У мирных сухопутных соседей появляется дух с §G+0.10§! ежедневного роста популярности демократии. Соседство, мир и существование демократической федерации проверяются еженедельно."
 MKN_free_communes_category:0 "Союз вольных коммун"
 MKN_free_communes_category_desc:0 "Свобода народа не может быть условной. Освобождаемая страна получает независимость и сама решает, вступать ли в наш союз."
 MKN_release_free_commune:0 "Освободить коммуну: [FROM.GetName]"
 MKN_release_free_commune_desc:0 "В мирное время освободить отсутствующую страну на её принадлежащих нам коренных землях. Требуются полный контроль и отсутствие общих коренных областей MKN. Новая страна станет независимой демократией и получит приглашение, которое может отклонить."
 MKN_invite_free_commune:0 "Предложить союз: [FROM.GetName]"
 MKN_invite_free_commune_desc:0 "За 25 политической власти предложить независимой мирной демократии вступить в федерацию. Отказ сохраняет её независимость и не даёт права на войну."
 MKN_free_labor_federation:0 "Вольная федерация труда"
 mkn_free_soviets.1.t:0 "Предложение вольных советов"
 mkn_free_soviets.1.d:0 "Из Махновщины прибыли делегаты рабочих и сельских коммун. Они предлагают союз равных, общую безопасность и обмен без сюзерена и подчинённых. Решение остаётся за нами: отказ не должен обернуться потерей свободы."
 mkn_free_soviets.1.a:0 "Вступить в союз равных."
 mkn_free_soviets.1.b:0 "Мы сохраним самостоятельный путь."
 MKN_sanctuary_hostility:0 "Пристанище революционных мыслителей"
```

## localisation/english/MKN_soviet_l_english.yml

Новый файл целиком. Сохранить как UTF-8 с BOM.

```yaml
l_english:
 MKN_ferrer_modern_schools:0 "Ferrer Modern Schools"
 MKN_ferrer_modern_schools_desc:0 "A child must learn to ask questions, not march at the sound of a bell. Ferrer schools will open laboratories and workshops to every commune. Science will gain a future, but fewer young people will choose the barracks."
 MKN_sanctuary_of_free_thought:0 "Sanctuary of Free Thought"
 MKN_sanctuary_of_free_thought_desc:0 "A scholar expelled by a king or dictator will find a desk, books and the freedom to argue here. Their knowledge will serve the people. Europe’s courts and fascist governments will regard our universities as a refuge for their enemies."
 MKN_eradication_of_wage_labor:0 "Eradication of Wage Labor"
 MKN_eradication_of_wage_labor_desc:0 "No one will sell the hours of their life to a master. Labor vouchers grant a share of the common product. Production will falter as the artels learn to coordinate the new accounts; freedom must be learned through practice."
 MKN_imperative_mandate:0 "The Imperative Mandate"
 MKN_imperative_mandate_desc:0 "A delegate is only the voice of their commune, with no right to replace its instructions with a personal opinion. Anyone who breaks their mandate is recalled without delay. Democracy tolerates no professional politicians, even when agreement takes weeks."
 MKN_syndicalist_work_ethic:0 "Syndicalist Work Ethic"
 MKN_syndicalist_work_ethic_desc:0 "The machine belongs to those who know its every sound. Syndicates will share experience between workshops, preserve their tools and rebuild ruined factory halls. Common labor requires skill, not an overseer."
 MKN_consumer_autonomy:0 "Universal Consumer Autonomy"
 MKN_consumer_autonomy_desc:0 "Consumer unions distribute bread, clothing and army supplies through local depots. Supply trains will become lighter, but no congress can turn a civilian factory into an arsenal with a single order."
 MKN_elected_instructor_collegiums:0 "Elected Instructor Collegiums"
 MKN_elected_instructor_collegiums_desc:0 "Generals lead people to slaughter for stars on their shoulders. Our commanders are elected by the fighters and recalled at their will. We lack staff maps and lengthy dispositions, but possess a brotherhood that knows no panic. Slow and imperfect planning is the price of this freedom."
 MKN_volost_signal_chains:0 "Volost Signal Chains"
 MKN_volost_signal_chains_desc:0 "Telephone operators, railway workers and village couriers will link the scattered detachments. On home soil the militia will gather faster at a breach and restore order after battle. Every volost will become a node of the People’s Defense."
 MKN_hearth_defense_doctrine:0 "Defense of the Hearth Doctrine"
 MKN_hearth_defense_doctrine_desc:0 "The free farmer will not take a rifle into another people’s fields or impose revolution by force. Yet for their homestead, children’s school and village well, they will turn the steppe into a blazing hell for any occupier."
 MKN_subversion_of_enemy_ranks:0 "Subversion of Enemy Ranks"
 MKN_subversion_of_enemy_ranks_desc:0 "Beneath the enemy’s uniform stands another worker or farmer. Our leaflets and the voices of deserters will make them question their orders. On communal soil the invader will face rifles and a question: whose interests are they dying for?"
 MKN_autonomous_free_communes:0 "Autonomous Free Communes"
 MKN_autonomous_free_communes_desc:0 "A liberated people must not exchange a foreign master for our commandant. We will offer independence and democratic self-government to the peoples of lands we own. Union requires their consent; refusal does not cancel freedom."
 MKN_world_federation_of_labor:0 "World Federation of Labor"
 MKN_world_federation_of_labor_desc:0 "Books, tools and letters from workers’ unions cross the borders. The federation lives through free consent, common labor and mutual aid. Its example will persuade neighbors more deeply than an occupying army, if we can survive the empires’ assault."
 MKN_ferrer_schools_idea:0 "Ferrer Modern Schools"
 MKN_ferrer_schools_idea_desc:0 "Free education accelerates scientific inquiry. Young people prefer laboratories to soldiering, reducing the available recruitment pool."
 MKN_labor_vouchers_idea:0 "Labor Vouchers"
 MKN_labor_vouchers_idea_desc:0 "The common product is distributed without commercial markups or an owner’s profit. Consumer unions reduce the burden of everyday supply on industry."
 MKN_voucher_transition_idea:0 "Transition to Labor Vouchers"
 MKN_voucher_transition_idea_desc:0 "The new accounting system is not yet established. For 120 days, disrupted records slow the growth of production efficiency."
 MKN_imperative_mandate_idea:0 "Imperative Mandate"
 MKN_imperative_mandate_idea_desc:0 "Trust in the councils protects society against foreign propaganda. Constant recalls and consultations consume time and political energy."
 MKN_syndicalist_work_ethic_idea:0 "Syndicalist Work Ethic"
 MKN_syndicalist_work_ethic_idea_desc:0 "Experience remains with the workers and is shared across the syndicate. They raise the efficiency ceiling and rapidly restore damaged enterprises."
 MKN_consumer_autonomy_idea:0 "Autonomous Consumer Unions"
 MKN_consumer_autonomy_idea_desc:0 "A factory changes its purpose only with the consent of its workers. Converting civilian enterprises to military production requires long and costly negotiations."
 MKN_elected_instructors_idea:0 "Elected Instructors"
 MKN_elected_instructors_idea_desc:0 "Comradeship and mutual instruction help fighters return to the ranks. The staff school has been dissolved: offensive plans develop slowly and detailed preparations rarely survive debate."
 MKN_hearth_defense_idea:0 "Defense of the Hearth"
 MKN_hearth_defense_idea_desc:0 "The communes’ defenders dig quickly and hold firm on their own soil. Beyond it, their willingness to attack falls sharply."
 MKN_enemy_subversion_idea:0 "Soldiers’ Solidarity"
 MKN_enemy_subversion_idea_desc:0 "Exhausted enemy formations lose people and faith in their orders. Within People’s Defense territory, propaganda increases the organization damage they suffer."
 MKN_free_communes_idea:0 "Freedom without Conquest"
 MKN_free_communes_idea_desc:0 "The communes demand serious grounds for war. A people’s right to independence matters more than convenient military plans."
 MKN_world_federation_idea:0 "World Federation of Labor"
 MKN_world_federation_idea_desc:0 "Mutual aid strengthens society and political initiative. Trade within the faction rests on trust, while neighbors can see an example of free self-government."
 MKN_federation_influence_idea:0 "Example of the Free Communes"
 MKN_federation_influence_idea_desc:0 "The open frontier with Makhnovshchina brings books and accounts of grassroots self-government. Democratic ideas gain support while peaceful neighborly relations and the federation endure."
 MKN_people_defense_signals:0 "People’s Defense: Volost Signals"
 MKN_people_defense_signals_desc:0 "Local couriers help our troops regain organization in this owned and controlled core state."
 MKN_people_defense_subversion:0 "People’s Defense: Fraternization"
 MKN_people_defense_subversion_desc:0 "Enemy troops take greater organization damage while fighting in People’s Defense territory. This modifier does not apply to MKN troops."
 MKN_people_signals_tt:0 "§YPeople’s Defense§!: army organization regain §G+20%§! in our owned and controlled core states."
 MKN_people_subversion_tt:0 "§YPeople’s Defense§!: enemies take §G+20%§! organization damage while fighting in our owned and controlled core states."
 MKN_free_thought_research:0 "Workshops of Free Thought"
 MKN_free_communes_unlock_tt:0 "Unlocks the peaceful release of independent democratic communes and invitations to a voluntary faction. MKN core states are protected; joining requires the recipient’s consent."
 MKN_federation_influence_tt:0 "Peaceful land neighbors gain a spirit with §G+0.10§! daily democratic support. Neighbor status, peace and the democratic federation’s existence are checked weekly."
 MKN_free_communes_category:0 "Union of Free Communes"
 MKN_free_communes_category_desc:0 "A people’s freedom cannot be conditional. A released nation gains independence and decides for itself whether to join our union."
 MKN_release_free_commune:0 "Release a Free Commune: [FROM.GetName]"
 MKN_release_free_commune_desc:0 "At peace, release an absent country on its core lands that we own. Requires full control and no shared MKN cores among the lands to be released. The new nation becomes an independent democracy and receives an invitation it may refuse."
 MKN_invite_free_commune:0 "Offer a Union: [FROM.GetName]"
 MKN_invite_free_commune_desc:0 "Spend 25 political power to invite an independent, peaceful democracy to the federation. Refusal preserves its independence and grants no claim to war."
 MKN_free_labor_federation:0 "Free Federation of Labor"
 mkn_free_soviets.1.t:0 "An Offer from the Free Soviets"
 mkn_free_soviets.1.d:0 "Delegates from Makhnovshchina’s workers’ and rural communes have arrived. They propose a union of equals, common security and exchange without overlords or subjects. The choice remains ours: refusal must not cost us our freedom."
 mkn_free_soviets.1.a:0 "Join the union of equals."
 mkn_free_soviets.1.b:0 "We will follow our own path."
 MKN_sanctuary_hostility:0 "Shelter for Revolutionary Thinkers"
```

## Проверка

Новый `tools/validate_mkn_free_soviets.py` подключён к общей проверке. Существующие интерпретаторы армии, экономики, поздних веток и Тратишова загружают `MKN_soviet_effects.txt`; проверка BoP учитывает новый экономический пересчёт, проверка науки разрешает источник слотов Феррера. Эти инструменты не нужны движку игры.

```sh
python tools/validate_country_content.py --game '/home/dima00138/.local/share/Steam/steamapps/common/Hearts of Iron IV'
git diff --check
```

Новая кампания, визуальная проверка tooltip и фактического боевого эффекта в этой сессии не выполнялись.
