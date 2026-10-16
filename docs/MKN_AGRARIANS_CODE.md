# MKN: готовые блоки файлов аграрной ветки

Код уже внесён в рабочий проект. Повторно вставлять определения не нужно. При конфликте чисел использованы значения из описаний фокусов. Механики, исходные образцы DLC и ограничения: [MKN_agrarians.md](MKN_agrarians.md).

## common/national_focus/MKN.txt

Внутрь существующего `focus_tree`:

```pdx
focus = {
    id = MKN_great_rural_exodus
    icon = GFX_focus_MKN_great_rural_exodus
    x = 88
    y = 5
    cost = 5
    prerequisite = {
        focus = MKN_grain_ultimatum
    }
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    available = {
        has_government = neutrality
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    completion_reward = {
        add_ideas = MKN_rural_exodus_idea
    }
    ai_will_do = {
        factor = 2
    }
}
focus = {
    id = MKN_black_partition_of_soil
    icon = GFX_focus_MKN_black_partition_of_soil
    x = 88
    y = 6
    cost = 5
    prerequisite = {
        focus = MKN_great_rural_exodus
    }
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    available = {
        has_government = neutrality
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    completion_reward = {
        add_ideas = MKN_black_partition_idea
        every_country = {
            limit = {
                exists = yes
                OR = {
                    tag = AUS
                    tag = LTB
                    tag = GER
                }
            }
            add_opinion_modifier = {
                target = ROOT
                modifier = MKN_black_partition_hostility
            }
        }
    }
    ai_will_do = {
        factor = 2
    }
}
focus = {
    id = MKN_village_assembly_sovereignty
    icon = GFX_focus_MKN_village_assembly_sovereignty
    x = 88
    y = 7
    cost = 5
    prerequisite = {
        focus = MKN_black_partition_of_soil
    }
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    available = {
        has_government = neutrality
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    completion_reward = {
        add_ideas = MKN_village_sovereignty_idea
    }
    ai_will_do = {
        factor = 2
    }
}
focus = {
    id = MKN_abolition_of_paper_money
    icon = GFX_focus_MKN_abolition_of_paper_money
    x = 92
    y = 5
    cost = 5
    prerequisite = {
        focus = MKN_grain_ultimatum
    }
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    available = {
        has_government = neutrality
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    completion_reward = {
        add_ideas = MKN_grain_currency_idea
    }
    ai_will_do = {
        factor = 2
    }
}
focus = {
    id = MKN_village_smithies_over_plants
    icon = GFX_focus_MKN_village_smithies_over_plants
    x = 92
    y = 6
    cost = 5
    prerequisite = {
        focus = MKN_abolition_of_paper_money
    }
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    available = {
        has_government = neutrality
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    completion_reward = {
        add_ideas = MKN_village_smithies_idea
    }
    ai_will_do = {
        factor = 2
    }
}
focus = {
    id = MKN_steppe_grain_monopoly
    icon = GFX_focus_MKN_steppe_grain_monopoly
    x = 92
    y = 7
    cost = 5
    prerequisite = {
        focus = MKN_village_smithies_over_plants
    }
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    available = {
        has_government = neutrality
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    completion_reward = {
        add_ideas = MKN_steppe_grain_monopoly_idea
        custom_effect_tooltip = MKN_grain_barter_unlock_tt
    }
    ai_will_do = {
        factor = 2
    }
}
focus = {
    id = MKN_hunters_of_the_steppe
    icon = GFX_focus_MKN_hunters_of_the_steppe
    x = 88
    y = 8
    cost = 5
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    available = {
        has_government = neutrality
        has_completed_focus = MKN_every_farm_a_fortress
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    completion_reward = {
        add_ideas = MKN_hunters_idea
        custom_effect_tooltip = MKN_hunters_terrain_tt
        hidden_effect = {
            set_technology = {
                MKN_steppe_hunter_training = 1
            }
        }
    }
    ai_will_do = {
        factor = 2
    }
}
focus = {
    id = MKN_fortified_homesteads
    icon = GFX_focus_MKN_fortified_homesteads
    x = 88
    y = 9
    cost = 5
    prerequisite = {
        focus = MKN_hunters_of_the_steppe
    }
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    available = {
        has_government = neutrality
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    completion_reward = {
        add_ideas = MKN_fortified_homesteads_idea
    }
    ai_will_do = {
        factor = 2
    }
}
focus = {
    id = MKN_traps_and_ambush_lines
    icon = GFX_focus_MKN_traps_and_ambush_lines
    x = 88
    y = 10
    cost = 5
    prerequisite = {
        focus = MKN_fortified_homesteads
    }
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    available = {
        has_government = neutrality
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    completion_reward = {
        add_ideas = MKN_steppe_traps_idea
        hidden_effect = {
            MKN_sync_agrarian_defense = yes
        }
    }
    ai_will_do = {
        factor = 2
    }
}
focus = {
    id = MKN_empty_field_doctrine
    icon = GFX_focus_MKN_empty_field_doctrine
    x = 90
    y = 11
    cost = 5
    prerequisite = {
        focus = MKN_impregnable_granary
    }
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    available = {
        has_government = neutrality
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    completion_reward = {
        add_ideas = MKN_empty_field_idea
    }
    ai_will_do = {
        factor = 2
    }
}
focus = {
    id = MKN_death_to_grain_thieves
    icon = GFX_focus_MKN_death_to_grain_thieves
    x = 90
    y = 12
    cost = 5
    prerequisite = {
        focus = MKN_empty_field_doctrine
    }
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    available = {
        has_government = neutrality
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    completion_reward = {
        add_ideas = MKN_death_to_thieves_idea
    }
    ai_will_do = {
        factor = 2
    }
}
focus = {
    id = MKN_chernozem_autarky
    icon = GFX_focus_MKN_chernozem_autarky
    x = 90
    y = 13
    cost = 5
    prerequisite = {
        focus = MKN_death_to_grain_thieves
    }
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    available = {
        has_government = neutrality
        is_subject = no
        is_in_faction = no
        has_offensive_war = no
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    completion_reward = {
        add_ideas = MKN_chernozem_autarky_idea
        custom_effect_tooltip = MKN_agrarian_isolation_tt
    }
    ai_will_do = {
        factor = 2
    }
}
```

## common/ideas/MKN_agrarian_ideas.txt

Новый файл целиком.

