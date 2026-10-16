# MKN: готовые блоки файлов Ревкома

Код уже внесён в проект. Все новые бонусы и штрафы ×2; фактор ТНП ×3 от исходного задания (+5% → +15%). По уточнению пользователя организация снижается у всех вражеских войск на нашей земле. Механики, баланс, аудит остальных территориальных штрафов и образцы DLC: [MKN_communists.md](MKN_communists.md).

## common/national_focus/MKN.txt

Добавить внутрь существующего `focus_tree`. Прежние определения сохраняются. У комиссаров и танковых корпусов второй межветочный допуск размещён в `available`, чтобы не проводить лишние линии.

```pdx
focus = {
    id = MKN_steppe_sovnarkhoz
    icon = GFX_focus_MKN_steppe_sovnarkhoz
    x = 94
    y = 6
    cost = 5
    prerequisite = {
        focus = MKN_embassy_to_kharkov
    }
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    available = {
        has_government = communism
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    completion_reward = {
        add_ideas = MKN_sovnarkhoz_idea
    }
    ai_will_do = {
        factor = 2
    }
}
focus = {
    id = MKN_artel_state_farms
    icon = GFX_focus_MKN_artel_state_farms
    x = 94
    y = 7
    cost = 5
    prerequisite = {
        focus = MKN_steppe_sovnarkhoz
    }
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    available = {
        has_government = communism
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    completion_reward = {
        add_ideas = MKN_state_farms_idea
    }
    ai_will_do = {
        factor = 2
    }
}
focus = {
    id = MKN_dnieper_five_year_plan
    icon = GFX_focus_MKN_dnieper_five_year_plan
    x = 94
    y = 8
    cost = 5
    prerequisite = {
        focus = MKN_artel_state_farms
    }
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    available = {
        has_government = communism
        226 = {
            is_owned_and_controlled_by = ROOT
        }
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    completion_reward = {
        add_to_variable = {
            MKN_unified_industrial_capacity_factory = 0.20
            tooltip = MKN_unified_industrial_capacity_factory_tt
        }
        add_to_variable = {
            MKN_unified_consumer_goods_factor = 0.15
            tooltip = MKN_unified_consumer_goods_factor_tt
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_revkom_nikopol_reward
                    }
                }
            }
            226 = {
                if = {
                    limit = {
                        is_owned_and_controlled_by = ROOT
                    }
                    add_extra_state_shared_building_slots = 8
                    add_building_construction = {
                        type = industrial_complex
                        level = 4
                        instant_build = yes
                    }
                    add_building_construction = {
                        type = arms_factory
                        level = 4
                        instant_build = yes
                    }
                }
            }
            set_country_flag = MKN_revkom_nikopol_reward
        }
    }
    ai_will_do = {
        factor = 2
    }
}
focus = {
    id = MKN_political_commissars
    icon = GFX_focus_MKN_political_commissars
    x = 94
    y = 9
    cost = 5
    prerequisite = {
        focus = MKN_dnieper_five_year_plan
    }
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    available = {
        has_government = communism
        has_completed_focus = MKN_red_military_specialists
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    completion_reward = {
        add_ideas = MKN_commissars_idea
    }
    ai_will_do = {
        factor = 2
    }
}
focus = {
    id = MKN_red_armored_corps
    icon = GFX_focus_MKN_red_armored_corps
    x = 94
    y = 10
    cost = 5
    prerequisite = {
        focus = MKN_political_commissars
    }
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    available = {
        has_government = communism
        has_completed_focus = MKN_tractors_for_grain
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    completion_reward = {
        add_to_variable = {
            MKN_army_army_armor_attack_factor = 0.20
            tooltip = MKN_army_army_armor_attack_factor_tt
        }
        add_to_variable = {
            MKN_army_army_armor_speed_factor = 0.20
            tooltip = MKN_army_army_armor_speed_factor_tt
        }
        add_tech_bonus = {
            name = MKN_red_armored_corps
            bonus = 2.0
            uses = 1
            category = cat_medium_armor
            category = cat_heavy_armor
        }
    }
    ai_will_do = {
        factor = 2
    }
}
focus = {
    id = MKN_equal_shield_of_socialism
    icon = GFX_focus_MKN_equal_shield_of_socialism
    x = 94
    y = 11
    cost = 5
    prerequisite = {
        focus = MKN_the_fatal_plenum
    }
    mutually_exclusive = {
        focus = MKN_true_socialism_against_bureaucrats
    }
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    available = {
        has_government = communism
        custom_trigger_tooltip = {
            tooltip = MKN_revkom_equal_path_tt
            MKN_revkom_equal_path = yes
        }
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    completion_reward = {
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_revkom_offsite_reward
                    }
                }
            }
            add_offsite_building = {
                type = industrial_complex
                level = 6
            }
            set_country_flag = MKN_revkom_offsite_reward
        }
        custom_effect_tooltip = MKN_revkom_equal_trade_tt
        hidden_effect = {
            MKN_sync_revkom_trade = yes
        }
    }
    ai_will_do = {
        factor = 2
    }
}
focus = {
    id = MKN_industrial_ram_of_comintern
    icon = GFX_focus_MKN_industrial_ram_of_comintern
    x = 94
    y = 12
    cost = 5
    prerequisite = {
        focus = MKN_equal_shield_of_socialism
    }
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    available = {
        has_government = communism
        custom_trigger_tooltip = {
            tooltip = MKN_revkom_equal_path_tt
            MKN_revkom_equal_path = yes
        }
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    completion_reward = {
        add_ideas = MKN_comintern_ram_idea
    }
    ai_will_do = {
        factor = 2
    }
}
focus = {
    id = MKN_red_brotherhood_in_arms
    icon = GFX_focus_MKN_red_brotherhood_in_arms
    x = 94
    y = 13
    cost = 5
    prerequisite = {
        focus = MKN_industrial_ram_of_comintern
    }
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    available = {
        has_government = communism
        custom_trigger_tooltip = {
            tooltip = MKN_revkom_equal_path_tt
            MKN_revkom_equal_path = yes
        }
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    completion_reward = {
        custom_effect_tooltip = MKN_revkom_brotherhood_tt
        hidden_effect = {
            MKN_sync_revkom_combat = yes
        }
        add_doctrine_cost_reduction = {
            name = MKN_red_brotherhood_land
            cost_reduction = 1.0
            uses = 1
            category = land_doctrine
        }
        add_doctrine_cost_reduction = {
            name = MKN_red_brotherhood_air
            cost_reduction = 1.0
            uses = 1
            category = air_doctrine
        }
    }
    ai_will_do = {
        factor = 2
    }
}
focus = {
    id = MKN_true_socialism_against_bureaucrats
    icon = GFX_focus_MKN_true_socialism_against_bureaucrats
    x = 98
    y = 11
    cost = 5
    prerequisite = {
        focus = MKN_the_fatal_plenum
    }
    mutually_exclusive = {
        focus = MKN_equal_shield_of_socialism
    }
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    available = {
        has_government = communism
        custom_trigger_tooltip = {
            tooltip = MKN_revkom_betrayal_path_tt
            MKN_revkom_betrayal_path = yes
        }
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    completion_reward = {
        add_to_variable = {
            MKN_army_army_core_defence_factor = 0.40
            tooltip = MKN_army_army_core_defence_factor_tt
        }
        custom_effect_tooltip = MKN_revkom_desertion_tt
        hidden_effect = {
            MKN_sync_revkom_combat = yes
        }
    }
    ai_will_do = {
        factor = 2
    }
}
focus = {
    id = MKN_liberation_of_soviet_ukraine
    icon = GFX_focus_MKN_liberation_of_soviet_ukraine
    x = 98
    y = 12
    cost = 5
    prerequisite = {
        focus = MKN_true_socialism_against_bureaucrats
    }
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    available = {
        has_government = communism
        custom_trigger_tooltip = {
            tooltip = MKN_revkom_betrayal_path_tt
            MKN_revkom_betrayal_path = yes
        }
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    completion_reward = {
        192 = {
            add_core_of = ROOT
        }
        197 = {
            add_core_of = ROOT
        }
        202 = {
            add_core_of = ROOT
        }
        225 = {
            add_core_of = ROOT
        }
        259 = {
            add_core_of = ROOT
        }
        add_war_support = 0.40
    }
    ai_will_do = {
        factor = 2
    }
}
focus = {
    id = MKN_strike_at_the_kremlin
    icon = GFX_focus_MKN_strike_at_the_kremlin
    x = 98
    y = 13
    cost = 5
    prerequisite = {
        focus = MKN_liberation_of_soviet_ukraine
    }
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    available = {
        has_government = communism
        custom_trigger_tooltip = {
            tooltip = MKN_revkom_betrayal_path_tt
            MKN_revkom_betrayal_path = yes
        }
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    completion_reward = {
        add_to_variable = {
            MKN_army_army_speed_factor = 0.30
            tooltip = MKN_army_army_speed_factor_tt
        }
        custom_effect_tooltip = MKN_revkom_kremlin_attack_tt
        hidden_effect = {
            MKN_sync_revkom_combat = yes
        }
        if = {
            limit = {
                SOV = {
                    exists = yes
                    NOT = {
                        is_subject_of = ROOT
                    }
                }
                NOT = {
                    has_war_with = SOV
                }
                NOT = {
                    is_in_faction_with = SOV
                }
                NOT = {
                    is_subject_of = SOV
                }
                MKN_revkom_betrayal_path = yes
            }
            create_wargoal = {
                type = annex_everything
                target = SOV
            }
        }
    }
    ai_will_do = {
        factor = 2
    }
}
focus = {
    id = MKN_red_beacon_of_the_east
    icon = GFX_focus_MKN_red_beacon_of_the_east
    x = 96
    y = 14
    cost = 5
    prerequisite = {
        focus = MKN_red_brotherhood_in_arms
        focus = MKN_strike_at_the_kremlin
    }
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    available = {
        has_government = communism
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    completion_reward = {
        add_ideas = MKN_red_beacon_idea
    }
    ai_will_do = {
        factor = 2
    }
}
```

