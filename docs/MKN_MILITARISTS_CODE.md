# MKN: полный код расширения анархо-милитаристов

Код уже применён к рабочему проекту. Ниже — блоки файлов для переноса и проверки. В существующие файлы вставляются только указанные блоки; новые файлы приведены целиком. Повторно добавлять те же ID в текущую рабочую копию не нужно.

Поведение, адаптации под HOI4 1.19.3, конкретные образцы DLC и результаты проверки: [MKN_militarists.md](MKN_militarists.md).

## common/national_focus/MKN.txt — 12 новых фокусов

Вставить внутрь существующего `focus_tree = { ... }`. Координаты абсолютные. Для округов второе условие AND находится в `available`, без длинного соединителя.

```pdx
focus = {
    id = MKN_field_counter_intelligence
    icon = GFX_focus_MKN_field_counter_intelligence
    x = 74
    y = 5
    cost = 5
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    prerequisite = {
        focus = MKN_arrest_demagogues
    }
    available = {
        has_government = fascism
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    completion_reward = {
        if = {
            limit = {
                has_dlc = "La Resistance"
            }
            add_ideas = MKN_field_counter_intelligence_idea
            add_tech_bonus = {
                name = MKN_counter_intelligence_research
                bonus = 1
                uses = 1
                category = computing_tech
            }
        }
        else = {
            add_ideas = MKN_field_counter_intelligence_reserve_idea
            add_political_power = 100
        }
    }
    ai_will_do = {
        factor = 2
    }
}
focus = {
    id = MKN_disarming_the_communes
    icon = GFX_focus_MKN_disarming_the_communes
    x = 74
    y = 6
    cost = 5
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    prerequisite = {
        focus = MKN_field_counter_intelligence
    }
    available = {
        has_government = fascism
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    completion_reward = {
        add_ideas = MKN_disarmed_communes_idea
    }
    ai_will_do = {
        factor = 2
    }
}
focus = {
    id = MKN_tribunals_of_the_black_staff
    icon = GFX_focus_MKN_tribunals_of_the_black_staff
    x = 74
    y = 7
    cost = 5
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    prerequisite = {
        focus = MKN_disarming_the_communes
    }
    available = {
        has_government = fascism
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    completion_reward = {
        add_ideas = MKN_tribunals_idea
    }
    ai_will_do = {
        factor = 2
    }
}
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
focus = {
    id = MKN_military_districts
    icon = GFX_focus_MKN_military_districts
    x = 74
    y = 9
    cost = 5
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    prerequisite = {
        focus = MKN_tribunals_of_the_black_staff
    }
    available = {
        has_government = fascism
        has_completed_focus = MKN_iron_fist_trains
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    completion_reward = {
        custom_effect_tooltip = MKN_unlock_military_districts_tt
        add_to_variable = {
            MKN_army_supply_consumption_factor = 0.16
            tooltip = MKN_army_supply_consumption_factor_tt
        }
    }
    ai_will_do = {
        factor = 2
    }
}
focus = {
    id = MKN_council_of_field_commanders
    icon = GFX_focus_MKN_council_of_field_commanders
    x = 74
    y = 10
    cost = 5
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    prerequisite = {
        focus = MKN_military_districts
    }
    available = {
        has_government = fascism
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    completion_reward = {
        random_unit_leader = {
            limit = {
                is_army_leader = yes
                NOT = {
                    has_trait = mkn_council_member_trait
                }
            }
            add_unit_leader_trait = mkn_council_member_trait
        }
        random_unit_leader = {
            limit = {
                is_army_leader = yes
                NOT = {
                    has_trait = mkn_council_member_trait
                }
            }
            add_unit_leader_trait = mkn_council_member_trait
        }
        random_unit_leader = {
            limit = {
                is_army_leader = yes
                NOT = {
                    has_trait = mkn_council_member_trait
                }
            }
            add_unit_leader_trait = mkn_council_member_trait
        }
        add_ideas = MKN_council_of_commanders_idea
    }
    ai_will_do = {
        factor = 2
    }
}
focus = {
    id = MKN_the_supreme_warlord
    icon = GFX_focus_MKN_the_supreme_warlord
    x = 74
    y = 11
    cost = 5
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    prerequisite = {
        focus = MKN_council_of_field_commanders
    }
    available = {
        has_government = fascism
        has_country_leader_with_trait = mkn_iron_warlord
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    completion_reward = {
        remove_country_leader_trait = mkn_iron_warlord
        add_country_leader_trait = mkn_supreme_warlord
    }
    ai_will_do = {
        factor = 2
    }
}
focus = {
    id = MKN_preemptive_strike_doctrine
    icon = GFX_focus_MKN_preemptive_strike_doctrine
    x = 78
    y = 11
    cost = 5
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    prerequisite = {
        focus = MKN_the_black_horde
    }
    available = {
        has_government = fascism
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    completion_reward = {
        add_ideas = MKN_preemptive_strike_idea
    }
    ai_will_do = {
        factor = 2
    }
}
focus = {
    id = MKN_military_marches
    icon = GFX_focus_MKN_military_marches
    x = 78
    y = 12
    cost = 5
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    prerequisite = {
        focus = MKN_preemptive_strike_doctrine
    }
    available = {
        has_government = fascism
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    completion_reward = {
        set_rule = {
            can_puppet = yes
        }
        add_ideas = MKN_military_marches_idea
        custom_effect_tooltip = MKN_unlock_military_marches_tt
    }
    ai_will_do = {
        factor = 2
    }
}
focus = {
    id = MKN_black_banner_over_europe
    icon = GFX_focus_MKN_black_banner_over_europe
    x = 78
    y = 13
    cost = 5
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    prerequisite = {
        focus = MKN_military_marches
    }
    available = {
        has_government = fascism
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    completion_reward = {
        add_ideas = MKN_permanent_revolution_idea
    }
    ai_will_do = {
        factor = 2
    }
}
```