```pdx
# Owner: MKN agrarians. The focus specification takes precedence over its summary.
ideas = {
	country = {
		MKN_rural_exodus_idea = {
			picture = generic_industrial_concern_1
			allowed = { original_tag = MKN }
			removal_cost = -1
			modifier = { monthly_population = 0.60 industrial_capacity_factory = -0.25 }
		}
		MKN_black_partition_idea = {
			picture = generic_industrial_concern_1
			allowed = { original_tag = MKN }
			removal_cost = -1
			modifier = { stability_factor = 0.20 consumer_goods_factor = -0.20 }
		}
		MKN_village_sovereignty_idea = {
			picture = generic_democratic_reformer_eastern_european_2d
			allowed = { original_tag = MKN }
			removal_cost = -1
			modifier = { stability_factor = 0.10 resistance_decay_on_our_occupied_states = 0.40 political_power_gain = -0.30 }
		}
		MKN_grain_currency_idea = {
			picture = generic_industrial_concern_1
			allowed = { original_tag = MKN }
			removal_cost = -1
			modifier = { stability_factor = 0.10 trade_opinion_factor = -0.40 custom_modifier_tooltip = MKN_grain_currency_resilience_tt }
		}
		MKN_village_smithies_idea = {
			picture = generic_industrial_concern_1
			allowed = { original_tag = MKN }
			removal_cost = -1
			equipment_bonus = {
				infantry_equipment = { build_cost_ic = -0.30 instant = yes }
				support_equipment = { build_cost_ic = -0.30 instant = yes }
			}
			research_bonus = { armor = -0.50 air_equipment = -0.50 }
			modifier = { }
		}
		MKN_steppe_grain_monopoly_idea = {
			picture = generic_industrial_concern_1
			allowed = { original_tag = MKN }
			removal_cost = -1
			modifier = { trade_opinion_factor = -0.25 }
		}
		MKN_hunters_idea = {
			picture = generic_army_war_college
			allowed = { original_tag = MKN }
			removal_cost = -1
			modifier = { recon_factor = 0.50 training_time_army_factor = 0.30 custom_modifier_tooltip = MKN_hunters_terrain_tt }
		}
		MKN_fortified_homesteads_idea = {
			picture = generic_army_war_college
			allowed = { original_tag = MKN }
			removal_cost = -1
			modifier = { dig_in_speed_factor = 0.45 max_dig_in = 10.0 }
		}
		MKN_steppe_traps_idea = {
			picture = generic_army_war_college
			allowed = { original_tag = MKN }
			removal_cost = -1
			modifier = { org_loss_when_moving = -0.20 custom_modifier_tooltip = MKN_steppe_traps_tt }
		}
		MKN_empty_field_idea = {
			picture = generic_army_war_college
			allowed = { original_tag = MKN }
			removal_cost = -1
			modifier = { enemy_attrition = 0.35 }
		}
		MKN_death_to_thieves_idea = {
			picture = generic_army_war_college
			allowed = { original_tag = MKN }
			removal_cost = -1
			modifier = { surrender_limit = 0.30 army_core_defence_factor = 0.45 }
		}
		MKN_chernozem_autarky_idea = {
			picture = generic_industrial_concern_1
			allowed = { original_tag = MKN }
			removal_cost = -1
			rule = { can_join_factions = no can_create_factions = no can_not_declare_war = yes }
			modifier = { consumer_goods_factor = -0.40 stability_factor = 0.20 conscription = 0.06 army_non_core_attack_factor = -0.35 }
		}
		# A temporary off-map factory is owned by this timed spirit, not by a delayed event.
		MKN_grain_barter_factory_idea = {
			picture = generic_industrial_concern_1
			allowed = { original_tag = MKN }
			removal_cost = -1
			modifier = { }
			on_add = {
				if = {
					limit = { NOT = { has_country_flag = MKN_grain_barter_factory_active } }
					set_country_flag = MKN_grain_barter_factory_active
					add_offsite_building = { type = industrial_complex level = 1 }
				}
			}
			on_remove = {
				if = {
					limit = { has_country_flag = MKN_grain_barter_factory_active }
					add_offsite_building = { type = industrial_complex level = -1 }
					clr_country_flag = MKN_grain_barter_factory_active
				}
			}
		}
	}
}
```

## common/dynamic_modifiers/MKN_agrarian_modifiers.txt

Новый файл целиком.

```pdx
# Native state/army modifier, restricted to the country whose territory is defended.
MKN_agrarian_trapped_roads = {
	enable = {
		is_owned_and_controlled_by = MKN
		MKN = { has_government = neutrality has_idea = MKN_steppe_traps_idea }
	}
	icon = GFX_modifiers_SOV_armored_battery
	enemy_army_speed_factor = -0.30
}
```

## common/technologies/MKN_agrarian_technologies.txt

Новый файл целиком.

```pdx
# Focus-only terrain training, following GoE urban_training_tech.
technologies = {
	MKN_steppe_hunter_training = {
		research_cost = 1
		allow = { always = no }
		infantry = { plains = { attack = 0.20 } forest = { attack = 0.20 } }
		irregular_infantry = { plains = { attack = 0.20 } forest = { attack = 0.20 } }
		militia = { plains = { attack = 0.20 } forest = { attack = 0.20 } }
		mountaineers = { plains = { attack = 0.20 } forest = { attack = 0.20 } }
		marine = { plains = { attack = 0.20 } forest = { attack = 0.20 } }
		paratrooper = { plains = { attack = 0.20 } forest = { attack = 0.20 } }
	}
}
```

## common/opinion_modifiers/MKN_agrarian_opinions.txt

Новый файл целиком.

```pdx
opinion_modifiers = {
	MKN_black_partition_hostility = { value = -30 }
}
```

## common/scripted_effects/MKN_agrarian_effects.txt

Новый файл целиком.

```pdx
MKN_sync_agrarian_defense = {
	if = {
		limit = { has_completed_focus = MKN_traps_and_ambush_lines }
		every_owned_state = {
			limit = { NOT = { has_dynamic_modifier = { modifier = MKN_agrarian_trapped_roads scope = MKN } } }
			add_dynamic_modifier = { modifier = MKN_agrarian_trapped_roads scope = MKN }
		}
	}
}
MKN_repair_agrarian_training = {
	if = {
		limit = { has_completed_focus = MKN_hunters_of_the_steppe NOT = { has_tech = MKN_steppe_hunter_training } }
		set_technology = { MKN_steppe_hunter_training = 1 }
	}
}
```