## common/ideas/MKN_communist_ideas.txt

Новый файл целиком.

```pdx
# Owner: MKN Revkom. All requested modifiers x2; consumer goods x3 instead.
ideas = {
	country = {
		MKN_sovnarkhoz_idea = {
			picture = generic_industrial_concern_1
			allowed = { original_tag = MKN }
			removal_cost = -1
			modifier = {
				production_speed_industrial_complex_factor = 0.30
				production_speed_arms_factory_factor = 0.30
				production_factory_efficiency_gain_factor = -0.20
			}
		}
		MKN_state_farms_idea = {
			picture = generic_industrial_concern_1
			allowed = { original_tag = MKN }
			removal_cost = -1
			modifier = { supply_consumption_factor = -0.20 stability_factor = -0.20 }
		}
		MKN_commissars_idea = {
			picture = generic_army_war_college
			allowed = { original_tag = MKN }
			removal_cost = -1
			modifier = { army_org_factor = 0.20 army_morale_factor = 0.20 planning_speed = -0.30 }
		}
		MKN_comintern_ram_idea = {
			picture = generic_industrial_concern_1
			allowed = { original_tag = MKN }
			removal_cost = -1
			modifier = { industrial_capacity_factory = 0.20 }
			equipment_bonus = {
				armor = { build_cost_ic = -0.20 instant = yes }
				artillery = { build_cost_ic = -0.20 instant = yes }
			}
		}
		MKN_red_beacon_idea = {
			picture = generic_industrial_concern_1
			allowed = { original_tag = MKN }
			removal_cost = -1
			modifier = { stability_factor = 0.30 war_support_factor = 0.30 political_power_gain = 0.40 }
			# The focus asks for industry/electronics only, not global research.
			research_bonus = { industry = 0.20 electronics = 0.20 }
		}
		MKN_equal_shield_trade_idea = {
			picture = generic_industrial_concern_1
			allowed = { original_tag = MKN }
			removal_cost = -1
			modifier = { trade_opinion_factor = 0.60 }
		}
		# Bilateral definition owned by MKN; maintained only while the pact survives.
		MKN_equal_shield_partner_idea = {
			picture = generic_industrial_concern_1
			allowed = { tag = SOV }
			removal_cost = -1
			modifier = { trade_opinion_factor = 0.60 }
		}
		MKN_red_brotherhood_idea = {
			picture = generic_army_war_college
			allowed = { original_tag = MKN }
			removal_cost = -1
			modifier = { army_attack_factor = 0.20 }
		}
		MKN_kremlin_offensive_idea = {
			picture = generic_army_war_college
			allowed = { original_tag = MKN }
			removal_cost = -1
			targeted_modifier = { tag = SOV attack_bonus_against = 0.30 }
			modifier = { }
		}
	}
}
```

## common/scripted_triggers/MKN_communist_triggers.txt

Новый файл целиком.

```pdx
MKN_revkom_equal_path = {
	has_government = communism
	has_completed_focus = MKN_the_fatal_plenum
	has_country_flag = MKN_equal_autonomy
	NOT = { has_country_flag = MKN_soviet_betrayal }
}
MKN_revkom_betrayal_path = {
	has_government = communism
	has_completed_focus = MKN_the_fatal_plenum
	has_country_flag = MKN_soviet_betrayal
	NOT = { has_country_flag = MKN_equal_autonomy }
	NOT = { SOV = { has_country_flag = NWW_SOV_MKN_settlement } }
}
MKN_revkom_trade_active = {
	exists = yes
	MKN_revkom_equal_path = yes
	has_completed_focus = MKN_equal_shield_of_socialism
	is_in_faction_with = SOV
	NOT = { has_war_with = SOV }
	SOV = { exists = yes has_government = communism }
}
MKN_revkom_joint_war = {
	MKN_revkom_equal_path = yes
	has_completed_focus = MKN_red_brotherhood_in_arms
	any_other_country = {
		exists = yes
		is_in_faction_with = MKN
		has_war_together_with = MKN
	}
}
```