## common/national_focus/MKN.txt — замена трёх существующих политических фокусов

Заменить соответствующие определения целиком, сохранив единственное определение каждого ID. Изменение — блокировка после «Трудовых армий». Экономические финалы не изменены.

```pdx
focus = {
    id = MKN_pact_of_free_communes
    y = 4
    completion_reward = {
        MKN_resolve_succession_crisis = yes
        add_stability = 0.10
        add_political_power = 50
    }
    prerequisite = {
        focus = MKN_triumph_of_free_soviets
    }
    available = {
        custom_trigger_tooltip = {
            tooltip = MKN_civil_settlement_allowed_tt
            NOT = {
                has_completed_focus = MKN_labor_armies
            }
        }
        NOT = {
            has_country_flag = MKN_crisis_legacy_settled
        }
        has_government = democratic
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    cost = 5
    icon = GFX_focus_MKN_program_nabat_1
    x = 84
}
focus = {
    id = MKN_grain_ultimatum
    y = 4
    completion_reward = {
        MKN_resolve_succession_crisis = yes
        add_stability = 0.10
        add_political_power = 50
    }
    prerequisite = {
        focus = MKN_peasant_delegates
    }
    available = {
        custom_trigger_tooltip = {
            tooltip = MKN_civil_settlement_allowed_tt
            NOT = {
                has_completed_focus = MKN_labor_armies
            }
        }
        NOT = {
            has_country_flag = MKN_crisis_legacy_settled
        }
        has_government = neutrality
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    cost = 5
    icon = GFX_focus_MKN_program_agrarian_1
    x = 90
}
focus = {
    id = MKN_purge_irreconcilables
    y = 4
    completion_reward = {
        MKN_resolve_succession_crisis = yes
        add_stability = 0.10
        add_political_power = 50
        MKN_install_tsebriy = yes
    }
    prerequisite = {
        focus = MKN_emergency_revkom
    }
    available = {
        custom_trigger_tooltip = {
            tooltip = MKN_civil_settlement_allowed_tt
            NOT = {
                has_completed_focus = MKN_labor_armies
            }
        }
        NOT = {
            has_country_flag = MKN_crisis_legacy_settled
        }
        has_government = communism
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    ai_will_do = {
        factor = 10
    }
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    cost = 5
    icon = GFX_focus_MKN_program_revkom_1
    x = 96
}
```

## common/ideas/MKN_militarist_ideas.txt

Новый файл целиком.

```pdx
# Owner: MKN. Separate political institutions explicitly requested for Tratishov's path.
# Army recruitment/training/recovery remain in the existing shared development spirits.
ideas = {
	country = {
		MKN_field_counter_intelligence_idea = {
			picture = generic_army_war_college
			allowed = { original_tag = MKN }
			removal_cost = -1
			modifier = {
				operative_slot = 2
				enemy_operative_detection_chance_factor = 0.30
				agency_upgrade_time = -0.30
			}
		}
		MKN_field_counter_intelligence_reserve_idea = {
			picture = generic_army_war_college
			allowed = { original_tag = MKN }
			removal_cost = -1
			modifier = { enemy_operative_detection_chance_factor = 0.30 }
		}
		MKN_disarmed_communes_idea = {
			picture = generic_army_war_college
			allowed = { original_tag = MKN }
			removal_cost = -1
			modifier = {
				stability_factor = -0.10
				political_power_gain = 0.20
				compliance_gain = 0.10
				trade_opinion_factor = -0.60
				consumer_goods_factor = 0.45
			}
		}
		MKN_tribunals_idea = {
			picture = generic_army_war_college
			allowed = { original_tag = MKN }
			removal_cost = -1
			modifier = {
				attrition = -0.20
				surrender_limit = 0.30
				political_power_gain = -0.30
			}
		}
		MKN_labor_armies_idea = {
			picture = generic_industrial_concern_1
			allowed = { original_tag = MKN }
			removal_cost = -1
			modifier = {
				industrial_capacity_factory = 0.30
				production_factory_efficiency_gain_factor = 0.20
				production_speed_industrial_complex_factor = -0.60
				stability_factor = -0.20
				custom_modifier_tooltip = MKN_labor_armies_lock_tt
			}
		}
		MKN_council_of_commanders_idea = {
			picture = generic_army_war_college
			allowed = { original_tag = MKN }
			removal_cost = -1
			modifier = {
				army_advisor_cost_factor = -0.30
				air_advisor_cost_factor = -0.30
				navy_advisor_cost_factor = -0.30
			}
		}
		MKN_preemptive_strike_idea = {
			picture = generic_army_war_college
			allowed = { original_tag = MKN }
			removal_cost = -1
			modifier = { justify_war_goal_time = -1 }
		}
		MKN_military_marches_idea = {
			picture = generic_army_war_college
			allowed = { original_tag = MKN }
			removal_cost = -1
			modifier = { compliance_gain = 0.10 }
		}
		MKN_permanent_revolution_idea = {
			picture = generic_army_war_college
			allowed = { original_tag = MKN }
			removal_cost = -1
			modifier = {
				army_speed_factor = 0.30
				breakthrough_factor = 0.20
				supply_consumption_factor = -0.20
				trade_opinion_factor = -1
			}
		}
	}
}
```