## common/on_actions/MKN_agrarian_on_actions.txt

Новый файл целиком.

```pdx
on_actions = {
	on_startup = {
		effect = {
			MKN = {
				if = {
					limit = { exists = yes }
					MKN_repair_agrarian_training = yes
					MKN_sync_agrarian_defense = yes
				}
			}
		}
	}
	on_daily_MKN = {
		effect = { MKN_repair_agrarian_training = yes MKN_sync_agrarian_defense = yes }
	}
}
```

## common/decisions/MKN_decisions.txt

Добавить внутрь существующей категории `MKN_steppe_operations_category`:

```pdx
MKN_barter_grain_surplus = {
    icon = generic_industry
    allowed = {
        original_tag = MKN
    }
    visible = {
        has_completed_focus = MKN_steppe_grain_monopoly
    }
    available = {
        has_government = neutrality
        has_capitulated = no
        any_owned_state = {
            is_owned_and_controlled_by = ROOT
            is_core_of = ROOT
        }
        NOT = {
            has_country_flag = MKN_grain_barter_project_active
        }
        NOT = {
            has_idea = MKN_grain_barter_factory_idea
        }
    }
    cost = 25
    days_remove = 60
    days_re_enable = 180
    complete_effect = {
        set_country_flag = MKN_grain_barter_project_active
        custom_effect_tooltip = MKN_grain_barter_reward_tt
    }
    cancel_trigger = {
        OR = {
            NOT = {
                has_government = neutrality
            }
            has_capitulated = yes
            NOT = {
                any_owned_state = {
                    is_owned_and_controlled_by = ROOT
                    is_core_of = ROOT
                }
            }
        }
    }
    cancel_effect = {
        if = {
            limit = {
                has_country_flag = MKN_grain_barter_project_active
            }
            add_political_power = 25
            clr_country_flag = MKN_grain_barter_project_active
        }
    }
    remove_effect = {
        if = {
            limit = {
                has_country_flag = MKN_grain_barter_project_active
            }
            if = {
                limit = {
                    has_government = neutrality
                    has_capitulated = no
                    any_owned_state = {
                        is_owned_and_controlled_by = ROOT
                        is_core_of = ROOT
                    }
                    NOT = {
                        has_idea = MKN_grain_barter_factory_idea
                    }
                }
                add_political_power = 50
                add_timed_idea = {
                    idea = MKN_grain_barter_factory_idea
                    days = 180
                }
            }
            else = {
                add_political_power = 25
            }
            clr_country_flag = MKN_grain_barter_project_active
        }
    }
    ai_will_do = {
        factor = 1
    }
}
```

## common/decisions/categories/MKN_bop_categories.txt

Заменить определение прежней категории целиком, сохранив остальные категории файла:

```pdx
MKN_steppe_operations_category = {
    icon = generic_guerilla_base
    allowed = {
        tag = MKN
    }
    visible = {
        OR = {
            has_completed_focus = MKN_steppe_grain_monopoly
            has_completed_focus = MKN_black_expansionism
            has_completed_focus = MKN_propaganda_by_deed
            has_completed_focus = MKN_railway_sabotage
            has_completed_focus = MKN_black_international
            has_completed_focus = MKN_embassy_to_kharkov
        }
    }
}
```

## localisation/russian/MKN_agrarian_l_russian.yml

Новый файл целиком, UTF-8 с BOM.