## common/dynamic_modifiers/MKN_communist_modifiers.txt

Новый файл целиком.

```pdx
# Applied separately to each current enemy; never to MKN, allies or neutrals.
MKN_revkom_enemy_disorganization = {
	enable = {
		is_owned_and_controlled_by = MKN
		MKN = {
			has_government = communism
			has_completed_focus = MKN_true_socialism_against_bureaucrats
		}
	}
	icon = GFX_modifiers_SOV_armored_battery
	army_org_factor = -0.30
}
```

## common/scripted_effects/MKN_communist_effects.txt

Новый файл целиком.

```pdx
# Reconstruct parameters, never factories, cores, war support or research coupons.
MKN_rebuild_communist_industry_stats = {
	if = {
		limit = { has_completed_focus = MKN_dnieper_five_year_plan }
		add_to_variable = { MKN_unified_industrial_capacity_factory = 0.20 }
		add_to_variable = { MKN_unified_consumer_goods_factor = 0.15 }
	}
}
MKN_rebuild_communist_army_stats = {
	if = {
		limit = { has_completed_focus = MKN_red_armored_corps }
		add_to_variable = { MKN_army_army_armor_attack_factor = 0.20 }
		add_to_variable = { MKN_army_army_armor_speed_factor = 0.20 }
	}
	if = {
		limit = { has_completed_focus = MKN_true_socialism_against_bureaucrats }
		add_to_variable = { MKN_army_army_core_defence_factor = 0.40 }
	}
	if = {
		limit = { has_completed_focus = MKN_strike_at_the_kremlin }
		add_to_variable = { MKN_army_army_speed_factor = 0.30 }
	}
}
MKN_sync_revkom_trade = {
	if = {
		limit = { MKN = { MKN_revkom_trade_active = yes } }
		MKN = {
			if = {
				limit = { NOT = { has_idea = MKN_equal_shield_trade_idea } }
				add_ideas = MKN_equal_shield_trade_idea
			}
		}
		SOV = {
			if = {
				limit = { NOT = { has_idea = MKN_equal_shield_partner_idea } }
				add_ideas = MKN_equal_shield_partner_idea
			}
		}
	}
	else = {
		MKN = { remove_ideas = MKN_equal_shield_trade_idea }
		SOV = { remove_ideas = MKN_equal_shield_partner_idea }
	}
}
MKN_sync_revkom_combat = {
	if = {
		limit = { MKN_revkom_joint_war = yes }
		if = {
			limit = { NOT = { has_idea = MKN_red_brotherhood_idea } }
			add_ideas = MKN_red_brotherhood_idea
		}
	}
	else = { remove_ideas = MKN_red_brotherhood_idea }
	if = {
		limit = {
			MKN_revkom_betrayal_path = yes
			has_completed_focus = MKN_strike_at_the_kremlin
			SOV = { exists = yes }
			NOT = { is_in_faction_with = SOV }
		}
		if = {
			limit = { NOT = { has_idea = MKN_kremlin_offensive_idea } }
			add_ideas = MKN_kremlin_offensive_idea
		}
	}
	else = { remove_ideas = MKN_kremlin_offensive_idea }
	if = {
		limit = { has_completed_focus = MKN_true_socialism_against_bureaucrats }
		every_country = {
			limit = { OR = { has_war_with = MKN has_country_flag = MKN_revkom_disorganization_active } }
			save_event_target_as = MKN_revkom_enemy
			MKN = {
				every_owned_state = {
					if = {
						limit = { has_dynamic_modifier = { modifier = MKN_revkom_enemy_disorganization scope = event_target:MKN_revkom_enemy } }
						remove_dynamic_modifier = { modifier = MKN_revkom_enemy_disorganization scope = event_target:MKN_revkom_enemy }
					}
					if = {
						limit = {
							is_owned_and_controlled_by = MKN
							MKN = { has_government = communism }
							event_target:MKN_revkom_enemy = { has_war_with = MKN }
						}
						# A two-day lease also expires on states MKN no longer owns.
						add_dynamic_modifier = { modifier = MKN_revkom_enemy_disorganization scope = event_target:MKN_revkom_enemy days = 2 }
					}
				}
			}
			if = {
				limit = { has_war_with = MKN }
				set_country_flag = MKN_revkom_disorganization_active
			}
			else = { clr_country_flag = MKN_revkom_disorganization_active }
		}
	}
}
MKN_repair_communist_progression = {
	# An already accepted charter always wins over a stale betrayal flag.
	if = {
		limit = {
			OR = {
				has_country_flag = MKN_equal_autonomy
				SOV = { has_country_flag = NWW_SOV_MKN_settlement }
			}
		}
		clr_country_flag = MKN_soviet_betrayal
	}
	if = {
		limit = { NOT = { has_country_flag = MKN_communist_progression_v1 } }
		nww_mkn_rebuild_industry = yes
		nww_mkn_rebuild_services = yes
		set_country_flag = MKN_communist_progression_v1
	}
}
```

## common/on_actions/MKN_communist_on_actions.txt

Новый файл целиком.

```pdx
# MKN owns these bilateral pact definitions; SOV's hook only cleans/updates trade.
on_actions = {
	on_startup = {
		effect = {
			MKN = {
				if = {
					limit = { exists = yes }
					MKN_repair_communist_progression = yes
					MKN_sync_revkom_combat = yes
				}
			}
			MKN_sync_revkom_trade = yes
		}
	}
	on_daily_MKN = {
		effect = {
			MKN_repair_communist_progression = yes
			MKN_sync_revkom_trade = yes
			MKN_sync_revkom_combat = yes
		}
	}
	on_daily_SOV = {
		effect = { MKN_sync_revkom_trade = yes }
	}
}
```

## common/scripted_effects/nww_mkn_progression.txt — экономика

В конце существующего `nww_mkn_rebuild_industry` оставить прежние пересчёты и добавить вызов Ревкома. Конец блока:

```pdx
MKN_rebuild_militarist_industry_stats = yes
MKN_rebuild_soviet_industry_stats = yes
MKN_rebuild_communist_industry_stats = yes
set_country_flag = MKN_industry_integration_v4
```

## common/scripted_effects/nww_mkn_progression.txt — армия

В начале существующего `nww_mkn_rebuild_services`, после миграции штаба, добавить обнуление новой переменной:

```pdx
set_variable = { MKN_army_army_armor_speed_factor = 0 }
```

В конце этого же эффекта оставить прежние пересчёты и добавить новый:

```pdx
MKN_rebuild_horizons_service_stats = yes
MKN_rebuild_militarist_army_stats = yes
MKN_rebuild_soviet_army_stats = yes
MKN_rebuild_communist_army_stats = yes
```