## common/unit_leader/MKN_militarist_traits.txt

Новый файл целиком.

```pdx
leader_traits = {
	mkn_council_member_trait = {
		type = land
		trait_type = personality_trait
		gain_xp = { always = no }
		new_commander_weight = { factor = 0 }
		modifier = { army_attack_factor = 0.10 planning_speed = 0.20 }
	}
}
```

## common/country_leader/MKN_militarist_traits.txt

Новый файл целиком.

```pdx
leader_traits = {
	mkn_supreme_warlord = {
		sprite = 15
		random = no
		army_attack_factor = 0.40
		war_support_factor = 0.40
	}
}
```

## interface/MKN_militarist_traits.gfx

Новый файл целиком.

```pdx
spriteTypes = {
	spriteType = {
		name = "GFX_trait_mkn_council_member_trait"
		texturefile = "gfx/interface/traits/personal/trait_brilliant_strategist.dds"
	}
}
```

## common/autonomous_states/MKN_military_march.txt

Новый файл целиком.

```pdx
# Owner: MKN. Native AAT/WUW autonomy format; no vanilla autonomy file is replaced.
autonomy_state = {
	id = autonomy_mkn_military_march
	default = yes
	is_puppet = yes
	min_freedom_level = 0.0
	manpower_influence = 1.0
	use_overlord_color = yes
	rule = {
		desc = RULE_DESC_IS_A_SUBJECT
		can_not_declare_war = yes
		can_decline_call_to_war = no
		units_deployed_to_overlord = yes
		can_be_spymaster = no
		contributes_operatives = no
		can_create_collaboration_government = no
	}
	modifier = {
		autonomy_manpower_share = 1.0
		can_master_build_for_us = 1
		cic_to_overlord_factor = 0.90
		mic_to_overlord_factor = 0.90
	}
	allowed = {
		has_government = fascism
		OVERLORD = {
			original_tag = MKN
			has_government = fascism
			has_completed_focus = MKN_military_marches
		}
	}
	can_take_level = {
		has_government = fascism
		OVERLORD = {
			original_tag = MKN
			has_government = fascism
			has_completed_focus = MKN_military_marches
		}
	}
	can_lose_level = { always = no }
	ai_subject_wants_higher = { factor = 1 }
	ai_overlord_wants_lower = { factor = 0 }
	ai_overlord_wants_garrison = { always = yes }
}
```

## common/dynamic_modifiers/MKN_militarist_modifiers.txt

Новый файл целиком.

```pdx
# State-scoped, country-restricted, following SOV_seraya_loshad_battery.
MKN_fortified_district_modifier = {
	enable = {
		has_state_flag = MKN_district_fortified
		is_owned_and_controlled_by = MKN
		is_core_of = MKN
	}
	icon = GFX_modifiers_SOV_armored_battery
	army_defence_factor = 0.20
}
```

## common/decisions/categories/MKN_militarist_categories.txt

Новый файл целиком.

```pdx
MKN_military_districts_decisions = {
	icon = military_operation
	allowed = { original_tag = MKN }
	visible = { has_completed_focus = MKN_military_districts }
}
MKN_military_marches_decisions = {
	icon = military_operation
	allowed = { original_tag = MKN }
	visible = { has_completed_focus = MKN_military_marches }
}
```

## common/decisions/MKN_military_decisions.txt — новые категории

Добавить эти два блока верхнего уровня после существующих категорий армейского, авиационного и морского штабов. Существующее содержимое файла сохранить.