```yaml
l_russian:
 MKN_great_rural_exodus:0 "Великий исход в сёла"
 MKN_great_rural_exodus_desc:0 "Город обещал человеку свободу, а дал очередь к проходной. Пусть рабочие возвращаются к родне и строят новые дворы на чернозёме. Семьи вырастут, но заводам придётся обходиться без прежних рук."
 MKN_black_partition_of_soil:0 "Чёрный передел чернозёма"
 MKN_black_partition_of_soil_desc:0 "На землю нет права у того, кто видел её только из окна усадьбы. Межи проведёт сам сельский сход. У крестьян появится уверенность в завтрашнем урожае, у соседних помещиков — новый повод нас ненавидеть."
 MKN_village_assembly_sovereignty:0 "Сельский сход — высший закон"
 MKN_village_assembly_sovereignty_desc:0 "Ни городскому писарю, ни приезжему оратору не распоряжаться нашим двором. Сход решает спор, выбирает старосту и отвечает перед соседями. Общая власть станет медлительнее, зато чужому приказу будет труднее пустить здесь корни."
 MKN_abolition_of_paper_money:0 "Отказ от бумажных билетов"
 MKN_abolition_of_paper_money_desc:0 "Бумагу печатает город, а хлеб выращиваем мы. Счёт пойдёт на мерки зерна, честный вес и расписку сельского амбара. Пусть чужие биржи лихорадит: местный урожай от их котировок не исчезнет."
 MKN_village_smithies_over_plants:0 "Кустарные кузницы вместо гигантов"
 MKN_village_smithies_over_plants_desc:0 "Селу не нужны гигантские мартены для постройки линкоров и авианосцев. Нам нужны тысячи кузниц, которые скуют плуг, насадят топор и изготовят детали для охотничьих штуцеров. Танки и самолёты пусть строят в городах, если найдут хлеб."
 MKN_steppe_grain_monopoly:0 "Хлебный диктат степи"
 MKN_steppe_grain_monopoly_desc:0 "Пока городские министры спорят о золоте, их народу нужен хлеб. Излишки урожая уйдут за станки и политические уступки. Покупатель может сердиться на наши условия, но голодный живот спорит громче посла."
 MKN_hunters_of_the_steppe:0 "Степные загонщики и звероловы"
 MKN_hunters_of_the_steppe_desc:0 "Охотник читает траву и кору лучше штабной карты. Он подведёт сотню к лесной опушке и различит засаду на ровной степи. Только строевая муштра даётся ему неохотно: свободного человека долго учить шагать по свистку."
 MKN_fortified_homesteads:0 "Каменные овчарни и валы"
 MKN_fortified_homesteads_desc:0 "Толстая стена овчарни, земляной вал и сухой ров послужат надёжнее обещаний городской власти. Пусть каждый двор заранее приготовит укрытие, запас воды и место для стрелка."
 MKN_traps_and_ambush_lines:0 "Волчьи капканы на дорогах"
 MKN_traps_and_ambush_lines_desc:0 "Мы знаем каждую гать и каждый овраг. Свой отряд пройдёт знакомой тропой без потери порядка; чужая колонна упрётся в завал, ложный поворот и проволоку под колёсами."
 MKN_empty_field_doctrine:0 "План «Пустого поля»"
 MKN_empty_field_doctrine_desc:0 "Если чужие полки перейдут нашу межу, они не найдут ни зёрнышка. Элеваторы опустеют, колодцы будут закрыты, скот уйдёт в плавни. Враг захватит лишь выжженную золу и встретит голод под ледяным степным ветром."
 MKN_death_to_grain_thieves:0 "Смертный приговор захватчикам"
 MKN_death_to_grain_thieves_desc:0 "Кто пришёл отнять последний мешок у наших детей, не найдёт здесь покорности. Амбары станут крепостями, старосты соберут сотни, и ни один двор не согласится сдаться ради чужого удобства."
 MKN_chernozem_autarky:0 "Чернозёмная автаркия"
 MKN_chernozem_autarky_desc:0 "Пусть старый мир сгорает в пожарах империй и войн за колонии. Степь сыта, вооружена и свободна. Мы никому не кланяемся, не просим чужой земли и никого не впустим за нашу ограду."
 MKN_rural_exodus_idea:0 "Возвращение к земле"
 MKN_rural_exodus_idea_desc:0 "Новые дворы и большие семьи ускоряют рост населения. Рабочие покидают городские заводы, снижая выпуск военной промышленности."
 MKN_black_partition_idea:0 "Чёрный передел"
 MKN_black_partition_idea_desc:0 "Семья, получившая землю, сама обеспечивает значительную часть своих нужд. Устойчивость растёт, а зависимость от городской потребительской промышленности уменьшается."
 MKN_village_sovereignty_idea:0 "Суверенитет сельского схода"
 MKN_village_sovereignty_idea_desc:0 "Незнакомая власть встречает упорное сопротивление на нашей земле. Но собственный общий приказ тоже требует согласия множества деревень и отнимает политические силы."
 MKN_grain_currency_idea:0 "Хлебная валюта"
 MKN_grain_currency_idea_desc:0 "Сельский счёт держится на урожае, а не на чужом бумажном курсе. Хлебные расчёты устойчивы к биржевой панике, хотя иностранные купцы не любят наши порядки."
 MKN_village_smithies_idea:0 "Сельские кузницы"
 MKN_village_smithies_idea_desc:0 "Винтовочные детали и простое снабженческое снаряжение обходятся дешевле. Сложная бронетехника и авиация остаются без инженерной школы и исследуются значительно медленнее."
 MKN_steppe_grain_monopoly_idea:0 "Хлебный диктат"
 MKN_steppe_grain_monopoly_idea_desc:0 "Соседи покупают наш урожай, но не прощают условий, поставленных сельскими амбарами."
 MKN_hunters_idea:0 "Степные охотники"
 MKN_hunters_idea_desc:0 "Опытные разведчики и меткие стрелки особенно опасны на равнинах и в лесах. Их приходится дольше приучать к армейскому порядку."
 MKN_fortified_homesteads_idea:0 "Укреплённые хутора"
 MKN_fortified_homesteads_idea_desc:0 "Каменные постройки и заранее подготовленные валы позволяют быстро занять глубокую оборону."
 MKN_steppe_traps_idea:0 "Дороги с подвохом"
 MKN_steppe_traps_idea_desc:0 "Знакомые тропы сохраняют строй наших отрядов. Вражеские войска медленнее продвигаются по принадлежащей нам и контролируемой территории."
 MKN_empty_field_idea:0 "Пустое поле"
 MKN_empty_field_idea_desc:0 "Спрятанные запасы и уходящие вместе с жителями обозы оставляют противника без местного пропитания."
 MKN_death_to_thieves_idea:0 "Не отдадим своего"
 MKN_death_to_thieves_idea_desc:0 "За родную землю сражаются до последнего рубежа. Повод для капитуляции здесь должен быть весомее занятой городской площади."
 MKN_chernozem_autarky_idea:0 "Чернозёмная автаркия"
 MKN_chernozem_autarky_idea_desc:0 "Хлеб и ополчение обеспечивают независимость степи. Объявлять новые войны, создавать фракции и вступать в них запрещено; нападение противника не отменяет права защищаться."
 MKN_grain_barter_factory_idea:0 "Станки за урожай"
 MKN_grain_barter_factory_idea_desc:0 "За излишки хлеба получена временная производственная линия: одна внекартовая гражданская фабрика на 180 дней. По окончании договора она исчезнет."
 MKN_barter_grain_surplus:0 "Обменять излишки урожая"
 MKN_barter_grain_surplus_desc:0 "За 25 PP организовать 60-дневный обмен хлебных излишков. По завершении получим 50 PP и одну внекартовую гражданскую фабрику на 180 дней. Повторное решение имеет кулдаун 180 дней; действующий договор нельзя складывать с новым. Отмена возвращает стоимость."
 MKN_grain_barter_unlock_tt:0 "Открывает §YОбменять излишки урожая§!: §Y25 PP§!, подготовка §Y60 дней§!, награда §G50 PP§! и §G1§! внекартовая гражданская фабрика на §Y180 дней§!."
 MKN_grain_currency_resilience_tt:0 "Хлебный обмен не зависит от доступа к международному рынку, импортных маршрутов и эмбарго."
 MKN_hunters_terrain_tt:0 "Пехота, ополчение, нерегулярная и специальная пехота: атака на §Yравнинах§! и в §Yлесах§! §G+20%§!."
 MKN_steppe_traps_tt:0 "Скорость вражеской армии в принадлежащих нам и контролируемых областях §G−30%§!."
 MKN_agrarian_isolation_tt:0 "Запрещает новые объявления войны, создание фракций и вступление в них. Перед завершением необходимо выйти из фракции и закончить наступательные войны."
 MKN_agrarian_trapped_roads:0 "Степные завалы и капканы"
 MKN_agrarian_trapped_roads_desc:0 "Вражеские части теряют темп на сельских дорогах, пока территория принадлежит Махновщине и находится под её контролем."
 MKN_black_partition_hostility:0 "Передел помещичьих земель"
 MKN_steppe_hunter_training:0 "Охотничья подготовка степной пехоты"
 MKN_steppe_hunter_training_desc:0 "Специальная подготовка к бою на равнинах и в лесах, выдаваемая аграрным фокусом."
 MKN_grain_barter_reward_tt:0 "Через §Y60 дней§!: §G+50§! политической власти и §G1§! внекартовая гражданская фабрика на §Y180 дней§!. При отмене стоимость возвращается."
```