Остальные условия, сбросы и награды существующих эффектов сохранить; это вставки, а не дополнительные одноимённые определения.

## common/dynamic_modifiers/nww_dynamic_modifiers.txt

Внутри прежнего `MKN_army_development`, рядом с танковой атакой, добавить:

```pdx
army_armor_speed_factor = MKN_army_army_armor_speed_factor
```

## localisation/russian/MKN_communist_l_russian.yml

Новый файл целиком, UTF-8 с BOM.

```yaml
l_russian:
 MKN_steppe_sovnarkhoz:0 "Степной Совнархоз"
 MKN_steppe_sovnarkhoz_desc:0 "Анархистская стихия базаров уступает место марксистскому расчёту. Каждая тонна никопольской руды, каждый вагон угля и каждая рабочая смена подчинены единому плану Совнархоза. Революция строится цифрами и чертежами, хотя печати ведомств порой движутся медленнее станков."
 MKN_artel_state_farms:0 "Артельные совхозы"
 MKN_artel_state_farms_desc:0 "Хлеб больше не станет игрушкой деревенского торговца. Совхозы снабдят рабочих и красноармейцев по твёрдым нормам. Но за воротами сельского склада уже собираются недовольные: крестьянин не считает свою землю приложением к городской ведомости."
 MKN_dnieper_five_year_plan:0 "Днепровская пятилетка"
 MKN_dnieper_five_year_plan_desc:0 "На берегах Днепра поднимутся новые цеха, и никопольский металл заговорит языком станков и орудий. Лёгкая промышленность получит остатки ресурсов. За быстрый рост тяжёлых заводов население заплатит дефицитом простых вещей."
 MKN_political_commissars:0 "Институт военных комиссаров"
 MKN_political_commissars_desc:0 "Винтовка в руках политически тёмного бойца опасна для самой революции. В каждую часть назначается комиссар Ревкома. Приказ командира требует партийной визы: двоевластие замедляет штаб, зато часть получает общий политический стержень."
 MKN_red_armored_corps:0 "Степные танковые корпуса"
 MKN_red_armored_corps_desc:0 "Тачанка открыла революции дорогу через степь; броня удержит её перед регулярной армией. Средние и тяжёлые машины сведут в корпуса, где заводской план встречается с оперативным расчётом."
 MKN_equal_shield_of_socialism:0 "Равноправный щит социализма"
 MKN_equal_shield_of_socialism_desc:0 "Москва признала хартию степи. Теперь совместные заказы и новые производственные линии станут доказательством того, что союз рабочих республик держится на равноправии. Ни один красный флаг не должен служить прикрытием чужому подчинению."
 MKN_industrial_ram_of_comintern:0 "Индустриальный таран Коминтерна"
 MKN_industrial_ram_of_comintern_desc:0 "Никопольские цеха станут арсеналом союзной революции. Серийные танки и артиллерия выйдут из ворот по общим стандартам, чтобы рабочая республика могла противопоставить империям металл и организованный труд."
 MKN_red_brotherhood_in_arms:0 "Боевое содружество революции"
 MKN_red_brotherhood_in_arms_desc:0 "Союз проверяют в одном окопе. Когда наши части и войска дружественной республики ведут общую войну, общий замысел превращает отдельные удары в наступление. Учиться будем вместе — на земле и в воздухе."
 MKN_true_socialism_against_bureaucrats:0 "Истинный социализм против бюрократов"
 MKN_true_socialism_against_bureaucrats_desc:0 "Москва предала хартию, объявив волю степи ошибкой канцелярии. Мы обратимся к солдатам, которых послали стрелять в братьев: защищайте революцию, а не кресла новых красных бонапартов. На нашей земле этот призыв услышат особенно ясно."
 MKN_liberation_of_soviet_ukraine:0 "Освобождение Советской Украины"
 MKN_liberation_of_soviet_ukraine_desc:0 "Одесса, Николаев, Киев, Сумы и Полтава принадлежат людям труда, а не ведомственным границам. Ревком признает эти земли частью общей республики и призовёт их жителей к борьбе. Хартия национальных прав не заменяет освобождения городов на деле."
 MKN_strike_at_the_kremlin:0 "Сокрушить кремлёвский бонапартизм"
 MKN_strike_at_the_kremlin_desc:0 "Нельзя бесконечно отражать удары и ждать новой московской директивы. Ускорим движение корпусов и подготовим удар по аппарату, который превратил братский союз в угрозу. Наш противник — кремлёвское командование, поправшее собственное слово."
 MKN_red_beacon_of_the_east:0 "Червоный маяк Востока"
 MKN_red_beacon_of_the_east_desc:0 "Из смуты, крестьянской земли и заводского огня выросла социалистическая степь. Её инженеры осваивают новые машины, её рабочие удерживают ритм пятилеток, её советы требуют права самим решать свою судьбу. Маяк горит для тех, кто ещё ищет дорогу."
 MKN_sovnarkhoz_idea:0 "Степной Совнархоз"
 MKN_sovnarkhoz_idea_desc:0 "План ускоряет строительство гражданских и военных заводов, но межведомственные согласования тормозят освоение производства."
 MKN_state_farms_idea:0 "Артельные совхозы"
 MKN_state_farms_idea_desc:0 "Плановые поставки уменьшают расход снабжения. Твёрдые цены и хлебозаготовки вызывают тяжёлое недовольство крестьян."
 MKN_commissars_idea:0 "Двоевластие командования"
 MKN_commissars_idea_desc:0 "Политрук укрепляет строй и волю части, но два утверждения каждого приказа задерживают планирование."
 MKN_comintern_ram_idea:0 "Индустриальный таран"
 MKN_comintern_ram_idea_desc:0 "Общие стандарты удешевляют танки и артиллерию, а координация заводов повышает выпуск военной продукции."
 MKN_red_beacon_idea:0 "Червоный маяк Востока"
 MKN_red_beacon_idea_desc:0 "Республика обрела устойчивость и уверенность. Исследовательские силы сосредоточены на промышленности и электронике, обеспечивающих независимость степи."
 MKN_equal_shield_trade_idea:0 "Заказы равноправного союза"
 MKN_equal_shield_trade_idea_desc:0 "Признанная хартия открывает общую торговую работу. Бонус сохраняется, пока коммунистические MKN и СССР остаются мирными союзниками."
 MKN_equal_shield_partner_idea:0 "Торговля с равноправной степью"
 MKN_equal_shield_partner_idea_desc:0 "Союзный Ревком обеспечивает встречные заказы и надёжные торговые связи. Разрыв согласованного союза прекращает эти преимущества."
 MKN_red_brotherhood_idea:0 "Боевое содружество"
 MKN_red_brotherhood_idea_desc:0 "Совместная война с участником нашей фракции усиливает атаку армии. В мирное время или без общего фронта этот бонус не действует."
 MKN_kremlin_offensive_idea:0 "Против кремлёвского командования"
 MKN_kremlin_offensive_idea_desc:0 "Наши войска подготовлены к удару по советской армии. Бонус к атаке направлен только против СССР."
 MKN_revkom_equal_path_tt:0 "Завершён §YРоковой пленум§!, СССР признал §Yравноправную автономию§! и не предал хартию."
 MKN_revkom_betrayal_path_tt:0 "Завершён §YРоковой пленум§! и установлен факт §Yсоветского предательства§!; принятой хартии автономии нет."
 MKN_revkom_equal_trade_tt:0 "Пока коммунистические MKN и СССР остаются союзниками и не воюют друг с другом: обеим сторонам §G+60%§! к фактору торгового влияния."
 MKN_revkom_brotherhood_tt:0 "Атака армии §G+20%§!, пока ведём общую войну хотя бы с одним участником своей фракции."
 MKN_revkom_desertion_tt:0 "Организация §Yвсех вражеских войск§! на принадлежащей и подконтрольной нам территории §G−30%§!. Наши, союзные и нейтральные части штрафа не получают."
 MKN_revkom_kremlin_attack_tt:0 "Атака против §YСССР§! §G+30%§!. Бонус не распространяется на другие страны и прекращается при восстановлении защищённого союза."
 MKN_revkom_enemy_disorganization:0 "Дезорганизация захватчиков"
 MKN_revkom_enemy_disorganization_desc:0 "Агитация и местное сопротивление подрывают организацию всех вражеских частей на нашей земле."
 MKN_red_brotherhood_land:0 "Общая сухопутная школа"
 MKN_red_brotherhood_air:0 "Общая воздушная школа"
 MKN_army_army_armor_speed_factor_tt:0 "Скорость бронетанковых частей: $RIGHT|+=%1$"
```