```pdx
MKN_military_districts_decisions = {
    MKN_fortify_military_district = {
        icon = generic_construction
        allowed = {
            original_tag = MKN
        }
        state_target = yes
        on_map_mode = map_and_decisions_view
        target_array = ROOT.owned_states
        target_root_trigger = {
            original_tag = MKN
            has_completed_focus = MKN_military_districts
        }
        target_trigger = {
            FROM = {
                is_owned_and_controlled_by = ROOT
                is_core_of = ROOT
                NOT = {
                    has_state_flag = MKN_district_fortified
                }
            }
        }
        visible = {
            has_completed_focus = MKN_military_districts
        }
        available = {
            has_government = fascism
            has_capitulated = no
            custom_trigger_tooltip = {
                tooltip = MKN_district_project_idle_tt
                NOT = {
                    has_country_flag = MKN_district_project_active
                }
            }
            FROM = {
                is_owned_and_controlled_by = ROOT
                is_fully_controlled_by = ROOT
                is_core_of = ROOT
                infrastructure < 5
                NOT = {
                    has_state_flag = MKN_district_fortified
                }
            }
        }
        cost = 0
        custom_cost_text = MKN_district_cost_20_cp
        custom_cost_trigger = {
            NOT = {
                command_power < 20
            }
        }
        days_remove = 30
        complete_effect = {
            add_command_power = -20
            set_country_flag = MKN_district_project_active
        }
        cancel_trigger = {
            NOT = {
                AND = {
                    has_government = fascism
                    has_capitulated = no
                    FROM = {
                        is_owned_and_controlled_by = ROOT
                        is_fully_controlled_by = ROOT
                        is_core_of = ROOT
                        infrastructure < 5
                        NOT = {
                            has_state_flag = MKN_district_fortified
                        }
                    }
                }
            }
        }
        cancel_effect = {
            add_command_power = 20
            clr_country_flag = MKN_district_project_active
        }
        remove_effect = {
            if = {
                limit = {
                    has_government = fascism
                    has_capitulated = no
                    FROM = {
                        is_owned_and_controlled_by = ROOT
                        is_fully_controlled_by = ROOT
                        is_core_of = ROOT
                        infrastructure < 5
                        NOT = {
                            has_state_flag = MKN_district_fortified
                        }
                    }
                }
                FROM = {
                    if = {
                        limit = {
                            infrastructure < 4
                        }
                        add_building_construction = {
                            type = infrastructure
                            level = 2
                            instant_build = yes
                        }
                    }
                    else = {
                        add_building_construction = {
                            type = infrastructure
                            level = 1
                            instant_build = yes
                        }
                    }
                    set_state_flag = MKN_district_fortified
                    add_dynamic_modifier = {
                        modifier = MKN_fortified_district_modifier
                        scope = ROOT
                    }
                }
            }
            else = {
                add_command_power = 20
            }
            clr_country_flag = MKN_district_project_active
        }
        ai_will_do = {
            factor = 1
        }
    }
}
MKN_military_marches_decisions = {
    MKN_establish_military_march = {
        icon = generic_operation
        allowed = {
            original_tag = MKN
        }
        target_root_trigger = {
            original_tag = MKN
            has_completed_focus = MKN_military_marches
        }
        target_trigger = {
            FROM = {
                is_subject_of = ROOT
                has_government = fascism
                NOT = {
                    has_autonomy_state = autonomy_mkn_military_march
                }
            }
        }
        visible = {
            has_completed_focus = MKN_military_marches
        }
        available = {
            has_government = fascism
            has_capitulated = no
            FROM = {
                is_subject_of = ROOT
                has_government = fascism
                NOT = {
                    has_autonomy_state = autonomy_mkn_military_march
                }
            }
        }
        cost = 0
        complete_effect = {
            set_autonomy = {
                target = FROM
                autonomy_state = autonomy_mkn_military_march
                freedom_level = 0.0
                end_wars = no
                end_civil_wars = no
            }
        }
        ai_will_do = {
            factor = 2
        }
    }
}
```

## common/scripted_effects/MKN_militarist_effects.txt

Новый файл целиком.

```pdx
# Called inside the existing rebuilds, after their variables have been reset.
# These are reconstruction effects, never repeat one-off focus rewards here.
MKN_rebuild_militarist_industry_stats = {
	if = {
		limit = { has_completed_focus = MKN_schools_of_young_insurgents }
		add_to_variable = { MKN_unified_training_time_army_factor = -0.20 }
		add_to_variable = { MKN_unified_research_speed_factor = -0.16 }
	}
}
MKN_rebuild_militarist_army_stats = {
	if = {
		limit = { has_completed_focus = MKN_military_districts }
		add_to_variable = { MKN_army_supply_consumption_factor = 0.16 }
	}
	if = {
		limit = { has_completed_focus = MKN_schools_of_young_insurgents }
		add_to_variable = { MKN_army_conscription = 0.06 }
	}
	if = {
		limit = { has_completed_focus = MKN_cult_of_fallen_atamans }
		add_to_variable = { MKN_army_casualty_trickleback = 0.10 }
	}
}
MKN_repair_militarist_progression = {
	if = {
		limit = { NOT = { has_country_flag = MKN_militarist_progression_v3 } }
		nww_mkn_rebuild_industry = yes
		nww_mkn_rebuild_services = yes
		set_country_flag = MKN_militarist_progression_v3
	}
}
```

## common/on_actions/MKN_militarist_on_actions.txt

Новый файл целиком.

```pdx
on_actions = {
	on_startup = {
		effect = {
			MKN = {
				if = {
					limit = { exists = yes }
					MKN_repair_militarist_progression = yes
				}
			}
		}
	}
	on_daily_MKN = {
		effect = { MKN_repair_militarist_progression = yes }
	}
}
```

## common/scripted_effects/nww_mkn_progression.txt — два подключения пересчёта

В конце `nww_mkn_rebuild_industry`, непосредственно перед существующей установкой `MKN_industry_integration_v4`, должны стоять следующие строки:

```pdx
	MKN_rebuild_militarist_industry_stats = yes
	set_country_flag = MKN_industry_integration_v4
```

Внутри `nww_mkn_rebuild_services`, сразу после существующего вызова `MKN_rebuild_horizons_service_stats`, должны стоять следующие строки:

```pdx
	MKN_rebuild_horizons_service_stats = yes
	MKN_rebuild_militarist_army_stats = yes
```

Это вставки в существующие определения, а не новые определения одноимённых эффектов. Остальные условия, сбросы переменных и версии миграции этих эффектов сохраняются.