## localisation/english/MKN_agrarian_l_english.yml

Новый файл целиком, UTF-8 с BOM.

```yaml
l_english:
 MKN_great_rural_exodus:0 "The Great Rural Exodus"
 MKN_great_rural_exodus_desc:0 "The city promised freedom and delivered a queue at the factory gate. Let workers return to their kin and build new homesteads on the black soil. Families will grow, but factories must make do with fewer hands."
 MKN_black_partition_of_soil:0 "The Black Partition of the Soil"
 MKN_black_partition_of_soil_desc:0 "No one who has seen the land only through a manor window has a right to it. Village assemblies will draw the boundaries themselves. Peasants will gain confidence in the next harvest, and neighboring landlords another reason to hate us."
 MKN_village_assembly_sovereignty:0 "The Village Assembly Is the Highest Law"
 MKN_village_assembly_sovereignty_desc:0 "Neither a city clerk nor a visiting orator will command our homestead. The assembly settles disputes, elects its elder and answers to its neighbors. Common authority will grow slower, but foreign commands will struggle to take root here."
 MKN_abolition_of_paper_money:0 "Abolition of Paper Money"
 MKN_abolition_of_paper_money_desc:0 "The city prints paper; we grow bread. Accounts will be kept in measures of grain, honest weight and village granary receipts. Let foreign exchanges tremble: their quotations cannot erase our harvest."
 MKN_village_smithies_over_plants:0 "Village Smithies Instead of Giants"
 MKN_village_smithies_over_plants_desc:0 "The village needs no giant furnaces to build battleships and carriers. It needs thousands of smithies to forge a plow, fit an axe and make parts for hunting rifles. Let the cities build tanks and aircraft, if they can find bread."
 MKN_steppe_grain_monopoly:0 "The Steppe Grain Monopoly"
 MKN_steppe_grain_monopoly_desc:0 "While city ministers argue over gold, their people need bread. Surplus harvests will buy machinery and political concessions. Buyers may resent our terms, but an empty stomach argues louder than an ambassador."
 MKN_hunters_of_the_steppe:0 "Hunters and Trappers of the Steppe"
 MKN_hunters_of_the_steppe_desc:0 "A hunter reads grass and bark better than a staff map. He can guide a company to the forest edge and spot an ambush on the open steppe. Drill comes reluctantly: a free person takes time to learn to march at a whistle."
 MKN_fortified_homesteads:0 "Stone Sheepfolds and Ramparts"
 MKN_fortified_homesteads_desc:0 "A thick sheepfold wall, an earthen bank and a dry ditch will serve better than promises from the city. Every homestead must prepare shelter, stored water and a place for a rifleman."
 MKN_traps_and_ambush_lines:0 "Wolf Traps on the Roads"
 MKN_traps_and_ambush_lines_desc:0 "We know every causeway and ravine. Our detachment follows familiar paths without losing cohesion; a foreign column meets barricades, false turns and wire beneath its wheels."
 MKN_empty_field_doctrine:0 "The Empty Field Plan"
 MKN_empty_field_doctrine_desc:0 "If foreign regiments cross our boundary, they will find no grain. Elevators will empty, wells will be closed and livestock driven into the marshes. The invader will seize scorched ash and face hunger in the freezing steppe wind."
 MKN_death_to_grain_thieves:0 "A Death Sentence for Invaders"
 MKN_death_to_grain_thieves_desc:0 "Those who come to take the last sack from our children will find no submission. Granaries will become fortresses, elders will gather the companies, and no homestead will surrender for an invader’s convenience."
 MKN_chernozem_autarky:0 "Black Soil Autarky"
 MKN_chernozem_autarky_desc:0 "Let the old world burn in the fires of empires and colonial wars. The steppe is fed, armed and free. We bow to no one, ask for no foreign land and will admit no master through our gate."
 MKN_rural_exodus_idea:0 "Return to the Land"
 MKN_rural_exodus_idea_desc:0 "New homesteads and larger families accelerate population growth. Workers leave the cities’ factories, reducing military industrial output."
 MKN_black_partition_idea:0 "The Black Partition"
 MKN_black_partition_idea_desc:0 "A family granted land provides for much of its own needs. Stability rises as dependence on urban consumer industry falls."
 MKN_village_sovereignty_idea:0 "Sovereignty of the Village Assembly"
 MKN_village_sovereignty_idea_desc:0 "Unfamiliar authority faces stubborn resistance on our land. Our own common orders also require the consent of many villages and consume political energy."
 MKN_grain_currency_idea:0 "Grain Currency"
 MKN_grain_currency_idea_desc:0 "Village accounts rest on the harvest, not foreign paper exchange rates. Grain settlements withstand market panic, though foreign merchants dislike our arrangements."
 MKN_village_smithies_idea:0 "Village Smithies"
 MKN_village_smithies_idea_desc:0 "Rifle parts and simple support equipment cost less. Complex armored vehicles and aircraft lack an engineering school and are researched much more slowly."
 MKN_steppe_grain_monopoly_idea:0 "Grain Dictate"
 MKN_steppe_grain_monopoly_idea_desc:0 "Our neighbors buy the harvest, but resent the terms dictated by village granaries."
 MKN_hunters_idea:0 "Steppe Hunters"
 MKN_hunters_idea_desc:0 "Experienced scouts and marksmen are particularly dangerous on plains and in forests. They take longer to adapt to army discipline."
 MKN_fortified_homesteads_idea:0 "Fortified Homesteads"
 MKN_fortified_homesteads_idea_desc:0 "Stone buildings and prepared earthworks allow a deep defensive position to be established quickly."
 MKN_steppe_traps_idea:0 "Treacherous Roads"
 MKN_steppe_traps_idea_desc:0 "Familiar paths preserve our detachments’ cohesion. Enemy troops move more slowly through territory we own and control."
 MKN_empty_field_idea:0 "The Empty Field"
 MKN_empty_field_idea_desc:0 "Hidden stocks and supply carts departing with the villagers leave the enemy without local provisions."
 MKN_death_to_thieves_idea:0 "We Will Not Yield Our Own"
 MKN_death_to_thieves_idea_desc:0 "The people fight for their land to the final defensive line. A captured town square is not enough reason to capitulate."
 MKN_chernozem_autarky_idea:0 "Black Soil Autarky"
 MKN_chernozem_autarky_idea_desc:0 "Grain and militia secure the steppe’s independence. New war declarations, faction creation and faction membership are forbidden; an enemy attack does not remove the right to defend ourselves."
 MKN_grain_barter_factory_idea:0 "Machinery for the Harvest"
 MKN_grain_barter_factory_idea_desc:0 "Surplus grain has secured a temporary production line: one off-map civilian factory for 180 days. It will be removed when the agreement ends."
 MKN_barter_grain_surplus:0 "Barter the Surplus Harvest"
 MKN_barter_grain_surplus_desc:0 "Spend 25 PP to organize a 60-day exchange of surplus grain. Completion grants 50 PP and one off-map civilian factory for 180 days. The decision has a 180-day cooldown; active agreements cannot stack. Cancellation refunds the cost."
 MKN_grain_barter_unlock_tt:0 "Unlocks §YBarter the Surplus Harvest§!: §Y25 PP§!, §Y60 days§! preparation, then §G50 PP§! and §G1§! off-map civilian factory for §Y180 days§!."
 MKN_grain_currency_resilience_tt:0 "Grain barter does not depend on international market access, import routes or embargoes."
 MKN_hunters_terrain_tt:0 "Infantry, militia, irregular and special infantry: §G+20%§! attack on §Yplains§! and in §Yforests§!."
 MKN_steppe_traps_tt:0 "Enemy army speed in states we own and control: §G−30%§!."
 MKN_agrarian_isolation_tt:0 "Forbids new war declarations, faction creation and joining factions. Leave any faction and end offensive wars before completing this focus."
 MKN_agrarian_trapped_roads:0 "Steppe Barricades and Traps"
 MKN_agrarian_trapped_roads_desc:0 "Enemy formations lose momentum on village roads while the territory is owned and controlled by Makhnovshchina."
 MKN_black_partition_hostility:0 "Partition of Landed Estates"
 MKN_steppe_hunter_training:0 "Steppe Infantry Hunting Training"
 MKN_steppe_hunter_training_desc:0 "Special training for combat on plains and in forests, granted by the agrarian focus."
 MKN_grain_barter_reward_tt:0 "After §Y60 days§!: §G+50§! political power and §G1§! off-map civilian factory for §Y180 days§!. Cancellation refunds the cost."
```