## localisation/english/MKN_communist_l_english.yml

Новый файл целиком, UTF-8 с BOM.

```yaml
l_english:
 MKN_steppe_sovnarkhoz:0 "Steppe Economic Council"
 MKN_steppe_sovnarkhoz_desc:0 "The markets yield to Marxist calculation. Every tonne of Nikopol ore, every wagon of coal and every shift answers to one economic plan. The revolution rises through figures and blueprints, though departmental stamps sometimes move more slowly than machines."
 MKN_artel_state_farms:0 "Cooperative State Farms"
 MKN_artel_state_farms_desc:0 "Grain will no longer be a village trader's plaything. State farms will supply workers and soldiers by fixed quotas. Yet anger gathers outside their storehouses: peasants do not consider their fields an appendix to a city ledger."
 MKN_dnieper_five_year_plan:0 "Dnieper Five-Year Plan"
 MKN_dnieper_five_year_plan_desc:0 "New workshops will rise along the Dnieper, turning Nikopol metal into machines and guns. Light industry will receive what remains. The people will pay for this industrial advance through shortages of everyday goods."
 MKN_political_commissars:0 "Institution of Military Commissars"
 MKN_political_commissars_desc:0 "A rifle without political purpose can threaten the revolution itself. A Revkom commissar will serve in every formation. Command orders require a party countersignature: divided authority slows the staff but gives the ranks a common political resolve."
 MKN_red_armored_corps:0 "Steppe Armoured Corps"
 MKN_red_armored_corps_desc:0 "The tachanka opened the steppe to revolution; armour will hold that road against a regular army. Medium and heavy machines will form corps where industrial planning meets operational purpose."
 MKN_equal_shield_of_socialism:0 "Equal Shield of Socialism"
 MKN_equal_shield_of_socialism_desc:0 "Moscow has recognised the steppe charter. Joint orders and new production lines will prove that a union of workers' republics can rest on equality. No red banner should conceal the subordination of one republic to another."
 MKN_industrial_ram_of_comintern:0 "Industrial Ram of the Comintern"
 MKN_industrial_ram_of_comintern_desc:0 "Nikopol's workshops will become an arsenal for the allied revolution. Standardised tanks and artillery will leave their gates so that the workers' republic can answer the empires with steel and organised labour."
 MKN_red_brotherhood_in_arms:0 "Revolutionary Brotherhood in Arms"
 MKN_red_brotherhood_in_arms_desc:0 "A union is tested in a shared trench. When our troops fight the same war as an allied republic, common purpose turns separate blows into an offensive. We will learn together on land and in the air."
 MKN_true_socialism_against_bureaucrats:0 "True Socialism against the Bureaucrats"
 MKN_true_socialism_against_bureaucrats_desc:0 "Moscow has betrayed the charter and dismissed the steppe's freedom as a clerical error. We will appeal to soldiers ordered to fire upon their brothers: defend the revolution, not the offices of new red Bonapartes. On our soil, that appeal will carry."
 MKN_liberation_of_soviet_ukraine:0 "Liberation of Soviet Ukraine"
 MKN_liberation_of_soviet_ukraine_desc:0 "Odesa, Mykolaiv, Kyiv, Sumy and Poltava belong to working people, not administrative borders. The Revkom will recognise them as part of our republic and call their inhabitants to struggle. A declaration of national rights cannot take the place of actual liberation."
 MKN_strike_at_the_kremlin:0 "Break Kremlin Bonapartism"
 MKN_strike_at_the_kremlin_desc:0 "We cannot repel one blow after another while awaiting Moscow's next directive. Our corps will move faster and prepare to strike the apparatus that turned a fraternal union into a threat. Our enemy is the Kremlin command that broke its own word."
 MKN_red_beacon_of_the_east:0 "Red Beacon of the East"
 MKN_red_beacon_of_the_east_desc:0 "From upheaval, peasant soil and factory fire, a socialist steppe has risen. Its engineers master new machines, its workers sustain the plans, and its councils demand the right to determine their own future. Its beacon shines for those still seeking a road."
 MKN_sovnarkhoz_idea:0 "Steppe Economic Council"
 MKN_sovnarkhoz_idea_desc:0 "The plan accelerates civilian and military construction, while departmental approvals hinder gains in production efficiency."
 MKN_state_farms_idea:0 "Cooperative State Farms"
 MKN_state_farms_idea_desc:0 "Planned deliveries reduce supply consumption. Fixed prices and grain requisitions provoke severe peasant discontent."
 MKN_commissars_idea:0 "Dual Command"
 MKN_commissars_idea_desc:0 "Commissars strengthen organisation and resolve, but requiring two approvals for an order delays planning."
 MKN_comintern_ram_idea:0 "Industrial Ram"
 MKN_comintern_ram_idea_desc:0 "Common standards make tanks and artillery cheaper, while coordinated factories increase military output."
 MKN_red_beacon_idea:0 "Red Beacon of the East"
 MKN_red_beacon_idea_desc:0 "The republic has found stability and confidence. Research concentrates on industry and electronics, the foundations of the steppe's independence."
 MKN_equal_shield_trade_idea:0 "Orders of an Equal Union"
 MKN_equal_shield_trade_idea_desc:0 "The recognised charter opens the way to common trade. The bonus lasts while communist MKN and the Soviet Union remain peaceful allies."
 MKN_equal_shield_partner_idea:0 "Trade with the Equal Steppe"
 MKN_equal_shield_partner_idea_desc:0 "The allied Revkom supplies reciprocal orders and reliable trade links. These benefits end if the agreed alliance breaks down."
 MKN_red_brotherhood_idea:0 "Brotherhood in Arms"
 MKN_red_brotherhood_idea_desc:0 "Fighting a shared war with a faction member strengthens our army's attack. The bonus ends in peacetime or without a common war."
 MKN_kremlin_offensive_idea:0 "Against the Kremlin Command"
 MKN_kremlin_offensive_idea_desc:0 "Our troops are prepared to strike the Soviet army. The attack bonus applies only against the Soviet Union."
 MKN_revkom_equal_path_tt:0 "The §YFatal Plenum§! is complete; the Soviet Union has recognised §Yequal autonomy§! and has not betrayed the charter."
 MKN_revkom_betrayal_path_tt:0 "The §YFatal Plenum§! is complete and §YSoviet betrayal§! has occurred; no accepted autonomy charter protects the settlement."
 MKN_revkom_equal_trade_tt:0 "While communist MKN and the Soviet Union remain allies at peace with one another: both receive §G+60%§! trade deal opinion factor."
 MKN_revkom_brotherhood_tt:0 "Army attack §G+20%§! while fighting a shared war with at least one member of our faction."
 MKN_revkom_desertion_tt:0 "Organisation of §Yall enemy troops§! in our owned and controlled territory: §G−30%§!. Our troops, allies and neutral countries are unaffected."
 MKN_revkom_kremlin_attack_tt:0 "Attack against the §YSoviet Union§!: §G+30%§!. This bonus does not apply to other countries and ends if a protected alliance is restored."
 MKN_revkom_enemy_disorganization:0 "Disorganisation of the Invaders"
 MKN_revkom_enemy_disorganization_desc:0 "Agitation and local resistance undermine the organisation of all enemy troops on our soil."
 MKN_red_brotherhood_land:0 "Joint Land Warfare School"
 MKN_red_brotherhood_air:0 "Joint Air Warfare School"
 MKN_army_army_armor_speed_factor_tt:0 "Armour speed: $RIGHT|+=%1$"
```