## localisation/russian/MKN_militarist_l_russian.yml

Новый файл целиком. Сохранить как UTF-8 с BOM.

```yaml
l_russian:
 MKN_field_counter_intelligence:0 "Полевая контрразведка"
 MKN_field_counter_intelligence_desc:0 "Враг прячет оружие под шинелью связного и приказ — в письме домой. Полевые особые отделы проверят каждый штаб, каждый эшелон и каждое донесение. Чёрное знамя не станет прикрытием для чужой разведки."
 MKN_disarming_the_communes:0 "Разоружение коммун"
 MKN_disarming_the_communes_desc:0 "Винтовки должны лежать в армейских арсеналах, а не под скамьями сельских собраний. Коммуны сдадут оружие по описи. Отныне право на вооружённую силу принадлежит только Повстанческой армии."
 MKN_tribunals_of_the_black_staff:0 "Трибуналы Чёрного штаба"
 MKN_tribunals_of_the_black_staff_desc:0 "Дезертирство, растрата снабжения и саботаж будут разбираться там, где совершены: перед строем. Трибунал выслушает свидетелей, огласит приказ и вернёт полк к выполнению задачи. Отступление без приказа больше не оправдать речами."
 MKN_labor_armies:0 "Трудовые армии"
 MKN_labor_armies_desc:0 "Заводские смены объявляются боевыми задачами. Забастовка приравнивается к мятежу перед лицом врага. Вместо новых соглашений с гражданскими собраниями штаб вводит трудовые батальоны, нормы выработки и единый приказ для всего тыла."
 MKN_schools_of_young_insurgents:0 "Школы юных повстанцев"
 MKN_schools_of_young_insurgents_desc:0 "Строевая площадка станет продолжением школьного двора. Будущие призывники научатся читать карту, перевязывать раненых и держать строй ещё до повестки. Часы естественных наук отданы огневой подготовке: армия получает обученное пополнение ценой академического кризиса."
 MKN_cult_of_fallen_atamans:0 "Культ павших атаманов"
 MKN_cult_of_fallen_atamans_desc:0 "Имена павших атаманов внесут в списки полков навечно. Их места на перекличке останутся пустыми, их раненых товарищей вернут в строй. Пока над казармой поднимается чёрный флаг, смерть командира не прервёт поход."
 MKN_military_districts:0 "Раздел на Военные округа"
 MKN_military_districts_desc:0 "Коммуны будут сведены в округа, связанные железной дорогой и подчинённые одному коменданту. Каждый округ обязан подготовить пути подвоза, оборонительные рубежи и резерв. Однако атаманы заводят собственные склады и требуют отдельного снабжения: единый тыл уступает место логистическому феодализму."
 MKN_council_of_field_commanders:0 "Совет Полевых Командиров"
 MKN_council_of_field_commanders_desc:0 "Три полевых командира получат места в постоянном совете при Чёрном штабе. Приказы будут опираться на опыт походов, а военные специалисты — получать назначения без прежних поборов. Спор допустим у карты; после подписания приказа он окончен."
 MKN_the_supreme_warlord:0 "Верховный Воевода"
 MKN_the_supreme_warlord_desc:0 "Тратишов соберёт полномочия округов и полевых штабов в одной ставке. Верховный Воевода отвечает за весь поход — от последнего патрона до первого удара. Личная власть станет постоянным порядком командования, а не новым поводом для смуты."
 MKN_preemptive_strike_doctrine:0 "Доктрина превентивного удара"
 MKN_preemptive_strike_doctrine_desc:0 "Ожидание даёт врагу время закрыть границу и наполнить склады. Штаб будет готовить обоснование войны одновременно с планом наступления. Удар должен опередить чужую мобилизацию."
 MKN_military_marches:0 "Военные Марки"
 MKN_military_marches_desc:0 "На освобождённых землях мы не строим старые границы. Мы создаём буферные зоны под управлением комендантов, чья единственная задача — снабжать Армию. Фашистские зависимые администрации могут быть преобразованы в Военные Марки."
 MKN_black_banner_over_europe:0 "Чёрное знамя над Европой"
 MKN_black_banner_over_europe_desc:0 "Революция не имеет границ. Пока в мире есть хоть один диктатор или президент, Повстанческая армия не вложит сабли в ножны. За передовыми колоннами пойдут эшелоны снабжения; каждый новый рубеж станет исходной позицией следующего похода."
 MKN_field_counter_intelligence_idea:0 "Особые отделы Чёрного штаба"
 MKN_field_counter_intelligence_idea_desc:0 "Контрразведчики действуют при полевых штабах. Два дополнительных оперативника, ускоренное оснащение агентства и проверка донесений защищают армейские планы."
 MKN_field_counter_intelligence_reserve_idea:0 "Полевые особые отделы"
 MKN_field_counter_intelligence_reserve_idea_desc:0 "Комендатуры проверяют курьеров, документы и доступ к армейским складам. Каждый маршрут снабжения и каждый связной поставлены на учёт полевых особых отделов."
 MKN_disarmed_communes_idea:0 "Разоружённые коммуны"
 MKN_disarmed_communes_idea_desc:0 "Арсеналы коммун опечатаны. Приказы штаба исполняются без переговоров с вооружёнными собраниями, но купцы боятся реквизиций, а сельские базары закрываются. Дефицит повседневных товаров требует отвлекать больше фабрик на нужды населения."
 MKN_tribunals_idea:0 "Трибуналы Чёрного штаба"
 MKN_tribunals_idea_desc:0 "Полковые трибуналы следят за сохранностью людей и имущества. Снабжение учитывают строго, а мысль о капитуляции пресекают прежде, чем она станет приказом. Страх перед обвинением парализует гражданскую инициативу: каждый ждёт разрешения штаба."
 MKN_labor_armies_idea:0 "Трудовые армии"
 MKN_labor_armies_idea_desc:0 "Рабочие сведены в батальоны, мастера отвечают за выполнение плана как за боевую задачу. Военные заказы растут, гражданские стройки заброшены. Ненависть к казарменным порядкам подтачивает устойчивость режима."
 MKN_council_of_commanders_idea:0 "Совет Чёрного штаба"
 MKN_council_of_commanders_idea_desc:0 "Полевые командиры определяют назначения военных специалистов. Единый порядок уменьшает стоимость привлечения армейских, авиационных и морских советников."
 MKN_preemptive_strike_idea:0 "Опережающая мобилизация"
 MKN_preemptive_strike_idea_desc:0 "Штаб готовит политическое обоснование удара ещё до завершения развёртывания. Война начинается в срок, назначенный нашими командирами."
 MKN_military_marches_idea:0 "Комендантское управление"
 MKN_military_marches_idea_desc:0 "Оккупационная администрация подчинена снабжению армии. Учёт населения, дорог и поставок ускоряет установление контроля над занятыми землями."
 MKN_permanent_revolution_idea:0 "Перманентный поход"
 MKN_permanent_revolution_idea_desc:0 "Армия живёт в движении. Штабы сокращают обозы, колонны наращивают темп, а прорыв обороны становится началом следующего марша. Соседние правительства отвечают торговой изоляцией: за чёрным знаменем закрываются рынки."
 mkn_council_member_trait:0 "Член Совета Полевых Командиров"
 mkn_council_member_trait_desc:0 "Командир допущен к планам Чёрного штаба. Его соединения действуют решительнее и быстрее готовят операции."
 mkn_supreme_warlord:0 "Верховный Воевода"
 mkn_supreme_warlord_desc:0 "Тратишов возглавляет постоянную ставку. Власть Воеводы усиливает натиск армии и поддержку войны, не снижая стабильность."
 autonomy_mkn_military_march:0 "Военная Марка"
 autonomy_mkn_military_march_desc:0 "Фашистская зависимая администрация Махновщины: 90% гражданских и военных фабрик передаются сюзерену, доля людских ресурсов в дивизиях из зависимой территории — 100%. Самостоятельное объявление войны запрещено."
 MKN_military_districts_decisions:0 "Военные округа"
 MKN_military_districts_decisions_desc:0 "Коменданты готовят коренные области к обороне и переброске войск. Штаб ведёт один проект одновременно; каждый округ укрепляется только один раз."
 MKN_fortify_military_district:0 "Укрепить военный округ: [FROM.GetName]"
 MKN_fortify_military_district_desc:0 "За 30 дней укрепить округ: инфраструктура до +2 (максимум 5) и защита наших дивизий в области +20%. Требуется коренная, полностью контролируемая область с инфраструктурой ниже 5. При отмене проекта 20 командного ресурса возвращаются."
 MKN_fortified_district_modifier:0 "Укреплённый военный округ"
 MKN_fortified_district_modifier_desc:0 "Подготовленные рубежи и дороги дают дивизиям Махновщины +20% к защите в этой коренной области, пока она принадлежит нам и находится под нашим контролем."
 MKN_military_marches_decisions:0 "Комендатуры Военных Марок"
 MKN_military_marches_decisions_desc:0 "Существующие фашистские марионетки могут быть переведены под непосредственное комендантское управление Чёрного штаба."
 MKN_establish_military_march:0 "Учредить Военную Марку: [FROM.GetName]"
 MKN_establish_military_march_desc:0 "Преобразовать нашу фашистскую марионетку в Военную Марку. Новый статус передаёт нам 90% её гражданских и военных фабрик и позволяет использовать 100% людских ресурсов в дивизиях из зависимой территории. Текущие войны продолжаются."
 MKN_counter_intelligence_research:0 "Вычислительная техника особых отделов"
 MKN_unlock_military_districts_tt:0 "Открывает решения §YВоенные округа§!: за §Y20£command_power§! и §Y30 дней§! — инфраструктура до §G+2§! (максимум 5) и защита наших дивизий в выбранной коренной области §G+20%§!."
 MKN_unlock_military_marches_tt:0 "Открывает статус §YВоенная Марка§! для фашистских марионеток и решение об их преобразовании. Передача фабрик: §Y90%§! гражданских и военных; доля людских ресурсов в дивизиях из зависимой территории: §Y100%§!. Марки не могут самостоятельно объявлять войны."
 MKN_labor_armies_lock_tt:0 "Блокирует ещё не завершённые политические фокусы §Y$MKN_pact_of_free_communes$§!, §Y$MKN_grain_ultimatum$§! и §Y$MKN_purge_irreconcilables$§!. Ранее полученные награды сохраняются."
 MKN_civil_settlement_allowed_tt:0 "Фокус §YТрудовые армии§! не завершён"
 MKN_district_project_idle_tt:0 "Другой военный округ сейчас не укрепляется"
 MKN_district_cost_20_cp:0 "£command_power §Y20§!"
```