## interface/MKN_political_expansions.gfx

Новый файл целиком. Содержит обычные и светящиеся спрайты всех 36 новых политических фокусов. Текстуры, исходники и точные промпты перечислены в [манифесте](art/mkn_political_expansions/assets.json).

```pdx
# Sources and prompts: docs/art/mkn_political_expansions/
spriteTypes = {
	spriteType = {
		name = GFX_focus_MKN_field_counter_intelligence
		texturefile = "gfx/interface/goals/MKN_field_counter_intelligence.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_field_counter_intelligence.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_field_counter_intelligence.dds"
		}
		legacy_lazy_load = no
		name = GFX_focus_MKN_field_counter_intelligence_shine
		texturefile = "gfx/interface/goals/MKN_field_counter_intelligence.dds"
	}
	spriteType = {
		name = GFX_focus_MKN_disarming_the_communes
		texturefile = "gfx/interface/goals/MKN_disarming_the_communes.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_disarming_the_communes.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_disarming_the_communes.dds"
		}
		legacy_lazy_load = no
		name = GFX_focus_MKN_disarming_the_communes_shine
		texturefile = "gfx/interface/goals/MKN_disarming_the_communes.dds"
	}
	spriteType = {
		name = GFX_focus_MKN_tribunals_of_the_black_staff
		texturefile = "gfx/interface/goals/MKN_tribunals_of_the_black_staff.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_tribunals_of_the_black_staff.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_tribunals_of_the_black_staff.dds"
		}
		legacy_lazy_load = no
		name = GFX_focus_MKN_tribunals_of_the_black_staff_shine
		texturefile = "gfx/interface/goals/MKN_tribunals_of_the_black_staff.dds"
	}
	spriteType = {
		name = GFX_focus_MKN_labor_armies
		texturefile = "gfx/interface/goals/MKN_labor_armies.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_labor_armies.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_labor_armies.dds"
		}
		legacy_lazy_load = no
		name = GFX_focus_MKN_labor_armies_shine
		texturefile = "gfx/interface/goals/MKN_labor_armies.dds"
	}
	spriteType = {
		name = GFX_focus_MKN_schools_of_young_insurgents
		texturefile = "gfx/interface/goals/MKN_schools_of_young_insurgents.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_schools_of_young_insurgents.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_schools_of_young_insurgents.dds"
		}
		legacy_lazy_load = no
		name = GFX_focus_MKN_schools_of_young_insurgents_shine
		texturefile = "gfx/interface/goals/MKN_schools_of_young_insurgents.dds"
	}
	spriteType = {
		name = GFX_focus_MKN_cult_of_fallen_atamans
		texturefile = "gfx/interface/goals/MKN_cult_of_fallen_atamans.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_cult_of_fallen_atamans.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_cult_of_fallen_atamans.dds"
		}
		legacy_lazy_load = no
		name = GFX_focus_MKN_cult_of_fallen_atamans_shine
		texturefile = "gfx/interface/goals/MKN_cult_of_fallen_atamans.dds"
	}
	spriteType = {
		name = GFX_focus_MKN_military_districts
		texturefile = "gfx/interface/goals/MKN_military_districts.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_military_districts.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_military_districts.dds"
		}
		legacy_lazy_load = no
		name = GFX_focus_MKN_military_districts_shine
		texturefile = "gfx/interface/goals/MKN_military_districts.dds"
	}
	spriteType = {
		name = GFX_focus_MKN_council_of_field_commanders
		texturefile = "gfx/interface/goals/MKN_council_of_field_commanders.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_council_of_field_commanders.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_council_of_field_commanders.dds"
		}
		legacy_lazy_load = no
		name = GFX_focus_MKN_council_of_field_commanders_shine
		texturefile = "gfx/interface/goals/MKN_council_of_field_commanders.dds"
	}
	spriteType = {
		name = GFX_focus_MKN_the_supreme_warlord
		texturefile = "gfx/interface/goals/MKN_the_supreme_warlord.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_the_supreme_warlord.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_the_supreme_warlord.dds"
		}
		legacy_lazy_load = no
		name = GFX_focus_MKN_the_supreme_warlord_shine
		texturefile = "gfx/interface/goals/MKN_the_supreme_warlord.dds"
	}
	spriteType = {
		name = GFX_focus_MKN_preemptive_strike_doctrine
		texturefile = "gfx/interface/goals/MKN_preemptive_strike_doctrine.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_preemptive_strike_doctrine.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_preemptive_strike_doctrine.dds"
		}
		legacy_lazy_load = no
		name = GFX_focus_MKN_preemptive_strike_doctrine_shine
		texturefile = "gfx/interface/goals/MKN_preemptive_strike_doctrine.dds"
	}
	spriteType = {
		name = GFX_focus_MKN_military_marches
		texturefile = "gfx/interface/goals/MKN_military_marches.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_military_marches.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_military_marches.dds"
		}
		legacy_lazy_load = no
		name = GFX_focus_MKN_military_marches_shine
		texturefile = "gfx/interface/goals/MKN_military_marches.dds"
	}
	spriteType = {
		name = GFX_focus_MKN_black_banner_over_europe
		texturefile = "gfx/interface/goals/MKN_black_banner_over_europe.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_black_banner_over_europe.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_black_banner_over_europe.dds"
		}
		legacy_lazy_load = no
		name = GFX_focus_MKN_black_banner_over_europe_shine
		texturefile = "gfx/interface/goals/MKN_black_banner_over_europe.dds"
	}
	spriteType = {
		name = GFX_focus_MKN_ferrer_modern_schools
		texturefile = "gfx/interface/goals/MKN_ferrer_modern_schools.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_ferrer_modern_schools.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_ferrer_modern_schools.dds"
		}
		legacy_lazy_load = no
		name = GFX_focus_MKN_ferrer_modern_schools_shine
		texturefile = "gfx/interface/goals/MKN_ferrer_modern_schools.dds"
	}
	spriteType = {
		name = GFX_focus_MKN_sanctuary_of_free_thought
		texturefile = "gfx/interface/goals/MKN_sanctuary_of_free_thought.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_sanctuary_of_free_thought.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_sanctuary_of_free_thought.dds"
		}
		legacy_lazy_load = no
		name = GFX_focus_MKN_sanctuary_of_free_thought_shine
		texturefile = "gfx/interface/goals/MKN_sanctuary_of_free_thought.dds"
	}
	spriteType = {
		name = GFX_focus_MKN_eradication_of_wage_labor
		texturefile = "gfx/interface/goals/MKN_eradication_of_wage_labor.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_eradication_of_wage_labor.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_eradication_of_wage_labor.dds"
		}
		legacy_lazy_load = no
		name = GFX_focus_MKN_eradication_of_wage_labor_shine
		texturefile = "gfx/interface/goals/MKN_eradication_of_wage_labor.dds"
	}
	spriteType = {
		name = GFX_focus_MKN_imperative_mandate
		texturefile = "gfx/interface/goals/MKN_imperative_mandate.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_imperative_mandate.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_imperative_mandate.dds"
		}
		legacy_lazy_load = no
		name = GFX_focus_MKN_imperative_mandate_shine
		texturefile = "gfx/interface/goals/MKN_imperative_mandate.dds"
	}
	spriteType = {
		name = GFX_focus_MKN_syndicalist_work_ethic
		texturefile = "gfx/interface/goals/MKN_syndicalist_work_ethic.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_syndicalist_work_ethic.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_syndicalist_work_ethic.dds"
		}
		legacy_lazy_load = no
		name = GFX_focus_MKN_syndicalist_work_ethic_shine
		texturefile = "gfx/interface/goals/MKN_syndicalist_work_ethic.dds"
	}
	spriteType = {
		name = GFX_focus_MKN_consumer_autonomy
		texturefile = "gfx/interface/goals/MKN_consumer_autonomy.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_consumer_autonomy.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_consumer_autonomy.dds"
		}
		legacy_lazy_load = no
		name = GFX_focus_MKN_consumer_autonomy_shine
		texturefile = "gfx/interface/goals/MKN_consumer_autonomy.dds"
	}
	spriteType = {
		name = GFX_focus_MKN_elected_instructor_collegiums
		texturefile = "gfx/interface/goals/MKN_elected_instructor_collegiums.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_elected_instructor_collegiums.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_elected_instructor_collegiums.dds"
		}
		legacy_lazy_load = no
		name = GFX_focus_MKN_elected_instructor_collegiums_shine
		texturefile = "gfx/interface/goals/MKN_elected_instructor_collegiums.dds"
	}
	spriteType = {
		name = GFX_focus_MKN_volost_signal_chains
		texturefile = "gfx/interface/goals/MKN_volost_signal_chains.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_volost_signal_chains.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_volost_signal_chains.dds"
		}
		legacy_lazy_load = no
		name = GFX_focus_MKN_volost_signal_chains_shine
		texturefile = "gfx/interface/goals/MKN_volost_signal_chains.dds"
	}
	spriteType = {
		name = GFX_focus_MKN_hearth_defense_doctrine
		texturefile = "gfx/interface/goals/MKN_hearth_defense_doctrine.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_hearth_defense_doctrine.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_hearth_defense_doctrine.dds"
		}
		legacy_lazy_load = no
		name = GFX_focus_MKN_hearth_defense_doctrine_shine
		texturefile = "gfx/interface/goals/MKN_hearth_defense_doctrine.dds"
	}
	spriteType = {
		name = GFX_focus_MKN_subversion_of_enemy_ranks
		texturefile = "gfx/interface/goals/MKN_subversion_of_enemy_ranks.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_subversion_of_enemy_ranks.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_subversion_of_enemy_ranks.dds"
		}
		legacy_lazy_load = no
		name = GFX_focus_MKN_subversion_of_enemy_ranks_shine
		texturefile = "gfx/interface/goals/MKN_subversion_of_enemy_ranks.dds"
	}
	spriteType = {
		name = GFX_focus_MKN_autonomous_free_communes
		texturefile = "gfx/interface/goals/MKN_autonomous_free_communes.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_autonomous_free_communes.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_autonomous_free_communes.dds"
		}
		legacy_lazy_load = no
		name = GFX_focus_MKN_autonomous_free_communes_shine
		texturefile = "gfx/interface/goals/MKN_autonomous_free_communes.dds"
	}
	spriteType = {
		name = GFX_focus_MKN_world_federation_of_labor
		texturefile = "gfx/interface/goals/MKN_world_federation_of_labor.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_world_federation_of_labor.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_world_federation_of_labor.dds"
		}
		legacy_lazy_load = no
		name = GFX_focus_MKN_world_federation_of_labor_shine
		texturefile = "gfx/interface/goals/MKN_world_federation_of_labor.dds"
	}
	spriteType = {
		name = GFX_focus_MKN_great_rural_exodus
		texturefile = "gfx/interface/goals/MKN_great_rural_exodus.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_great_rural_exodus.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_great_rural_exodus.dds"
		}
		legacy_lazy_load = no
		name = GFX_focus_MKN_great_rural_exodus_shine
		texturefile = "gfx/interface/goals/MKN_great_rural_exodus.dds"
	}
	spriteType = {
		name = GFX_focus_MKN_black_partition_of_soil
		texturefile = "gfx/interface/goals/MKN_black_partition_of_soil.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_black_partition_of_soil.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_black_partition_of_soil.dds"
		}
		legacy_lazy_load = no
		name = GFX_focus_MKN_black_partition_of_soil_shine
		texturefile = "gfx/interface/goals/MKN_black_partition_of_soil.dds"
	}
	spriteType = {
		name = GFX_focus_MKN_village_assembly_sovereignty
		texturefile = "gfx/interface/goals/MKN_village_assembly_sovereignty.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_village_assembly_sovereignty.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_village_assembly_sovereignty.dds"
		}
		legacy_lazy_load = no
		name = GFX_focus_MKN_village_assembly_sovereignty_shine
		texturefile = "gfx/interface/goals/MKN_village_assembly_sovereignty.dds"
	}
	spriteType = {
		name = GFX_focus_MKN_abolition_of_paper_money
		texturefile = "gfx/interface/goals/MKN_abolition_of_paper_money.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_abolition_of_paper_money.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_abolition_of_paper_money.dds"
		}
		legacy_lazy_load = no
		name = GFX_focus_MKN_abolition_of_paper_money_shine
		texturefile = "gfx/interface/goals/MKN_abolition_of_paper_money.dds"
	}
	spriteType = {
		name = GFX_focus_MKN_village_smithies_over_plants
		texturefile = "gfx/interface/goals/MKN_village_smithies_over_plants.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_village_smithies_over_plants.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_village_smithies_over_plants.dds"
		}
		legacy_lazy_load = no
		name = GFX_focus_MKN_village_smithies_over_plants_shine
		texturefile = "gfx/interface/goals/MKN_village_smithies_over_plants.dds"
	}
	spriteType = {
		name = GFX_focus_MKN_steppe_grain_monopoly
		texturefile = "gfx/interface/goals/MKN_steppe_grain_monopoly.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_steppe_grain_monopoly.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_steppe_grain_monopoly.dds"
		}
		legacy_lazy_load = no
		name = GFX_focus_MKN_steppe_grain_monopoly_shine
		texturefile = "gfx/interface/goals/MKN_steppe_grain_monopoly.dds"
	}
	spriteType = {
		name = GFX_focus_MKN_hunters_of_the_steppe
		texturefile = "gfx/interface/goals/MKN_hunters_of_the_steppe.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_hunters_of_the_steppe.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_hunters_of_the_steppe.dds"
		}
		legacy_lazy_load = no
		name = GFX_focus_MKN_hunters_of_the_steppe_shine
		texturefile = "gfx/interface/goals/MKN_hunters_of_the_steppe.dds"
	}
	spriteType = {
		name = GFX_focus_MKN_fortified_homesteads
		texturefile = "gfx/interface/goals/MKN_fortified_homesteads.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_fortified_homesteads.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_fortified_homesteads.dds"
		}
		legacy_lazy_load = no
		name = GFX_focus_MKN_fortified_homesteads_shine
		texturefile = "gfx/interface/goals/MKN_fortified_homesteads.dds"
	}
	spriteType = {
		name = GFX_focus_MKN_traps_and_ambush_lines
		texturefile = "gfx/interface/goals/MKN_traps_and_ambush_lines.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_traps_and_ambush_lines.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_traps_and_ambush_lines.dds"
		}
		legacy_lazy_load = no
		name = GFX_focus_MKN_traps_and_ambush_lines_shine
		texturefile = "gfx/interface/goals/MKN_traps_and_ambush_lines.dds"
	}
	spriteType = {
		name = GFX_focus_MKN_empty_field_doctrine
		texturefile = "gfx/interface/goals/MKN_empty_field_doctrine.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_empty_field_doctrine.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_empty_field_doctrine.dds"
		}
		legacy_lazy_load = no
		name = GFX_focus_MKN_empty_field_doctrine_shine
		texturefile = "gfx/interface/goals/MKN_empty_field_doctrine.dds"
	}
	spriteType = {
		name = GFX_focus_MKN_death_to_grain_thieves
		texturefile = "gfx/interface/goals/MKN_death_to_grain_thieves.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_death_to_grain_thieves.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_death_to_grain_thieves.dds"
		}
		legacy_lazy_load = no
		name = GFX_focus_MKN_death_to_grain_thieves_shine
		texturefile = "gfx/interface/goals/MKN_death_to_grain_thieves.dds"
	}
	spriteType = {
		name = GFX_focus_MKN_chernozem_autarky
		texturefile = "gfx/interface/goals/MKN_chernozem_autarky.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_chernozem_autarky.dds"
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
			animationmaskfile = "gfx/interface/goals/MKN_chernozem_autarky.dds"
		}
		legacy_lazy_load = no
		name = GFX_focus_MKN_chernozem_autarky_shine
		texturefile = "gfx/interface/goals/MKN_chernozem_autarky.dds"
	}
}
```

Предпросмотр: [96×96](mkn_political_expansions_preview_1x.png), [увеличение ×2](mkn_political_expansions_preview_2x.png).