## interface/MKN_communist_focus_icons.gfx

Новый файл целиком. Текстуры, источники и точные промпты находятся в [манифесте](art/mkn_communist_expansion/assets.json).

```pdx
# Sources and prompts: docs/art/mkn_communist_expansion
spriteTypes = {
	spriteType = {
		name = GFX_focus_MKN_steppe_sovnarkhoz
		texturefile = "gfx/interface/goals/MKN_steppe_sovnarkhoz.dds"
	}
	spriteType = {
		effectFile = "gfx/FX/buttonstate.lua"
		animation = {
			animationtexturefile = "gfx/interface/goals/shine_overlay.dds"
			animationrotation = -90.0
			animationlooping = no
			animationtime = 0.75
			animationdelay = 0
			animationblendmode = add
			animationtype = scrolling
			animationrotationoffset = {
				x = 0.0
				y = 0.0
			}
			animationtexturescale = {
				x = 1.0
				y = 1.0
			}
			animationmaskfile = "gfx/interface/goals/MKN_steppe_sovnarkhoz.dds"
		}
		animation = {
			animationtexturefile = "gfx/interface/goals/shine_overlay.dds"
			animationrotation = 90.0
			animationlooping = no
			animationtime = 0.75
			animationdelay = 0
			animationblendmode = add
			animationtype = scrolling
			animationrotationoffset = {
				x = 0.0
				y = 0.0
			}
			animationtexturescale = {
				x = 1.0
				y = 1.0
			}
			animationmaskfile = "gfx/interface/goals/MKN_steppe_sovnarkhoz.dds"
		}
		legacy_lazy_load = no
		name = GFX_focus_MKN_steppe_sovnarkhoz_shine
		texturefile = "gfx/interface/goals/MKN_steppe_sovnarkhoz.dds"
	}
	spriteType = {
		name = GFX_focus_MKN_artel_state_farms
		texturefile = "gfx/interface/goals/MKN_artel_state_farms.dds"
	}
	spriteType = {
		effectFile = "gfx/FX/buttonstate.lua"
		animation = {
			animationtexturefile = "gfx/interface/goals/shine_overlay.dds"
			animationrotation = -90.0
			animationlooping = no
			animationtime = 0.75
			animationdelay = 0
			animationblendmode = add
			animationtype = scrolling
			animationrotationoffset = {
				x = 0.0
				y = 0.0
			}
			animationtexturescale = {
				x = 1.0
				y = 1.0
			}
			animationmaskfile = "gfx/interface/goals/MKN_artel_state_farms.dds"
		}
		animation = {
			animationtexturefile = "gfx/interface/goals/shine_overlay.dds"
			animationrotation = 90.0
			animationlooping = no
			animationtime = 0.75
			animationdelay = 0
			animationblendmode = add
			animationtype = scrolling
			animationrotationoffset = {
				x = 0.0
				y = 0.0
			}
			animationtexturescale = {
				x = 1.0
				y = 1.0
			}
			animationmaskfile = "gfx/interface/goals/MKN_artel_state_farms.dds"
		}
		legacy_lazy_load = no
		name = GFX_focus_MKN_artel_state_farms_shine
		texturefile = "gfx/interface/goals/MKN_artel_state_farms.dds"
	}
	spriteType = {
		name = GFX_focus_MKN_dnieper_five_year_plan
		texturefile = "gfx/interface/goals/MKN_dnieper_five_year_plan.dds"
	}
	spriteType = {
		effectFile = "gfx/FX/buttonstate.lua"
		animation = {
			animationtexturefile = "gfx/interface/goals/shine_overlay.dds"
			animationrotation = -90.0
			animationlooping = no
			animationtime = 0.75
			animationdelay = 0
			animationblendmode = add
			animationtype = scrolling
			animationrotationoffset = {
				x = 0.0
				y = 0.0
			}
			animationtexturescale = {
				x = 1.0
				y = 1.0
			}
			animationmaskfile = "gfx/interface/goals/MKN_dnieper_five_year_plan.dds"
		}
		animation = {
			animationtexturefile = "gfx/interface/goals/shine_overlay.dds"
			animationrotation = 90.0
			animationlooping = no
			animationtime = 0.75
			animationdelay = 0
			animationblendmode = add
			animationtype = scrolling
			animationrotationoffset = {
				x = 0.0
				y = 0.0
			}
			animationtexturescale = {
				x = 1.0
				y = 1.0
			}
			animationmaskfile = "gfx/interface/goals/MKN_dnieper_five_year_plan.dds"
		}
		legacy_lazy_load = no
		name = GFX_focus_MKN_dnieper_five_year_plan_shine
		texturefile = "gfx/interface/goals/MKN_dnieper_five_year_plan.dds"
	}
	spriteType = {
		name = GFX_focus_MKN_political_commissars
		texturefile = "gfx/interface/goals/MKN_political_commissars.dds"
	}
	spriteType = {
		effectFile = "gfx/FX/buttonstate.lua"
		animation = {
			animationtexturefile = "gfx/interface/goals/shine_overlay.dds"
			animationrotation = -90.0
			animationlooping = no
			animationtime = 0.75
			animationdelay = 0
			animationblendmode = add
			animationtype = scrolling
			animationrotationoffset = {
				x = 0.0
				y = 0.0
			}
			animationtexturescale = {
				x = 1.0
				y = 1.0
			}
			animationmaskfile = "gfx/interface/goals/MKN_political_commissars.dds"
		}
		animation = {
			animationtexturefile = "gfx/interface/goals/shine_overlay.dds"
			animationrotation = 90.0
			animationlooping = no
			animationtime = 0.75
			animationdelay = 0
			animationblendmode = add
			animationtype = scrolling
			animationrotationoffset = {
				x = 0.0
				y = 0.0
			}
			animationtexturescale = {
				x = 1.0
				y = 1.0
			}
			animationmaskfile = "gfx/interface/goals/MKN_political_commissars.dds"
		}
		legacy_lazy_load = no
		name = GFX_focus_MKN_political_commissars_shine
		texturefile = "gfx/interface/goals/MKN_political_commissars.dds"
	}
	spriteType = {
		name = GFX_focus_MKN_red_armored_corps
		texturefile = "gfx/interface/goals/MKN_red_armored_corps.dds"
	}
	spriteType = {
		effectFile = "gfx/FX/buttonstate.lua"
		animation = {
			animationtexturefile = "gfx/interface/goals/shine_overlay.dds"
			animationrotation = -90.0
			animationlooping = no
			animationtime = 0.75
			animationdelay = 0
			animationblendmode = add
			animationtype = scrolling
			animationrotationoffset = {
				x = 0.0
				y = 0.0
			}
			animationtexturescale = {
				x = 1.0
				y = 1.0
			}
			animationmaskfile = "gfx/interface/goals/MKN_red_armored_corps.dds"
		}
		animation = {
			animationtexturefile = "gfx/interface/goals/shine_overlay.dds"
			animationrotation = 90.0
			animationlooping = no
			animationtime = 0.75
			animationdelay = 0
			animationblendmode = add
			animationtype = scrolling
			animationrotationoffset = {
				x = 0.0
				y = 0.0
			}
			animationtexturescale = {
				x = 1.0
				y = 1.0
			}
			animationmaskfile = "gfx/interface/goals/MKN_red_armored_corps.dds"
		}
		legacy_lazy_load = no
		name = GFX_focus_MKN_red_armored_corps_shine
		texturefile = "gfx/interface/goals/MKN_red_armored_corps.dds"
	}
	spriteType = {
		name = GFX_focus_MKN_equal_shield_of_socialism
		texturefile = "gfx/interface/goals/MKN_equal_shield_of_socialism.dds"
	}
	spriteType = {
		effectFile = "gfx/FX/buttonstate.lua"
		animation = {
			animationtexturefile = "gfx/interface/goals/shine_overlay.dds"
			animationrotation = -90.0
			animationlooping = no
			animationtime = 0.75
			animationdelay = 0
			animationblendmode = add
			animationtype = scrolling
			animationrotationoffset = {
				x = 0.0
				y = 0.0
			}
			animationtexturescale = {
				x = 1.0
				y = 1.0
			}
			animationmaskfile = "gfx/interface/goals/MKN_equal_shield_of_socialism.dds"
		}
		animation = {
			animationtexturefile = "gfx/interface/goals/shine_overlay.dds"
			animationrotation = 90.0
			animationlooping = no
			animationtime = 0.75
			animationdelay = 0
			animationblendmode = add
			animationtype = scrolling
			animationrotationoffset = {
				x = 0.0
				y = 0.0
			}
			animationtexturescale = {
				x = 1.0
				y = 1.0
			}
			animationmaskfile = "gfx/interface/goals/MKN_equal_shield_of_socialism.dds"
		}
		legacy_lazy_load = no
		name = GFX_focus_MKN_equal_shield_of_socialism_shine
		texturefile = "gfx/interface/goals/MKN_equal_shield_of_socialism.dds"
	}
	spriteType = {
		name = GFX_focus_MKN_industrial_ram_of_comintern
		texturefile = "gfx/interface/goals/MKN_industrial_ram_of_comintern.dds"
	}
	spriteType = {
		effectFile = "gfx/FX/buttonstate.lua"
		animation = {
			animationtexturefile = "gfx/interface/goals/shine_overlay.dds"
			animationrotation = -90.0
			animationlooping = no
			animationtime = 0.75
			animationdelay = 0
			animationblendmode = add
			animationtype = scrolling
			animationrotationoffset = {
				x = 0.0
				y = 0.0
			}
			animationtexturescale = {
				x = 1.0
				y = 1.0
			}
			animationmaskfile = "gfx/interface/goals/MKN_industrial_ram_of_comintern.dds"
		}
		animation = {
			animationtexturefile = "gfx/interface/goals/shine_overlay.dds"
			animationrotation = 90.0
			animationlooping = no
			animationtime = 0.75
			animationdelay = 0
			animationblendmode = add
			animationtype = scrolling
			animationrotationoffset = {
				x = 0.0
				y = 0.0
			}
			animationtexturescale = {
				x = 1.0
				y = 1.0
			}
			animationmaskfile = "gfx/interface/goals/MKN_industrial_ram_of_comintern.dds"
		}
		legacy_lazy_load = no
		name = GFX_focus_MKN_industrial_ram_of_comintern_shine
		texturefile = "gfx/interface/goals/MKN_industrial_ram_of_comintern.dds"
	}
	spriteType = {
		name = GFX_focus_MKN_red_brotherhood_in_arms
		texturefile = "gfx/interface/goals/MKN_red_brotherhood_in_arms.dds"
	}
	spriteType = {
		effectFile = "gfx/FX/buttonstate.lua"
		animation = {
			animationtexturefile = "gfx/interface/goals/shine_overlay.dds"
			animationrotation = -90.0
			animationlooping = no
			animationtime = 0.75
			animationdelay = 0
			animationblendmode = add
			animationtype = scrolling
			animationrotationoffset = {
				x = 0.0
				y = 0.0
			}
			animationtexturescale = {
				x = 1.0
				y = 1.0
			}
			animationmaskfile = "gfx/interface/goals/MKN_red_brotherhood_in_arms.dds"
		}
		animation = {
			animationtexturefile = "gfx/interface/goals/shine_overlay.dds"
			animationrotation = 90.0
			animationlooping = no
			animationtime = 0.75
			animationdelay = 0
			animationblendmode = add
			animationtype = scrolling
			animationrotationoffset = {
				x = 0.0
				y = 0.0
			}
			animationtexturescale = {
				x = 1.0
				y = 1.0
			}
			animationmaskfile = "gfx/interface/goals/MKN_red_brotherhood_in_arms.dds"
		}
		legacy_lazy_load = no
		name = GFX_focus_MKN_red_brotherhood_in_arms_shine
		texturefile = "gfx/interface/goals/MKN_red_brotherhood_in_arms.dds"
	}
	spriteType = {
		name = GFX_focus_MKN_true_socialism_against_bureaucrats
		texturefile = "gfx/interface/goals/MKN_true_socialism_against_bureaucrats.dds"
	}
	spriteType = {
		effectFile = "gfx/FX/buttonstate.lua"
		animation = {
			animationtexturefile = "gfx/interface/goals/shine_overlay.dds"
			animationrotation = -90.0
			animationlooping = no
			animationtime = 0.75
			animationdelay = 0
			animationblendmode = add
			animationtype = scrolling
			animationrotationoffset = {
				x = 0.0
				y = 0.0
			}
			animationtexturescale = {
				x = 1.0
				y = 1.0
			}
			animationmaskfile = "gfx/interface/goals/MKN_true_socialism_against_bureaucrats.dds"
		}
		animation = {
			animationtexturefile = "gfx/interface/goals/shine_overlay.dds"
			animationrotation = 90.0
			animationlooping = no
			animationtime = 0.75
			animationdelay = 0
			animationblendmode = add
			animationtype = scrolling
			animationrotationoffset = {
				x = 0.0
				y = 0.0
			}
			animationtexturescale = {
				x = 1.0
				y = 1.0
			}
			animationmaskfile = "gfx/interface/goals/MKN_true_socialism_against_bureaucrats.dds"
		}
		legacy_lazy_load = no
		name = GFX_focus_MKN_true_socialism_against_bureaucrats_shine
		texturefile = "gfx/interface/goals/MKN_true_socialism_against_bureaucrats.dds"
	}
	spriteType = {
		name = GFX_focus_MKN_liberation_of_soviet_ukraine
		texturefile = "gfx/interface/goals/MKN_liberation_of_soviet_ukraine.dds"
	}
	spriteType = {
		effectFile = "gfx/FX/buttonstate.lua"
		animation = {
			animationtexturefile = "gfx/interface/goals/shine_overlay.dds"
			animationrotation = -90.0
			animationlooping = no
			animationtime = 0.75
			animationdelay = 0
			animationblendmode = add
			animationtype = scrolling
			animationrotationoffset = {
				x = 0.0
				y = 0.0
			}
			animationtexturescale = {
				x = 1.0
				y = 1.0
			}
			animationmaskfile = "gfx/interface/goals/MKN_liberation_of_soviet_ukraine.dds"
		}
		animation = {
			animationtexturefile = "gfx/interface/goals/shine_overlay.dds"
			animationrotation = 90.0
			animationlooping = no
			animationtime = 0.75
			animationdelay = 0
			animationblendmode = add
			animationtype = scrolling
			animationrotationoffset = {
				x = 0.0
				y = 0.0
			}
			animationtexturescale = {
				x = 1.0
				y = 1.0
			}
			animationmaskfile = "gfx/interface/goals/MKN_liberation_of_soviet_ukraine.dds"
		}
		legacy_lazy_load = no
		name = GFX_focus_MKN_liberation_of_soviet_ukraine_shine
		texturefile = "gfx/interface/goals/MKN_liberation_of_soviet_ukraine.dds"
	}
	spriteType = {
		name = GFX_focus_MKN_strike_at_the_kremlin
		texturefile = "gfx/interface/goals/MKN_strike_at_the_kremlin.dds"
	}
	spriteType = {
		effectFile = "gfx/FX/buttonstate.lua"
		animation = {
			animationtexturefile = "gfx/interface/goals/shine_overlay.dds"
			animationrotation = -90.0
			animationlooping = no
			animationtime = 0.75
			animationdelay = 0
			animationblendmode = add
			animationtype = scrolling
			animationrotationoffset = {
				x = 0.0
				y = 0.0
			}
			animationtexturescale = {
				x = 1.0
				y = 1.0
			}
			animationmaskfile = "gfx/interface/goals/MKN_strike_at_the_kremlin.dds"
		}
		animation = {
			animationtexturefile = "gfx/interface/goals/shine_overlay.dds"
			animationrotation = 90.0
			animationlooping = no
			animationtime = 0.75
			animationdelay = 0
			animationblendmode = add
			animationtype = scrolling
			animationrotationoffset = {
				x = 0.0
				y = 0.0
			}
			animationtexturescale = {
				x = 1.0
				y = 1.0
			}
			animationmaskfile = "gfx/interface/goals/MKN_strike_at_the_kremlin.dds"
		}
		legacy_lazy_load = no
		name = GFX_focus_MKN_strike_at_the_kremlin_shine
		texturefile = "gfx/interface/goals/MKN_strike_at_the_kremlin.dds"
	}
	spriteType = {
		name = GFX_focus_MKN_red_beacon_of_the_east
		texturefile = "gfx/interface/goals/MKN_red_beacon_of_the_east.dds"
	}
	spriteType = {
		effectFile = "gfx/FX/buttonstate.lua"
		animation = {
			animationtexturefile = "gfx/interface/goals/shine_overlay.dds"
			animationrotation = -90.0
			animationlooping = no
			animationtime = 0.75
			animationdelay = 0
			animationblendmode = add
			animationtype = scrolling
			animationrotationoffset = {
				x = 0.0
				y = 0.0
			}
			animationtexturescale = {
				x = 1.0
				y = 1.0
			}
			animationmaskfile = "gfx/interface/goals/MKN_red_beacon_of_the_east.dds"
		}
		animation = {
			animationtexturefile = "gfx/interface/goals/shine_overlay.dds"
			animationrotation = 90.0
			animationlooping = no
			animationtime = 0.75
			animationdelay = 0
			animationblendmode = add
			animationtype = scrolling
			animationrotationoffset = {
				x = 0.0
				y = 0.0
			}
			animationtexturescale = {
				x = 1.0
				y = 1.0
			}
			animationmaskfile = "gfx/interface/goals/MKN_red_beacon_of_the_east.dds"
		}
		legacy_lazy_load = no
		name = GFX_focus_MKN_red_beacon_of_the_east_shine
		texturefile = "gfx/interface/goals/MKN_red_beacon_of_the_east.dds"
	}
}
```

[Предпросмотр 12 иконок](mkn_communist_expansion_preview_2x.png).

## Проверка

```sh
python tools/validate_country_content.py --game '/home/dima00138/.local/share/Steam/steamapps/common/Hearts of Iron IV'
git diff --check
```

Новая кампания и runtime-проверка боёв/подсказок не проводились.