## localisation/english/MKN_militarist_l_english.yml

Новый файл целиком. Сохранить как UTF-8 с BOM.

```yaml
l_english:
 MKN_field_counter_intelligence:0 "Field Counterintelligence"
 MKN_field_counter_intelligence_desc:0 "The enemy hides a weapon beneath a courier’s coat and orders inside a letter home. Field security sections will inspect every headquarters, every train and every dispatch. The black banner will give no shelter to foreign intelligence."
 MKN_disarming_the_communes:0 "Disarming the Communes"
 MKN_disarming_the_communes_desc:0 "Rifles belong in army arsenals, not beneath the benches of village assemblies. Every commune will surrender its weapons against an inventory. The Insurgent Army alone will wield armed force."
 MKN_tribunals_of_the_black_staff:0 "Tribunals of the Black Staff"
 MKN_tribunals_of_the_black_staff_desc:0 "Desertion, stolen supplies and sabotage will be judged where they occur: before the ranks. The tribunal will hear witnesses, read its sentence and return the regiment to its task. Speeches will no longer excuse an unauthorized retreat."
 MKN_labor_armies:0 "Labor Armies"
 MKN_labor_armies_desc:0 "Factory shifts are declared combat assignments. A strike is treated as mutiny in the face of the enemy. In place of further bargains with civilian assemblies, headquarters imposes labor battalions, production quotas and a single command over the rear."
 MKN_schools_of_young_insurgents:0 "Schools of Young Insurgents"
 MKN_schools_of_young_insurgents_desc:0 "The drill ground will extend the schoolyard. Future conscripts will learn to read a map, dress a wound and hold formation before receiving their call-up. Science lessons give way to weapons training: the army gains trained recruits at the cost of an academic crisis."
 MKN_cult_of_fallen_atamans:0 "Cult of the Fallen Atamans"
 MKN_cult_of_fallen_atamans_desc:0 "The fallen atamans’ names will remain on regimental rolls forever. Their places at roll call will stand empty; their wounded comrades will return to the ranks. As long as the black flag rises over the barracks, a commander’s death will not end the march."
 MKN_military_districts:0 "Establish Military Districts"
 MKN_military_districts_desc:0 "Communes will be grouped into districts linked by rail and placed under a single commandant. Every district must prepare supply routes, defensive positions and reserves. Yet the atamans maintain separate depots and demand their own deliveries, fragmenting army logistics into competing fiefdoms."
 MKN_council_of_field_commanders:0 "Council of Field Commanders"
 MKN_council_of_field_commanders_desc:0 "Three field commanders will receive seats on the Black Staff’s standing council. Campaign experience will guide its orders, and military specialists will be appointed at reduced cost. Debate is permitted over the map; once the order is signed, it ends."
 MKN_the_supreme_warlord:0 "The Supreme Warlord"
 MKN_the_supreme_warlord_desc:0 "Tratishov will gather the authority of district commands and field staffs into one supreme headquarters. The Supreme Warlord answers for the whole campaign, from the last cartridge to the opening attack. Personal rule will become a settled chain of command."
 MKN_preemptive_strike_doctrine:0 "Preemptive Strike Doctrine"
 MKN_preemptive_strike_doctrine_desc:0 "Waiting gives the enemy time to close the frontier and fill its depots. Headquarters will prepare the case for war alongside its offensive plans. Our attack must precede the enemy’s mobilization."
 MKN_military_marches:0 "Military Marches"
 MKN_military_marches_desc:0 "On liberated lands we will establish buffer territories under commandants whose sole task is to supply the Army. Fascist subject administrations may be reorganized into Military Marches, bound to the Black Staff’s campaigns."
 MKN_black_banner_over_europe:0 "Black Banner over Europe"
 MKN_black_banner_over_europe_desc:0 "The revolution has no borders. While a dictator or president remains anywhere in the world, the Insurgent Army will not sheathe its sabres. Supply trains will follow the advance, and every captured line will become the starting point of another campaign."
 MKN_field_counter_intelligence_idea:0 "Black Staff Security Sections"
 MKN_field_counter_intelligence_idea_desc:0 "Counterintelligence sections operate alongside field headquarters. Two additional operatives, faster agency upgrades and screened dispatches protect army plans."
 MKN_field_counter_intelligence_reserve_idea:0 "Field Security Sections"
 MKN_field_counter_intelligence_reserve_idea_desc:0 "Commandants screen couriers, papers and access to army depots. Field security sections keep registers of every supply route and every messenger."
 MKN_disarmed_communes_idea:0 "Disarmed Communes"
 MKN_disarmed_communes_idea_desc:0 "Communal arsenals are sealed. Headquarters no longer bargains with armed assemblies, but merchants fear requisitions and rural markets close. Shortages of everyday goods require more factories to serve civilian demand."
 MKN_tribunals_idea:0 "Tribunals of the Black Staff"
 MKN_tribunals_idea_desc:0 "Regimental tribunals enforce the preservation of personnel and equipment. Supplies are strictly accounted for, and talk of surrender is suppressed before it becomes an order. Fear of prosecution paralyzes civilian initiative: everyone waits for permission from headquarters."
 MKN_labor_armies_idea:0 "Labor Armies"
 MKN_labor_armies_idea_desc:0 "Workers are organized into battalions, and foremen answer for production plans as combat assignments. Military orders expand while civilian construction is abandoned. Hatred of barracks discipline erodes the regime’s stability."
 MKN_council_of_commanders_idea:0 "Council of the Black Staff"
 MKN_council_of_commanders_idea_desc:0 "Field commanders oversee military appointments. A common procedure reduces the cost of army, air force and naval advisors."
 MKN_preemptive_strike_idea:0 "Preemptive Mobilization"
 MKN_preemptive_strike_idea_desc:0 "Headquarters prepares the political case for an attack before deployment is complete. War begins on the date set by our commanders."
 MKN_military_marches_idea:0 "Commandant Administration"
 MKN_military_marches_idea_desc:0 "Occupation administration serves army supply. Registers of population, roads and deliveries accelerate the establishment of control over occupied lands."
 MKN_permanent_revolution_idea:0 "The Permanent Campaign"
 MKN_permanent_revolution_idea_desc:0 "The army lives on the move. Staffs trim supply trains, columns accelerate their advance, and every breakthrough begins the next march. Neighboring governments answer with trade isolation: markets close behind the black banner."
 mkn_council_member_trait:0 "Field Commanders’ Council Member"
 mkn_council_member_trait_desc:0 "This commander has access to the Black Staff’s plans. His formations attack more decisively and prepare operations faster."
 mkn_supreme_warlord:0 "Supreme Warlord"
 mkn_supreme_warlord_desc:0 "Tratishov heads the permanent supreme headquarters. The Warlord’s authority strengthens the army’s attack and support for war without reducing stability."
 autonomy_mkn_military_march:0 "Military March"
 autonomy_mkn_military_march_desc:0 "A fascist subject administration of Makhnovshchina: 90% of civilian and military factories go to the overlord; the subject manpower share in subject-template divisions is 100%. Independent declarations of war are forbidden."
 MKN_military_districts_decisions:0 "Military Districts"
 MKN_military_districts_decisions_desc:0 "Commandants prepare core states for defense and troop movements. Headquarters supervises one project at a time; each district can be fortified once."
 MKN_fortify_military_district:0 "Fortify Military District: [FROM.GetName]"
 MKN_fortify_military_district_desc:0 "Fortify the district over 30 days: up to +2 infrastructure (maximum level 5) and +20% defense for our divisions in the state. Requires a fully controlled core state with infrastructure below 5. Cancellation refunds the 20 command power cost."
 MKN_fortified_district_modifier:0 "Fortified Military District"
 MKN_fortified_district_modifier_desc:0 "Prepared positions and roads grant Makhnovshchina’s divisions +20% defense in this core state while it remains owned and controlled by us."
 MKN_military_marches_decisions:0 "Military March Commandancies"
 MKN_military_marches_decisions_desc:0 "Existing fascist subjects may be placed under the Black Staff’s direct commandant administration."
 MKN_establish_military_march:0 "Establish Military March: [FROM.GetName]"
 MKN_establish_military_march_desc:0 "Reorganize our fascist subject into a Military March. The new status transfers 90% of its civilian and military factories to us and allows a 100% subject manpower share in subject-template divisions. Existing wars continue."
 MKN_counter_intelligence_research:0 "Security Sections’ Computing Research"
 MKN_unlock_military_districts_tt:0 "Unlocks §YMilitary Districts§! decisions: spend §Y20£command_power§! over §Y30 days§! for up to §G+2§! infrastructure (maximum level 5) and §G+20%§! defense for our divisions in a selected core state."
 MKN_unlock_military_marches_tt:0 "Unlocks §YMilitary March§! status for fascist subjects and a decision to reorganize them. Factory contribution: §Y90%§! civilian and military; subject manpower share in subject-template divisions: §Y100%§!. Marches cannot declare wars independently."
 MKN_labor_armies_lock_tt:0 "Blocks the §Y$MKN_pact_of_free_communes$§!, §Y$MKN_grain_ultimatum$§! and §Y$MKN_purge_irreconcilables$§! political focuses if not already completed. Previously earned rewards remain."
 MKN_civil_settlement_allowed_tt:0 "The §YLabor Armies§! focus has not been completed"
 MKN_district_project_idle_tt:0 "No other military district is currently being fortified"
 MKN_district_cost_20_cp:0 "£command_power §Y20§!"
```

## Проверки проекта

Новый валидатор `tools/validate_mkn_militarists.py` подключён к `tools/validate_country_content.py`. Интерпретаторы в `validate_mkn_military.py`, `validate_mkn_economy.py`, `validate_mkn_horizons.py` и проверка пересчёта в `validate_mkn_bop.py` учитывают новые эффекты. Эти инструменты не загружаются игрой.

```sh
python tools/validate_country_content.py --game '/home/dima00138/.local/share/Steam/steamapps/common/Hearts of Iron IV'
git diff --check
```

Результат: общая статическая проверка пройдена, включая 138 сценариев. Новая кампания, игровой tooltip, боевой эффект области и свежий игровой журнал в этой сессии не проверялись.
