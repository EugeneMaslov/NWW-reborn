# MKN: обновлённые военные фокусы и полевые штабы

Снимок действующих скриптов NWW Reborn на 16 октября 2026 года. Самодостаточный файл для передачи другой нейросети: названия RU/EN, описания, точные награды, зависимости, ограничения, решения, общие духи и вспомогательные эффекты.

Военные деревья: **30 фокусов** (армия: 12, авиация: 10, флот: 8). Отдельно: 30 связанных фокусов с прямыми военными наградами; 51 дополнительных определений предпосылок.

## Что изменилось относительно старого пакета

Прежние 130 военных фокусов переработаны в 30 институтов. Часть постоянных бонусов перенесена в тактические решения, строительство — в штабные проекты; поэтому оценивать баланс только по completion_reward фокусов недостаточно. Архивные ID используются для миграции сохранений и не означают отдельные игровые фокусы.

## Правила анализа

- Первая мировая война не происходила. Сохранять существующий лор, ID и монарха Махно с его портретом.
- cost измеряется неделями: 5 = 35 дней, 10 = 70 дней. Несколько блоков prerequisite соединяются И; focus в одном блоке — ИЛИ. available добавляет ограничения, mutually_exclusive исключает альтернативную программу.
- Один развиваемый постоянный дух на службу: MKN_army_development, MKN_air_development, MKN_navy_development. Параметры add_to_variable складываются; восстановление сохранений пересчитывает фактические ступени.
- MKN_marusyas_legacy — отдельное памятное исключение. Фокусы Маруси сохраняют общий доступ после штаба и требования технологий/Гуляйполя для дивизий.
- В наградах числовые параметры приведены в сырых единицах движка. Фактор 0.05 обычно означает 5 процентных пунктов; опыт, manpower и количество техники — абсолютные величины.
- if/limit/else, DLC, флаги, владение и контроль могут ограничивать выдачу. Перечень эффектов не означает безусловную сумму наград. Проверять полное определение.
- custom_effect_tooltip/show_mio_tooltip/unlock_mio_trait_tooltip только отображают информацию. Доступ к MIO, предприятиям и чертам определяется их собственными allowed/available.
- Тактики и проекты имеют собственные цены, сроки, ограничения и отмену. Не переносить их награды обратно в фокусы без пересчёта баланса.
- Миграция старых сохранений не должна повторно выдавать дивизии, опыт, технику или постройки. Старые флаги могут уже учитывать часть постоянных бонусов.
- Статический снимок не подтверждает работу в новой кампании. После изменений проверять текущие игровые документацию и DLC-примеры, tooltips и свежий лог.

## Сводка фокусов

| Раздел | Название | ID | Дней |
| --- | --- | --- | --- |
| Армия | Штаб степных армий | `MKN_steppe_general_staff` | 70 |
| Армия | Моторизованный авангард | `MKN_motorized_vanguard` | 70 |
| Армия | Степная Орда | `MKN_steppe_horde` | 70 |
| Армия | Бронепоезда и ремонтные базы | `MKN_armored_trains_and_repair_focus` | 70 |
| Армия | Схроны и базы снабжения | `MKN_hidden_supply_bases_focus` | 35 |
| Армия | Огневая поддержка коммун | `MKN_communal_fire_support_focus` | 70 |
| Армия | Связь вольных колонн | `MKN_free_column_command_focus` | 35 |
| Армия | Штаб общевойсковых соединений | `MKN_combined_arms_command_focus` | 35 |
| Армия | Армия вольных колонн | `MKN_free_army_compact` | 70 |
| Армия | Механизированная армия коммун | `MKN_mechanized_compact` | 70 |
| Армия | Памяти атаманши Маруси | `MKN_memory_of_atamansha_marusya` | 35 |
| Армия | Батальоны Чёрной гвардии | `MKN_the_black_guard_battalions` | 35 |
| Авиация | Степные соколы и школы | `MKN_steppe_hawks_and_schools` | 70 |
| Авиация | Авиакооперативы перехвата | `MKN_interceptor_cooperatives` | 70 |
| Авиация | Летающая артиллерия | `MKN_flying_artillery_focus` | 70 |
| Авиация | Эшелонированное ПВО коммун | `MKN_communal_aa_defense_focus` | 35 |
| Авиация | Передовые посадочные полосы | `MKN_forward_airstrips_focus` | 35 |
| Авиация | Единый стандарт авиамастерских | `MKN_airframe_standardization_focus` | 70 |
| Авиация | Карта для вольных колонн | `MKN_air_ground_coordination_focus` | 35 |
| Авиация | Небо под защитой коммун | `MKN_free_sky_compact` | 70 |
| Авиация | Сеть штурмовых авиамастерских | `MKN_cas_workshop_network_focus` | 35 |
| Авиация | Крылья над вольными колоннами | `MKN_air_support_compact` | 70 |
| Флот | Черноморская флотилия и верфи | `MKN_black_sea_flotilla_and_yards` | 70 |
| Флот | Служба морского эскорта | `MKN_sea_escort_service` | 70 |
| Флот | Торпедные артели | `MKN_torpedo_artels_focus` | 70 |
| Флот | Береговые укрепления | `MKN_coastal_fortifications_focus` | 35 |
| Флот | Тайные базы контрабандистов | `MKN_hidden_smuggler_bases_focus` | 70 |
| Флот | Ремонтные артели эскорта | `MKN_escort_repair_network_focus` | 70 |
| Флот | Море для вольных рейдеров | `MKN_raider_compact` | 70 |
| Флот | Море для хлебных конвоев | `MKN_escort_compact` | 70 |

## Армия

### Штаб степных армий — `MKN_steppe_general_staff`

EN: Steppe Army Staff.

Описание RU: Вооружим колонны и введём общий порядок сбора, сохраняя выборных командиров.\n\nСогласованные эшелоны подвезут боеприпасы быстрее случайных крестьянских обозов.\n\nШтаб Белаша свяжет самостоятельные отряды общим планом операций.\n\nОткрывает одноразовые тактики полевого штаба за опыт и командный ресурс.

Описание EN: Equip the columns and establish mustering rules under elected commanders.\n\nScheduled trains will deliver ammunition instead of relying on improvised carts.\n\nBelash's staff will coordinate independent detachments through shared operational plans.\n\nUnlocks one-time field headquarters tactics purchased with experience and command power.

Источник: `common/national_focus/MKN.txt:2049`. Стоимость: 10 (70 дней). Координаты: x=50, y=0.

Предпосылки: нет нарисованной предпосылки; см. available.

Взаимоисключения: нет.

Прямые продолжения: MKN_steppe_horde, MKN_motorized_vanguard.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_steppe_general_staff
    icon = GFX_focus_generic_military_academy
    x = 50
    y = 0
    cost = 10
    available_if_capitulated = no
    bypass = {
        hidden_trigger = {
            has_country_flag = MKN_military_stat_tachanka_columns
            has_country_flag = MKN_military_stat_railway_war
            has_country_flag = MKN_military_stat_steppe_general_staff
            has_country_flag = MKN_military_reward_tachanka_columns
            has_country_flag = MKN_military_reward_railway_war
            has_country_flag = MKN_military_reward_steppe_general_staff
        }
    }
    completion_reward = {
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_tachanka_columns
                    }
                }
            }
            add_to_variable = {
                MKN_army_army_org_factor = 0.04
                tooltip = MKN_army_army_org_factor_tt
            }
            set_country_flag = MKN_military_stat_tachanka_columns
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_tachanka_columns
                    }
                }
            }
            army_experience = 20
            add_equipment_to_stockpile = {
                type = infantry_equipment_0
                amount = 800
                producer = ROOT
            }
            set_country_flag = MKN_military_reward_tachanka_columns
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_railway_war
                    }
                }
            }
            add_to_variable = {
                MKN_army_supply_consumption_factor = -0.05
                tooltip = MKN_army_supply_consumption_factor_tt
            }
            set_country_flag = MKN_military_stat_railway_war
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_railway_war
                    }
                }
            }
            add_tech_bonus = {
                name = MKN_railway_war
                bonus = 0.5
                uses = 1
                category = train_tech
            }
            add_tech_bonus = {
                name = MKN_railway_war
                bonus = 0.5
                uses = 1
                category = logistics_tech
            }
            set_country_flag = MKN_military_reward_railway_war
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_steppe_general_staff
                    }
                }
            }
            add_to_variable = {
                MKN_army_max_planning = 0.05
                tooltip = MKN_army_max_planning_tt
            }
            set_country_flag = MKN_military_stat_steppe_general_staff
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_steppe_general_staff
                    }
                }
            }
            army_experience = 25
            add_command_power = 20
            add_doctrine_cost_reduction = {
                name = MKN_steppe_general_staff
                cost_reduction = 0.35
                uses = 2
                category = land_doctrine
            }
            set_country_flag = MKN_military_reward_steppe_general_staff
        }
        set_country_flag = MKN_military_bundle_steppe_general_staff
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
        custom_effect_tooltip = MKN_army_hq_unlock_tt
    }
    ai_will_do = {
        factor = 3
    }
}
```

### Моторизованный авангард — `MKN_motorized_vanguard`

EN: The Motorized Vanguard.

Описание RU: Тракторные артели освоят бронетехнику для прорыва, но ей нужны экипажи и горючее.\n\nЭкипаж должен уметь чинить машину и действовать вместе с пехотой.\n\nКвартирмейстеры сведут потребности моторизованных частей в единый реестр.\n\nГрузовики и заправщики будут следовать за наступающей бронёй.

Описание EN: Tractor cooperatives will develop breakthrough armour that needs trained crews and fuel.\n\nCrews must repair their vehicles and cooperate with infantry.\n\nQuartermasters will reconcile the supply requirements of motorized formations.\n\nTrucks and fuel tenders will follow advancing armoured units.

Источник: `common/national_focus/MKN.txt:2785`. Стоимость: 10 (70 дней). Координаты: x=46, y=1.

Предпосылки: (Штаб степных армий [MKN_steppe_general_staff]).

Взаимоисключения: MKN_steppe_horde.

Прямые продолжения: MKN_armored_trains_and_repair_focus.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_motorized_vanguard
    icon = GFX_focus_MKN_company_kommunar
    x = 46
    y = 1
    cost = 10
    available_if_capitulated = no
    prerequisite = {
        focus = MKN_steppe_general_staff
    }
    mutually_exclusive = {
        focus = MKN_steppe_horde
    }
    bypass = {
        hidden_trigger = {
            has_country_flag = MKN_military_stat_steel_horses
            has_country_flag = MKN_military_stat_tank_crews
            has_country_flag = MKN_military_stat_steppe_quartermasters
            has_country_flag = MKN_military_stat_mobile_supply_columns
            has_country_flag = MKN_military_reward_steel_horses
            has_country_flag = MKN_military_reward_tank_crews
            has_country_flag = MKN_military_reward_steppe_quartermasters
            has_country_flag = MKN_military_reward_mobile_supply_columns
        }
    }
    completion_reward = {
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_steel_horses
                    }
                }
            }
            add_to_variable = {
                MKN_army_army_armor_attack_factor = 0.05
                tooltip = MKN_army_army_armor_attack_factor_tt
            }
            set_country_flag = MKN_military_stat_steel_horses
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_steel_horses
                    }
                }
            }
            add_tech_bonus = {
                name = MKN_steel_horses
                bonus = 0.75
                uses = 1
                category = armor
            }
            set_country_flag = MKN_military_reward_steel_horses
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_tank_crews
                    }
                }
            }
            add_to_variable = {
                MKN_army_army_org_factor = 0.04
                tooltip = MKN_army_army_org_factor_tt
            }
            set_country_flag = MKN_military_stat_tank_crews
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_tank_crews
                    }
                }
            }
            army_experience = 20
            add_tech_bonus = {
                name = MKN_tank_crews
                bonus = 0.5
                uses = 1
                category = maintenance_company_tech
            }
            if = {
                limit = {
                    has_dlc = "Arms Against Tyranny"
                }
                mio:MKN_kommunar_organization = {
                    add_mio_size = 1
                }
            }
            add_mastery_bonus = {
                bonus = 0.1
                days = 240
                track = armor
                name = MKN_tank_crews
            }
            set_country_flag = MKN_military_reward_tank_crews
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_steppe_quartermasters
                    }
                }
            }
            add_to_variable = {
                MKN_army_supply_consumption_factor = -0.05
                tooltip = MKN_army_supply_consumption_factor_tt
            }
            set_country_flag = MKN_military_stat_steppe_quartermasters
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_steppe_quartermasters
                    }
                }
            }
            add_tech_bonus = {
                name = MKN_steppe_quartermasters
                bonus = 0.5
                uses = 1
                category = logistics_tech
            }
            set_country_flag = MKN_military_reward_steppe_quartermasters
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_mobile_supply_columns
                    }
                }
            }
            add_to_variable = {
                MKN_army_army_fuel_consumption_factor = -0.08
                tooltip = MKN_army_army_fuel_consumption_factor_tt
            }
            set_country_flag = MKN_military_stat_mobile_supply_columns
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_mobile_supply_columns
                    }
                }
            }
            add_equipment_to_stockpile = {
                type = motorized_equipment_1
                amount = 120
                producer = ROOT
            }
            set_country_flag = MKN_military_reward_mobile_supply_columns
        }
        set_country_flag = MKN_military_bundle_motorized_vanguard
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
        custom_effect_tooltip = MKN_military_program_progress_tt
    }
    ai_will_do = {
        factor = 3
    }
}
```

### Степная Орда — `MKN_steppe_horde`

EN: The Steppe Horde.

Описание RU: Сохраним мобильность конницы, вложившись в вооружение и связь вместо дорогой брони.\n\nСельские сборные пункты заранее распределят людей по отрядам.\n\nОбщие конюшни и запас верховых лошадей поддержат темп похода.\n\nПулемётные тачанки дадут конным отрядам огневую опору.

Описание EN: Preserve cavalry mobility by investing in weapons and communications rather than expensive armour.\n\nVillage mustering stations will assign recruits to detachments in advance.\n\nShared stables and remount reserves will sustain the march.\n\nMachine-gun carts will provide cavalry detachments with sustained firepower.

Источник: `common/national_focus/MKN.txt:2175`. Стоимость: 10 (70 дней). Координаты: x=54, y=1.

Предпосылки: (Штаб степных армий [MKN_steppe_general_staff]).

Взаимоисключения: MKN_motorized_vanguard.

Прямые продолжения: MKN_hidden_supply_bases_focus.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_steppe_horde
    icon = GFX_goal_generic_cavalry
    x = 54
    y = 1
    cost = 10
    available_if_capitulated = no
    prerequisite = {
        focus = MKN_steppe_general_staff
    }
    mutually_exclusive = {
        focus = MKN_motorized_vanguard
    }
    bypass = {
        hidden_trigger = {
            has_country_flag = MKN_military_stat_batko_cavalry
            has_country_flag = MKN_military_stat_village_muster
            has_country_flag = MKN_military_stat_remount_artels
            has_country_flag = MKN_military_stat_machinegun_carts
            has_country_flag = MKN_military_reward_batko_cavalry
            has_country_flag = MKN_military_reward_village_muster
            has_country_flag = MKN_military_reward_remount_artels
            has_country_flag = MKN_military_reward_machinegun_carts
        }
    }
    completion_reward = {
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_batko_cavalry
                    }
                }
            }
            add_to_variable = {
                MKN_army_modifier_army_sub_unit_cavalry_attack_factor = 0.08
                tooltip = MKN_army_modifier_army_sub_unit_cavalry_attack_factor_tt
            }
            set_country_flag = MKN_military_stat_batko_cavalry
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_batko_cavalry
                    }
                }
            }
            add_equipment_to_stockpile = {
                type = infantry_equipment_0
                amount = 600
                producer = ROOT
            }
            set_country_flag = MKN_military_reward_batko_cavalry
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_village_muster
                    }
                }
            }
            add_to_variable = {
                MKN_army_mobilization_speed = 0.15
                tooltip = MKN_army_mobilization_speed_tt
            }
            set_country_flag = MKN_military_stat_village_muster
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_village_muster
                    }
                }
            }
            army_experience = 15
            if = {
                limit = {
                    has_dlc = "Arms Against Tyranny"
                }
                mio:MKN_rifle_artels_organization = {
                    add_mio_size = 1
                }
            }
            set_country_flag = MKN_military_reward_village_muster
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_remount_artels
                    }
                }
            }
            add_to_variable = {
                MKN_army_modifier_army_sub_unit_cavalry_speed_factor = 0.08
                tooltip = MKN_army_modifier_army_sub_unit_cavalry_speed_factor_tt
            }
            set_country_flag = MKN_military_stat_remount_artels
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_remount_artels
                    }
                }
            }
            add_tech_bonus = {
                name = MKN_remount_artels
                bonus = 0.5
                uses = 1
                category = logistics_tech
            }
            set_country_flag = MKN_military_reward_remount_artels
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_machinegun_carts
                    }
                }
            }
            add_to_variable = {
                MKN_army_modifier_army_sub_unit_cavalry_attack_factor = 0.07
                tooltip = MKN_army_modifier_army_sub_unit_cavalry_attack_factor_tt
            }
            set_country_flag = MKN_military_stat_machinegun_carts
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_machinegun_carts
                    }
                }
            }
            add_equipment_to_stockpile = {
                type = infantry_equipment_0
                amount = 800
                producer = ROOT
            }
            add_tech_bonus = {
                name = MKN_machinegun_carts
                bonus = 0.5
                uses = 1
                category = infantry_weapons
            }
            if = {
                limit = {
                    has_dlc = "Arms Against Tyranny"
                }
                mio:MKN_rifle_artels_organization = {
                    add_mio_size = 1
                    unlock_mio_trait_tooltip = MKN_rifle_artels_organization_specialization_a
                }
            }
            if = {
                limit = {
                    has_dlc = "Arms Against Tyranny"
                }
                mio:MKN_rifle_artels_organization = {
                    add_mio_size = 1
                    unlock_mio_trait_tooltip = MKN_rifle_artels_organization_specialization_b
                }
            }
            set_country_flag = MKN_military_reward_machinegun_carts
        }
        set_country_flag = MKN_military_bundle_steppe_horde
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
        custom_effect_tooltip = MKN_military_program_progress_tt
    }
    ai_will_do = {
        factor = 3
    }
}
```

### Бронепоезда и ремонтные базы — `MKN_armored_trains_and_repair_focus`

EN: Armored Trains and Repair Bases.

Описание RU: Эвакуационные тягачи вернут повреждённые машины в мастерские.\n\nРемонтная база Днепра обеспечит запасные узлы и восстановление техники.

Описание EN: Recovery tractors will retrieve damaged vehicles for the workshops.\n\nA Dnipro repair plant will provide replacement assemblies and equipment repairs.

Источник: `common/national_focus/MKN.txt:2955`. Стоимость: 10 (70 дней). Координаты: x=46, y=2.

Предпосылки: (Моторизованный авангард [MKN_motorized_vanguard]).

Взаимоисключения: нет.

Прямые продолжения: MKN_communal_fire_support_focus.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_armored_trains_and_repair_focus
    icon = GFX_focus_generic_purchase_mechanized_equipment
    x = 46
    y = 2
    cost = 10
    available_if_capitulated = no
    prerequisite = {
        focus = MKN_motorized_vanguard
    }
    bypass = {
        hidden_trigger = {
            has_country_flag = MKN_military_stat_recovery_tractors
            has_country_flag = MKN_military_stat_tank_maintenance
            has_country_flag = MKN_military_reward_recovery_tractors
            has_country_flag = MKN_military_reward_tank_maintenance
        }
    }
    completion_reward = {
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_recovery_tractors
                    }
                }
            }
            add_to_variable = {
                MKN_army_attrition = -0.08
                tooltip = MKN_army_attrition_tt
            }
            set_country_flag = MKN_military_stat_recovery_tractors
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_recovery_tractors
                    }
                }
            }
            add_tech_bonus = {
                name = MKN_recovery_tractors
                bonus = 0.5
                uses = 1
                category = maintenance_company_tech
            }
            set_country_flag = MKN_military_reward_recovery_tractors
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_tank_maintenance
                    }
                }
            }
            add_to_variable = {
                MKN_army_repair_speed_factor = 0.1
                tooltip = MKN_army_repair_speed_factor_tt
            }
            set_country_flag = MKN_military_stat_tank_maintenance
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_tank_maintenance
                    }
                }
            }
            226 = {
                if = {
                    limit = {
                        is_owned_and_controlled_by = ROOT
                    }
                    add_extra_state_shared_building_slots = 1
                    add_building_construction = {
                        type = arms_factory
                        level = 1
                        instant_build = yes
                    }
                }
            }
            if = {
                limit = {
                    has_dlc = "Arms Against Tyranny"
                }
                mio:MKN_kommunar_organization = {
                    add_mio_size = 1
                    unlock_mio_trait_tooltip = MKN_kommunar_organization_specialization_a
                }
            }
            if = {
                limit = {
                    has_dlc = "Arms Against Tyranny"
                }
                mio:MKN_kommunar_organization = {
                    add_mio_size = 1
                    unlock_mio_trait_tooltip = MKN_kommunar_organization_specialization_b
                }
            }
            set_country_flag = MKN_military_reward_tank_maintenance
        }
        set_country_flag = MKN_military_bundle_armored_trains_and_repair_focus
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
        custom_effect_tooltip = MKN_military_program_progress_tt
        custom_effect_tooltip = MKN_project_front_railway_unlock_tt
        custom_effect_tooltip = MKN_project_repair_infrastructure_unlock_tt
    }
    ai_will_do = {
        factor = 3
    }
}
```

### Схроны и базы снабжения — `MKN_hidden_supply_bases_focus`

EN: Hidden Supply Bases.

Описание RU: Местные проводники найдут броды и обходные тропы раньше противника.\n\nВетеринарная служба снизит потери лошадей в длительных переходах.

Описание EN: Local guides will locate fords and flanking routes before the enemy.\n\nVeterinary teams will reduce horse losses on long marches.

Источник: `common/national_focus/MKN.txt:2356`. Стоимость: 5 (35 дней). Координаты: x=54, y=2.

Предпосылки: (Степная Орда [MKN_steppe_horde]).

Взаимоисключения: нет.

Прямые продолжения: MKN_free_column_command_focus.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_hidden_supply_bases_focus
    icon = GFX_focus_generic_infiltration
    x = 54
    y = 2
    cost = 5
    available_if_capitulated = no
    prerequisite = {
        focus = MKN_steppe_horde
    }
    bypass = {
        hidden_trigger = {
            has_country_flag = MKN_military_stat_local_guides
            has_country_flag = MKN_military_stat_field_veterinary
            has_country_flag = MKN_military_reward_local_guides
            has_country_flag = MKN_military_reward_field_veterinary
        }
    }
    completion_reward = {
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_local_guides
                    }
                }
            }
            add_to_variable = {
                MKN_army_recon_factor = 0.1
                tooltip = MKN_army_recon_factor_tt
            }
            set_country_flag = MKN_military_stat_local_guides
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_local_guides
                    }
                }
            }
            add_tech_bonus = {
                name = MKN_local_guides
                bonus = 0.5
                uses = 1
                category = recon_tech
            }
            set_country_flag = MKN_military_reward_local_guides
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_field_veterinary
                    }
                }
            }
            add_to_variable = {
                MKN_army_attrition = -0.08
                tooltip = MKN_army_attrition_tt
            }
            set_country_flag = MKN_military_stat_field_veterinary
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_field_veterinary
                    }
                }
            }
            add_tech_bonus = {
                name = MKN_field_veterinary
                bonus = 0.5
                uses = 1
                category = logistics_tech
            }
            set_country_flag = MKN_military_reward_field_veterinary
        }
        set_country_flag = MKN_military_bundle_hidden_supply_bases_focus
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
        custom_effect_tooltip = MKN_military_program_progress_tt
        custom_effect_tooltip = MKN_project_hidden_supply_node_unlock_tt
    }
    ai_will_do = {
        factor = 3
    }
}
```

### Огневая поддержка коммун — `MKN_communal_fire_support_focus`

EN: Communal Fire Support.

Описание RU: Никопольские артели наладят орудия для сопровождения наступающей пехоты.\n\nЕдиные таблицы стрельбы свяжут огонь батарей с планами танковых командиров.

Описание EN: Nikopol workshops will manufacture guns to support advancing infantry.\n\nCommon firing tables will align battery fire with armoured commanders' plans.

Источник: `common/national_focus/MKN.txt:3071`. Стоимость: 10 (70 дней). Координаты: x=46, y=3.

Предпосылки: (Бронепоезда и ремонтные базы [MKN_armored_trains_and_repair_focus]).

Взаимоисключения: нет.

Прямые продолжения: MKN_combined_arms_command_focus.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_communal_fire_support_focus
    icon = GFX_focus_MKN_company_artillery_works
    x = 46
    y = 3
    cost = 10
    available_if_capitulated = no
    prerequisite = {
        focus = MKN_armored_trains_and_repair_focus
    }
    bypass = {
        hidden_trigger = {
            has_country_flag = MKN_military_stat_artillery_artels
            has_country_flag = MKN_military_stat_fire_tables
            has_country_flag = MKN_military_reward_artillery_artels
            has_country_flag = MKN_military_reward_fire_tables
        }
    }
    completion_reward = {
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_artillery_artels
                    }
                }
            }
            add_to_variable = {
                MKN_army_modifier_army_sub_unit_infantry_attack_factor = 0.04
                tooltip = MKN_army_modifier_army_sub_unit_infantry_attack_factor_tt
            }
            set_country_flag = MKN_military_stat_artillery_artels
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_artillery_artels
                    }
                }
            }
            add_tech_bonus = {
                name = MKN_artillery_artels
                bonus = 0.75
                uses = 1
                category = artillery
            }
            set_country_flag = MKN_military_reward_artillery_artels
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_fire_tables
                    }
                }
            }
            add_to_variable = {
                MKN_army_max_planning = 0.05
                tooltip = MKN_army_max_planning_tt
            }
            set_country_flag = MKN_military_stat_fire_tables
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_fire_tables
                    }
                }
            }
            army_experience = 15
            if = {
                limit = {
                    has_dlc = "Arms Against Tyranny"
                }
                mio:MKN_artillery_works_organization = {
                    add_mio_size = 1
                    unlock_mio_trait_tooltip = MKN_artillery_works_organization_specialization_a
                }
            }
            if = {
                limit = {
                    has_dlc = "Arms Against Tyranny"
                }
                mio:MKN_artillery_works_organization = {
                    add_mio_size = 1
                    unlock_mio_trait_tooltip = MKN_artillery_works_organization_specialization_b
                }
            }
            set_country_flag = MKN_military_reward_fire_tables
        }
        set_country_flag = MKN_military_bundle_communal_fire_support_focus
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
        custom_effect_tooltip = MKN_military_program_progress_tt
    }
    ai_will_do = {
        factor = 3
    }
}
```

### Связь вольных колонн — `MKN_free_column_command_focus`

EN: Signals of the Free Columns.

Описание RU: Разведывательные партии расчистят путь основной колонне.\n\nСигнальные команды свяжут волости и выведут резерв на нужный участок.

Описание EN: Small scouting parties will clear the route for the main column.\n\nSignals teams will connect districts and bring reserves to the right sector.

Источник: `common/national_focus/MKN.txt:2446`. Стоимость: 5 (35 дней). Координаты: x=54, y=3.

Предпосылки: (Схроны и базы снабжения [MKN_hidden_supply_bases_focus]).

Взаимоисключения: нет.

Прямые продолжения: MKN_free_army_compact.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_free_column_command_focus
    icon = GFX_focus_generic_forest_brothers
    x = 54
    y = 3
    cost = 5
    available_if_capitulated = no
    prerequisite = {
        focus = MKN_hidden_supply_bases_focus
    }
    bypass = {
        hidden_trigger = {
            has_country_flag = MKN_military_stat_scout_parties
            has_country_flag = MKN_military_stat_militia_signals
            has_country_flag = MKN_military_reward_scout_parties
            has_country_flag = MKN_military_reward_militia_signals
        }
    }
    completion_reward = {
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_scout_parties
                    }
                }
            }
            add_to_variable = {
                MKN_army_army_speed_factor = 0.05
                tooltip = MKN_army_army_speed_factor_tt
            }
            set_country_flag = MKN_military_stat_scout_parties
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_scout_parties
                    }
                }
            }
            army_experience = 15
            set_country_flag = MKN_military_reward_scout_parties
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_militia_signals
                    }
                }
            }
            add_to_variable = {
                MKN_army_land_reinforce_rate = 0.02
                tooltip = MKN_army_land_reinforce_rate_tt
            }
            set_country_flag = MKN_military_stat_militia_signals
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_militia_signals
                    }
                }
            }
            add_tech_bonus = {
                name = MKN_militia_signals
                bonus = 0.5
                uses = 1
                category = signal_company_tech
            }
            set_country_flag = MKN_military_reward_militia_signals
        }
        set_country_flag = MKN_military_bundle_free_column_command_focus
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
        custom_effect_tooltip = MKN_military_program_progress_tt
    }
    ai_will_do = {
        factor = 3
    }
}
```

### Штаб общевойсковых соединений — `MKN_combined_arms_command_focus`

EN: Combined Arms Command.

Описание RU: Радиосвязь позволит подкреплениям вступать в бой по команде штаба.

Описание EN: Radios will bring reinforcements into battle when the staff needs them.

Источник: `common/national_focus/MKN.txt:3173`. Стоимость: 5 (35 дней). Координаты: x=46, y=4.

Предпосылки: (Огневая поддержка коммун [MKN_communal_fire_support_focus]).

Взаимоисключения: нет.

Прямые продолжения: MKN_mechanized_compact.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_combined_arms_command_focus
    icon = GFX_focus_generic_radio_communication
    x = 46
    y = 4
    cost = 5
    available_if_capitulated = no
    prerequisite = {
        focus = MKN_communal_fire_support_focus
    }
    bypass = {
        hidden_trigger = {
            has_country_flag = MKN_military_stat_radio_sections
            has_country_flag = MKN_military_reward_radio_sections
        }
    }
    completion_reward = {
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_radio_sections
                    }
                }
            }
            add_to_variable = {
                MKN_army_land_reinforce_rate = 0.02
                tooltip = MKN_army_land_reinforce_rate_tt
            }
            set_country_flag = MKN_military_stat_radio_sections
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_radio_sections
                    }
                }
            }
            add_tech_bonus = {
                name = MKN_radio_sections
                bonus = 0.5
                uses = 1
                category = signal_company_tech
            }
            set_country_flag = MKN_military_reward_radio_sections
        }
        set_country_flag = MKN_military_bundle_combined_arms_command_focus
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
        custom_effect_tooltip = MKN_military_program_progress_tt
    }
    ai_will_do = {
        factor = 3
    }
}
```

### Армия вольных колонн — `MKN_free_army_compact`

EN: Army of Free Columns.

Описание RU: Вольные колонны готовы к походу; дополнительные службы можно развивать по нуждам фронта. Дополнительные тактики приобретаются отдельно в полевом штабе.

Описание EN: The free columns are ready; additional services can develop according to front-line needs. Further tactics can be purchased separately at the field headquarters.

Источник: `common/national_focus/MKN.txt:2530`. Стоимость: 10 (70 дней). Координаты: x=54, y=4.

Предпосылки: (Связь вольных колонн [MKN_free_column_command_focus]).

Взаимоисключения: нет.

Прямые продолжения: нет.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_free_army_compact
    icon = GFX_focus_generic_freedom_council
    x = 54
    y = 4
    cost = 10
    available_if_capitulated = no
    prerequisite = {
        focus = MKN_free_column_command_focus
    }
    bypass = {
        hidden_trigger = {
            has_country_flag = MKN_military_stat_free_army_compact
            has_country_flag = MKN_military_reward_free_army_compact
            has_country_flag = MKN_military_reward_night_marches
            has_country_flag = MKN_military_reward_militia_junior_leaders
            has_country_flag = MKN_military_reward_hidden_depots
            has_country_flag = MKN_military_reward_militia_engineers
            has_country_flag = MKN_military_reward_militia_hospitals
            has_country_flag = MKN_military_reward_flexible_orders
            has_country_flag = MKN_military_reward_rural_reserve
            has_country_flag = MKN_military_reward_tachanka_tactics
            has_country_flag = MKN_military_reward_steppe_camouflage
            has_country_flag = MKN_military_reward_mobile_rearguard
            has_country_flag = MKN_military_reward_free_column_exercises
        }
    }
    completion_reward = {
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_free_army_compact
                    }
                }
            }
            add_to_variable = {
                MKN_army_modifier_army_sub_unit_cavalry_attack_factor = 0.05
                tooltip = MKN_army_modifier_army_sub_unit_cavalry_attack_factor_tt
            }
            add_to_variable = {
                MKN_army_supply_consumption_factor = -0.05
                tooltip = MKN_army_supply_consumption_factor_tt
            }
            set_country_flag = MKN_military_stat_free_army_compact
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_free_army_compact
                    }
                }
            }
            add_doctrine_cost_reduction = {
                name = MKN_free_army_compact
                cost_reduction = 0.5
                uses = 2
                category = land_doctrine
            }
            if = {
                limit = {
                    has_dlc = "Arms Against Tyranny"
                }
                mio:MKN_rifle_artels_organization = {
                    add_mio_size = 1
                    unlock_mio_trait_tooltip = MKN_rifle_artels_organization_mature
                }
            }
            set_country_flag = MKN_military_reward_free_army_compact
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_night_marches
                    }
                }
            }
            army_experience = 20
            set_country_flag = MKN_military_reward_night_marches
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_militia_junior_leaders
                    }
                }
            }
            add_doctrine_cost_reduction = {
                name = MKN_militia_junior_leaders
                cost_reduction = 0.5
                uses = 1
                category = land_doctrine
            }
            add_mastery_bonus = {
                bonus = 0.1
                days = 240
                track = infantry
                name = MKN_militia_junior_leaders
            }
            set_country_flag = MKN_military_reward_militia_junior_leaders
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_hidden_depots
                    }
                }
            }
            add_equipment_to_stockpile = {
                type = support_equipment_1
                amount = 150
                producer = ROOT
            }
            set_country_flag = MKN_military_reward_hidden_depots
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_militia_engineers
                    }
                }
            }
            add_tech_bonus = {
                name = MKN_militia_engineers
                bonus = 0.5
                uses = 1
                category = engineers_tech
            }
            set_country_flag = MKN_military_reward_militia_engineers
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_militia_hospitals
                    }
                }
            }
            add_tech_bonus = {
                name = MKN_militia_hospitals
                bonus = 0.5
                uses = 1
                category = hospital_tech
            }
            set_country_flag = MKN_military_reward_militia_hospitals
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_flexible_orders
                    }
                }
            }
            add_doctrine_cost_reduction = {
                name = MKN_flexible_orders
                cost_reduction = 0.5
                uses = 1
                category = land_doctrine
            }
            set_country_flag = MKN_military_reward_flexible_orders
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_rural_reserve
                    }
                }
            }
            add_equipment_to_stockpile = {
                type = infantry_equipment_0
                amount = 1000
                producer = ROOT
            }
            set_country_flag = MKN_military_reward_rural_reserve
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_tachanka_tactics
                    }
                }
            }
            army_experience = 20
            set_country_flag = MKN_military_reward_tachanka_tactics
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_steppe_camouflage
                    }
                }
            }
            add_tech_bonus = {
                name = MKN_steppe_camouflage
                bonus = 0.5
                uses = 1
                category = recon_tech
            }
            set_country_flag = MKN_military_reward_steppe_camouflage
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_mobile_rearguard
                    }
                }
            }
            army_experience = 20
            set_country_flag = MKN_military_reward_mobile_rearguard
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_free_column_exercises
                    }
                }
            }
            army_experience = 30
            add_doctrine_cost_reduction = {
                name = MKN_free_column_exercises
                cost_reduction = 0.5
                uses = 1
                category = land_doctrine
            }
            set_country_flag = MKN_military_reward_free_column_exercises
        }
        set_country_flag = MKN_military_bundle_free_army_compact
        add_to_variable = {
            MKN_army_supply_consumption_factor = -0.1
            tooltip = MKN_army_supply_consumption_factor_tt
        }
        add_to_variable = {
            MKN_army_modifier_army_sub_unit_cavalry_attack_factor = 0.05
            tooltip = MKN_army_modifier_army_sub_unit_cavalry_attack_factor_tt
        }
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
        custom_effect_tooltip = MKN_military_program_progress_tt
    }
    ai_will_do = {
        factor = 3
    }
}
```

### Механизированная армия коммун — `MKN_mechanized_compact`

EN: Mechanized Communal Army.

Описание RU: Основные службы готовы: коммуны располагают механизированной армией, а дальнейшие специализации остаются добровольными. Дополнительные тактики приобретаются отдельно в полевом штабе.

Описание EN: The core services are ready: communes now field a mechanized army with optional further specializations. Further tactics can be purchased separately at the field headquarters.

Источник: `common/national_focus/MKN.txt:3230`. Стоимость: 10 (70 дней). Координаты: x=46, y=5.

Предпосылки: (Штаб общевойсковых соединений [MKN_combined_arms_command_focus]).

Взаимоисключения: нет.

Прямые продолжения: нет.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_mechanized_compact
    icon = GFX_focus_generic_mechanized
    x = 46
    y = 5
    cost = 10
    available_if_capitulated = no
    prerequisite = {
        focus = MKN_combined_arms_command_focus
    }
    bypass = {
        hidden_trigger = {
            has_country_flag = MKN_military_stat_mechanized_compact
            has_country_flag = MKN_military_reward_mechanized_compact
            has_country_flag = MKN_military_reward_motorized_infantry
            has_country_flag = MKN_military_reward_bridge_columns
            has_country_flag = MKN_military_reward_fuel_discipline
            has_country_flag = MKN_military_reward_staff_games
            has_country_flag = MKN_military_reward_mobile_medical
            has_country_flag = MKN_military_reward_combined_arms
            has_country_flag = MKN_military_reward_deep_reserves
            has_country_flag = MKN_military_reward_breakthrough_workshops
            has_country_flag = MKN_military_reward_armoured_manoeuvres
        }
    }
    completion_reward = {
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_mechanized_compact
                    }
                }
            }
            add_to_variable = {
                MKN_army_army_armor_attack_factor = 0.06
                tooltip = MKN_army_army_armor_attack_factor_tt
            }
            add_to_variable = {
                MKN_army_army_org_factor = 0.05
                tooltip = MKN_army_army_org_factor_tt
            }
            set_country_flag = MKN_military_stat_mechanized_compact
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_mechanized_compact
                    }
                }
            }
            add_doctrine_cost_reduction = {
                name = MKN_mechanized_compact
                cost_reduction = 0.5
                uses = 2
                category = land_doctrine
            }
            if = {
                limit = {
                    has_dlc = "Arms Against Tyranny"
                }
                mio:MKN_kommunar_organization = {
                    add_mio_size = 1
                    unlock_mio_trait_tooltip = MKN_kommunar_organization_mature
                }
            }
            if = {
                limit = {
                    has_dlc = "Arms Against Tyranny"
                }
                mio:MKN_artillery_works_organization = {
                    add_mio_size = 1
                    unlock_mio_trait_tooltip = MKN_artillery_works_organization_mature
                }
            }
            set_country_flag = MKN_military_reward_mechanized_compact
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_motorized_infantry
                    }
                }
            }
            add_tech_bonus = {
                name = MKN_motorized_infantry
                bonus = 0.75
                uses = 1
                category = cat_mechanized_equipment
            }
            set_country_flag = MKN_military_reward_motorized_infantry
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_bridge_columns
                    }
                }
            }
            add_tech_bonus = {
                name = MKN_bridge_columns
                bonus = 0.5
                uses = 1
                category = engineers_tech
            }
            set_country_flag = MKN_military_reward_bridge_columns
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_fuel_discipline
                    }
                }
            }
            200 = {
                if = {
                    limit = {
                        is_owned_and_controlled_by = ROOT
                    }
                    add_building_construction = {
                        type = fuel_silo
                        level = 1
                        instant_build = yes
                    }
                }
            }
            set_country_flag = MKN_military_reward_fuel_discipline
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_staff_games
                    }
                }
            }
            add_doctrine_cost_reduction = {
                name = MKN_staff_games
                cost_reduction = 0.5
                uses = 2
                category = land_doctrine
            }
            set_country_flag = MKN_military_reward_staff_games
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_mobile_medical
                    }
                }
            }
            add_tech_bonus = {
                name = MKN_mobile_medical
                bonus = 0.5
                uses = 1
                category = hospital_tech
            }
            set_country_flag = MKN_military_reward_mobile_medical
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_combined_arms
                    }
                }
            }
            army_experience = 25
            add_doctrine_cost_reduction = {
                name = MKN_combined_arms
                cost_reduction = 0.5
                uses = 1
                category = land_doctrine
            }
            set_country_flag = MKN_military_reward_combined_arms
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_deep_reserves
                    }
                }
            }
            add_equipment_to_stockpile = {
                type = infantry_equipment_0
                amount = 1000
                producer = ROOT
            }
            set_country_flag = MKN_military_reward_deep_reserves
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_breakthrough_workshops
                    }
                }
            }
            200 = {
                if = {
                    limit = {
                        is_owned_and_controlled_by = ROOT
                    }
                    add_extra_state_shared_building_slots = 1
                    add_building_construction = {
                        type = arms_factory
                        level = 1
                        instant_build = yes
                    }
                }
            }
            set_country_flag = MKN_military_reward_breakthrough_workshops
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_armoured_manoeuvres
                    }
                }
            }
            army_experience = 30
            set_country_flag = MKN_military_reward_armoured_manoeuvres
        }
        set_country_flag = MKN_military_bundle_mechanized_compact
        add_to_variable = {
            MKN_army_breakthrough_factor = 0.1
            tooltip = MKN_army_breakthrough_factor_tt
        }
        add_to_variable = {
            MKN_army_army_armor_attack_factor = 0.05
            tooltip = MKN_army_army_armor_attack_factor_tt
        }
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
        custom_effect_tooltip = MKN_military_program_progress_tt
    }
    ai_will_do = {
        factor = 3
    }
}
```

### Памяти атаманши Маруси — `MKN_memory_of_atamansha_marusya`

EN: In Memory of Atamansha Marusya.

Описание RU: Маруся Никифорова превратила дерзость и инициативу в оружие повстанцев. Сохраним её наследие в постоянной подготовке к уличным боям, прорывам и быстрому восстановлению сил.

Описание EN: Marusya Nikiforova made audacity and initiative a weapon of the insurgency. Preserve her legacy through permanent training in street fighting, breakthrough tactics and rapid recovery.

Источник: `common/national_focus/MKN.txt:6498`. Стоимость: 5 (35 дней). Координаты: x=50, y=5.

Предпосылки: нет нарисованной предпосылки; см. available.

Взаимоисключения: нет.

Прямые продолжения: MKN_the_black_guard_battalions.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_memory_of_atamansha_marusya
    cost = 5
    available_if_capitulated = no
    icon = GFX_focus_generic_soldier_salute
    completion_reward = {
        add_ideas = MKN_marusyas_legacy
    }
    ai_will_do = {
        factor = 1
    }
    x = 50
    y = 5
    available = {
        has_completed_focus = MKN_steppe_general_staff
    }
}
```

### Батальоны Чёрной гвардии — `MKN_the_black_guard_battalions`

EN: The Black Guard Battalions.

Описание RU: Сформируем в Гуляйполе два ветеранских штурмовых отряда. В каждом — девять пехотных и два артиллерийских батальона, сапёры, разведка и полевой госпиталь. Элитный шаблон нельзя редактировать или набирать вручную. Гуляйполе должно принадлежать нам и быть под нашим контролем; необходимо исследовать все три технологии рот поддержки.

Описание EN: Form two veteran shock detachments in Huliaipole. Each has nine infantry and two artillery battalions, with engineers, reconnaissance and a field hospital. Their elite template cannot be edited or recruited manually. Huliaipole must be ours and under our control, and all three support technologies must be researched.

Источник: `common/national_focus/MKN.txt:7979`. Стоимость: 5 (35 дней). Координаты: x=50, y=6.

Предпосылки: (Памяти атаманши Маруси [MKN_memory_of_atamansha_marusya]).

Взаимоисключения: нет.

Прямые продолжения: нет.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_the_black_guard_battalions
    cost = 5
    available_if_capitulated = no
    cancel_if_invalid = yes
    continue_if_invalid = no
    icon = GFX_focus_generic_special_forces
    prerequisite = {
        focus = MKN_memory_of_atamansha_marusya
    }
    available = {
        1082 = {
            is_owned_and_controlled_by = ROOT
        }
        has_tech = tech_engineers
        has_tech = tech_recon
        has_tech = tech_field_hospital
    }
    completion_reward = {
        MKN_raise_black_guard_battalions = yes
    }
    ai_will_do = {
        factor = 1
    }
    x = 50
    y = 6
}
```

## Авиация

### Степные соколы и школы — `MKN_steppe_hawks_and_schools`

EN: Steppe Hawks and Flying Schools.

Описание RU: Создадим воздушную службу коммун с общей диспетчерской и правилами полётов.\n\nПолевые полосы приблизят авиацию к войскам и сократят бесполезные перелёты.\n\nШкола лётчиков даст общую подготовку перед выбором боевой специализации.\n\nОткрывает одноразовые тактики полевого штаба за опыт и командный ресурс.

Описание EN: Establish a communal air service with shared flight control and operating rules.\n\nForward strips will bring aircraft closer to troops and reduce ferry flights.\n\nThe pilot school will provide common training before combat specialization.\n\nUnlocks one-time field headquarters tactics purchased with experience and command power.

Источник: `common/national_focus/MKN.txt:3478`. Стоимость: 10 (70 дней). Координаты: x=66, y=0.

Предпосылки: нет нарисованной предпосылки; см. available.

Взаимоисключения: нет.

Прямые продолжения: MKN_interceptor_cooperatives, MKN_flying_artillery_focus.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_steppe_hawks_and_schools
    icon = GFX_focus_generic_swooping_falcon
    x = 66
    y = 0
    cost = 10
    available_if_capitulated = no
    bypass = {
        hidden_trigger = {
            has_country_flag = MKN_military_stat_steppe_hawks
            has_country_flag = MKN_military_stat_village_airfields
            has_country_flag = MKN_military_stat_gulyaipole_pilot_school
            has_country_flag = MKN_military_reward_steppe_hawks
            has_country_flag = MKN_military_reward_village_airfields
            has_country_flag = MKN_military_reward_gulyaipole_pilot_school
        }
    }
    completion_reward = {
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_steppe_hawks
                    }
                }
            }
            add_to_variable = {
                MKN_air_air_mission_efficiency = 0.03
                tooltip = MKN_air_air_mission_efficiency_tt
            }
            set_country_flag = MKN_military_stat_steppe_hawks
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_steppe_hawks
                    }
                }
            }
            air_experience = 20
            set_country_flag = MKN_military_reward_steppe_hawks
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_village_airfields
                    }
                }
            }
            add_to_variable = {
                MKN_air_air_range_factor = 0.05
                tooltip = MKN_air_air_range_factor_tt
            }
            set_country_flag = MKN_military_stat_village_airfields
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_village_airfields
                    }
                }
            }
            226 = {
                if = {
                    limit = {
                        is_owned_and_controlled_by = ROOT
                    }
                    add_building_construction = {
                        type = air_base
                        level = 2
                        instant_build = yes
                    }
                }
            }
            set_country_flag = MKN_military_reward_village_airfields
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_gulyaipole_pilot_school
                    }
                }
            }
            add_to_variable = {
                MKN_air_air_accidents_factor = -0.05
                tooltip = MKN_air_air_accidents_factor_tt
            }
            set_country_flag = MKN_military_stat_gulyaipole_pilot_school
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_gulyaipole_pilot_school
                    }
                }
            }
            air_experience = 25
            add_doctrine_cost_reduction = {
                name = MKN_gulyaipole_pilot_school
                cost_reduction = 0.35
                uses = 2
                category = air_doctrine
            }
            set_country_flag = MKN_military_reward_gulyaipole_pilot_school
        }
        set_country_flag = MKN_military_bundle_steppe_hawks_and_schools
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
        custom_effect_tooltip = MKN_air_hq_unlock_tt
    }
    ai_will_do = {
        factor = 3
    }
}
```

### Авиакооперативы перехвата — `MKN_interceptor_cooperatives`

EN: Interceptor Cooperatives.

Описание RU: Истребители станут щитом коммун; ударная авиация останется второстепенной.\n\nЛёгкие планеры артели «Степной сокол» приспособят для манёвренного перехвата.\n\nЛучшие инструкторы покажут молодым пилотам приёмы боя в паре.\n\nВедущий прикрывает ведомого: одиночный герой уступит место слаженной паре.

Описание EN: Fighters will shield the communes while strike aviation remains secondary.\n\nSteppe Falcon cooperatives will adapt light airframes for agile interception.\n\nVeteran instructors will teach new pilots how to fight in pairs.\n\nLeaders and wingmen will replace lone heroics with coordinated pairs.

Источник: `common/national_focus/MKN.txt:3598`. Стоимость: 10 (70 дней). Координаты: x=62, y=1.

Предпосылки: (Степные соколы и школы [MKN_steppe_hawks_and_schools]).

Взаимоисключения: MKN_flying_artillery_focus.

Прямые продолжения: MKN_communal_aa_defense_focus.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_interceptor_cooperatives
    icon = GFX_goal_generic_air_fighter
    x = 62
    y = 1
    cost = 10
    available_if_capitulated = no
    prerequisite = {
        focus = MKN_steppe_hawks_and_schools
    }
    mutually_exclusive = {
        focus = MKN_flying_artillery_focus
    }
    bypass = {
        hidden_trigger = {
            has_country_flag = MKN_military_stat_black_swarm
            has_country_flag = MKN_military_stat_aircraft_artels
            has_country_flag = MKN_military_stat_fighter_instructors
            has_country_flag = MKN_military_stat_interceptor_pairs
            has_country_flag = MKN_military_reward_black_swarm
            has_country_flag = MKN_military_reward_aircraft_artels
            has_country_flag = MKN_military_reward_fighter_instructors
            has_country_flag = MKN_military_reward_interceptor_pairs
        }
    }
    completion_reward = {
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_black_swarm
                    }
                }
            }
            add_to_variable = {
                MKN_air_air_intercept_efficiency = 0.1
                tooltip = MKN_air_air_intercept_efficiency_tt
            }
            set_country_flag = MKN_military_stat_black_swarm
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_black_swarm
                    }
                }
            }
            add_tech_bonus = {
                name = MKN_black_swarm
                bonus = 0.75
                uses = 1
                category = light_fighter
            }
            set_country_flag = MKN_military_reward_black_swarm
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_aircraft_artels
                    }
                }
            }
            add_to_variable = {
                MKN_air_air_agility_factor = 0.04
                tooltip = MKN_air_air_agility_factor_tt
            }
            set_country_flag = MKN_military_stat_aircraft_artels
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_aircraft_artels
                    }
                }
            }
            add_tech_bonus = {
                name = MKN_aircraft_artels
                bonus = 0.75
                uses = 1
                category = light_air
            }
            if = {
                limit = {
                    has_dlc = "Arms Against Tyranny"
                }
                mio:MKN_air_artels_organization = {
                    add_mio_size = 1
                }
            }
            set_country_flag = MKN_military_reward_aircraft_artels
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_fighter_instructors
                    }
                }
            }
            add_to_variable = {
                MKN_air_air_ace_generation_chance_factor = 0.15
                tooltip = MKN_air_air_ace_generation_chance_factor_tt
            }
            set_country_flag = MKN_military_stat_fighter_instructors
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_fighter_instructors
                    }
                }
            }
            air_experience = 20
            add_ace = {
                name = Stepan
                surname = Koval
                callsign = Sokil
                type = fighter_genius
            }
            set_country_flag = MKN_military_reward_fighter_instructors
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_interceptor_pairs
                    }
                }
            }
            add_to_variable = {
                MKN_air_air_agility_factor = 0.04
                tooltip = MKN_air_air_agility_factor_tt
            }
            set_country_flag = MKN_military_stat_interceptor_pairs
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_interceptor_pairs
                    }
                }
            }
            air_experience = 20
            add_doctrine_cost_reduction = {
                name = MKN_interceptor_pairs
                cost_reduction = 0.5
                uses = 1
                category = air_doctrine
            }
            if = {
                limit = {
                    has_dlc = "Arms Against Tyranny"
                }
                mio:MKN_air_artels_organization = {
                    add_mio_size = 1
                    unlock_mio_trait_tooltip = MKN_air_artels_organization_specialization_a
                }
            }
            if = {
                limit = {
                    has_dlc = "Arms Against Tyranny"
                }
                mio:MKN_air_artels_organization = {
                    add_mio_size = 1
                    unlock_mio_trait_tooltip = MKN_air_artels_organization_specialization_b
                }
            }
            set_country_flag = MKN_military_reward_interceptor_pairs
        }
        set_country_flag = MKN_military_bundle_interceptor_cooperatives
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
        custom_effect_tooltip = MKN_military_program_progress_tt
    }
    ai_will_do = {
        factor = 3
    }
}
```

### Летающая артиллерия — `MKN_flying_artillery_focus`

EN: Flying Artillery.

Описание RU: Авиация станет летающей артиллерией для вольных колонн.\n\n«Днепровское крыло» приспособит лёгкие самолёты для ударов по наземным целям.\n\nТяжёлое вооружение штурмовиков поможет разрушать узлы сопротивления.\n\nНа полигонах экипажи научатся поражать цель рядом со своими войсками.

Описание EN: Aviation will become flying artillery for the free columns.\n\nDnipro Wing cooperatives will adapt light aircraft for ground attack.\n\nHeavier aircraft armament will break enemy strongpoints.\n\nRange training will teach crews to strike targets close to friendly troops.

Источник: `common/national_focus/MKN.txt:4258`. Стоимость: 10 (70 дней). Координаты: x=70, y=1.

Предпосылки: (Степные соколы и школы [MKN_steppe_hawks_and_schools]).

Взаимоисключения: MKN_interceptor_cooperatives.

Прямые продолжения: MKN_forward_airstrips_focus.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_flying_artillery_focus
    icon = GFX_focus_generic_cas_aircraft
    x = 70
    y = 1
    cost = 10
    available_if_capitulated = no
    prerequisite = {
        focus = MKN_steppe_hawks_and_schools
    }
    mutually_exclusive = {
        focus = MKN_interceptor_cooperatives
    }
    bypass = {
        hidden_trigger = {
            has_country_flag = MKN_military_stat_close_support_program
            has_country_flag = MKN_military_stat_attack_air_artels
            has_country_flag = MKN_military_stat_flying_artillery
            has_country_flag = MKN_military_stat_bombing_ranges
            has_country_flag = MKN_military_reward_close_support_program
            has_country_flag = MKN_military_reward_attack_air_artels
            has_country_flag = MKN_military_reward_flying_artillery
            has_country_flag = MKN_military_reward_bombing_ranges
        }
    }
    completion_reward = {
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_close_support_program
                    }
                }
            }
            add_to_variable = {
                MKN_air_air_cas_efficiency = 0.1
                tooltip = MKN_air_air_cas_efficiency_tt
            }
            set_country_flag = MKN_military_stat_close_support_program
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_close_support_program
                    }
                }
            }
            add_tech_bonus = {
                name = MKN_close_support_program
                bonus = 0.75
                uses = 1
                category = cas_bomber
            }
            set_country_flag = MKN_military_reward_close_support_program
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_attack_air_artels
                    }
                }
            }
            add_to_variable = {
                MKN_air_air_attack_factor = 0.04
                tooltip = MKN_air_air_attack_factor_tt
            }
            set_country_flag = MKN_military_stat_attack_air_artels
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_attack_air_artels
                    }
                }
            }
            add_tech_bonus = {
                name = MKN_attack_air_artels
                bonus = 0.75
                uses = 1
                category = light_air
            }
            if = {
                limit = {
                    has_dlc = "Arms Against Tyranny"
                }
                mio:MKN_attack_air_artels_organization = {
                    add_mio_size = 1
                }
            }
            set_country_flag = MKN_military_reward_attack_air_artels
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_flying_artillery
                    }
                }
            }
            add_to_variable = {
                MKN_air_air_cas_efficiency = 0.05
                tooltip = MKN_air_air_cas_efficiency_tt
            }
            set_country_flag = MKN_military_stat_flying_artillery
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_flying_artillery
                    }
                }
            }
            if = {
                limit = {
                    has_dlc = "By Blood Alone"
                }
                add_tech_bonus = {
                    name = MKN_flying_artillery
                    bonus = 0.75
                    uses = 1
                    category = cat_air_bombs
                }
            }
            else = {
                add_tech_bonus = {
                    name = MKN_flying_artillery
                    bonus = 0.75
                    uses = 1
                    category = cas_bomber
                }
            }
            if = {
                limit = {
                    has_dlc = "Arms Against Tyranny"
                }
                mio:MKN_attack_air_artels_organization = {
                    add_mio_size = 1
                    unlock_mio_trait_tooltip = MKN_attack_air_artels_organization_specialization_a
                }
            }
            if = {
                limit = {
                    has_dlc = "Arms Against Tyranny"
                }
                mio:MKN_attack_air_artels_organization = {
                    add_mio_size = 1
                    unlock_mio_trait_tooltip = MKN_attack_air_artels_organization_specialization_b
                }
            }
            set_country_flag = MKN_military_reward_flying_artillery
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_bombing_ranges
                    }
                }
            }
            add_to_variable = {
                MKN_air_air_mission_efficiency = 0.04
                tooltip = MKN_air_air_mission_efficiency_tt
            }
            set_country_flag = MKN_military_stat_bombing_ranges
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_bombing_ranges
                    }
                }
            }
            air_experience = 20
            add_doctrine_cost_reduction = {
                name = MKN_bombing_ranges
                cost_reduction = 0.5
                uses = 1
                category = air_doctrine
            }
            set_country_flag = MKN_military_reward_bombing_ranges
        }
        set_country_flag = MKN_military_bundle_flying_artillery_focus
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
        custom_effect_tooltip = MKN_military_program_progress_tt
    }
    ai_will_do = {
        factor = 3
    }
}
```

### Эшелонированное ПВО коммун — `MKN_communal_aa_defense_focus`

EN: Layered Communal Air Defense.

Описание RU: Наблюдатели передадут предупреждение до появления бомбардировщиков над городами.\n\nЕдиная тревога поднимет нужные звенья вместо всей авиации сразу.

Описание EN: Observers will report bombers before they reach the towns.\n\nA shared warning system will scramble the right flights without exhausting the whole air force.

Источник: `common/national_focus/MKN.txt:3782`. Стоимость: 5 (35 дней). Координаты: x=62, y=2.

Предпосылки: (Авиакооперативы перехвата [MKN_interceptor_cooperatives]).

Взаимоисключения: нет.

Прямые продолжения: MKN_airframe_standardization_focus.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_communal_aa_defense_focus
    icon = GFX_focus_generic_air_defense
    x = 62
    y = 2
    cost = 5
    available_if_capitulated = no
    prerequisite = {
        focus = MKN_interceptor_cooperatives
    }
    bypass = {
        hidden_trigger = {
            has_country_flag = MKN_military_stat_observation_posts
            has_country_flag = MKN_military_stat_air_warning
            has_country_flag = MKN_military_reward_observation_posts
            has_country_flag = MKN_military_reward_air_warning
        }
    }
    completion_reward = {
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_observation_posts
                    }
                }
            }
            add_to_variable = {
                MKN_air_air_interception_detect_factor = 0.1
                tooltip = MKN_air_air_interception_detect_factor_tt
            }
            set_country_flag = MKN_military_stat_observation_posts
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_observation_posts
                    }
                }
            }
            add_tech_bonus = {
                name = MKN_observation_posts
                bonus = 0.5
                uses = 1
                category = radar_tech
            }
            set_country_flag = MKN_military_reward_observation_posts
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_air_warning
                    }
                }
            }
            add_to_variable = {
                MKN_air_air_intercept_efficiency = 0.05
                tooltip = MKN_air_air_intercept_efficiency_tt
            }
            set_country_flag = MKN_military_stat_air_warning
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_air_warning
                    }
                }
            }
            add_tech_bonus = {
                name = MKN_air_warning
                bonus = 0.5
                uses = 1
                category = electronics
            }
            set_country_flag = MKN_military_reward_air_warning
        }
        set_country_flag = MKN_military_bundle_communal_aa_defense_focus
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
        custom_effect_tooltip = MKN_military_program_progress_tt
        custom_effect_tooltip = MKN_project_observation_posts_unlock_tt
        custom_effect_tooltip = MKN_project_aa_batteries_unlock_tt
    }
    ai_will_do = {
        factor = 3
    }
}
```

### Передовые посадочные полосы — `MKN_forward_airstrips_focus`

EN: Forward Airstrips.

Описание RU: Передовые полосы сократят время между запросом поддержки и ударом.\n\nСвязные передадут запросы пехоты прямо на аэродром.

Описание EN: Forward strips will shorten the delay between a support request and the strike.\n\nLiaison teams will carry infantry requests directly to the airfields.

Источник: `common/national_focus/MKN.txt:4454`. Стоимость: 5 (35 дней). Координаты: x=70, y=2.

Предпосылки: (Летающая артиллерия [MKN_flying_artillery_focus]).

Взаимоисключения: нет.

Прямые продолжения: MKN_air_ground_coordination_focus.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_forward_airstrips_focus
    icon = GFX_focus_generic_air_bases
    x = 70
    y = 2
    cost = 5
    available_if_capitulated = no
    prerequisite = {
        focus = MKN_flying_artillery_focus
    }
    bypass = {
        hidden_trigger = {
            has_country_flag = MKN_military_stat_forward_airstrips
            has_country_flag = MKN_military_stat_air_ground_liaisons
            has_country_flag = MKN_military_reward_forward_airstrips
            has_country_flag = MKN_military_reward_air_ground_liaisons
        }
    }
    completion_reward = {
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_forward_airstrips
                    }
                }
            }
            add_to_variable = {
                MKN_air_air_range_factor = 0.08
                tooltip = MKN_air_air_range_factor_tt
            }
            set_country_flag = MKN_military_stat_forward_airstrips
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_forward_airstrips
                    }
                }
            }
            226 = {
                if = {
                    limit = {
                        is_owned_and_controlled_by = ROOT
                    }
                    add_building_construction = {
                        type = air_base
                        level = 2
                        instant_build = yes
                    }
                }
            }
            set_country_flag = MKN_military_reward_forward_airstrips
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_air_ground_liaisons
                    }
                }
            }
            add_to_variable = {
                MKN_air_air_cas_efficiency = 0.05
                tooltip = MKN_air_air_cas_efficiency_tt
            }
            set_country_flag = MKN_military_stat_air_ground_liaisons
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_air_ground_liaisons
                    }
                }
            }
            air_experience = 20
            set_country_flag = MKN_military_reward_air_ground_liaisons
        }
        set_country_flag = MKN_military_bundle_forward_airstrips_focus
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
        custom_effect_tooltip = MKN_military_program_progress_tt
        custom_effect_tooltip = MKN_project_forward_airstrip_unlock_tt
    }
    ai_will_do = {
        factor = 3
    }
}
```

### Единый стандарт авиамастерских — `MKN_airframe_standardization_focus`

EN: Air Workshop Standards.

Описание RU: Радиомаяки помогут перехватчикам вернуться даже в плохую погоду.\n\nСерийная оснастка обеспечит точную сборку и вооружение истребителей.\n\nЭвакуационные бригады вернут повреждённые машины и спасут ремонтный фонд.

Описание EN: Radio beacons will guide interceptors home in poor weather.\n\nProduction jigs will improve fighter assembly and armament.\n\nRecovery teams will retrieve damaged aircraft for repair.

Источник: `common/national_focus/MKN.txt:3873`. Стоимость: 10 (70 дней). Координаты: x=62, y=3.

Предпосылки: (Эшелонированное ПВО коммун [MKN_communal_aa_defense_focus]).

Взаимоисключения: нет.

Прямые продолжения: MKN_free_sky_compact.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_airframe_standardization_focus
    icon = GFX_focus_generic_phone
    x = 62
    y = 3
    cost = 10
    available_if_capitulated = no
    prerequisite = {
        focus = MKN_communal_aa_defense_focus
    }
    bypass = {
        hidden_trigger = {
            has_country_flag = MKN_military_stat_radio_beacons
            has_country_flag = MKN_military_stat_airframe_jigs
            has_country_flag = MKN_military_stat_aircraft_recovery
            has_country_flag = MKN_military_reward_radio_beacons
            has_country_flag = MKN_military_reward_airframe_jigs
            has_country_flag = MKN_military_reward_aircraft_recovery
        }
    }
    completion_reward = {
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_radio_beacons
                    }
                }
            }
            add_to_variable = {
                MKN_air_air_mission_efficiency = 0.05
                tooltip = MKN_air_air_mission_efficiency_tt
            }
            set_country_flag = MKN_military_stat_radio_beacons
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_radio_beacons
                    }
                }
            }
            add_tech_bonus = {
                name = MKN_radio_beacons
                bonus = 0.5
                uses = 1
                category = signal_company_tech
            }
            set_country_flag = MKN_military_reward_radio_beacons
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_airframe_jigs
                    }
                }
            }
            add_to_variable = {
                MKN_air_air_attack_factor = 0.04
                tooltip = MKN_air_air_attack_factor_tt
            }
            set_country_flag = MKN_military_stat_airframe_jigs
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_airframe_jigs
                    }
                }
            }
            200 = {
                if = {
                    limit = {
                        is_owned_and_controlled_by = ROOT
                    }
                    add_extra_state_shared_building_slots = 1
                    add_building_construction = {
                        type = arms_factory
                        level = 1
                        instant_build = yes
                    }
                }
            }
            set_country_flag = MKN_military_reward_airframe_jigs
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_aircraft_recovery
                    }
                }
            }
            add_to_variable = {
                MKN_air_air_accidents_factor = -0.05
                tooltip = MKN_air_air_accidents_factor_tt
            }
            set_country_flag = MKN_military_stat_aircraft_recovery
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_aircraft_recovery
                    }
                }
            }
            add_tech_bonus = {
                name = MKN_aircraft_recovery
                bonus = 0.5
                uses = 1
                category = maintenance_company_tech
            }
            set_country_flag = MKN_military_reward_aircraft_recovery
        }
        set_country_flag = MKN_military_bundle_airframe_standardization_focus
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
        custom_effect_tooltip = MKN_military_program_progress_tt
    }
    ai_will_do = {
        factor = 3
    }
}
```

### Карта для вольных колонн — `MKN_air_ground_coordination_focus`

EN: Maps for the Free Columns.

Описание RU: Карты, фотосъёмка и единая сетка координат избавят экипажи от поиска цели вслепую.\n\nДымовые сигналы и условные полотнища обозначат передний край.

Описание EN: Maps, photographs and shared coordinates will prevent blind target searches.\n\nSmoke signals and recognition panels will mark the front line.

Источник: `common/national_focus/MKN.txt:4545`. Стоимость: 5 (35 дней). Координаты: x=70, y=3.

Предпосылки: (Передовые посадочные полосы [MKN_forward_airstrips_focus]).

Взаимоисключения: нет.

Прямые продолжения: MKN_cas_workshop_network_focus.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_air_ground_coordination_focus
    icon = GFX_focus_generic_advanced_military_studies
    x = 70
    y = 3
    cost = 5
    available_if_capitulated = no
    prerequisite = {
        focus = MKN_forward_airstrips_focus
    }
    bypass = {
        hidden_trigger = {
            has_country_flag = MKN_military_stat_air_map_bureau
            has_country_flag = MKN_military_stat_target_markers
            has_country_flag = MKN_military_reward_air_map_bureau
            has_country_flag = MKN_military_reward_target_markers
        }
    }
    completion_reward = {
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_air_map_bureau
                    }
                }
            }
            add_to_variable = {
                MKN_air_air_mission_efficiency = 0.04
                tooltip = MKN_air_air_mission_efficiency_tt
            }
            set_country_flag = MKN_military_stat_air_map_bureau
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_air_map_bureau
                    }
                }
            }
            if = {
                limit = {
                    has_dlc = "By Blood Alone"
                }
                add_tech_bonus = {
                    name = MKN_air_map_bureau
                    bonus = 0.5
                    uses = 1
                    category = cat_scout_plane
                }
            }
            else = {
                add_tech_bonus = {
                    name = MKN_air_map_bureau
                    bonus = 0.5
                    uses = 1
                    category = tactical_bomber
                }
            }
            set_country_flag = MKN_military_reward_air_map_bureau
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_target_markers
                    }
                }
            }
            add_to_variable = {
                MKN_air_air_cas_efficiency = 0.05
                tooltip = MKN_air_air_cas_efficiency_tt
            }
            set_country_flag = MKN_military_stat_target_markers
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_target_markers
                    }
                }
            }
            air_experience = 15
            set_country_flag = MKN_military_reward_target_markers
        }
        set_country_flag = MKN_military_bundle_air_ground_coordination_focus
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
        custom_effect_tooltip = MKN_military_program_progress_tt
    }
    ai_will_do = {
        factor = 3
    }
}
```

### Небо под защитой коммун — `MKN_free_sky_compact`

EN: Communal Sky Defence.

Описание RU: Основная система перехвата готова; ночные и радиолокационные службы останутся дополнительными. Дополнительные тактики приобретаются отдельно в полевом штабе.

Описание EN: The core interception system is ready, with night and radar services available as extensions. Further tactics can be purchased separately at the field headquarters.

Источник: `common/national_focus/MKN.txt:4001`. Стоимость: 10 (70 дней). Координаты: x=62, y=4.

Предпосылки: (Единый стандарт авиамастерских [MKN_airframe_standardization_focus]).

Взаимоисключения: нет.

Прямые продолжения: нет.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_free_sky_compact
    icon = GFX_goal_generic_build_airforce
    x = 62
    y = 4
    cost = 10
    available_if_capitulated = no
    prerequisite = {
        focus = MKN_airframe_standardization_focus
    }
    bypass = {
        hidden_trigger = {
            has_country_flag = MKN_military_stat_free_sky_compact
            has_country_flag = MKN_military_reward_free_sky_compact
            has_country_flag = MKN_military_reward_air_dispersal
            has_country_flag = MKN_military_reward_fighter_patrols
            has_country_flag = MKN_military_reward_air_radar_school
            has_country_flag = MKN_military_reward_night_interceptors
            has_country_flag = MKN_military_reward_aircraft_spares
            has_country_flag = MKN_military_reward_fighter_conversion
            has_country_flag = MKN_military_reward_air_rescue
            has_country_flag = MKN_military_reward_fighter_controllers
            has_country_flag = MKN_military_reward_air_home_defence
            has_country_flag = MKN_military_reward_sky_watch_exercises
        }
    }
    completion_reward = {
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_free_sky_compact
                    }
                }
            }
            add_to_variable = {
                MKN_air_air_agility_factor = 0.04
                tooltip = MKN_air_air_agility_factor_tt
            }
            add_to_variable = {
                MKN_air_air_intercept_efficiency = 0.1
                tooltip = MKN_air_air_intercept_efficiency_tt
            }
            set_country_flag = MKN_military_stat_free_sky_compact
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_free_sky_compact
                    }
                }
            }
            add_doctrine_cost_reduction = {
                name = MKN_free_sky_compact
                cost_reduction = 0.5
                uses = 2
                category = air_doctrine
            }
            if = {
                limit = {
                    has_dlc = "Arms Against Tyranny"
                }
                mio:MKN_air_artels_organization = {
                    add_mio_size = 1
                    unlock_mio_trait_tooltip = MKN_air_artels_organization_mature
                }
            }
            set_country_flag = MKN_military_reward_free_sky_compact
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_air_dispersal
                    }
                }
            }
            226 = {
                if = {
                    limit = {
                        is_owned_and_controlled_by = ROOT
                    }
                    add_building_construction = {
                        type = air_base
                        level = 2
                        instant_build = yes
                    }
                }
            }
            set_country_flag = MKN_military_reward_air_dispersal
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_fighter_patrols
                    }
                }
            }
            air_experience = 15
            set_country_flag = MKN_military_reward_fighter_patrols
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_air_radar_school
                    }
                }
            }
            add_tech_bonus = {
                name = MKN_air_radar_school
                bonus = 0.75
                uses = 1
                category = radar_tech
            }
            set_country_flag = MKN_military_reward_air_radar_school
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_night_interceptors
                    }
                }
            }
            air_experience = 20
            set_country_flag = MKN_military_reward_night_interceptors
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_aircraft_spares
                    }
                }
            }
            if = {
                limit = {
                    has_dlc = "By Blood Alone"
                }
                add_tech_bonus = {
                    name = MKN_aircraft_spares
                    bonus = 0.5
                    uses = 1
                    category = plane_modules_tech
                }
            }
            else = {
                add_tech_bonus = {
                    name = MKN_aircraft_spares
                    bonus = 0.5
                    uses = 1
                    category = light_air
                }
            }
            set_country_flag = MKN_military_reward_aircraft_spares
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_fighter_conversion
                    }
                }
            }
            add_tech_bonus = {
                name = MKN_fighter_conversion
                bonus = 0.75
                uses = 1
                category = light_fighter
            }
            add_mastery_bonus = {
                bonus = 0.1
                days = 240
                track = fighter_aircraft
                name = MKN_fighter_conversion
            }
            set_country_flag = MKN_military_reward_fighter_conversion
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_air_rescue
                    }
                }
            }
            air_experience = 15
            set_country_flag = MKN_military_reward_air_rescue
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_fighter_controllers
                    }
                }
            }
            add_doctrine_cost_reduction = {
                name = MKN_fighter_controllers
                cost_reduction = 0.5
                uses = 1
                category = air_doctrine
            }
            set_country_flag = MKN_military_reward_fighter_controllers
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_air_home_defence
                    }
                }
            }
            200 = {
                if = {
                    limit = {
                        is_owned_and_controlled_by = ROOT
                    }
                    add_building_construction = {
                        type = anti_air
                        level = 2
                        instant_build = yes
                    }
                }
            }
            set_country_flag = MKN_military_reward_air_home_defence
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_sky_watch_exercises
                    }
                }
            }
            air_experience = 30
            add_doctrine_cost_reduction = {
                name = MKN_sky_watch_exercises
                cost_reduction = 0.5
                uses = 1
                category = air_doctrine
            }
            set_country_flag = MKN_military_reward_sky_watch_exercises
        }
        set_country_flag = MKN_military_bundle_free_sky_compact
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
        custom_effect_tooltip = MKN_military_program_progress_tt
    }
    ai_will_do = {
        factor = 3
    }
}
```

### Сеть штурмовых авиамастерских — `MKN_cas_workshop_network_focus`

EN: Attack Aircraft Workshop Network.

Описание RU: Прифронтовые мастерские восстановят повреждения от наземного огня.

Описание EN: Front-line workshops will repair damage inflicted by ground fire.

Источник: `common/national_focus/MKN.txt:4642`. Стоимость: 5 (35 дней). Координаты: x=70, y=4.

Предпосылки: (Карта для вольных колонн [MKN_air_ground_coordination_focus]).

Взаимоисключения: нет.

Прямые продолжения: MKN_air_support_compact.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_cas_workshop_network_focus
    icon = GFX_focus_generic_industrial_experts
    x = 70
    y = 4
    cost = 5
    available_if_capitulated = no
    prerequisite = {
        focus = MKN_air_ground_coordination_focus
    }
    bypass = {
        hidden_trigger = {
            has_country_flag = MKN_military_stat_cas_maintenance
            has_country_flag = MKN_military_reward_cas_maintenance
        }
    }
    completion_reward = {
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_cas_maintenance
                    }
                }
            }
            add_to_variable = {
                MKN_air_air_accidents_factor = -0.08
                tooltip = MKN_air_air_accidents_factor_tt
            }
            set_country_flag = MKN_military_stat_cas_maintenance
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_cas_maintenance
                    }
                }
            }
            226 = {
                if = {
                    limit = {
                        is_owned_and_controlled_by = ROOT
                    }
                    add_extra_state_shared_building_slots = 1
                    add_building_construction = {
                        type = arms_factory
                        level = 1
                        instant_build = yes
                    }
                }
            }
            set_country_flag = MKN_military_reward_cas_maintenance
        }
        set_country_flag = MKN_military_bundle_cas_workshop_network_focus
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
        custom_effect_tooltip = MKN_military_program_progress_tt
    }
    ai_will_do = {
        factor = 3
    }
}
```

### Крылья над вольными колоннами — `MKN_air_support_compact`

EN: Wings over Free Columns.

Описание RU: Колонны получили воздушную поддержку; дальние и морские операции можно развивать отдельно. Дополнительные тактики приобретаются отдельно в полевом штабе.

Описание EN: Columns now have air support, with long-range and maritime operations available as extensions. Further tactics can be purchased separately at the field headquarters.

Источник: `common/national_focus/MKN.txt:4706`. Стоимость: 10 (70 дней). Координаты: x=70, y=5.

Предпосылки: (Сеть штурмовых авиамастерских [MKN_cas_workshop_network_focus]).

Взаимоисключения: нет.

Прямые продолжения: нет.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_air_support_compact
    icon = GFX_goal_generic_CAS
    x = 70
    y = 5
    cost = 10
    available_if_capitulated = no
    prerequisite = {
        focus = MKN_cas_workshop_network_focus
    }
    bypass = {
        hidden_trigger = {
            has_country_flag = MKN_military_stat_air_support_compact
            has_country_flag = MKN_military_reward_air_support_compact
            has_country_flag = MKN_military_reward_airfield_fuel
            has_country_flag = MKN_military_reward_tactical_recon
            has_country_flag = MKN_military_reward_bomber_navigation
            has_country_flag = MKN_military_reward_air_supply_lift
            has_country_flag = MKN_military_reward_air_coastal_support
            has_country_flag = MKN_military_reward_cas_replacement_crews
            has_country_flag = MKN_military_reward_joint_target_planning
            has_country_flag = MKN_military_reward_air_weather_service
            has_country_flag = MKN_military_reward_attack_wing_rotations
            has_country_flag = MKN_military_reward_cas_joint_exercises
        }
    }
    completion_reward = {
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_air_support_compact
                    }
                }
            }
            add_to_variable = {
                MKN_air_air_cas_efficiency = 0.05
                tooltip = MKN_air_air_cas_efficiency_tt
            }
            add_to_variable = {
                MKN_air_air_mission_efficiency = 0.05
                tooltip = MKN_air_air_mission_efficiency_tt
            }
            set_country_flag = MKN_military_stat_air_support_compact
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_air_support_compact
                    }
                }
            }
            add_doctrine_cost_reduction = {
                name = MKN_air_support_compact
                cost_reduction = 0.5
                uses = 2
                category = air_doctrine
            }
            if = {
                limit = {
                    has_dlc = "Arms Against Tyranny"
                }
                mio:MKN_attack_air_artels_organization = {
                    add_mio_size = 1
                    unlock_mio_trait_tooltip = MKN_attack_air_artels_organization_mature
                }
            }
            set_country_flag = MKN_military_reward_air_support_compact
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_airfield_fuel
                    }
                }
            }
            226 = {
                if = {
                    limit = {
                        is_owned_and_controlled_by = ROOT
                    }
                    add_building_construction = {
                        type = fuel_silo
                        level = 1
                        instant_build = yes
                    }
                }
            }
            set_country_flag = MKN_military_reward_airfield_fuel
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_tactical_recon
                    }
                }
            }
            if = {
                limit = {
                    has_dlc = "By Blood Alone"
                }
                add_tech_bonus = {
                    name = MKN_tactical_recon
                    bonus = 0.5
                    uses = 1
                    category = cat_scout_plane
                }
            }
            else = {
                add_tech_bonus = {
                    name = MKN_tactical_recon
                    bonus = 0.5
                    uses = 1
                    category = tactical_bomber
                }
            }
            set_country_flag = MKN_military_reward_tactical_recon
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_bomber_navigation
                    }
                }
            }
            add_tech_bonus = {
                name = MKN_bomber_navigation
                bonus = 0.5
                uses = 1
                category = tactical_bomber
            }
            set_country_flag = MKN_military_reward_bomber_navigation
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_air_supply_lift
                    }
                }
            }
            add_tech_bonus = {
                name = MKN_air_supply_lift
                bonus = 0.5
                uses = 1
                category = air_equipment
            }
            set_country_flag = MKN_military_reward_air_supply_lift
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_air_coastal_support
                    }
                }
            }
            add_tech_bonus = {
                name = MKN_air_coastal_support
                bonus = 0.5
                uses = 1
                category = naval_bomber
            }
            set_country_flag = MKN_military_reward_air_coastal_support
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_cas_replacement_crews
                    }
                }
            }
            air_experience = 20
            set_country_flag = MKN_military_reward_cas_replacement_crews
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_joint_target_planning
                    }
                }
            }
            add_doctrine_cost_reduction = {
                name = MKN_joint_target_planning
                cost_reduction = 0.5
                uses = 2
                category = air_doctrine
            }
            set_country_flag = MKN_military_reward_joint_target_planning
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_air_weather_service
                    }
                }
            }
            add_tech_bonus = {
                name = MKN_air_weather_service
                bonus = 0.5
                uses = 1
                category = electronics
            }
            set_country_flag = MKN_military_reward_air_weather_service
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_attack_wing_rotations
                    }
                }
            }
            air_experience = 20
            set_country_flag = MKN_military_reward_attack_wing_rotations
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_cas_joint_exercises
                    }
                }
            }
            air_experience = 30
            add_doctrine_cost_reduction = {
                name = MKN_cas_joint_exercises
                cost_reduction = 0.5
                uses = 1
                category = air_doctrine
            }
            add_mastery_bonus = {
                bonus = 0.1
                days = 240
                track = strike_aircraft
                name = MKN_cas_joint_exercises
            }
            set_country_flag = MKN_military_reward_cas_joint_exercises
        }
        set_country_flag = MKN_military_bundle_air_support_compact
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
        custom_effect_tooltip = MKN_military_program_progress_tt
    }
    ai_will_do = {
        factor = 3
    }
}
```

## Флот

### Черноморская флотилия и верфи — `MKN_black_sea_flotilla_and_yards`

EN: Black Sea Flotilla and Shipyards.

Описание RU: Создадим малую флотилию с задачами, посильными бюджету коммун.\n\nДнепровские дозоры станут школой будущих морских экипажей.\n\nХерсонские верфи дадут флотилии собственную строительную и ремонтную базу.\n\nОткрывает одноразовые тактики полевого штаба за опыт и командный ресурс.

Описание EN: Establish a small flotilla with missions the communes can afford.\n\nDnieper patrols will train the future sea-going crews.\n\nKherson yards will give the flotilla its own construction and repair base.\n\nUnlocks one-time field headquarters tactics purchased with experience and command power.

Источник: `common/national_focus/MKN.txt:4962`. Стоимость: 10 (70 дней). Координаты: x=82, y=0.

Предпосылки: нет нарисованной предпосылки; см. available.

Взаимоисключения: нет.

Прямые продолжения: MKN_sea_escort_service, MKN_torpedo_artels_focus.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_black_sea_flotilla_and_yards
    icon = GFX_focus_generic_black_sea_focus
    x = 82
    y = 0
    cost = 10
    available_if_capitulated = no
    available = {
        196 = {
            is_owned_and_controlled_by = ROOT
        }
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    bypass = {
        hidden_trigger = {
            has_country_flag = MKN_military_stat_black_sea_flotilla
            has_country_flag = MKN_military_stat_dnieper_patrol
            has_country_flag = MKN_military_stat_kherson_shipyard
            has_country_flag = MKN_military_reward_black_sea_flotilla
            has_country_flag = MKN_military_reward_dnieper_patrol
            has_country_flag = MKN_military_reward_kherson_shipyard
        }
    }
    completion_reward = {
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_black_sea_flotilla
                    }
                }
            }
            add_to_variable = {
                MKN_navy_naval_defense_factor = 0.03
                tooltip = MKN_navy_naval_defense_factor_tt
            }
            set_country_flag = MKN_military_stat_black_sea_flotilla
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_black_sea_flotilla
                    }
                }
            }
            navy_experience = 20
            set_country_flag = MKN_military_reward_black_sea_flotilla
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_dnieper_patrol
                    }
                }
            }
            add_to_variable = {
                MKN_navy_naval_detection = 0.05
                tooltip = MKN_navy_naval_detection_tt
            }
            set_country_flag = MKN_military_stat_dnieper_patrol
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_dnieper_patrol
                    }
                }
            }
            add_tech_bonus = {
                name = MKN_dnieper_patrol
                bonus = 0.5
                uses = 1
                category = dd_tech
            }
            set_country_flag = MKN_military_reward_dnieper_patrol
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_kherson_shipyard
                    }
                }
            }
            add_to_variable = {
                MKN_navy_industrial_capacity_dockyard = 0.05
                tooltip = MKN_navy_industrial_capacity_dockyard_tt
            }
            set_country_flag = MKN_military_stat_kherson_shipyard
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_kherson_shipyard
                    }
                }
            }
            196 = {
                if = {
                    limit = {
                        is_owned_and_controlled_by = ROOT
                    }
                    add_extra_state_shared_building_slots = 1
                    add_building_construction = {
                        type = dockyard
                        level = 1
                        instant_build = yes
                    }
                }
            }
            set_country_flag = MKN_military_reward_kherson_shipyard
        }
        set_country_flag = MKN_military_bundle_black_sea_flotilla_and_yards
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
        custom_effect_tooltip = MKN_navy_hq_unlock_tt
    }
    ai_will_do = {
        factor = 3
    }
}
```

### Служба морского эскорта — `MKN_sea_escort_service`

EN: Sea Escort Service.

Описание RU: Защитим подходы к портам и сделаем зерновую торговлю главной задачей флота.\n\nЛёгкие эскорты Херсонской артели будут держать строй вокруг конвоя.\n\nЭкипажи отработают охранение медленных транспортов вместо погони за славой.\n\nГидроакустики и расчёты глубинных бомб будут работать одной командой.

Описание EN: Defend port approaches and make grain shipping the navy's main mission.\n\nLight escorts from the Kherson cooperative will hold formation around convoys.\n\nCrews will train to protect slow transports rather than chase glory.\n\nSonar operators and depth-charge crews will work as one team.

Источник: `common/national_focus/MKN.txt:5089`. Стоимость: 10 (70 дней). Координаты: x=78, y=1.

Предпосылки: (Черноморская флотилия и верфи [MKN_black_sea_flotilla_and_yards]).

Взаимоисключения: MKN_torpedo_artels_focus.

Прямые продолжения: MKN_coastal_fortifications_focus.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_sea_escort_service
    icon = GFX_focus_generic_coastal_fort
    x = 78
    y = 1
    cost = 10
    available_if_capitulated = no
    prerequisite = {
        focus = MKN_black_sea_flotilla_and_yards
    }
    mutually_exclusive = {
        focus = MKN_torpedo_artels_focus
    }
    available = {
        196 = {
            is_owned_and_controlled_by = ROOT
        }
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    bypass = {
        hidden_trigger = {
            has_country_flag = MKN_military_stat_coastal_defense_steppe
            has_country_flag = MKN_military_stat_black_sea_escorts
            has_country_flag = MKN_military_stat_escort_crews
            has_country_flag = MKN_military_stat_depth_charge_school
            has_country_flag = MKN_military_reward_coastal_defense_steppe
            has_country_flag = MKN_military_reward_black_sea_escorts
            has_country_flag = MKN_military_reward_escort_crews
            has_country_flag = MKN_military_reward_depth_charge_school
        }
    }
    completion_reward = {
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_coastal_defense_steppe
                    }
                }
            }
            add_to_variable = {
                MKN_navy_convoy_escort_efficiency = 0.1
                tooltip = MKN_navy_convoy_escort_efficiency_tt
            }
            set_country_flag = MKN_military_stat_coastal_defense_steppe
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_coastal_defense_steppe
                    }
                }
            }
            196 = {
                if = {
                    limit = {
                        is_owned_and_controlled_by = ROOT
                    }
                    add_building_construction = {
                        type = coastal_bunker
                        level = 1
                        province = 568
                        instant_build = yes
                    }
                }
            }
            set_country_flag = MKN_military_reward_coastal_defense_steppe
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_black_sea_escorts
                    }
                }
            }
            add_to_variable = {
                MKN_navy_screening_efficiency = 0.08
                tooltip = MKN_navy_screening_efficiency_tt
            }
            set_country_flag = MKN_military_stat_black_sea_escorts
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_black_sea_escorts
                    }
                }
            }
            add_tech_bonus = {
                name = MKN_black_sea_escorts
                bonus = 0.5
                uses = 1
                category = asw_tech
            }
            set_country_flag = MKN_military_reward_black_sea_escorts
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_escort_crews
                    }
                }
            }
            add_to_variable = {
                MKN_navy_convoy_escort_efficiency = 0.05
                tooltip = MKN_navy_convoy_escort_efficiency_tt
            }
            set_country_flag = MKN_military_stat_escort_crews
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_escort_crews
                    }
                }
            }
            navy_experience = 20
            add_doctrine_cost_reduction = {
                name = MKN_escort_crews
                cost_reduction = 0.5
                uses = 1
                category = naval_doctrine
            }
            set_country_flag = MKN_military_reward_escort_crews
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_depth_charge_school
                    }
                }
            }
            add_to_variable = {
                MKN_navy_navy_submarine_detection_factor = 0.15
                tooltip = MKN_navy_navy_submarine_detection_factor_tt
            }
            set_country_flag = MKN_military_stat_depth_charge_school
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_depth_charge_school
                    }
                }
            }
            add_tech_bonus = {
                name = MKN_depth_charge_school
                bonus = 0.75
                uses = 1
                category = asw_tech
            }
            navy_experience = 15
            if = {
                limit = {
                    has_dlc = "Arms Against Tyranny"
                }
                mio:MKN_kherson_works_organization = {
                    add_mio_size = 1
                    unlock_mio_trait_tooltip = MKN_kherson_works_organization_specialization_a
                }
            }
            if = {
                limit = {
                    has_dlc = "Arms Against Tyranny"
                }
                mio:MKN_kherson_works_organization = {
                    add_mio_size = 1
                    unlock_mio_trait_tooltip = MKN_kherson_works_organization_specialization_b
                }
            }
            set_country_flag = MKN_military_reward_depth_charge_school
        }
        set_country_flag = MKN_military_bundle_sea_escort_service
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
        custom_effect_tooltip = MKN_military_program_progress_tt
    }
    ai_will_do = {
        factor = 3
    }
}
```

### Торпедные артели — `MKN_torpedo_artels_focus`

EN: Torpedo Artels.

Описание RU: Малые подлодки и рейдеры сделают вражеские перевозки уязвимыми без гонки линкоров.\n\nТорпедные мастерские займутся качеством оружия для скрытных атак.\n\nЭкипажи научатся выбирать цель и момент атаки, а не искать открытого боя.\n\nИспытания устранят отказы и уточнят дистанцию атаки.

Описание EN: Small submarines and raiders will threaten enemy shipping without a battleship race.\n\nTorpedo workshops will improve weapons for concealed attacks.\n\nCrews will choose targets and timing rather than seek open battle.\n\nTrials will eliminate failures and establish attack ranges.

Источник: `common/national_focus/MKN.txt:5802`. Стоимость: 10 (70 дней). Координаты: x=86, y=1.

Предпосылки: (Черноморская флотилия и верфи [MKN_black_sea_flotilla_and_yards]).

Взаимоисключения: MKN_sea_escort_service.

Прямые продолжения: MKN_hidden_smuggler_bases_focus.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_torpedo_artels_focus
    icon = GFX_focus_generic_smugglers
    x = 86
    y = 1
    cost = 10
    available_if_capitulated = no
    prerequisite = {
        focus = MKN_black_sea_flotilla_and_yards
    }
    mutually_exclusive = {
        focus = MKN_sea_escort_service
    }
    available = {
        196 = {
            is_owned_and_controlled_by = ROOT
        }
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    bypass = {
        hidden_trigger = {
            has_country_flag = MKN_military_stat_black_sea_smugglers
            has_country_flag = MKN_military_stat_torpedo_artels
            has_country_flag = MKN_military_stat_submarine_crews
            has_country_flag = MKN_military_stat_torpedo_trials
            has_country_flag = MKN_military_reward_black_sea_smugglers
            has_country_flag = MKN_military_reward_torpedo_artels
            has_country_flag = MKN_military_reward_submarine_crews
            has_country_flag = MKN_military_reward_torpedo_trials
        }
    }
    completion_reward = {
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_black_sea_smugglers
                    }
                }
            }
            add_to_variable = {
                MKN_navy_convoy_raiding_efficiency_factor = 0.1
                tooltip = MKN_navy_convoy_raiding_efficiency_factor_tt
            }
            set_country_flag = MKN_military_stat_black_sea_smugglers
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_black_sea_smugglers
                    }
                }
            }
            add_tech_bonus = {
                name = MKN_black_sea_smugglers
                bonus = 0.75
                uses = 1
                category = ss_tech
            }
            set_country_flag = MKN_military_reward_black_sea_smugglers
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_torpedo_artels
                    }
                }
            }
            add_to_variable = {
                MKN_navy_naval_torpedo_hit_chance_factor = 0.05
                tooltip = MKN_navy_naval_torpedo_hit_chance_factor_tt
            }
            set_country_flag = MKN_military_stat_torpedo_artels
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_torpedo_artels
                    }
                }
            }
            if = {
                limit = {
                    has_dlc = "Man the Guns"
                }
                add_tech_bonus = {
                    name = MKN_torpedo_artels
                    bonus = 0.5
                    uses = 1
                    category = cat_torpedoes
                }
            }
            else = {
                add_tech_bonus = {
                    name = MKN_torpedo_artels
                    bonus = 0.5
                    uses = 1
                    category = ss_tech
                }
            }
            if = {
                limit = {
                    has_dlc = "Arms Against Tyranny"
                }
                mio:MKN_submarine_works_organization = {
                    add_mio_size = 1
                }
            }
            set_country_flag = MKN_military_reward_torpedo_artels
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_submarine_crews
                    }
                }
            }
            add_to_variable = {
                MKN_navy_navy_submarine_attack_factor = 0.05
                tooltip = MKN_navy_navy_submarine_attack_factor_tt
            }
            set_country_flag = MKN_military_stat_submarine_crews
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_submarine_crews
                    }
                }
            }
            navy_experience = 20
            add_doctrine_cost_reduction = {
                name = MKN_submarine_crews
                cost_reduction = 0.5
                uses = 1
                category = naval_doctrine
            }
            set_country_flag = MKN_military_reward_submarine_crews
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_torpedo_trials
                    }
                }
            }
            add_to_variable = {
                MKN_navy_naval_torpedo_hit_chance_factor = 0.05
                tooltip = MKN_navy_naval_torpedo_hit_chance_factor_tt
            }
            set_country_flag = MKN_military_stat_torpedo_trials
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_torpedo_trials
                    }
                }
            }
            if = {
                limit = {
                    has_dlc = "Man the Guns"
                }
                add_tech_bonus = {
                    name = MKN_torpedo_trials
                    bonus = 0.5
                    uses = 1
                    category = cat_torpedoes
                }
            }
            else = {
                add_tech_bonus = {
                    name = MKN_torpedo_trials
                    bonus = 0.5
                    uses = 1
                    category = ss_tech
                }
            }
            navy_experience = 15
            set_country_flag = MKN_military_reward_torpedo_trials
        }
        set_country_flag = MKN_military_bundle_torpedo_artels_focus
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
        custom_effect_tooltip = MKN_military_program_progress_tt
    }
    ai_will_do = {
        factor = 3
    }
}
```

### Береговые укрепления — `MKN_coastal_fortifications_focus`

EN: Coastal Fortifications.

Описание RU: Речные экипажи перейдут на лёгкие мореходные корабли для прибрежной службы.\n\nБереговые посты предупредят капитанов о появлении противника.

Описание EN: River crews will move to light sea-going ships for coastal service.\n\nCoastal stations will warn captains of enemy movements.

Источник: `common/national_focus/MKN.txt:5279`. Стоимость: 5 (35 дней). Координаты: x=78, y=2.

Предпосылки: (Служба морского эскорта [MKN_sea_escort_service]).

Взаимоисключения: нет.

Прямые продолжения: MKN_escort_repair_network_focus.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_coastal_fortifications_focus
    icon = GFX_goal_generic_navy_cruiser
    x = 78
    y = 2
    cost = 5
    available_if_capitulated = no
    prerequisite = {
        focus = MKN_sea_escort_service
    }
    available = {
        196 = {
            is_owned_and_controlled_by = ROOT
        }
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    bypass = {
        hidden_trigger = {
            has_country_flag = MKN_military_stat_dnieper_gun_flotilla
            has_country_flag = MKN_military_stat_coastal_signal_posts
            has_country_flag = MKN_military_reward_dnieper_gun_flotilla
            has_country_flag = MKN_military_reward_coastal_signal_posts
        }
    }
    completion_reward = {
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_dnieper_gun_flotilla
                    }
                }
            }
            add_to_variable = {
                MKN_navy_naval_defense_factor = 0.05
                tooltip = MKN_navy_naval_defense_factor_tt
            }
            set_country_flag = MKN_military_stat_dnieper_gun_flotilla
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_dnieper_gun_flotilla
                    }
                }
            }
            add_tech_bonus = {
                name = MKN_dnieper_gun_flotilla
                bonus = 0.75
                uses = 1
                category = dd_tech
            }
            if = {
                limit = {
                    has_dlc = "Arms Against Tyranny"
                }
                mio:MKN_kherson_works_organization = {
                    add_mio_size = 1
                }
            }
            set_country_flag = MKN_military_reward_dnieper_gun_flotilla
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_coastal_signal_posts
                    }
                }
            }
            add_to_variable = {
                MKN_navy_naval_detection = 0.08
                tooltip = MKN_navy_naval_detection_tt
            }
            set_country_flag = MKN_military_stat_coastal_signal_posts
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_coastal_signal_posts
                    }
                }
            }
            add_tech_bonus = {
                name = MKN_coastal_signal_posts
                bonus = 0.5
                uses = 1
                category = radar_tech
            }
            set_country_flag = MKN_military_reward_coastal_signal_posts
        }
        set_country_flag = MKN_military_bundle_coastal_fortifications_focus
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
        custom_effect_tooltip = MKN_military_program_progress_tt
        custom_effect_tooltip = MKN_project_coastal_battery_unlock_tt
    }
    ai_will_do = {
        factor = 3
    }
}
```

### Тайные базы контрабандистов — `MKN_hidden_smuggler_bases_focus`

EN: Hidden Smuggler Bases.

Описание RU: Тайные стоянки позволят подготовить выход, не выдавая расположение рейдеров.\n\nКарты торговых маршрутов укажут ценные цели и безопасные районы ожидания.\n\nЛиманские мастерские наладят серийное строительство малых подлодок.\n\nНочные выходы сократят время, когда рейдер виден береговым наблюдателям.\n\nСкрытые топливные запасы увеличат время охоты на торговых путях.

Описание EN: Concealed anchorages will prepare sorties without exposing raider positions.\n\nShipping intelligence will identify valuable targets and safe waiting areas.\n\nEstuary workshops will organize serial construction of small submarines.\n\nNight sorties will reduce exposure to coastal observers.\n\nConcealed fuel reserves will extend patrols along shipping routes.

Источник: `common/national_focus/MKN.txt:6001`. Стоимость: 10 (70 дней). Координаты: x=86, y=2.

Предпосылки: (Торпедные артели [MKN_torpedo_artels_focus]).

Взаимоисключения: нет.

Прямые продолжения: MKN_raider_compact.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_hidden_smuggler_bases_focus
    icon = GFX_focus_generic_infiltration
    x = 86
    y = 2
    cost = 10
    available_if_capitulated = no
    prerequisite = {
        focus = MKN_torpedo_artels_focus
    }
    available = {
        196 = {
            is_owned_and_controlled_by = ROOT
        }
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    bypass = {
        hidden_trigger = {
            has_country_flag = MKN_military_stat_hidden_anchorages
            has_country_flag = MKN_military_stat_naval_intelligence
            has_country_flag = MKN_military_stat_raider_dockyard
            has_country_flag = MKN_military_stat_night_sorties
            has_country_flag = MKN_military_stat_raider_supply
            has_country_flag = MKN_military_reward_hidden_anchorages
            has_country_flag = MKN_military_reward_naval_intelligence
            has_country_flag = MKN_military_reward_raider_dockyard
            has_country_flag = MKN_military_reward_night_sorties
            has_country_flag = MKN_military_reward_raider_supply
        }
    }
    completion_reward = {
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_hidden_anchorages
                    }
                }
            }
            add_to_variable = {
                MKN_navy_naval_torpedo_reveal_chance_factor = -0.08
                tooltip = MKN_navy_naval_torpedo_reveal_chance_factor_tt
            }
            set_country_flag = MKN_military_stat_hidden_anchorages
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_hidden_anchorages
                    }
                }
            }
            196 = {
                if = {
                    limit = {
                        is_owned_and_controlled_by = ROOT
                    }
                    add_building_construction = {
                        type = naval_base
                        level = 1
                        province = 568
                        instant_build = yes
                    }
                }
            }
            set_country_flag = MKN_military_reward_hidden_anchorages
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_naval_intelligence
                    }
                }
            }
            add_to_variable = {
                MKN_navy_naval_detection = 0.08
                tooltip = MKN_navy_naval_detection_tt
            }
            set_country_flag = MKN_military_stat_naval_intelligence
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_naval_intelligence
                    }
                }
            }
            add_tech_bonus = {
                name = MKN_naval_intelligence
                bonus = 0.5
                uses = 1
                category = decryption_tech
            }
            set_country_flag = MKN_military_reward_naval_intelligence
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_raider_dockyard
                    }
                }
            }
            add_to_variable = {
                MKN_navy_industrial_capacity_dockyard = 0.05
                tooltip = MKN_navy_industrial_capacity_dockyard_tt
            }
            set_country_flag = MKN_military_stat_raider_dockyard
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_raider_dockyard
                    }
                }
            }
            196 = {
                if = {
                    limit = {
                        is_owned_and_controlled_by = ROOT
                    }
                    add_extra_state_shared_building_slots = 1
                    add_building_construction = {
                        type = dockyard
                        level = 1
                        instant_build = yes
                    }
                }
            }
            set_country_flag = MKN_military_reward_raider_dockyard
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_night_sorties
                    }
                }
            }
            add_to_variable = {
                MKN_navy_naval_torpedo_reveal_chance_factor = -0.07
                tooltip = MKN_navy_naval_torpedo_reveal_chance_factor_tt
            }
            set_country_flag = MKN_military_stat_night_sorties
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_night_sorties
                    }
                }
            }
            navy_experience = 20
            if = {
                limit = {
                    has_dlc = "Arms Against Tyranny"
                }
                mio:MKN_submarine_works_organization = {
                    add_mio_size = 1
                    unlock_mio_trait_tooltip = MKN_submarine_works_organization_specialization_a
                }
            }
            if = {
                limit = {
                    has_dlc = "Arms Against Tyranny"
                }
                mio:MKN_submarine_works_organization = {
                    add_mio_size = 1
                    unlock_mio_trait_tooltip = MKN_submarine_works_organization_specialization_b
                }
            }
            set_country_flag = MKN_military_reward_night_sorties
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_raider_supply
                    }
                }
            }
            add_to_variable = {
                MKN_navy_navy_fuel_consumption_factor = -0.1
                tooltip = MKN_navy_navy_fuel_consumption_factor_tt
            }
            set_country_flag = MKN_military_stat_raider_supply
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_raider_supply
                    }
                }
            }
            196 = {
                if = {
                    limit = {
                        is_owned_and_controlled_by = ROOT
                    }
                    add_building_construction = {
                        type = fuel_silo
                        level = 1
                        instant_build = yes
                    }
                }
            }
            set_country_flag = MKN_military_reward_raider_supply
        }
        set_country_flag = MKN_military_bundle_hidden_smuggler_bases_focus
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
        custom_effect_tooltip = MKN_military_program_progress_tt
        custom_effect_tooltip = MKN_project_hidden_cove_unlock_tt
        custom_effect_tooltip = MKN_project_fuel_cache_unlock_tt
    }
    ai_will_do = {
        factor = 3
    }
}
```

### Ремонтные артели эскорта — `MKN_escort_repair_network_focus`

EN: Escort Repair Artels.

Описание RU: Расчищенные фарватеры ускорят оборот кораблей и портовое снабжение.\n\nСудоремонтные артели освоят замену повреждённых секций и переоборудование.\n\nОбщие расписания и новые транспорты позволят сопровождать торговлю организованными группами.

Описание EN: Dredged channels will improve ship turnaround and harbour logistics.\n\nRepair cooperatives will learn hull repairs and refitting.\n\nShared schedules and new transports will organize shipping into escorted groups.

Источник: `common/national_focus/MKN.txt:5384`. Стоимость: 10 (70 дней). Координаты: x=78, y=3.

Предпосылки: (Береговые укрепления [MKN_coastal_fortifications_focus]).

Взаимоисключения: нет.

Прямые продолжения: MKN_escort_compact.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_escort_repair_network_focus
    icon = GFX_focus_generic_public_works
    x = 78
    y = 3
    cost = 10
    available_if_capitulated = no
    prerequisite = {
        focus = MKN_coastal_fortifications_focus
    }
    available = {
        196 = {
            is_owned_and_controlled_by = ROOT
        }
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    bypass = {
        hidden_trigger = {
            has_country_flag = MKN_military_stat_harbour_dredging
            has_country_flag = MKN_military_stat_hull_repair_artels
            has_country_flag = MKN_military_stat_convoy_schedules
            has_country_flag = MKN_military_reward_harbour_dredging
            has_country_flag = MKN_military_reward_hull_repair_artels
            has_country_flag = MKN_military_reward_convoy_schedules
        }
    }
    completion_reward = {
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_harbour_dredging
                    }
                }
            }
            add_to_variable = {
                MKN_navy_navy_fuel_consumption_factor = -0.08
                tooltip = MKN_navy_navy_fuel_consumption_factor_tt
            }
            set_country_flag = MKN_military_stat_harbour_dredging
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_harbour_dredging
                    }
                }
            }
            196 = {
                if = {
                    limit = {
                        is_owned_and_controlled_by = ROOT
                    }
                    add_building_construction = {
                        type = naval_base
                        level = 1
                        province = 568
                        instant_build = yes
                    }
                }
            }
            set_country_flag = MKN_military_reward_harbour_dredging
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_hull_repair_artels
                    }
                }
            }
            add_to_variable = {
                MKN_navy_repair_speed_factor = 0.15
                tooltip = MKN_navy_repair_speed_factor_tt
            }
            set_country_flag = MKN_military_stat_hull_repair_artels
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_hull_repair_artels
                    }
                }
            }
            if = {
                limit = {
                    has_dlc = "Man the Guns"
                }
                add_tech_bonus = {
                    name = MKN_hull_repair_artels
                    bonus = 0.5
                    uses = 1
                    category = ship_modules_tech
                }
            }
            else = {
                add_tech_bonus = {
                    name = MKN_hull_repair_artels
                    bonus = 0.5
                    uses = 1
                    category = dd_tech
                }
            }
            set_country_flag = MKN_military_reward_hull_repair_artels
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_convoy_schedules
                    }
                }
            }
            add_to_variable = {
                MKN_navy_convoy_escort_efficiency = 0.05
                tooltip = MKN_navy_convoy_escort_efficiency_tt
            }
            set_country_flag = MKN_military_stat_convoy_schedules
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_convoy_schedules
                    }
                }
            }
            add_equipment_to_stockpile = {
                type = convoy_1
                amount = 20
                producer = ROOT
            }
            set_country_flag = MKN_military_reward_convoy_schedules
        }
        set_country_flag = MKN_military_bundle_escort_repair_network_focus
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
        custom_effect_tooltip = MKN_military_program_progress_tt
    }
    ai_will_do = {
        factor = 3
    }
}
```

### Море для вольных рейдеров — `MKN_raider_compact`

EN: Sea for Free Raiders.

Описание RU: Рейдерская система готова; дополнительные катера, ремонт и тактику засад можно развивать по обстановке. Дополнительные тактики приобретаются отдельно в полевом штабе.

Описание EN: The raiding system is ready, with craft, repair and ambush tactics available as extensions. Further tactics can be purchased separately at the field headquarters.

Источник: `common/national_focus/MKN.txt:6228`. Стоимость: 10 (70 дней). Координаты: x=86, y=3.

Предпосылки: (Тайные базы контрабандистов [MKN_hidden_smuggler_bases_focus]).

Взаимоисключения: нет.

Прямые продолжения: нет.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_raider_compact
    icon = GFX_goal_generic_navy_submarine
    x = 86
    y = 3
    cost = 10
    available_if_capitulated = no
    prerequisite = {
        focus = MKN_hidden_smuggler_bases_focus
    }
    available = {
        196 = {
            is_owned_and_controlled_by = ROOT
        }
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    bypass = {
        hidden_trigger = {
            has_country_flag = MKN_military_stat_raider_compact
            has_country_flag = MKN_military_reward_raider_compact
            has_country_flag = MKN_military_reward_submarine_listening
            has_country_flag = MKN_military_reward_fast_attack_craft
            has_country_flag = MKN_military_reward_raider_radio_discipline
            has_country_flag = MKN_military_reward_submarine_repair
            has_country_flag = MKN_military_reward_raider_weather
            has_country_flag = MKN_military_reward_raider_replacement_crews
            has_country_flag = MKN_military_reward_torpedo_ambushes
            has_country_flag = MKN_military_reward_disrupt_enemy_trade
            has_country_flag = MKN_military_reward_raider_escape_routes
            has_country_flag = MKN_military_reward_raider_exercises
        }
    }
    completion_reward = {
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_raider_compact
                    }
                }
            }
            add_to_variable = {
                MKN_navy_convoy_raiding_efficiency_factor = 0.1
                tooltip = MKN_navy_convoy_raiding_efficiency_factor_tt
            }
            add_to_variable = {
                MKN_navy_navy_submarine_attack_factor = 0.05
                tooltip = MKN_navy_navy_submarine_attack_factor_tt
            }
            set_country_flag = MKN_military_stat_raider_compact
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_raider_compact
                    }
                }
            }
            add_doctrine_cost_reduction = {
                name = MKN_raider_compact
                cost_reduction = 0.5
                uses = 2
                category = naval_doctrine
            }
            if = {
                limit = {
                    has_dlc = "Arms Against Tyranny"
                }
                mio:MKN_submarine_works_organization = {
                    add_mio_size = 1
                    unlock_mio_trait_tooltip = MKN_submarine_works_organization_mature
                }
            }
            set_country_flag = MKN_military_reward_raider_compact
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_submarine_listening
                    }
                }
            }
            if = {
                limit = {
                    has_dlc = "Man the Guns"
                }
                add_tech_bonus = {
                    name = MKN_submarine_listening
                    bonus = 0.5
                    uses = 1
                    category = asw_tech
                }
            }
            else = {
                add_tech_bonus = {
                    name = MKN_submarine_listening
                    bonus = 0.5
                    uses = 1
                    category = ss_tech
                }
            }
            set_country_flag = MKN_military_reward_submarine_listening
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_fast_attack_craft
                    }
                }
            }
            add_tech_bonus = {
                name = MKN_fast_attack_craft
                bonus = 0.5
                uses = 1
                category = dd_tech
            }
            set_country_flag = MKN_military_reward_fast_attack_craft
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_raider_radio_discipline
                    }
                }
            }
            add_tech_bonus = {
                name = MKN_raider_radio_discipline
                bonus = 0.5
                uses = 1
                category = encryption_tech
            }
            set_country_flag = MKN_military_reward_raider_radio_discipline
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_submarine_repair
                    }
                }
            }
            if = {
                limit = {
                    has_dlc = "Man the Guns"
                }
                add_tech_bonus = {
                    name = MKN_submarine_repair
                    bonus = 0.5
                    uses = 1
                    category = ship_modules_tech
                }
            }
            else = {
                add_tech_bonus = {
                    name = MKN_submarine_repair
                    bonus = 0.5
                    uses = 1
                    category = ss_tech
                }
            }
            set_country_flag = MKN_military_reward_submarine_repair
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_raider_weather
                    }
                }
            }
            add_tech_bonus = {
                name = MKN_raider_weather
                bonus = 0.5
                uses = 1
                category = electronics
            }
            set_country_flag = MKN_military_reward_raider_weather
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_raider_replacement_crews
                    }
                }
            }
            navy_experience = 20
            set_country_flag = MKN_military_reward_raider_replacement_crews
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_torpedo_ambushes
                    }
                }
            }
            add_doctrine_cost_reduction = {
                name = MKN_torpedo_ambushes
                cost_reduction = 0.5
                uses = 2
                category = naval_doctrine
            }
            set_country_flag = MKN_military_reward_torpedo_ambushes
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_disrupt_enemy_trade
                    }
                }
            }
            navy_experience = 20
            set_country_flag = MKN_military_reward_disrupt_enemy_trade
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_raider_escape_routes
                    }
                }
            }
            add_tech_bonus = {
                name = MKN_raider_escape_routes
                bonus = 0.5
                uses = 1
                category = recon_tech
            }
            set_country_flag = MKN_military_reward_raider_escape_routes
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_raider_exercises
                    }
                }
            }
            navy_experience = 30
            add_doctrine_cost_reduction = {
                name = MKN_raider_exercises
                cost_reduction = 0.5
                uses = 1
                category = naval_doctrine
            }
            add_mastery_bonus = {
                bonus = 0.1
                days = 240
                track = submarines
                name = MKN_raider_exercises
            }
            set_country_flag = MKN_military_reward_raider_exercises
        }
        set_country_flag = MKN_military_bundle_raider_compact
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
        custom_effect_tooltip = MKN_military_program_progress_tt
    }
    ai_will_do = {
        factor = 3
    }
}
```

### Море для хлебных конвоев — `MKN_escort_compact`

EN: Sea Lanes for Grain Convoys.

Описание RU: Основная система эскорта готова; противолодочные и спасательные службы можно расширять дальше. Дополнительные тактики приобретаются отдельно в полевом штабе.

Описание EN: The core escort system is ready, with room to expand anti-submarine and rescue services. Further tactics can be purchased separately at the field headquarters.

Источник: `common/national_focus/MKN.txt:5531`. Стоимость: 10 (70 дней). Координаты: x=78, y=4.

Предпосылки: (Ремонтные артели эскорта [MKN_escort_repair_network_focus]).

Взаимоисключения: нет.

Прямые продолжения: нет.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_escort_compact
    icon = GFX_focus_generic_merchant_fleet
    x = 78
    y = 4
    cost = 10
    available_if_capitulated = no
    prerequisite = {
        focus = MKN_escort_repair_network_focus
    }
    available = {
        196 = {
            is_owned_and_controlled_by = ROOT
        }
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    bypass = {
        hidden_trigger = {
            has_country_flag = MKN_military_stat_escort_compact
            has_country_flag = MKN_military_reward_escort_compact
            has_country_flag = MKN_military_reward_fleet_damage_control
            has_country_flag = MKN_military_reward_coastal_watch
            has_country_flag = MKN_military_reward_sweeper_sections
            has_country_flag = MKN_military_reward_escort_radio_net
            has_country_flag = MKN_military_reward_coastal_depots
            has_country_flag = MKN_military_reward_river_sea_coordination
            has_country_flag = MKN_military_reward_anti_submarine_patrols
            has_country_flag = MKN_military_reward_convoy_rescue
            has_country_flag = MKN_military_reward_escort_reserves
            has_country_flag = MKN_military_reward_coastal_fleet_exercises
        }
    }
    completion_reward = {
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_escort_compact
                    }
                }
            }
            add_to_variable = {
                MKN_navy_convoy_escort_efficiency = 0.05
                tooltip = MKN_navy_convoy_escort_efficiency_tt
            }
            add_to_variable = {
                MKN_navy_screening_efficiency = 0.05
                tooltip = MKN_navy_screening_efficiency_tt
            }
            set_country_flag = MKN_military_stat_escort_compact
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_escort_compact
                    }
                }
            }
            add_doctrine_cost_reduction = {
                name = MKN_escort_compact
                cost_reduction = 0.5
                uses = 2
                category = naval_doctrine
            }
            if = {
                limit = {
                    has_dlc = "Arms Against Tyranny"
                }
                mio:MKN_kherson_works_organization = {
                    add_mio_size = 1
                    unlock_mio_trait_tooltip = MKN_kherson_works_organization_mature
                }
            }
            set_country_flag = MKN_military_reward_escort_compact
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_fleet_damage_control
                    }
                }
            }
            navy_experience = 15
            set_country_flag = MKN_military_reward_fleet_damage_control
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_coastal_watch
                    }
                }
            }
            add_tech_bonus = {
                name = MKN_coastal_watch
                bonus = 0.75
                uses = 1
                category = radar_tech
            }
            set_country_flag = MKN_military_reward_coastal_watch
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_sweeper_sections
                    }
                }
            }
            if = {
                limit = {
                    has_dlc = "Man the Guns"
                }
                add_tech_bonus = {
                    name = MKN_sweeper_sections
                    bonus = 0.5
                    uses = 1
                    category = naval_minesweeping
                }
            }
            else = {
                add_tech_bonus = {
                    name = MKN_sweeper_sections
                    bonus = 0.5
                    uses = 1
                    category = dd_tech
                }
            }
            set_country_flag = MKN_military_reward_sweeper_sections
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_escort_radio_net
                    }
                }
            }
            add_tech_bonus = {
                name = MKN_escort_radio_net
                bonus = 0.5
                uses = 1
                category = electronics
            }
            set_country_flag = MKN_military_reward_escort_radio_net
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_coastal_depots
                    }
                }
            }
            196 = {
                if = {
                    limit = {
                        is_owned_and_controlled_by = ROOT
                    }
                    add_building_construction = {
                        type = fuel_silo
                        level = 1
                        instant_build = yes
                    }
                }
            }
            set_country_flag = MKN_military_reward_coastal_depots
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_river_sea_coordination
                    }
                }
            }
            add_doctrine_cost_reduction = {
                name = MKN_river_sea_coordination
                cost_reduction = 0.5
                uses = 2
                category = naval_doctrine
            }
            set_country_flag = MKN_military_reward_river_sea_coordination
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_anti_submarine_patrols
                    }
                }
            }
            add_tech_bonus = {
                name = MKN_anti_submarine_patrols
                bonus = 0.5
                uses = 1
                category = asw_tech
            }
            navy_experience = 20
            set_country_flag = MKN_military_reward_anti_submarine_patrols
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_convoy_rescue
                    }
                }
            }
            navy_experience = 15
            set_country_flag = MKN_military_reward_convoy_rescue
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_escort_reserves
                    }
                }
            }
            196 = {
                if = {
                    limit = {
                        is_owned_and_controlled_by = ROOT
                    }
                    add_extra_state_shared_building_slots = 1
                    add_building_construction = {
                        type = dockyard
                        level = 1
                        instant_build = yes
                    }
                }
            }
            set_country_flag = MKN_military_reward_escort_reserves
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_reward_coastal_fleet_exercises
                    }
                }
            }
            navy_experience = 30
            add_doctrine_cost_reduction = {
                name = MKN_coastal_fleet_exercises
                cost_reduction = 0.5
                uses = 1
                category = naval_doctrine
            }
            add_mastery_bonus = {
                bonus = 0.1
                days = 240
                track = screens
                name = MKN_coastal_fleet_exercises
            }
            set_country_flag = MKN_military_reward_coastal_fleet_exercises
        }
        set_country_flag = MKN_military_bundle_escort_compact
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
        custom_effect_tooltip = MKN_military_program_progress_tt
    }
    ai_will_do = {
        factor = 3
    }
}
```

## Связанные военные награды вне основных деревьев

### Мандаты северных волостей — `MKN_northern_delegates`

EN: Mandates of the Northern Districts.

Описание RU: Глухов и бывшая украинская область Лиски отправят своих делегатов. Местные мандаты обеспечат национализацию, добровольцев и политический доход.

Описание EN: Hlukhiv and the former Ukrainian district of Liski send delegates. Local mandates bring cores, volunteers and political income.

Источник: `common/national_focus/MKN_ukraine_integration_focuses.txt:110`. Стоимость: 5 (35 дней). Координаты: x=150, y=1.

Предпосылки: (Съезд украинских коммун [MKN_ukrainian_communes_congress]).

Взаимоисключения: нет.

Прямые продолжения: MKN_ukrainian_rail_reconstruction.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_northern_delegates
    icon = GFX_focus_generic_manpower
    x = 150
    y = 1
    cost = 5
    available_if_capitulated = no
    cancel_if_invalid = yes
    continue_if_invalid = no
    available = {
        MKN_ukraine_integration_ready = yes
    }
    search_filters = {
        FOCUS_FILTER_POLITICAL
        FOCUS_FILTER_INDUSTRY
    }
    ai_will_do = {
        factor = 5
    }
    completion_reward = {
        add_manpower = 10000
        225 = {
            add_core_of = ROOT
        }
        259 = {
            add_core_of = ROOT
        }
        add_to_variable = {
            MKN_unified_political_power_gain = 0.1000
            tooltip = MKN_unified_political_power_gain_tt
        }
    }
    prerequisite = {
        focus = MKN_ukrainian_communes_congress
    }
}
```

### Передвижные мастерские и кузницы — `MKN_mobile_workshops`

EN: Mobile Workshops and Village Smithies.

Описание RU: Сельские кузни войдут в сеть ремонтных поездок и передвижных мастерских. Два военных завода, грузовики и обмен инструментом восстановят выпуск, не собирая всё хозяйство в одном уязвимом центре.

Описание EN: Village smithies join travelling repair teams. Two military factories, trucks and shared tools restore production without concentrating it in one vulnerable industrial centre.

Источник: `common/national_focus/MKN.txt:621`. Стоимость: 10 (70 дней). Координаты: x=16, y=3.

Предпосылки: (Степные рынки [MKN_steppe_markets]).

Взаимоисключения: нет.

Прямые продолжения: MKN_rifle_concern.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_mobile_workshops
    icon = GFX_focus_generic_industry_2
    x = 16
    y = 3
    cost = 10
    available_if_capitulated = no
    ai_will_do = {
        factor = 2
    }
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    prerequisite = {
        focus = MKN_steppe_markets
    }
    completion_reward = {
        army_experience = 20
        add_equipment_to_stockpile = {
            type = motorized_equipment_1
            amount = 100
            producer = MKN
        }
        random_owned_controlled_state = {
            limit = {
                is_core_of = ROOT
            }
            prioritize = {
                1082
                200
                196
            }
            add_extra_state_shared_building_slots = 2
            add_building_construction = {
                type = arms_factory
                level = 2
                instant_build = yes
            }
        }
        add_to_variable = {
            MKN_unified_political_power_gain = 0.1000
            tooltip = MKN_unified_political_power_gain_tt
        }
        add_to_variable = {
            MKN_unified_consumer_goods_factor = -0.0500
            tooltip = MKN_unified_consumer_goods_factor_tt
        }
        add_to_variable = {
            MKN_unified_production_speed_buildings_factor = 0.0500
            tooltip = MKN_unified_production_speed_buildings_factor_tt
        }
        add_to_variable = {
            MKN_unified_industrial_capacity_factory = 0.1000
            tooltip = MKN_unified_industrial_capacity_factory_tt
        }
        add_to_variable = {
            MKN_unified_production_factory_efficiency_gain_factor = 0.1000
            tooltip = MKN_unified_production_factory_efficiency_gain_factor_tt
        }
        add_to_variable = {
            MKN_unified_research_speed_factor = 0.0500
            tooltip = MKN_unified_research_speed_factor_tt
        }
    }
}
```

### Артельные авиамастерские — `MKN_workshop_airplane_artels`

EN: Artel Aviation Workshops.

Описание RU: Разъездные авиамастерские ремонтируют и сколачивают машины прямо под открытым небом.

Описание EN: Itinerant aviation workshops repair and assemble machines in the open air.

Источник: `common/national_focus/MKN.txt:979`. Стоимость: 5 (35 дней). Координаты: x=27, y=4.

Предпосылки: (Технические коммуны [MKN_technical_communes]).

Взаимоисключения: нет.

Прямые продолжения: MKN_advanced_research.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_workshop_airplane_artels
    icon = GFX_focus_generic_air_research_boost
    completion_reward = {
        air_experience = 20
        226 = {
            if = {
                limit = {
                    is_owned_and_controlled_by = ROOT
                }
                add_extra_state_shared_building_slots = 1
                add_building_construction = {
                    type = arms_factory
                    level = 1
                    instant_build = yes
                }
            }
        }
        add_tech_bonus = {
            bonus = 0.5
            uses = 1
            category = air_equipment
        }
    }
    prerequisite = {
        focus = MKN_technical_communes
    }
    x = 27
    y = 4
    cost = 5
}
```

### Теневое государство — `MKN_shadow_republic`

EN: Shadow Republic.

Описание RU: Государство, которое почти никогда не спорит вслух, но всегда чувствуется в воздухе.

Описание EN: The state that never quite appears, but is always felt.

Источник: `common/national_focus/MKN.txt:1074`. Стоимость: 5 (35 дней). Координаты: x=32, y=4.

Предпосылки: (Крестьяне и рабочие [MKN_farmers_and_workers]).

Взаимоисключения: нет.

Прямые продолжения: нет.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_shadow_republic
    icon = GFX_focus_generic_industry_1
    prerequisite = {
        focus = MKN_farmers_and_workers
    }
    completion_reward = {
        add_tech_bonus = {
            bonus = 0.5
            uses = 1
            category = industry
        }
        add_manpower = 20000
    }
    x = 32
    y = 4
    cost = 5
}
```

### Чёрное знамя на восток — `MKN_black_banner_east`

EN: Black Banner East.

Описание RU: Киев кланяется Москве. Восток надо освободить от обоих.

Описание EN: Kiev bows to Moscow. The east must be freed from both.

Источник: `common/national_focus/MKN.txt:1118`. Стоимость: 5 (35 дней). Координаты: x=36, y=4.

Предпосылки: (Федерация «Набат» [MKN_nabat_federation]).

Взаимоисключения: нет.

Прямые продолжения: MKN_makhno_moves_south.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_black_banner_east
    icon = GFX_focus_generic_army_attack
    prerequisite = {
        focus = MKN_nabat_federation
    }
    completion_reward = {
        army_experience = 20
        add_political_power = 80
        add_war_support = 0.1
        country_event = {
            id = mkn.1
            days = 1
        }
    }
    x = 36
    y = 4
    cost = 5
}
```

### Рабочие батальоны резерва — `MKN_worker_battalions`

EN: Workers’ Reserve Battalions.

Описание RU: Выборные бригадиры и заводские инструкторы подготовят резерв без разрыва с производством. Общие сборы улучшат организацию и планирование армии и сократят подготовку новых частей.

Описание EN: Elected brigadiers and factory instructors train a reserve without severing its ties to production. Joint exercises improve organization and planning while reducing training time.

Источник: `common/national_focus/MKN.txt:282`. Стоимость: 5 (35 дней). Координаты: x=6, y=5.

Предпосылки: (Запорожсталь [MKN_zaporizhstal]).

Взаимоисключения: нет.

Прямые продолжения: MKN_production_cycles.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_worker_battalions
    icon = GFX_focus_generic_manpower
    x = 6
    y = 5
    cost = 5
    available_if_capitulated = no
    ai_will_do = {
        factor = 2
    }
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    prerequisite = {
        focus = MKN_zaporizhstal
    }
    completion_reward = {
        army_experience = 40
        add_to_variable = {
            MKN_unified_army_org_factor = 0.2000
            tooltip = MKN_unified_army_org_factor_tt
        }
        add_to_variable = {
            MKN_unified_training_time_army_factor = -0.2000
            tooltip = MKN_unified_training_time_army_factor_tt
        }
        add_to_variable = {
            MKN_unified_max_planning = 0.1500
            tooltip = MKN_unified_max_planning_tt
        }
    }
}
```

### Махно идёт на юг — `MKN_makhno_moves_south`

EN: Makhno Moves South.

Описание RU: К морю, к портам, к кораблям, что везут наш хлеб.

Описание EN: To the sea, to the ports, to the ships that carry our grain.

Источник: `common/national_focus/MKN.txt:1154`. Стоимость: 5 (35 дней). Координаты: x=36, y=5.

Предпосылки: (Чёрное знамя на восток [MKN_black_banner_east]).

Взаимоисключения: нет.

Прямые продолжения: MKN_the_steppe_holds.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_makhno_moves_south
    icon = GFX_focus_generic_manpower
    prerequisite = {
        focus = MKN_black_banner_east
    }
    completion_reward = {
        add_manpower = 30000
        add_equipment_to_stockpile = {
            type = infantry_equipment_1
            amount = 3000
            producer = MKN
        }
    }
    x = 36
    y = 5
    cost = 5
}
```

### Отменить выборность командиров — `MKN_abolish_election_of_commanders`

EN: Abolish the Election of Commanders.

Описание RU: Бой не может ждать голосования об отзыве. Упраздним баланс сил и закрепим власть военных в существующей армейской организации: постоянный штаб улучшит планирование и сплочённость.

Описание EN: A battle cannot wait for a recall vote. End the balance of power and fold military authority into our existing army organization: stronger planning and cohesion under a permanent staff.

Источник: `common/national_focus/MKN.txt:6911`. Стоимость: 5 (35 дней). Координаты: x=100, y=5.

Предпосылки: (Арестовать демагогов [MKN_arrest_demagogues]).

Взаимоисключения: нет.

Прямые продолжения: MKN_militarize_communes.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_abolish_election_of_commanders
    x = 100
    y = 5
    completion_reward = {
        MKN_dismantle_bop = yes
        add_to_variable = {
            MKN_army_planning_speed = 0.1
            tooltip = MKN_army_planning_speed_tt
        }
        add_to_variable = {
            MKN_army_army_org_factor = 0.1
            tooltip = MKN_army_army_org_factor_tt
        }
    }
    prerequisite = {
        focus = MKN_arrest_demagogues
    }
    available = {
        NOT = {
            has_country_flag = MKN_crisis_legacy_settled
        }
        has_government = fascism
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    cost = 5
    icon = GFX_focus_MKN_program_militarism_2
}
```

### Упразднить генеральный штаб — `MKN_abolish_general_staff`

EN: Abolish the General Staff.

Описание RU: Штаб станет техническим бюро, подотчётным коммунам. Закрепим полный контроль советов на шкале баланса сил и улучшим взаимодействие местных боевых отрядов.

Описание EN: The staff becomes a technical bureau answerable to the communes. Lock the balance at complete soviet control and improve coordination between local fighting detachments.

Источник: `common/national_focus/MKN.txt:7200`. Стоимость: 5 (35 дней). Координаты: x=106, y=5.

Предпосылки: (Пакт вольных коммун [MKN_pact_of_free_communes]).

Взаимоисключения: нет.

Прямые продолжения: MKN_arms_to_the_people.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_abolish_general_staff
    x = 106
    y = 5
    completion_reward = {
        if = {
            limit = {
                NOT = {
                    has_country_flag = MKN_bop_abandoned
                }
            }
            set_power_balance = {
                id = MKN_power_balance
                set_value = 1
            }
        }
        set_country_flag = MKN_bop_locked
        add_to_variable = {
            MKN_army_land_reinforce_rate = 0.05
            tooltip = MKN_army_land_reinforce_rate_tt
        }
    }
    prerequisite = {
        focus = MKN_pact_of_free_communes
    }
    available = {
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
    icon = GFX_focus_MKN_program_nabat_2
}
```

### Крестьянские милиции — `MKN_peasant_militias`

EN: Peasant Militias.

Описание RU: Каждому селу — свою сотню.

Описание EN: Every village its own sotnya.

Источник: `common/national_focus/MKN.txt:1172`. Стоимость: 5 (35 дней). Координаты: x=32, y=6.

Предпосылки: (Анархистские школы [MKN_anarchist_schools]).

Взаимоисключения: нет.

Прямые продолжения: нет.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_peasant_militias
    icon = GFX_focus_generic_manpower
    prerequisite = {
        focus = MKN_anarchist_schools
    }
    completion_reward = {
        add_manpower = 50000
        add_war_support = 0.05
    }
    x = 32
    y = 6
    cost = 5
}
```

### Милитаризовать коммуны — `MKN_militarize_communes`

EN: Militarize the Communes.

Описание RU: Каждая коммуна будет держать призывной список рядом с зерновой книгой. Расширим набор, заплатив за это новым ударом по доверию общин.

Описание EN: Every commune must keep a muster roll beside its grain ledger. Broaden recruitment, at the price of another wound to communal confidence.

Источник: `common/national_focus/MKN.txt:6943`. Стоимость: 5 (35 дней). Координаты: x=100, y=6.

Предпосылки: (Отменить выборность командиров [MKN_abolish_election_of_commanders]).

Взаимоисключения: нет.

Прямые продолжения: MKN_standardize_workshops.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_militarize_communes
    x = 100
    y = 6
    completion_reward = {
        add_to_variable = {
            MKN_army_conscription = 0.02
            tooltip = MKN_army_conscription_tt
        }
        add_to_variable = {
            MKN_unified_stability_factor = -0.05
            tooltip = MKN_unified_stability_factor_tt
        }
    }
    prerequisite = {
        focus = MKN_abolish_election_of_commanders
    }
    available = {
        NOT = {
            has_country_flag = MKN_crisis_legacy_settled
        }
        has_government = fascism
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    cost = 5
    icon = GFX_focus_MKN_program_militarism_3
}
```

### Оружие народу — `MKN_arms_to_the_people`

EN: Arms to the People.

Описание RU: Выдадим винтовки из общих складов и сформируем три оснащённых отряда коммунальной гвардии. Расширенная система набора сделает каждое село ответственным за свою оборону.

Описание EN: Issue rifles from the common depots and form three equipped commune guards. A broader recruitment system makes each village responsible for its own defense.

Источник: `common/national_focus/MKN.txt:7239`. Стоимость: 5 (35 дней). Координаты: x=106, y=6.

Предпосылки: (Упразднить генеральный штаб [MKN_abolish_general_staff]).

Взаимоисключения: нет.

Прямые продолжения: MKN_propaganda_by_deed.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_arms_to_the_people
    x = 106
    y = 6
    completion_reward = {
        MKN_raise_communal_militias = yes
        add_to_variable = {
            MKN_army_conscription = 0.02
            tooltip = MKN_army_conscription_tt
        }
    }
    prerequisite = {
        focus = MKN_abolish_general_staff
    }
    available = {
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
    icon = GFX_focus_MKN_program_nabat_3
}
```

### Полевые школы коммун — `MKN_field_schools`

EN: Commune Field Schools.

Описание RU: Передвижные инструкторы и сменяемые командиры обучат самооборону связи, маскировке и совместному манёвру. Подготовка станет короче, а отряды сохранят подвижность и связь со своими коммунами.

Описание EN: Travelling instructors and recallable commanders train local defence in signals, concealment and coordinated manoeuvre. Units train faster while retaining their mobility and communal ties.

Источник: `common/national_focus/MKN.txt:885`. Стоимость: 5 (35 дней). Координаты: x=16, y=7.

Предпосылки: (Договор о взаимозаменяемости [MKN_workshop_standards]).

Взаимоисключения: нет.

Прямые продолжения: MKN_communal_compact.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_field_schools
    icon = GFX_focus_generic_army_doctrines_2
    x = 16
    y = 7
    cost = 5
    available_if_capitulated = no
    ai_will_do = {
        factor = 2
    }
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    prerequisite = {
        focus = MKN_workshop_standards
    }
    completion_reward = {
        army_experience = 30
        add_to_variable = {
            MKN_unified_army_org_factor = 0.2000
            tooltip = MKN_unified_army_org_factor_tt
        }
        add_to_variable = {
            MKN_unified_training_time_army_factor = -0.2500
            tooltip = MKN_unified_training_time_army_factor_tt
        }
        add_to_variable = {
            MKN_unified_max_planning = 0.1000
            tooltip = MKN_unified_max_planning_tt
        }
        add_to_variable = {
            MKN_unified_army_speed_factor = 0.0500
            tooltip = MKN_unified_army_speed_factor_tt
        }
    }
}
```

### Чёрный интернационал — `MKN_black_international`

EN: The Black International.

Описание RU: Общее начинание синдикалистов и аграриев после вооружения народа или организации укреплённых хозяйств. Открывает четыре приглашения Чёрного интернационала, повторный набор иностранных добровольцев и поддержку зарубежных революций.

Описание EN: A shared initiative of the syndicalists and agrarians, prepared after arming the people or organizing the fortified farms. Opens the four Black International invitations, repeated recruitment of foreign volunteers and support for overseas revolutions.

Источник: `common/national_focus/MKN.txt:7267`. Стоимость: 5 (35 дней). Координаты: x=109, y=7.

Предпосылки: нет нарисованной предпосылки; см. available.

Взаимоисключения: нет.

Прямые продолжения: нет.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_black_international
    y = 7
    completion_reward = {
        custom_effect_tooltip = MKN_unlock_volunteers_tt
        add_to_variable = {
            MKN_army_send_volunteer_size = 3
            tooltip = MKN_army_send_volunteer_size_tt
        }
        add_to_variable = {
            MKN_army_send_volunteers_tension = -0.5
            tooltip = MKN_army_send_volunteers_tension_tt
        }
        set_rule = {
            can_send_volunteers = yes
        }
        custom_effect_tooltip = MKN_black_international_decisions_unlock_tt
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    cost = 5
    icon = GFX_focus_MKN_program_nabat_4
    x = 109
    available = {
        NOT = {
            has_country_flag = MKN_crisis_legacy_settled
        }
        OR = {
            has_completed_focus = MKN_arms_to_the_people
            has_completed_focus = MKN_every_farm_a_fortress
        }
    }
}
```

### Степные снайперы — `MKN_steppe_snipers`

EN: Steppe Snipers.

Описание RU: Борозда, терпеливый взгляд и один выстрел. Улучшим защиту и разведку, уменьшив преимущество противника от господства в воздухе.

Описание EN: A furrow, a patient eye and one shot. Improve defense and reconnaissance while reducing the enemy’s advantage from air superiority.

Источник: `common/national_focus/MKN.txt:7507`. Стоимость: 5 (35 дней). Координаты: x=112, y=7.

Предпосылки: (Каждый хутор — крепость [MKN_every_farm_a_fortress]).

Взаимоисключения: нет.

Прямые продолжения: MKN_railway_sabotage.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_steppe_snipers
    x = 112
    y = 7
    completion_reward = {
        add_to_variable = {
            MKN_army_army_defence_factor = 0.15
            tooltip = MKN_army_army_defence_factor_tt
        }
        add_to_variable = {
            MKN_army_recon_factor = 0.2
            tooltip = MKN_army_recon_factor_tt
        }
        add_to_variable = {
            MKN_army_enemy_army_bonus_air_superiority_factor = -0.15
            tooltip = MKN_army_enemy_army_bonus_air_superiority_factor_tt
        }
    }
    prerequisite = {
        focus = MKN_every_farm_a_fortress
    }
    available = {
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
    icon = GFX_focus_MKN_program_agrarian_4
}
```

### Красные военные специалисты — `MKN_red_military_specialists`

EN: Red Military Specialists.

Описание RU: Прибывшие инструкторы привезут штатные таблицы, а не проповеди. Улучшим сплочённость и планирование армии, получим опыт и освоение сухопутной доктрины.

Описание EN: The visiting instructors bring tables of organization, not sermons. Improve army cohesion and planning, and gain experience and land doctrine mastery.

Источник: `common/national_focus/MKN.txt:7783`. Стоимость: 5 (35 дней). Координаты: x=118, y=7.

Предпосылки: (Объединить стальные магистрали [MKN_integrate_steel_lines]).

Взаимоисключения: нет.

Прямые продолжения: MKN_tractors_for_grain.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_red_military_specialists
    x = 118
    y = 7
    completion_reward = {
        army_experience = 30
        add_mastery = {
            folder = land
            amount = 100
        }
        add_to_variable = {
            MKN_army_army_org_factor = 0.15
            tooltip = MKN_army_army_org_factor_tt
        }
        add_to_variable = {
            MKN_army_planning_speed = 0.15
            tooltip = MKN_army_planning_speed_tt
        }
    }
    prerequisite = {
        focus = MKN_integrate_steel_lines
    }
    available = {
        NOT = {
            has_country_flag = MKN_crisis_legacy_settled
        }
        has_government = communism
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    cost = 5
    icon = GFX_focus_MKN_program_revkom_4
}
```

### Красный компромисс — `MKN_red_banner_steppe`

EN: The Red Compromise.

Описание RU: При поддержке не менее 40% государственные социалисты создают центральное управление, признавая местные советы. Баланс смещается на 0,35 к советам. Независимая коммунистическая Москва получает предложение об оборонительном союзе, если страны не воюют друг с другом и Вольная территория не состоит в альянсе.

Описание EN: With at least 40% support, state socialists establish a central administration while recognizing local councils. The balance shifts by 0.35 toward the soviets. An independent communist Moscow receives a proposal for a defence pact if neither country is already fighting the other and the Free Territory is outside a faction.

Источник: `common/national_focus/MKN.txt:1604`. Стоимость: 5 (35 дней). Координаты: x=38, y=8.

Предпосылки: (Советская печать [MKN_soviet_press]).

Взаимоисключения: MKN_black_hundreds, MKN_constituent_assembly, MKN_nestor_the_first.

Прямые продолжения: MKN_hand_to_moscow, MKN_collectivize_the_steppe.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_red_banner_steppe
    icon = GFX_focus_generic_army_attack
    completion_reward = {
        set_politics = {
            ruling_party = communism
            elections_allowed = no
        }
        add_manpower = 40000
        create_country_leader = {
            name = "Viktor Belash"
            picture = GFX_Portrait_MKN_viktor_belash
            ideology = leninism
            traits = {

            }
        }
        if = {
            limit = {
                has_power_balance = {
                    id = MKN_power_balance
                }
                NOT = {
                    has_country_flag = MKN_bop_locked
                }
            }
            add_power_balance_value = {
                id = MKN_power_balance
                value = 0.35
                tooltip_side = MKN_free_soviets_side
            }
        }
        if = {
            limit = {
                SOV = {
                    exists = yes
                    has_government = communism
                    is_subject = no
                }
                is_subject = no
                is_in_faction = no
                NOT = {
                    has_war_with = SOV
                }
            }
            set_country_flag = MKN_moscow_request_pending
            SOV = {
                country_event = {
                    id = mkn_bop.1
                    days = 1
                }
            }
        }
    }
    available = {
        has_completed_focus = MKN_soviet_press
        NOT = {
            communism < 0.40
        }
        NOT = {
            OR = {
                has_completed_focus = MKN_everlasting_makhnovshchina
                has_completed_focus = MKN_council_communism
            }
        }
        NOT = {
            has_country_flag = MKN_crisis_enabled
        }
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    x = 38
    y = 8
    prerequisite = {
        focus = MKN_soviet_press
    }
    mutually_exclusive = {
        focus = MKN_black_hundreds
        focus = MKN_constituent_assembly
        focus = MKN_nestor_the_first
    }
    allow_branch = {
        NOT = {
            has_country_flag = MKN_crisis_enabled
        }
    }
    cost = 5
}
```

### Железный кулак на рельсах — `MKN_iron_fist_trains`

EN: The Iron Fist on Rails.

Описание RU: Бронепоезда понесут волю штаба за горизонт. Сохраним культ железных дорог, ускорим изучение поездов и уменьшим потребности армии в снабжении.

Описание EN: Armored trains shall carry the staff’s will beyond the horizon. Preserve the railway cult, accelerate train research and reduce the army’s supply burden.

Источник: `common/national_focus/MKN.txt:7005`. Стоимость: 5 (35 дней). Координаты: x=100, y=8.

Предпосылки: (Стандартизировать мастерские [MKN_standardize_workshops]).

Взаимоисключения: нет.

Прямые продолжения: MKN_black_expansionism.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_iron_fist_trains
    x = 100
    y = 8
    completion_reward = {
        if = {
            limit = {
                NOT = {
                    has_idea = MKN_cult_of_railways
                }
            }
            add_ideas = MKN_cult_of_railways
        }
        add_tech_bonus = {
            bonus = 0.5
            uses = 1
            category = train_tech
        }
        add_to_variable = {
            MKN_army_supply_consumption_factor = -0.05
            tooltip = MKN_army_supply_consumption_factor_tt
        }
    }
    prerequisite = {
        focus = MKN_standardize_workshops
    }
    available = {
        NOT = {
            has_country_flag = MKN_crisis_legacy_settled
        }
        has_government = fascism
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    cost = 5
    icon = GFX_focus_MKN_program_militarism_5
}
```

### Единые боевые приказы — `MKN_order_through_tachanka`

EN: Unified Operational Orders.

Описание RU: Атаманы устанавливают общую цепь командования, смещая баланс ещё на 0,20 к военным.

Описание EN: The atamans establish a common chain of command, shifting the balance another 0.20 toward the military.

Источник: `common/national_focus/MKN.txt:1844`. Стоимость: 5 (35 дней). Координаты: x=29, y=9.

Предпосылки: (Власть атаманов [MKN_black_hundreds]).

Взаимоисключения: нет.

Прямые продолжения: MKN_steppe_legions.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_order_through_tachanka
    icon = GFX_focus_generic_army_tanks2
    prerequisite = {
        focus = MKN_black_hundreds
    }
    completion_reward = {
        army_experience = 30
        add_war_support = 0.05
        if = {
            limit = {
                has_power_balance = {
                    id = MKN_power_balance
                }
                NOT = {
                    has_country_flag = MKN_bop_locked
                }
            }
            add_power_balance_value = {
                id = MKN_power_balance
                value = -0.2
                tooltip_side = MKN_military_command_side
            }
        }
    }
    x = 29
    y = 9
    allow_branch = {
        NOT = {
            has_country_flag = MKN_crisis_enabled
        }
    }
    cost = 5
}
```

### Маяк безгосударственности — `MKN_beacon_of_statelessness`

EN: The Beacon of Statelessness.

Описание RU: Они могут занять станцию, но не сельский сход за ней. Получим ещё 35% к защите национальной территории и 75% к урону вражеским гарнизонам на нашей оккупированной земле.

Описание EN: They may occupy a station, but never the village assembly behind it. Add 35% core defense and 75% damage to enemy garrisons on our occupied soil.

Источник: `common/national_focus/MKN.txt:7356`. Стоимость: 5 (35 дней). Координаты: x=106, y=9.

Предпосылки: (Самоуправляемые железнодорожные бригады [MKN_autonomous_rail_crews]).

Взаимоисключения: нет.

Прямые продолжения: нет.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_beacon_of_statelessness
    icon = GFX_focus_MKN_beacon_of_statelessness
    x = 106
    completion_reward = {
        add_to_variable = {
            MKN_army_army_core_defence_factor = 0.35
            tooltip = MKN_army_army_core_defence_factor_tt
        }
        add_to_variable = {
            MKN_army_resistance_damage_to_garrison_on_our_occupied_states = 0.75
            tooltip = MKN_army_resistance_damage_to_garrison_on_our_occupied_states_tt
        }
    }
    prerequisite = {
        focus = MKN_autonomous_rail_crews
    }
    available = {
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
    y = 9
}
```

### Кавалерийская засада — `MKN_cavalry_ambush`

EN: Cavalry Ambush.

Описание RU: Тачанки ждут за холмом, их лошади тихо стоят во ржи. Добавим общему армейскому духу 30% к атаке кавалерийских и моторизованных батальонов.

Описание EN: Tachankas wait behind the rise, their horses silent in the rye. Add 30% cavalry and motorized battalion attack to the common army spirit.

Источник: `common/national_focus/MKN.txt:7566`. Стоимость: 5 (35 дней). Координаты: x=112, y=9.

Предпосылки: (Железнодорожные диверсии [MKN_railway_sabotage]).

Взаимоисключения: нет.

Прямые продолжения: MKN_impregnable_granary.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_cavalry_ambush
    x = 112
    y = 9
    completion_reward = {
        add_to_variable = {
            MKN_army_modifier_army_sub_unit_cavalry_attack_factor = 0.3
            tooltip = MKN_army_modifier_army_sub_unit_cavalry_attack_factor_tt
        }
        add_to_variable = {
            MKN_army_motorized_attack_factor = 0.3
            tooltip = MKN_army_motorized_attack_factor_tt
        }
    }
    prerequisite = {
        focus = MKN_railway_sabotage
    }
    available = {
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
    icon = GFX_focus_MKN_program_agrarian_6
}
```

### Степные легионы — `MKN_steppe_legions`

EN: The Steppe Legions.

Описание RU: Постоянные соединения заменяют слабо согласованные отряды. Для этого учреждения требуется более 80% контроля командования; баланс смещается ещё на 0,10 к военным.

Описание EN: Permanent formations replace the loosely coordinated detachments. This institution requires more than 80% military control and shifts the balance another 0.10 toward command.

Источник: `common/national_focus/MKN.txt:1878`. Стоимость: 5 (35 дней). Координаты: x=29, y=10.

Предпосылки: (Единые боевые приказы [MKN_order_through_tachanka]).

Взаимоисключения: нет.

Прямые продолжения: MKN_ataman_directorate.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_steppe_legions
    icon = GFX_focus_generic_manpower
    completion_reward = {
        add_manpower = 60000
        add_stability = -0.05
        country_event = {
            id = mkn.20
            days = 1
        }
        remove_ideas = MKN_free_territory
        remove_ideas = MKN_free_soviets_idea
        if = {
            limit = {
                has_power_balance = {
                    id = MKN_power_balance
                }
                NOT = {
                    has_country_flag = MKN_bop_locked
                }
            }
            add_power_balance_value = {
                id = MKN_power_balance
                value = -0.1
                tooltip_side = MKN_military_command_side
            }
        }
        add_to_variable = {
            MKN_army_army_org_factor = 0.05
            tooltip = MKN_army_army_org_factor_tt
        }
        add_to_variable = {
            MKN_army_war_support_factor = 0.1
            tooltip = MKN_army_war_support_factor_tt
        }
        if = {
            limit = {
                NOT = {
                    has_dynamic_modifier = {
                        modifier = MKN_army_development
                    }
                }
            }
            add_dynamic_modifier = {
                modifier = MKN_army_development
            }
        }
    }
    prerequisite = {
        focus = MKN_order_through_tachanka
    }
    x = 29
    y = 10
    available = {
        has_power_balance = {
            id = MKN_power_balance
        }
        power_balance_value = {
            id = MKN_power_balance
            value < -0.6
        }
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    allow_branch = {
        NOT = {
            has_country_flag = MKN_crisis_enabled
        }
    }
    cost = 5
}
```

### Махновская традиция — `MKN_everlasting_makhnovshchina`

EN: The Makhnovist Tradition.

Описание RU: Съезд может вновь пригласить Махно как гражданского делегата без восстановления его военной должности. Добровольная оборона и автономия общин усиливают советы на 0,20.

Описание EN: The congress may invite Makhno back as a civilian delegate, without restoring his military office. Voluntary defence and communal autonomy strengthen the soviets by 0.20.

Источник: `common/national_focus/MKN.txt:1241`. Стоимость: 5 (35 дней). Координаты: x=31, y=10.

Предпосылки: (Отзывные мандаты общин [MKN_free_elections_steppe]).

Взаимоисключения: MKN_council_communism.

Прямые продолжения: MKN_soviets_forever.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_everlasting_makhnovshchina
    icon = GFX_focus_generic_support_the_left_right
    completion_reward = {
        add_war_support = 0.1
        add_manpower = 50000
        army_experience = 20
        set_politics = {
            ruling_party = democratic
            elections_allowed = no
        }
        create_country_leader = {
            name = "Nestor Makhno"
            picture = GFX_Portrait_makhno
            traits = {

            }
            ideology = socialism
        }
        if = {
            limit = {
                has_power_balance = {
                    id = MKN_power_balance
                }
                NOT = {
                    has_country_flag = MKN_bop_locked
                }
            }
            add_power_balance_value = {
                id = MKN_power_balance
                value = 0.2
                tooltip_side = MKN_free_soviets_side
            }
        }
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    x = 31
    y = 10
    prerequisite = {
        focus = MKN_free_elections_steppe
    }
    mutually_exclusive = {
        focus = MKN_council_communism
    }
    available = {
        has_completed_focus = MKN_soviet_press
        NOT = {
            democratic < 0.40
        }
    }
    allow_branch = {
        NOT = {
            has_country_flag = MKN_crisis_enabled
        }
    }
    cost = 5
}
```

### Коллективизировать степь — `MKN_collectivize_the_steppe`

EN: Collectivize the Steppe.

Описание RU: Добровольно. Преимущественно.

Описание EN: Voluntarily. Mostly.

Источник: `common/national_focus/MKN.txt:1737`. Стоимость: 5 (35 дней). Координаты: x=38, y=10.

Предпосылки: (Красный компромисс [MKN_red_banner_steppe]).

Взаимоисключения: нет.

Прямые продолжения: MKN_red_compromise_institutions.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_collectivize_the_steppe
    icon = GFX_focus_generic_manpower
    completion_reward = {
        add_manpower = 60000
        add_stability = 0.05
        country_event = {
            id = mkn.20
            days = 1
        }
        remove_ideas = MKN_free_territory
        remove_ideas = MKN_free_soviets_idea
        if = {
            limit = {
                has_power_balance = {
                    id = MKN_power_balance
                }
                NOT = {
                    has_country_flag = MKN_bop_locked
                }
            }
            add_power_balance_value = {
                id = MKN_power_balance
                value = 0.2
                tooltip_side = MKN_free_soviets_side
            }
        }
        add_to_variable = {
            MKN_unified_industrial_capacity_factory = 0.08
            tooltip = MKN_unified_industrial_capacity_factory_tt
        }
        add_to_variable = {
            MKN_unified_consumer_goods_factor = -0.03
            tooltip = MKN_unified_consumer_goods_factor_tt
        }
    }
    prerequisite = {
        focus = MKN_red_banner_steppe
    }
    x = 38
    y = 10
    allow_branch = {
        NOT = {
            has_country_flag = MKN_crisis_enabled
        }
    }
    cost = 5
}
```

### Оборона крестьянского края — `MKN_steppe_empire`

EN: Defend the Peasant Realm.

Описание RU: Покровительство готовится защищать деревни, не стремясь к внешним завоеваниям. Нестор остаётся монархом, связанным соглашениями крестьянского съезда.

Описание EN: The protectorate prepares to defend its villages without seeking foreign conquest. Nestor remains a monarch, bound by the agreements of the peasant congress.

Источник: `common/national_focus/MKN.txt:2030`. Стоимость: 5 (35 дней). Координаты: x=41, y=10.

Предпосылки: (Императорская коронация [MKN_imperial_coronation]).

Взаимоисключения: нет.

Прямые продолжения: MKN_peasant_charter.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_steppe_empire
    icon = GFX_focus_generic_army_doctrines_2
    completion_reward = {
        army_experience = 25
        add_manpower = 40000
    }
    prerequisite = {
        focus = MKN_imperial_coronation
    }
    x = 41
    y = 10
    allow_branch = {
        NOT = {
            has_country_flag = MKN_crisis_enabled
        }
    }
    cost = 5
}
```

### Чёрная орда — `MKN_the_black_horde`

EN: The Black Horde.

Описание RU: Под чёрным знаменем поднимаются штыки. Армия получит 25% к атаке и 30% к прорыву; независимые соседи вне нашего альянса станут целями аннексии. Штаб обещает свободу в конце каждого похода.

Описание EN: Bayonets rise beneath the black banner. The army gains 25% attack and 30% breakthrough; sovereign neighbors outside our faction become targets for annexation. The staff promises freedom at the end of every march.

Источник: `common/national_focus/MKN.txt:7070`. Стоимость: 5 (35 дней). Координаты: x=100, y=10.

Предпосылки: (Чёрный экспансионизм [MKN_black_expansionism]).

Взаимоисключения: нет.

Прямые продолжения: нет.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_the_black_horde
    icon = GFX_focus_MKN_the_black_horde
    x = 100
    y = 10
    completion_reward = {
        add_to_variable = {
            MKN_army_army_attack_factor = 0.25
            tooltip = MKN_army_army_attack_factor_tt
        }
        add_to_variable = {
            MKN_army_breakthrough_factor = 0.3
            tooltip = MKN_army_breakthrough_factor_tt
        }
        every_neighbor_country = {
            limit = {
                is_subject = no
                NOT = {
                    original_tag = MKN
                }
                NOT = {
                    is_in_faction_with = ROOT
                }
                NOT = {
                    has_war_with = ROOT
                }
            }
            ROOT = {
                create_wargoal = {
                    type = annex_everything
                    target = PREV
                }
            }
        }
    }
    prerequisite = {
        focus = MKN_black_expansionism
    }
    available = {
        NOT = {
            has_country_flag = MKN_crisis_legacy_settled
        }
        has_government = fascism
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    cost = 5
}
```

### Неприступная житница — `MKN_impregnable_granary`

EN: The Impregnable Granary.

Описание RU: Захватчику не достанется лёгкой жатвы. Получим ещё 50% к защите национальной территории и увеличим вражеские потери от истощения на нашей земле на 40%.

Описание EN: There will be no easy harvest for an invader. Add 50% core defense and impose 40% additional hostile attrition in our territory.

Источник: `common/national_focus/MKN.txt:7597`. Стоимость: 5 (35 дней). Координаты: x=112, y=10.

Предпосылки: (Кавалерийская засада [MKN_cavalry_ambush]).

Взаимоисключения: нет.

Прямые продолжения: нет.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_impregnable_granary
    icon = GFX_focus_MKN_impregnable_granary
    x = 112
    y = 10
    completion_reward = {
        add_to_variable = {
            MKN_army_army_core_defence_factor = 0.5
            tooltip = MKN_army_army_core_defence_factor_tt
        }
        add_to_variable = {
            MKN_army_enemy_attrition = 0.4
            tooltip = MKN_army_enemy_attrition_tt
        }
    }
    prerequisite = {
        focus = MKN_cavalry_ambush
    }
    available = {
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
}
```

### Директория атаманов — `MKN_ataman_directorate`

EN: The Ataman Directorate.

Описание RU: Директория учреждает постоянный совет командования. Требуется более 80% военного контроля; политические решения сохраняют возможность изменять баланс.

Описание EN: The directorate establishes a permanent command council. It requires more than 80% military control; the balance remains adjustable through political decisions.

Источник: `common/national_focus/MKN.txt:6631`. Стоимость: 5 (35 дней). Координаты: x=29, y=11.

Предпосылки: (Степные легионы [MKN_steppe_legions]).

Взаимоисключения: нет.

Прямые продолжения: нет.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_ataman_directorate
    icon = GFX_focus_generic_army_doctrines_2
    x = 29
    y = 11
    prerequisite = {
        focus = MKN_steppe_legions
    }
    available = {
        has_power_balance = {
            id = MKN_power_balance
        }
        power_balance_value = {
            id = MKN_power_balance
            value < -0.6
        }
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    completion_reward = {
        add_war_support = 0.05
        add_political_power = 50
        add_to_variable = {
            MKN_army_planning_speed = 0.05
            tooltip = MKN_army_planning_speed_tt
        }
        if = {
            limit = {
                NOT = {
                    has_dynamic_modifier = {
                        modifier = MKN_army_development
                    }
                }
            }
            add_dynamic_modifier = {
                modifier = MKN_army_development
            }
        }
    }
    allow_branch = {
        NOT = {
            has_country_flag = MKN_crisis_enabled
        }
    }
    cost = 5
}
```

### Тачаночная гвардия — `MKN_tachanka_guards`

EN: Tachanka Guards.

Описание RU: Элита Повстанческой армии.

Описание EN: The elite of the Insurgent Army.

Источник: `common/national_focus/MKN.txt:1332`. Стоимость: 5 (35 дней). Координаты: x=31, y=12.

Предпосылки: (Советы навсегда [MKN_soviets_forever]).

Взаимоисключения: нет.

Прямые продолжения: MKN_recallable_delegates.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_tachanka_guards
    icon = GFX_focus_generic_army_attack
    completion_reward = {
        army_experience = 30
        add_equipment_to_stockpile = {
            type = motorized_equipment_1
            amount = 300
            producer = MKN
        }
    }
    prerequisite = {
        focus = MKN_soviets_forever
    }
    x = 31
    y = 12
    allow_branch = {
        NOT = {
            has_country_flag = MKN_crisis_enabled
        }
    }
    cost = 5
}
```

### Федерация коммун — `MKN_commune_federation`

EN: Commune Federation.

Описание RU: Тысяча коммун — одна федерация.

Описание EN: A thousand communes, one federation.

Источник: `common/national_focus/MKN.txt:1447`. Стоимость: 5 (35 дней). Координаты: x=35, y=12.

Предпосылки: (Рабочий контроль [MKN_workers_control]).

Взаимоисключения: нет.

Прямые продолжения: MKN_recallable_delegates.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_commune_federation
    icon = GFX_focus_generic_diplomatic_treaty
    completion_reward = {
        add_manpower = 40000
        add_war_support = 0.05
        country_event = {
            id = mkn.20
            days = 1
        }
        remove_ideas = MKN_free_territory
        add_ideas = MKN_free_soviets_idea
        add_to_variable = {
            MKN_unified_stability_factor = 0.05
            tooltip = MKN_unified_stability_factor_tt
        }
        add_to_variable = {
            MKN_unified_production_speed_buildings_factor = 0.05
            tooltip = MKN_unified_production_speed_buildings_factor_tt
        }
    }
    prerequisite = {
        focus = MKN_workers_control
    }
    x = 35
    y = 12
    allow_branch = {
        NOT = {
            has_country_flag = MKN_crisis_enabled
        }
    }
    cost = 5
}
```

## Контекст предпосылок

### Днепрострой — `MKN_dneprostroi`

EN: Dnieper Industrial Program.

Описание RU: Коммуны поручат общему совету крупные стройки, оставив сметы открытыми делегатам. Единый план свяжет металлургию, энергетику и транспорт; путь вольных кооперативов станет недоступен.

Описание EN: Open accounts and elected delegates will oversee a common plan for heavy industry, power and transport. This choice excludes the free cooperatives.

Источник: `common/national_focus/MKN.txt:12`. Стоимость: 5 (35 дней). Координаты: x=4, y=0.

Предпосылки: нет нарисованной предпосылки; см. available.

Взаимоисключения: MKN_free_cooperatives.

Прямые продолжения: MKN_dnieper_audit.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_dneprostroi
    icon = GFX_focus_generic_hydroelectric_energy
    x = 4
    y = 0
    cost = 5
    available_if_capitulated = no
    ai_will_do = {
        factor = 2
    }
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    mutually_exclusive = {
        focus = MKN_free_cooperatives
    }
    completion_reward = {
        add_political_power = 50
        add_to_variable = {
            MKN_unified_political_power_gain = 0.1000
            tooltip = MKN_unified_political_power_gain_tt
        }
        add_to_variable = {
            MKN_unified_consumer_goods_factor = -0.0500
            tooltip = MKN_unified_consumer_goods_factor_tt
        }
        add_to_variable = {
            MKN_unified_production_speed_buildings_factor = 0.0500
            tooltip = MKN_unified_production_speed_buildings_factor_tt
        }
        add_to_variable = {
            MKN_unified_industrial_capacity_factory = 0.0500
            tooltip = MKN_unified_industrial_capacity_factory_tt
        }
    }
}
```

### Вольные кооперативы — `MKN_free_cooperatives`

EN: Free Cooperatives.

Описание RU: Артели сохранят самостоятельность и примут взаимные обязательства по снабжению и заказам. Хозяйственный кризис ослабнет; централизованный путь Днепростроя станет недоступен.

Описание EN: Independent artels accept mutual supply and production obligations. The economic crisis eases; this choice excludes the Dnieper industrial program.

Источник: `common/national_focus/MKN.txt:519`. Стоимость: 5 (35 дней). Координаты: x=16, y=0.

Предпосылки: нет нарисованной предпосылки; см. available.

Взаимоисключения: MKN_dneprostroi.

Прямые продолжения: MKN_artel_register.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_free_cooperatives
    icon = GFX_focus_generic_agricultural_subsidies
    x = 16
    y = 0
    cost = 5
    available_if_capitulated = no
    ai_will_do = {
        factor = 2
    }
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    mutually_exclusive = {
        focus = MKN_dneprostroi
    }
    completion_reward = {
        add_political_power = 50
        add_to_variable = {
            MKN_unified_political_power_gain = 0.1000
            tooltip = MKN_unified_political_power_gain_tt
        }
        add_to_variable = {
            MKN_unified_consumer_goods_factor = -0.0500
            tooltip = MKN_unified_consumer_goods_factor_tt
        }
        add_to_variable = {
            MKN_unified_production_speed_buildings_factor = 0.0500
            tooltip = MKN_unified_production_speed_buildings_factor_tt
        }
        add_to_variable = {
            MKN_unified_industrial_capacity_factory = 0.0500
            tooltip = MKN_unified_industrial_capacity_factory_tt
        }
    }
}
```

### Съезд 1936 года — `MKN_congress_1936`

EN: The Congress of 1936.

Описание RU: В зале пахнет мокрыми шинелями и типографской краской. Махно ещё способен заставить его замолчать одним взглядом, но никто не верит, что это будет длиться вечно. Дадим делегатам мандат и вынесем спор штаба Тратишова с советами Волина на съезд.

Описание EN: The hall smells of wet greatcoats and printer’s ink. Makhno can still silence it with a glance, but no one believes that he can do so forever. Give the delegates a mandate and bring the struggle between Tratishov’s staff and Volin’s soviets into the open.

Источник: `common/national_focus/MKN.txt:6591`. Стоимость: 5 (35 дней). Координаты: x=108, y=0.

Предпосылки: нет нарисованной предпосылки; см. available.

Взаимоисключения: нет.

Прямые продолжения: MKN_departure_of_batko, MKN_question_of_supply, MKN_question_of_discipline.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_congress_1936
    icon = GFX_focus_generic_support_the_left_right
    y = 0
    x = 108
    completion_reward = {
        add_political_power = 100
        if = {
            limit = {
                NOT = {
                    has_country_flag = MKN_bop_abandoned
                }
            }
            set_power_balance = {
                id = MKN_power_balance
                set_value = 0
            }
        }
    }
    ai_will_do = {
        factor = 20
    }
    cost = 5
}
```

### Съезд украинских коммун — `MKN_ukrainian_communes_congress`

EN: Congress of Ukrainian Communes.

Описание RU: Война закончилась, но власть над областями ещё не стала общим договором. Созовём делегатов всех бывших украинских земель и определим порядок добровольного самоуправления.

Описание EN: The war is over, but ownership has yet to become a shared compact. Delegates from the former Ukrainian lands will define local self-government.

Источник: `common/national_focus/MKN_ukraine_integration_focuses.txt:3`. Стоимость: 5 (35 дней). Координаты: x=146, y=0.

Предпосылки: нет нарисованной предпосылки; см. available.

Взаимоисключения: нет.

Прямые продолжения: MKN_southern_commune_charters, MKN_right_bank_councils, MKN_northern_delegates.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_ukrainian_communes_congress
    icon = GFX_focus_generic_conference
    x = 146
    y = 0
    cost = 5
    available_if_capitulated = no
    cancel_if_invalid = yes
    continue_if_invalid = no
    available = {
        MKN_ukraine_integration_ready = yes
    }
    search_filters = {
        FOCUS_FILTER_POLITICAL
        FOCUS_FILTER_INDUSTRY
    }
    ai_will_do = {
        factor = 5
    }
    completion_reward = {
        add_political_power = 100
        add_stability = 0.05
    }
    allow_branch = {
        has_country_flag = MKN_ukraine_integration_unlocked
    }
}
```

### Открытые сметы Днепростроя — `MKN_dnieper_audit`

EN: Open Accounts of the Dnieper Program.

Описание RU: Инженеры ответят перед хозяйственным съездом за каждую машину и рабочую смену. Учреждаем проектное бюро и новую фабрику; делегаты выберут строительный сезон или бережливое переоснащение на один год.

Описание EN: Engineers will answer to the congress for every machine and shift. A design office and civilian factory support recovery; delegates choose a year of accelerated construction or careful investment.

Источник: `common/national_focus/MKN.txt:48`. Стоимость: 5 (35 дней). Координаты: x=4, y=1.

Предпосылки: (Днепрострой [MKN_dneprostroi]).

Взаимоисключения: нет.

Прямые продолжения: MKN_southern_resources.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_dnieper_audit
    icon = GFX_focus_generic_money_for_equipment
    x = 4
    y = 1
    cost = 5
    available_if_capitulated = no
    ai_will_do = {
        factor = 2
    }
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    prerequisite = {
        focus = MKN_dneprostroi
    }
    completion_reward = {
        country_event = {
            id = mkn.30
            days = 1
        }
        add_tech_bonus = {
            bonus = 0.5
            uses = 1
            category = industry
        }
        random_owned_controlled_state = {
            limit = {
                is_core_of = ROOT
            }
            prioritize = {
                1082
                200
                196
            }
            add_extra_state_shared_building_slots = 1
            add_building_construction = {
                type = industrial_complex
                level = 1
                instant_build = yes
            }
        }
        add_to_variable = {
            MKN_unified_industrial_capacity_factory = 0.0500
            tooltip = MKN_unified_industrial_capacity_factory_tt
        }
        add_to_variable = {
            MKN_unified_production_factory_efficiency_gain_factor = 0.1000
            tooltip = MKN_unified_production_factory_efficiency_gain_factor_tt
        }
        add_to_variable = {
            MKN_unified_research_speed_factor = 0.0500
            tooltip = MKN_unified_research_speed_factor_tt
        }
    }
}
```

### Реестр взаимных обязательств — `MKN_artel_register`

EN: Register of Mutual Obligations.

Описание RU: Артели запишут свои запасы, инструменты и обещания соседям. Хозяйственный конгресс получит право оплачивать соляные промыслы, ветряки, обучение командиров, хлебную политику и взаимное страхование.

Описание EN: Artels record their stocks, tools and promises. The Economic Congress can fund salt workings, windmills, elected commanders, grain policy and mutual insurance.

Источник: `common/national_focus/MKN.txt:555`. Стоимость: 5 (35 дней). Координаты: x=16, y=1.

Предпосылки: (Вольные кооперативы [MKN_free_cooperatives]).

Взаимоисключения: нет.

Прямые продолжения: MKN_steppe_markets.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_artel_register
    icon = GFX_focus_generic_money_for_equipment
    x = 16
    y = 1
    cost = 5
    available_if_capitulated = no
    ai_will_do = {
        factor = 2
    }
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    prerequisite = {
        focus = MKN_free_cooperatives
    }
    completion_reward = {
        add_political_power = 50
        custom_effect_tooltip = MKN_economic_congress_unlock_tt
        add_to_variable = {
            MKN_unified_industrial_capacity_factory = 0.0500
            tooltip = MKN_unified_industrial_capacity_factory_tt
        }
    }
}
```

### Технические коммуны — `MKN_technical_communes`

EN: Technical Communes.

Описание RU: Учёные и мастера создадут общую сеть технических школ, доступную при любой форме хозяйства.

Описание EN: Scientists and craftsmen establish a technical school network under either economic model.

Источник: `common/national_focus/MKN.txt:6519`. Стоимость: 5 (35 дней). Координаты: x=27, y=1.

Предпосылки: нет нарисованной предпосылки; см. available.

Взаимоисключения: нет.

Прямые продолжения: MKN_workshop_airplane_artels, MKN_polytechnic_institute.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_technical_communes
    icon = GFX_focus_research
    completion_reward = {
        add_tech_bonus = {
            bonus = 0.5
            uses = 2
            category = electronics
        }
        add_political_power = 50
    }
    x = 27
    y = 1
    cost = 5
}
```

### Вопрос снабжения — `MKN_question_of_supply`

EN: The Question of Supply.

Описание RU: Винтовку не накормишь резолюцией. Коммуны проверят запасы зерна, боеприпасов и железнодорожные поставки; вольные советы усилят влияние на общее военное дело.

Описание EN: A rifle cannot eat a resolution. Let the communes audit grain, ammunition and rail deliveries; the free soviets gain influence over the common war effort.

Источник: `common/national_focus/MKN.txt:6770`. Стоимость: 5 (35 дней). Координаты: x=106, y=1.

Предпосылки: (Съезд 1936 года [MKN_congress_1936]).

Взаимоисключения: нет.

Прямые продолжения: нет.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_question_of_supply
    icon = GFX_focus_generic_railroad
    x = 106
    y = 1
    completion_reward = {
        if = {
            limit = {
                has_power_balance = {
                    id = MKN_power_balance
                }
            }
            add_power_balance_value = {
                id = MKN_power_balance
                value = 0.15
                tooltip_side = MKN_free_soviets_side
            }
        }
        add_political_power = 50
    }
    prerequisite = {
        focus = MKN_congress_1936
    }
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    cost = 5
}
```

### Вопрос дисциплины — `MKN_question_of_discipline`

EN: The Question of Discipline.

Описание RU: Приказы умирают на пути из зала съезда в окопы. Штаб согласует движение колонн и работу складов, даже если делегаты назовут это первым камнем нового государства.

Описание EN: Orders die between the congress hall and the trenches. Let the staff coordinate marching columns and reserve depots, even if the delegates call that the first stone of a new state.

Источник: `common/national_focus/MKN.txt:6798`. Стоимость: 5 (35 дней). Координаты: x=110, y=1.

Предпосылки: (Съезд 1936 года [MKN_congress_1936]).

Взаимоисключения: нет.

Прямые продолжения: нет.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_question_of_discipline
    icon = GFX_focus_generic_army_doctrines_2
    x = 110
    y = 1
    completion_reward = {
        if = {
            limit = {
                has_power_balance = {
                    id = MKN_power_balance
                }
            }
            add_power_balance_value = {
                id = MKN_power_balance
                value = -0.15
                tooltip_side = MKN_military_command_side
            }
        }
        add_political_power = 50
    }
    prerequisite = {
        focus = MKN_congress_1936
    }
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    cost = 5
}
```

### Ресурсная база Юга — `MKN_southern_resources`

EN: Resource Base of the South.

Описание RU: Никопольский марганец и угольные промыслы войдут в общий договор поставок. Сырьё останется достоянием коммун, а заводы получат устойчивую основу для больших серий.

Описание EN: Nikopol manganese and the southern coal workings will enter a common supply agreement, providing the raw materials for large production runs.

Источник: `common/national_focus/MKN.txt:104`. Стоимость: 5 (35 дней). Координаты: x=4, y=2.

Предпосылки: (Открытые сметы Днепростроя [MKN_dnieper_audit]).

Взаимоисключения: нет.

Прямые продолжения: MKN_steppe_industrial_giants.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_southern_resources
    icon = GFX_focus_generic_mining_industry
    x = 4
    y = 2
    cost = 5
    available_if_capitulated = no
    ai_will_do = {
        factor = 2
    }
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    prerequisite = {
        focus = MKN_dnieper_audit
    }
    completion_reward = {
        add_political_power = 50
        226 = {
            if = {
                limit = {
                    is_owned_and_controlled_by = ROOT
                }
                add_resource = {
                    type = steel
                    amount = 15
                }
            }
        }
        226 = {
            if = {
                limit = {
                    is_owned_and_controlled_by = ROOT
                }
                add_resource = {
                    type = coal
                    amount = 12
                }
            }
        }
        add_tech_bonus = {
            bonus = 0.5
            uses = 1
            category = excavation_tech
        }
    }
}
```

### Степные рынки — `MKN_steppe_markets`

EN: Steppe Markets.

Описание RU: Базары, монетный двор и кредитные кассы примут общий расчёт без ростовщичества. Две фабрики и устойчивый политический доход закрепят доверие к договорам между коммунами.

Описание EN: Bazaars, the mint and mutual credit funds agree on common settlement without usury. Two civilian factories and a lasting political income strengthen confidence between communes.

Источник: `common/national_focus/MKN.txt:580`. Стоимость: 5 (35 дней). Координаты: x=16, y=2.

Предпосылки: (Реестр взаимных обязательств [MKN_artel_register]).

Взаимоисключения: нет.

Прямые продолжения: MKN_mobile_workshops.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_steppe_markets
    icon = GFX_focus_generic_money_for_equipment
    x = 16
    y = 2
    cost = 5
    available_if_capitulated = no
    ai_will_do = {
        factor = 2
    }
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    prerequisite = {
        focus = MKN_artel_register
    }
    completion_reward = {
        add_political_power = 150
        add_stability = 0.10
        random_owned_controlled_state = {
            limit = {
                is_core_of = ROOT
            }
            prioritize = {
                1082
                200
                196
            }
            add_extra_state_shared_building_slots = 2
            add_building_construction = {
                type = industrial_complex
                level = 2
                instant_build = yes
            }
        }
        add_to_variable = {
            MKN_unified_political_power_gain = 0.2000
            tooltip = MKN_unified_political_power_gain_tt
        }
    }
}
```

### Вольная территория — `MKN_the_free_territory`

EN: The Free Territory.

Описание RU: Ни господ, ни государств — только вольные советы крестьян и рабочих.

Описание EN: No masters, no states - only free soviets of peasants and workers.

Источник: `common/national_focus/MKN.txt:1010`. Стоимость: 5 (35 дней). Координаты: x=34, y=2.

Предпосылки: нет нарисованной предпосылки; см. available.

Взаимоисключения: нет.

Прямые продолжения: MKN_farmers_and_workers, MKN_free_soviets, MKN_nabat_federation.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_the_free_territory
    icon = GFX_focus_generic_support_the_left_right
    completion_reward = {
        add_political_power = 100
        add_stability = 0.05
    }
    x = 34
    y = 2
    available = {
        has_completed_focus = MKN_congress_1936
    }
    cost = 5
}
```

### Уход Батько — `MKN_departure_of_batko`

EN: The Departure of the Batko.

Описание RU: Этот фокус завершается событием смерти Махно. Его гроб закрывает эпоху, но не спор. У нас 180 дней на решение вопроса о преемственности, прежде чем степь расколется на вооружённые лагеря.

Описание EN: This focus is completed by Makhno’s death event. His coffin closes an age, not an argument. There are 180 days to settle the succession before the steppe splits into armed camps.

Источник: `common/national_focus/MKN.txt:6615`. Стоимость: 5 (35 дней). Координаты: x=108, y=2.

Предпосылки: (Съезд 1936 года [MKN_congress_1936]).

Взаимоисключения: нет.

Прямые продолжения: MKN_military_takes_charge, MKN_triumph_of_free_soviets, MKN_peasant_delegates, MKN_emergency_revkom.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_departure_of_batko
    prerequisite = {
        focus = MKN_congress_1936
    }
    x = 108
    y = 2
    icon = GFX_focus_MKN_departure_of_batko
    available = {
        always = no
    }
    completion_reward = {

    }
    cost = 5
}
```

### Индустриальные гиганты степи — `MKN_steppe_industrial_giants`

EN: Industrial Giants of the Steppe.

Описание RU: «Коммунар», трубные мастерские и алюминиевое производство объединят заказы и инженерные кадры. Новые корпуса дадут фабрику и три военных завода, а собственный алюминий обеспечит машиностроение.

Описание EN: Kommunar, the tube works and aluminium plants pool their orders and engineers. One civilian factory, three military factories and aluminium supplies restore large-scale manufacturing.

Источник: `common/national_focus/MKN.txt:151`. Стоимость: 10 (70 дней). Координаты: x=4, y=3.

Предпосылки: (Ресурсная база Юга [MKN_southern_resources]).

Взаимоисключения: нет.

Прямые продолжения: MKN_zaporizhstal.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_steppe_industrial_giants
    icon = GFX_focus_generic_military_industry
    x = 4
    y = 3
    cost = 10
    available_if_capitulated = no
    ai_will_do = {
        factor = 2
    }
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    prerequisite = {
        focus = MKN_southern_resources
    }
    completion_reward = {
        226 = {
            if = {
                limit = {
                    is_owned_and_controlled_by = ROOT
                }
                add_extra_state_shared_building_slots = 4
                add_building_construction = {
                    type = industrial_complex
                    level = 1
                    instant_build = yes
                }
                add_building_construction = {
                    type = arms_factory
                    level = 3
                    instant_build = yes
                }
            }
        }
        226 = {
            if = {
                limit = {
                    is_owned_and_controlled_by = ROOT
                }
                add_resource = {
                    type = aluminium
                    amount = 8
                }
            }
        }
        add_tech_bonus = {
            bonus = 0.5
            uses = 1
            category = air_equipment
        }
        add_to_variable = {
            MKN_unified_industrial_capacity_factory = 0.1000
            tooltip = MKN_unified_industrial_capacity_factory_tt
        }
        add_to_variable = {
            MKN_unified_production_factory_efficiency_gain_factor = 0.0500
            tooltip = MKN_unified_production_factory_efficiency_gain_factor_tt
        }
    }
}
```

### Крестьяне и рабочие — `MKN_farmers_and_workers`

EN: Farmers and Workers.

Описание RU: Вольная территория держится на руках труда, а не на коронах старого мира.

Описание EN: The Free Territory stands on the hands that labor, not on the crowns of the old world.

Источник: `common/national_focus/MKN.txt:1024`. Стоимость: 5 (35 дней). Координаты: x=32, y=3.

Предпосылки: (Вольная территория [MKN_the_free_territory]).

Взаимоисключения: нет.

Прямые продолжения: MKN_shadow_republic.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_farmers_and_workers
    icon = GFX_focus_generic_support_the_left_right
    prerequisite = {
        focus = MKN_the_free_territory
    }
    completion_reward = {
        add_political_power = 80
        add_stability = 0.05
    }
    x = 32
    y = 3
    cost = 5
}
```

### Вольные советы — `MKN_free_soviets`

EN: Free Soviets.

Описание RU: Каждому селу — свою коммуну, каждой коммуне — свой голос.

Описание EN: Every village its own commune, every commune its own voice.

Источник: `common/national_focus/MKN.txt:1038`. Стоимость: 5 (35 дней). Координаты: x=34, y=3.

Предпосылки: (Вольная территория [MKN_the_free_territory]).

Взаимоисключения: нет.

Прямые продолжения: MKN_gulyai_polye_commune.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_free_soviets
    icon = GFX_focus_generic_diplomatic_treaty
    prerequisite = {
        focus = MKN_the_free_territory
    }
    completion_reward = {
        swap_ideas = {
            remove_idea = MKN_free_territory
            add_idea = MKN_free_soviets_idea
        }
        add_stability = 0.05
        add_war_support = 0.05
    }
    x = 34
    y = 3
    cost = 5
}
```

### Федерация «Набат» — `MKN_nabat_federation`

EN: The Nabat Federation.

Описание RU: Анархистские федерации от Харькова до Одессы смотрят на Гуляй-Поле.

Описание EN: Anarchist federations from Kharkov to Odessa look to Gulyai-Polye.

Источник: `common/national_focus/MKN.txt:1056`. Стоимость: 5 (35 дней). Координаты: x=36, y=3.

Предпосылки: (Вольная территория [MKN_the_free_territory]).

Взаимоисключения: нет.

Прямые продолжения: MKN_black_banner_east.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_nabat_federation
    icon = GFX_focus_research
    prerequisite = {
        focus = MKN_the_free_territory
    }
    completion_reward = {
        add_political_power = 80
        add_tech_bonus = {
            bonus = 0.5
            uses = 1
            category = industry
        }
    }
    x = 36
    y = 3
    cost = 5
}
```

### Военные берут власть — `MKN_military_takes_charge`

EN: The Military Takes Charge.

Описание RU: Тратишов расстилает железнодорожную карту на столе съезда. Революции нужно единое оперативное командование. При поддержке не менее 40% населения и подготовленном съезде правящей программой станет анархо-милитаризм.

Описание EN: Tratishov spreads a railway map over the congress table. The revolution needs a single operational command. With at least 40% public support and a prepared congress, anarcho-militarism becomes the ruling program.

Источник: `common/national_focus/MKN.txt:6826`. Стоимость: 5 (35 дней). Координаты: x=100, y=3.

Предпосылки: (Уход Батько [MKN_departure_of_batko]).

Взаимоисключения: MKN_triumph_of_free_soviets, MKN_peasant_delegates, MKN_emergency_revkom.

Прямые продолжения: MKN_arrest_demagogues.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_military_takes_charge
    x = 100
    y = 3
    completion_reward = {
        set_politics = {
            ruling_party = fascism
            elections_allowed = no
        }
        add_stability = -0.05
        if = {
            limit = {
                has_power_balance = {
                    id = MKN_power_balance
                }
            }
            add_power_balance_value = {
                id = MKN_power_balance
                value = -0.35
                tooltip_side = MKN_military_command_side
            }
        }
        remove_ideas = MKN_revkom_terror
    }
    prerequisite = {
        focus = MKN_departure_of_batko
    }
    available = {
        NOT = {
            has_country_flag = MKN_crisis_legacy_settled
        }
        has_completed_focus = MKN_congress_1936
        OR = {
            has_completed_focus = MKN_question_of_supply
            has_completed_focus = MKN_question_of_discipline
        }
        NOT = {
            fascism < 0.40
        }
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    mutually_exclusive = {
        focus = MKN_triumph_of_free_soviets
        focus = MKN_peasant_delegates
        focus = MKN_emergency_revkom
    }
    ai_will_do = {
        factor = 10
    }
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    cost = 5
    icon = GFX_focus_MKN_militarism
}
```

### Торжество вольных советов — `MKN_triumph_of_free_soviets`

EN: The Triumph of the Free Soviets.

Описание RU: Волин спрашивает делегатов, кто дал штабу право править. При подготовленном съезде и поддержке не менее 40% анархо-коммунизм станет правящей программой местных советов с отзывными делегатами.

Описание EN: Volin asks the delegates who gave a staff the right to govern. With a prepared congress and at least 40% support, anarcho-communism becomes the ruling program of recallable local councils.

Источник: `common/national_focus/MKN.txt:7121`. Стоимость: 5 (35 дней). Координаты: x=106, y=3.

Предпосылки: (Уход Батько [MKN_departure_of_batko]).

Взаимоисключения: MKN_military_takes_charge, MKN_peasant_delegates, MKN_emergency_revkom.

Прямые продолжения: MKN_pact_of_free_communes.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_triumph_of_free_soviets
    x = 106
    y = 3
    completion_reward = {
        set_politics = {
            ruling_party = democratic
            elections_allowed = no
        }
        add_stability = -0.05
        if = {
            limit = {
                has_power_balance = {
                    id = MKN_power_balance
                }
            }
            add_power_balance_value = {
                id = MKN_power_balance
                value = 0.35
                tooltip_side = MKN_free_soviets_side
            }
        }
        remove_ideas = MKN_revkom_terror
    }
    prerequisite = {
        focus = MKN_departure_of_batko
    }
    available = {
        NOT = {
            has_country_flag = MKN_crisis_legacy_settled
        }
        has_completed_focus = MKN_congress_1936
        OR = {
            has_completed_focus = MKN_question_of_supply
            has_completed_focus = MKN_question_of_discipline
        }
        NOT = {
            democratic < 0.40
        }
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    mutually_exclusive = {
        focus = MKN_military_takes_charge
        focus = MKN_peasant_delegates
        focus = MKN_emergency_revkom
    }
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    cost = 5
    icon = GFX_focus_MKN_nabat
}
```

### Крестьянские делегаты — `MKN_peasant_delegates`

EN: The Peasant Delegates.

Описание RU: Новая корона не заменит шапку Батько. Избранный совет сёл возьмёт на себя ответственность за житницу. Аграрный изоляционизм требует подготовленного съезда и поддержки не менее 40%.

Описание EN: No new crown shall replace the Batko’s hat. An elected council of villages takes responsibility for the granary. Agrarian isolationism requires a prepared congress and at least 40% support.

Источник: `common/national_focus/MKN.txt:7387`. Стоимость: 5 (35 дней). Координаты: x=112, y=3.

Предпосылки: (Уход Батько [MKN_departure_of_batko]).

Взаимоисключения: MKN_military_takes_charge, MKN_triumph_of_free_soviets, MKN_emergency_revkom.

Прямые продолжения: MKN_grain_ultimatum.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_peasant_delegates
    x = 112
    y = 3
    completion_reward = {
        set_politics = {
            ruling_party = neutrality
            elections_allowed = no
        }
        add_stability = -0.05
        remove_ideas = MKN_revkom_terror
    }
    prerequisite = {
        focus = MKN_departure_of_batko
    }
    available = {
        NOT = {
            has_country_flag = MKN_crisis_legacy_settled
        }
        has_completed_focus = MKN_congress_1936
        OR = {
            has_completed_focus = MKN_question_of_supply
            has_completed_focus = MKN_question_of_discipline
        }
        NOT = {
            neutrality < 0.40
        }
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    mutually_exclusive = {
        focus = MKN_military_takes_charge
        focus = MKN_triumph_of_free_soviets
        focus = MKN_emergency_revkom
    }
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    cost = 5
    icon = GFX_focus_MKN_agrarian
}
```

### Чрезвычайный ревком — `MKN_emergency_revkom`

EN: The Emergency Revkom.

Описание RU: Красные делегаты требуют администрации, способной пережить своего основателя. При подготовленном съезде и поддержке не менее 40% государственный социализм станет правящей программой.

Описание EN: The red delegates demand an administration that can survive its founder. With a prepared congress and at least 40% support, state socialism becomes the ruling program.

Источник: `common/national_focus/MKN.txt:7628`. Стоимость: 5 (35 дней). Координаты: x=118, y=3.

Предпосылки: (Уход Батько [MKN_departure_of_batko]).

Взаимоисключения: MKN_military_takes_charge, MKN_triumph_of_free_soviets, MKN_peasant_delegates.

Прямые продолжения: MKN_purge_irreconcilables.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_emergency_revkom
    x = 118
    y = 3
    completion_reward = {
        set_politics = {
            ruling_party = communism
            elections_allowed = no
        }
        add_stability = -0.05
        add_ideas = MKN_revkom_terror
    }
    prerequisite = {
        focus = MKN_departure_of_batko
    }
    available = {
        NOT = {
            has_country_flag = MKN_crisis_legacy_settled
        }
        has_completed_focus = MKN_congress_1936
        OR = {
            has_completed_focus = MKN_question_of_supply
            has_completed_focus = MKN_question_of_discipline
        }
        NOT = {
            communism < 0.40
        }
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    mutually_exclusive = {
        focus = MKN_military_takes_charge
        focus = MKN_triumph_of_free_soviets
        focus = MKN_peasant_delegates
    }
    ai_will_do = {
        factor = 10
    }
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    cost = 5
    icon = GFX_focus_MKN_revkom
}
```

### Запорожсталь — `MKN_zaporizhstal`

EN: Zaporizhstal.

Описание RU: Две новые линии и дополнительные плавки станут основой концерна «Вольная сталь». Промышленный совет доступен всем коммунам; с Arms Against Tyranny заводы также образуют артиллерийскую MIO, развиваемую производственными циклами и финальным договором.

Описание EN: Two new production lines and additional steel establish the Free Steel concern. Its industrial council is available with or without DLC; Arms Against Tyranny also enables an artillery MIO developed through production cycles and the final compact.

Источник: `common/national_focus/MKN.txt:212`. Стоимость: 10 (70 дней). Координаты: x=4, y=4.

Предпосылки: (Индустриальные гиганты степи [MKN_steppe_industrial_giants]).

Взаимоисключения: нет.

Прямые продолжения: MKN_worker_battalions, MKN_dnieper_logistics_hub.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_zaporizhstal
    icon = GFX_focus_generic_steel_mill
    x = 4
    y = 4
    cost = 10
    available_if_capitulated = no
    ai_will_do = {
        factor = 2
    }
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    prerequisite = {
        focus = MKN_steppe_industrial_giants
    }
    completion_reward = {
        add_political_power = 50
        226 = {
            if = {
                limit = {
                    is_owned_and_controlled_by = ROOT
                }
                add_extra_state_shared_building_slots = 2
                add_building_construction = {
                    type = arms_factory
                    level = 2
                    instant_build = yes
                }
            }
        }
        show_ideas_tooltip = MKN_industry_concern_1
        if = {
            limit = {
                has_dlc = "Arms Against Tyranny"
            }
            show_mio_tooltip = MKN_zaporizhstal_organization
            mio:MKN_zaporizhstal_organization = {
                add_mio_size = 1
            }
        }
        226 = {
            if = {
                limit = {
                    is_owned_and_controlled_by = ROOT
                }
                add_resource = {
                    type = steel
                    amount = 10
                }
            }
        }
        add_to_variable = {
            MKN_unified_political_power_gain = 0.1000
            tooltip = MKN_unified_political_power_gain_tt
        }
        add_to_variable = {
            MKN_unified_consumer_goods_factor = -0.0500
            tooltip = MKN_unified_consumer_goods_factor_tt
        }
        add_to_variable = {
            MKN_unified_production_speed_buildings_factor = 0.0500
            tooltip = MKN_unified_production_speed_buildings_factor_tt
        }
        add_to_variable = {
            MKN_unified_industrial_capacity_factory = 0.0500
            tooltip = MKN_unified_industrial_capacity_factory_tt
        }
    }
}
```

### Артели стрелкового вооружения — `MKN_rifle_concern`

EN: Rifle Artels.

Описание RU: Оружейные артели получат защищённую внекарточную производственную линию. С Arms Against Tyranny доступна пехотная MIO; без дополнения — оружейный конструктор. Договор о взаимозаменяемости позволит развить выбранное предприятие.

Описание EN: The rifle artels receive a protected off-map military factory. Arms Against Tyranny enables an infantry MIO; without it, a weapons designer is available. Workshop standards develop the enterprise further.

Источник: `common/national_focus/MKN.txt:686`. Стоимость: 10 (70 дней). Координаты: x=16, y=4.

Предпосылки: (Передвижные мастерские и кузницы [MKN_mobile_workshops]).

Взаимоисключения: нет.

Прямые продолжения: MKN_grain_exchanges, MKN_freight_logistics.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_rifle_concern
    icon = GFX_focus_generic_anti_tank_guns
    x = 16
    y = 4
    cost = 10
    available_if_capitulated = no
    ai_will_do = {
        factor = 2
    }
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    prerequisite = {
        focus = MKN_mobile_workshops
    }
    completion_reward = {
        add_offsite_building = {
            type = arms_factory
            level = 1
        }
        if = {
            limit = {
                has_dlc = "Arms Against Tyranny"
            }
            show_mio_tooltip = MKN_rifle_artels_organization
        }
        else = {
            show_ideas_tooltip = MKN_rifle_concern_1
        }
        add_to_variable = {
            MKN_unified_industrial_capacity_factory = 0.0500
            tooltip = MKN_unified_industrial_capacity_factory_tt
        }
    }
}
```

### Гуляйпольская коммуна — `MKN_gulyai_polye_commune`

EN: Gulyai-Polye Commune.

Описание RU: Столица анархии покажет миру иной способ жить.

Описание EN: The capital of anarchy will show the world a different way to live.

Источник: `common/national_focus/MKN.txt:1092`. Стоимость: 5 (35 дней). Координаты: x=34, y=4.

Предпосылки: (Вольные советы [MKN_free_soviets]).

Взаимоисключения: нет.

Прямые продолжения: MKN_anarchist_schools.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_gulyai_polye_commune
    icon = GFX_focus_generic_industry_1
    prerequisite = {
        focus = MKN_free_soviets
    }
    completion_reward = {
        add_political_power = 50
        226 = {
            if = {
                limit = {
                    is_owned_and_controlled_by = ROOT
                }
                add_extra_state_shared_building_slots = 1
                add_building_construction = {
                    type = industrial_complex
                    level = 1
                    instant_build = yes
                }
            }
        }
    }
    x = 34
    y = 4
    cost = 5
}
```

### Арестовать демагогов — `MKN_arrest_demagogues`

EN: Arrest the Demagogues.

Описание RU: Штаб опечатывает фракционные типографии и задерживает организаторов соперничающих командований. Жестокое урегулирование останавливает 180-дневный отсчёт до гражданской войны.

Описание EN: The staff seals the faction presses and detains those organizing rival commands. A brutal settlement ends the 180-day countdown to civil war.

Источник: `common/national_focus/MKN.txt:6882`. Стоимость: 5 (35 дней). Координаты: x=100, y=4.

Предпосылки: (Военные берут власть [MKN_military_takes_charge]).

Взаимоисключения: нет.

Прямые продолжения: MKN_abolish_election_of_commanders.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_arrest_demagogues
    x = 100
    y = 4
    completion_reward = {
        MKN_resolve_succession_crisis = yes
        add_stability = 0.10
        add_political_power = 50
    }
    prerequisite = {
        focus = MKN_military_takes_charge
    }
    available = {
        NOT = {
            has_country_flag = MKN_crisis_legacy_settled
        }
        has_government = fascism
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
    icon = GFX_focus_MKN_program_militarism_1
}
```

### Пакт вольных коммун — `MKN_pact_of_free_communes`

EN: The Pact of Free Communes.

Описание RU: Коммуны обязуются разрешать споры без создания соперничающих армий. Ратификация остановит отсчёт до гражданской войны и восстановит доверие к коллективному управлению.

Описание EN: The communes sign a common obligation to settle disputes without rival armies. Ratification stops the civil-war countdown and restores confidence in collective rule.

Источник: `common/national_focus/MKN.txt:7174`. Стоимость: 5 (35 дней). Координаты: x=106, y=4.

Предпосылки: (Торжество вольных советов [MKN_triumph_of_free_soviets]).

Взаимоисключения: нет.

Прямые продолжения: MKN_abolish_general_staff.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_pact_of_free_communes
    x = 106
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
}
```

### Зерновой ультиматум — `MKN_grain_ultimatum`

EN: The Grain Ultimatum.

Описание RU: Сёла прокормят общую оборону, но никогда — четыре соперничающих штаба. Их ультиматум разрешит вопрос преемственности и остановит отсчёт до гражданской войны.

Описание EN: The villages will feed a common defense, never four rival headquarters. Their ultimatum settles the succession and stops the civil-war countdown.

Источник: `common/national_focus/MKN.txt:7428`. Стоимость: 5 (35 дней). Координаты: x=112, y=4.

Предпосылки: (Крестьянские делегаты [MKN_peasant_delegates]).

Взаимоисключения: нет.

Прямые продолжения: MKN_sever_urban_ties.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_grain_ultimatum
    x = 112
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
}
```

### Устранить непримиримых — `MKN_purge_irreconcilables`

EN: Purge the Irreconcilables.

Описание RU: Ревком прикажет каждому вооружённому комитету сдать оружие и списки. Разрешим вопрос преемственности и остановим 180-дневный отсчёт.

Описание EN: The revkom orders every armed committee to submit its weapons and registers. Resolve the succession and stop the 180-day countdown.

Источник: `common/national_focus/MKN.txt:7672`. Стоимость: 5 (35 дней). Координаты: x=118, y=4.

Предпосылки: (Чрезвычайный ревком [MKN_emergency_revkom]).

Взаимоисключения: нет.

Прямые продолжения: MKN_embassy_to_kharkov.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_purge_irreconcilables
    x = 118
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
}
```

### Хлебные биржи и резервы — `MKN_grain_exchanges`

EN: Grain Exchanges and Reserves.

Описание RU: Фабрика в Херсоне поддержит переработку и обмен урожая. На карте открываются три проекта по 60 дней: запорожские элеваторы, херсонские зерновые терминалы и степная посевная. Политику запасов выбирает хозяйственный конгресс.

Описание EN: A Kherson factory supports processing and exchange. Unlock three 60-day map projects: Zaporizhzhia elevators, Kherson grain terminals and steppe sowing. The Economic Congress chooses stockpile policy.

Источник: `common/national_focus/MKN.txt:722`. Стоимость: 5 (35 дней). Координаты: x=14, y=5.

Предпосылки: (Артели стрелкового вооружения [MKN_rifle_concern]).

Взаимоисключения: нет.

Прямые продолжения: MKN_workshop_standards.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_grain_exchanges
    icon = GFX_focus_generic_agricultural_subsidies
    x = 14
    y = 5
    cost = 5
    available_if_capitulated = no
    ai_will_do = {
        factor = 2
    }
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    prerequisite = {
        focus = MKN_rifle_concern
    }
    completion_reward = {
        196 = {
            if = {
                limit = {
                    is_owned_and_controlled_by = ROOT
                }
                add_extra_state_shared_building_slots = 1
                add_building_construction = {
                    type = industrial_complex
                    level = 1
                    instant_build = yes
                }
            }
        }
        custom_effect_tooltip = MKN_grain_projects_unlock_tt
    }
}
```

### Гужевая и грузовая логистика — `MKN_freight_logistics`

EN: Wagon and Truck Logistics.

Описание RU: Обозные артели и ремонтные биржи распределят склады между хуторами. Договоры подвоза резко сократят расход снабжения и истощение, а резервный уголь обеспечит мастерские.

Описание EN: Freight artels and repair exchanges distribute depots among the villages. Supply agreements sharply reduce consumption and attrition while reserve coal keeps workshops running.

Источник: `common/national_focus/MKN.txt:755`. Стоимость: 5 (35 дней). Координаты: x=18, y=5.

Предпосылки: (Артели стрелкового вооружения [MKN_rifle_concern]).

Взаимоисключения: нет.

Прямые продолжения: MKN_workshop_standards.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_freight_logistics
    icon = GFX_focus_generic_railroad
    x = 18
    y = 5
    cost = 5
    available_if_capitulated = no
    ai_will_do = {
        factor = 2
    }
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    prerequisite = {
        focus = MKN_rifle_concern
    }
    completion_reward = {
        add_tech_bonus = {
            bonus = 0.5
            uses = 1
            category = train_tech
        }
        add_tech_bonus = {
            bonus = 0.5
            uses = 1
            category = motorized_equipment
        }
        196 = {
            if = {
                limit = {
                    is_owned_and_controlled_by = ROOT
                }
                add_resource = {
                    type = coal
                    amount = 8
                }
            }
        }
        add_to_variable = {
            MKN_unified_supply_consumption_factor = -0.3000
            tooltip = MKN_unified_supply_consumption_factor_tt
        }
        add_to_variable = {
            MKN_unified_army_org_regain = 0.1500
            tooltip = MKN_unified_army_org_regain_tt
        }
        add_to_variable = {
            MKN_unified_attrition = -0.0500
            tooltip = MKN_unified_attrition_tt
        }
    }
}
```

### Анархистские школы — `MKN_anarchist_schools`

EN: Anarchist Schools.

Описание RU: Школы Феррера для свободных детей.

Описание EN: Ferrer schools for free children.

Источник: `common/national_focus/MKN.txt:1137`. Стоимость: 5 (35 дней). Координаты: x=34, y=5.

Предпосылки: (Гуляйпольская коммуна [MKN_gulyai_polye_commune]).

Взаимоисключения: нет.

Прямые продолжения: MKN_peasant_militias, MKN_the_steppe_holds.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_anarchist_schools
    icon = GFX_focus_generic_industry_1
    prerequisite = {
        focus = MKN_gulyai_polye_commune
    }
    completion_reward = {
        add_tech_bonus = {
            bonus = 0.5
            uses = 1
            category = industry
        }
    }
    x = 34
    y = 5
    cost = 5
}
```

### Разорвать связи с городом — `MKN_sever_urban_ties`

EN: Sever Urban Ties.

Описание RU: Закроем экспортные книги и распустим соперничающие делегации. Упраздним баланс сил, введём закрытую экономику и оставим больше продукции сёлам.

Описание EN: Close the export ledgers and dismiss the competing delegations. Abolish the balance of power, adopt a closed economy and reserve more output for the villages.

Источник: `common/national_focus/MKN.txt:7454`. Стоимость: 5 (35 дней). Координаты: x=112, y=5.

Предпосылки: (Зерновой ультиматум [MKN_grain_ultimatum]).

Взаимоисключения: нет.

Прямые продолжения: MKN_every_farm_a_fortress.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_sever_urban_ties
    x = 112
    y = 5
    completion_reward = {
        MKN_dismantle_bop = yes
        add_ideas = closed_economy
        add_to_variable = {
            MKN_unified_consumer_goods_factor = -0.05
            tooltip = MKN_unified_consumer_goods_factor_tt
        }
    }
    prerequisite = {
        focus = MKN_grain_ultimatum
    }
    available = {
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
    icon = GFX_focus_MKN_program_agrarian_2
}
```

### Посольство в Харьков — `MKN_embassy_to_kharkov`

EN: An Embassy to Kharkov.

Описание RU: Упраздним баланс сил и отправим делегацию в советские республики. Первое предложение предусматривает взаимный военный транзит и обмен зерна на снабжение; Харьков вправе отказать.

Описание EN: Disband the balance of power and send a delegation to the Soviet Republics. The first proposal offers reciprocal military transit and a grain-for-supply agreement; Kharkov may refuse.

Источник: `common/national_focus/MKN.txt:7702`. Стоимость: 5 (35 дней). Координаты: x=118, y=5.

Предпосылки: (Устранить непримиримых [MKN_purge_irreconcilables]).

Взаимоисключения: нет.

Прямые продолжения: MKN_integrate_steel_lines.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_embassy_to_kharkov
    x = 118
    y = 5
    completion_reward = {
        MKN_dismantle_bop = yes
        SOV = {
            country_event = {
                id = mkn_crisis.20
                days = 1
            }
        }
    }
    prerequisite = {
        focus = MKN_purge_irreconcilables
    }
    available = {
        NOT = {
            has_country_flag = MKN_crisis_legacy_settled
        }
        has_government = communism
        is_subject = no
        SOV = {
            exists = yes
            has_government = communism
            is_subject = no
        }
        NOT = {
            has_war_with = SOV
        }
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    cost = 5
    icon = GFX_focus_MKN_program_revkom_2
}
```

### Договор о взаимозаменяемости — `MKN_workshop_standards`

EN: Interchangeability Agreement.

Описание RU: Общие калибры, ремонтные образцы и портфель заказов соединят самостоятельные мастерские. Дополнительный военный завод и развитие оружейного предприятия повысят выпуск и эффективность без единственного промышленного центра.

Описание EN: Common calibres, repair patterns and pooled orders unite independent workshops. Another military factory and an upgraded weapons enterprise improve output without a single industrial centre.

Источник: `common/national_focus/MKN.txt:807`. Стоимость: 10 (70 дней). Координаты: x=16, y=6.

Предпосылки: (Хлебные биржи и резервы [MKN_grain_exchanges]) И (Гужевая и грузовая логистика [MKN_freight_logistics]).

Взаимоисключения: нет.

Прямые продолжения: MKN_field_schools.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_workshop_standards
    icon = GFX_focus_generic_industry_2
    x = 16
    y = 6
    cost = 10
    available_if_capitulated = no
    ai_will_do = {
        factor = 2
    }
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    prerequisite = {
        focus = MKN_grain_exchanges
    }
    prerequisite = {
        focus = MKN_freight_logistics
    }
    completion_reward = {
        add_tech_bonus = {
            bonus = 0.5
            uses = 1
            category = infantry_weapons
        }
        random_owned_controlled_state = {
            limit = {
                is_core_of = ROOT
            }
            prioritize = {
                1082
                200
                196
            }
            add_extra_state_shared_building_slots = 1
            add_building_construction = {
                type = arms_factory
                level = 1
                instant_build = yes
            }
        }
        if = {
            limit = {
                has_dlc = "Arms Against Tyranny"
            }
            mio:MKN_rifle_artels_organization = {
                add_mio_size = 1
                add_mio_research_bonus = 0.05
                unlock_mio_trait_tooltip = MKN_rifle_artels_organization_specialization_a
                unlock_mio_trait_tooltip = MKN_rifle_artels_organization_specialization_b
            }
        }
        else = {
            if = {
                limit = {
                    has_idea = MKN_rifle_concern_1
                }
                swap_ideas = {
                    remove_idea = MKN_rifle_concern_1
                    add_idea = MKN_rifle_concern_2
                }
            }
            show_ideas_tooltip = MKN_rifle_concern_2
        }
        add_to_variable = {
            MKN_unified_industrial_capacity_factory = 0.1500
            tooltip = MKN_unified_industrial_capacity_factory_tt
        }
        add_to_variable = {
            MKN_unified_production_factory_efficiency_gain_factor = 0.2500
            tooltip = MKN_unified_production_factory_efficiency_gain_factor_tt
        }
        add_to_variable = {
            MKN_unified_research_speed_factor = 0.0500
            tooltip = MKN_unified_research_speed_factor_tt
        }
    }
}
```

### Степь держится — `MKN_the_steppe_holds`

EN: The Steppe Holds.

Описание RU: Три года войны, а Вольная территория стоит. Пусть приходят.

Описание EN: Three years of war and the Free Territory still stands. Let them come.

Источник: `common/national_focus/MKN.txt:1200`. Стоимость: 5 (35 дней). Координаты: x=34, y=6.

Предпосылки: (Анархистские школы [MKN_anarchist_schools] ИЛИ Махно идёт на юг [MKN_makhno_moves_south]).

Взаимоисключения: нет.

Прямые продолжения: MKN_soviet_press, MKN_border_tensions.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_the_steppe_holds
    icon = GFX_focus_generic_diplomatic_treaty
    completion_reward = {
        add_stability = 0.1
        add_political_power = 150
    }
    x = 34
    y = 6
    prerequisite = {
        focus = MKN_anarchist_schools
        focus = MKN_makhno_moves_south
    }
    available = {
        OR = {
            has_completed_focus = MKN_shadow_republic
            has_completed_focus = MKN_makhno_moves_south
        }
    }
    cost = 5
}
```

### Каждый хутор — крепость — `MKN_every_farm_a_fortress`

EN: Every Farm a Fortress.

Описание RU: Подвалы станут складами боеприпасов, изгороди скроют огневые позиции. Построим два уровня сухопутных укреплений вдоль границ принадлежащих нам и контролируемых нами областей.

Описание EN: Cellars become ammunition stores; hedges conceal firing positions. Build two levels of land forts along the borders of states we own and control.

Источник: `common/national_focus/MKN.txt:7483`. Стоимость: 5 (35 дней). Координаты: x=112, y=6.

Предпосылки: (Разорвать связи с городом [MKN_sever_urban_ties]).

Взаимоисключения: нет.

Прямые продолжения: MKN_steppe_snipers.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_every_farm_a_fortress
    x = 112
    y = 6
    completion_reward = {
        MKN_build_border_forts = yes
    }
    prerequisite = {
        focus = MKN_sever_urban_ties
    }
    available = {
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
    icon = GFX_focus_MKN_program_agrarian_3
}
```

### Объединить стальные магистрали — `MKN_integrate_steel_lines`

EN: Integrate the Steel Lines.

Описание RU: С согласия советской стороны и при контролируемой общей границе построим железнодорожное соединение второго уровня. Получим десять локомотивов и два года помощи в организации снабжения.

Описание EN: With Soviet consent and a controlled common border, build a level-two railway connection. Receive ten locomotives and two years of coordinated supply assistance.

Источник: `common/national_focus/MKN.txt:7741`. Стоимость: 5 (35 дней). Координаты: x=118, y=6.

Предпосылки: (Посольство в Харьков [MKN_embassy_to_kharkov]).

Взаимоисключения: нет.

Прямые продолжения: MKN_red_military_specialists.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_integrate_steel_lines
    x = 118
    y = 6
    completion_reward = {
        MKN_build_soviet_rail_link = yes
        add_timed_idea = {
            idea = MKN_soviet_supply_agreement
            days = 730
        }
    }
    prerequisite = {
        focus = MKN_embassy_to_kharkov
    }
    available = {
        NOT = {
            has_country_flag = MKN_crisis_legacy_settled
        }
        has_government = communism
        has_country_flag = MKN_soviet_trade_accepted
        SOV = {
            exists = yes
            NOT = {
                has_war_with = ROOT
            }
        }
        has_military_access_to = SOV
        any_owned_state = {
            is_controlled_by = ROOT
            any_neighbor_state = {
                is_owned_and_controlled_by = SOV
            }
        }
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    cost = 5
    icon = GFX_focus_MKN_program_revkom_3
}
```

### Советская печать — `MKN_soviet_press`

EN: Soviet Press.

Описание RU: «Набат» и «Голос» ежедневно печатают правду.

Описание EN: Nabat and Golos print the truth daily.

Источник: `common/national_focus/MKN.txt:1186`. Стоимость: 5 (35 дней). Координаты: x=32, y=7.

Предпосылки: (Степь держится [MKN_the_steppe_holds]).

Взаимоисключения: нет.

Прямые продолжения: MKN_constituent_assembly, MKN_red_banner_steppe, MKN_black_hundreds, MKN_nestor_the_first.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_soviet_press
    icon = GFX_focus_research
    prerequisite = {
        focus = MKN_the_steppe_holds
    }
    completion_reward = {
        add_political_power = 80
        add_stability = 0.05
    }
    x = 32
    y = 7
    cost = 5
}
```

### Стандартизировать мастерские — `MKN_standardize_workshops`

EN: Standardize the Workshops.

Описание RU: Дюжина несовместимых затворов — дюжина способов проиграть бой. Общие калибры и согласованные заказы повысят выпуск и эффективность производства в артелях.

Описание EN: A dozen incompatible breech blocks are a dozen ways to lose a battle. Give the artels common gauges and coordinated orders to raise output and production efficiency.

Источник: `common/national_focus/MKN.txt:6974`. Стоимость: 5 (35 дней). Координаты: x=100, y=7.

Предпосылки: (Милитаризовать коммуны [MKN_militarize_communes]).

Взаимоисключения: нет.

Прямые продолжения: MKN_iron_fist_trains.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_standardize_workshops
    x = 100
    y = 7
    completion_reward = {
        add_to_variable = {
            MKN_unified_industrial_capacity_factory = 0.15
            tooltip = MKN_unified_industrial_capacity_factory_tt
        }
        add_to_variable = {
            MKN_unified_production_factory_efficiency_gain_factor = 0.1
            tooltip = MKN_unified_production_factory_efficiency_gain_factor_tt
        }
    }
    prerequisite = {
        focus = MKN_militarize_communes
    }
    available = {
        NOT = {
            has_country_flag = MKN_crisis_legacy_settled
        }
        has_government = fascism
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    cost = 5
    icon = GFX_focus_MKN_program_militarism_4
}
```

### Пропаганда действием — `MKN_propaganda_by_deed`

EN: Propaganda by Deed.

Описание RU: Погасшая печь говорит громче манифеста. Откроем сети стачек в соседних странах; их правительства должны будут переждать остановку производства или заплатить за её подавление.

Описание EN: A stopped furnace speaks more loudly than a manifesto. Unlock strike networks in neighboring countries; their governments must endure the stoppage or pay to break it.

Источник: `common/national_focus/MKN.txt:7303`. Стоимость: 5 (35 дней). Координаты: x=106, y=7.

Предпосылки: (Оружие народу [MKN_arms_to_the_people]).

Взаимоисключения: нет.

Прямые продолжения: MKN_autonomous_rail_crews.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_propaganda_by_deed
    x = 106
    completion_reward = {
        custom_effect_tooltip = MKN_unlock_strikes_tt
        add_political_power = 75
    }
    available = {
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
    icon = GFX_focus_MKN_program_nabat_5
    y = 7
    prerequisite = {
        focus = MKN_arms_to_the_people
    }
}
```

### Власть атаманов — `MKN_black_hundreds`

EN: The Atamans Take Command.

Описание RU: При поддержке не менее 40% и после подготовки общественного мандата атаманы устанавливают анархо-милитаризм. Баланс смещается на 0,45 к командованию; согласие общин уступает место военным приказам.

Описание EN: With at least 40% support and a mandate from the communal press, the atamans establish anarcho-militarism. Army command gains 0.45 on the native balance scale; village consent gives way to military orders.

Источник: `common/national_focus/MKN.txt:1785`. Стоимость: 5 (35 дней). Координаты: x=29, y=8.

Предпосылки: (Советская печать [MKN_soviet_press]).

Взаимоисключения: MKN_constituent_assembly, MKN_nestor_the_first, MKN_red_banner_steppe.

Прямые продолжения: MKN_order_through_tachanka.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_black_hundreds
    icon = GFX_focus_generic_army_attack
    completion_reward = {
        set_politics = {
            ruling_party = fascism
            elections_allowed = no
        }
        add_war_support = 0.1
        if = {
            limit = {
                has_power_balance = {
                    id = MKN_power_balance
                }
                NOT = {
                    has_country_flag = MKN_bop_locked
                }
            }
            add_power_balance_value = {
                id = MKN_power_balance
                value = -0.45
                tooltip_side = MKN_military_command_side
            }
        }
    }
    available = {
        has_completed_focus = MKN_soviet_press
        NOT = {
            fascism < 0.40
        }
        NOT = {
            OR = {
                has_completed_focus = MKN_everlasting_makhnovshchina
                has_completed_focus = MKN_council_communism
            }
        }
        NOT = {
            has_country_flag = MKN_crisis_enabled
        }
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    x = 29
    y = 8
    prerequisite = {
        focus = MKN_soviet_press
    }
    mutually_exclusive = {
        focus = MKN_constituent_assembly
        focus = MKN_nestor_the_first
        focus = MKN_red_banner_steppe
    }
    allow_branch = {
        NOT = {
            has_country_flag = MKN_crisis_enabled
        }
    }
    cost = 5
}
```

### Съезд вольных советов — `MKN_constituent_assembly`

EN: The Congress of Free Soviets.

Описание RU: Для передачи власти отзывным делегатам советов нужна поддержка не менее 40%. Анархо-коммунизм использует демократическую группу идеологий, но общегосударственные парламентские выборы отключены. Баланс смещается на 0,45 к вольным советам.

Описание EN: At least 40% support is required to entrust authority to recallable council delegates. Anarcho-communism uses the democratic ideology group, while national parliamentary elections remain disabled. The balance shifts by 0.45 toward the free soviets.

Источник: `common/national_focus/MKN.txt:1480`. Стоимость: 5 (35 дней). Координаты: x=33, y=8.

Предпосылки: (Советская печать [MKN_soviet_press]).

Взаимоисключения: MKN_black_hundreds, MKN_nestor_the_first, MKN_red_banner_steppe.

Прямые продолжения: MKN_free_elections_steppe.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_constituent_assembly
    icon = GFX_focus_generic_support_the_left_right
    completion_reward = {
        set_politics = {
            ruling_party = democratic
            elections_allowed = no
        }
        add_stability = -0.05
        if = {
            limit = {
                has_power_balance = {
                    id = MKN_power_balance
                }
                NOT = {
                    has_country_flag = MKN_bop_locked
                }
            }
            add_power_balance_value = {
                id = MKN_power_balance
                value = 0.45
                tooltip_side = MKN_free_soviets_side
            }
        }
    }
    available = {
        has_completed_focus = MKN_soviet_press
        NOT = {
            democratic < 0.40
        }
        NOT = {
            has_country_flag = MKN_crisis_enabled
        }
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    x = 33
    y = 8
    prerequisite = {
        focus = MKN_soviet_press
    }
    mutually_exclusive = {
        focus = MKN_black_hundreds
        focus = MKN_nestor_the_first
        focus = MKN_red_banner_steppe
    }
    allow_branch = {
        NOT = {
            has_country_flag = MKN_crisis_enabled
        }
    }
    cost = 5
}
```

### Крестьянский покровитель — `MKN_nestor_the_first`

EN: The Peasant Protector.

Описание RU: При поддержке не менее 40% крестьянский съезд выбирает аграрный изоляционизм под покровительством Нестора I. Спор командования с советами упраздняется вместе со шкалой баланса и её модификаторами. Махно сохраняет корону и портрет, а его военные должности остаются доступны только при коммунизме.

Описание EN: With at least 40% support, the peasant congress chooses agrarian isolationism under Nestor I. The dispute between command and soviets is abolished, removing the balance of power and its modifiers. Makhno retains his crown and portrait, while his military offices remain restricted to communism.

Источник: `common/national_focus/MKN.txt:1949`. Стоимость: 5 (35 дней). Координаты: x=41, y=8.

Предпосылки: (Советская печать [MKN_soviet_press]).

Взаимоисключения: MKN_black_hundreds, MKN_constituent_assembly, MKN_red_banner_steppe.

Прямые продолжения: MKN_imperial_coronation.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_nestor_the_first
    icon = GFX_focus_generic_diplomatic_treaty
    completion_reward = {
        set_politics = {
            ruling_party = neutrality
            elections_allowed = no
        }
        add_stability = 0.05
        remove_power_balance = {
            id = MKN_power_balance
        }
        set_country_flag = MKN_bop_abandoned
    }
    available = {
        has_completed_focus = MKN_soviet_press
        NOT = {
            neutrality < 0.40
        }
        NOT = {
            OR = {
                has_completed_focus = MKN_everlasting_makhnovshchina
                has_completed_focus = MKN_council_communism
            }
        }
        NOT = {
            has_country_flag = MKN_crisis_enabled
        }
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    x = 41
    y = 8
    prerequisite = {
        focus = MKN_soviet_press
    }
    mutually_exclusive = {
        focus = MKN_black_hundreds
        focus = MKN_constituent_assembly
        focus = MKN_red_banner_steppe
    }
    allow_branch = {
        NOT = {
            has_country_flag = MKN_crisis_enabled
        }
    }
    cost = 5
}
```

### Самоуправляемые железнодорожные бригады — `MKN_autonomous_rail_crews`

EN: Autonomous Rail Crews.

Описание RU: Расписание принадлежит тем, кто обеспечивает движение. Рабочие бригады снизят стоимость поездов и ускорят строительство железных дорог и инфраструктуры.

Описание EN: The timetable belongs to those who keep it running. Worker crews lower train costs and accelerate railway and infrastructure construction.

Источник: `common/national_focus/MKN.txt:7328`. Стоимость: 5 (35 дней). Координаты: x=106, y=8.

Предпосылки: (Пропаганда действием [MKN_propaganda_by_deed]).

Взаимоисключения: нет.

Прямые продолжения: MKN_beacon_of_statelessness.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_autonomous_rail_crews
    x = 106
    completion_reward = {
        add_ideas = MKN_autonomous_rail_crews_idea
        add_to_variable = {
            MKN_unified_production_speed_buildings_factor = 0.05
            tooltip = MKN_unified_production_speed_buildings_factor_tt
        }
    }
    prerequisite = {
        focus = MKN_propaganda_by_deed
    }
    available = {
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
    icon = GFX_focus_MKN_program_nabat_6
    y = 8
}
```

### Железнодорожные диверсии — `MKN_railway_sabotage`

EN: Railway Sabotage.

Описание RU: Подготовим заряды до приказа об отступлении. Откроем намеренное разрушение инфраструктуры и железных дорог в пограничных областях под угрозой; ремонт займёт больше времени.

Описание EN: Prepare the charges before the retreat order comes. Unlock deliberate damage to infrastructure and railways in threatened border states; their repair will take longer.

Источник: `common/national_focus/MKN.txt:7542`. Стоимость: 5 (35 дней). Координаты: x=112, y=8.

Предпосылки: (Степные снайперы [MKN_steppe_snipers]).

Взаимоисключения: нет.

Прямые продолжения: MKN_cavalry_ambush.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_railway_sabotage
    x = 112
    y = 8
    completion_reward = {
        custom_effect_tooltip = MKN_unlock_sabotage_tt
    }
    prerequisite = {
        focus = MKN_steppe_snipers
    }
    available = {
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
    icon = GFX_focus_MKN_program_agrarian_5
}
```

### Отзывные мандаты общин — `MKN_free_elections_steppe`

EN: Recallable Communal Mandates.

Описание RU: Каждая коммуна избирает и отзывает своих делегатов. Федерация получает устойчивые мандаты без постоянного парламента. Вольные советы получают ещё 0,20 на шкале баланса.

Описание EN: Each commune elects and may recall its delegates. The federation receives reliable mandates without creating a permanent parliament. Free soviets gain another 0.20 on the balance scale.

Источник: `common/national_focus/MKN.txt:1533`. Стоимость: 5 (35 дней). Координаты: x=33, y=9.

Предпосылки: (Съезд вольных советов [MKN_constituent_assembly]).

Взаимоисключения: нет.

Прямые продолжения: MKN_everlasting_makhnovshchina, MKN_council_communism, MKN_open_markets.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_free_elections_steppe
    icon = GFX_focus_generic_diplomatic_treaty
    prerequisite = {
        focus = MKN_constituent_assembly
    }
    completion_reward = {
        add_stability = 0.1
        add_political_power = 100
        country_event = {
            id = mkn.20
            days = 1
        }
        remove_ideas = MKN_free_territory
        remove_ideas = MKN_free_soviets_idea
        if = {
            limit = {
                has_power_balance = {
                    id = MKN_power_balance
                }
                NOT = {
                    has_country_flag = MKN_bop_locked
                }
            }
            add_power_balance_value = {
                id = MKN_power_balance
                value = 0.2
                tooltip_side = MKN_free_soviets_side
            }
        }
        add_to_variable = {
            MKN_unified_stability_factor = 0.1
            tooltip = MKN_unified_stability_factor_tt
        }
        add_to_variable = {
            MKN_unified_political_power_gain = 0.1
            tooltip = MKN_unified_political_power_gain_tt
        }
    }
    x = 33
    y = 9
    allow_branch = {
        NOT = {
            has_country_flag = MKN_crisis_enabled
        }
    }
    cost = 5
}
```

### Императорская коронация — `MKN_imperial_coronation`

EN: Imperial Coronation.

Описание RU: Корона из пшеницы и стали.

Описание EN: A crown of wheat and steel.

Источник: `common/national_focus/MKN.txt:1997`. Стоимость: 5 (35 дней). Координаты: x=41, y=9.

Предпосылки: (Крестьянский покровитель [MKN_nestor_the_first]).

Взаимоисключения: нет.

Прямые продолжения: MKN_steppe_empire.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_imperial_coronation
    icon = GFX_focus_generic_support_the_left_right
    prerequisite = {
        focus = MKN_nestor_the_first
    }
    completion_reward = {
        add_political_power = 150
        add_war_support = 0.1
        country_event = {
            id = mkn.20
            days = 1
        }
        remove_ideas = MKN_free_territory
        remove_ideas = MKN_free_soviets_idea
        add_to_variable = {
            MKN_unified_stability_factor = 0.1
            tooltip = MKN_unified_stability_factor_tt
        }
        add_to_variable = {
            MKN_unified_political_power_gain = 0.15
            tooltip = MKN_unified_political_power_gain_tt
        }
    }
    x = 41
    y = 9
    allow_branch = {
        NOT = {
            has_country_flag = MKN_crisis_enabled
        }
    }
    cost = 5
}
```

### Чёрный экспансионизм — `MKN_black_expansionism`

EN: Black Expansionism.

Описание RU: Граница, проведённая канцелярией, не священна. Откроем пограничные столкновения с ЛитБелом и советскими республиками там, где наши территории действительно соприкасаются.

Описание EN: A frontier drawn by a chancery is no sacred boundary. Unlock controlled border clashes with LitBel and the Soviet Republics wherever our territories actually meet.

Источник: `common/national_focus/MKN.txt:7045`. Стоимость: 5 (35 дней). Координаты: x=100, y=9.

Предпосылки: (Железный кулак на рельсах [MKN_iron_fist_trains]).

Взаимоисключения: нет.

Прямые продолжения: MKN_the_black_horde.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_black_expansionism
    x = 100
    y = 9
    completion_reward = {
        custom_effect_tooltip = MKN_unlock_border_clashes_tt
        add_war_support = 0.05
    }
    prerequisite = {
        focus = MKN_iron_fist_trains
    }
    available = {
        NOT = {
            has_country_flag = MKN_crisis_legacy_settled
        }
        has_government = fascism
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    cost = 5
    icon = GFX_focus_MKN_program_militarism_6
}
```

### Синдикалистская программа — `MKN_council_communism`

EN: The Syndicalist Program.

Описание RU: Заводские собрания и крестьянские коммуны согласуют производство через выборных делегатов. Этот вариант анархо-коммунизма усиливает советы на 0,20 без подчинения Москве.

Описание EN: Factory assemblies and peasant communes coordinate production through elected delegates. This alternative within anarcho-communism strengthens the soviets by 0.20 without submitting to Moscow.

Источник: `common/national_focus/MKN.txt:1355`. Стоимость: 5 (35 дней). Координаты: x=35, y=10.

Предпосылки: (Отзывные мандаты общин [MKN_free_elections_steppe]).

Взаимоисключения: MKN_everlasting_makhnovshchina.

Прямые продолжения: MKN_workers_control.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_council_communism
    icon = GFX_focus_research
    completion_reward = {
        add_tech_bonus = {
            bonus = 0.5
            uses = 2
            category = industry
        }
        set_politics = {
            ruling_party = democratic
            elections_allowed = no
        }
        create_country_leader = {
            name = "Nestor Makhno"
            picture = GFX_Portrait_makhno
            traits = {

            }
            ideology = socialism
        }
        if = {
            limit = {
                has_power_balance = {
                    id = MKN_power_balance
                }
                NOT = {
                    has_country_flag = MKN_bop_locked
                }
            }
            add_power_balance_value = {
                id = MKN_power_balance
                value = 0.2
                tooltip_side = MKN_free_soviets_side
            }
        }
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    x = 35
    y = 10
    prerequisite = {
        focus = MKN_free_elections_steppe
    }
    mutually_exclusive = {
        focus = MKN_everlasting_makhnovshchina
    }
    available = {
        has_completed_focus = MKN_soviet_press
        NOT = {
            democratic < 0.40
        }
    }
    allow_branch = {
        NOT = {
            has_country_flag = MKN_crisis_enabled
        }
    }
    cost = 5
}
```

### Советы навсегда — `MKN_soviets_forever`

EN: Soviets Forever.

Описание RU: Коммуна вечна.

Описание EN: The commune is eternal.

Источник: `common/national_focus/MKN.txt:1299`. Стоимость: 5 (35 дней). Координаты: x=31, y=11.

Предпосылки: (Махновская традиция [MKN_everlasting_makhnovshchina]).

Взаимоисключения: нет.

Прямые продолжения: MKN_tachanka_guards.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_soviets_forever
    icon = GFX_focus_generic_diplomatic_treaty
    prerequisite = {
        focus = MKN_everlasting_makhnovshchina
    }
    completion_reward = {
        add_stability = 0.1
        add_political_power = 100
        country_event = {
            id = mkn.20
            days = 1
        }
        remove_ideas = MKN_free_territory
        add_ideas = MKN_free_soviets_idea
        add_to_variable = {
            MKN_unified_stability_factor = 0.05
            tooltip = MKN_unified_stability_factor_tt
        }
        add_to_variable = {
            MKN_unified_production_speed_buildings_factor = 0.05
            tooltip = MKN_unified_production_speed_buildings_factor_tt
        }
    }
    x = 31
    y = 11
    allow_branch = {
        NOT = {
            has_country_flag = MKN_crisis_enabled
        }
    }
    cost = 5
}
```

### Рабочий контроль — `MKN_workers_control`

EN: Workers Control.

Описание RU: Завод — тем, кто на нём работает.

Описание EN: The factory to those who work it.

Источник: `common/national_focus/MKN.txt:1415`. Стоимость: 5 (35 дней). Координаты: x=35, y=11.

Предпосылки: (Синдикалистская программа [MKN_council_communism]).

Взаимоисключения: нет.

Прямые продолжения: MKN_commune_federation.

Точные награды (completion_reward), доступность, обход, AI и остальные поля:

```pdx
focus = {
    id = MKN_workers_control
    icon = GFX_focus_generic_industry_1
    prerequisite = {
        focus = MKN_council_communism
    }
    completion_reward = {
        add_stability = 0.05
        add_political_power = 80
        200 = {
            if = {
                limit = {
                    is_owned_and_controlled_by = ROOT
                }
                add_extra_state_shared_building_slots = 1
                add_building_construction = {
                    type = industrial_complex
                    level = 1
                    instant_build = yes
                }
            }
        }
    }
    x = 35
    y = 11
    allow_branch = {
        NOT = {
            has_country_flag = MKN_crisis_enabled
        }
    }
    cost = 5
}
```

## Тактики и штабные проекты

### Полевые штабы: армия — `MKN_army_hq_decisions`

#### Ночные переходы — `MKN_tactic_night_marches`

EN: Night Marches.

Отряды научатся уходить из-под удара ночью без распада колонны.\n\nВыборный командир тоже нуждается в тактической школе и понятной ответственности.\n\nОдноразовая подготовка. Цена: 20 опыта соответствующего рода войск и 10 командного ресурса. Постоянно усиливает его национальный дух.

Оплата, сроки, focus-gates, награды, возврат при отмене и правила региона:

```pdx
MKN_tactic_night_marches = {
    icon = generic_operation
    allowed = {
        original_tag = MKN
    }
    visible = {
        has_completed_focus = MKN_steppe_horde
        NOT = {
            has_country_flag = MKN_tactic_night_marches_unlocked
        }
        NOT = {
            AND = {
                has_country_flag = MKN_military_stat_night_marches
                has_country_flag = MKN_military_stat_militia_junior_leaders
            }
        }
    }
    available = {
        has_capitulated = no
    }
    cost = 0
    fire_only_once = yes
    days_remove = 1
    custom_cost_text = MKN_hq_army_cost
    custom_cost_trigger = {
        NOT = {
            has_army_experience < 20
        }
        NOT = {
            command_power < 10
        }
    }
    complete_effect = {
        army_experience = -20
        add_command_power = -10
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_night_marches
                    }
                }
            }
            add_to_variable = {
                MKN_army_org_loss_when_moving = -0.1
                tooltip = MKN_army_org_loss_when_moving_tt
            }
            set_country_flag = MKN_military_stat_night_marches
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_militia_junior_leaders
                    }
                }
            }
            add_to_variable = {
                MKN_army_army_org_factor = 0.05
                tooltip = MKN_army_army_org_factor_tt
            }
            set_country_flag = MKN_military_stat_militia_junior_leaders
        }
        set_country_flag = MKN_tactic_night_marches_unlocked
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
    }
    ai_will_do = {
        factor = 2
    }
}
```

#### Степная маскировка — `MKN_tactic_steppe_camouflage`

EN: Steppe Camouflage.

Маскировка степных позиций поможет переждать превосходство противника в огне.\n\nСеть тайных складов поддержит колонны вдали от железной дороги.\n\nОдноразовая подготовка. Цена: 20 опыта соответствующего рода войск и 10 командного ресурса. Постоянно усиливает его национальный дух.

Оплата, сроки, focus-gates, награды, возврат при отмене и правила региона:

```pdx
MKN_tactic_steppe_camouflage = {
    icon = generic_operation
    allowed = {
        original_tag = MKN
    }
    visible = {
        has_completed_focus = MKN_steppe_horde
        NOT = {
            has_country_flag = MKN_tactic_steppe_camouflage_unlocked
        }
        NOT = {
            AND = {
                has_country_flag = MKN_military_stat_steppe_camouflage
                has_country_flag = MKN_military_stat_hidden_depots
            }
        }
    }
    available = {
        has_capitulated = no
    }
    cost = 0
    fire_only_once = yes
    days_remove = 1
    custom_cost_text = MKN_hq_army_cost
    custom_cost_trigger = {
        NOT = {
            has_army_experience < 20
        }
        NOT = {
            command_power < 10
        }
    }
    complete_effect = {
        army_experience = -20
        add_command_power = -10
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_steppe_camouflage
                    }
                }
            }
            add_to_variable = {
                MKN_army_max_dig_in = 2
                tooltip = MKN_army_max_dig_in_tt
            }
            set_country_flag = MKN_military_stat_steppe_camouflage
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_hidden_depots
                    }
                }
            }
            add_to_variable = {
                MKN_army_supply_consumption_factor = -0.08
                tooltip = MKN_army_supply_consumption_factor_tt
            }
            set_country_flag = MKN_military_stat_hidden_depots
        }
        set_country_flag = MKN_tactic_steppe_camouflage_unlocked
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
    }
    ai_will_do = {
        factor = 2
    }
}
```

#### Сапёрные десятки — `MKN_tactic_militia_engineers`

EN: Engineer Squads.

Сапёрные десятки подготовят переправы и укрытия лёгкими средствами.\n\nОбщины организуют эвакуацию раненых и восстановление бойцов.\n\nОдноразовая подготовка. Цена: 20 опыта соответствующего рода войск и 10 командного ресурса. Постоянно усиливает его национальный дух.

Оплата, сроки, focus-gates, награды, возврат при отмене и правила региона:

```pdx
MKN_tactic_militia_engineers = {
    icon = generic_operation
    allowed = {
        original_tag = MKN
    }
    visible = {
        has_completed_focus = MKN_steppe_horde
        NOT = {
            has_country_flag = MKN_tactic_militia_engineers_unlocked
        }
        NOT = {
            AND = {
                has_country_flag = MKN_military_stat_militia_engineers
                has_country_flag = MKN_military_stat_militia_hospitals
            }
        }
    }
    available = {
        has_capitulated = no
    }
    cost = 0
    fire_only_once = yes
    days_remove = 1
    custom_cost_text = MKN_hq_army_cost
    custom_cost_trigger = {
        NOT = {
            has_army_experience < 20
        }
        NOT = {
            command_power < 10
        }
    }
    complete_effect = {
        army_experience = -20
        add_command_power = -10
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_militia_engineers
                    }
                }
            }
            add_to_variable = {
                MKN_army_dig_in_speed_factor = 0.2
                tooltip = MKN_army_dig_in_speed_factor_tt
            }
            set_country_flag = MKN_military_stat_militia_engineers
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_militia_hospitals
                    }
                }
            }
            add_to_variable = {
                MKN_army_casualty_trickleback = 0.06
                tooltip = MKN_army_casualty_trickleback_tt
            }
            set_country_flag = MKN_military_stat_militia_hospitals
        }
        set_country_flag = MKN_tactic_militia_engineers_unlocked
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
    }
    ai_will_do = {
        factor = 2
    }
}
```

#### Задача вместо длинного приказа — `MKN_tactic_flexible_orders`

EN: Mission over Lengthy Orders.

Командир получит цель и свободу исполнения вместо цепочки мелких приказов.\n\nСменяемый резерв позволит сельским общинам содержать армию и продолжать посевную.\n\nОдноразовая подготовка. Цена: 20 опыта соответствующего рода войск и 10 командного ресурса. Постоянно усиливает его национальный дух.

Оплата, сроки, focus-gates, награды, возврат при отмене и правила региона:

```pdx
MKN_tactic_flexible_orders = {
    icon = generic_operation
    allowed = {
        original_tag = MKN
    }
    visible = {
        has_completed_focus = MKN_steppe_horde
        NOT = {
            has_country_flag = MKN_tactic_flexible_orders_unlocked
        }
        NOT = {
            AND = {
                has_country_flag = MKN_military_stat_flexible_orders
                has_country_flag = MKN_military_stat_rural_reserve
            }
        }
    }
    available = {
        has_capitulated = no
    }
    cost = 0
    fire_only_once = yes
    days_remove = 1
    custom_cost_text = MKN_hq_army_cost
    custom_cost_trigger = {
        NOT = {
            has_army_experience < 20
        }
        NOT = {
            command_power < 10
        }
    }
    complete_effect = {
        army_experience = -20
        add_command_power = -10
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_flexible_orders
                    }
                }
            }
            add_to_variable = {
                MKN_army_planning_speed = 0.15
                tooltip = MKN_army_planning_speed_tt
            }
            set_country_flag = MKN_military_stat_flexible_orders
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_rural_reserve
                    }
                }
            }
            add_to_variable = {
                MKN_army_conscription = 0.02
                tooltip = MKN_army_conscription_tt
            }
            set_country_flag = MKN_military_stat_rural_reserve
        }
        set_country_flag = MKN_tactic_flexible_orders_unlocked
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
    }
    ai_will_do = {
        factor = 2
    }
}
```

#### Тачанки и пеший заслон — `MKN_tactic_tachanka_tactics`

EN: Tachankas and Infantry Screens.

Пеший заслон прикроет отход тачанок и сорвёт преследование.\n\nПодвижный арьергард задержит врага, пока обозы меняют стоянку.\n\nОдноразовая подготовка. Цена: 20 опыта соответствующего рода войск и 10 командного ресурса. Постоянно усиливает его национальный дух.

Оплата, сроки, focus-gates, награды, возврат при отмене и правила региона:

```pdx
MKN_tactic_tachanka_tactics = {
    icon = generic_operation
    allowed = {
        original_tag = MKN
    }
    visible = {
        has_completed_focus = MKN_steppe_horde
        NOT = {
            has_country_flag = MKN_tactic_tachanka_tactics_unlocked
        }
        NOT = {
            AND = {
                has_country_flag = MKN_military_stat_tachanka_tactics
                has_country_flag = MKN_military_stat_mobile_rearguard
            }
        }
    }
    available = {
        has_capitulated = no
    }
    cost = 0
    fire_only_once = yes
    days_remove = 1
    custom_cost_text = MKN_hq_army_cost
    custom_cost_trigger = {
        NOT = {
            has_army_experience < 20
        }
        NOT = {
            command_power < 10
        }
    }
    complete_effect = {
        army_experience = -20
        add_command_power = -10
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_tachanka_tactics
                    }
                }
            }
            add_to_variable = {
                MKN_army_modifier_army_sub_unit_cavalry_defence_factor = 0.08
                tooltip = MKN_army_modifier_army_sub_unit_cavalry_defence_factor_tt
            }
            set_country_flag = MKN_military_stat_tachanka_tactics
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_mobile_rearguard
                    }
                }
            }
            add_to_variable = {
                MKN_army_modifier_army_sub_unit_infantry_defence_factor = 0.05
                tooltip = MKN_army_modifier_army_sub_unit_infantry_defence_factor_tt
            }
            set_country_flag = MKN_military_stat_mobile_rearguard
        }
        set_country_flag = MKN_tactic_tachanka_tactics_unlocked
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
    }
    ai_will_do = {
        factor = 2
    }
}
```

#### Сборы вольных колонн — `MKN_tactic_free_column_exercises`

EN: Free Column Exercises.

Сборы сведут конные и пешие отряды в согласованные колонны.\n\nОдноразовая подготовка. Цена: 20 опыта соответствующего рода войск и 10 командного ресурса. Постоянно усиливает его национальный дух.

Оплата, сроки, focus-gates, награды, возврат при отмене и правила региона:

```pdx
MKN_tactic_free_column_exercises = {
    icon = generic_operation
    allowed = {
        original_tag = MKN
    }
    visible = {
        has_completed_focus = MKN_steppe_horde
        NOT = {
            has_country_flag = MKN_tactic_free_column_exercises_unlocked
        }
        NOT = {
            AND = {
                has_country_flag = MKN_military_stat_free_column_exercises
            }
        }
    }
    available = {
        has_capitulated = no
    }
    cost = 0
    fire_only_once = yes
    days_remove = 1
    custom_cost_text = MKN_hq_army_cost
    custom_cost_trigger = {
        NOT = {
            has_army_experience < 20
        }
        NOT = {
            command_power < 10
        }
    }
    complete_effect = {
        army_experience = -20
        add_command_power = -10
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_free_column_exercises
                    }
                }
            }
            add_to_variable = {
                MKN_army_army_org_factor = 0.05
                tooltip = MKN_army_army_org_factor_tt
            }
            set_country_flag = MKN_military_stat_free_column_exercises
        }
        set_country_flag = MKN_tactic_free_column_exercises_unlocked
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
    }
    ai_will_do = {
        factor = 2
    }
}
```

#### Пехота вслед за бронёй — `MKN_tactic_motorized_infantry`

EN: Infantry Behind the Armour.

Подвижная пехота закрепит захваченные танками переправы и населённые пункты.\n\nСборные мосты позволят колоннам продолжать наступление за Днепром.\n\nОдноразовая подготовка. Цена: 20 опыта соответствующего рода войск и 10 командного ресурса. Постоянно усиливает его национальный дух.

Оплата, сроки, focus-gates, награды, возврат при отмене и правила региона:

```pdx
MKN_tactic_motorized_infantry = {
    icon = generic_operation
    allowed = {
        original_tag = MKN
    }
    visible = {
        has_completed_focus = MKN_motorized_vanguard
        NOT = {
            has_country_flag = MKN_tactic_motorized_infantry_unlocked
        }
        NOT = {
            AND = {
                has_country_flag = MKN_military_stat_motorized_infantry
                has_country_flag = MKN_military_stat_bridge_columns
            }
        }
    }
    available = {
        has_capitulated = no
    }
    cost = 0
    fire_only_once = yes
    days_remove = 1
    custom_cost_text = MKN_hq_army_cost
    custom_cost_trigger = {
        NOT = {
            has_army_experience < 20
        }
        NOT = {
            command_power < 10
        }
    }
    complete_effect = {
        army_experience = -20
        add_command_power = -10
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_motorized_infantry
                    }
                }
            }
            add_to_variable = {
                MKN_army_modifier_army_sub_unit_infantry_speed_factor = 0.05
                tooltip = MKN_army_modifier_army_sub_unit_infantry_speed_factor_tt
            }
            set_country_flag = MKN_military_stat_motorized_infantry
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_bridge_columns
                    }
                }
            }
            add_to_variable = {
                MKN_army_army_speed_factor = 0.04
                tooltip = MKN_army_army_speed_factor_tt
            }
            set_country_flag = MKN_military_stat_bridge_columns
        }
        set_country_flag = MKN_tactic_motorized_infantry_unlocked
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
    }
    ai_will_do = {
        factor = 2
    }
}
```

#### Учёт горючего в походе — `MKN_tactic_fuel_discipline`

EN: Fuel Accounting on Campaign.

Запас горючего и маршруты заправки избавят наступление от пустых баков.\n\nПроверим планы на штабных играх прежде, чем проверять их людьми.\n\nОдноразовая подготовка. Цена: 20 опыта соответствующего рода войск и 10 командного ресурса. Постоянно усиливает его национальный дух.

Оплата, сроки, focus-gates, награды, возврат при отмене и правила региона:

```pdx
MKN_tactic_fuel_discipline = {
    icon = generic_operation
    allowed = {
        original_tag = MKN
    }
    visible = {
        has_completed_focus = MKN_motorized_vanguard
        NOT = {
            has_country_flag = MKN_tactic_fuel_discipline_unlocked
        }
        NOT = {
            AND = {
                has_country_flag = MKN_military_stat_fuel_discipline
                has_country_flag = MKN_military_stat_staff_games
            }
        }
    }
    available = {
        has_capitulated = no
    }
    cost = 0
    fire_only_once = yes
    days_remove = 1
    custom_cost_text = MKN_hq_army_cost
    custom_cost_trigger = {
        NOT = {
            has_army_experience < 20
        }
        NOT = {
            command_power < 10
        }
    }
    complete_effect = {
        army_experience = -20
        add_command_power = -10
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_fuel_discipline
                    }
                }
            }
            add_to_variable = {
                MKN_army_army_fuel_consumption_factor = -0.1
                tooltip = MKN_army_army_fuel_consumption_factor_tt
            }
            set_country_flag = MKN_military_stat_fuel_discipline
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_staff_games
                    }
                }
            }
            add_to_variable = {
                MKN_army_planning_speed = 0.15
                tooltip = MKN_army_planning_speed_tt
            }
            set_country_flag = MKN_military_stat_staff_games
        }
        set_country_flag = MKN_tactic_fuel_discipline_unlocked
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
    }
    ai_will_do = {
        factor = 2
    }
}
```

#### Подвижные санитарные пункты — `MKN_tactic_mobile_medical`

EN: Mobile Medical Posts.

Санитарные автомобили вернут раненых в строй и сохранят кадры.\n\nБроня, артиллерия и пехота научатся действовать в одном боевом порядке.\n\nОдноразовая подготовка. Цена: 20 опыта соответствующего рода войск и 10 командного ресурса. Постоянно усиливает его национальный дух.

Оплата, сроки, focus-gates, награды, возврат при отмене и правила региона:

```pdx
MKN_tactic_mobile_medical = {
    icon = generic_operation
    allowed = {
        original_tag = MKN
    }
    visible = {
        has_completed_focus = MKN_motorized_vanguard
        NOT = {
            has_country_flag = MKN_tactic_mobile_medical_unlocked
        }
        NOT = {
            AND = {
                has_country_flag = MKN_military_stat_mobile_medical
                has_country_flag = MKN_military_stat_combined_arms
            }
        }
    }
    available = {
        has_capitulated = no
    }
    cost = 0
    fire_only_once = yes
    days_remove = 1
    custom_cost_text = MKN_hq_army_cost
    custom_cost_trigger = {
        NOT = {
            has_army_experience < 20
        }
        NOT = {
            command_power < 10
        }
    }
    complete_effect = {
        army_experience = -20
        add_command_power = -10
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_mobile_medical
                    }
                }
            }
            add_to_variable = {
                MKN_army_casualty_trickleback = 0.05
                tooltip = MKN_army_casualty_trickleback_tt
            }
            set_country_flag = MKN_military_stat_mobile_medical
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_combined_arms
                    }
                }
            }
            add_to_variable = {
                MKN_army_army_armor_attack_factor = 0.05
                tooltip = MKN_army_army_armor_attack_factor_tt
            }
            set_country_flag = MKN_military_stat_combined_arms
        }
        set_country_flag = MKN_tactic_mobile_medical_unlocked
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
    }
    ai_will_do = {
        factor = 2
    }
}
```

#### Резерв второго эшелона — `MKN_tactic_armoured_manoeuvres`

EN: Second Echelon Reserve.

Второй эшелон получит оружие заранее, чтобы поддерживать прорыв без пауз.\n\nМастерские прорыва будут выпускать бронетехнику по требованиям полевых экипажей.\n\nБольшие манёвры отработают смену направления без потери управления.\n\nОдноразовая подготовка. Цена: 20 опыта соответствующего рода войск и 10 командного ресурса. Постоянно усиливает его национальный дух.

Оплата, сроки, focus-gates, награды, возврат при отмене и правила региона:

```pdx
MKN_tactic_armoured_manoeuvres = {
    icon = generic_operation
    allowed = {
        original_tag = MKN
    }
    visible = {
        has_completed_focus = MKN_motorized_vanguard
        NOT = {
            has_country_flag = MKN_tactic_armoured_manoeuvres_unlocked
        }
        NOT = {
            AND = {
                has_country_flag = MKN_military_stat_deep_reserves
                has_country_flag = MKN_military_stat_breakthrough_workshops
                has_country_flag = MKN_military_stat_armoured_manoeuvres
            }
        }
    }
    available = {
        has_capitulated = no
    }
    cost = 0
    fire_only_once = yes
    days_remove = 1
    custom_cost_text = MKN_hq_army_cost
    custom_cost_trigger = {
        NOT = {
            has_army_experience < 20
        }
        NOT = {
            command_power < 10
        }
    }
    complete_effect = {
        army_experience = -20
        add_command_power = -10
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_deep_reserves
                    }
                }
            }
            add_to_variable = {
                MKN_army_land_reinforce_rate = 0.02
                tooltip = MKN_army_land_reinforce_rate_tt
            }
            set_country_flag = MKN_military_stat_deep_reserves
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_breakthrough_workshops
                    }
                }
            }
            add_to_variable = {
                MKN_army_army_armor_attack_factor = 0.04
                tooltip = MKN_army_army_armor_attack_factor_tt
            }
            set_country_flag = MKN_military_stat_breakthrough_workshops
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_armoured_manoeuvres
                    }
                }
            }
            add_to_variable = {
                MKN_army_org_loss_when_moving = -0.1
                tooltip = MKN_army_org_loss_when_moving_tt
            }
            set_country_flag = MKN_military_stat_armoured_manoeuvres
        }
        set_country_flag = MKN_tactic_armoured_manoeuvres_unlocked
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
    }
    ai_will_do = {
        factor = 2
    }
}
```

#### Скрытый узел снабжения — `MKN_project_hidden_supply_node`

EN: Hidden Supply Hub.

Замаскированные склады и подводы свяжут колонны с тылом. За 50 политической власти через 30 дней в выбранном регионе появится один узел снабжения.\n\nЭтот тип проекта доступен один раз за кампанию, в одном выбранном регионе. Требуется полное владение и контроль. При отмене PP/CP возвращаются; повторное начало невозможно.

Оплата, сроки, focus-gates, награды, возврат при отмене и правила региона:

```pdx
MKN_project_hidden_supply_node = {
    icon = generic_construction
    allowed = {
        original_tag = MKN
    }
    state_target = yes
    on_map_mode = map_and_decisions_view
    target_array = ROOT.owned_states
    target_root_trigger = {
        original_tag = MKN
    }
    target_trigger = {
        FROM = {
            is_owned_and_controlled_by = ROOT
        }
    }
    visible = {
        has_completed_focus = MKN_hidden_supply_bases_focus
        NOT = {
            has_country_flag = MKN_project_hidden_supply_node_done
        }
        NOT = {
            has_country_flag = MKN_project_hidden_supply_node_cancelled
        }
    }
    available = {
        has_capitulated = no
        FROM = {
            is_owned_and_controlled_by = ROOT
            is_fully_controlled_by = ROOT
        }
        FROM = {
            supply_node < 1
        }
        hidden_trigger = {
            NOT = {
                has_country_flag = MKN_project_hidden_supply_node_spent
            }
        }
        custom_trigger_tooltip = {
            tooltip = MKN_military_project_idle_tt
            NOT = {
                has_country_flag = MKN_military_project_active
            }
        }
    }
    cost = 50
    days_remove = 30
    fire_only_once = yes
    complete_effect = {
        set_country_flag = MKN_project_hidden_supply_node_spent
        set_country_flag = MKN_military_project_active
    }
    cancel_trigger = {
        NOT = {
            AND = {
                has_capitulated = no
                FROM = {
                    is_owned_and_controlled_by = ROOT
                    is_fully_controlled_by = ROOT
                }
                FROM = {
                    supply_node < 1
                }
            }
        }
    }
    cancel_effect = {
        add_political_power = 50
        set_country_flag = MKN_project_hidden_supply_node_cancelled
        clr_country_flag = MKN_military_project_active
    }
    remove_effect = {
        if = {
            limit = {
                has_capitulated = no
                FROM = {
                    is_owned_and_controlled_by = ROOT
                    is_fully_controlled_by = ROOT
                }
                FROM = {
                    supply_node < 1
                }
            }
            FROM = {
                add_building_construction = {
                    type = supply_node
                    level = 1
                    instant_build = yes
                    province = {
                        all_provinces = no
                    }
                }
            }
            set_country_flag = MKN_project_hidden_supply_node_done
            FROM = {
                set_state_flag = MKN_project_hidden_supply_node_done
            }
        }
        else = {
            add_political_power = 50
            set_country_flag = MKN_project_hidden_supply_node_cancelled
        }
        clr_country_flag = MKN_military_project_active
    }
    ai_will_do = {
        factor = 1
    }
}
```

#### Укладка рельс к фронту — `MKN_project_front_railway`

EN: Lay Rails to the Front.

Железнодорожные артели проложат новую линию первого уровня от столицы к выбранному региону без существующего сообщения. Работы займут 15 дней и потребуют 20 командного ресурса. Маршрут проходит только по нашей территории.\n\nЭтот тип проекта доступен один раз за кампанию, в одном выбранном регионе. Требуется полное владение и контроль. При отмене PP/CP возвращаются; повторное начало невозможно.

Оплата, сроки, focus-gates, награды, возврат при отмене и правила региона:

```pdx
MKN_project_front_railway = {
    icon = generic_construction
    allowed = {
        original_tag = MKN
    }
    state_target = yes
    on_map_mode = map_and_decisions_view
    target_array = ROOT.owned_states
    target_root_trigger = {
        original_tag = MKN
    }
    target_trigger = {
        FROM = {
            is_owned_and_controlled_by = ROOT
        }
    }
    visible = {
        has_completed_focus = MKN_armored_trains_and_repair_focus
        NOT = {
            has_country_flag = MKN_project_front_railway_done
        }
        NOT = {
            has_country_flag = MKN_project_front_railway_cancelled
        }
    }
    available = {
        has_capitulated = no
        FROM = {
            is_owned_and_controlled_by = ROOT
            is_fully_controlled_by = ROOT
        }
        FROM = {
            is_capital = no
        }
        capital_scope = {
            ROOT = {
                can_build_railway = {
                    start_state = PREV
                    target_state = FROM
                    build_only_on_allied = yes
                    controller_priority = {
                        base = -1
                        modifier = {
                            add = 2
                            tag = ROOT
                        }
                    }
                }
                NOT = {
                    has_railway_connection = {
                        start_state = PREV
                        target_state = FROM
                    }
                }
            }
        }
        hidden_trigger = {
            NOT = {
                has_country_flag = MKN_project_front_railway_spent
            }
        }
        custom_trigger_tooltip = {
            tooltip = MKN_military_project_idle_tt
            NOT = {
                has_country_flag = MKN_military_project_active
            }
        }
    }
    cost = 0
    days_remove = 15
    fire_only_once = yes
    custom_cost_text = MKN_hq_20_cp_cost
    custom_cost_trigger = {
        NOT = {
            command_power < 20
        }
    }
    complete_effect = {
        add_command_power = -20
        set_country_flag = MKN_project_front_railway_spent
        set_country_flag = MKN_military_project_active
    }
    cancel_trigger = {
        NOT = {
            AND = {
                has_capitulated = no
                FROM = {
                    is_owned_and_controlled_by = ROOT
                    is_fully_controlled_by = ROOT
                }
                FROM = {
                    is_capital = no
                }
                capital_scope = {
                    ROOT = {
                        can_build_railway = {
                            start_state = PREV
                            target_state = FROM
                            build_only_on_allied = yes
                            controller_priority = {
                                base = -1
                                modifier = {
                                    add = 2
                                    tag = ROOT
                                }
                            }
                        }
                        NOT = {
                            has_railway_connection = {
                                start_state = PREV
                                target_state = FROM
                            }
                        }
                    }
                }
            }
        }
    }
    cancel_effect = {
        add_command_power = 20
        set_country_flag = MKN_project_front_railway_cancelled
        clr_country_flag = MKN_military_project_active
    }
    remove_effect = {
        if = {
            limit = {
                has_capitulated = no
                FROM = {
                    is_owned_and_controlled_by = ROOT
                    is_fully_controlled_by = ROOT
                }
                FROM = {
                    is_capital = no
                }
                capital_scope = {
                    ROOT = {
                        can_build_railway = {
                            start_state = PREV
                            target_state = FROM
                            build_only_on_allied = yes
                            controller_priority = {
                                base = -1
                                modifier = {
                                    add = 2
                                    tag = ROOT
                                }
                            }
                        }
                        NOT = {
                            has_railway_connection = {
                                start_state = PREV
                                target_state = FROM
                            }
                        }
                    }
                }
            }
            capital_scope = {
                ROOT = {
                    build_railway = {
                        level = 1
                        start_state = PREV
                        target_state = FROM
                        build_only_on_allied = yes
                        controller_priority = {
                            base = -1
                            modifier = {
                                add = 2
                                tag = ROOT
                            }
                        }
                    }
                }
            }
            set_country_flag = MKN_project_front_railway_done
            FROM = {
                set_state_flag = MKN_project_front_railway_done
            }
        }
        else = {
            add_command_power = 20
            set_country_flag = MKN_project_front_railway_cancelled
        }
        clr_country_flag = MKN_military_project_active
    }
    ai_will_do = {
        factor = 1
    }
}
```

#### Ремонт инфраструктуры — `MKN_project_repair_infrastructure`

EN: Repair Infrastructure.

Ремонтные команды восстановят повреждённую инфраструктуру выбранного региона за 7 дней и 20 командного ресурса.\n\nЭтот тип проекта доступен один раз за кампанию, в одном выбранном регионе. Требуется полное владение и контроль. При отмене PP/CP возвращаются; повторное начало невозможно.

Оплата, сроки, focus-gates, награды, возврат при отмене и правила региона:

```pdx
MKN_project_repair_infrastructure = {
    icon = generic_construction
    allowed = {
        original_tag = MKN
    }
    state_target = yes
    on_map_mode = map_and_decisions_view
    target_array = ROOT.owned_states
    target_root_trigger = {
        original_tag = MKN
    }
    target_trigger = {
        FROM = {
            is_owned_and_controlled_by = ROOT
        }
    }
    visible = {
        has_completed_focus = MKN_armored_trains_and_repair_focus
        NOT = {
            has_country_flag = MKN_project_repair_infrastructure_done
        }
        NOT = {
            has_country_flag = MKN_project_repair_infrastructure_cancelled
        }
    }
    available = {
        has_capitulated = no
        FROM = {
            is_owned_and_controlled_by = ROOT
            is_fully_controlled_by = ROOT
        }
        FROM = {
            check_variable = {
                var = damaged_building_level@infrastructure
                value = 0
                compare = greater_than
            }
        }
        hidden_trigger = {
            NOT = {
                has_country_flag = MKN_project_repair_infrastructure_spent
            }
        }
        custom_trigger_tooltip = {
            tooltip = MKN_military_project_idle_tt
            NOT = {
                has_country_flag = MKN_military_project_active
            }
        }
    }
    cost = 0
    days_remove = 7
    fire_only_once = yes
    custom_cost_text = MKN_hq_20_cp_cost
    custom_cost_trigger = {
        NOT = {
            command_power < 20
        }
    }
    complete_effect = {
        add_command_power = -20
        set_country_flag = MKN_project_repair_infrastructure_spent
        set_country_flag = MKN_military_project_active
    }
    cancel_trigger = {
        NOT = {
            AND = {
                has_capitulated = no
                FROM = {
                    is_owned_and_controlled_by = ROOT
                    is_fully_controlled_by = ROOT
                }
                FROM = {
                    check_variable = {
                        var = damaged_building_level@infrastructure
                        value = 0
                        compare = greater_than
                    }
                }
            }
        }
    }
    cancel_effect = {
        add_command_power = 20
        set_country_flag = MKN_project_repair_infrastructure_cancelled
        clr_country_flag = MKN_military_project_active
    }
    remove_effect = {
        if = {
            limit = {
                has_capitulated = no
                FROM = {
                    is_owned_and_controlled_by = ROOT
                    is_fully_controlled_by = ROOT
                }
                FROM = {
                    check_variable = {
                        var = damaged_building_level@infrastructure
                        value = 0
                        compare = greater_than
                    }
                }
            }
            FROM = {
                damage_building = {
                    type = infrastructure
                    damage = -5
                }
            }
            set_country_flag = MKN_project_repair_infrastructure_done
            FROM = {
                set_state_flag = MKN_project_repair_infrastructure_done
            }
        }
        else = {
            add_command_power = 20
            set_country_flag = MKN_project_repair_infrastructure_cancelled
        }
        clr_country_flag = MKN_military_project_active
    }
    ai_will_do = {
        factor = 1
    }
}
```

### Полевые штабы: авиация — `MKN_air_hq_decisions`

#### Рассредоточенные аэродромы — `MKN_tactic_air_dispersal`

EN: Dispersed Airfields.

Рассредоточим самолёты по запасным полосам и защитим домашнее небо.\n\nПатрули над переправами прикроют связь между промышленными районами.\n\nОдноразовая подготовка. Цена: 20 опыта соответствующего рода войск и 10 командного ресурса. Постоянно усиливает его национальный дух.

Оплата, сроки, focus-gates, награды, возврат при отмене и правила региона:

```pdx
MKN_tactic_air_dispersal = {
    icon = generic_operation
    allowed = {
        original_tag = MKN
    }
    visible = {
        has_completed_focus = MKN_interceptor_cooperatives
        NOT = {
            has_country_flag = MKN_tactic_air_dispersal_unlocked
        }
        NOT = {
            AND = {
                has_country_flag = MKN_military_stat_air_dispersal
                has_country_flag = MKN_military_stat_fighter_patrols
            }
        }
    }
    available = {
        has_capitulated = no
    }
    cost = 0
    fire_only_once = yes
    days_remove = 1
    custom_cost_text = MKN_hq_air_cost
    custom_cost_trigger = {
        NOT = {
            has_air_experience < 20
        }
        NOT = {
            command_power < 10
        }
    }
    complete_effect = {
        air_experience = -20
        add_command_power = -10
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_air_dispersal
                    }
                }
            }
            add_to_variable = {
                MKN_air_air_home_defence_factor = 0.1
                tooltip = MKN_air_air_home_defence_factor_tt
            }
            set_country_flag = MKN_military_stat_air_dispersal
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_fighter_patrols
                    }
                }
            }
            add_to_variable = {
                MKN_air_air_range_factor = 0.05
                tooltip = MKN_air_air_range_factor_tt
            }
            set_country_flag = MKN_military_stat_fighter_patrols
        }
        set_country_flag = MKN_tactic_air_dispersal_unlocked
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
    }
    ai_will_do = {
        factor = 2
    }
}
```

#### Школа радиолокации — `MKN_tactic_night_interceptors`

EN: Radar School.

Радиолокационная школа научит расчёты сопровождать цели и наводить истребители.\n\nНочные звенья отработают перехват по командам с земли.\n\nОдноразовая подготовка. Цена: 20 опыта соответствующего рода войск и 10 командного ресурса. Постоянно усиливает его национальный дух.

Оплата, сроки, focus-gates, награды, возврат при отмене и правила региона:

```pdx
MKN_tactic_night_interceptors = {
    icon = generic_operation
    allowed = {
        original_tag = MKN
    }
    visible = {
        has_completed_focus = MKN_interceptor_cooperatives
        NOT = {
            has_country_flag = MKN_tactic_night_interceptors_unlocked
        }
        NOT = {
            AND = {
                has_country_flag = MKN_military_stat_air_radar_school
                has_country_flag = MKN_military_stat_night_interceptors
            }
        }
    }
    available = {
        has_capitulated = no
    }
    cost = 0
    fire_only_once = yes
    days_remove = 1
    custom_cost_text = MKN_hq_air_cost
    custom_cost_trigger = {
        NOT = {
            has_air_experience < 20
        }
        NOT = {
            command_power < 10
        }
    }
    complete_effect = {
        air_experience = -20
        add_command_power = -10
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_air_radar_school
                    }
                }
            }
            add_to_variable = {
                MKN_air_air_interception_detect_factor = 0.1
                tooltip = MKN_air_air_interception_detect_factor_tt
            }
            set_country_flag = MKN_military_stat_air_radar_school
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_night_interceptors
                    }
                }
            }
            add_to_variable = {
                MKN_air_air_intercept_efficiency = 0.05
                tooltip = MKN_air_air_intercept_efficiency_tt
            }
            set_country_flag = MKN_military_stat_night_interceptors
        }
        set_country_flag = MKN_tactic_night_interceptors_unlocked
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
    }
    ai_will_do = {
        factor = 2
    }
}
```

#### Общий запас авиационных деталей — `MKN_tactic_fighter_conversion`

EN: Shared Aircraft Spares.

Общий запас моторов сократит простои и аварии изношенных самолётов.\n\nПереучивание позволит быстро освоить следующее поколение истребителей.\n\nОдноразовая подготовка. Цена: 20 опыта соответствующего рода войск и 10 командного ресурса. Постоянно усиливает его национальный дух.

Оплата, сроки, focus-gates, награды, возврат при отмене и правила региона:

```pdx
MKN_tactic_fighter_conversion = {
    icon = generic_operation
    allowed = {
        original_tag = MKN
    }
    visible = {
        has_completed_focus = MKN_interceptor_cooperatives
        NOT = {
            has_country_flag = MKN_tactic_fighter_conversion_unlocked
        }
        NOT = {
            AND = {
                has_country_flag = MKN_military_stat_aircraft_spares
                has_country_flag = MKN_military_stat_fighter_conversion
            }
        }
    }
    available = {
        has_capitulated = no
    }
    cost = 0
    fire_only_once = yes
    days_remove = 1
    custom_cost_text = MKN_hq_air_cost
    custom_cost_trigger = {
        NOT = {
            has_air_experience < 20
        }
        NOT = {
            command_power < 10
        }
    }
    complete_effect = {
        air_experience = -20
        add_command_power = -10
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_aircraft_spares
                    }
                }
            }
            add_to_variable = {
                MKN_air_air_accidents_factor = -0.05
                tooltip = MKN_air_air_accidents_factor_tt
            }
            set_country_flag = MKN_military_stat_aircraft_spares
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_fighter_conversion
                    }
                }
            }
            add_to_variable = {
                MKN_air_air_agility_factor = 0.04
                tooltip = MKN_air_air_agility_factor_tt
            }
            set_country_flag = MKN_military_stat_fighter_conversion
        }
        set_country_flag = MKN_tactic_fighter_conversion_unlocked
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
    }
    ai_will_do = {
        factor = 2
    }
}
```

#### Спасение сбитых лётчиков — `MKN_tactic_air_rescue`

EN: Downed Pilot Rescue.

Спасённый лётчик вернётся к полётам и передаст опыт новым экипажам.\n\nДиспетчеры распределят звенья по целям, исключая бесполезное дублирование.\n\nОдноразовая подготовка. Цена: 20 опыта соответствующего рода войск и 10 командного ресурса. Постоянно усиливает его национальный дух.

Оплата, сроки, focus-gates, награды, возврат при отмене и правила региона:

```pdx
MKN_tactic_air_rescue = {
    icon = generic_operation
    allowed = {
        original_tag = MKN
    }
    visible = {
        has_completed_focus = MKN_interceptor_cooperatives
        NOT = {
            has_country_flag = MKN_tactic_air_rescue_unlocked
        }
        NOT = {
            AND = {
                has_country_flag = MKN_military_stat_air_rescue
                has_country_flag = MKN_military_stat_fighter_controllers
            }
        }
    }
    available = {
        has_capitulated = no
    }
    cost = 0
    fire_only_once = yes
    days_remove = 1
    custom_cost_text = MKN_hq_air_cost
    custom_cost_trigger = {
        NOT = {
            has_air_experience < 20
        }
        NOT = {
            command_power < 10
        }
    }
    complete_effect = {
        air_experience = -20
        add_command_power = -10
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_air_rescue
                    }
                }
            }
            add_to_variable = {
                MKN_air_air_ace_generation_chance_factor = 0.1
                tooltip = MKN_air_air_ace_generation_chance_factor_tt
            }
            set_country_flag = MKN_military_stat_air_rescue
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_fighter_controllers
                    }
                }
            }
            add_to_variable = {
                MKN_air_air_mission_efficiency = 0.05
                tooltip = MKN_air_air_mission_efficiency_tt
            }
            set_country_flag = MKN_military_stat_fighter_controllers
        }
        set_country_flag = MKN_tactic_air_rescue_unlocked
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
    }
    ai_will_do = {
        factor = 2
    }
}
```

#### Защита промышленных районов — `MKN_tactic_sky_watch_exercises`

EN: Industrial Air Defence.

Зенитные батареи и истребители разделят зоны защиты промышленных коммун.\n\nУчения проверят цепочку от обнаружения цели до посадки перехватчика.\n\nОдноразовая подготовка. Цена: 20 опыта соответствующего рода войск и 10 командного ресурса. Постоянно усиливает его национальный дух.

Оплата, сроки, focus-gates, награды, возврат при отмене и правила региона:

```pdx
MKN_tactic_sky_watch_exercises = {
    icon = generic_operation
    allowed = {
        original_tag = MKN
    }
    visible = {
        has_completed_focus = MKN_interceptor_cooperatives
        NOT = {
            has_country_flag = MKN_tactic_sky_watch_exercises_unlocked
        }
        NOT = {
            AND = {
                has_country_flag = MKN_military_stat_air_home_defence
                has_country_flag = MKN_military_stat_sky_watch_exercises
            }
        }
    }
    available = {
        has_capitulated = no
    }
    cost = 0
    fire_only_once = yes
    days_remove = 1
    custom_cost_text = MKN_hq_air_cost
    custom_cost_trigger = {
        NOT = {
            has_air_experience < 20
        }
        NOT = {
            command_power < 10
        }
    }
    complete_effect = {
        air_experience = -20
        add_command_power = -10
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_air_home_defence
                    }
                }
            }
            add_to_variable = {
                MKN_air_air_home_defence_factor = 0.1
                tooltip = MKN_air_air_home_defence_factor_tt
            }
            set_country_flag = MKN_military_stat_air_home_defence
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_sky_watch_exercises
                    }
                }
            }
            add_to_variable = {
                MKN_air_air_attack_factor = 0.04
                tooltip = MKN_air_air_attack_factor_tt
            }
            set_country_flag = MKN_military_stat_sky_watch_exercises
        }
        set_country_flag = MKN_tactic_sky_watch_exercises_unlocked
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
    }
    ai_will_do = {
        factor = 2
    }
}
```

#### Тактическая воздушная разведка — `MKN_tactic_tactical_recon`

EN: Tactical Aerial Reconnaissance.

Воздушная разведка укажет колоннам обходные пути и вражеские резервы.\n\nШтурманы обеспечат поддержку за пределами знакомых аэродромов.\n\nОдноразовая подготовка. Цена: 20 опыта соответствующего рода войск и 10 командного ресурса. Постоянно усиливает его национальный дух.

Оплата, сроки, focus-gates, награды, возврат при отмене и правила региона:

```pdx
MKN_tactic_tactical_recon = {
    icon = generic_operation
    allowed = {
        original_tag = MKN
    }
    visible = {
        has_completed_focus = MKN_flying_artillery_focus
        NOT = {
            has_country_flag = MKN_tactic_tactical_recon_unlocked
        }
        NOT = {
            AND = {
                has_country_flag = MKN_military_stat_tactical_recon
                has_country_flag = MKN_military_stat_bomber_navigation
            }
        }
    }
    available = {
        has_capitulated = no
    }
    cost = 0
    fire_only_once = yes
    days_remove = 1
    custom_cost_text = MKN_hq_air_cost
    custom_cost_trigger = {
        NOT = {
            has_air_experience < 20
        }
        NOT = {
            command_power < 10
        }
    }
    complete_effect = {
        air_experience = -20
        add_command_power = -10
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_tactical_recon
                    }
                }
            }
            add_to_variable = {
                MKN_air_recon_factor = 0.1
                tooltip = MKN_air_recon_factor_tt
            }
            set_country_flag = MKN_military_stat_tactical_recon
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_bomber_navigation
                    }
                }
            }
            add_to_variable = {
                MKN_air_air_range_factor = 0.07
                tooltip = MKN_air_air_range_factor_tt
            }
            set_country_flag = MKN_military_stat_bomber_navigation
        }
        set_country_flag = MKN_tactic_tactical_recon_unlocked
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
    }
    ai_will_do = {
        factor = 2
    }
}
```

#### Доставка срочных грузов — `MKN_tactic_air_supply_lift`

EN: Urgent Air Deliveries.

Воздушные перевозки восполнят самые срочные нужды оторвавшихся колонн.\n\nПриморские эскадрильи прикроют переправы и ударят по кораблям противника.\n\nОдноразовая подготовка. Цена: 20 опыта соответствующего рода войск и 10 командного ресурса. Постоянно усиливает его национальный дух.

Оплата, сроки, focus-gates, награды, возврат при отмене и правила региона:

```pdx
MKN_tactic_air_supply_lift = {
    icon = generic_operation
    allowed = {
        original_tag = MKN
    }
    visible = {
        has_completed_focus = MKN_flying_artillery_focus
        NOT = {
            has_country_flag = MKN_tactic_air_supply_lift_unlocked
        }
        NOT = {
            AND = {
                has_country_flag = MKN_military_stat_air_supply_lift
                has_country_flag = MKN_military_stat_air_coastal_support
            }
        }
    }
    available = {
        has_capitulated = no
    }
    cost = 0
    fire_only_once = yes
    days_remove = 1
    custom_cost_text = MKN_hq_air_cost
    custom_cost_trigger = {
        NOT = {
            has_air_experience < 20
        }
        NOT = {
            command_power < 10
        }
    }
    complete_effect = {
        air_experience = -20
        add_command_power = -10
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_air_supply_lift
                    }
                }
            }
            add_to_variable = {
                MKN_air_supply_consumption_factor = -0.03
                tooltip = MKN_air_supply_consumption_factor_tt
            }
            set_country_flag = MKN_military_stat_air_supply_lift
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_air_coastal_support
                    }
                }
            }
            add_to_variable = {
                MKN_air_naval_strike_attack_factor = 0.1
                tooltip = MKN_air_naval_strike_attack_factor_tt
            }
            set_country_flag = MKN_military_stat_air_coastal_support
        }
        set_country_flag = MKN_tactic_air_supply_lift_unlocked
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
    }
    ai_will_do = {
        factor = 2
    }
}
```

#### Резерв экипажей штурмовиков — `MKN_tactic_replacement_crews`

EN: Attack Crew Reserve.

Резерв подготовленных экипажей позволит сохранять темп вылетов.\n\nСменяемые группы распределят нагрузку между людьми, машинами и складами горючего.\n\nОдноразовая подготовка. Цена: 20 опыта соответствующего рода войск и 10 командного ресурса. Постоянно усиливает его национальный дух.

Оплата, сроки, focus-gates, награды, возврат при отмене и правила региона:

```pdx
MKN_tactic_replacement_crews = {
    icon = generic_operation
    allowed = {
        original_tag = MKN
    }
    visible = {
        has_completed_focus = MKN_flying_artillery_focus
        NOT = {
            has_country_flag = MKN_tactic_replacement_crews_unlocked
        }
        NOT = {
            AND = {
                has_country_flag = MKN_military_stat_cas_replacement_crews
                has_country_flag = MKN_military_stat_attack_wing_rotations
            }
        }
    }
    available = {
        has_capitulated = no
    }
    cost = 0
    fire_only_once = yes
    days_remove = 1
    custom_cost_text = MKN_hq_air_cost
    custom_cost_trigger = {
        NOT = {
            has_air_experience < 20
        }
        NOT = {
            command_power < 10
        }
    }
    complete_effect = {
        air_experience = -20
        add_command_power = -10
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_cas_replacement_crews
                    }
                }
            }
            add_to_variable = {
                MKN_air_air_accidents_factor = -0.05
                tooltip = MKN_air_air_accidents_factor_tt
            }
            set_country_flag = MKN_military_stat_cas_replacement_crews
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_attack_wing_rotations
                    }
                }
            }
            add_to_variable = {
                MKN_air_air_fuel_consumption_factor = -0.05
                tooltip = MKN_air_air_fuel_consumption_factor_tt
            }
            set_country_flag = MKN_military_stat_attack_wing_rotations
        }
        set_country_flag = MKN_tactic_replacement_crews_unlocked
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
    }
    ai_will_do = {
        factor = 2
    }
}
```

#### Топливные склады эскадрилий — `MKN_tactic_weather_service`

EN: Squadron Fuel Depots.

Наладим заправку, чтобы ударные группы не пропускали решающий вылет.\n\nМетеопосты помогут выбирать окно для удара вместо отмены всей операции.\n\nОдноразовая подготовка. Цена: 20 опыта соответствующего рода войск и 10 командного ресурса. Постоянно усиливает его национальный дух.

Оплата, сроки, focus-gates, награды, возврат при отмене и правила региона:

```pdx
MKN_tactic_weather_service = {
    icon = generic_operation
    allowed = {
        original_tag = MKN
    }
    visible = {
        has_completed_focus = MKN_flying_artillery_focus
        NOT = {
            has_country_flag = MKN_tactic_weather_service_unlocked
        }
        NOT = {
            AND = {
                has_country_flag = MKN_military_stat_airfield_fuel
                has_country_flag = MKN_military_stat_air_weather_service
            }
        }
    }
    available = {
        has_capitulated = no
    }
    cost = 0
    fire_only_once = yes
    days_remove = 1
    custom_cost_text = MKN_hq_air_cost
    custom_cost_trigger = {
        NOT = {
            has_air_experience < 20
        }
        NOT = {
            command_power < 10
        }
    }
    complete_effect = {
        air_experience = -20
        add_command_power = -10
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_airfield_fuel
                    }
                }
            }
            add_to_variable = {
                MKN_air_air_fuel_consumption_factor = -0.1
                tooltip = MKN_air_air_fuel_consumption_factor_tt
            }
            set_country_flag = MKN_military_stat_airfield_fuel
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_air_weather_service
                    }
                }
            }
            add_to_variable = {
                MKN_air_air_mission_efficiency = 0.04
                tooltip = MKN_air_air_mission_efficiency_tt
            }
            set_country_flag = MKN_military_stat_air_weather_service
        }
        set_country_flag = MKN_tactic_weather_service_unlocked
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
    }
    ai_will_do = {
        factor = 2
    }
}
```

#### Совместное планирование ударов — `MKN_tactic_joint_target_planning`

EN: Joint Strike Planning.

Штабы армии и авиации составят общие списки целей перед наступлением.\n\nСовместные учения проверят взаимодействие пилотов, артиллеристов и передовых наблюдателей.\n\nОдноразовая подготовка. Цена: 20 опыта соответствующего рода войск и 10 командного ресурса. Постоянно усиливает его национальный дух.

Оплата, сроки, focus-gates, награды, возврат при отмене и правила региона:

```pdx
MKN_tactic_joint_target_planning = {
    icon = generic_operation
    allowed = {
        original_tag = MKN
    }
    visible = {
        has_completed_focus = MKN_flying_artillery_focus
        NOT = {
            has_country_flag = MKN_tactic_joint_target_planning_unlocked
        }
        NOT = {
            AND = {
                has_country_flag = MKN_military_stat_joint_target_planning
                has_country_flag = MKN_military_stat_cas_joint_exercises
            }
        }
    }
    available = {
        has_capitulated = no
    }
    cost = 0
    fire_only_once = yes
    days_remove = 1
    custom_cost_text = MKN_hq_air_cost
    custom_cost_trigger = {
        NOT = {
            has_air_experience < 20
        }
        NOT = {
            command_power < 10
        }
    }
    complete_effect = {
        air_experience = -20
        add_command_power = -10
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_joint_target_planning
                    }
                }
            }
            add_to_variable = {
                MKN_air_air_cas_efficiency = 0.05
                tooltip = MKN_air_air_cas_efficiency_tt
            }
            set_country_flag = MKN_military_stat_joint_target_planning
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_cas_joint_exercises
                    }
                }
            }
            add_to_variable = {
                MKN_air_air_cas_efficiency = 0.05
                tooltip = MKN_air_air_cas_efficiency_tt
            }
            set_country_flag = MKN_military_stat_cas_joint_exercises
        }
        set_country_flag = MKN_tactic_joint_target_planning_unlocked
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
    }
    ai_will_do = {
        factor = 2
    }
}
```

#### Наблюдательные посты — `MKN_project_observation_posts`

EN: Observation Posts.

После исследования радиолокации две гражданские фабрики за 45 дней оборудуют первую радарную станцию в выбранном регионе.\n\nЭтот тип проекта доступен один раз за кампанию, в одном выбранном регионе. Требуется полное владение и контроль. При отмене PP/CP возвращаются; повторное начало невозможно.

Оплата, сроки, focus-gates, награды, возврат при отмене и правила региона:

```pdx
MKN_project_observation_posts = {
    icon = generic_construction
    allowed = {
        original_tag = MKN
    }
    state_target = yes
    on_map_mode = map_and_decisions_view
    target_array = ROOT.owned_states
    target_root_trigger = {
        original_tag = MKN
    }
    target_trigger = {
        FROM = {
            is_owned_and_controlled_by = ROOT
        }
    }
    visible = {
        has_completed_focus = MKN_communal_aa_defense_focus
        NOT = {
            has_country_flag = MKN_project_observation_posts_done
        }
        NOT = {
            has_country_flag = MKN_project_observation_posts_cancelled
        }
    }
    available = {
        has_capitulated = no
        FROM = {
            is_owned_and_controlled_by = ROOT
            is_fully_controlled_by = ROOT
        }
        has_tech = radio_detection
        FROM = {
            radar_station < 1
        }
        hidden_trigger = {
            NOT = {
                has_country_flag = MKN_project_observation_posts_spent
            }
        }
        custom_trigger_tooltip = {
            tooltip = MKN_military_project_idle_tt
            NOT = {
                has_country_flag = MKN_military_project_active
            }
        }
        num_of_civilian_factories_available_for_projects > 1
    }
    cost = 0
    days_remove = 45
    fire_only_once = yes
    modifier = {
        civilian_factory_use = 2
    }
    complete_effect = {
        set_country_flag = MKN_project_observation_posts_spent
        set_country_flag = MKN_military_project_active
    }
    cancel_trigger = {
        NOT = {
            AND = {
                has_capitulated = no
                FROM = {
                    is_owned_and_controlled_by = ROOT
                    is_fully_controlled_by = ROOT
                }
                has_tech = radio_detection
                FROM = {
                    radar_station < 1
                }
            }
        }
    }
    cancel_effect = {
        set_country_flag = MKN_project_observation_posts_cancelled
        clr_country_flag = MKN_military_project_active
    }
    remove_effect = {
        if = {
            limit = {
                has_capitulated = no
                FROM = {
                    is_owned_and_controlled_by = ROOT
                    is_fully_controlled_by = ROOT
                }
                has_tech = radio_detection
                FROM = {
                    radar_station < 1
                }
            }
            FROM = {
                add_building_construction = {
                    type = radar_station
                    level = 1
                    instant_build = yes
                }
            }
            set_country_flag = MKN_project_observation_posts_done
            FROM = {
                set_state_flag = MKN_project_observation_posts_done
            }
        }
        else = {
            set_country_flag = MKN_project_observation_posts_cancelled
        }
        clr_country_flag = MKN_military_project_active
    }
    ai_will_do = {
        factor = 1
    }
}
```

#### Зенитные батареи — `MKN_project_aa_batteries`

EN: Anti-Aircraft Batteries.

Две гражданские фабрики за 45 дней оборудуют один уровень стационарной ПВО для защиты коммун.\n\nЭтот тип проекта доступен один раз за кампанию, в одном выбранном регионе. Требуется полное владение и контроль. При отмене PP/CP возвращаются; повторное начало невозможно.

Оплата, сроки, focus-gates, награды, возврат при отмене и правила региона:

```pdx
MKN_project_aa_batteries = {
    icon = generic_construction
    allowed = {
        original_tag = MKN
    }
    state_target = yes
    on_map_mode = map_and_decisions_view
    target_array = ROOT.owned_states
    target_root_trigger = {
        original_tag = MKN
    }
    target_trigger = {
        FROM = {
            is_owned_and_controlled_by = ROOT
        }
    }
    visible = {
        has_completed_focus = MKN_communal_aa_defense_focus
        NOT = {
            has_country_flag = MKN_project_aa_batteries_done
        }
        NOT = {
            has_country_flag = MKN_project_aa_batteries_cancelled
        }
    }
    available = {
        has_capitulated = no
        FROM = {
            is_owned_and_controlled_by = ROOT
            is_fully_controlled_by = ROOT
        }
        FROM = {
            anti_air_building < 5
        }
        hidden_trigger = {
            NOT = {
                has_country_flag = MKN_project_aa_batteries_spent
            }
        }
        custom_trigger_tooltip = {
            tooltip = MKN_military_project_idle_tt
            NOT = {
                has_country_flag = MKN_military_project_active
            }
        }
        num_of_civilian_factories_available_for_projects > 1
    }
    cost = 0
    days_remove = 45
    fire_only_once = yes
    modifier = {
        civilian_factory_use = 2
    }
    complete_effect = {
        set_country_flag = MKN_project_aa_batteries_spent
        set_country_flag = MKN_military_project_active
    }
    cancel_trigger = {
        NOT = {
            AND = {
                has_capitulated = no
                FROM = {
                    is_owned_and_controlled_by = ROOT
                    is_fully_controlled_by = ROOT
                }
                FROM = {
                    anti_air_building < 5
                }
            }
        }
    }
    cancel_effect = {
        set_country_flag = MKN_project_aa_batteries_cancelled
        clr_country_flag = MKN_military_project_active
    }
    remove_effect = {
        if = {
            limit = {
                has_capitulated = no
                FROM = {
                    is_owned_and_controlled_by = ROOT
                    is_fully_controlled_by = ROOT
                }
                FROM = {
                    anti_air_building < 5
                }
            }
            FROM = {
                add_building_construction = {
                    type = anti_air_building
                    level = 1
                    instant_build = yes
                }
            }
            set_country_flag = MKN_project_aa_batteries_done
            FROM = {
                set_state_flag = MKN_project_aa_batteries_done
            }
        }
        else = {
            set_country_flag = MKN_project_aa_batteries_cancelled
        }
        clr_country_flag = MKN_military_project_active
    }
    ai_will_do = {
        factor = 1
    }
}
```

#### Степной аэродром — `MKN_project_forward_airstrip`

EN: Steppe Airfield.

За 30 политической власти артели за 15 дней добавят один уровень авиабазы в регионе, соседнем с территорией под контролем противника.\n\nЭтот тип проекта доступен один раз за кампанию, в одном выбранном регионе. Требуется полное владение и контроль. При отмене PP/CP возвращаются; повторное начало невозможно.

Оплата, сроки, focus-gates, награды, возврат при отмене и правила региона:

```pdx
MKN_project_forward_airstrip = {
    icon = generic_construction
    allowed = {
        original_tag = MKN
    }
    state_target = yes
    on_map_mode = map_and_decisions_view
    target_array = ROOT.owned_states
    target_root_trigger = {
        original_tag = MKN
    }
    target_trigger = {
        FROM = {
            is_owned_and_controlled_by = ROOT
        }
    }
    visible = {
        has_completed_focus = MKN_forward_airstrips_focus
        NOT = {
            has_country_flag = MKN_project_forward_airstrip_done
        }
        NOT = {
            has_country_flag = MKN_project_forward_airstrip_cancelled
        }
    }
    available = {
        has_capitulated = no
        FROM = {
            is_owned_and_controlled_by = ROOT
            is_fully_controlled_by = ROOT
        }
        FROM = {
            air_base < 10
            any_neighbor_state = {
                controller = {
                    has_war_with = ROOT
                }
            }
        }
        hidden_trigger = {
            NOT = {
                has_country_flag = MKN_project_forward_airstrip_spent
            }
        }
        custom_trigger_tooltip = {
            tooltip = MKN_military_project_idle_tt
            NOT = {
                has_country_flag = MKN_military_project_active
            }
        }
    }
    cost = 30
    days_remove = 15
    fire_only_once = yes
    complete_effect = {
        set_country_flag = MKN_project_forward_airstrip_spent
        set_country_flag = MKN_military_project_active
    }
    cancel_trigger = {
        NOT = {
            AND = {
                has_capitulated = no
                FROM = {
                    is_owned_and_controlled_by = ROOT
                    is_fully_controlled_by = ROOT
                }
                FROM = {
                    air_base < 10
                    any_neighbor_state = {
                        controller = {
                            has_war_with = ROOT
                        }
                    }
                }
            }
        }
    }
    cancel_effect = {
        add_political_power = 30
        set_country_flag = MKN_project_forward_airstrip_cancelled
        clr_country_flag = MKN_military_project_active
    }
    remove_effect = {
        if = {
            limit = {
                has_capitulated = no
                FROM = {
                    is_owned_and_controlled_by = ROOT
                    is_fully_controlled_by = ROOT
                }
                FROM = {
                    air_base < 10
                    any_neighbor_state = {
                        controller = {
                            has_war_with = ROOT
                        }
                    }
                }
            }
            FROM = {
                add_building_construction = {
                    type = air_base
                    level = 1
                    instant_build = yes
                }
            }
            set_country_flag = MKN_project_forward_airstrip_done
            FROM = {
                set_state_flag = MKN_project_forward_airstrip_done
            }
        }
        else = {
            add_political_power = 30
            set_country_flag = MKN_project_forward_airstrip_cancelled
        }
        clr_country_flag = MKN_military_project_active
    }
    ai_will_do = {
        factor = 1
    }
}
```

### Полевые штабы: флот — `MKN_navy_hq_decisions`

#### Артели аварийного ремонта — `MKN_tactic_damage_control`

EN: Repair and Salvage Artels.

Аварийные команды спасут корабль после попадания и вернут его в порт.\n\nПостоянный дозор закроет промежутки между портовыми районами.\n\nОдноразовая подготовка. Цена: 20 опыта соответствующего рода войск и 10 командного ресурса. Постоянно усиливает его национальный дух.

Оплата, сроки, focus-gates, награды, возврат при отмене и правила региона:

```pdx
MKN_tactic_damage_control = {
    icon = generic_operation
    allowed = {
        original_tag = MKN
    }
    visible = {
        has_completed_focus = MKN_sea_escort_service
        NOT = {
            has_country_flag = MKN_tactic_damage_control_unlocked
        }
        NOT = {
            AND = {
                has_country_flag = MKN_military_stat_fleet_damage_control
                has_country_flag = MKN_military_stat_coastal_watch
            }
        }
    }
    available = {
        has_capitulated = no
    }
    cost = 0
    fire_only_once = yes
    days_remove = 1
    custom_cost_text = MKN_hq_navy_cost
    custom_cost_trigger = {
        NOT = {
            has_navy_experience < 20
        }
        NOT = {
            command_power < 10
        }
    }
    complete_effect = {
        navy_experience = -20
        add_command_power = -10
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_fleet_damage_control
                    }
                }
            }
            add_to_variable = {
                MKN_navy_naval_ship_recovery_chance_factor = 0.1
                tooltip = MKN_navy_naval_ship_recovery_chance_factor_tt
            }
            set_country_flag = MKN_military_stat_fleet_damage_control
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_coastal_watch
                    }
                }
            }
            add_to_variable = {
                MKN_navy_naval_detection = 0.08
                tooltip = MKN_navy_naval_detection_tt
            }
            set_country_flag = MKN_military_stat_coastal_watch
        }
        set_country_flag = MKN_tactic_damage_control_unlocked
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
    }
    ai_will_do = {
        factor = 2
    }
}
```

#### Тральные отряды — `MKN_tactic_sweeper_sections`

EN: Minesweeper Sections.

Тральные команды очистят торговые фарватеры от мин.\n\nОбщая частота охранения позволит быстро перестроить защитный экран.\n\nОдноразовая подготовка. Цена: 20 опыта соответствующего рода войск и 10 командного ресурса. Постоянно усиливает его национальный дух.

Оплата, сроки, focus-gates, награды, возврат при отмене и правила региона:

```pdx
MKN_tactic_sweeper_sections = {
    icon = generic_operation
    allowed = {
        original_tag = MKN
    }
    visible = {
        has_completed_focus = MKN_sea_escort_service
        NOT = {
            has_country_flag = MKN_tactic_sweeper_sections_unlocked
        }
        NOT = {
            AND = {
                has_country_flag = MKN_military_stat_sweeper_sections
                has_country_flag = MKN_military_stat_escort_radio_net
            }
        }
    }
    available = {
        has_capitulated = no
    }
    cost = 0
    fire_only_once = yes
    days_remove = 1
    custom_cost_text = MKN_hq_navy_cost
    custom_cost_trigger = {
        NOT = {
            has_navy_experience < 20
        }
        NOT = {
            command_power < 10
        }
    }
    complete_effect = {
        navy_experience = -20
        add_command_power = -10
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_sweeper_sections
                    }
                }
            }
            add_to_variable = {
                MKN_navy_mines_sweeping_by_fleets_factor = 0.25
                tooltip = MKN_navy_mines_sweeping_by_fleets_factor_tt
            }
            set_country_flag = MKN_military_stat_sweeper_sections
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_escort_radio_net
                    }
                }
            }
            add_to_variable = {
                MKN_navy_screening_efficiency = 0.07
                tooltip = MKN_navy_screening_efficiency_tt
            }
            set_country_flag = MKN_military_stat_escort_radio_net
        }
        set_country_flag = MKN_tactic_sweeper_sections_unlocked
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
    }
    ai_will_do = {
        factor = 2
    }
}
```

#### Портовые склады снабжения — `MKN_tactic_coastal_depots`

EN: Port Supply Depots.

Прибрежные склады поддержат длительное патрулирование без дальних переходов на заправку.\n\nСогласуем речные перевозки, морской эскорт и береговую разведку.\n\nОдноразовая подготовка. Цена: 20 опыта соответствующего рода войск и 10 командного ресурса. Постоянно усиливает его национальный дух.

Оплата, сроки, focus-gates, награды, возврат при отмене и правила региона:

```pdx
MKN_tactic_coastal_depots = {
    icon = generic_operation
    allowed = {
        original_tag = MKN
    }
    visible = {
        has_completed_focus = MKN_sea_escort_service
        NOT = {
            has_country_flag = MKN_tactic_coastal_depots_unlocked
        }
        NOT = {
            AND = {
                has_country_flag = MKN_military_stat_coastal_depots
                has_country_flag = MKN_military_stat_river_sea_coordination
            }
        }
    }
    available = {
        has_capitulated = no
    }
    cost = 0
    fire_only_once = yes
    days_remove = 1
    custom_cost_text = MKN_hq_navy_cost
    custom_cost_trigger = {
        NOT = {
            has_navy_experience < 20
        }
        NOT = {
            command_power < 10
        }
    }
    complete_effect = {
        navy_experience = -20
        add_command_power = -10
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_coastal_depots
                    }
                }
            }
            add_to_variable = {
                MKN_navy_navy_fuel_consumption_factor = -0.1
                tooltip = MKN_navy_navy_fuel_consumption_factor_tt
            }
            set_country_flag = MKN_military_stat_coastal_depots
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_river_sea_coordination
                    }
                }
            }
            add_to_variable = {
                MKN_navy_naval_coordination = 0.08
                tooltip = MKN_navy_naval_coordination_tt
            }
            set_country_flag = MKN_military_stat_river_sea_coordination
        }
        set_country_flag = MKN_tactic_coastal_depots_unlocked
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
    }
    ai_will_do = {
        factor = 2
    }
}
```

#### Противолодочные патрули — `MKN_tactic_convoy_rescue`

EN: Anti Submarine Patrols.

Охотничьи группы будут прочёсывать район перед выходом конвоев.\n\nСпасательные суда подберут людей и возьмут повреждённые транспорты на буксир.\n\nОдноразовая подготовка. Цена: 20 опыта соответствующего рода войск и 10 командного ресурса. Постоянно усиливает его национальный дух.

Оплата, сроки, focus-gates, награды, возврат при отмене и правила региона:

```pdx
MKN_tactic_convoy_rescue = {
    icon = generic_operation
    allowed = {
        original_tag = MKN
    }
    visible = {
        has_completed_focus = MKN_sea_escort_service
        NOT = {
            has_country_flag = MKN_tactic_convoy_rescue_unlocked
        }
        NOT = {
            AND = {
                has_country_flag = MKN_military_stat_anti_submarine_patrols
                has_country_flag = MKN_military_stat_convoy_rescue
            }
        }
    }
    available = {
        has_capitulated = no
    }
    cost = 0
    fire_only_once = yes
    days_remove = 1
    custom_cost_text = MKN_hq_navy_cost
    custom_cost_trigger = {
        NOT = {
            has_navy_experience < 20
        }
        NOT = {
            command_power < 10
        }
    }
    complete_effect = {
        navy_experience = -20
        add_command_power = -10
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_anti_submarine_patrols
                    }
                }
            }
            add_to_variable = {
                MKN_navy_navy_submarine_detection_factor = 0.15
                tooltip = MKN_navy_navy_submarine_detection_factor_tt
            }
            set_country_flag = MKN_military_stat_anti_submarine_patrols
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_convoy_rescue
                    }
                }
            }
            add_to_variable = {
                MKN_navy_navy_casualty_on_sink = -0.1
                tooltip = MKN_navy_navy_casualty_on_sink_tt
            }
            set_country_flag = MKN_military_stat_convoy_rescue
        }
        set_country_flag = MKN_tactic_convoy_rescue_unlocked
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
    }
    ai_will_do = {
        factor = 2
    }
}
```

#### Резерв портовых экипажей — `MKN_tactic_coastal_fleet_exercises`

EN: Port Crew Reserve.

Резерв экипажей и дополнительная верфь обеспечат замену потерь.\n\nПроверим охранение торгового каравана в условиях учебной атаки.\n\nОдноразовая подготовка. Цена: 20 опыта соответствующего рода войск и 10 командного ресурса. Постоянно усиливает его национальный дух.

Оплата, сроки, focus-gates, награды, возврат при отмене и правила региона:

```pdx
MKN_tactic_coastal_fleet_exercises = {
    icon = generic_operation
    allowed = {
        original_tag = MKN
    }
    visible = {
        has_completed_focus = MKN_sea_escort_service
        NOT = {
            has_country_flag = MKN_tactic_coastal_fleet_exercises_unlocked
        }
        NOT = {
            AND = {
                has_country_flag = MKN_military_stat_escort_reserves
                has_country_flag = MKN_military_stat_coastal_fleet_exercises
            }
        }
    }
    available = {
        has_capitulated = no
    }
    cost = 0
    fire_only_once = yes
    days_remove = 1
    custom_cost_text = MKN_hq_navy_cost
    custom_cost_trigger = {
        NOT = {
            has_navy_experience < 20
        }
        NOT = {
            command_power < 10
        }
    }
    complete_effect = {
        navy_experience = -20
        add_command_power = -10
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_escort_reserves
                    }
                }
            }
            add_to_variable = {
                MKN_navy_naval_defense_factor = 0.05
                tooltip = MKN_navy_naval_defense_factor_tt
            }
            set_country_flag = MKN_military_stat_escort_reserves
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_coastal_fleet_exercises
                    }
                }
            }
            add_to_variable = {
                MKN_navy_convoy_escort_efficiency = 0.05
                tooltip = MKN_navy_convoy_escort_efficiency_tt
            }
            set_country_flag = MKN_military_stat_coastal_fleet_exercises
        }
        set_country_flag = MKN_tactic_coastal_fleet_exercises_unlocked
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
    }
    ai_will_do = {
        factor = 2
    }
}
```

#### Школа гидроакустиков — `MKN_tactic_submarine_listening`

EN: Hydrophone School.

Гидроакустики услышат цель раньше, чем противник заметит подлодку.\n\nБыстрые катера прикроют выход рейдеров и атакуют в тесных прибрежных водах.\n\nОдноразовая подготовка. Цена: 20 опыта соответствующего рода войск и 10 командного ресурса. Постоянно усиливает его национальный дух.

Оплата, сроки, focus-gates, награды, возврат при отмене и правила региона:

```pdx
MKN_tactic_submarine_listening = {
    icon = generic_operation
    allowed = {
        original_tag = MKN
    }
    visible = {
        has_completed_focus = MKN_torpedo_artels_focus
        NOT = {
            has_country_flag = MKN_tactic_submarine_listening_unlocked
        }
        NOT = {
            AND = {
                has_country_flag = MKN_military_stat_submarine_listening
                has_country_flag = MKN_military_stat_fast_attack_craft
            }
        }
    }
    available = {
        has_capitulated = no
    }
    cost = 0
    fire_only_once = yes
    days_remove = 1
    custom_cost_text = MKN_hq_navy_cost
    custom_cost_trigger = {
        NOT = {
            has_navy_experience < 20
        }
        NOT = {
            command_power < 10
        }
    }
    complete_effect = {
        navy_experience = -20
        add_command_power = -10
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_submarine_listening
                    }
                }
            }
            add_to_variable = {
                MKN_navy_naval_detection = 0.08
                tooltip = MKN_navy_naval_detection_tt
            }
            set_country_flag = MKN_military_stat_submarine_listening
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_fast_attack_craft
                    }
                }
            }
            add_to_variable = {
                MKN_navy_naval_speed_factor = 0.08
                tooltip = MKN_navy_naval_speed_factor_tt
            }
            set_country_flag = MKN_military_stat_fast_attack_craft
        }
        set_country_flag = MKN_tactic_submarine_listening_unlocked
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
    }
    ai_will_do = {
        factor = 2
    }
}
```

#### Радиодисциплина рейдеров — `MKN_tactic_radio_discipline`

EN: Raider Radio Discipline.

Короткие зашифрованные передачи затруднят поиск рейдерских групп.\n\nРемонтные бригады восстановят механизмы между боевыми походами.\n\nОдноразовая подготовка. Цена: 20 опыта соответствующего рода войск и 10 командного ресурса. Постоянно усиливает его национальный дух.

Оплата, сроки, focus-gates, награды, возврат при отмене и правила региона:

```pdx
MKN_tactic_radio_discipline = {
    icon = generic_operation
    allowed = {
        original_tag = MKN
    }
    visible = {
        has_completed_focus = MKN_torpedo_artels_focus
        NOT = {
            has_country_flag = MKN_tactic_radio_discipline_unlocked
        }
        NOT = {
            AND = {
                has_country_flag = MKN_military_stat_raider_radio_discipline
                has_country_flag = MKN_military_stat_submarine_repair
            }
        }
    }
    available = {
        has_capitulated = no
    }
    cost = 0
    fire_only_once = yes
    days_remove = 1
    custom_cost_text = MKN_hq_navy_cost
    custom_cost_trigger = {
        NOT = {
            has_navy_experience < 20
        }
        NOT = {
            command_power < 10
        }
    }
    complete_effect = {
        navy_experience = -20
        add_command_power = -10
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_raider_radio_discipline
                    }
                }
            }
            add_to_variable = {
                MKN_navy_naval_torpedo_reveal_chance_factor = -0.08
                tooltip = MKN_navy_naval_torpedo_reveal_chance_factor_tt
            }
            set_country_flag = MKN_military_stat_raider_radio_discipline
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_submarine_repair
                    }
                }
            }
            add_to_variable = {
                MKN_navy_repair_speed_factor = 0.15
                tooltip = MKN_navy_repair_speed_factor_tt
            }
            set_country_flag = MKN_military_stat_submarine_repair
        }
        set_country_flag = MKN_tactic_radio_discipline_unlocked
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
    }
    ai_will_do = {
        factor = 2
    }
}
```

#### Погода как союзник — `MKN_tactic_raider_weather`

EN: Weather as an Ally.

Метеосводки помогут использовать плохую видимость для подхода к цели.\n\nРезервные экипажи отработают аварийное погружение и уклонение от охотников.\n\nОдноразовая подготовка. Цена: 20 опыта соответствующего рода войск и 10 командного ресурса. Постоянно усиливает его национальный дух.

Оплата, сроки, focus-gates, награды, возврат при отмене и правила региона:

```pdx
MKN_tactic_raider_weather = {
    icon = generic_operation
    allowed = {
        original_tag = MKN
    }
    visible = {
        has_completed_focus = MKN_torpedo_artels_focus
        NOT = {
            has_country_flag = MKN_tactic_raider_weather_unlocked
        }
        NOT = {
            AND = {
                has_country_flag = MKN_military_stat_raider_weather
                has_country_flag = MKN_military_stat_raider_replacement_crews
            }
        }
    }
    available = {
        has_capitulated = no
    }
    cost = 0
    fire_only_once = yes
    days_remove = 1
    custom_cost_text = MKN_hq_navy_cost
    custom_cost_trigger = {
        NOT = {
            has_navy_experience < 20
        }
        NOT = {
            command_power < 10
        }
    }
    complete_effect = {
        navy_experience = -20
        add_command_power = -10
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_raider_weather
                    }
                }
            }
            add_to_variable = {
                MKN_navy_naval_detection = 0.05
                tooltip = MKN_navy_naval_detection_tt
            }
            set_country_flag = MKN_military_stat_raider_weather
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_raider_replacement_crews
                    }
                }
            }
            add_to_variable = {
                MKN_navy_navy_submarine_defence_factor = 0.08
                tooltip = MKN_navy_navy_submarine_defence_factor_tt
            }
            set_country_flag = MKN_military_stat_raider_replacement_crews
        }
        set_country_flag = MKN_tactic_raider_weather_unlocked
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
    }
    ai_will_do = {
        factor = 2
    }
}
```

#### Торпедные засады — `MKN_tactic_torpedo_ambushes`

EN: Torpedo Ambushes.

Засады у узких проходов позволят сосредоточить торпедный залп.\n\nРаспределим районы охоты, чтобы лишать противника снабжения систематически.\n\nОдноразовая подготовка. Цена: 20 опыта соответствующего рода войск и 10 командного ресурса. Постоянно усиливает его национальный дух.

Оплата, сроки, focus-gates, награды, возврат при отмене и правила региона:

```pdx
MKN_tactic_torpedo_ambushes = {
    icon = generic_operation
    allowed = {
        original_tag = MKN
    }
    visible = {
        has_completed_focus = MKN_torpedo_artels_focus
        NOT = {
            has_country_flag = MKN_tactic_torpedo_ambushes_unlocked
        }
        NOT = {
            AND = {
                has_country_flag = MKN_military_stat_torpedo_ambushes
                has_country_flag = MKN_military_stat_disrupt_enemy_trade
            }
        }
    }
    available = {
        has_capitulated = no
    }
    cost = 0
    fire_only_once = yes
    days_remove = 1
    custom_cost_text = MKN_hq_navy_cost
    custom_cost_trigger = {
        NOT = {
            has_navy_experience < 20
        }
        NOT = {
            command_power < 10
        }
    }
    complete_effect = {
        navy_experience = -20
        add_command_power = -10
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_torpedo_ambushes
                    }
                }
            }
            add_to_variable = {
                MKN_navy_naval_torpedo_hit_chance_factor = 0.05
                tooltip = MKN_navy_naval_torpedo_hit_chance_factor_tt
            }
            set_country_flag = MKN_military_stat_torpedo_ambushes
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_disrupt_enemy_trade
                    }
                }
            }
            add_to_variable = {
                MKN_navy_convoy_raiding_efficiency_factor = 0.1
                tooltip = MKN_navy_convoy_raiding_efficiency_factor_tt
            }
            set_country_flag = MKN_military_stat_disrupt_enemy_trade
        }
        set_country_flag = MKN_tactic_torpedo_ambushes_unlocked
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
    }
    ai_will_do = {
        factor = 2
    }
}
```

#### Маршруты отхода — `MKN_tactic_raider_escape_routes`

EN: Escape Routes.

Заранее рассчитанные маршруты отхода спасут рейдеров от превосходящего флота.\n\nСовместные учения подготовят группы подлодок к согласованной атаке.\n\nОдноразовая подготовка. Цена: 20 опыта соответствующего рода войск и 10 командного ресурса. Постоянно усиливает его национальный дух.

Оплата, сроки, focus-gates, награды, возврат при отмене и правила региона:

```pdx
MKN_tactic_raider_escape_routes = {
    icon = generic_operation
    allowed = {
        original_tag = MKN
    }
    visible = {
        has_completed_focus = MKN_torpedo_artels_focus
        NOT = {
            has_country_flag = MKN_tactic_raider_escape_routes_unlocked
        }
        NOT = {
            AND = {
                has_country_flag = MKN_military_stat_raider_escape_routes
                has_country_flag = MKN_military_stat_raider_exercises
            }
        }
    }
    available = {
        has_capitulated = no
    }
    cost = 0
    fire_only_once = yes
    days_remove = 1
    custom_cost_text = MKN_hq_navy_cost
    custom_cost_trigger = {
        NOT = {
            has_navy_experience < 20
        }
        NOT = {
            command_power < 10
        }
    }
    complete_effect = {
        navy_experience = -20
        add_command_power = -10
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_raider_escape_routes
                    }
                }
            }
            add_to_variable = {
                MKN_navy_naval_retreat_speed = 0.15
                tooltip = MKN_navy_naval_retreat_speed_tt
            }
            set_country_flag = MKN_military_stat_raider_escape_routes
        }
        if = {
            limit = {
                hidden_trigger = {
                    NOT = {
                        has_country_flag = MKN_military_stat_raider_exercises
                    }
                }
            }
            add_to_variable = {
                MKN_navy_navy_submarine_attack_factor = 0.05
                tooltip = MKN_navy_navy_submarine_attack_factor_tt
            }
            set_country_flag = MKN_military_stat_raider_exercises
        }
        set_country_flag = MKN_tactic_raider_escape_routes_unlocked
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
    }
    ai_will_do = {
        factor = 2
    }
}
```

#### Береговая батарея — `MKN_project_coastal_battery`

EN: Coastal Battery.

За 50 политической власти через 45 дней одна прибрежная провинция выбранного региона получит один уровень береговых укреплений.\n\nЭтот тип проекта доступен один раз за кампанию, в одном выбранном регионе. Требуется полное владение и контроль. При отмене PP/CP возвращаются; повторное начало невозможно.

Оплата, сроки, focus-gates, награды, возврат при отмене и правила региона:

```pdx
MKN_project_coastal_battery = {
    icon = generic_construction
    allowed = {
        original_tag = MKN
    }
    state_target = yes
    on_map_mode = map_and_decisions_view
    target_array = ROOT.owned_states
    target_root_trigger = {
        original_tag = MKN
    }
    target_trigger = {
        FROM = {
            is_owned_and_controlled_by = ROOT
        }
    }
    visible = {
        has_completed_focus = MKN_coastal_fortifications_focus
        NOT = {
            has_country_flag = MKN_project_coastal_battery_done
        }
        NOT = {
            has_country_flag = MKN_project_coastal_battery_cancelled
        }
    }
    available = {
        has_capitulated = no
        FROM = {
            is_owned_and_controlled_by = ROOT
            is_fully_controlled_by = ROOT
        }
        FROM = {
            is_coastal = yes
            any_province_building_level = {
                province = {
                    all_provinces = yes
                    limit_to_coastal = yes
                }
                building = coastal_bunker
                level < 10
            }
        }
        hidden_trigger = {
            NOT = {
                has_country_flag = MKN_project_coastal_battery_spent
            }
        }
        custom_trigger_tooltip = {
            tooltip = MKN_military_project_idle_tt
            NOT = {
                has_country_flag = MKN_military_project_active
            }
        }
    }
    cost = 50
    days_remove = 45
    fire_only_once = yes
    complete_effect = {
        set_country_flag = MKN_project_coastal_battery_spent
        set_country_flag = MKN_military_project_active
    }
    cancel_trigger = {
        NOT = {
            AND = {
                has_capitulated = no
                FROM = {
                    is_owned_and_controlled_by = ROOT
                    is_fully_controlled_by = ROOT
                }
                FROM = {
                    is_coastal = yes
                    any_province_building_level = {
                        province = {
                            all_provinces = yes
                            limit_to_coastal = yes
                        }
                        building = coastal_bunker
                        level < 10
                    }
                }
            }
        }
    }
    cancel_effect = {
        add_political_power = 50
        set_country_flag = MKN_project_coastal_battery_cancelled
        clr_country_flag = MKN_military_project_active
    }
    remove_effect = {
        if = {
            limit = {
                has_capitulated = no
                FROM = {
                    is_owned_and_controlled_by = ROOT
                    is_fully_controlled_by = ROOT
                }
                FROM = {
                    is_coastal = yes
                    any_province_building_level = {
                        province = {
                            all_provinces = yes
                            limit_to_coastal = yes
                        }
                        building = coastal_bunker
                        level < 10
                    }
                }
            }
            FROM = {
                add_building_construction = {
                    type = coastal_bunker
                    level = 1
                    instant_build = yes
                    province = {
                        all_provinces = no
                        limit_to_coastal = yes
                    }
                }
            }
            set_country_flag = MKN_project_coastal_battery_done
            FROM = {
                set_state_flag = MKN_project_coastal_battery_done
            }
        }
        else = {
            add_political_power = 50
            set_country_flag = MKN_project_coastal_battery_cancelled
        }
        clr_country_flag = MKN_military_project_active
    }
    ai_will_do = {
        factor = 1
    }
}
```

#### Скрытая бухта — `MKN_project_hidden_cove`

EN: Hidden Cove.

За 30 политической власти через 30 дней одна прибрежная провинция выбранного региона получит один уровень морской базы.\n\nЭтот тип проекта доступен один раз за кампанию, в одном выбранном регионе. Требуется полное владение и контроль. При отмене PP/CP возвращаются; повторное начало невозможно.

Оплата, сроки, focus-gates, награды, возврат при отмене и правила региона:

```pdx
MKN_project_hidden_cove = {
    icon = generic_construction
    allowed = {
        original_tag = MKN
    }
    state_target = yes
    on_map_mode = map_and_decisions_view
    target_array = ROOT.owned_states
    target_root_trigger = {
        original_tag = MKN
    }
    target_trigger = {
        FROM = {
            is_owned_and_controlled_by = ROOT
        }
    }
    visible = {
        has_completed_focus = MKN_hidden_smuggler_bases_focus
        NOT = {
            has_country_flag = MKN_project_hidden_cove_done
        }
        NOT = {
            has_country_flag = MKN_project_hidden_cove_cancelled
        }
    }
    available = {
        has_capitulated = no
        FROM = {
            is_owned_and_controlled_by = ROOT
            is_fully_controlled_by = ROOT
        }
        FROM = {
            is_coastal = yes
            any_province_building_level = {
                province = {
                    all_provinces = yes
                    limit_to_coastal = yes
                }
                building = naval_base
                level < 10
            }
        }
        hidden_trigger = {
            NOT = {
                has_country_flag = MKN_project_hidden_cove_spent
            }
        }
        custom_trigger_tooltip = {
            tooltip = MKN_military_project_idle_tt
            NOT = {
                has_country_flag = MKN_military_project_active
            }
        }
    }
    cost = 30
    days_remove = 30
    fire_only_once = yes
    complete_effect = {
        set_country_flag = MKN_project_hidden_cove_spent
        set_country_flag = MKN_military_project_active
    }
    cancel_trigger = {
        NOT = {
            AND = {
                has_capitulated = no
                FROM = {
                    is_owned_and_controlled_by = ROOT
                    is_fully_controlled_by = ROOT
                }
                FROM = {
                    is_coastal = yes
                    any_province_building_level = {
                        province = {
                            all_provinces = yes
                            limit_to_coastal = yes
                        }
                        building = naval_base
                        level < 10
                    }
                }
            }
        }
    }
    cancel_effect = {
        add_political_power = 30
        set_country_flag = MKN_project_hidden_cove_cancelled
        clr_country_flag = MKN_military_project_active
    }
    remove_effect = {
        if = {
            limit = {
                has_capitulated = no
                FROM = {
                    is_owned_and_controlled_by = ROOT
                    is_fully_controlled_by = ROOT
                }
                FROM = {
                    is_coastal = yes
                    any_province_building_level = {
                        province = {
                            all_provinces = yes
                            limit_to_coastal = yes
                        }
                        building = naval_base
                        level < 10
                    }
                }
            }
            FROM = {
                add_building_construction = {
                    type = naval_base
                    level = 1
                    instant_build = yes
                    province = {
                        all_provinces = no
                        limit_to_coastal = yes
                    }
                }
            }
            set_country_flag = MKN_project_hidden_cove_done
            FROM = {
                set_state_flag = MKN_project_hidden_cove_done
            }
        }
        else = {
            add_political_power = 30
            set_country_flag = MKN_project_hidden_cove_cancelled
        }
        clr_country_flag = MKN_military_project_active
    }
    ai_will_do = {
        factor = 1
    }
}
```

#### Схрон топлива — `MKN_project_fuel_cache`

EN: Fuel Cache.

За 30 политической власти две гражданские фабрики за 30 дней построят одно топливохранилище в выбранном регионе.\n\nЭтот тип проекта доступен один раз за кампанию, в одном выбранном регионе. Требуется полное владение и контроль. При отмене PP/CP возвращаются; повторное начало невозможно.

Оплата, сроки, focus-gates, награды, возврат при отмене и правила региона:

```pdx
MKN_project_fuel_cache = {
    icon = generic_construction
    allowed = {
        original_tag = MKN
    }
    state_target = yes
    on_map_mode = map_and_decisions_view
    target_array = ROOT.owned_states
    target_root_trigger = {
        original_tag = MKN
    }
    target_trigger = {
        FROM = {
            is_owned_and_controlled_by = ROOT
        }
    }
    visible = {
        has_completed_focus = MKN_hidden_smuggler_bases_focus
        NOT = {
            has_country_flag = MKN_project_fuel_cache_done
        }
        NOT = {
            has_country_flag = MKN_project_fuel_cache_cancelled
        }
    }
    available = {
        has_capitulated = no
        FROM = {
            is_owned_and_controlled_by = ROOT
            is_fully_controlled_by = ROOT
        }
        FROM = {
            free_building_slots = {
                building = fuel_silo
                size > 0
            }
        }
        hidden_trigger = {
            NOT = {
                has_country_flag = MKN_project_fuel_cache_spent
            }
        }
        custom_trigger_tooltip = {
            tooltip = MKN_military_project_idle_tt
            NOT = {
                has_country_flag = MKN_military_project_active
            }
        }
        num_of_civilian_factories_available_for_projects > 1
    }
    cost = 30
    days_remove = 30
    fire_only_once = yes
    modifier = {
        civilian_factory_use = 2
    }
    complete_effect = {
        set_country_flag = MKN_project_fuel_cache_spent
        set_country_flag = MKN_military_project_active
    }
    cancel_trigger = {
        NOT = {
            AND = {
                has_capitulated = no
                FROM = {
                    is_owned_and_controlled_by = ROOT
                    is_fully_controlled_by = ROOT
                }
                FROM = {
                    free_building_slots = {
                        building = fuel_silo
                        size > 0
                    }
                }
            }
        }
    }
    cancel_effect = {
        add_political_power = 30
        set_country_flag = MKN_project_fuel_cache_cancelled
        clr_country_flag = MKN_military_project_active
    }
    remove_effect = {
        if = {
            limit = {
                has_capitulated = no
                FROM = {
                    is_owned_and_controlled_by = ROOT
                    is_fully_controlled_by = ROOT
                }
                FROM = {
                    free_building_slots = {
                        building = fuel_silo
                        size > 0
                    }
                }
            }
            FROM = {
                add_building_construction = {
                    type = fuel_silo
                    level = 1
                    instant_build = yes
                }
            }
            set_country_flag = MKN_project_fuel_cache_done
            FROM = {
                set_state_flag = MKN_project_fuel_cache_done
            }
        }
        else = {
            add_political_power = 30
            set_country_flag = MKN_project_fuel_cache_cancelled
        }
        clr_country_flag = MKN_military_project_active
    }
    ai_will_do = {
        factor = 1
    }
}
```

## Опорные определения механик

### `common/decisions/categories/MKN_military_categories.txt`

```pdx
MKN_army_hq_decisions = {
    icon = military_operation
    allowed = {
        original_tag = MKN
    }
    visible = {
        has_completed_focus = MKN_steppe_general_staff
    }
}
MKN_air_hq_decisions = {
    icon = military_operation
    allowed = {
        original_tag = MKN
    }
    visible = {
        has_completed_focus = MKN_steppe_hawks_and_schools
    }
}
MKN_navy_hq_decisions = {
    icon = military_operation
    allowed = {
        original_tag = MKN
    }
    visible = {
        has_completed_focus = MKN_black_sea_flotilla_and_yards
    }
}
```

### `common/dynamic_modifiers/nww_dynamic_modifiers.txt`

```pdx
MKN_free_industry_modifier = {
    enable = {
        always = yes
    }
    icon = GFX_idea_eng_spirit_of_the_industrial_revolution
    army_org_factor = MKN_unified_army_org_factor
    army_org_regain = MKN_unified_army_org_regain
    army_speed_factor = MKN_unified_army_speed_factor
    attrition = MKN_unified_attrition
    consumer_goods_factor = MKN_unified_consumer_goods_factor
    factory_energy_consumption = MKN_unified_factory_energy_consumption
    industrial_capacity_factory = MKN_unified_industrial_capacity_factory
    max_planning = MKN_unified_max_planning
    political_power_gain = MKN_unified_political_power_gain
    production_factory_efficiency_gain_factor = MKN_unified_production_factory_efficiency_gain_factor
    production_factory_max_efficiency_factor = MKN_unified_production_factory_max_efficiency_factor
    production_speed_buildings_factor = MKN_unified_production_speed_buildings_factor
    research_speed_factor = MKN_unified_research_speed_factor
    stability_factor = MKN_unified_stability_factor
    supply_consumption_factor = MKN_unified_supply_consumption_factor
    training_time_army_factor = MKN_unified_training_time_army_factor
    global_building_slots_factor = MKN_unified_global_building_slots_factor
    industry_air_damage_factor = MKN_unified_industry_air_damage_factor
    repair_speed_factor = MKN_unified_repair_speed_factor
    energy_gain_factor = MKN_unified_energy_gain_factor
    convoy_retreat_speed = MKN_unified_convoy_retreat_speed
}
MKN_army_development = {
    enable = {
        always = yes
    }
    icon = GFX_idea_YUG_local_militias
    war_support_factor = MKN_army_war_support_factor
    army_armor_attack_factor = MKN_army_army_armor_attack_factor
    army_fuel_consumption_factor = MKN_army_army_fuel_consumption_factor
    army_org_factor = MKN_army_army_org_factor
    army_speed_factor = MKN_army_army_speed_factor
    attrition = MKN_army_attrition
    casualty_trickleback = MKN_army_casualty_trickleback
    dig_in_speed_factor = MKN_army_dig_in_speed_factor
    experience_loss_factor = MKN_army_experience_loss_factor
    land_reinforce_rate = MKN_army_land_reinforce_rate
    max_dig_in = MKN_army_max_dig_in
    max_planning = MKN_army_max_planning
    mobilization_speed = MKN_army_mobilization_speed
    modifier_army_sub_unit_cavalry_attack_factor = MKN_army_modifier_army_sub_unit_cavalry_attack_factor
    modifier_army_sub_unit_cavalry_defence_factor = MKN_army_modifier_army_sub_unit_cavalry_defence_factor
    modifier_army_sub_unit_cavalry_speed_factor = MKN_army_modifier_army_sub_unit_cavalry_speed_factor
    modifier_army_sub_unit_infantry_attack_factor = MKN_army_modifier_army_sub_unit_infantry_attack_factor
    modifier_army_sub_unit_infantry_defence_factor = MKN_army_modifier_army_sub_unit_infantry_defence_factor
    modifier_army_sub_unit_infantry_speed_factor = MKN_army_modifier_army_sub_unit_infantry_speed_factor
    org_loss_when_moving = MKN_army_org_loss_when_moving
    planning_speed = MKN_army_planning_speed
    recon_factor = MKN_army_recon_factor
    repair_speed_factor = MKN_army_repair_speed_factor
    supply_consumption_factor = MKN_army_supply_consumption_factor
    custom_modifier_tooltip = MKN_army_development_summary
    army_attack_factor = MKN_army_army_attack_factor
    breakthrough_factor = MKN_army_breakthrough_factor
    send_volunteer_size = MKN_army_send_volunteer_size
    send_volunteers_tension = MKN_army_send_volunteers_tension
    army_core_defence_factor = MKN_army_army_core_defence_factor
    resistance_damage_to_garrison_on_our_occupied_states = MKN_army_resistance_damage_to_garrison_on_our_occupied_states
    army_defence_factor = MKN_army_army_defence_factor
    enemy_army_bonus_air_superiority_factor = MKN_army_enemy_army_bonus_air_superiority_factor
    motorized_attack_factor = MKN_army_motorized_attack_factor
    enemy_attrition = MKN_army_enemy_attrition
    conscription = MKN_army_conscription
}
MKN_air_development = {
    enable = {
        always = yes
    }
    icon = GFX_idea_generic_air_bonus
    air_accidents_factor = MKN_air_air_accidents_factor
    air_ace_generation_chance_factor = MKN_air_air_ace_generation_chance_factor
    air_agility_factor = MKN_air_air_agility_factor
    air_attack_factor = MKN_air_air_attack_factor
    air_cas_efficiency = MKN_air_air_cas_efficiency
    air_fuel_consumption_factor = MKN_air_air_fuel_consumption_factor
    air_home_defence_factor = MKN_air_air_home_defence_factor
    air_intercept_efficiency = MKN_air_air_intercept_efficiency
    air_interception_detect_factor = MKN_air_air_interception_detect_factor
    air_mission_efficiency = MKN_air_air_mission_efficiency
    air_range_factor = MKN_air_air_range_factor
    naval_strike_attack_factor = MKN_air_naval_strike_attack_factor
    recon_factor = MKN_air_recon_factor
    supply_consumption_factor = MKN_air_supply_consumption_factor
    custom_modifier_tooltip = MKN_air_development_summary
}
MKN_navy_development = {
    enable = {
        always = yes
    }
    icon = GFX_idea_generic_naval_manufacturer_1
    convoy_escort_efficiency = MKN_navy_convoy_escort_efficiency
    convoy_raiding_efficiency_factor = MKN_navy_convoy_raiding_efficiency_factor
    industrial_capacity_dockyard = MKN_navy_industrial_capacity_dockyard
    mines_sweeping_by_fleets_factor = MKN_navy_mines_sweeping_by_fleets_factor
    naval_coordination = MKN_navy_naval_coordination
    naval_defense_factor = MKN_navy_naval_defense_factor
    naval_detection = MKN_navy_naval_detection
    naval_retreat_speed = MKN_navy_naval_retreat_speed
    naval_ship_recovery_chance_factor = MKN_navy_naval_ship_recovery_chance_factor
    naval_speed_factor = MKN_navy_naval_speed_factor
    naval_torpedo_hit_chance_factor = MKN_navy_naval_torpedo_hit_chance_factor
    naval_torpedo_reveal_chance_factor = MKN_navy_naval_torpedo_reveal_chance_factor
    navy_fuel_consumption_factor = MKN_navy_navy_fuel_consumption_factor
    navy_submarine_attack_factor = MKN_navy_navy_submarine_attack_factor
    navy_submarine_defence_factor = MKN_navy_navy_submarine_defence_factor
    navy_submarine_detection_factor = MKN_navy_navy_submarine_detection_factor
    repair_speed_factor = MKN_navy_repair_speed_factor
    screening_efficiency = MKN_navy_screening_efficiency
    custom_modifier_tooltip = MKN_navy_development_summary
    navy_casualty_on_sink = MKN_navy_navy_casualty_on_sink
}
```

### `common/scripted_effects/nww_mkn_progression.txt`

```pdx
nww_mkn_rebuild_industry = {
    set_variable = {
        MKN_unified_convoy_retreat_speed = 0
    }
    set_variable = {
        MKN_unified_energy_gain_factor = 0
    }
    set_variable = {
        MKN_unified_repair_speed_factor = 0
    }
    set_variable = {
        MKN_unified_industry_air_damage_factor = 0
    }
    set_variable = {
        MKN_unified_global_building_slots_factor = 0
    }
    set_variable = {
        MKN_unified_army_org_factor = -0.1500
    }
    set_variable = {
        MKN_unified_army_org_regain = -0.1500
    }
    set_variable = {
        MKN_unified_army_speed_factor = 0.0000
    }
    set_variable = {
        MKN_unified_attrition = 0.0000
    }
    set_variable = {
        MKN_unified_consumer_goods_factor = 0.1500
    }
    set_variable = {
        MKN_unified_factory_energy_consumption = 0.0000
    }
    set_variable = {
        MKN_unified_industrial_capacity_factory = -0.2500
    }
    set_variable = {
        MKN_unified_max_planning = -0.1000
    }
    set_variable = {
        MKN_unified_political_power_gain = -0.2500
    }
    set_variable = {
        MKN_unified_production_factory_efficiency_gain_factor = -0.2000
    }
    set_variable = {
        MKN_unified_production_factory_max_efficiency_factor = 0.0000
    }
    set_variable = {
        MKN_unified_production_speed_buildings_factor = -0.1500
    }
    set_variable = {
        MKN_unified_research_speed_factor = -0.0500
    }
    set_variable = {
        MKN_unified_stability_factor = 0.0000
    }
    set_variable = {
        MKN_unified_supply_consumption_factor = 0.2000
    }
    set_variable = {
        MKN_unified_training_time_army_factor = 0.2000
    }
    if = {
        limit = {
            has_completed_focus = MKN_soviets_forever
        }
        add_to_variable = {
            MKN_unified_stability_factor = 0.05
        }
        add_to_variable = {
            MKN_unified_production_speed_buildings_factor = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_commune_federation
        }
        add_to_variable = {
            MKN_unified_stability_factor = 0.05
        }
        add_to_variable = {
            MKN_unified_production_speed_buildings_factor = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_free_elections_steppe
        }
        add_to_variable = {
            MKN_unified_stability_factor = 0.1
        }
        add_to_variable = {
            MKN_unified_political_power_gain = 0.1
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_collectivize_the_steppe
        }
        add_to_variable = {
            MKN_unified_industrial_capacity_factory = 0.08
        }
        add_to_variable = {
            MKN_unified_consumer_goods_factor = -0.03
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_imperial_coronation
        }
        add_to_variable = {
            MKN_unified_stability_factor = 0.1
        }
        add_to_variable = {
            MKN_unified_political_power_gain = 0.15
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_recallable_delegates
        }
        add_to_variable = {
            MKN_unified_political_power_gain = 0.1
        }
        add_to_variable = {
            MKN_unified_stability_factor = 0.03
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_peasant_charter
        }
        add_to_variable = {
            MKN_unified_consumer_goods_factor = -0.02
        }
        add_to_variable = {
            MKN_unified_stability_factor = 0.03
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_red_compromise_institutions
        }
        add_to_variable = {
            MKN_unified_production_factory_efficiency_gain_factor = 0.05
        }
        add_to_variable = {
            MKN_unified_political_power_gain = 0.05
        }
    }
    remove_ideas = {
        MKN_communal_federation
        MKN_federal_republic
        MKN_imperial_administration
        MKN_planned_economy
        MKN_accountable_militias
        MKN_anarchic_economy_idea
        MKN_artel_logistics
        MKN_broken_supply
        MKN_catalogued_workshops
        MKN_cooperative_production
        MKN_coordinated_supply
        MKN_dneprostroi_power
        MKN_dnieper_economy
        MKN_dnieper_logistics
        MKN_drilled_militias
        MKN_economic_coordination
        MKN_economic_recovery
        MKN_fragmented_workshops
        MKN_free_mint_idea
        MKN_mapped_supply
        MKN_mobile_self_defence_idea
        MKN_mutual_aid_economy
        MKN_serial_production
        MKN_standardized_workshops
        MKN_untrained_militias
        MKN_worker_battalions_idea
    }
    add_dynamic_modifier = {
        modifier = MKN_free_industry_modifier
    }
    if = {
        limit = {
            has_completed_focus = MKN_militarize_communes
        }
        add_to_variable = {
            MKN_unified_stability_factor = -0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_standardize_workshops
        }
        add_to_variable = {
            MKN_unified_industrial_capacity_factory = 0.15
        }
        add_to_variable = {
            MKN_unified_production_factory_efficiency_gain_factor = 0.1
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_autonomous_rail_crews
        }
        add_to_variable = {
            MKN_unified_production_speed_buildings_factor = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_sever_urban_ties
        }
        add_to_variable = {
            MKN_unified_consumer_goods_factor = -0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_tractors_for_grain
        }
        add_to_variable = {
            MKN_unified_production_speed_buildings_factor = 0.1
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_dneprostroi
        }
        add_to_variable = {
            MKN_unified_political_power_gain = 0.1000
        }
        add_to_variable = {
            MKN_unified_consumer_goods_factor = -0.0500
        }
        add_to_variable = {
            MKN_unified_production_speed_buildings_factor = 0.0500
        }
        add_to_variable = {
            MKN_unified_industrial_capacity_factory = 0.0500
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_dnieper_audit
        }
        add_to_variable = {
            MKN_unified_industrial_capacity_factory = 0.0500
        }
        add_to_variable = {
            MKN_unified_production_factory_efficiency_gain_factor = 0.1000
        }
        add_to_variable = {
            MKN_unified_research_speed_factor = 0.0500
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_steppe_industrial_giants
        }
        add_to_variable = {
            MKN_unified_industrial_capacity_factory = 0.1000
        }
        add_to_variable = {
            MKN_unified_production_factory_efficiency_gain_factor = 0.0500
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_zaporizhstal
        }
        add_to_variable = {
            MKN_unified_political_power_gain = 0.1000
        }
        add_to_variable = {
            MKN_unified_consumer_goods_factor = -0.0500
        }
        add_to_variable = {
            MKN_unified_production_speed_buildings_factor = 0.0500
        }
        add_to_variable = {
            MKN_unified_industrial_capacity_factory = 0.0500
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_worker_battalions
        }
        add_to_variable = {
            MKN_unified_army_org_factor = 0.2000
        }
        add_to_variable = {
            MKN_unified_training_time_army_factor = -0.2000
        }
        add_to_variable = {
            MKN_unified_max_planning = 0.1500
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_dnieper_logistics_hub
        }
        add_to_variable = {
            MKN_unified_supply_consumption_factor = -0.1500
        }
        add_to_variable = {
            MKN_unified_army_org_regain = 0.1000
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_steppe_electrification
        }
        add_to_variable = {
            MKN_unified_production_speed_buildings_factor = 0.0500
        }
        add_to_variable = {
            MKN_unified_factory_energy_consumption = -0.1000
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_production_cycles
        }
        add_to_variable = {
            MKN_unified_industrial_capacity_factory = 0.2000
        }
        add_to_variable = {
            MKN_unified_production_factory_efficiency_gain_factor = 0.0500
        }
        add_to_variable = {
            MKN_unified_production_factory_max_efficiency_factor = 0.1000
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_steel_volnitsa
        }
        add_to_variable = {
            MKN_unified_political_power_gain = 0.1500
        }
        add_to_variable = {
            MKN_unified_consumer_goods_factor = -0.0500
        }
        add_to_variable = {
            MKN_unified_production_speed_buildings_factor = 0.1500
        }
        add_to_variable = {
            MKN_unified_global_building_slots_factor = 0.3000
        }
        add_to_variable = {
            MKN_unified_supply_consumption_factor = -0.1500
        }
        add_to_variable = {
            MKN_unified_army_org_regain = 0.1000
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_free_cooperatives
        }
        add_to_variable = {
            MKN_unified_political_power_gain = 0.1000
        }
        add_to_variable = {
            MKN_unified_consumer_goods_factor = -0.0500
        }
        add_to_variable = {
            MKN_unified_production_speed_buildings_factor = 0.0500
        }
        add_to_variable = {
            MKN_unified_industrial_capacity_factory = 0.0500
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_artel_register
        }
        add_to_variable = {
            MKN_unified_industrial_capacity_factory = 0.0500
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_steppe_markets
        }
        add_to_variable = {
            MKN_unified_political_power_gain = 0.2000
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_mobile_workshops
        }
        add_to_variable = {
            MKN_unified_political_power_gain = 0.1000
        }
        add_to_variable = {
            MKN_unified_consumer_goods_factor = -0.0500
        }
        add_to_variable = {
            MKN_unified_production_speed_buildings_factor = 0.0500
        }
        add_to_variable = {
            MKN_unified_industrial_capacity_factory = 0.1000
        }
        add_to_variable = {
            MKN_unified_production_factory_efficiency_gain_factor = 0.1000
        }
        add_to_variable = {
            MKN_unified_research_speed_factor = 0.0500
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_rifle_concern
        }
        add_to_variable = {
            MKN_unified_industrial_capacity_factory = 0.0500
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_freight_logistics
        }
        add_to_variable = {
            MKN_unified_supply_consumption_factor = -0.3000
        }
        add_to_variable = {
            MKN_unified_army_org_regain = 0.1500
        }
        add_to_variable = {
            MKN_unified_attrition = -0.0500
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_workshop_standards
        }
        add_to_variable = {
            MKN_unified_industrial_capacity_factory = 0.1500
        }
        add_to_variable = {
            MKN_unified_production_factory_efficiency_gain_factor = 0.2500
        }
        add_to_variable = {
            MKN_unified_research_speed_factor = 0.0500
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_field_schools
        }
        add_to_variable = {
            MKN_unified_army_org_factor = 0.2000
        }
        add_to_variable = {
            MKN_unified_training_time_army_factor = -0.2500
        }
        add_to_variable = {
            MKN_unified_max_planning = 0.1000
        }
        add_to_variable = {
            MKN_unified_army_speed_factor = 0.0500
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_communal_compact
        }
        add_to_variable = {
            MKN_unified_political_power_gain = 0.1500
        }
        add_to_variable = {
            MKN_unified_consumer_goods_factor = -0.1000
        }
        add_to_variable = {
            MKN_unified_production_speed_buildings_factor = 0.0500
        }
        add_to_variable = {
            MKN_unified_stability_factor = 0.0500
        }
        add_to_variable = {
            MKN_unified_global_building_slots_factor = 0.3000
        }
        add_to_variable = {
            MKN_unified_industry_air_damage_factor = -0.2000
        }
        add_to_variable = {
            MKN_unified_repair_speed_factor = 0.2000
        }
    }
    if = {
        limit = {
            has_country_flag = MKN_project_dnieper_turbines_done
        }
        add_to_variable = {
            MKN_unified_energy_gain_factor = 0.1000
        }
    }
    if = {
        limit = {
            has_country_flag = MKN_project_kherson_terminals_done
        }
        add_to_variable = {
            MKN_unified_convoy_retreat_speed = 0.1000
        }
    }
    set_country_flag = MKN_industry_unified_v2
    set_country_flag = MKN_industry_projects_v3
    if = {
        limit = {
            has_completed_focus = MKN_southern_commune_charters
        }
        add_to_variable = {
            MKN_unified_supply_consumption_factor = -0.0500
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_right_bank_councils
        }
        add_to_variable = {
            MKN_unified_stability_factor = 0.0500
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_northern_delegates
        }
        add_to_variable = {
            MKN_unified_political_power_gain = 0.1000
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_dnieper_workshop_federation
        }
        add_to_variable = {
            MKN_unified_industrial_capacity_factory = 0.0500
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_ukrainian_rail_reconstruction
        }
        add_to_variable = {
            MKN_unified_production_speed_buildings_factor = 0.1000
        }
        add_to_variable = {
            MKN_unified_repair_speed_factor = 0.1000
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_federation_of_free_councils
        }
        add_to_variable = {
            MKN_unified_stability_factor = 0.0500
        }
        add_to_variable = {
            MKN_unified_supply_consumption_factor = -0.0500
        }
        add_to_variable = {
            MKN_unified_production_factory_max_efficiency_factor = 0.0500
        }
    }
    set_country_flag = MKN_industry_integration_v4
}
nww_mkn_rebuild_services = {
    MKN_migrate_military_hq = yes
    set_variable = {
        MKN_army_enemy_attrition = 0
    }
    set_variable = {
        MKN_army_motorized_attack_factor = 0
    }
    set_variable = {
        MKN_army_enemy_army_bonus_air_superiority_factor = 0
    }
    set_variable = {
        MKN_army_army_defence_factor = 0
    }
    set_variable = {
        MKN_army_resistance_damage_to_garrison_on_our_occupied_states = 0
    }
    set_variable = {
        MKN_army_army_core_defence_factor = 0
    }
    set_variable = {
        MKN_army_send_volunteers_tension = 0
    }
    set_variable = {
        MKN_army_send_volunteer_size = 0
    }
    set_variable = {
        MKN_army_breakthrough_factor = 0
    }
    set_variable = {
        MKN_army_army_attack_factor = 0
    }
    set_variable = {
        MKN_army_war_support_factor = 0
    }
    set_variable = {
        MKN_army_army_armor_attack_factor = 0
    }
    set_variable = {
        MKN_army_army_fuel_consumption_factor = 0
    }
    set_variable = {
        MKN_army_army_org_factor = 0
    }
    set_variable = {
        MKN_army_army_speed_factor = 0
    }
    set_variable = {
        MKN_army_attrition = 0
    }
    set_variable = {
        MKN_army_casualty_trickleback = 0
    }
    set_variable = {
        MKN_army_dig_in_speed_factor = 0
    }
    set_variable = {
        MKN_army_experience_loss_factor = 0
    }
    set_variable = {
        MKN_army_land_reinforce_rate = 0
    }
    set_variable = {
        MKN_army_max_dig_in = 0
    }
    set_variable = {
        MKN_army_max_planning = 0
    }
    set_variable = {
        MKN_army_mobilization_speed = 0
    }
    set_variable = {
        MKN_army_modifier_army_sub_unit_cavalry_attack_factor = 0
    }
    set_variable = {
        MKN_army_modifier_army_sub_unit_cavalry_defence_factor = 0
    }
    set_variable = {
        MKN_army_modifier_army_sub_unit_cavalry_speed_factor = 0
    }
    set_variable = {
        MKN_army_modifier_army_sub_unit_infantry_attack_factor = 0
    }
    set_variable = {
        MKN_army_modifier_army_sub_unit_infantry_defence_factor = 0
    }
    set_variable = {
        MKN_army_modifier_army_sub_unit_infantry_speed_factor = 0
    }
    set_variable = {
        MKN_army_org_loss_when_moving = 0
    }
    set_variable = {
        MKN_army_planning_speed = 0
    }
    set_variable = {
        MKN_army_recon_factor = 0
    }
    set_variable = {
        MKN_army_conscription = 0
    }
    set_variable = {
        MKN_army_repair_speed_factor = 0
    }
    set_variable = {
        MKN_army_supply_consumption_factor = 0
    }
    set_variable = {
        MKN_air_air_accidents_factor = 0
    }
    set_variable = {
        MKN_air_air_ace_generation_chance_factor = 0
    }
    set_variable = {
        MKN_air_air_agility_factor = 0
    }
    set_variable = {
        MKN_air_air_attack_factor = 0
    }
    set_variable = {
        MKN_air_air_cas_efficiency = 0
    }
    set_variable = {
        MKN_air_air_fuel_consumption_factor = 0
    }
    set_variable = {
        MKN_air_air_home_defence_factor = 0
    }
    set_variable = {
        MKN_air_air_intercept_efficiency = 0
    }
    set_variable = {
        MKN_air_air_interception_detect_factor = 0
    }
    set_variable = {
        MKN_air_air_mission_efficiency = 0
    }
    set_variable = {
        MKN_air_air_range_factor = 0
    }
    set_variable = {
        MKN_air_naval_strike_attack_factor = 0
    }
    set_variable = {
        MKN_air_recon_factor = 0
    }
    set_variable = {
        MKN_air_supply_consumption_factor = 0
    }
    set_variable = {
        MKN_navy_convoy_escort_efficiency = 0
    }
    set_variable = {
        MKN_navy_convoy_raiding_efficiency_factor = 0
    }
    set_variable = {
        MKN_navy_industrial_capacity_dockyard = 0
    }
    set_variable = {
        MKN_navy_mines_sweeping_by_fleets_factor = 0
    }
    set_variable = {
        MKN_navy_naval_coordination = 0
    }
    set_variable = {
        MKN_navy_naval_defense_factor = 0
    }
    set_variable = {
        MKN_navy_naval_detection = 0
    }
    set_variable = {
        MKN_navy_naval_retreat_speed = 0
    }
    set_variable = {
        MKN_navy_naval_ship_recovery_chance_factor = 0
    }
    set_variable = {
        MKN_navy_naval_speed_factor = 0
    }
    set_variable = {
        MKN_navy_naval_torpedo_hit_chance_factor = 0
    }
    set_variable = {
        MKN_navy_naval_torpedo_reveal_chance_factor = 0
    }
    set_variable = {
        MKN_navy_navy_fuel_consumption_factor = 0
    }
    set_variable = {
        MKN_navy_navy_submarine_attack_factor = 0
    }
    set_variable = {
        MKN_navy_navy_submarine_defence_factor = 0
    }
    set_variable = {
        MKN_navy_navy_submarine_detection_factor = 0
    }
    set_variable = {
        MKN_navy_repair_speed_factor = 0
    }
    set_variable = {
        MKN_navy_screening_efficiency = 0
    }
    set_variable = {
        MKN_navy_navy_casualty_on_sink = 0
    }
    if = {
        limit = {
            has_completed_focus = MKN_steppe_general_staff
            has_country_flag = MKN_military_bundle_steppe_general_staff
        }
        add_to_variable = {
            MKN_army_army_org_factor = 0.04
        }
        add_to_variable = {
            MKN_army_max_planning = 0.05
        }
        add_to_variable = {
            MKN_army_supply_consumption_factor = -0.05
        }
    }
    else = {
        if = {
            limit = {
                has_country_flag = MKN_military_stat_tachanka_columns
            }
            add_to_variable = {
                MKN_army_army_org_factor = 0.04
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_railway_war
            }
            add_to_variable = {
                MKN_army_supply_consumption_factor = -0.05
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_steppe_general_staff
            }
            add_to_variable = {
                MKN_army_max_planning = 0.05
            }
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_steppe_horde
            has_country_flag = MKN_military_bundle_steppe_horde
        }
        add_to_variable = {
            MKN_army_mobilization_speed = 0.15
        }
        add_to_variable = {
            MKN_army_modifier_army_sub_unit_cavalry_attack_factor = 0.15
        }
        add_to_variable = {
            MKN_army_modifier_army_sub_unit_cavalry_speed_factor = 0.08
        }
    }
    else = {
        if = {
            limit = {
                has_country_flag = MKN_military_stat_batko_cavalry
            }
            add_to_variable = {
                MKN_army_modifier_army_sub_unit_cavalry_attack_factor = 0.08
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_village_muster
            }
            add_to_variable = {
                MKN_army_mobilization_speed = 0.15
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_remount_artels
            }
            add_to_variable = {
                MKN_army_modifier_army_sub_unit_cavalry_speed_factor = 0.08
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_machinegun_carts
            }
            add_to_variable = {
                MKN_army_modifier_army_sub_unit_cavalry_attack_factor = 0.07
            }
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_hidden_supply_bases_focus
            has_country_flag = MKN_military_bundle_hidden_supply_bases_focus
        }
        add_to_variable = {
            MKN_army_attrition = -0.08
        }
        add_to_variable = {
            MKN_army_recon_factor = 0.1
        }
    }
    else = {
        if = {
            limit = {
                has_country_flag = MKN_military_stat_local_guides
            }
            add_to_variable = {
                MKN_army_recon_factor = 0.1
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_field_veterinary
            }
            add_to_variable = {
                MKN_army_attrition = -0.08
            }
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_free_column_command_focus
            has_country_flag = MKN_military_bundle_free_column_command_focus
        }
        add_to_variable = {
            MKN_army_army_speed_factor = 0.05
        }
        add_to_variable = {
            MKN_army_land_reinforce_rate = 0.02
        }
    }
    else = {
        if = {
            limit = {
                has_country_flag = MKN_military_stat_scout_parties
            }
            add_to_variable = {
                MKN_army_army_speed_factor = 0.05
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_militia_signals
            }
            add_to_variable = {
                MKN_army_land_reinforce_rate = 0.02
            }
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_free_army_compact
            has_country_flag = MKN_military_bundle_free_army_compact
        }
        add_to_variable = {
            MKN_army_modifier_army_sub_unit_cavalry_attack_factor = 0.05
        }
        add_to_variable = {
            MKN_army_supply_consumption_factor = -0.05
        }
    }
    else = {
        if = {
            limit = {
                has_country_flag = MKN_military_stat_free_army_compact
            }
            add_to_variable = {
                MKN_army_modifier_army_sub_unit_cavalry_attack_factor = 0.05
            }
            add_to_variable = {
                MKN_army_supply_consumption_factor = -0.05
            }
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_motorized_vanguard
            has_country_flag = MKN_military_bundle_motorized_vanguard
        }
        add_to_variable = {
            MKN_army_army_armor_attack_factor = 0.05
        }
        add_to_variable = {
            MKN_army_army_fuel_consumption_factor = -0.08
        }
        add_to_variable = {
            MKN_army_army_org_factor = 0.04
        }
        add_to_variable = {
            MKN_army_supply_consumption_factor = -0.05
        }
    }
    else = {
        if = {
            limit = {
                has_country_flag = MKN_military_stat_steel_horses
            }
            add_to_variable = {
                MKN_army_army_armor_attack_factor = 0.05
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_tank_crews
            }
            add_to_variable = {
                MKN_army_army_org_factor = 0.04
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_steppe_quartermasters
            }
            add_to_variable = {
                MKN_army_supply_consumption_factor = -0.05
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_mobile_supply_columns
            }
            add_to_variable = {
                MKN_army_army_fuel_consumption_factor = -0.08
            }
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_armored_trains_and_repair_focus
            has_country_flag = MKN_military_bundle_armored_trains_and_repair_focus
        }
        add_to_variable = {
            MKN_army_attrition = -0.08
        }
        add_to_variable = {
            MKN_army_repair_speed_factor = 0.1
        }
    }
    else = {
        if = {
            limit = {
                has_country_flag = MKN_military_stat_recovery_tractors
            }
            add_to_variable = {
                MKN_army_attrition = -0.08
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_tank_maintenance
            }
            add_to_variable = {
                MKN_army_repair_speed_factor = 0.1
            }
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_communal_fire_support_focus
            has_country_flag = MKN_military_bundle_communal_fire_support_focus
        }
        add_to_variable = {
            MKN_army_max_planning = 0.05
        }
        add_to_variable = {
            MKN_army_modifier_army_sub_unit_infantry_attack_factor = 0.04
        }
    }
    else = {
        if = {
            limit = {
                has_country_flag = MKN_military_stat_artillery_artels
            }
            add_to_variable = {
                MKN_army_modifier_army_sub_unit_infantry_attack_factor = 0.04
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_fire_tables
            }
            add_to_variable = {
                MKN_army_max_planning = 0.05
            }
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_combined_arms_command_focus
            has_country_flag = MKN_military_bundle_combined_arms_command_focus
        }
        add_to_variable = {
            MKN_army_land_reinforce_rate = 0.02
        }
    }
    else = {
        if = {
            limit = {
                has_country_flag = MKN_military_stat_radio_sections
            }
            add_to_variable = {
                MKN_army_land_reinforce_rate = 0.02
            }
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_mechanized_compact
            has_country_flag = MKN_military_bundle_mechanized_compact
        }
        add_to_variable = {
            MKN_army_army_armor_attack_factor = 0.06
        }
        add_to_variable = {
            MKN_army_army_org_factor = 0.05
        }
    }
    else = {
        if = {
            limit = {
                has_country_flag = MKN_military_stat_mechanized_compact
            }
            add_to_variable = {
                MKN_army_army_armor_attack_factor = 0.06
            }
            add_to_variable = {
                MKN_army_army_org_factor = 0.05
            }
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_steppe_hawks_and_schools
            has_country_flag = MKN_military_bundle_steppe_hawks_and_schools
        }
        add_to_variable = {
            MKN_air_air_accidents_factor = -0.05
        }
        add_to_variable = {
            MKN_air_air_mission_efficiency = 0.03
        }
        add_to_variable = {
            MKN_air_air_range_factor = 0.05
        }
    }
    else = {
        if = {
            limit = {
                has_country_flag = MKN_military_stat_steppe_hawks
            }
            add_to_variable = {
                MKN_air_air_mission_efficiency = 0.03
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_village_airfields
            }
            add_to_variable = {
                MKN_air_air_range_factor = 0.05
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_gulyaipole_pilot_school
            }
            add_to_variable = {
                MKN_air_air_accidents_factor = -0.05
            }
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_interceptor_cooperatives
            has_country_flag = MKN_military_bundle_interceptor_cooperatives
        }
        add_to_variable = {
            MKN_air_air_ace_generation_chance_factor = 0.15
        }
        add_to_variable = {
            MKN_air_air_agility_factor = 0.08
        }
        add_to_variable = {
            MKN_air_air_intercept_efficiency = 0.1
        }
    }
    else = {
        if = {
            limit = {
                has_country_flag = MKN_military_stat_black_swarm
            }
            add_to_variable = {
                MKN_air_air_intercept_efficiency = 0.1
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_aircraft_artels
            }
            add_to_variable = {
                MKN_air_air_agility_factor = 0.04
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_fighter_instructors
            }
            add_to_variable = {
                MKN_air_air_ace_generation_chance_factor = 0.15
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_interceptor_pairs
            }
            add_to_variable = {
                MKN_air_air_agility_factor = 0.04
            }
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_communal_aa_defense_focus
            has_country_flag = MKN_military_bundle_communal_aa_defense_focus
        }
        add_to_variable = {
            MKN_air_air_intercept_efficiency = 0.05
        }
        add_to_variable = {
            MKN_air_air_interception_detect_factor = 0.1
        }
    }
    else = {
        if = {
            limit = {
                has_country_flag = MKN_military_stat_observation_posts
            }
            add_to_variable = {
                MKN_air_air_interception_detect_factor = 0.1
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_air_warning
            }
            add_to_variable = {
                MKN_air_air_intercept_efficiency = 0.05
            }
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_airframe_standardization_focus
            has_country_flag = MKN_military_bundle_airframe_standardization_focus
        }
        add_to_variable = {
            MKN_air_air_accidents_factor = -0.05
        }
        add_to_variable = {
            MKN_air_air_attack_factor = 0.04
        }
        add_to_variable = {
            MKN_air_air_mission_efficiency = 0.05
        }
    }
    else = {
        if = {
            limit = {
                has_country_flag = MKN_military_stat_radio_beacons
            }
            add_to_variable = {
                MKN_air_air_mission_efficiency = 0.05
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_airframe_jigs
            }
            add_to_variable = {
                MKN_air_air_attack_factor = 0.04
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_aircraft_recovery
            }
            add_to_variable = {
                MKN_air_air_accidents_factor = -0.05
            }
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_free_sky_compact
            has_country_flag = MKN_military_bundle_free_sky_compact
        }
        add_to_variable = {
            MKN_air_air_agility_factor = 0.04
        }
        add_to_variable = {
            MKN_air_air_intercept_efficiency = 0.1
        }
    }
    else = {
        if = {
            limit = {
                has_country_flag = MKN_military_stat_free_sky_compact
            }
            add_to_variable = {
                MKN_air_air_agility_factor = 0.04
            }
            add_to_variable = {
                MKN_air_air_intercept_efficiency = 0.1
            }
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_flying_artillery_focus
            has_country_flag = MKN_military_bundle_flying_artillery_focus
        }
        add_to_variable = {
            MKN_air_air_attack_factor = 0.04
        }
        add_to_variable = {
            MKN_air_air_cas_efficiency = 0.15
        }
        add_to_variable = {
            MKN_air_air_mission_efficiency = 0.04
        }
    }
    else = {
        if = {
            limit = {
                has_country_flag = MKN_military_stat_close_support_program
            }
            add_to_variable = {
                MKN_air_air_cas_efficiency = 0.1
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_attack_air_artels
            }
            add_to_variable = {
                MKN_air_air_attack_factor = 0.04
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_flying_artillery
            }
            add_to_variable = {
                MKN_air_air_cas_efficiency = 0.05
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_bombing_ranges
            }
            add_to_variable = {
                MKN_air_air_mission_efficiency = 0.04
            }
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_forward_airstrips_focus
            has_country_flag = MKN_military_bundle_forward_airstrips_focus
        }
        add_to_variable = {
            MKN_air_air_cas_efficiency = 0.05
        }
        add_to_variable = {
            MKN_air_air_range_factor = 0.08
        }
    }
    else = {
        if = {
            limit = {
                has_country_flag = MKN_military_stat_forward_airstrips
            }
            add_to_variable = {
                MKN_air_air_range_factor = 0.08
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_air_ground_liaisons
            }
            add_to_variable = {
                MKN_air_air_cas_efficiency = 0.05
            }
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_air_ground_coordination_focus
            has_country_flag = MKN_military_bundle_air_ground_coordination_focus
        }
        add_to_variable = {
            MKN_air_air_cas_efficiency = 0.05
        }
        add_to_variable = {
            MKN_air_air_mission_efficiency = 0.04
        }
    }
    else = {
        if = {
            limit = {
                has_country_flag = MKN_military_stat_air_map_bureau
            }
            add_to_variable = {
                MKN_air_air_mission_efficiency = 0.04
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_target_markers
            }
            add_to_variable = {
                MKN_air_air_cas_efficiency = 0.05
            }
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_cas_workshop_network_focus
            has_country_flag = MKN_military_bundle_cas_workshop_network_focus
        }
        add_to_variable = {
            MKN_air_air_accidents_factor = -0.08
        }
    }
    else = {
        if = {
            limit = {
                has_country_flag = MKN_military_stat_cas_maintenance
            }
            add_to_variable = {
                MKN_air_air_accidents_factor = -0.08
            }
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_air_support_compact
            has_country_flag = MKN_military_bundle_air_support_compact
        }
        add_to_variable = {
            MKN_air_air_cas_efficiency = 0.05
        }
        add_to_variable = {
            MKN_air_air_mission_efficiency = 0.05
        }
    }
    else = {
        if = {
            limit = {
                has_country_flag = MKN_military_stat_air_support_compact
            }
            add_to_variable = {
                MKN_air_air_cas_efficiency = 0.05
            }
            add_to_variable = {
                MKN_air_air_mission_efficiency = 0.05
            }
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_black_sea_flotilla_and_yards
            has_country_flag = MKN_military_bundle_black_sea_flotilla_and_yards
        }
        add_to_variable = {
            MKN_navy_industrial_capacity_dockyard = 0.05
        }
        add_to_variable = {
            MKN_navy_naval_defense_factor = 0.03
        }
        add_to_variable = {
            MKN_navy_naval_detection = 0.05
        }
    }
    else = {
        if = {
            limit = {
                has_country_flag = MKN_military_stat_black_sea_flotilla
            }
            add_to_variable = {
                MKN_navy_naval_defense_factor = 0.03
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_dnieper_patrol
            }
            add_to_variable = {
                MKN_navy_naval_detection = 0.05
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_kherson_shipyard
            }
            add_to_variable = {
                MKN_navy_industrial_capacity_dockyard = 0.05
            }
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_sea_escort_service
            has_country_flag = MKN_military_bundle_sea_escort_service
        }
        add_to_variable = {
            MKN_navy_convoy_escort_efficiency = 0.15
        }
        add_to_variable = {
            MKN_navy_navy_submarine_detection_factor = 0.15
        }
        add_to_variable = {
            MKN_navy_screening_efficiency = 0.08
        }
    }
    else = {
        if = {
            limit = {
                has_country_flag = MKN_military_stat_coastal_defense_steppe
            }
            add_to_variable = {
                MKN_navy_convoy_escort_efficiency = 0.1
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_black_sea_escorts
            }
            add_to_variable = {
                MKN_navy_screening_efficiency = 0.08
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_escort_crews
            }
            add_to_variable = {
                MKN_navy_convoy_escort_efficiency = 0.05
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_depth_charge_school
            }
            add_to_variable = {
                MKN_navy_navy_submarine_detection_factor = 0.15
            }
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_coastal_fortifications_focus
            has_country_flag = MKN_military_bundle_coastal_fortifications_focus
        }
        add_to_variable = {
            MKN_navy_naval_defense_factor = 0.05
        }
        add_to_variable = {
            MKN_navy_naval_detection = 0.08
        }
    }
    else = {
        if = {
            limit = {
                has_country_flag = MKN_military_stat_dnieper_gun_flotilla
            }
            add_to_variable = {
                MKN_navy_naval_defense_factor = 0.05
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_coastal_signal_posts
            }
            add_to_variable = {
                MKN_navy_naval_detection = 0.08
            }
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_escort_repair_network_focus
            has_country_flag = MKN_military_bundle_escort_repair_network_focus
        }
        add_to_variable = {
            MKN_navy_convoy_escort_efficiency = 0.05
        }
        add_to_variable = {
            MKN_navy_navy_fuel_consumption_factor = -0.08
        }
        add_to_variable = {
            MKN_navy_repair_speed_factor = 0.15
        }
    }
    else = {
        if = {
            limit = {
                has_country_flag = MKN_military_stat_harbour_dredging
            }
            add_to_variable = {
                MKN_navy_navy_fuel_consumption_factor = -0.08
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_hull_repair_artels
            }
            add_to_variable = {
                MKN_navy_repair_speed_factor = 0.15
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_convoy_schedules
            }
            add_to_variable = {
                MKN_navy_convoy_escort_efficiency = 0.05
            }
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_escort_compact
            has_country_flag = MKN_military_bundle_escort_compact
        }
        add_to_variable = {
            MKN_navy_convoy_escort_efficiency = 0.05
        }
        add_to_variable = {
            MKN_navy_screening_efficiency = 0.05
        }
    }
    else = {
        if = {
            limit = {
                has_country_flag = MKN_military_stat_escort_compact
            }
            add_to_variable = {
                MKN_navy_convoy_escort_efficiency = 0.05
            }
            add_to_variable = {
                MKN_navy_screening_efficiency = 0.05
            }
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_torpedo_artels_focus
            has_country_flag = MKN_military_bundle_torpedo_artels_focus
        }
        add_to_variable = {
            MKN_navy_convoy_raiding_efficiency_factor = 0.1
        }
        add_to_variable = {
            MKN_navy_naval_torpedo_hit_chance_factor = 0.1
        }
        add_to_variable = {
            MKN_navy_navy_submarine_attack_factor = 0.05
        }
    }
    else = {
        if = {
            limit = {
                has_country_flag = MKN_military_stat_black_sea_smugglers
            }
            add_to_variable = {
                MKN_navy_convoy_raiding_efficiency_factor = 0.1
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_torpedo_artels
            }
            add_to_variable = {
                MKN_navy_naval_torpedo_hit_chance_factor = 0.05
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_submarine_crews
            }
            add_to_variable = {
                MKN_navy_navy_submarine_attack_factor = 0.05
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_torpedo_trials
            }
            add_to_variable = {
                MKN_navy_naval_torpedo_hit_chance_factor = 0.05
            }
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_hidden_smuggler_bases_focus
            has_country_flag = MKN_military_bundle_hidden_smuggler_bases_focus
        }
        add_to_variable = {
            MKN_navy_industrial_capacity_dockyard = 0.05
        }
        add_to_variable = {
            MKN_navy_naval_detection = 0.08
        }
        add_to_variable = {
            MKN_navy_naval_torpedo_reveal_chance_factor = -0.15
        }
        add_to_variable = {
            MKN_navy_navy_fuel_consumption_factor = -0.1
        }
    }
    else = {
        if = {
            limit = {
                has_country_flag = MKN_military_stat_hidden_anchorages
            }
            add_to_variable = {
                MKN_navy_naval_torpedo_reveal_chance_factor = -0.08
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_naval_intelligence
            }
            add_to_variable = {
                MKN_navy_naval_detection = 0.08
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_raider_dockyard
            }
            add_to_variable = {
                MKN_navy_industrial_capacity_dockyard = 0.05
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_night_sorties
            }
            add_to_variable = {
                MKN_navy_naval_torpedo_reveal_chance_factor = -0.07
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_raider_supply
            }
            add_to_variable = {
                MKN_navy_navy_fuel_consumption_factor = -0.1
            }
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_raider_compact
            has_country_flag = MKN_military_bundle_raider_compact
        }
        add_to_variable = {
            MKN_navy_convoy_raiding_efficiency_factor = 0.1
        }
        add_to_variable = {
            MKN_navy_navy_submarine_attack_factor = 0.05
        }
    }
    else = {
        if = {
            limit = {
                has_country_flag = MKN_military_stat_raider_compact
            }
            add_to_variable = {
                MKN_navy_convoy_raiding_efficiency_factor = 0.1
            }
            add_to_variable = {
                MKN_navy_navy_submarine_attack_factor = 0.05
            }
        }
    }
    if = {
        limit = {
            has_country_flag = MKN_tactic_night_marches_unlocked
        }
        add_to_variable = {
            MKN_army_army_org_factor = 0.05
        }
        add_to_variable = {
            MKN_army_org_loss_when_moving = -0.1
        }
    }
    else = {
        if = {
            limit = {
                has_country_flag = MKN_military_stat_night_marches
            }
            add_to_variable = {
                MKN_army_org_loss_when_moving = -0.1
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_militia_junior_leaders
            }
            add_to_variable = {
                MKN_army_army_org_factor = 0.05
            }
        }
    }
    if = {
        limit = {
            has_country_flag = MKN_tactic_steppe_camouflage_unlocked
        }
        add_to_variable = {
            MKN_army_max_dig_in = 2
        }
        add_to_variable = {
            MKN_army_supply_consumption_factor = -0.08
        }
    }
    else = {
        if = {
            limit = {
                has_country_flag = MKN_military_stat_steppe_camouflage
            }
            add_to_variable = {
                MKN_army_max_dig_in = 2
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_hidden_depots
            }
            add_to_variable = {
                MKN_army_supply_consumption_factor = -0.08
            }
        }
    }
    if = {
        limit = {
            has_country_flag = MKN_tactic_militia_engineers_unlocked
        }
        add_to_variable = {
            MKN_army_casualty_trickleback = 0.06
        }
        add_to_variable = {
            MKN_army_dig_in_speed_factor = 0.2
        }
    }
    else = {
        if = {
            limit = {
                has_country_flag = MKN_military_stat_militia_engineers
            }
            add_to_variable = {
                MKN_army_dig_in_speed_factor = 0.2
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_militia_hospitals
            }
            add_to_variable = {
                MKN_army_casualty_trickleback = 0.06
            }
        }
    }
    if = {
        limit = {
            has_country_flag = MKN_tactic_flexible_orders_unlocked
        }
        add_to_variable = {
            MKN_army_conscription = 0.02
        }
        add_to_variable = {
            MKN_army_planning_speed = 0.15
        }
    }
    else = {
        if = {
            limit = {
                has_country_flag = MKN_military_stat_flexible_orders
            }
            add_to_variable = {
                MKN_army_planning_speed = 0.15
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_rural_reserve
            }
            add_to_variable = {
                MKN_army_conscription = 0.02
            }
        }
    }
    if = {
        limit = {
            has_country_flag = MKN_tactic_tachanka_tactics_unlocked
        }
        add_to_variable = {
            MKN_army_modifier_army_sub_unit_cavalry_defence_factor = 0.08
        }
        add_to_variable = {
            MKN_army_modifier_army_sub_unit_infantry_defence_factor = 0.05
        }
    }
    else = {
        if = {
            limit = {
                has_country_flag = MKN_military_stat_tachanka_tactics
            }
            add_to_variable = {
                MKN_army_modifier_army_sub_unit_cavalry_defence_factor = 0.08
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_mobile_rearguard
            }
            add_to_variable = {
                MKN_army_modifier_army_sub_unit_infantry_defence_factor = 0.05
            }
        }
    }
    if = {
        limit = {
            has_country_flag = MKN_tactic_free_column_exercises_unlocked
        }
        add_to_variable = {
            MKN_army_army_org_factor = 0.05
        }
    }
    else = {
        if = {
            limit = {
                has_country_flag = MKN_military_stat_free_column_exercises
            }
            add_to_variable = {
                MKN_army_army_org_factor = 0.05
            }
        }
    }
    if = {
        limit = {
            has_country_flag = MKN_tactic_motorized_infantry_unlocked
        }
        add_to_variable = {
            MKN_army_army_speed_factor = 0.04
        }
        add_to_variable = {
            MKN_army_modifier_army_sub_unit_infantry_speed_factor = 0.05
        }
    }
    else = {
        if = {
            limit = {
                has_country_flag = MKN_military_stat_motorized_infantry
            }
            add_to_variable = {
                MKN_army_modifier_army_sub_unit_infantry_speed_factor = 0.05
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_bridge_columns
            }
            add_to_variable = {
                MKN_army_army_speed_factor = 0.04
            }
        }
    }
    if = {
        limit = {
            has_country_flag = MKN_tactic_fuel_discipline_unlocked
        }
        add_to_variable = {
            MKN_army_army_fuel_consumption_factor = -0.1
        }
        add_to_variable = {
            MKN_army_planning_speed = 0.15
        }
    }
    else = {
        if = {
            limit = {
                has_country_flag = MKN_military_stat_fuel_discipline
            }
            add_to_variable = {
                MKN_army_army_fuel_consumption_factor = -0.1
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_staff_games
            }
            add_to_variable = {
                MKN_army_planning_speed = 0.15
            }
        }
    }
    if = {
        limit = {
            has_country_flag = MKN_tactic_mobile_medical_unlocked
        }
        add_to_variable = {
            MKN_army_army_armor_attack_factor = 0.05
        }
        add_to_variable = {
            MKN_army_casualty_trickleback = 0.05
        }
    }
    else = {
        if = {
            limit = {
                has_country_flag = MKN_military_stat_mobile_medical
            }
            add_to_variable = {
                MKN_army_casualty_trickleback = 0.05
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_combined_arms
            }
            add_to_variable = {
                MKN_army_army_armor_attack_factor = 0.05
            }
        }
    }
    if = {
        limit = {
            has_country_flag = MKN_tactic_armoured_manoeuvres_unlocked
        }
        add_to_variable = {
            MKN_army_army_armor_attack_factor = 0.04
        }
        add_to_variable = {
            MKN_army_land_reinforce_rate = 0.02
        }
        add_to_variable = {
            MKN_army_org_loss_when_moving = -0.1
        }
    }
    else = {
        if = {
            limit = {
                has_country_flag = MKN_military_stat_deep_reserves
            }
            add_to_variable = {
                MKN_army_land_reinforce_rate = 0.02
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_breakthrough_workshops
            }
            add_to_variable = {
                MKN_army_army_armor_attack_factor = 0.04
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_armoured_manoeuvres
            }
            add_to_variable = {
                MKN_army_org_loss_when_moving = -0.1
            }
        }
    }
    if = {
        limit = {
            has_country_flag = MKN_tactic_air_dispersal_unlocked
        }
        add_to_variable = {
            MKN_air_air_home_defence_factor = 0.1
        }
        add_to_variable = {
            MKN_air_air_range_factor = 0.05
        }
    }
    else = {
        if = {
            limit = {
                has_country_flag = MKN_military_stat_air_dispersal
            }
            add_to_variable = {
                MKN_air_air_home_defence_factor = 0.1
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_fighter_patrols
            }
            add_to_variable = {
                MKN_air_air_range_factor = 0.05
            }
        }
    }
    if = {
        limit = {
            has_country_flag = MKN_tactic_night_interceptors_unlocked
        }
        add_to_variable = {
            MKN_air_air_intercept_efficiency = 0.05
        }
        add_to_variable = {
            MKN_air_air_interception_detect_factor = 0.1
        }
    }
    else = {
        if = {
            limit = {
                has_country_flag = MKN_military_stat_air_radar_school
            }
            add_to_variable = {
                MKN_air_air_interception_detect_factor = 0.1
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_night_interceptors
            }
            add_to_variable = {
                MKN_air_air_intercept_efficiency = 0.05
            }
        }
    }
    if = {
        limit = {
            has_country_flag = MKN_tactic_fighter_conversion_unlocked
        }
        add_to_variable = {
            MKN_air_air_accidents_factor = -0.05
        }
        add_to_variable = {
            MKN_air_air_agility_factor = 0.04
        }
    }
    else = {
        if = {
            limit = {
                has_country_flag = MKN_military_stat_aircraft_spares
            }
            add_to_variable = {
                MKN_air_air_accidents_factor = -0.05
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_fighter_conversion
            }
            add_to_variable = {
                MKN_air_air_agility_factor = 0.04
            }
        }
    }
    if = {
        limit = {
            has_country_flag = MKN_tactic_air_rescue_unlocked
        }
        add_to_variable = {
            MKN_air_air_ace_generation_chance_factor = 0.1
        }
        add_to_variable = {
            MKN_air_air_mission_efficiency = 0.05
        }
    }
    else = {
        if = {
            limit = {
                has_country_flag = MKN_military_stat_air_rescue
            }
            add_to_variable = {
                MKN_air_air_ace_generation_chance_factor = 0.1
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_fighter_controllers
            }
            add_to_variable = {
                MKN_air_air_mission_efficiency = 0.05
            }
        }
    }
    if = {
        limit = {
            has_country_flag = MKN_tactic_sky_watch_exercises_unlocked
        }
        add_to_variable = {
            MKN_air_air_attack_factor = 0.04
        }
        add_to_variable = {
            MKN_air_air_home_defence_factor = 0.1
        }
    }
    else = {
        if = {
            limit = {
                has_country_flag = MKN_military_stat_air_home_defence
            }
            add_to_variable = {
                MKN_air_air_home_defence_factor = 0.1
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_sky_watch_exercises
            }
            add_to_variable = {
                MKN_air_air_attack_factor = 0.04
            }
        }
    }
    if = {
        limit = {
            has_country_flag = MKN_tactic_tactical_recon_unlocked
        }
        add_to_variable = {
            MKN_air_air_range_factor = 0.07
        }
        add_to_variable = {
            MKN_air_recon_factor = 0.1
        }
    }
    else = {
        if = {
            limit = {
                has_country_flag = MKN_military_stat_tactical_recon
            }
            add_to_variable = {
                MKN_air_recon_factor = 0.1
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_bomber_navigation
            }
            add_to_variable = {
                MKN_air_air_range_factor = 0.07
            }
        }
    }
    if = {
        limit = {
            has_country_flag = MKN_tactic_air_supply_lift_unlocked
        }
        add_to_variable = {
            MKN_air_naval_strike_attack_factor = 0.1
        }
        add_to_variable = {
            MKN_air_supply_consumption_factor = -0.03
        }
    }
    else = {
        if = {
            limit = {
                has_country_flag = MKN_military_stat_air_supply_lift
            }
            add_to_variable = {
                MKN_air_supply_consumption_factor = -0.03
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_air_coastal_support
            }
            add_to_variable = {
                MKN_air_naval_strike_attack_factor = 0.1
            }
        }
    }
    if = {
        limit = {
            has_country_flag = MKN_tactic_replacement_crews_unlocked
        }
        add_to_variable = {
            MKN_air_air_accidents_factor = -0.05
        }
        add_to_variable = {
            MKN_air_air_fuel_consumption_factor = -0.05
        }
    }
    else = {
        if = {
            limit = {
                has_country_flag = MKN_military_stat_cas_replacement_crews
            }
            add_to_variable = {
                MKN_air_air_accidents_factor = -0.05
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_attack_wing_rotations
            }
            add_to_variable = {
                MKN_air_air_fuel_consumption_factor = -0.05
            }
        }
    }
    if = {
        limit = {
            has_country_flag = MKN_tactic_weather_service_unlocked
        }
        add_to_variable = {
            MKN_air_air_fuel_consumption_factor = -0.1
        }
        add_to_variable = {
            MKN_air_air_mission_efficiency = 0.04
        }
    }
    else = {
        if = {
            limit = {
                has_country_flag = MKN_military_stat_airfield_fuel
            }
            add_to_variable = {
                MKN_air_air_fuel_consumption_factor = -0.1
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_air_weather_service
            }
            add_to_variable = {
                MKN_air_air_mission_efficiency = 0.04
            }
        }
    }
    if = {
        limit = {
            has_country_flag = MKN_tactic_joint_target_planning_unlocked
        }
        add_to_variable = {
            MKN_air_air_cas_efficiency = 0.1
        }
    }
    else = {
        if = {
            limit = {
                has_country_flag = MKN_military_stat_joint_target_planning
            }
            add_to_variable = {
                MKN_air_air_cas_efficiency = 0.05
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_cas_joint_exercises
            }
            add_to_variable = {
                MKN_air_air_cas_efficiency = 0.05
            }
        }
    }
    if = {
        limit = {
            has_country_flag = MKN_tactic_damage_control_unlocked
        }
        add_to_variable = {
            MKN_navy_naval_detection = 0.08
        }
        add_to_variable = {
            MKN_navy_naval_ship_recovery_chance_factor = 0.1
        }
    }
    else = {
        if = {
            limit = {
                has_country_flag = MKN_military_stat_fleet_damage_control
            }
            add_to_variable = {
                MKN_navy_naval_ship_recovery_chance_factor = 0.1
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_coastal_watch
            }
            add_to_variable = {
                MKN_navy_naval_detection = 0.08
            }
        }
    }
    if = {
        limit = {
            has_country_flag = MKN_tactic_sweeper_sections_unlocked
        }
        add_to_variable = {
            MKN_navy_mines_sweeping_by_fleets_factor = 0.25
        }
        add_to_variable = {
            MKN_navy_screening_efficiency = 0.07
        }
    }
    else = {
        if = {
            limit = {
                has_country_flag = MKN_military_stat_sweeper_sections
            }
            add_to_variable = {
                MKN_navy_mines_sweeping_by_fleets_factor = 0.25
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_escort_radio_net
            }
            add_to_variable = {
                MKN_navy_screening_efficiency = 0.07
            }
        }
    }
    if = {
        limit = {
            has_country_flag = MKN_tactic_coastal_depots_unlocked
        }
        add_to_variable = {
            MKN_navy_naval_coordination = 0.08
        }
        add_to_variable = {
            MKN_navy_navy_fuel_consumption_factor = -0.1
        }
    }
    else = {
        if = {
            limit = {
                has_country_flag = MKN_military_stat_coastal_depots
            }
            add_to_variable = {
                MKN_navy_navy_fuel_consumption_factor = -0.1
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_river_sea_coordination
            }
            add_to_variable = {
                MKN_navy_naval_coordination = 0.08
            }
        }
    }
    if = {
        limit = {
            has_country_flag = MKN_tactic_convoy_rescue_unlocked
        }
        add_to_variable = {
            MKN_navy_navy_casualty_on_sink = -0.1
        }
        add_to_variable = {
            MKN_navy_navy_submarine_detection_factor = 0.15
        }
    }
    else = {
        if = {
            limit = {
                has_country_flag = MKN_military_stat_anti_submarine_patrols
            }
            add_to_variable = {
                MKN_navy_navy_submarine_detection_factor = 0.15
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_convoy_rescue
            }
            add_to_variable = {
                MKN_navy_navy_casualty_on_sink = -0.1
            }
        }
    }
    if = {
        limit = {
            has_country_flag = MKN_tactic_coastal_fleet_exercises_unlocked
        }
        add_to_variable = {
            MKN_navy_convoy_escort_efficiency = 0.05
        }
        add_to_variable = {
            MKN_navy_naval_defense_factor = 0.05
        }
    }
    else = {
        if = {
            limit = {
                has_country_flag = MKN_military_stat_escort_reserves
            }
            add_to_variable = {
                MKN_navy_naval_defense_factor = 0.05
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_coastal_fleet_exercises
            }
            add_to_variable = {
                MKN_navy_convoy_escort_efficiency = 0.05
            }
        }
    }
    if = {
        limit = {
            has_country_flag = MKN_tactic_submarine_listening_unlocked
        }
        add_to_variable = {
            MKN_navy_naval_detection = 0.08
        }
        add_to_variable = {
            MKN_navy_naval_speed_factor = 0.08
        }
    }
    else = {
        if = {
            limit = {
                has_country_flag = MKN_military_stat_submarine_listening
            }
            add_to_variable = {
                MKN_navy_naval_detection = 0.08
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_fast_attack_craft
            }
            add_to_variable = {
                MKN_navy_naval_speed_factor = 0.08
            }
        }
    }
    if = {
        limit = {
            has_country_flag = MKN_tactic_radio_discipline_unlocked
        }
        add_to_variable = {
            MKN_navy_naval_torpedo_reveal_chance_factor = -0.08
        }
        add_to_variable = {
            MKN_navy_repair_speed_factor = 0.15
        }
    }
    else = {
        if = {
            limit = {
                has_country_flag = MKN_military_stat_raider_radio_discipline
            }
            add_to_variable = {
                MKN_navy_naval_torpedo_reveal_chance_factor = -0.08
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_submarine_repair
            }
            add_to_variable = {
                MKN_navy_repair_speed_factor = 0.15
            }
        }
    }
    if = {
        limit = {
            has_country_flag = MKN_tactic_raider_weather_unlocked
        }
        add_to_variable = {
            MKN_navy_naval_detection = 0.05
        }
        add_to_variable = {
            MKN_navy_navy_submarine_defence_factor = 0.08
        }
    }
    else = {
        if = {
            limit = {
                has_country_flag = MKN_military_stat_raider_weather
            }
            add_to_variable = {
                MKN_navy_naval_detection = 0.05
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_raider_replacement_crews
            }
            add_to_variable = {
                MKN_navy_navy_submarine_defence_factor = 0.08
            }
        }
    }
    if = {
        limit = {
            has_country_flag = MKN_tactic_torpedo_ambushes_unlocked
        }
        add_to_variable = {
            MKN_navy_convoy_raiding_efficiency_factor = 0.1
        }
        add_to_variable = {
            MKN_navy_naval_torpedo_hit_chance_factor = 0.05
        }
    }
    else = {
        if = {
            limit = {
                has_country_flag = MKN_military_stat_torpedo_ambushes
            }
            add_to_variable = {
                MKN_navy_naval_torpedo_hit_chance_factor = 0.05
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_disrupt_enemy_trade
            }
            add_to_variable = {
                MKN_navy_convoy_raiding_efficiency_factor = 0.1
            }
        }
    }
    if = {
        limit = {
            has_country_flag = MKN_tactic_raider_escape_routes_unlocked
        }
        add_to_variable = {
            MKN_navy_naval_retreat_speed = 0.15
        }
        add_to_variable = {
            MKN_navy_navy_submarine_attack_factor = 0.05
        }
    }
    else = {
        if = {
            limit = {
                has_country_flag = MKN_military_stat_raider_escape_routes
            }
            add_to_variable = {
                MKN_navy_naval_retreat_speed = 0.15
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_military_stat_raider_exercises
            }
            add_to_variable = {
                MKN_navy_navy_submarine_attack_factor = 0.05
            }
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_steppe_legions
        }
        add_to_variable = {
            MKN_army_army_org_factor = 0.05
        }
        add_to_variable = {
            MKN_army_war_support_factor = 0.1
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_ataman_directorate
        }
        add_to_variable = {
            MKN_army_planning_speed = 0.05
        }
    }
    remove_ideas = {
        MKN_military_directory
        MKN_tachanka_warfare
        MKN_railway_guards
        MKN_steel_horses_idea
        MKN_batko_cavalry_idea
        MKN_black_guard_veterans_idea
        MKN_steppe_quartermasters_idea
        MKN_free_airmen
        MKN_black_swarm_idea
    }
    if = {
        limit = {
            has_completed_focus = MKN_abolish_election_of_commanders
        }
        add_to_variable = {
            MKN_army_planning_speed = 0.1
        }
        add_to_variable = {
            MKN_army_army_org_factor = 0.1
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_militarize_communes
        }
        add_to_variable = {
            MKN_army_conscription = 0.02
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_iron_fist_trains
        }
        add_to_variable = {
            MKN_army_supply_consumption_factor = -0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_the_black_horde
        }
        add_to_variable = {
            MKN_army_army_attack_factor = 0.25
        }
        add_to_variable = {
            MKN_army_breakthrough_factor = 0.3
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_abolish_general_staff
        }
        add_to_variable = {
            MKN_army_land_reinforce_rate = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_arms_to_the_people
        }
        add_to_variable = {
            MKN_army_conscription = 0.02
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_black_international
        }
        add_to_variable = {
            MKN_army_send_volunteer_size = 3
        }
        add_to_variable = {
            MKN_army_send_volunteers_tension = -0.5
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_beacon_of_statelessness
        }
        add_to_variable = {
            MKN_army_army_core_defence_factor = 0.35
        }
        add_to_variable = {
            MKN_army_resistance_damage_to_garrison_on_our_occupied_states = 0.75
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_steppe_snipers
        }
        add_to_variable = {
            MKN_army_army_defence_factor = 0.15
        }
        add_to_variable = {
            MKN_army_recon_factor = 0.2
        }
        add_to_variable = {
            MKN_army_enemy_army_bonus_air_superiority_factor = -0.15
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_cavalry_ambush
        }
        add_to_variable = {
            MKN_army_modifier_army_sub_unit_cavalry_attack_factor = 0.3
        }
        add_to_variable = {
            MKN_army_motorized_attack_factor = 0.3
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_impregnable_granary
        }
        add_to_variable = {
            MKN_army_army_core_defence_factor = 0.5
        }
        add_to_variable = {
            MKN_army_enemy_attrition = 0.4
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_red_military_specialists
        }
        add_to_variable = {
            MKN_army_army_org_factor = 0.15
        }
        add_to_variable = {
            MKN_army_planning_speed = 0.15
        }
    }
    if = {
        limit = {
            OR = {
                has_completed_focus = MKN_steppe_general_staff
                has_country_flag = MKN_military_stat_village_muster
                has_country_flag = MKN_military_stat_steppe_general_staff
                has_country_flag = MKN_military_stat_bridge_columns
                has_country_flag = MKN_military_stat_recovery_tractors
                has_country_flag = MKN_military_stat_night_marches
                has_country_flag = MKN_military_stat_fuel_discipline
                has_country_flag = MKN_military_stat_tachanka_columns
                has_country_flag = MKN_military_stat_radio_sections
                has_country_flag = MKN_military_stat_batko_cavalry
                has_country_flag = MKN_military_stat_motorized_infantry
                has_country_flag = MKN_military_stat_scout_parties
                has_country_flag = MKN_military_stat_staff_games
                has_country_flag = MKN_military_stat_mobile_medical
                has_country_flag = MKN_military_stat_tank_maintenance
                has_country_flag = MKN_military_stat_militia_hospitals
                has_country_flag = MKN_military_stat_field_veterinary
                has_country_flag = MKN_military_stat_tank_crews
                has_country_flag = MKN_military_stat_rural_reserve
                has_country_flag = MKN_military_stat_militia_junior_leaders
                has_country_flag = MKN_military_stat_free_column_exercises
                has_country_flag = MKN_military_stat_remount_artels
                has_country_flag = MKN_military_stat_mobile_rearguard
                has_country_flag = MKN_military_stat_machinegun_carts
                has_country_flag = MKN_military_stat_fire_tables
                has_country_flag = MKN_military_stat_mechanized_compact
                has_country_flag = MKN_military_stat_deep_reserves
                has_country_flag = MKN_military_stat_steppe_quartermasters
                has_country_flag = MKN_military_stat_steel_horses
                has_country_flag = MKN_military_stat_steppe_camouflage
                has_country_flag = MKN_military_stat_artillery_artels
                has_country_flag = MKN_military_stat_mobile_supply_columns
                has_country_flag = MKN_military_stat_free_army_compact
                has_country_flag = MKN_military_stat_flexible_orders
                has_country_flag = MKN_military_stat_tachanka_tactics
                has_country_flag = MKN_military_stat_hidden_depots
                has_country_flag = MKN_military_stat_breakthrough_workshops
                has_country_flag = MKN_military_stat_militia_engineers
                has_country_flag = MKN_military_stat_armoured_manoeuvres
                has_country_flag = MKN_military_stat_militia_signals
                has_country_flag = MKN_military_stat_combined_arms
                has_country_flag = MKN_military_stat_local_guides
                has_country_flag = MKN_military_stat_railway_war
                has_completed_focus = MKN_steppe_legions
                has_completed_focus = MKN_ataman_directorate
                has_completed_focus = MKN_abolish_election_of_commanders
                has_completed_focus = MKN_militarize_communes
                has_completed_focus = MKN_iron_fist_trains
                has_completed_focus = MKN_the_black_horde
                has_completed_focus = MKN_abolish_general_staff
                has_completed_focus = MKN_arms_to_the_people
                has_completed_focus = MKN_black_international
                has_completed_focus = MKN_beacon_of_statelessness
                has_completed_focus = MKN_steppe_snipers
                has_completed_focus = MKN_cavalry_ambush
                has_completed_focus = MKN_impregnable_granary
                has_completed_focus = MKN_red_military_specialists
            }
            NOT = {
                has_dynamic_modifier = {
                    modifier = MKN_army_development
                }
            }
        }
        add_dynamic_modifier = {
            modifier = MKN_army_development
        }
    }
    if = {
        limit = {
            OR = {
                has_completed_focus = MKN_steppe_hawks_and_schools
                has_country_flag = MKN_military_stat_air_rescue
                has_country_flag = MKN_military_stat_air_home_defence
                has_country_flag = MKN_military_stat_village_airfields
                has_country_flag = MKN_military_stat_fighter_controllers
                has_country_flag = MKN_military_stat_joint_target_planning
                has_country_flag = MKN_military_stat_air_coastal_support
                has_country_flag = MKN_military_stat_bombing_ranges
                has_country_flag = MKN_military_stat_tactical_recon
                has_country_flag = MKN_military_stat_aircraft_spares
                has_country_flag = MKN_military_stat_air_support_compact
                has_country_flag = MKN_military_stat_observation_posts
                has_country_flag = MKN_military_stat_air_ground_liaisons
                has_country_flag = MKN_military_stat_air_map_bureau
                has_country_flag = MKN_military_stat_aircraft_recovery
                has_country_flag = MKN_military_stat_attack_wing_rotations
                has_country_flag = MKN_military_stat_fighter_conversion
                has_country_flag = MKN_military_stat_aircraft_artels
                has_country_flag = MKN_military_stat_cas_joint_exercises
                has_country_flag = MKN_military_stat_fighter_patrols
                has_country_flag = MKN_military_stat_air_weather_service
                has_country_flag = MKN_military_stat_air_warning
                has_country_flag = MKN_military_stat_radio_beacons
                has_country_flag = MKN_military_stat_steppe_hawks
                has_country_flag = MKN_military_stat_flying_artillery
                has_country_flag = MKN_military_stat_target_markers
                has_country_flag = MKN_military_stat_interceptor_pairs
                has_country_flag = MKN_military_stat_gulyaipole_pilot_school
                has_country_flag = MKN_military_stat_forward_airstrips
                has_country_flag = MKN_military_stat_fighter_instructors
                has_country_flag = MKN_military_stat_night_interceptors
                has_country_flag = MKN_military_stat_air_supply_lift
                has_country_flag = MKN_military_stat_close_support_program
                has_country_flag = MKN_military_stat_airframe_jigs
                has_country_flag = MKN_military_stat_cas_replacement_crews
                has_country_flag = MKN_military_stat_airfield_fuel
                has_country_flag = MKN_military_stat_attack_air_artels
                has_country_flag = MKN_military_stat_air_radar_school
                has_country_flag = MKN_military_stat_cas_maintenance
                has_country_flag = MKN_military_stat_black_swarm
                has_country_flag = MKN_military_stat_sky_watch_exercises
                has_country_flag = MKN_military_stat_air_dispersal
                has_country_flag = MKN_military_stat_bomber_navigation
                has_country_flag = MKN_military_stat_free_sky_compact
            }
            NOT = {
                has_dynamic_modifier = {
                    modifier = MKN_air_development
                }
            }
        }
        add_dynamic_modifier = {
            modifier = MKN_air_development
        }
    }
    if = {
        limit = {
            OR = {
                has_completed_focus = MKN_black_sea_flotilla_and_yards
                has_country_flag = MKN_military_stat_convoy_rescue
                has_country_flag = MKN_military_stat_raider_weather
                has_country_flag = MKN_military_stat_anti_submarine_patrols
                has_country_flag = MKN_military_stat_black_sea_flotilla
                has_country_flag = MKN_military_stat_coastal_defense_steppe
                has_country_flag = MKN_military_stat_black_sea_escorts
                has_country_flag = MKN_military_stat_night_sorties
                has_country_flag = MKN_military_stat_hidden_anchorages
                has_country_flag = MKN_military_stat_river_sea_coordination
                has_country_flag = MKN_military_stat_raider_dockyard
                has_country_flag = MKN_military_stat_convoy_schedules
                has_country_flag = MKN_military_stat_escort_compact
                has_country_flag = MKN_military_stat_dnieper_gun_flotilla
                has_country_flag = MKN_military_stat_submarine_listening
                has_country_flag = MKN_military_stat_escort_crews
                has_country_flag = MKN_military_stat_sweeper_sections
                has_country_flag = MKN_military_stat_raider_compact
                has_country_flag = MKN_military_stat_disrupt_enemy_trade
                has_country_flag = MKN_military_stat_raider_escape_routes
                has_country_flag = MKN_military_stat_coastal_signal_posts
                has_country_flag = MKN_military_stat_submarine_repair
                has_country_flag = MKN_military_stat_dnieper_patrol
                has_country_flag = MKN_military_stat_kherson_shipyard
                has_country_flag = MKN_military_stat_coastal_fleet_exercises
                has_country_flag = MKN_military_stat_escort_radio_net
                has_country_flag = MKN_military_stat_raider_replacement_crews
                has_country_flag = MKN_military_stat_torpedo_artels
                has_country_flag = MKN_military_stat_escort_reserves
                has_country_flag = MKN_military_stat_naval_intelligence
                has_country_flag = MKN_military_stat_raider_exercises
                has_country_flag = MKN_military_stat_harbour_dredging
                has_country_flag = MKN_military_stat_submarine_crews
                has_country_flag = MKN_military_stat_coastal_watch
                has_country_flag = MKN_military_stat_raider_supply
                has_country_flag = MKN_military_stat_fast_attack_craft
                has_country_flag = MKN_military_stat_torpedo_ambushes
                has_country_flag = MKN_military_stat_torpedo_trials
                has_country_flag = MKN_military_stat_raider_radio_discipline
                has_country_flag = MKN_military_stat_depth_charge_school
                has_country_flag = MKN_military_stat_black_sea_smugglers
                has_country_flag = MKN_military_stat_fleet_damage_control
                has_country_flag = MKN_military_stat_hull_repair_artels
                has_country_flag = MKN_military_stat_coastal_depots
            }
            NOT = {
                has_dynamic_modifier = {
                    modifier = MKN_navy_development
                }
            }
        }
        add_dynamic_modifier = {
            modifier = MKN_navy_development
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_free_army_compact
        }
        add_to_variable = {
            MKN_army_supply_consumption_factor = -0.1
        }
        add_to_variable = {
            MKN_army_modifier_army_sub_unit_cavalry_attack_factor = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_mechanized_compact
        }
        add_to_variable = {
            MKN_army_breakthrough_factor = 0.1
        }
        add_to_variable = {
            MKN_army_army_armor_attack_factor = 0.05
        }
    }
    set_country_flag = MKN_services_redesign_v5
}
MKN_migrate_military_hq = {
    if = {
        limit = {
            NOT = {
                has_country_flag = MKN_military_hq_migrated_v5
            }
        }
        if = {
            limit = {
                has_completed_focus = MKN_air_coastal_support
            }
            set_country_flag = MKN_military_stat_air_coastal_support
            set_country_flag = MKN_military_reward_air_coastal_support
        }
        if = {
            limit = {
                has_completed_focus = MKN_air_dispersal
            }
            set_country_flag = MKN_military_stat_air_dispersal
            set_country_flag = MKN_military_reward_air_dispersal
        }
        if = {
            limit = {
                has_completed_focus = MKN_air_ground_liaisons
            }
            set_country_flag = MKN_military_stat_air_ground_liaisons
            set_country_flag = MKN_military_reward_air_ground_liaisons
        }
        if = {
            limit = {
                has_completed_focus = MKN_air_home_defence
            }
            set_country_flag = MKN_military_stat_air_home_defence
            set_country_flag = MKN_military_reward_air_home_defence
        }
        if = {
            limit = {
                has_completed_focus = MKN_air_map_bureau
            }
            set_country_flag = MKN_military_stat_air_map_bureau
            set_country_flag = MKN_military_reward_air_map_bureau
        }
        if = {
            limit = {
                has_completed_focus = MKN_air_radar_school
            }
            set_country_flag = MKN_military_stat_air_radar_school
            set_country_flag = MKN_military_reward_air_radar_school
        }
        if = {
            limit = {
                has_completed_focus = MKN_air_rescue
            }
            set_country_flag = MKN_military_stat_air_rescue
            set_country_flag = MKN_military_reward_air_rescue
        }
        if = {
            limit = {
                has_completed_focus = MKN_air_supply_lift
            }
            set_country_flag = MKN_military_stat_air_supply_lift
            set_country_flag = MKN_military_reward_air_supply_lift
        }
        if = {
            limit = {
                has_completed_focus = MKN_air_support_compact
            }
            set_country_flag = MKN_military_stat_air_support_compact
            set_country_flag = MKN_military_reward_air_support_compact
        }
        if = {
            limit = {
                has_completed_focus = MKN_air_warning
            }
            set_country_flag = MKN_military_stat_air_warning
            set_country_flag = MKN_military_reward_air_warning
        }
        if = {
            limit = {
                has_completed_focus = MKN_air_weather_service
            }
            set_country_flag = MKN_military_stat_air_weather_service
            set_country_flag = MKN_military_reward_air_weather_service
        }
        if = {
            limit = {
                has_completed_focus = MKN_aircraft_artels
            }
            set_country_flag = MKN_military_stat_aircraft_artels
            set_country_flag = MKN_military_reward_aircraft_artels
        }
        if = {
            limit = {
                has_completed_focus = MKN_aircraft_recovery
            }
            set_country_flag = MKN_military_stat_aircraft_recovery
            set_country_flag = MKN_military_reward_aircraft_recovery
        }
        if = {
            limit = {
                has_completed_focus = MKN_aircraft_spares
            }
            set_country_flag = MKN_military_stat_aircraft_spares
            set_country_flag = MKN_military_reward_aircraft_spares
        }
        if = {
            limit = {
                has_completed_focus = MKN_airfield_fuel
            }
            set_country_flag = MKN_military_stat_airfield_fuel
            set_country_flag = MKN_military_reward_airfield_fuel
        }
        if = {
            limit = {
                has_completed_focus = MKN_airframe_jigs
            }
            set_country_flag = MKN_military_stat_airframe_jigs
            set_country_flag = MKN_military_reward_airframe_jigs
        }
        if = {
            limit = {
                has_completed_focus = MKN_anti_submarine_patrols
            }
            set_country_flag = MKN_military_stat_anti_submarine_patrols
            set_country_flag = MKN_military_reward_anti_submarine_patrols
        }
        if = {
            limit = {
                has_completed_focus = MKN_armoured_manoeuvres
            }
            set_country_flag = MKN_military_stat_armoured_manoeuvres
            set_country_flag = MKN_military_reward_armoured_manoeuvres
        }
        if = {
            limit = {
                has_completed_focus = MKN_artillery_artels
            }
            set_country_flag = MKN_military_stat_artillery_artels
            set_country_flag = MKN_military_reward_artillery_artels
        }
        if = {
            limit = {
                has_completed_focus = MKN_attack_air_artels
            }
            set_country_flag = MKN_military_stat_attack_air_artels
            set_country_flag = MKN_military_reward_attack_air_artels
        }
        if = {
            limit = {
                has_completed_focus = MKN_attack_wing_rotations
            }
            set_country_flag = MKN_military_stat_attack_wing_rotations
            set_country_flag = MKN_military_reward_attack_wing_rotations
        }
        if = {
            limit = {
                has_completed_focus = MKN_batko_cavalry
            }
            set_country_flag = MKN_military_stat_batko_cavalry
            set_country_flag = MKN_military_reward_batko_cavalry
        }
        if = {
            limit = {
                has_completed_focus = MKN_black_sea_escorts
            }
            set_country_flag = MKN_military_stat_black_sea_escorts
            set_country_flag = MKN_military_reward_black_sea_escorts
        }
        if = {
            limit = {
                has_completed_focus = MKN_black_sea_flotilla
            }
            set_country_flag = MKN_military_stat_black_sea_flotilla
            set_country_flag = MKN_military_reward_black_sea_flotilla
        }
        if = {
            limit = {
                has_completed_focus = MKN_black_sea_smugglers
            }
            set_country_flag = MKN_military_stat_black_sea_smugglers
            set_country_flag = MKN_military_reward_black_sea_smugglers
        }
        if = {
            limit = {
                has_completed_focus = MKN_black_swarm
            }
            set_country_flag = MKN_military_stat_black_swarm
            set_country_flag = MKN_military_reward_black_swarm
        }
        if = {
            limit = {
                has_completed_focus = MKN_bomber_navigation
            }
            set_country_flag = MKN_military_stat_bomber_navigation
            set_country_flag = MKN_military_reward_bomber_navigation
        }
        if = {
            limit = {
                has_completed_focus = MKN_bombing_ranges
            }
            set_country_flag = MKN_military_stat_bombing_ranges
            set_country_flag = MKN_military_reward_bombing_ranges
        }
        if = {
            limit = {
                has_completed_focus = MKN_breakthrough_workshops
            }
            set_country_flag = MKN_military_stat_breakthrough_workshops
            set_country_flag = MKN_military_reward_breakthrough_workshops
        }
        if = {
            limit = {
                has_completed_focus = MKN_bridge_columns
            }
            set_country_flag = MKN_military_stat_bridge_columns
            set_country_flag = MKN_military_reward_bridge_columns
        }
        if = {
            limit = {
                has_completed_focus = MKN_cas_joint_exercises
            }
            set_country_flag = MKN_military_stat_cas_joint_exercises
            set_country_flag = MKN_military_reward_cas_joint_exercises
        }
        if = {
            limit = {
                has_completed_focus = MKN_cas_maintenance
            }
            set_country_flag = MKN_military_stat_cas_maintenance
            set_country_flag = MKN_military_reward_cas_maintenance
        }
        if = {
            limit = {
                has_completed_focus = MKN_cas_replacement_crews
            }
            set_country_flag = MKN_military_stat_cas_replacement_crews
            set_country_flag = MKN_military_reward_cas_replacement_crews
        }
        if = {
            limit = {
                has_completed_focus = MKN_close_support_program
            }
            set_country_flag = MKN_military_stat_close_support_program
            set_country_flag = MKN_military_reward_close_support_program
        }
        if = {
            limit = {
                has_completed_focus = MKN_coastal_defense_steppe
            }
            set_country_flag = MKN_military_stat_coastal_defense_steppe
            set_country_flag = MKN_military_reward_coastal_defense_steppe
        }
        if = {
            limit = {
                has_completed_focus = MKN_coastal_depots
            }
            set_country_flag = MKN_military_stat_coastal_depots
            set_country_flag = MKN_military_reward_coastal_depots
        }
        if = {
            limit = {
                has_completed_focus = MKN_coastal_fleet_exercises
            }
            set_country_flag = MKN_military_stat_coastal_fleet_exercises
            set_country_flag = MKN_military_reward_coastal_fleet_exercises
        }
        if = {
            limit = {
                has_completed_focus = MKN_coastal_signal_posts
            }
            set_country_flag = MKN_military_stat_coastal_signal_posts
            set_country_flag = MKN_military_reward_coastal_signal_posts
        }
        if = {
            limit = {
                has_completed_focus = MKN_coastal_watch
            }
            set_country_flag = MKN_military_stat_coastal_watch
            set_country_flag = MKN_military_reward_coastal_watch
        }
        if = {
            limit = {
                has_completed_focus = MKN_combined_arms
            }
            set_country_flag = MKN_military_stat_combined_arms
            set_country_flag = MKN_military_reward_combined_arms
        }
        if = {
            limit = {
                has_completed_focus = MKN_convoy_rescue
            }
            set_country_flag = MKN_military_stat_convoy_rescue
            set_country_flag = MKN_military_reward_convoy_rescue
        }
        if = {
            limit = {
                has_completed_focus = MKN_convoy_schedules
            }
            set_country_flag = MKN_military_stat_convoy_schedules
            set_country_flag = MKN_military_reward_convoy_schedules
        }
        if = {
            limit = {
                has_completed_focus = MKN_deep_reserves
            }
            set_country_flag = MKN_military_stat_deep_reserves
            set_country_flag = MKN_military_reward_deep_reserves
        }
        if = {
            limit = {
                has_completed_focus = MKN_depth_charge_school
            }
            set_country_flag = MKN_military_stat_depth_charge_school
            set_country_flag = MKN_military_reward_depth_charge_school
        }
        if = {
            limit = {
                has_completed_focus = MKN_disrupt_enemy_trade
            }
            set_country_flag = MKN_military_stat_disrupt_enemy_trade
            set_country_flag = MKN_military_reward_disrupt_enemy_trade
        }
        if = {
            limit = {
                has_completed_focus = MKN_dnieper_gun_flotilla
            }
            set_country_flag = MKN_military_stat_dnieper_gun_flotilla
            set_country_flag = MKN_military_reward_dnieper_gun_flotilla
        }
        if = {
            limit = {
                has_completed_focus = MKN_dnieper_patrol
            }
            set_country_flag = MKN_military_stat_dnieper_patrol
            set_country_flag = MKN_military_reward_dnieper_patrol
        }
        if = {
            limit = {
                has_completed_focus = MKN_escort_compact
            }
            set_country_flag = MKN_military_stat_escort_compact
            set_country_flag = MKN_military_reward_escort_compact
        }
        if = {
            limit = {
                has_completed_focus = MKN_escort_crews
            }
            set_country_flag = MKN_military_stat_escort_crews
            set_country_flag = MKN_military_reward_escort_crews
        }
        if = {
            limit = {
                has_completed_focus = MKN_escort_radio_net
            }
            set_country_flag = MKN_military_stat_escort_radio_net
            set_country_flag = MKN_military_reward_escort_radio_net
        }
        if = {
            limit = {
                has_completed_focus = MKN_escort_reserves
            }
            set_country_flag = MKN_military_stat_escort_reserves
            set_country_flag = MKN_military_reward_escort_reserves
        }
        if = {
            limit = {
                has_completed_focus = MKN_fast_attack_craft
            }
            set_country_flag = MKN_military_stat_fast_attack_craft
            set_country_flag = MKN_military_reward_fast_attack_craft
        }
        if = {
            limit = {
                has_completed_focus = MKN_field_veterinary
            }
            set_country_flag = MKN_military_stat_field_veterinary
            set_country_flag = MKN_military_reward_field_veterinary
        }
        if = {
            limit = {
                has_completed_focus = MKN_fighter_controllers
            }
            set_country_flag = MKN_military_stat_fighter_controllers
            set_country_flag = MKN_military_reward_fighter_controllers
        }
        if = {
            limit = {
                has_completed_focus = MKN_fighter_conversion
            }
            set_country_flag = MKN_military_stat_fighter_conversion
            set_country_flag = MKN_military_reward_fighter_conversion
        }
        if = {
            limit = {
                has_completed_focus = MKN_fighter_instructors
            }
            set_country_flag = MKN_military_stat_fighter_instructors
            set_country_flag = MKN_military_reward_fighter_instructors
        }
        if = {
            limit = {
                has_completed_focus = MKN_fighter_patrols
            }
            set_country_flag = MKN_military_stat_fighter_patrols
            set_country_flag = MKN_military_reward_fighter_patrols
        }
        if = {
            limit = {
                has_completed_focus = MKN_fire_tables
            }
            set_country_flag = MKN_military_stat_fire_tables
            set_country_flag = MKN_military_reward_fire_tables
        }
        if = {
            limit = {
                has_completed_focus = MKN_fleet_damage_control
            }
            set_country_flag = MKN_military_stat_fleet_damage_control
            set_country_flag = MKN_military_reward_fleet_damage_control
        }
        if = {
            limit = {
                has_completed_focus = MKN_flexible_orders
            }
            set_country_flag = MKN_military_stat_flexible_orders
            set_country_flag = MKN_military_reward_flexible_orders
        }
        if = {
            limit = {
                has_completed_focus = MKN_flying_artillery
            }
            set_country_flag = MKN_military_stat_flying_artillery
            set_country_flag = MKN_military_reward_flying_artillery
        }
        if = {
            limit = {
                has_completed_focus = MKN_forward_airstrips
            }
            set_country_flag = MKN_military_stat_forward_airstrips
            set_country_flag = MKN_military_reward_forward_airstrips
        }
        if = {
            limit = {
                has_completed_focus = MKN_free_army_compact
            }
            set_country_flag = MKN_military_stat_free_army_compact
            set_country_flag = MKN_military_reward_free_army_compact
        }
        if = {
            limit = {
                has_completed_focus = MKN_free_column_exercises
            }
            set_country_flag = MKN_military_stat_free_column_exercises
            set_country_flag = MKN_military_reward_free_column_exercises
        }
        if = {
            limit = {
                has_completed_focus = MKN_free_sky_compact
            }
            set_country_flag = MKN_military_stat_free_sky_compact
            set_country_flag = MKN_military_reward_free_sky_compact
        }
        if = {
            limit = {
                has_completed_focus = MKN_fuel_discipline
            }
            set_country_flag = MKN_military_stat_fuel_discipline
            set_country_flag = MKN_military_reward_fuel_discipline
        }
        if = {
            limit = {
                has_completed_focus = MKN_gulyaipole_pilot_school
            }
            set_country_flag = MKN_military_stat_gulyaipole_pilot_school
            set_country_flag = MKN_military_reward_gulyaipole_pilot_school
        }
        if = {
            limit = {
                has_completed_focus = MKN_harbour_dredging
            }
            set_country_flag = MKN_military_stat_harbour_dredging
            set_country_flag = MKN_military_reward_harbour_dredging
        }
        if = {
            limit = {
                has_completed_focus = MKN_hidden_anchorages
            }
            set_country_flag = MKN_military_stat_hidden_anchorages
            set_country_flag = MKN_military_reward_hidden_anchorages
        }
        if = {
            limit = {
                has_completed_focus = MKN_hidden_depots
            }
            set_country_flag = MKN_military_stat_hidden_depots
            set_country_flag = MKN_military_reward_hidden_depots
        }
        if = {
            limit = {
                has_completed_focus = MKN_hull_repair_artels
            }
            set_country_flag = MKN_military_stat_hull_repair_artels
            set_country_flag = MKN_military_reward_hull_repair_artels
        }
        if = {
            limit = {
                has_completed_focus = MKN_interceptor_pairs
            }
            set_country_flag = MKN_military_stat_interceptor_pairs
            set_country_flag = MKN_military_reward_interceptor_pairs
        }
        if = {
            limit = {
                has_completed_focus = MKN_joint_target_planning
            }
            set_country_flag = MKN_military_stat_joint_target_planning
            set_country_flag = MKN_military_reward_joint_target_planning
        }
        if = {
            limit = {
                has_completed_focus = MKN_kherson_shipyard
            }
            set_country_flag = MKN_military_stat_kherson_shipyard
            set_country_flag = MKN_military_reward_kherson_shipyard
        }
        if = {
            limit = {
                has_completed_focus = MKN_local_guides
            }
            set_country_flag = MKN_military_stat_local_guides
            set_country_flag = MKN_military_reward_local_guides
        }
        if = {
            limit = {
                has_completed_focus = MKN_machinegun_carts
            }
            set_country_flag = MKN_military_stat_machinegun_carts
            set_country_flag = MKN_military_reward_machinegun_carts
        }
        if = {
            limit = {
                has_completed_focus = MKN_mechanized_compact
            }
            set_country_flag = MKN_military_stat_mechanized_compact
            set_country_flag = MKN_military_reward_mechanized_compact
        }
        if = {
            limit = {
                has_completed_focus = MKN_militia_engineers
            }
            set_country_flag = MKN_military_stat_militia_engineers
            set_country_flag = MKN_military_reward_militia_engineers
        }
        if = {
            limit = {
                has_completed_focus = MKN_militia_hospitals
            }
            set_country_flag = MKN_military_stat_militia_hospitals
            set_country_flag = MKN_military_reward_militia_hospitals
        }
        if = {
            limit = {
                has_completed_focus = MKN_militia_junior_leaders
            }
            set_country_flag = MKN_military_stat_militia_junior_leaders
            set_country_flag = MKN_military_reward_militia_junior_leaders
        }
        if = {
            limit = {
                has_completed_focus = MKN_militia_signals
            }
            set_country_flag = MKN_military_stat_militia_signals
            set_country_flag = MKN_military_reward_militia_signals
        }
        if = {
            limit = {
                has_completed_focus = MKN_mobile_medical
            }
            set_country_flag = MKN_military_stat_mobile_medical
            set_country_flag = MKN_military_reward_mobile_medical
        }
        if = {
            limit = {
                has_completed_focus = MKN_mobile_rearguard
            }
            set_country_flag = MKN_military_stat_mobile_rearguard
            set_country_flag = MKN_military_reward_mobile_rearguard
        }
        if = {
            limit = {
                has_completed_focus = MKN_mobile_supply_columns
            }
            set_country_flag = MKN_military_stat_mobile_supply_columns
            set_country_flag = MKN_military_reward_mobile_supply_columns
        }
        if = {
            limit = {
                has_completed_focus = MKN_motorized_infantry
            }
            set_country_flag = MKN_military_stat_motorized_infantry
            set_country_flag = MKN_military_reward_motorized_infantry
        }
        if = {
            limit = {
                has_completed_focus = MKN_naval_intelligence
            }
            set_country_flag = MKN_military_stat_naval_intelligence
            set_country_flag = MKN_military_reward_naval_intelligence
        }
        if = {
            limit = {
                has_completed_focus = MKN_night_interceptors
            }
            set_country_flag = MKN_military_stat_night_interceptors
            set_country_flag = MKN_military_reward_night_interceptors
        }
        if = {
            limit = {
                has_completed_focus = MKN_night_marches
            }
            set_country_flag = MKN_military_stat_night_marches
            set_country_flag = MKN_military_reward_night_marches
        }
        if = {
            limit = {
                has_completed_focus = MKN_night_sorties
            }
            set_country_flag = MKN_military_stat_night_sorties
            set_country_flag = MKN_military_reward_night_sorties
        }
        if = {
            limit = {
                has_completed_focus = MKN_observation_posts
            }
            set_country_flag = MKN_military_stat_observation_posts
            set_country_flag = MKN_military_reward_observation_posts
        }
        if = {
            limit = {
                has_completed_focus = MKN_radio_beacons
            }
            set_country_flag = MKN_military_stat_radio_beacons
            set_country_flag = MKN_military_reward_radio_beacons
        }
        if = {
            limit = {
                has_completed_focus = MKN_radio_sections
            }
            set_country_flag = MKN_military_stat_radio_sections
            set_country_flag = MKN_military_reward_radio_sections
        }
        if = {
            limit = {
                has_completed_focus = MKN_raider_compact
            }
            set_country_flag = MKN_military_stat_raider_compact
            set_country_flag = MKN_military_reward_raider_compact
        }
        if = {
            limit = {
                has_completed_focus = MKN_raider_dockyard
            }
            set_country_flag = MKN_military_stat_raider_dockyard
            set_country_flag = MKN_military_reward_raider_dockyard
        }
        if = {
            limit = {
                has_completed_focus = MKN_raider_escape_routes
            }
            set_country_flag = MKN_military_stat_raider_escape_routes
            set_country_flag = MKN_military_reward_raider_escape_routes
        }
        if = {
            limit = {
                has_completed_focus = MKN_raider_exercises
            }
            set_country_flag = MKN_military_stat_raider_exercises
            set_country_flag = MKN_military_reward_raider_exercises
        }
        if = {
            limit = {
                has_completed_focus = MKN_raider_radio_discipline
            }
            set_country_flag = MKN_military_stat_raider_radio_discipline
            set_country_flag = MKN_military_reward_raider_radio_discipline
        }
        if = {
            limit = {
                has_completed_focus = MKN_raider_replacement_crews
            }
            set_country_flag = MKN_military_stat_raider_replacement_crews
            set_country_flag = MKN_military_reward_raider_replacement_crews
        }
        if = {
            limit = {
                has_completed_focus = MKN_raider_supply
            }
            set_country_flag = MKN_military_stat_raider_supply
            set_country_flag = MKN_military_reward_raider_supply
        }
        if = {
            limit = {
                has_completed_focus = MKN_raider_weather
            }
            set_country_flag = MKN_military_stat_raider_weather
            set_country_flag = MKN_military_reward_raider_weather
        }
        if = {
            limit = {
                has_completed_focus = MKN_railway_war
            }
            set_country_flag = MKN_military_stat_railway_war
            set_country_flag = MKN_military_reward_railway_war
        }
        if = {
            limit = {
                has_completed_focus = MKN_recovery_tractors
            }
            set_country_flag = MKN_military_stat_recovery_tractors
            set_country_flag = MKN_military_reward_recovery_tractors
        }
        if = {
            limit = {
                has_completed_focus = MKN_remount_artels
            }
            set_country_flag = MKN_military_stat_remount_artels
            set_country_flag = MKN_military_reward_remount_artels
        }
        if = {
            limit = {
                has_completed_focus = MKN_river_sea_coordination
            }
            set_country_flag = MKN_military_stat_river_sea_coordination
            set_country_flag = MKN_military_reward_river_sea_coordination
        }
        if = {
            limit = {
                has_completed_focus = MKN_rural_reserve
            }
            set_country_flag = MKN_military_stat_rural_reserve
            set_country_flag = MKN_military_reward_rural_reserve
        }
        if = {
            limit = {
                has_completed_focus = MKN_scout_parties
            }
            set_country_flag = MKN_military_stat_scout_parties
            set_country_flag = MKN_military_reward_scout_parties
        }
        if = {
            limit = {
                has_completed_focus = MKN_sky_watch_exercises
            }
            set_country_flag = MKN_military_stat_sky_watch_exercises
            set_country_flag = MKN_military_reward_sky_watch_exercises
        }
        if = {
            limit = {
                has_completed_focus = MKN_staff_games
            }
            set_country_flag = MKN_military_stat_staff_games
            set_country_flag = MKN_military_reward_staff_games
        }
        if = {
            limit = {
                has_completed_focus = MKN_steel_horses
            }
            set_country_flag = MKN_military_stat_steel_horses
            set_country_flag = MKN_military_reward_steel_horses
        }
        if = {
            limit = {
                has_completed_focus = MKN_steppe_camouflage
            }
            set_country_flag = MKN_military_stat_steppe_camouflage
            set_country_flag = MKN_military_reward_steppe_camouflage
        }
        if = {
            limit = {
                has_completed_focus = MKN_steppe_general_staff
            }
            set_country_flag = MKN_military_stat_steppe_general_staff
            set_country_flag = MKN_military_reward_steppe_general_staff
        }
        if = {
            limit = {
                has_completed_focus = MKN_steppe_hawks
            }
            set_country_flag = MKN_military_stat_steppe_hawks
            set_country_flag = MKN_military_reward_steppe_hawks
        }
        if = {
            limit = {
                has_completed_focus = MKN_steppe_quartermasters
            }
            set_country_flag = MKN_military_stat_steppe_quartermasters
            set_country_flag = MKN_military_reward_steppe_quartermasters
        }
        if = {
            limit = {
                has_completed_focus = MKN_submarine_crews
            }
            set_country_flag = MKN_military_stat_submarine_crews
            set_country_flag = MKN_military_reward_submarine_crews
        }
        if = {
            limit = {
                has_completed_focus = MKN_submarine_listening
            }
            set_country_flag = MKN_military_stat_submarine_listening
            set_country_flag = MKN_military_reward_submarine_listening
        }
        if = {
            limit = {
                has_completed_focus = MKN_submarine_repair
            }
            set_country_flag = MKN_military_stat_submarine_repair
            set_country_flag = MKN_military_reward_submarine_repair
        }
        if = {
            limit = {
                has_completed_focus = MKN_sweeper_sections
            }
            set_country_flag = MKN_military_stat_sweeper_sections
            set_country_flag = MKN_military_reward_sweeper_sections
        }
        if = {
            limit = {
                has_completed_focus = MKN_tachanka_columns
            }
            set_country_flag = MKN_military_stat_tachanka_columns
            set_country_flag = MKN_military_reward_tachanka_columns
        }
        if = {
            limit = {
                has_completed_focus = MKN_tachanka_tactics
            }
            set_country_flag = MKN_military_stat_tachanka_tactics
            set_country_flag = MKN_military_reward_tachanka_tactics
        }
        if = {
            limit = {
                has_completed_focus = MKN_tactical_recon
            }
            set_country_flag = MKN_military_stat_tactical_recon
            set_country_flag = MKN_military_reward_tactical_recon
        }
        if = {
            limit = {
                has_completed_focus = MKN_tank_crews
            }
            set_country_flag = MKN_military_stat_tank_crews
            set_country_flag = MKN_military_reward_tank_crews
        }
        if = {
            limit = {
                has_completed_focus = MKN_tank_maintenance
            }
            set_country_flag = MKN_military_stat_tank_maintenance
            set_country_flag = MKN_military_reward_tank_maintenance
        }
        if = {
            limit = {
                has_completed_focus = MKN_target_markers
            }
            set_country_flag = MKN_military_stat_target_markers
            set_country_flag = MKN_military_reward_target_markers
        }
        if = {
            limit = {
                has_completed_focus = MKN_torpedo_ambushes
            }
            set_country_flag = MKN_military_stat_torpedo_ambushes
            set_country_flag = MKN_military_reward_torpedo_ambushes
        }
        if = {
            limit = {
                has_completed_focus = MKN_torpedo_artels
            }
            set_country_flag = MKN_military_stat_torpedo_artels
            set_country_flag = MKN_military_reward_torpedo_artels
        }
        if = {
            limit = {
                has_completed_focus = MKN_torpedo_trials
            }
            set_country_flag = MKN_military_stat_torpedo_trials
            set_country_flag = MKN_military_reward_torpedo_trials
        }
        if = {
            limit = {
                has_completed_focus = MKN_village_airfields
            }
            set_country_flag = MKN_military_stat_village_airfields
            set_country_flag = MKN_military_reward_village_airfields
        }
        if = {
            limit = {
                has_completed_focus = MKN_village_muster
            }
            set_country_flag = MKN_military_stat_village_muster
            set_country_flag = MKN_military_reward_village_muster
        }
        set_country_flag = MKN_military_hq_migrated_v5
    }
}
```

### `common/on_actions/nww_mkn_progression.txt`

```pdx
on_actions = {
    on_startup = {
        effect = {
            MKN = {
                if = {
                    limit = {
                        exists = yes
                    }
                    nww_mkn_initialize_bop = yes
                }
                if = {
                    limit = {
                        exists = yes
                        NOT = {
                            has_country_flag = MKN_industry_integration_v4
                        }
                    }
                    nww_mkn_rebuild_industry = yes
                }
                if = {
                    limit = {
                        exists = yes
                        NOT = {
                            has_country_flag = MKN_services_redesign_v5
                        }
                    }
                    nww_mkn_rebuild_services = yes
                }
                MKN_repair_succession_crisis = yes
            }
        }
    }
    on_daily_MKN = {
        effect = {
            nww_mkn_initialize_bop = yes
            if = {
                limit = {
                    NOT = {
                        has_country_flag = MKN_industry_integration_v4
                    }
                }
                nww_mkn_rebuild_industry = yes
            }
            if = {
                limit = {
                    has_country_flag = MKN_moscow_request_pending
                    OR = {
                        NOT = {
                            SOV = {
                                exists = yes
                                has_government = communism
                                is_subject = no
                            }
                        }
                        NOT = {
                            has_government = communism
                        }
                        is_subject = yes
                        is_in_faction = yes
                        has_war_with = SOV
                    }
                }
                clr_country_flag = MKN_moscow_request_pending
            }
            if = {
                limit = {
                    NOT = {
                        has_country_flag = MKN_services_redesign_v5
                    }
                }
                nww_mkn_rebuild_services = yes
            }
            MKN_repair_succession_crisis = yes
        }
    }
}
```

### `common/on_actions/MKN_international_on_actions.txt`

```pdx
on_actions = {
    on_startup = {
        effect = {
            every_country = {
                limit = {
                    original_tag = MKN
                    has_focus_tree = MKN_focus
                }
                MKN_repair_international_content = yes
            }
        }
    }
    on_daily = {
        effect = {
            every_country = {
                limit = {
                    original_tag = MKN
                    has_focus_tree = MKN_focus
                }
                MKN_repair_international_content = yes
            }
        }
    }
}
```

### `common/ideas/MKN_ideas.txt`

```pdx
ideas = {
    country = {
        MKN_decaying_batko = {
            picture = generic_constitutional_guarantees
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                political_power_gain = -0.30
                stability_factor = -0.20
                war_support_factor = -0.15
                army_org_factor = -0.10
                org_loss_when_moving = 0.15
            }
        }
        MKN_steppes_freedom = {
            picture = HABSBURG_cavalry
            allowed = {
                original_tag = MKN
            }
            allowed_civil_war = {
                always = yes
            }
            removal_cost = -1
            modifier = {
                modifier_army_sub_unit_cavalry_speed_factor = 0.15
                supply_consumption_factor = -0.20
                resistance_damage_to_garrison_on_our_occupied_states = 0.25
            }
            equipment_bonus = {
                motorized_equipment = {
                    instant = yes
                    maximum_speed = 0.15
                }
            }
        }
        MKN_cult_of_railways = {
            picture = generic_railroads
            allowed = {
                original_tag = MKN
            }
            allowed_civil_war = {
                always = yes
            }
            removal_cost = -1
            modifier = {
                railway_gun_bombardment_factor = 0.25
                production_speed_rail_way_factor = 0.35
                production_speed_supply_node_factor = 0.35
            }
            equipment_bonus = {
                train_equipment_3 = {
                    instant = yes
                    build_cost_ic = -0.35
                }
                railway_gun_equipment = {
                    instant = yes
                    build_cost_ic = -0.25
                }
            }
        }
        MKN_autonomous_rail_crews_idea = {
            picture = generic_railroads
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                production_speed_rail_way_factor = 0.25
                production_speed_infrastructure_factor = 0.20
            }
            equipment_bonus = {
                train_equipment = {
                    instant = yes
                    build_cost_ic = -0.25
                }
            }
        }
        MKN_soviet_supply_agreement = {
            picture = generic_railroads
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                supply_consumption_factor = -0.10
                army_org_regain = 0.10
            }
        }
        MKN_neighbor_strikes = {
            picture = FRA_factory_strikes
            allowed = {
                always = yes
            }
            removal_cost = -1
            modifier = {
                industrial_capacity_factory = -0.15
                production_speed_buildings_factor = -0.15
                stability_factor = -0.05
            }
        }
        MKN_betrayed_twice = {
            picture = generic_manpower_bonus
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                army_core_defence_factor = 0.30
                army_org_regain = 0.20
                war_support_factor = 0.25
                surrender_limit = 0.15
            }
        }
        MKN_revkom_terror = {
            picture = MKN_revkom
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                stability_factor = -0.35
                consumer_goods_factor = 0.15
                industrial_capacity_factory = -0.25
                political_power_gain = -0.40
            }
        }
        MKN_armored_train_staff_bonus = {
            picture = generic_railroads
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            equipment_bonus = {
                train_equipment_3 = {
                    instant = yes
                    armor_value = 0.20
                    air_attack = 0.20
                }
            }
        }
        MKN_mobile_patrols = {
            picture = generic_army_war_college
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                army_speed_factor = 0.10
                supply_consumption_factor = 0.05
            }
        }
        MKN_seed_cooperatives = {
            picture = generic_industrial_concern_1
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                consumer_goods_factor = -0.05
                production_factory_efficiency_gain_factor = 0.10
            }
        }
        MKN_extra_workshop_shifts = {
            picture = generic_army_war_college
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                industrial_capacity_factory = 0.10
                consumer_goods_factor = 0.05
            }
        }
        MKN_recallable_front_delegates = {
            picture = generic_industrial_concern_1
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                army_morale_factor = 0.10
                political_power_gain = -0.10
            }
        }
    }
    industrial_concern = {
        MKN_free_workshops = {
            picture = MKN_free_workshops
            allowed = {
                original_tag = MKN
            }
            available = {
                has_completed_focus = MKN_free_workshops_focus
            }
            cost = 150
            research_bonus = {
                industry = 0.15
            }
            modifier = {
                production_speed_buildings_factor = 0.10
                production_factory_max_efficiency_factor = 0.05
            }
        }
    }
}
```

### `common/ideas/MKN_international_ideas.txt`

```pdx
ideas = {
    country = {
        MKN_expropriated_funds = {
            picture = generic_industrial_concern_1
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                custom_modifier_tooltip = MKN_expropriated_funds_factories_tt
            }
            on_remove = {
                MKN_clear_expropriation_factories = yes
            }
        }
        MKN_spartacist_engineers = {
            picture = generic_industrial_concern_1
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            on_add = {
                if = {
                    limit = {
                        NOT = {
                            has_country_flag = MKN_spartacist_factory_active
                        }
                    }
                    set_country_flag = MKN_spartacist_factory_active
                    add_offsite_building = {
                        type = arms_factory
                        level = 1
                    }
                }
            }
            on_remove = {
                if = {
                    limit = {
                        has_country_flag = MKN_spartacist_factory_active
                    }
                    add_offsite_building = {
                        type = arms_factory
                        level = -1
                    }
                    clr_country_flag = MKN_spartacist_factory_active
                }
            }
            modifier = {
                custom_modifier_tooltip = MKN_spartacist_factory_tt
            }
        }
        MKN_marusyas_legacy = {
            picture = generic_army_war_college
            allowed = {
                original_tag = MKN
            }
            allowed_civil_war = {
                always = yes
            }
            removal_cost = -1
            on_add = {
                set_technology = {
                    MKN_marusya_assault_training = 1
                }
            }
            on_remove = {
                set_technology = {
                    MKN_marusya_assault_training = 0
                }
            }
            modifier = {
                breakthrough_factor = 0.10
                army_morale_factor = 0.05
                custom_modifier_tooltip = MKN_marusya_urban_attack_tt
            }
        }
    }
}
```

### `history/countries/MKN - Makhnovists.txt`

```pdx
set_oob = MKN_1936
set_research_slots = 3
set_politics = {
    ruling_party = communism
    elections_allowed = no
}
set_popularities = {
    communism = 25
    democratic = 25
    fascism = 25
    neutrality = 25
}
add_ideas = {
    MKN_free_territory
    MKN_decaying_batko
    MKN_steppes_freedom
    MKN_cult_of_railways
}
create_country_leader = {
    name = "Nestor Makhno"
    desc = MKN_NESTOR_MAKHNO_DESC
    picture = GFX_Portrait_makhno
    ideology = anarchist_communism
    traits = {

    }
}
set_technology = {
    infantry_weapons = 1
    tech_support = 1
    tech_recon = 1
    gw_artillery = 1
}
create_country_leader = {
    name = MKN_dmitruk_tratishov
    desc = MKN_fascism_successor_desc
    ideology = fascism_ideology
    traits = {
        mkn_iron_warlord
    }
    picture = GFX_Portrait_MKN_dmitruk_tratishov
}
create_country_leader = {
    name = "Emperor Nestor I"
    desc = MKN_EMPEROR_DESC
    picture = GFX_Portrait_makhno
    ideology = despotism
    traits = {

    }
}
create_country_leader = {
    name = "Vsevolod Volin"
    desc = MKN_VOLIN_DESC
    picture = GFX_Portrait_volin
    ideology = liberalism
    traits = {

    }
}
recruit_character = NWW_MKN_viktor_belash
recruit_character = NWW_MKN_eugen
recruit_character = NWW_MKN_fedir_shchus
recruit_character = NWW_MKN_volin
recruit_character = NWW_MKN_makhno
recruit_character = NWW_MKN_peter_arshinov
recruit_character = NWW_MKN_school_delegate
recruit_character = NWW_MKN_logistics_delegate
recruit_character = NWW_MKN_military_theorist
recruit_character = NWW_MKN_oleksandr_hordiienko
recruit_character = NWW_MKN_andrii_dorosh
recruit_character = NWW_MKN_mykola_kovalenko
recruit_character = NWW_MKN_roman_danylenko
recruit_character = NWW_MKN_olena_hrytsenko
recruit_character = NWW_MKN_dmytro_savchenko
recruit_character = NWW_MKN_yakiv_levchenko
recruit_character = NWW_MKN_petro_stepanenko
recruit_character = NWW_MKN_ivan_bondarenko
recruit_character = NWW_MKN_serhii_melnyk
set_country_flag = MKN_crisis_enabled
recruit_character = MKN_advisor_weapons_broker
recruit_character = MKN_advisor_recruiting_commissar
recruit_character = MKN_advisor_military_orator
recruit_character = MKN_advisor_frontline_delegate
recruit_character = MKN_advisor_arsenal_coordinator
recruit_character = MKN_advisor_veterans_organizer
recruit_character = MKN_advisor_education_delegate
recruit_character = MKN_advisor_commune_secretary
recruit_character = MKN_advisor_anti_statist_theorist
recruit_character = MKN_advisor_cooperative_treasurer
recruit_character = MKN_advisor_literacy_organizer
recruit_character = MKN_advisor_free_press_editor
recruit_character = MKN_advisor_grain_distributor
recruit_character = MKN_advisor_rural_defender
recruit_character = MKN_advisor_militia_delegate
recruit_character = MKN_advisor_agronomist
recruit_character = MKN_advisor_village_mediator
recruit_character = MKN_advisor_market_keeper
recruit_character = MKN_advisor_industrial_organizer
recruit_character = MKN_advisor_rail_dispatcher
recruit_character = MKN_advisor_union_secretary
recruit_character = MKN_advisor_workshop_engineer
recruit_character = MKN_advisor_labor_delegate
recruit_character = MKN_advisor_syndicalist_theorist
capital = 1082
set_cosmetic_tag = MKN_batko
MKN_repair_personnel = yes
```

### `history/units/MKN_1936.txt`

```pdx
division_template = {
    name = "Повстанческая дивизия"
    division_names_group = MKN_INF_01
    regiments = {
        infantry = {
            x = 0
            y = 0
        }
        infantry = {
            x = 0
            y = 1
        }
        infantry = {
            x = 0
            y = 2
        }
    }
}
division_template = {
    name = "Конный отряд"
    division_names_group = MKN_CAV_01
    regiments = {
        cavalry = {
            x = 0
            y = 0
        }
        cavalry = {
            x = 0
            y = 1
        }
        cavalry = {
            x = 0
            y = 2
        }
    }
}
units = {
    division = {
        name = "1. Povstancheskaya Rota"
        location = 429
        division_template = "Повстанческая дивизия"
        start_experience_factor = 0.2
        start_equipment_factor = 0.45
    }
    division = {
        name = "2. Povstancheskaya Rota"
        location = 429
        division_template = "Повстанческая дивизия"
        start_experience_factor = 0.2
        start_equipment_factor = 0.45
    }
    division = {
        name = "3. Povstancheskaya Rota"
        location = 429
        division_template = "Повстанческая дивизия"
        start_experience_factor = 0.2
        start_equipment_factor = 0.45
    }
    division = {
        name = "1. Konny Otryad"
        location = 429
        division_template = "Конный отряд"
        start_experience_factor = 0.2
        start_equipment_factor = 0.35
    }
    division = {
        name = "2. Konny Otryad"
        location = 429
        division_template = "Конный отряд"
        start_experience_factor = 0.2
        start_equipment_factor = 0.35
    }
    division = {
        name = "3. Konny Otryad"
        location = 429
        division_template = "Конный отряд"
        start_experience_factor = 0.2
        start_equipment_factor = 0.35
    }
}
instant_effect = {
    add_equipment_production = {
        equipment = {
            type = infantry_equipment_0
            creator = MKN
        }
        requested_factories = 1
        progress = 0.2
        efficiency = 80
    }
}
```

### `history/units/MKN_black_guard.txt`

```pdx
division_template = {
    name = "Штурмовой отряд Маруси"
    is_locked = yes
    force_allow_recruiting = no
    division_cap = 2
    priority = 2
    regiments = {
        infantry = {
            x = 0
            y = 0
        }
        infantry = {
            x = 0
            y = 1
        }
        infantry = {
            x = 0
            y = 2
        }
        infantry = {
            x = 1
            y = 0
        }
        infantry = {
            x = 1
            y = 1
        }
        infantry = {
            x = 1
            y = 2
        }
        infantry = {
            x = 2
            y = 0
        }
        infantry = {
            x = 2
            y = 1
        }
        infantry = {
            x = 2
            y = 2
        }
        artillery_brigade = {
            x = 3
            y = 0
        }
        artillery_brigade = {
            x = 3
            y = 1
        }
    }
    support = {
        engineer = {
            x = 0
            y = 0
        }
        recon = {
            x = 0
            y = 1
        }
        field_hospital = {
            x = 0
            y = 2
        }
    }
}
units = {
    division = {
        name = "1-й штурмовой отряд Маруси"
        location = 429
        division_template = "Штурмовой отряд Маруси"
        start_experience_factor = 1.0
        start_equipment_factor = 1.0
    }
    division = {
        name = "2-й штурмовой отряд Маруси"
        location = 429
        division_template = "Штурмовой отряд Маруси"
        start_experience_factor = 1.0
        start_equipment_factor = 1.0
    }
}
```

### `history/units/MKN_black_guard_oob.txt`

```pdx
instant_effect = {
    load_oob = MKN_black_guard
}
```

### `common/technologies/MKN_technologies.txt`

```pdx
technologies = {
    MKN_marusya_assault_training = {
        research_cost = 1
        allow = {
            always = no
        }
        enable_equipments = {

        }
        amphibious_armor = {
            urban = {
                attack = 0.15
            }
        }
        amphibious_heavy_armor = {
            urban = {
                attack = 0.15
            }
        }
        amphibious_light_armor = {
            urban = {
                attack = 0.15
            }
        }
        amphibious_mechanized = {
            urban = {
                attack = 0.15
            }
        }
        amphibious_medium_armor = {
            urban = {
                attack = 0.15
            }
        }
        anti_air_brigade = {
            urban = {
                attack = 0.15
            }
        }
        anti_tank_brigade = {
            urban = {
                attack = 0.15
            }
        }
        armored_car = {
            urban = {
                attack = 0.15
            }
        }
        artillery_brigade = {
            urban = {
                attack = 0.15
            }
        }
        bicycle_battalion = {
            urban = {
                attack = 0.15
            }
        }
        camelry = {
            urban = {
                attack = 0.15
            }
        }
        cavalry = {
            urban = {
                attack = 0.15
            }
        }
        fake_intel_unit = {
            urban = {
                attack = 0.15
            }
        }
        heavy_armor = {
            urban = {
                attack = 0.15
            }
        }
        heavy_sp_anti_air_brigade = {
            urban = {
                attack = 0.15
            }
        }
        heavy_sp_artillery_brigade = {
            urban = {
                attack = 0.15
            }
        }
        heavy_tank_destroyer_brigade = {
            urban = {
                attack = 0.15
            }
        }
        hq_armored_car = {
            urban = {
                attack = 0.15
            }
        }
        hq_heavy_armor = {
            urban = {
                attack = 0.15
            }
        }
        hq_infantry = {
            urban = {
                attack = 0.15
            }
        }
        hq_light_armor = {
            urban = {
                attack = 0.15
            }
        }
        hq_medium_armor = {
            urban = {
                attack = 0.15
            }
        }
        hq_motorized = {
            urban = {
                attack = 0.15
            }
        }
        hq_paratrooper = {
            urban = {
                attack = 0.15
            }
        }
        infantry = {
            urban = {
                attack = 0.15
            }
        }
        irregular_infantry = {
            urban = {
                attack = 0.15
            }
        }
        light_armor = {
            urban = {
                attack = 0.15
            }
        }
        light_sp_anti_air_brigade = {
            urban = {
                attack = 0.15
            }
        }
        light_sp_artillery_brigade = {
            urban = {
                attack = 0.15
            }
        }
        light_tank_destroyer_brigade = {
            urban = {
                attack = 0.15
            }
        }
        marine = {
            urban = {
                attack = 0.15
            }
        }
        marine_commando = {
            urban = {
                attack = 0.15
            }
        }
        mechanized = {
            urban = {
                attack = 0.15
            }
        }
        medium_armor = {
            urban = {
                attack = 0.15
            }
        }
        medium_sp_anti_air_brigade = {
            urban = {
                attack = 0.15
            }
        }
        medium_sp_artillery_brigade = {
            urban = {
                attack = 0.15
            }
        }
        medium_tank_destroyer_brigade = {
            urban = {
                attack = 0.15
            }
        }
        militia = {
            urban = {
                attack = 0.15
            }
        }
        modern_armor = {
            urban = {
                attack = 0.15
            }
        }
        modern_sp_anti_air_brigade = {
            urban = {
                attack = 0.15
            }
        }
        modern_sp_artillery_brigade = {
            urban = {
                attack = 0.15
            }
        }
        modern_tank_destroyer_brigade = {
            urban = {
                attack = 0.15
            }
        }
        mot_anti_air_brigade = {
            urban = {
                attack = 0.15
            }
        }
        mot_anti_tank_brigade = {
            urban = {
                attack = 0.15
            }
        }
        mot_artillery_brigade = {
            urban = {
                attack = 0.15
            }
        }
        mot_rocket_artillery_brigade = {
            urban = {
                attack = 0.15
            }
        }
        motorized = {
            urban = {
                attack = 0.15
            }
        }
        motorized_rocket_brigade = {
            urban = {
                attack = 0.15
            }
        }
        mountaineers = {
            urban = {
                attack = 0.15
            }
        }
        paratrooper = {
            urban = {
                attack = 0.15
            }
        }
        penal_battalion = {
            urban = {
                attack = 0.15
            }
        }
        ranger_battalion = {
            urban = {
                attack = 0.15
            }
        }
        rocket_artillery_brigade = {
            urban = {
                attack = 0.15
            }
        }
    }
}
```

## Предприятия, MIO, советники и характеристики

### `common/military_industrial_organization/organizations/MKN_organizations.txt`

```pdx
MKN_free_workshops = {
    include = generic_infantry_equipment_organization
    icon = GFX_idea_MKN_free_workshops
    allowed = {
        original_tag = MKN
        has_dlc = "Arms Against Tyranny"
    }
    available = {
        FROM = {
            has_completed_focus = MKN_free_workshops_focus
        }
    }
    initial_trait = {
        name = MKN_free_workshops_initial_trait
        organization_modifier = {
            military_industrial_organization_research_bonus = 0.15
        }
        production_bonus = {
            production_efficiency_cap_factor = 0.05
        }
    }
}
MKN_zaporizhstal_organization = {
    include = generic_artillery_organization
    icon = GFX_idea_generic_industrial_concern_1
    allowed = {
        original_tag = MKN
        has_dlc = "Arms Against Tyranny"
    }
    available = {
        FROM = {
            has_completed_focus = MKN_zaporizhstal
        }
    }
    initial_trait = {
        name = MKN_zaporizhstal_organization_initial
        equipment_bonus = {
            reliability = 0.05
        }
        production_bonus = {
            production_capacity_factor = 0.05
        }
    }
    add_trait = {
        token = MKN_zaporizhstal_serial_forging
        name = MKN_zaporizhstal_serial_forging
        icon = GFX_generic_mio_trait_icon_production_capacity
        special_trait_background = yes
        position = {
            x = 13
            y = 0
        }
        available = {
            FROM = {
                has_completed_focus = MKN_production_cycles
            }
        }
        production_bonus = {
            production_efficiency_cap_factor = 0.05
        }
    }
}
```

### `common/military_industrial_organization/organizations/nww_organizations.txt`

```pdx
MKN_kommunar_organization = {
    include = generic_mobile_tank_organization
    icon = GFX_idea_MKN_company_kommunar
    allowed = {
        original_tag = MKN
        has_dlc = "Arms Against Tyranny"
    }
    available = {
        FROM = {
            OR = {
                has_completed_focus = MKN_motorized_vanguard
                hidden_trigger = {
                    has_country_flag = MKN_military_stat_steel_horses
                }
            }
        }
    }
    initial_trait = {
        name = MKN_kommunar_organization_initial
        equipment_bonus = {
            maximum_speed = 0.05
            reliability = 0.04
        }
    }
    add_trait = {
        token = MKN_kommunar_organization_specialization_a
        name = MKN_kommunar_organization_specialization_a
        icon = GFX_generic_mio_trait_icon_production_capacity
        special_trait_background = yes
        position = {
            x = 13
            y = 0
        }
        mutually_exclusive = {
            MKN_kommunar_organization_specialization_b
        }
        available = {
            FROM = {
                OR = {
                    has_completed_focus = MKN_armored_trains_and_repair_focus
                    hidden_trigger = {
                        has_country_flag = MKN_military_stat_tank_maintenance
                    }
                }
            }
        }
        equipment_bonus = {
            maximum_speed = 0.08
            armor_value = -0.03
        }
    }
    add_trait = {
        token = MKN_kommunar_organization_specialization_b
        name = MKN_kommunar_organization_specialization_b
        icon = GFX_generic_mio_trait_icon_production_capacity
        special_trait_background = yes
        position = {
            x = 15
            y = 0
        }
        mutually_exclusive = {
            MKN_kommunar_organization_specialization_a
        }
        available = {
            FROM = {
                OR = {
                    has_completed_focus = MKN_armored_trains_and_repair_focus
                    hidden_trigger = {
                        has_country_flag = MKN_military_stat_tank_maintenance
                    }
                }
            }
        }
        equipment_bonus = {
            armor_value = 0.08
            maximum_speed = -0.03
        }
    }
    add_trait = {
        token = MKN_kommunar_organization_mature
        name = MKN_kommunar_organization_mature
        icon = GFX_generic_mio_trait_icon_production_capacity
        special_trait_background = yes
        position = {
            x = 14
            y = 2
        }
        parent = {
            traits = {
                MKN_kommunar_organization_specialization_a
                MKN_kommunar_organization_specialization_b
            }
            num_parents_needed = 1
        }
        available = {
            FROM = {
                has_completed_focus = MKN_mechanized_compact
            }
        }
        equipment_bonus = {
            reliability = 0.04
        }
        production_bonus = {
            production_capacity_factor = 0.05
            production_cost_factor = -0.03
        }
    }
}
MKN_rifle_artels_organization = {
    include = generic_infantry_equipment_organization
    icon = GFX_idea_MKN_company_rifle_artels
    allowed = {
        original_tag = MKN
        has_dlc = "Arms Against Tyranny"
    }
    available = {
        FROM = {
            OR = {
                OR = {
                    has_completed_focus = MKN_steppe_horde
                    hidden_trigger = {
                        has_country_flag = MKN_military_stat_village_muster
                    }
                }
                has_completed_focus = MKN_rifle_concern
            }
        }
    }
    initial_trait = {
        name = MKN_rifle_artels_organization_initial
        equipment_bonus = {
            reliability = 0.06
            soft_attack = 0.02
        }
    }
    add_trait = {
        token = MKN_rifle_artels_organization_specialization_a
        name = MKN_rifle_artels_organization_specialization_a
        icon = GFX_generic_mio_trait_icon_production_capacity
        special_trait_background = yes
        position = {
            x = 13
            y = 0
        }
        mutually_exclusive = {
            MKN_rifle_artels_organization_specialization_b
        }
        available = {
            FROM = {
                OR = {
                    OR = {
                        has_completed_focus = MKN_steppe_horde
                        hidden_trigger = {
                            has_country_flag = MKN_military_stat_machinegun_carts
                        }
                    }
                    has_completed_focus = MKN_workshop_standards
                }
            }
        }
        equipment_bonus = {
            build_cost_ic = -0.08
            soft_attack = -0.02
        }
    }
    add_trait = {
        token = MKN_rifle_artels_organization_specialization_b
        name = MKN_rifle_artels_organization_specialization_b
        icon = GFX_generic_mio_trait_icon_production_capacity
        special_trait_background = yes
        position = {
            x = 15
            y = 0
        }
        mutually_exclusive = {
            MKN_rifle_artels_organization_specialization_a
        }
        available = {
            FROM = {
                OR = {
                    OR = {
                        has_completed_focus = MKN_steppe_horde
                        hidden_trigger = {
                            has_country_flag = MKN_military_stat_machinegun_carts
                        }
                    }
                    has_completed_focus = MKN_workshop_standards
                }
            }
        }
        equipment_bonus = {
            soft_attack = 0.08
            build_cost_ic = 0.03
        }
    }
    add_trait = {
        token = MKN_rifle_artels_organization_mature
        name = MKN_rifle_artels_organization_mature
        icon = GFX_generic_mio_trait_icon_production_capacity
        special_trait_background = yes
        position = {
            x = 14
            y = 2
        }
        parent = {
            traits = {
                MKN_rifle_artels_organization_specialization_a
                MKN_rifle_artels_organization_specialization_b
            }
            num_parents_needed = 1
        }
        available = {
            FROM = {
                OR = {
                    has_completed_focus = MKN_free_army_compact
                    has_completed_focus = MKN_communal_compact
                }
            }
        }
        equipment_bonus = {
            reliability = 0.04
        }
        production_bonus = {
            production_capacity_factor = 0.05
            production_cost_factor = -0.03
        }
    }
}
MKN_artillery_works_organization = {
    include = generic_artillery_organization
    icon = GFX_idea_MKN_company_artillery_works
    allowed = {
        original_tag = MKN
        has_dlc = "Arms Against Tyranny"
    }
    available = {
        FROM = {
            OR = {
                OR = {
                    has_completed_focus = MKN_communal_fire_support_focus
                    hidden_trigger = {
                        has_country_flag = MKN_military_stat_artillery_artels
                    }
                }
                OR = {
                    has_completed_focus = MKN_steppe_horde
                    hidden_trigger = {
                        has_country_flag = MKN_military_stat_machinegun_carts
                    }
                }
            }
        }
    }
    initial_trait = {
        name = MKN_artillery_works_organization_initial
        equipment_bonus = {
            reliability = 0.05
            soft_attack = 0.03
        }
    }
    add_trait = {
        token = MKN_artillery_works_organization_specialization_a
        name = MKN_artillery_works_organization_specialization_a
        icon = GFX_generic_mio_trait_icon_production_capacity
        special_trait_background = yes
        position = {
            x = 13
            y = 0
        }
        mutually_exclusive = {
            MKN_artillery_works_organization_specialization_b
        }
        available = {
            FROM = {
                OR = {
                    has_completed_focus = MKN_communal_fire_support_focus
                    hidden_trigger = {
                        has_country_flag = MKN_military_stat_fire_tables
                    }
                }
            }
        }
        equipment_bonus = {
            build_cost_ic = -0.06
            reliability = 0.05
        }
    }
    add_trait = {
        token = MKN_artillery_works_organization_specialization_b
        name = MKN_artillery_works_organization_specialization_b
        icon = GFX_generic_mio_trait_icon_production_capacity
        special_trait_background = yes
        position = {
            x = 15
            y = 0
        }
        mutually_exclusive = {
            MKN_artillery_works_organization_specialization_a
        }
        available = {
            FROM = {
                OR = {
                    has_completed_focus = MKN_communal_fire_support_focus
                    hidden_trigger = {
                        has_country_flag = MKN_military_stat_fire_tables
                    }
                }
            }
        }
        equipment_bonus = {
            soft_attack = 0.08
            build_cost_ic = 0.03
        }
    }
    add_trait = {
        token = MKN_artillery_works_organization_mature
        name = MKN_artillery_works_organization_mature
        icon = GFX_generic_mio_trait_icon_production_capacity
        special_trait_background = yes
        position = {
            x = 14
            y = 2
        }
        parent = {
            traits = {
                MKN_artillery_works_organization_specialization_a
                MKN_artillery_works_organization_specialization_b
            }
            num_parents_needed = 1
        }
        available = {
            FROM = {
                has_completed_focus = MKN_mechanized_compact
            }
        }
        equipment_bonus = {
            reliability = 0.04
        }
        production_bonus = {
            production_capacity_factor = 0.05
            production_cost_factor = -0.03
        }
    }
}
MKN_air_artels_organization = {
    include = generic_light_aircraft_organization
    icon = GFX_idea_MKN_company_air_artels
    allowed = {
        original_tag = MKN
        has_dlc = "Arms Against Tyranny"
    }
    available = {
        FROM = {
            OR = {
                has_completed_focus = MKN_interceptor_cooperatives
                hidden_trigger = {
                    has_country_flag = MKN_military_stat_aircraft_artels
                }
            }
        }
    }
    initial_trait = {
        name = MKN_air_artels_organization_initial
        equipment_bonus = {
            air_agility = 0.05
            maximum_speed = 0.03
        }
    }
    add_trait = {
        token = MKN_air_artels_organization_specialization_a
        name = MKN_air_artels_organization_specialization_a
        icon = GFX_generic_mio_trait_icon_production_capacity
        special_trait_background = yes
        position = {
            x = 13
            y = 0
        }
        mutually_exclusive = {
            MKN_air_artels_organization_specialization_b
        }
        available = {
            FROM = {
                OR = {
                    has_completed_focus = MKN_interceptor_cooperatives
                    hidden_trigger = {
                        has_country_flag = MKN_military_stat_interceptor_pairs
                    }
                }
            }
        }
        equipment_bonus = {
            air_agility = 0.08
            air_range = -0.03
        }
    }
    add_trait = {
        token = MKN_air_artels_organization_specialization_b
        name = MKN_air_artels_organization_specialization_b
        icon = GFX_generic_mio_trait_icon_production_capacity
        special_trait_background = yes
        position = {
            x = 15
            y = 0
        }
        mutually_exclusive = {
            MKN_air_artels_organization_specialization_a
        }
        available = {
            FROM = {
                OR = {
                    has_completed_focus = MKN_interceptor_cooperatives
                    hidden_trigger = {
                        has_country_flag = MKN_military_stat_interceptor_pairs
                    }
                }
            }
        }
        equipment_bonus = {
            maximum_speed = 0.08
            air_agility = -0.03
        }
    }
    add_trait = {
        token = MKN_air_artels_organization_mature
        name = MKN_air_artels_organization_mature
        icon = GFX_generic_mio_trait_icon_production_capacity
        special_trait_background = yes
        position = {
            x = 14
            y = 2
        }
        parent = {
            traits = {
                MKN_air_artels_organization_specialization_a
                MKN_air_artels_organization_specialization_b
            }
            num_parents_needed = 1
        }
        available = {
            FROM = {
                has_completed_focus = MKN_free_sky_compact
            }
        }
        equipment_bonus = {
            reliability = 0.04
        }
        production_bonus = {
            production_capacity_factor = 0.05
            production_cost_factor = -0.03
        }
    }
}
MKN_attack_air_artels_organization = {
    include = generic_cas_aircraft_organization
    icon = GFX_idea_MKN_company_attack_air_artels
    allowed = {
        original_tag = MKN
        has_dlc = "Arms Against Tyranny"
    }
    available = {
        FROM = {
            OR = {
                has_completed_focus = MKN_flying_artillery_focus
                hidden_trigger = {
                    has_country_flag = MKN_military_stat_attack_air_artels
                }
            }
        }
    }
    initial_trait = {
        name = MKN_attack_air_artels_organization_initial
        equipment_bonus = {
            air_ground_attack = 0.05
            reliability = 0.04
        }
    }
    add_trait = {
        token = MKN_attack_air_artels_organization_specialization_a
        name = MKN_attack_air_artels_organization_specialization_a
        icon = GFX_generic_mio_trait_icon_production_capacity
        special_trait_background = yes
        position = {
            x = 13
            y = 0
        }
        mutually_exclusive = {
            MKN_attack_air_artels_organization_specialization_b
        }
        available = {
            FROM = {
                OR = {
                    has_completed_focus = MKN_flying_artillery_focus
                    hidden_trigger = {
                        has_country_flag = MKN_military_stat_flying_artillery
                    }
                }
            }
        }
        equipment_bonus = {
            air_defence = 0.08
            maximum_speed = -0.03
        }
    }
    add_trait = {
        token = MKN_attack_air_artels_organization_specialization_b
        name = MKN_attack_air_artels_organization_specialization_b
        icon = GFX_generic_mio_trait_icon_production_capacity
        special_trait_background = yes
        position = {
            x = 15
            y = 0
        }
        mutually_exclusive = {
            MKN_attack_air_artels_organization_specialization_a
        }
        available = {
            FROM = {
                OR = {
                    has_completed_focus = MKN_flying_artillery_focus
                    hidden_trigger = {
                        has_country_flag = MKN_military_stat_flying_artillery
                    }
                }
            }
        }
        equipment_bonus = {
            air_range = 0.10
            air_defence = -0.03
        }
    }
    add_trait = {
        token = MKN_attack_air_artels_organization_mature
        name = MKN_attack_air_artels_organization_mature
        icon = GFX_generic_mio_trait_icon_production_capacity
        special_trait_background = yes
        position = {
            x = 14
            y = 2
        }
        parent = {
            traits = {
                MKN_attack_air_artels_organization_specialization_a
                MKN_attack_air_artels_organization_specialization_b
            }
            num_parents_needed = 1
        }
        available = {
            FROM = {
                has_completed_focus = MKN_air_support_compact
            }
        }
        equipment_bonus = {
            reliability = 0.04
        }
        production_bonus = {
            production_capacity_factor = 0.05
            production_cost_factor = -0.03
        }
    }
}
MKN_kherson_works_organization = {
    include = generic_escort_ship_organization
    icon = GFX_idea_MKN_company_kherson_works
    allowed = {
        original_tag = MKN
        has_dlc = "Arms Against Tyranny"
    }
    available = {
        FROM = {
            OR = {
                has_completed_focus = MKN_black_sea_flotilla_and_yards
                hidden_trigger = {
                    has_country_flag = MKN_military_stat_kherson_shipyard
                }
            }
        }
    }
    initial_trait = {
        name = MKN_kherson_works_organization_initial
        equipment_bonus = {
            sub_detection = 0.05
            naval_speed = 0.03
        }
    }
    add_trait = {
        token = MKN_kherson_works_organization_specialization_a
        name = MKN_kherson_works_organization_specialization_a
        icon = GFX_generic_mio_trait_icon_production_capacity
        special_trait_background = yes
        position = {
            x = 13
            y = 0
        }
        mutually_exclusive = {
            MKN_kherson_works_organization_specialization_b
        }
        available = {
            FROM = {
                OR = {
                    has_completed_focus = MKN_sea_escort_service
                    hidden_trigger = {
                        has_country_flag = MKN_military_stat_depth_charge_school
                    }
                }
            }
        }
        equipment_bonus = {
            sub_detection = 0.10
            naval_speed = -0.02
        }
    }
    add_trait = {
        token = MKN_kherson_works_organization_specialization_b
        name = MKN_kherson_works_organization_specialization_b
        icon = GFX_generic_mio_trait_icon_production_capacity
        special_trait_background = yes
        position = {
            x = 15
            y = 0
        }
        mutually_exclusive = {
            MKN_kherson_works_organization_specialization_a
        }
        available = {
            FROM = {
                OR = {
                    has_completed_focus = MKN_sea_escort_service
                    hidden_trigger = {
                        has_country_flag = MKN_military_stat_depth_charge_school
                    }
                }
            }
        }
        equipment_bonus = {
            naval_speed = 0.08
            sub_detection = -0.03
        }
    }
    add_trait = {
        token = MKN_kherson_works_organization_mature
        name = MKN_kherson_works_organization_mature
        icon = GFX_generic_mio_trait_icon_production_capacity
        special_trait_background = yes
        position = {
            x = 14
            y = 2
        }
        parent = {
            traits = {
                MKN_kherson_works_organization_specialization_a
                MKN_kherson_works_organization_specialization_b
            }
            num_parents_needed = 1
        }
        available = {
            FROM = {
                has_completed_focus = MKN_escort_compact
            }
        }
        equipment_bonus = {
            reliability = 0.04
        }
        production_bonus = {
            production_capacity_factor = 0.05
            production_cost_factor = -0.03
        }
    }
}
MKN_submarine_works_organization = {
    include = generic_submarine_organization
    icon = GFX_idea_MKN_company_submarine_works
    allowed = {
        original_tag = MKN
        has_dlc = "Arms Against Tyranny"
    }
    available = {
        FROM = {
            OR = {
                has_completed_focus = MKN_torpedo_artels_focus
                hidden_trigger = {
                    has_country_flag = MKN_military_stat_submarine_crews
                }
            }
        }
    }
    initial_trait = {
        name = MKN_submarine_works_organization_initial
        equipment_bonus = {
            sub_visibility = -0.05
            reliability = 0.04
        }
    }
    add_trait = {
        token = MKN_submarine_works_organization_specialization_a
        name = MKN_submarine_works_organization_specialization_a
        icon = GFX_generic_mio_trait_icon_production_capacity
        special_trait_background = yes
        position = {
            x = 13
            y = 0
        }
        mutually_exclusive = {
            MKN_submarine_works_organization_specialization_b
        }
        available = {
            FROM = {
                OR = {
                    has_completed_focus = MKN_hidden_smuggler_bases_focus
                    hidden_trigger = {
                        has_country_flag = MKN_military_stat_night_sorties
                    }
                }
            }
        }
        equipment_bonus = {
            sub_visibility = -0.10
            naval_range = -0.04
        }
    }
    add_trait = {
        token = MKN_submarine_works_organization_specialization_b
        name = MKN_submarine_works_organization_specialization_b
        icon = GFX_generic_mio_trait_icon_production_capacity
        special_trait_background = yes
        position = {
            x = 15
            y = 0
        }
        mutually_exclusive = {
            MKN_submarine_works_organization_specialization_a
        }
        available = {
            FROM = {
                OR = {
                    has_completed_focus = MKN_hidden_smuggler_bases_focus
                    hidden_trigger = {
                        has_country_flag = MKN_military_stat_night_sorties
                    }
                }
            }
        }
        equipment_bonus = {
            naval_range = 0.10
            sub_visibility = 0.03
        }
    }
    add_trait = {
        token = MKN_submarine_works_organization_mature
        name = MKN_submarine_works_organization_mature
        icon = GFX_generic_mio_trait_icon_production_capacity
        special_trait_background = yes
        position = {
            x = 14
            y = 2
        }
        parent = {
            traits = {
                MKN_submarine_works_organization_specialization_a
                MKN_submarine_works_organization_specialization_b
            }
            num_parents_needed = 1
        }
        available = {
            FROM = {
                has_completed_focus = MKN_raider_compact
            }
        }
        equipment_bonus = {
            reliability = 0.04
        }
        production_bonus = {
            production_capacity_factor = 0.05
            production_cost_factor = -0.03
        }
    }
}
```

### `common/ideas/MKN_economic_ideas.txt`

```pdx
ideas = {
    country = {
        MKN_congress_elected_commanders = {
            picture = generic_army_war_college
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                army_org_factor = 0.05
            }
        }
        MKN_congress_mutual_insurance = {
            picture = generic_industrial_concern_1
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                repair_speed_factor = 0.10
            }
        }
    }
}
```

### `common/ideas/MKN_eugen_ideas.txt`

```pdx
ideas = {
    country = {
        MKN_eugen_no_one_left_behind = {
            picture = generic_infantry_bonus
            allowed = {
                original_tag = MKN
            }
            allowed_civil_war = {
                always = no
            }
            removal_cost = -1
            modifier = {
                army_morale_factor = 0.10
            }
        }
        MKN_eugen_instructor_courses = {
            picture = generic_army_war_college
            allowed = {
                original_tag = MKN
            }
            allowed_civil_war = {
                always = no
            }
            removal_cost = -1
            modifier = {
                army_infantry_defence_factor = 0.05
                army_morale_factor = 0.05
            }
        }
    }
}
```

### `common/ideas/MKN_ukr_border_ideas.txt`

```pdx
ideas = {
    country = {
        MKN_border_fury_buff = {
            picture = generic_manpower_bonus
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                army_attack_factor = 0.15
                army_speed_factor = 0.10
                breakthrough_factor = 0.15
            }
        }
        MKN_border_relaxation_debuff = {
            picture = generic_constitutional_guarantees
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                army_attack_factor = -0.10
                army_org_regain = -0.15
                stability_factor = 0.05
            }
        }
        MKN_war_for_the_steppe = {
            picture = generic_manpower_bonus
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                army_core_attack_factor = 0.10
            }
        }
    }
}
```

### `common/ideas/nww_MKN_ideas.txt`

```pdx
ideas = {
    country = {
        MKN_free_territory = {
            picture = gre_agricultural_communes
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                conscription = 0.02
                supply_consumption_factor = -0.05
                army_attack_factor = 0.05
            }
        }
        MKN_free_soviets_idea = {
            picture = generic_constitutional_guarantees
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                conscription = 0.02
                supply_consumption_factor = -0.05
                stability_factor = 0.03
                political_power_gain = 0.05
            }
        }
        MKN_tachanka_warfare = {
            picture = HABSBURG_cavalry
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                army_attack_factor = 0.1
            }
        }
        MKN_railway_guards = {
            picture = ARG_invest_in_railways
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                industrial_capacity_factory = 0.05
                research_speed_factor = 0.05
            }
        }
        MKN_dneprostroi_power = {
            picture = por_hydroelectric_power
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                production_speed_buildings_factor = 0.05
                factory_energy_consumption = -0.10
            }
        }
        MKN_electrified_steppe = {
            picture = ETH_ethiopian_electric_power
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                research_speed_factor = 0.05
                industrial_capacity_factory = 0.05
            }
        }
        MKN_steel_horses_idea = {
            picture = generic_acquire_tanks
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                army_armor_attack_factor = 0.05
                army_armor_defence_factor = 0.1
                army_armor_speed_factor = 0.05
            }
        }
        MKN_batko_cavalry_idea = {
            picture = HABSBURG_cavalry
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                modifier_army_sub_unit_cavalry_attack_factor = 0.1
                modifier_army_sub_unit_cavalry_speed_factor = 0.1
                modifier_army_sub_unit_cavalry_defence_factor = 0.05
                conscription = 0.02
            }
        }
        MKN_black_guard_veterans_idea = {
            picture = YUG_local_militias
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                max_planning = 0.1
                org_loss_when_moving = -0.05
            }
        }
        MKN_steppe_quartermasters_idea = {
            picture = generic_supply_depot
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                supply_consumption_factor = -0.1
            }
        }
        MKN_free_airmen = {
            picture = generic_air_bonus
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                air_agility_factor = 0.05
                air_accidents_factor = -0.05
            }
        }
        MKN_black_swarm_idea = {
            picture = air_support_focus
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                air_agility_factor = 0.1
                air_maximum_speed_factor = 0.1
                air_accidents_factor = -0.05
            }
        }
        MKN_free_mint_idea = {
            picture = generic_supply_depot
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                political_power_gain = 0.2
            }
        }
        MKN_anarchic_economy_idea = {
            picture = CHL_near_anarchic_society
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                political_power_gain = -0.25
                consumer_goods_factor = 0.15
                production_speed_buildings_factor = -0.15
            }
        }
        MKN_smuggling_network = {
            picture = COG_transports_et_ports
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                consumer_goods_factor = -0.05
            }
        }
        MKN_communal_federation = {
            picture = generic_constitutional_guarantees
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                stability_factor = 0.05
                production_speed_buildings_factor = 0.05
            }
        }
        MKN_federal_republic = {
            picture = generic_constitutional_guarantees
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                stability_factor = 0.10
                political_power_gain = 0.10
            }
        }
        MKN_planned_economy = {
            picture = generic_constitutional_guarantees
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                industrial_capacity_factory = 0.08
                consumer_goods_factor = -0.03
            }
        }
        MKN_military_directory = {
            picture = generic_constitutional_guarantees
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                war_support_factor = 0.10
                army_org_factor = 0.05
            }
        }
        MKN_imperial_administration = {
            picture = generic_constitutional_guarantees
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                stability_factor = 0.10
                political_power_gain = 0.15
            }
        }
        MKN_economic_coordination = {
            picture = CHL_near_anarchic_society
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                political_power_gain = -0.15
                consumer_goods_factor = 0.10
                production_speed_buildings_factor = -0.10
            }
        }
        MKN_economic_recovery = {
            picture = CHL_near_anarchic_society
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                political_power_gain = -0.05
                consumer_goods_factor = 0.05
                production_speed_buildings_factor = -0.05
            }
        }
        MKN_fragmented_workshops = {
            picture = generic_industrial_concern_1
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                industrial_capacity_factory = -0.15
                production_factory_efficiency_gain_factor = -0.20
                research_speed_factor = -0.05
            }
        }
        MKN_catalogued_workshops = {
            picture = generic_industrial_concern_1
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                industrial_capacity_factory = -0.10
                production_factory_efficiency_gain_factor = -0.12
                research_speed_factor = -0.03
            }
        }
        MKN_standardized_workshops = {
            picture = generic_industrial_concern_2
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                industrial_capacity_factory = -0.05
                production_factory_efficiency_gain_factor = -0.05
                research_speed_factor = -0.01
            }
        }
        MKN_broken_supply = {
            picture = generic_supply_depot
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                supply_consumption_factor = 0.20
                army_org_regain = -0.15
            }
        }
        MKN_mapped_supply = {
            picture = generic_supply_depot
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                supply_consumption_factor = 0.12
                army_org_regain = -0.10
            }
        }
        MKN_coordinated_supply = {
            picture = generic_supply_depot
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                supply_consumption_factor = 0.05
                army_org_regain = -0.04
            }
        }
        MKN_untrained_militias = {
            picture = YUG_local_militias
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                army_org_factor = -0.15
                training_time_army_factor = 0.20
                max_planning = -0.10
            }
        }
        MKN_accountable_militias = {
            picture = YUG_local_militias
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                army_org_factor = -0.10
                training_time_army_factor = 0.12
                max_planning = -0.06
            }
        }
        MKN_drilled_militias = {
            picture = YUG_local_militias
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                army_org_factor = -0.04
                training_time_army_factor = 0.05
                max_planning = -0.03
            }
        }
        MKN_dnieper_economy = {
            picture = generic_constitutional_guarantees
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                production_speed_buildings_factor = 0.08
                political_power_gain = 0.10
            }
        }
        MKN_mutual_aid_economy = {
            picture = gre_agricultural_communes
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                consumer_goods_factor = -0.05
                stability_factor = 0.05
                political_power_gain = 0.10
            }
        }
        MKN_serial_production = {
            picture = generic_industrial_concern_2
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                industrial_capacity_factory = 0.10
                production_factory_max_efficiency_factor = 0.10
            }
        }
        MKN_cooperative_production = {
            picture = generic_industrial_concern_2
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                industrial_capacity_factory = 0.06
                production_factory_efficiency_gain_factor = 0.15
                research_speed_factor = 0.03
            }
        }
        MKN_dnieper_logistics = {
            picture = ARG_invest_in_railways
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                supply_consumption_factor = -0.10
                army_org_regain = 0.05
            }
        }
        MKN_artel_logistics = {
            picture = generic_supply_depot
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                supply_consumption_factor = -0.08
                attrition = -0.05
            }
        }
        MKN_worker_battalions_idea = {
            picture = YUG_local_militias
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                army_org_factor = 0.06
                max_planning = 0.05
            }
        }
        MKN_mobile_self_defence_idea = {
            picture = HABSBURG_cavalry
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                army_org_factor = 0.04
                army_speed_factor = 0.05
                training_time_army_factor = -0.05
            }
        }
        MKN_construction_drive = {
            picture = generic_industrial_concern_1
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                production_speed_buildings_factor = 0.10
                consumer_goods_factor = 0.05
            }
        }
        MKN_careful_investment = {
            picture = generic_industrial_concern_1
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                production_factory_efficiency_gain_factor = 0.08
            }
        }
        MKN_export_contracts = {
            picture = generic_supply_depot
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                consumer_goods_factor = -0.05
                political_power_gain = -0.10
            }
        }
        MKN_local_reserves = {
            picture = gre_agricultural_communes
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                stability_factor = 0.03
                supply_consumption_factor = -0.05
            }
        }
    }
    industrial_concern = {
        MKN_industry_concern_1 = {
            visible = {
                NOT = {
                    has_completed_focus = MKN_steel_volnitsa
                }
            }
            picture = generic_industrial_concern_1
            allowed = {
                original_tag = MKN
            }
            available = {
                has_completed_focus = MKN_zaporizhstal
                NOT = {
                    has_completed_focus = MKN_steel_volnitsa
                }
            }
            cost = 100
            research_bonus = {
                industry = 0.1
            }
            modifier = {
                production_speed_buildings_factor = 0.05
            }
        }
        MKN_industry_concern_2 = {
            visible = {
                has_completed_focus = MKN_steel_volnitsa
            }
            name = MKN_industry_concern_1
            picture = generic_industrial_concern_2
            allowed = {
                original_tag = MKN
            }
            available = {
                has_completed_focus = MKN_steel_volnitsa
            }
            cost = 100
            research_bonus = {
                industry = 0.15
            }
            modifier = {
                production_speed_buildings_factor = 0.08
                industrial_capacity_factory = 0.05
            }
        }
    }
    materiel_manufacturer = {
        designer = yes
        MKN_rifle_concern_1 = {
            visible = {
                NOT = {
                    has_completed_focus = MKN_workshop_standards
                }
            }
            allowed = {
                original_tag = MKN
                NOT = {
                    has_dlc = "Arms Against Tyranny"
                }
            }
            available = {
                NOT = {
                    has_completed_focus = MKN_workshop_standards
                }
                OR = {
                    has_completed_focus = MKN_rifle_concern
                    OR = {
                        has_completed_focus = MKN_steppe_horde
                        hidden_trigger = {
                            has_country_flag = MKN_military_stat_village_muster
                        }
                    }
                }
            }
            cost = 100
            research_bonus = {
                infantry_weapons = 0.1
            }
            modifier = {
                political_power_gain = 0.05
            }
            picture = MKN_company_rifle_artels
        }
        MKN_rifle_concern_2 = {
            visible = {
                has_completed_focus = MKN_workshop_standards
            }
            name = MKN_rifle_concern_1
            allowed = {
                original_tag = MKN
                NOT = {
                    has_dlc = "Arms Against Tyranny"
                }
            }
            available = {
                OR = {
                    has_completed_focus = MKN_rifle_concern
                    OR = {
                        has_completed_focus = MKN_steppe_horde
                        hidden_trigger = {
                            has_country_flag = MKN_military_stat_village_muster
                        }
                    }
                }
                has_completed_focus = MKN_workshop_standards
            }
            cost = 100
            research_bonus = {
                infantry_weapons = 0.15
            }
            modifier = {
                political_power_gain = 0.05
                industrial_capacity_factory = 0.03
            }
            picture = MKN_company_rifle_artels
        }
    }
}
```

### `common/ideas/nww_companies.txt`

```pdx
MKN_kommunar_company = {
    picture = MKN_company_kommunar
    cost = 150
    allowed = {
        original_tag = MKN
        NOT = {
            has_dlc = "Arms Against Tyranny"
        }
    }
    available = {
        OR = {
            has_completed_focus = MKN_motorized_vanguard
            hidden_trigger = {
                has_country_flag = MKN_military_stat_steel_horses
            }
        }
    }
    research_bonus = {
        armor = 0.10
    }
    traits = {
        MKN_kommunar_company_specialization
    }
}
MKN_artillery_works_company = {
    picture = MKN_company_artillery_works
    cost = 150
    allowed = {
        original_tag = MKN
        NOT = {
            has_dlc = "Arms Against Tyranny"
        }
    }
    available = {
        OR = {
            OR = {
                has_completed_focus = MKN_communal_fire_support_focus
                hidden_trigger = {
                    has_country_flag = MKN_military_stat_artillery_artels
                }
            }
            OR = {
                has_completed_focus = MKN_steppe_horde
                hidden_trigger = {
                    has_country_flag = MKN_military_stat_machinegun_carts
                }
            }
        }
    }
    research_bonus = {
        artillery = 0.10
    }
    traits = {
        MKN_artillery_works_company_specialization
    }
}
MKN_air_artels_company = {
    picture = MKN_company_air_artels
    cost = 150
    allowed = {
        original_tag = MKN
        NOT = {
            has_dlc = "Arms Against Tyranny"
        }
    }
    available = {
        OR = {
            has_completed_focus = MKN_interceptor_cooperatives
            hidden_trigger = {
                has_country_flag = MKN_military_stat_aircraft_artels
            }
        }
    }
    research_bonus = {
        air_equipment = 0.10
    }
    traits = {
        MKN_air_artels_company_specialization
    }
}
MKN_attack_air_artels_company = {
    picture = MKN_company_attack_air_artels
    cost = 150
    allowed = {
        original_tag = MKN
        NOT = {
            has_dlc = "Arms Against Tyranny"
        }
    }
    available = {
        OR = {
            has_completed_focus = MKN_flying_artillery_focus
            hidden_trigger = {
                has_country_flag = MKN_military_stat_attack_air_artels
            }
        }
    }
    research_bonus = {
        air_equipment = 0.10
    }
    traits = {
        MKN_attack_air_artels_company_specialization
    }
}
MKN_kherson_works_company = {
    picture = MKN_company_kherson_works
    cost = 150
    allowed = {
        original_tag = MKN
        NOT = {
            has_dlc = "Arms Against Tyranny"
        }
    }
    available = {
        OR = {
            has_completed_focus = MKN_black_sea_flotilla_and_yards
            hidden_trigger = {
                has_country_flag = MKN_military_stat_kherson_shipyard
            }
        }
    }
    research_bonus = {
        naval_equipment = 0.10
    }
    traits = {
        MKN_kherson_works_company_specialization
    }
}
MKN_submarine_works_company = {
    picture = MKN_company_submarine_works
    cost = 150
    allowed = {
        original_tag = MKN
        NOT = {
            has_dlc = "Arms Against Tyranny"
        }
    }
    available = {
        OR = {
            has_completed_focus = MKN_torpedo_artels_focus
            hidden_trigger = {
                has_country_flag = MKN_military_stat_submarine_crews
            }
        }
    }
    research_bonus = {
        naval_equipment = 0.10
    }
    traits = {
        MKN_submarine_works_company_specialization
    }
}
```

### `common/country_leader/MKN_eugen_traits.txt`

```pdx
leader_traits = {
    mkn_eugen_infantry_master = {
        sprite = 5
        random = no
        army_infantry_attack_factor = 0.15
        army_infantry_defence_factor = 0.15
        army_morale_factor = 0.05
    }
}
```

### `common/country_leader/MKN_overhaul_traits.txt`

```pdx
leader_traits = {
    mkn_iron_warlord = {
        sprite = 15
        random = no
        army_attack_factor = 0.15
        war_support_factor = 0.15
        stability_factor = -0.15
    }
    mkn_idealist_philosopher = {
        sprite = 15
        random = no
        stability_factor = 0.25
        political_power_gain = 0.30
        war_support_factor = -0.10
    }
    mkn_granary_overseer = {
        sprite = 15
        random = no
        army_defence_factor = 0.20
        trade_opinion_factor = -0.20
        global_building_slots_factor = 0.20
    }
    mkn_paralyzed_committee = {
        sprite = 15
        random = no
        political_power_gain = -0.10
    }
    mkn_syndicalist_organizer = {
        sprite = 15
        random = no
        industrial_capacity_factory = 0.10
        army_org_factor = 0.10
    }
    mkn_batko_advisor = {
        sprite = 15
        random = no
        army_org_factor = 0.25
        org_loss_when_moving = -0.20
        planning_speed = 0.20
    }
    mkn_infantry_specialist = {
        sprite = 15
        random = no
        army_infantry_attack_factor = 0.10
        army_infantry_defence_factor = 0.10
    }
    mkn_tachanka_expert = {
        sprite = 15
        random = no
        army_speed_factor = 0.15
        modifier_army_sub_unit_cavalry_attack_factor = 0.10
        motorized_attack_factor = 0.10
    }
    mkn_armored_train_commander = {
        sprite = 15
        random = no
        custom_modifier_tooltip = MKN_armored_train_commander_tt
    }
    mkn_steppe_logistics_officer = {
        sprite = 15
        random = no
        supply_consumption_factor = -0.15
    }
    mkn_entrenchment_specialist = {
        sprite = 15
        random = no
        dig_in_speed_factor = 0.15
    }
    mkn_weapons_broker = {
        sprite = 15
        random = no
        production_speed_arms_factory_factor = 0.10
    }
    mkn_recruiting_commissar = {
        sprite = 15
        random = no
        conscription = 0.02
    }
    mkn_military_orator = {
        sprite = 15
        random = no
        war_support_factor = 0.10
    }
    mkn_frontline_delegate = {
        sprite = 15
        random = no
        army_org_factor = 0.05
    }
    mkn_arsenal_coordinator = {
        sprite = 15
        random = no
        industrial_capacity_factory = 0.10
    }
    mkn_veterans_organizer = {
        sprite = 15
        random = no
        experience_gain_army_factor = 0.10
    }
    mkn_education_delegate = {
        sprite = 15
        random = no
        research_speed_factor = 0.05
    }
    mkn_commune_secretary = {
        sprite = 15
        random = no
        political_power_gain = 0.20
    }
    mkn_anti_statist_theorist = {
        sprite = 15
        random = no
        stability_factor = 0.10
    }
    mkn_cooperative_treasurer = {
        sprite = 15
        random = no
        consumer_goods_factor = -0.05
    }
    mkn_literacy_organizer = {
        sprite = 15
        random = no
        research_speed_factor = 0.05
    }
    mkn_free_press_editor = {
        sprite = 15
        random = no
        democratic_drift = 0.05
    }
    mkn_grain_distributor = {
        sprite = 15
        random = no
        supply_consumption_factor = -0.10
    }
    mkn_rural_defender = {
        sprite = 15
        random = no
        army_core_defence_factor = 0.10
    }
    mkn_militia_delegate = {
        sprite = 15
        random = no
        conscription = 0.02
    }
    mkn_agronomist = {
        sprite = 15
        random = no
        production_speed_infrastructure_factor = 0.10
    }
    mkn_village_mediator = {
        sprite = 15
        random = no
        stability_factor = 0.10
    }
    mkn_market_keeper = {
        sprite = 15
        random = no
        trade_opinion_factor = 0.10
    }
    mkn_industrial_organizer = {
        sprite = 15
        random = no
        industrial_capacity_factory = 0.10
    }
    mkn_rail_dispatcher = {
        sprite = 15
        random = no
        production_speed_rail_way_factor = 0.15
    }
    mkn_union_secretary = {
        sprite = 15
        random = no
        political_power_gain = 0.20
    }
    mkn_workshop_engineer = {
        sprite = 15
        random = no
        production_factory_max_efficiency_factor = 0.05
    }
    mkn_labor_delegate = {
        sprite = 15
        random = no
        production_speed_buildings_factor = 0.10
    }
    mkn_syndicalist_theorist = {
        sprite = 15
        random = no
        communism_drift = 0.05
    }
}
```

### `common/country_leader/nww_mkn_advisor_traits.txt`

```pdx
leader_traits = {
    NWW_MKN_oleksandr_hordiienko_specialty = {
        sprite = 15
        max_dig_in_factor = 0.06
        production_speed_bunker_factor = 0.10
        random = no
    }
    NWW_MKN_andrii_dorosh_specialty = {
        sprite = 15
        army_defence_factor = 0.05
        army_org_factor = 0.03
        random = no
    }
    NWW_MKN_mykola_kovalenko_specialty = {
        sprite = 15
        experience_gain_army = 0.05
        land_doctrine_cost_factor = -0.05
        random = no
    }
    NWW_MKN_roman_danylenko_specialty = {
        sprite = 15
        army_artillery_attack_factor = 0.07
        army_artillery_defence_factor = 0.04
        random = no
    }
    NWW_MKN_olena_hrytsenko_specialty = {
        sprite = 15
        supply_consumption_factor = -0.06
        attrition = -0.04
        random = no
    }
    NWW_MKN_dmytro_savchenko_specialty = {
        sprite = 15
        air_cas_efficiency = 0.06
        air_mission_efficiency = 0.03
        random = no
    }
    NWW_MKN_yakiv_levchenko_specialty = {
        sprite = 15
        convoy_escort_efficiency = 0.08
        repair_speed_factor = 0.05
        random = no
    }
    NWW_MKN_petro_stepanenko_specialty = {
        sprite = 15
        production_speed_buildings_factor = 0.05
        factory_energy_consumption = -0.05
        random = no
    }
    NWW_MKN_ivan_bondarenko_specialty = {
        sprite = 15
        political_power_gain = 0.10
        consumer_goods_factor = -0.04
        random = no
    }
    NWW_MKN_serhii_melnyk_specialty = {
        sprite = 15
        research_speed_factor = 0.04
        random = no
    }
}
```

### `common/country_leader/nww_mkn_industry_traits.txt`

```pdx
leader_traits = {
    MKN_kommunar_company_specialization = {
        army_armor_speed_factor = 0.05
        army_armor_defence_factor = 0.03
        random = no
    }
    MKN_artillery_works_company_specialization = {
        army_artillery_attack_factor = 0.05
        random = no
    }
    MKN_air_artels_company_specialization = {
        air_agility_factor = 0.05
        random = no
    }
    MKN_attack_air_artels_company_specialization = {
        air_cas_efficiency = 0.05
        random = no
    }
    MKN_kherson_works_company_specialization = {
        convoy_escort_efficiency = 0.05
        random = no
    }
    MKN_submarine_works_company_specialization = {
        convoy_raiding_efficiency_factor = 0.05
        random = no
    }
}
```

### `common/characters/MKN.txt`

```pdx
characters = {
    MKN_buenaventura_durruti = {
        name = MKN_buenaventura_durruti
        portraits = {
            army = {
                large = GFX_Portrait_MKN_buenaventura_durruti
                small = GFX_Portrait_MKN_buenaventura_durruti_small
            }
        }
        corps_commander = {
            skill = 4
            attack_skill = 4
            defense_skill = 3
            planning_skill = 3
            logistics_skill = 3
            traits = {
                urban_assault_specialist
                commando
                trait_mountaineer
            }
        }
    }
}
```

### `common/characters/MKN_eugen.txt`

```pdx
characters = {
    NWW_MKN_eugen = {
        name = NWW_MKN_eugen
        portraits = {
            army = {
                large = GFX_Portrait_MKN_eugen
                small = GFX_idea_MKN_eugen
            }
            civilian = {
                large = GFX_Portrait_MKN_eugen
                small = GFX_idea_MKN_eugen
            }
        }
        advisor = {
            slot = high_command
            idea_token = NWW_MKN_eugen_high_command
            ledger = army
            cost = 200
            allowed = {
                original_tag = MKN
            }
            available = {
                has_completed_focus = MKN_steppe_general_staff
            }
            traits = {
                mkn_eugen_infantry_master
            }
            ai_will_do = {
                factor = 2
            }
        }
        corps_commander = {
            skill = 4
            attack_skill = 4
            defense_skill = 4
            planning_skill = 3
            logistics_skill = 3
            traits = {
                infantry_officer
                infantry_leader
            }
        }
    }
}
```

### `common/characters/nww_MKN.txt`

```pdx
characters = {
    NWW_MKN_viktor_belash = {
        name = NWW_MKN_viktor_belash
        portraits = {
            civilian = {
                large = GFX_Portrait_MKN_viktor_belash
                small = GFX_idea_MKN_viktor_belash
            }
            army = {
                large = GFX_Portrait_MKN_viktor_belash
                small = GFX_idea_MKN_viktor_belash
            }
            navy = {
                large = GFX_Portrait_MKN_viktor_belash
                small = GFX_idea_MKN_viktor_belash
            }
        }
        advisor = {
            slot = army_chief
            idea_token = NWW_MKN_viktor_belash_army_chief
            cost = 150
            allowed = {
                original_tag = MKN
            }
            traits = {
                army_chief_maneuver_2
            }
        }
        field_marshal = {
            traits = {
                offensive_doctrine
            }
            skill = 3
            attack_skill = 3
            defense_skill = 3
            planning_skill = 4
            logistics_skill = 4
        }
    }
    NWW_MKN_fedir_shchus = {
        name = NWW_MKN_fedir_shchus
        portraits = {
            civilian = {
                large = GFX_Portrait_MKN_fedir_shchus
                small = GFX_idea_MKN_fedir_shchus
            }
            army = {
                large = GFX_Portrait_MKN_fedir_shchus
                small = GFX_idea_MKN_fedir_shchus
            }
            navy = {
                large = GFX_Portrait_MKN_fedir_shchus
                small = GFX_idea_MKN_fedir_shchus
            }
        }
        advisor = {
            slot = navy_chief
            idea_token = NWW_MKN_fedir_shchus_navy_chief
            cost = 150
            allowed = {
                original_tag = MKN
            }
            traits = {
                navy_chief_commerce_raiding_1
            }
        }
        advisor = {
            slot = high_command
            idea_token = NWW_MKN_fedir_shchus_high_command
            cost = 150
            allowed = {
                original_tag = MKN
            }
            ledger = army
            traits = {
                mkn_tachanka_expert
            }
        }
        corps_commander = {
            traits = {
                cavalry_leader
            }
            skill = 3
            attack_skill = 5
            defense_skill = 2
            planning_skill = 2
            logistics_skill = 2
        }
    }
    NWW_MKN_volin = {
        name = NWW_MKN_volin
        portraits = {
            civilian = {
                large = GFX_Portrait_volin
                small = GFX_idea_volin
            }
            army = {
                large = GFX_Portrait_volin
                small = GFX_idea_volin
            }
            navy = {
                large = GFX_Portrait_volin
                small = GFX_idea_volin
            }
        }
    }
    NWW_MKN_makhno = {
        name = NWW_MKN_makhno
        portraits = {
            civilian = {
                large = GFX_Portrait_makhno
                small = GFX_idea_makhno
            }
            army = {
                large = GFX_Portrait_makhno
                small = GFX_idea_makhno
            }
            navy = {
                large = GFX_Portrait_makhno
                small = GFX_idea_makhno
            }
        }
        advisor = {
            slot = high_command
            idea_token = NWW_MKN_makhno_high_command
            cost = 150
            allowed = {
                original_tag = MKN
            }
            ledger = army
            available = {
                has_government = communism
            }
            traits = {
                mkn_batko_advisor
            }
        }
        field_marshal = {
            visible = {
                has_government = communism
            }
            skill = 6
            attack_skill = 6
            defense_skill = 5
            planning_skill = 5
            logistics_skill = 5
            traits = {
                trickster
                cavalry_officer
                skirmisher
                mkn_batko_legend
            }
        }
        corps_commander = {
            skill = 6
            attack_skill = 6
            defense_skill = 5
            planning_skill = 5
            logistics_skill = 5
            traits = {
                trickster
                cavalry_officer
                skirmisher
                mkn_batko_legend
            }
        }
    }
    NWW_MKN_peter_arshinov = {
        name = NWW_MKN_peter_arshinov
        portraits = {
            army = {
                small = GFX_idea_generic_political_advisor_europe_2
            }
        }
    }
    NWW_MKN_school_delegate = {
        name = NWW_MKN_school_delegate
        portraits = {
            army = {
                small = GFX_idea_generic_air_europe_2
            }
        }
        advisor = {
            slot = air_chief
            idea_token = NWW_MKN_school_delegate
            cost = 150
            allowed = {
                original_tag = MKN
            }
            traits = {
                air_chief_safety_2
            }
        }
    }
    NWW_MKN_logistics_delegate = {
        name = NWW_MKN_logistics_delegate
        portraits = {
            army = {
                small = GFX_idea_generic_army_europe_3
            }
        }
        advisor = {
            slot = high_command
            idea_token = NWW_MKN_logistics_delegate
            cost = 150
            allowed = {
                original_tag = MKN
            }
            traits = {
                army_logistics_2
            }
            ledger = army
        }
    }
    NWW_MKN_military_theorist = {
        name = NWW_MKN_military_theorist
        portraits = {
            army = {
                small = GFX_idea_generic_army_europe_4
            }
        }
        advisor = {
            slot = theorist
            idea_token = NWW_MKN_military_theorist
            cost = 150
            allowed = {
                original_tag = MKN
            }
            traits = {
                military_theorist
            }
            ledger = army
        }
    }
    NWW_MKN_oleksandr_hordiienko = {
        name = NWW_MKN_oleksandr_hordiienko
        portraits = {
            army = {
                large = GFX_Portrait_MKN_oleksandr_hordiienko
                small = GFX_idea_MKN_oleksandr_hordiienko
            }
            civilian = {
                large = GFX_Portrait_MKN_oleksandr_hordiienko
                small = GFX_idea_MKN_oleksandr_hordiienko
            }
        }
        advisor = {
            slot = high_command
            idea_token = NWW_MKN_oleksandr_hordiienko_advisor
            cost = 125
            allowed = {
                original_tag = MKN
            }
            available = {
                has_completed_focus = MKN_steppe_general_staff
            }
            ledger = army
            traits = {
                mkn_entrenchment_specialist
            }
        }
        corps_commander = {
            skill = 3
            attack_skill = 3
            defense_skill = 3
            planning_skill = 2
            logistics_skill = 3
            traits = {
                engineer_officer
            }
        }
    }
    NWW_MKN_andrii_dorosh = {
        name = NWW_MKN_andrii_dorosh
        portraits = {
            army = {
                large = GFX_Portrait_MKN_andrii_dorosh
                small = GFX_idea_MKN_andrii_dorosh
            }
            civilian = {
                large = GFX_Portrait_MKN_andrii_dorosh
                small = GFX_idea_MKN_andrii_dorosh
            }
        }
        advisor = {
            slot = army_chief
            idea_token = NWW_MKN_andrii_dorosh_advisor
            cost = 125
            allowed = {
                original_tag = MKN
            }
            available = {
                has_completed_focus = MKN_steppe_general_staff
            }
            traits = {
                NWW_MKN_andrii_dorosh_specialty
            }
            ledger = army
        }
        corps_commander = {
            skill = 3
            attack_skill = 2
            defense_skill = 4
            planning_skill = 3
            logistics_skill = 2
            traits = {
                inflexible_strategist
            }
        }
        advisor = {
            slot = high_command
            idea_token = NWW_MKN_andrii_dorosh_high_command
            cost = 150
            allowed = {
                original_tag = MKN
            }
            ledger = army
            traits = {
                mkn_infantry_specialist
            }
        }
    }
    NWW_MKN_mykola_kovalenko = {
        name = NWW_MKN_mykola_kovalenko
        portraits = {
            army = {
                large = GFX_Portrait_MKN_mykola_kovalenko
                small = GFX_idea_MKN_mykola_kovalenko
            }
            civilian = {
                large = GFX_Portrait_MKN_mykola_kovalenko
                small = GFX_idea_MKN_mykola_kovalenko
            }
        }
        advisor = {
            slot = theorist
            idea_token = NWW_MKN_mykola_kovalenko_advisor
            cost = 125
            allowed = {
                original_tag = MKN
            }
            available = {
                OR = {
                    has_completed_focus = MKN_steppe_general_staff
                    hidden_trigger = {
                        has_country_flag = MKN_military_stat_tachanka_columns
                    }
                }
            }
            traits = {
                NWW_MKN_mykola_kovalenko_specialty
            }
            ledger = army
        }
        corps_commander = {
            skill = 2
            attack_skill = 3
            defense_skill = 2
            planning_skill = 2
            logistics_skill = 2
            traits = {
                cavalry_officer
            }
        }
    }
    NWW_MKN_roman_danylenko = {
        name = NWW_MKN_roman_danylenko
        portraits = {
            army = {
                large = GFX_Portrait_MKN_roman_danylenko
                small = GFX_idea_MKN_roman_danylenko
            }
            civilian = {
                large = GFX_Portrait_MKN_roman_danylenko
                small = GFX_idea_MKN_roman_danylenko
            }
        }
        advisor = {
            slot = high_command
            idea_token = NWW_MKN_roman_danylenko_advisor
            cost = 125
            allowed = {
                original_tag = MKN
            }
            available = {
                has_completed_focus = MKN_steppe_general_staff
            }
            ledger = army
            traits = {
                mkn_armored_train_commander
            }
            on_add = {
                MKN = {
                    add_ideas = MKN_armored_train_staff_bonus
                }
            }
            on_remove = {
                MKN = {
                    remove_ideas = MKN_armored_train_staff_bonus
                }
            }
        }
        corps_commander = {
            skill = 3
            attack_skill = 3
            defense_skill = 2
            planning_skill = 4
            logistics_skill = 2
            traits = {
                brilliant_strategist
            }
        }
    }
    NWW_MKN_olena_hrytsenko = {
        name = NWW_MKN_olena_hrytsenko
        portraits = {
            army = {
                large = GFX_Portrait_MKN_olena_hrytsenko
                small = GFX_idea_MKN_olena_hrytsenko
            }
            civilian = {
                large = GFX_Portrait_MKN_olena_hrytsenko
                small = GFX_idea_MKN_olena_hrytsenko
            }
        }
        advisor = {
            slot = high_command
            idea_token = NWW_MKN_olena_hrytsenko_advisor
            cost = 125
            allowed = {
                original_tag = MKN
            }
            available = {
                has_completed_focus = MKN_steppe_general_staff
            }
            ledger = army
            traits = {
                mkn_steppe_logistics_officer
            }
        }
        gender = female
        corps_commander = {
            skill = 2
            attack_skill = 2
            defense_skill = 3
            planning_skill = 2
            logistics_skill = 3
            traits = {
                organizer
            }
        }
    }
    NWW_MKN_dmytro_savchenko = {
        name = NWW_MKN_dmytro_savchenko
        portraits = {
            army = {
                large = GFX_Portrait_MKN_dmytro_savchenko
                small = GFX_idea_MKN_dmytro_savchenko
            }
            civilian = {
                large = GFX_Portrait_MKN_dmytro_savchenko
                small = GFX_idea_MKN_dmytro_savchenko
            }
        }
        advisor = {
            slot = air_chief
            idea_token = NWW_MKN_dmytro_savchenko_advisor
            cost = 125
            allowed = {
                original_tag = MKN
            }
            available = {
                OR = {
                    has_completed_focus = MKN_steppe_hawks_and_schools
                    hidden_trigger = {
                        has_country_flag = MKN_military_stat_gulyaipole_pilot_school
                    }
                }
            }
            traits = {
                NWW_MKN_dmytro_savchenko_specialty
            }
            ledger = air
        }
        corps_commander = {
            skill = 2
            attack_skill = 2
            defense_skill = 2
            planning_skill = 3
            logistics_skill = 2
            traits = {
                infantry_officer
            }
        }
    }
    NWW_MKN_yakiv_levchenko = {
        name = NWW_MKN_yakiv_levchenko
        portraits = {
            army = {
                large = GFX_Portrait_MKN_yakiv_levchenko
                small = GFX_idea_MKN_yakiv_levchenko
            }
            civilian = {
                large = GFX_Portrait_MKN_yakiv_levchenko
                small = GFX_idea_MKN_yakiv_levchenko
            }
        }
        advisor = {
            slot = navy_chief
            idea_token = NWW_MKN_yakiv_levchenko_advisor
            cost = 125
            allowed = {
                original_tag = MKN
            }
            available = {
                OR = {
                    has_completed_focus = MKN_black_sea_flotilla_and_yards
                    hidden_trigger = {
                        has_country_flag = MKN_military_stat_kherson_shipyard
                    }
                }
            }
            traits = {
                NWW_MKN_yakiv_levchenko_specialty
            }
            ledger = navy
        }
        corps_commander = {
            skill = 3
            attack_skill = 2
            defense_skill = 3
            planning_skill = 3
            logistics_skill = 3
            traits = {
                infantry_officer
            }
        }
    }
    NWW_MKN_petro_stepanenko = {
        name = NWW_MKN_petro_stepanenko
        portraits = {
            army = {
                small = GFX_idea_generic_political_advisor_europe_1
            }
            civilian = {
                small = GFX_idea_generic_political_advisor_europe_1
            }
        }
    }
    NWW_MKN_ivan_bondarenko = {
        name = NWW_MKN_ivan_bondarenko
        portraits = {
            army = {
                small = GFX_idea_generic_political_advisor_europe_2
            }
            civilian = {
                small = GFX_idea_generic_political_advisor_europe_2
            }
        }
    }
    NWW_MKN_serhii_melnyk = {
        name = NWW_MKN_serhii_melnyk
        portraits = {
            army = {
                small = GFX_idea_generic_political_advisor_europe_3
            }
            civilian = {
                small = GFX_idea_generic_political_advisor_europe_3
            }
        }
    }
    MKN_advisor_weapons_broker = {
        name = MKN_advisor_weapons_broker
        portraits = {
            civilian = {
                small = GFX_idea_generic_political_advisor_europe_1
            }
        }
        advisor = {
            slot = political_advisor
            idea_token = MKN_advisor_weapons_broker
            cost = 150
            allowed = {
                original_tag = MKN
            }
            available = {
                has_government = fascism
            }
            traits = {
                mkn_weapons_broker
            }
        }
    }
    MKN_advisor_recruiting_commissar = {
        name = MKN_advisor_recruiting_commissar
        portraits = {
            civilian = {
                small = GFX_idea_generic_political_advisor_europe_2
            }
        }
        advisor = {
            slot = political_advisor
            idea_token = MKN_advisor_recruiting_commissar
            cost = 150
            allowed = {
                original_tag = MKN
            }
            available = {
                has_government = fascism
            }
            traits = {
                mkn_recruiting_commissar
            }
        }
    }
    MKN_advisor_military_orator = {
        name = MKN_advisor_military_orator
        portraits = {
            civilian = {
                small = GFX_idea_generic_political_advisor_europe_1
            }
        }
        advisor = {
            slot = political_advisor
            idea_token = MKN_advisor_military_orator
            cost = 150
            allowed = {
                original_tag = MKN
            }
            available = {
                has_government = fascism
            }
            traits = {
                mkn_military_orator
            }
        }
    }
    MKN_advisor_frontline_delegate = {
        name = MKN_advisor_frontline_delegate
        portraits = {
            civilian = {
                small = GFX_idea_generic_political_advisor_europe_2
            }
        }
        advisor = {
            slot = political_advisor
            idea_token = MKN_advisor_frontline_delegate
            cost = 150
            allowed = {
                original_tag = MKN
            }
            available = {
                has_government = fascism
            }
            traits = {
                mkn_frontline_delegate
            }
        }
    }
    MKN_advisor_arsenal_coordinator = {
        name = MKN_advisor_arsenal_coordinator
        portraits = {
            civilian = {
                small = GFX_idea_generic_political_advisor_europe_1
            }
        }
        advisor = {
            slot = political_advisor
            idea_token = MKN_advisor_arsenal_coordinator
            cost = 150
            allowed = {
                original_tag = MKN
            }
            available = {
                has_government = fascism
            }
            traits = {
                mkn_arsenal_coordinator
            }
        }
    }
    MKN_advisor_veterans_organizer = {
        name = MKN_advisor_veterans_organizer
        portraits = {
            civilian = {
                small = GFX_idea_generic_political_advisor_europe_2
            }
        }
        advisor = {
            slot = political_advisor
            idea_token = MKN_advisor_veterans_organizer
            cost = 150
            allowed = {
                original_tag = MKN
            }
            available = {
                has_government = fascism
            }
            traits = {
                mkn_veterans_organizer
            }
        }
    }
    MKN_advisor_education_delegate = {
        name = MKN_advisor_education_delegate
        portraits = {
            civilian = {
                small = GFX_idea_generic_political_advisor_europe_1
            }
        }
        advisor = {
            slot = political_advisor
            idea_token = MKN_advisor_education_delegate
            cost = 150
            allowed = {
                original_tag = MKN
            }
            available = {
                has_government = democratic
            }
            traits = {
                mkn_education_delegate
            }
        }
    }
    MKN_advisor_commune_secretary = {
        name = MKN_advisor_commune_secretary
        portraits = {
            civilian = {
                small = GFX_idea_generic_political_advisor_europe_2
            }
        }
        advisor = {
            slot = political_advisor
            idea_token = MKN_advisor_commune_secretary
            cost = 150
            allowed = {
                original_tag = MKN
            }
            available = {
                has_government = democratic
            }
            traits = {
                mkn_commune_secretary
            }
        }
    }
    MKN_advisor_anti_statist_theorist = {
        name = MKN_advisor_anti_statist_theorist
        portraits = {
            civilian = {
                small = GFX_idea_generic_political_advisor_europe_1
            }
        }
        advisor = {
            slot = political_advisor
            idea_token = MKN_advisor_anti_statist_theorist
            cost = 150
            allowed = {
                original_tag = MKN
            }
            available = {
                has_government = democratic
            }
            traits = {
                mkn_anti_statist_theorist
            }
        }
    }
    MKN_advisor_cooperative_treasurer = {
        name = MKN_advisor_cooperative_treasurer
        portraits = {
            civilian = {
                small = GFX_idea_generic_political_advisor_europe_2
            }
        }
        advisor = {
            slot = political_advisor
            idea_token = MKN_advisor_cooperative_treasurer
            cost = 150
            allowed = {
                original_tag = MKN
            }
            available = {
                has_government = democratic
            }
            traits = {
                mkn_cooperative_treasurer
            }
        }
    }
    MKN_advisor_literacy_organizer = {
        name = MKN_advisor_literacy_organizer
        portraits = {
            civilian = {
                small = GFX_idea_generic_political_advisor_europe_1
            }
        }
        advisor = {
            slot = political_advisor
            idea_token = MKN_advisor_literacy_organizer
            cost = 150
            allowed = {
                original_tag = MKN
            }
            available = {
                has_government = democratic
            }
            traits = {
                mkn_literacy_organizer
            }
        }
    }
    MKN_advisor_free_press_editor = {
        name = MKN_advisor_free_press_editor
        portraits = {
            civilian = {
                small = GFX_idea_generic_political_advisor_europe_2
            }
        }
        advisor = {
            slot = political_advisor
            idea_token = MKN_advisor_free_press_editor
            cost = 150
            allowed = {
                original_tag = MKN
            }
            available = {
                has_government = democratic
            }
            traits = {
                mkn_free_press_editor
            }
        }
    }
    MKN_advisor_grain_distributor = {
        name = MKN_advisor_grain_distributor
        portraits = {
            civilian = {
                small = GFX_idea_generic_political_advisor_europe_1
            }
        }
        advisor = {
            slot = political_advisor
            idea_token = MKN_advisor_grain_distributor
            cost = 150
            allowed = {
                original_tag = MKN
            }
            available = {
                has_government = neutrality
            }
            traits = {
                mkn_grain_distributor
            }
        }
    }
    MKN_advisor_rural_defender = {
        name = MKN_advisor_rural_defender
        portraits = {
            civilian = {
                small = GFX_idea_generic_political_advisor_europe_2
            }
        }
        advisor = {
            slot = political_advisor
            idea_token = MKN_advisor_rural_defender
            cost = 150
            allowed = {
                original_tag = MKN
            }
            available = {
                has_government = neutrality
            }
            traits = {
                mkn_rural_defender
            }
        }
    }
    MKN_advisor_militia_delegate = {
        name = MKN_advisor_militia_delegate
        portraits = {
            civilian = {
                small = GFX_idea_generic_political_advisor_europe_1
            }
        }
        advisor = {
            slot = political_advisor
            idea_token = MKN_advisor_militia_delegate
            cost = 150
            allowed = {
                original_tag = MKN
            }
            available = {
                has_government = neutrality
            }
            traits = {
                mkn_militia_delegate
            }
        }
    }
    MKN_advisor_agronomist = {
        name = MKN_advisor_agronomist
        portraits = {
            civilian = {
                small = GFX_idea_generic_political_advisor_europe_2
            }
        }
        advisor = {
            slot = political_advisor
            idea_token = MKN_advisor_agronomist
            cost = 150
            allowed = {
                original_tag = MKN
            }
            available = {
                has_government = neutrality
            }
            traits = {
                mkn_agronomist
            }
        }
    }
    MKN_advisor_village_mediator = {
        name = MKN_advisor_village_mediator
        portraits = {
            civilian = {
                small = GFX_idea_generic_political_advisor_europe_1
            }
        }
        advisor = {
            slot = political_advisor
            idea_token = MKN_advisor_village_mediator
            cost = 150
            allowed = {
                original_tag = MKN
            }
            available = {
                has_government = neutrality
            }
            traits = {
                mkn_village_mediator
            }
        }
    }
    MKN_advisor_market_keeper = {
        name = MKN_advisor_market_keeper
        portraits = {
            civilian = {
                small = GFX_idea_generic_political_advisor_europe_2
            }
        }
        advisor = {
            slot = political_advisor
            idea_token = MKN_advisor_market_keeper
            cost = 150
            allowed = {
                original_tag = MKN
            }
            available = {
                has_government = neutrality
            }
            traits = {
                mkn_market_keeper
            }
        }
    }
    MKN_advisor_industrial_organizer = {
        name = MKN_advisor_industrial_organizer
        portraits = {
            civilian = {
                small = GFX_Portrait_MKN_osyp_tsebriy_small
            }
        }
        advisor = {
            slot = political_advisor
            idea_token = MKN_advisor_industrial_organizer
            cost = 150
            allowed = {
                original_tag = MKN
            }
            available = {
                has_government = communism
            }
            traits = {
                mkn_industrial_organizer
            }
        }
    }
    MKN_advisor_rail_dispatcher = {
        name = MKN_advisor_rail_dispatcher
        portraits = {
            civilian = {
                small = GFX_idea_generic_political_advisor_europe_2
            }
        }
        advisor = {
            slot = political_advisor
            idea_token = MKN_advisor_rail_dispatcher
            cost = 150
            allowed = {
                original_tag = MKN
            }
            available = {
                has_government = communism
            }
            traits = {
                mkn_rail_dispatcher
            }
        }
    }
    MKN_advisor_union_secretary = {
        name = MKN_advisor_union_secretary
        portraits = {
            civilian = {
                small = GFX_idea_generic_political_advisor_europe_1
            }
        }
        advisor = {
            slot = political_advisor
            idea_token = MKN_advisor_union_secretary
            cost = 150
            allowed = {
                original_tag = MKN
            }
            available = {
                has_government = communism
            }
            traits = {
                mkn_union_secretary
            }
        }
    }
    MKN_advisor_workshop_engineer = {
        name = MKN_advisor_workshop_engineer
        portraits = {
            civilian = {
                small = GFX_idea_generic_political_advisor_europe_2
            }
        }
        advisor = {
            slot = political_advisor
            idea_token = MKN_advisor_workshop_engineer
            cost = 150
            allowed = {
                original_tag = MKN
            }
            available = {
                has_government = communism
            }
            traits = {
                mkn_workshop_engineer
            }
        }
    }
    MKN_advisor_labor_delegate = {
        name = MKN_advisor_labor_delegate
        portraits = {
            civilian = {
                small = GFX_idea_generic_political_advisor_europe_1
            }
        }
        advisor = {
            slot = political_advisor
            idea_token = MKN_advisor_labor_delegate
            cost = 150
            allowed = {
                original_tag = MKN
            }
            available = {
                has_government = communism
            }
            traits = {
                mkn_labor_delegate
            }
        }
    }
    MKN_advisor_syndicalist_theorist = {
        name = MKN_advisor_syndicalist_theorist
        portraits = {
            civilian = {
                small = GFX_idea_generic_political_advisor_europe_2
            }
        }
        advisor = {
            slot = political_advisor
            idea_token = MKN_advisor_syndicalist_theorist
            cost = 150
            allowed = {
                original_tag = MKN
            }
            available = {
                has_government = communism
            }
            traits = {
                mkn_syndicalist_theorist
            }
        }
    }
}
```

## Вызываемые scripted effects и triggers

### `MKN_build_border_forts` — `common/scripted_effects/MKN_effects.txt`

```pdx
MKN_build_border_forts = {
    every_neighbor_country = {
        limit = {
            NOT = {
                original_tag = MKN
            }
        }
        save_event_target_as = MKN_fort_neighbor
        ROOT = {
            every_owned_state = {
                limit = {
                    is_controlled_by = ROOT
                    any_neighbor_state = {
                        is_owned_by = event_target:MKN_fort_neighbor
                    }
                }
                add_building_construction = {
                    type = bunker
                    level = 2
                    instant_build = yes
                    province = {
                        all_provinces = yes
                        limit_to_border_country = event_target:MKN_fort_neighbor
                    }
                }
            }
        }
    }
}
```

### `MKN_build_soviet_rail_link` — `common/scripted_effects/MKN_effects.txt`

```pdx
MKN_build_soviet_rail_link = {
    random_owned_state = {
        limit = {
            is_controlled_by = ROOT
            any_neighbor_state = {
                is_owned_and_controlled_by = SOV
            }
        }
        save_event_target_as = MKN_rail_start
        random_neighbor_state = {
            limit = {
                is_owned_and_controlled_by = SOV
            }
            save_event_target_as = MKN_rail_end
        }
    }
    build_railway = {
        level = 2
        start_state = event_target:MKN_rail_start
        target_state = event_target:MKN_rail_end
        controller_priority = {
            base = -1
            modifier = {
                add = 2
                OR = {
                    tag = MKN
                    tag = SOV
                }
            }
        }
    }
    add_equipment_to_stockpile = {
        type = train_equipment_1
        amount = 10
        producer = SOV
    }
}
```

### `MKN_clear_expropriation_factories` — `common/scripted_effects/MKN_international_effects.txt`

```pdx
MKN_clear_expropriation_factories = {
    if = {
        limit = {
            has_country_flag = MKN_expropriation_factories_active
            NOT = {
                has_variable = MKN_expropriation_factories
            }
        }
        set_variable = {
            MKN_expropriation_factories = 2
        }
    }
    while = {
        limit = {
            check_variable = {
                MKN_expropriation_factories > 0
            }
        }
        add_offsite_building = {
            type = industrial_complex
            level = -1
        }
        subtract_from_variable = {
            MKN_expropriation_factories = 1
        }
    }
    clr_country_flag = MKN_expropriation_factories_active
    clear_variable = MKN_expropriation_factories
}
```

### `MKN_dismantle_bop` — `common/scripted_effects/MKN_effects.txt`

```pdx
MKN_dismantle_bop = {
    set_country_flag = MKN_bop_abandoned
    if = {
        limit = {
            has_power_balance = {
                id = MKN_power_balance
            }
        }
        remove_power_balance = {
            id = MKN_power_balance
        }
    }
}
```

### `MKN_install_tsebriy` — `common/scripted_effects/MKN_effects.txt`

```pdx
MKN_install_tsebriy = {
    retire_ideology_leader = communism
    create_country_leader = {
        name = MKN_osyp_tsebriy
        picture = GFX_Portrait_MKN_osyp_tsebriy
        ideology = leninism
        traits = {
            mkn_syndicalist_organizer
        }
    }
    remove_ideas = MKN_revkom_terror
}
```

### `MKN_raise_black_guard_battalions` — `common/scripted_effects/MKN_international_effects.txt`

```pdx
MKN_raise_black_guard_battalions = {
    if = {
        limit = {
            NOT = {
                has_country_flag = MKN_black_guard_deployed
            }
            1082 = {
                is_owned_and_controlled_by = ROOT
            }
            has_tech = tech_engineers
            has_tech = tech_recon
            has_tech = tech_field_hospital
        }
        set_country_flag = MKN_black_guard_deployed
        load_oob = MKN_black_guard_oob
        army_experience = 20
    }
}
```

### `MKN_raise_communal_militias` — `common/scripted_effects/MKN_effects.txt`

```pdx
MKN_raise_communal_militias = {
    division_template = {
        name = MKN_Commune_Guard
        regiments = {
            infantry = {
                x = 0
                y = 0
            }
            infantry = {
                x = 0
                y = 1
            }
            infantry = {
                x = 0
                y = 2
            }
        }
    }
    add_manpower = 9000
    add_equipment_to_stockpile = {
        type = infantry_equipment_0
        amount = 900
        producer = MKN
    }
    create_unit = {
        owner = ROOT
        division = "division_template = MKN_Commune_Guard start_experience_factor = 0.10 start_equipment_factor = 1"
    }
    create_unit = {
        owner = ROOT
        division = "division_template = MKN_Commune_Guard start_experience_factor = 0.10 start_equipment_factor = 1"
    }
    create_unit = {
        owner = ROOT
        division = "division_template = MKN_Commune_Guard start_experience_factor = 0.10 start_equipment_factor = 1"
    }
}
```

### `MKN_repair_international_content` — `common/scripted_effects/MKN_international_effects.txt`

```pdx
MKN_repair_international_content = {
    if = {
        limit = {
            has_country_flag = MKN_expropriation_factories_active
            has_idea = MKN_expropriated_funds
            NOT = {
                has_variable = MKN_expropriation_factories
            }
        }
        set_variable = {
            MKN_expropriation_factories = 2
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_black_guard_veterans
            NOT = {
                has_completed_focus = MKN_memory_of_atamansha_marusya
            }
        }
        complete_national_focus = MKN_memory_of_atamansha_marusya
        nww_mkn_rebuild_services = yes
    }
    if = {
        limit = {
            has_completed_focus = MKN_memory_of_atamansha_marusya
            NOT = {
                has_idea = MKN_marusyas_legacy
            }
        }
        add_ideas = MKN_marusyas_legacy
    }
    if = {
        limit = {
            has_idea = MKN_marusyas_legacy
            NOT = {
                has_tech = MKN_marusya_assault_training
            }
        }
        set_technology = {
            MKN_marusya_assault_training = 1
        }
    }
    if = {
        limit = {
            has_country_flag = MKN_expropriation_factories_active
            NOT = {
                has_idea = MKN_expropriated_funds
            }
        }
        MKN_clear_expropriation_factories = yes
    }
    if = {
        limit = {
            has_country_flag = MKN_spartacist_factory_active
            NOT = {
                has_idea = MKN_spartacist_engineers
            }
        }
        add_offsite_building = {
            type = arms_factory
            level = -1
        }
        clr_country_flag = MKN_spartacist_factory_active
    }
}
```

### `MKN_repair_succession_crisis` — `common/scripted_effects/MKN_effects.txt`

```pdx
MKN_repair_succession_crisis = {
    if = {
        limit = {
            NOT = {
                has_country_flag = MKN_crisis_enabled
            }
        }
        set_country_flag = MKN_crisis_legacy_settled
    }
    if = {
        limit = {
            has_country_flag = MKN_crisis_enabled
            NOT = {
                has_country_flag = MKN_collapse_started
            }
            OR = {
                has_completed_focus = MKN_arrest_demagogues
                has_completed_focus = MKN_pact_of_free_communes
                has_completed_focus = MKN_grain_ultimatum
                has_completed_focus = MKN_purge_irreconcilables
            }
        }
        if = {
            limit = {
                NOT = {
                    has_country_flag = MKN_crisis_settled
                }
            }
            MKN_resolve_succession_crisis = yes
        }
    }
    if = {
        limit = {
            has_country_flag = MKN_crisis_enabled
            date > 1938.1.30
            NOT = {
                has_country_flag = mkn_batko_departed
            }
        }
        country_event = {
            id = mkn_crisis.1
        }
    }
    if = {
        limit = {
            NOT = {
                has_country_flag = MKN_political_reconstruction_v1
            }
        }
        nww_mkn_rebuild_industry = yes
        nww_mkn_rebuild_services = yes
        set_country_flag = MKN_political_reconstruction_v1
    }
    if = {
        limit = {
            OR = {
                NOT = {
                    SOV = {
                        exists = yes
                        has_government = communism
                        is_subject = no
                    }
                }
                NOT = {
                    has_government = communism
                }
                is_subject = yes
                has_war_with = SOV
            }
        }
        clr_country_flag = MKN_soviet_front_pending
        clr_country_flag = MKN_plenum_pending
    }
}
```

### `MKN_resolve_succession_crisis` — `common/scripted_effects/MKN_effects.txt`

```pdx
MKN_resolve_succession_crisis = {
    set_country_flag = MKN_crisis_settled
    clr_country_flag = MKN_crisis_active
    remove_mission = MKN_civil_war_timer_mission
}
```

### `MKN_ukraine_integration_ready` — `common/scripted_triggers/MKN_ukraine_integration_triggers.txt`

```pdx
MKN_ukraine_integration_ready = {
    MKN_owns_ukrainian_homeland = yes
    NOT = {
        UKR = {
            exists = yes
        }
    }
    has_capitulated = no
    has_war = no
}
```

### `nww_mkn_initialize_bop` — `common/scripted_effects/MKN_bop_effects.txt`

```pdx
nww_mkn_initialize_bop = {
    if = {
        limit = {
            has_country_flag = MKN_crisis_enabled
        }
        if = {
            limit = {
                OR = {
                    has_completed_focus = MKN_abolish_election_of_commanders
                    has_completed_focus = MKN_sever_urban_ties
                    has_completed_focus = MKN_embassy_to_kharkov
                    has_country_flag = MKN_collapse_started
                }
            }
            set_country_flag = MKN_bop_abandoned
            if = {
                limit = {
                    has_power_balance = {
                        id = MKN_power_balance
                    }
                }
                remove_power_balance = {
                    id = MKN_power_balance
                }
            }
        }
        else_if = {
            limit = {
                has_completed_focus = MKN_abolish_general_staff
            }
            set_country_flag = MKN_bop_locked
            if = {
                limit = {
                    NOT = {
                        power_balance_value = {
                            id = MKN_power_balance
                            value = 1
                        }
                    }
                }
                set_power_balance = {
                    id = MKN_power_balance
                    set_value = 1
                }
            }
        }
        else_if = {
            limit = {
                has_completed_focus = MKN_congress_1936
                NOT = {
                    has_country_flag = MKN_bop_abandoned
                }
                NOT = {
                    has_power_balance = {
                        id = MKN_power_balance
                    }
                }
            }
            set_power_balance = {
                id = MKN_power_balance
                set_value = 0
            }
        }
    }
    else_if = {
        limit = {
            has_completed_focus = MKN_nestor_the_first
        }
        if = {
            limit = {
                has_power_balance = {
                    id = MKN_power_balance
                }
            }
            remove_power_balance = {
                id = MKN_power_balance
            }
        }
        set_country_flag = MKN_bop_abandoned
    }
    else_if = {
        limit = {
            NOT = {
                has_country_flag = MKN_bop_abandoned
            }
            NOT = {
                has_power_balance = {
                    id = MKN_power_balance
                }
            }
        }
        set_power_balance = {
            id = MKN_power_balance
            set_value = 0
        }
        if = {
            limit = {
                has_completed_focus = MKN_black_hundreds
            }
            set_power_balance = {
                id = MKN_power_balance
                set_value = -0.65
            }
        }
        else_if = {
            limit = {
                OR = {
                    has_completed_focus = MKN_constituent_assembly
                    has_completed_focus = MKN_everlasting_makhnovshchina
                    has_completed_focus = MKN_council_communism
                }
            }
            set_power_balance = {
                id = MKN_power_balance
                set_value = 0.65
            }
        }
        else_if = {
            limit = {
                has_completed_focus = MKN_red_banner_steppe
            }
            set_power_balance = {
                id = MKN_power_balance
                set_value = 0.35
            }
        }
    }
}
```

### `MKN_owns_ukrainian_homeland` — `common/scripted_triggers/MKN_ukraine_integration_triggers.txt`

```pdx
MKN_owns_ukrainian_homeland = {
    tag = MKN
    192 = {
        is_owned_and_controlled_by = MKN
    }
    193 = {
        is_owned_and_controlled_by = MKN
    }
    197 = {
        is_owned_and_controlled_by = MKN
    }
    198 = {
        is_owned_and_controlled_by = MKN
    }
    199 = {
        is_owned_and_controlled_by = MKN
    }
    201 = {
        is_owned_and_controlled_by = MKN
    }
    202 = {
        is_owned_and_controlled_by = MKN
    }
    203 = {
        is_owned_and_controlled_by = MKN
    }
    225 = {
        is_owned_and_controlled_by = MKN
    }
    259 = {
        is_owned_and_controlled_by = MKN
    }
    834 = {
        is_owned_and_controlled_by = MKN
    }
}
```

## Структура программ и примечания к переработке

### `docs/MKN_military_programs.json`

```json
[
  {
    "service": "army",
    "entry": "MKN_motorized_vanguard",
    "finale": "MKN_mechanized_compact",
    "focuses": [
      "MKN_motorized_vanguard",
      "MKN_armored_trains_and_repair_focus",
      "MKN_communal_fire_support_focus",
      "MKN_combined_arms_command_focus",
      "MKN_mechanized_compact"
    ],
    "core": [
      "MKN_motorized_vanguard",
      "MKN_armored_trains_and_repair_focus",
      "MKN_communal_fire_support_focus",
      "MKN_combined_arms_command_focus",
      "MKN_mechanized_compact"
    ],
    "optional": [],
    "tactics": [
      "MKN_tactic_motorized_infantry",
      "MKN_tactic_fuel_discipline",
      "MKN_tactic_mobile_medical",
      "MKN_tactic_armoured_manoeuvres"
    ]
  },
  {
    "service": "army",
    "entry": "MKN_steppe_horde",
    "finale": "MKN_free_army_compact",
    "focuses": [
      "MKN_steppe_horde",
      "MKN_hidden_supply_bases_focus",
      "MKN_free_column_command_focus",
      "MKN_free_army_compact"
    ],
    "core": [
      "MKN_steppe_horde",
      "MKN_hidden_supply_bases_focus",
      "MKN_free_column_command_focus",
      "MKN_free_army_compact"
    ],
    "optional": [],
    "tactics": [
      "MKN_tactic_night_marches",
      "MKN_tactic_steppe_camouflage",
      "MKN_tactic_militia_engineers",
      "MKN_tactic_flexible_orders",
      "MKN_tactic_tachanka_tactics",
      "MKN_tactic_free_column_exercises"
    ]
  },
  {
    "service": "air",
    "entry": "MKN_interceptor_cooperatives",
    "finale": "MKN_free_sky_compact",
    "focuses": [
      "MKN_interceptor_cooperatives",
      "MKN_communal_aa_defense_focus",
      "MKN_airframe_standardization_focus",
      "MKN_free_sky_compact"
    ],
    "core": [
      "MKN_interceptor_cooperatives",
      "MKN_communal_aa_defense_focus",
      "MKN_airframe_standardization_focus",
      "MKN_free_sky_compact"
    ],
    "optional": [],
    "tactics": [
      "MKN_tactic_air_dispersal",
      "MKN_tactic_night_interceptors",
      "MKN_tactic_fighter_conversion",
      "MKN_tactic_air_rescue",
      "MKN_tactic_sky_watch_exercises"
    ]
  },
  {
    "service": "air",
    "entry": "MKN_flying_artillery_focus",
    "finale": "MKN_air_support_compact",
    "focuses": [
      "MKN_flying_artillery_focus",
      "MKN_forward_airstrips_focus",
      "MKN_air_ground_coordination_focus",
      "MKN_cas_workshop_network_focus",
      "MKN_air_support_compact"
    ],
    "core": [
      "MKN_flying_artillery_focus",
      "MKN_forward_airstrips_focus",
      "MKN_air_ground_coordination_focus",
      "MKN_cas_workshop_network_focus",
      "MKN_air_support_compact"
    ],
    "optional": [],
    "tactics": [
      "MKN_tactic_tactical_recon",
      "MKN_tactic_air_supply_lift",
      "MKN_tactic_replacement_crews",
      "MKN_tactic_weather_service",
      "MKN_tactic_joint_target_planning"
    ]
  },
  {
    "service": "navy",
    "entry": "MKN_sea_escort_service",
    "finale": "MKN_escort_compact",
    "focuses": [
      "MKN_sea_escort_service",
      "MKN_coastal_fortifications_focus",
      "MKN_escort_repair_network_focus",
      "MKN_escort_compact"
    ],
    "core": [
      "MKN_sea_escort_service",
      "MKN_coastal_fortifications_focus",
      "MKN_escort_repair_network_focus",
      "MKN_escort_compact"
    ],
    "optional": [],
    "tactics": [
      "MKN_tactic_damage_control",
      "MKN_tactic_sweeper_sections",
      "MKN_tactic_coastal_depots",
      "MKN_tactic_convoy_rescue",
      "MKN_tactic_coastal_fleet_exercises"
    ]
  },
  {
    "service": "navy",
    "entry": "MKN_torpedo_artels_focus",
    "finale": "MKN_raider_compact",
    "focuses": [
      "MKN_torpedo_artels_focus",
      "MKN_hidden_smuggler_bases_focus",
      "MKN_raider_compact"
    ],
    "core": [
      "MKN_torpedo_artels_focus",
      "MKN_hidden_smuggler_bases_focus",
      "MKN_raider_compact"
    ],
    "optional": [],
    "tactics": [
      "MKN_tactic_submarine_listening",
      "MKN_tactic_radio_discipline",
      "MKN_tactic_raider_weather",
      "MKN_tactic_torpedo_ambushes",
      "MKN_tactic_raider_escape_routes"
    ]
  }
]
```

### `docs/MKN_military_refactor.md`

```text
# MKN: военные программы и полевые штабы

130 военных фокусов заменены 30 фокусами: 12 армейских (включая память Маруси и батальоны Чёрной гвардии), 10 авиационных и 8 морских. Стоимость — 35 или 70 дней. Политические программы, монарх Махно, награды Маруси и её требования к технологиям сохранены.

## 1. Фокусы

Рабочие определения находятся в [`common/national_focus/MKN.txt`](../common/national_focus/MKN.txt). [Схема всего дерева](mkn_focus_tree.svg) построена из текущих координат и предпосылок. Армейские программы расходятся на столбцы 46/54, авиационные — 62/70, морские — 78/86. Два фокуса Маруси остаются в общем армейском стволе, на столбце 50. Военные ветки занимают ряды 0–6; непрерывные фокусы остаются на `y = 3400`, ниже всего дерева.

| Программа | Корень | Институты после корня | Минимальное время с корнем |
| --- | --- | --- | --- |
| Вольные колонны | `MKN_steppe_general_staff` | Орда → схроны → связь → вольная армия | 280 дней |
| Механизация | `MKN_steppe_general_staff` | Авангард → ремонтные базы → огневая поддержка → общевойсковой штаб → механизированная армия | 385 дней |
| Перехват | `MKN_steppe_hawks_and_schools` | Кооперативы → ПВО → стандарты мастерских → свободное небо | 315 дней |
| Штурмовая авиация | `MKN_steppe_hawks_and_schools` | Летающая артиллерия → полосы → карты → мастерские → воздушная поддержка | 315 дней |
| Эскорт | `MKN_black_sea_flotilla_and_yards` | Эскортная служба → укрепления → ремонтные артели → хлебные конвои | 315 дней |
| Рейдеры | `MKN_black_sea_flotilla_and_yards` | Торпедные артели → тайные базы → вольные рейдеры | 280 дней |

Взаимоисключения стоят у входов в программы. Морское направление сохраняет требование владения и контроля Херсона. Советники, предприятия, не-AAT конструкторы и MIO ссылаются на новые институты; индивидуальные исторические отметки сохраняют доступность предприятий в частично пройденных старых сохранениях. Шаблонные MIO-трейты сохранены, все MKN MIO и эффекты их развития проверяют Arms Against Tyranny.

Суммы исходных постоянных бонусов сохранены между фокусами и тактиками. Опыт, техника, строительство, исследовательские и доктринальные скидки, мастерство и размеры MIO из дополнительных фокусов перенесены в финалы соответствующих программ. Тактические решения выдают только постоянные параметры духа.

По дополнению пользователя финалы армии получили умеренное дополнительное усиление:

| Финал | Дополнительные параметры сверх исходных наград |
| --- | --- |
| `MKN_free_army_compact` | −10 п.п. расхода снабжения; +5 п.п. атаки кавалерии |
| `MKN_mechanized_compact` | +10 п.п. прорыва; +5 п.п. атаки бронетехники |

После всех военных улучшений соответствующего пути армейский дух вольных колонн даёт −28% расхода снабжения и +25% атаки кавалерии; механизированный путь даёт +25% атаки бронетехники и +10% прорыва. Эти значения не включают отдельные политические, экономические и командирские бонусы. Усиления финалов применяются и к уже завершившим их старым сохранениям.

## 2. Решения и проекты

Категории: [`MKN_military_categories.txt`](../common/decisions/categories/MKN_military_categories.txt). Решения: [`MKN_military_decisions.txt`](../common/decisions/MKN_military_decisions.txt). Названия и описания доступны на русском и английском.

У исходного дерева было 59 дополнительных фокусов. Они объединены в 30 тактик, по 10 на род войск; прежние основные «Ночные переходы» также перенесены в армейский штаб. Все исходные постоянные бонусы учитываются ровно один раз. Выбор программы открывает её тактики; противоположная программа остаётся недоступной.

Каждая тактика стоит ровно **20 опыта своего рода войск и 10 CP**, покупается один раз, усиливает соответствующий общий дух сразу и исчезает через один день. Решение сохраняет собственный флаг приобретения. Опыт и CP не возвращаются в качестве награды тактики.

Каждый из девяти типов проектов доступен **один раз за кампанию, в одном выбранном регионе**, включая отменённые проекты. Все имеют `fire_only_once = yes`, постоянную отметку начала и проверки полного владения/контроля. Одновременно выполняется один военный проект. Строительство выдаётся только в конце срока. Отмена, потеря региона, капитуляция или исчезновение необходимых условий возвращают PP/CP, освобождают фабрики и закрывают этот тип проекта. Условия повторно проверяются непосредственно перед строительством.

| Проект | Открывающий фокус | Цена | Срок | Результат и ограничения |
| --- | --- | --- | --- | --- |
| Скрытый узел снабжения | Схроны и базы снабжения | 50 PP | 30 дней | Один узел в одной провинции региона без узлов |
| Укладка рельс к фронту | Бронепоезда и ремонтные базы | 20 CP | 15 дней | Новая линия уровня 1 от столицы; существующее сообщение исключено; путь только через нашу территорию |
| Ремонт инфраструктуры | Бронепоезда и ремонтные базы | 20 CP | 7 дней | Восстановление повреждённой инфраструктуры, без добавления уровней |
| Наблюдательные посты | Эшелонированное ПВО коммун | 2 гражданские фабрики | 45 дней | Первый радар; обязательно исследование `radio_detection` |
| Зенитные батареи | Эшелонированное ПВО коммун | 2 гражданские фабрики | 45 дней | +1 ПВО, ниже предела 5 |
| Степной аэродром | Передовые посадочные полосы | 30 PP | 15 дней | +1 авиабаза, ниже предела 10; соседний регион контролирует противник |
| Береговая батарея | Береговые укрепления | 50 PP | 45 дней | +1 береговое укрепление в одной прибрежной провинции |
| Скрытая бухта | Тайные базы контрабандистов | 30 PP | 30 дней | +1 морская база в одной прибрежной провинции |
| Схрон топлива | Тайные базы контрабандистов | 30 PP и 2 гражданские фабрики | 30 дней | +1 топливохранилище при наличии места |

Для радара и ПВО фабрики заняты только на время проекта. Требование исследования радара проверяется при начале и в течение работы. Провинциальные стройки используют селектор одной провинции; морская база и укрепление ограничены побережьем. Железнодорожный проект создаёт новое сообщение первого уровня; повышение существующих линий выполняется обычным строительством.

## 3. Восстановление переменных

[`nww_mkn_progression.txt`](../common/scripted_effects/nww_mkn_progression.txt) содержит `nww_mkn_rebuild_services` и однократный импорт `MKN_migrate_military_hq`.

- Импорт читает только реально завершённые прежние фокусы и сохраняет индивидуальные отметки постоянных параметров и уже выданных разовых наград.
- Восстановление обнуляет параметры трёх военных духов, затем складывает завершённые новые программы, флаги тактик, частично заработанные исторические параметры и политические бонусы. Отдельно учитываются умеренные усиления финалов.
- Повторный вызов не складывает бонусы поверх прежних значений и не выдаёт технику, опыт, здания, MIO, мастерство или другие разовые награды.
- Новый укрупнённый фокус выдаёт только недостающие части своих наград. Полностью заработанные институты имеют явные условия `bypass`, без повторной выдачи наград.
- Прежние токены зарегистрированы как скрытые `shared_focus` в [`MKN_legacy_focus_compatibility.txt`](../common/national_focus/MKN_legacy_focus_compatibility.txt), без импорта в игровое дерево и без наград. Совместимость собирается только из непосредственных определений фокусов.
- Startup и ежедневный callback используют версию `MKN_services_redesign_v5`. Память Маруси и подготовка Чёрной гвардии не пересоздаются восстановлением.

Полный исходный снимок наград, распределение каждого старого ID и точные новые усиления: [`MKN_military_refactor.json`](MKN_military_refactor.json). Текущие игровые маршруты: [`MKN_military_programs.json`](MKN_military_programs.json).

## Проверенные примеры установленной игры

Использована локальная установка `/home/dima00138/.local/share/Steam/steamapps/common/Hearts of Iron IV`:

- `common/national_focus/finland.txt`: фокусы Arms Against Tyranny, `mio:`/`add_mio_size`/`unlock_mio_trait_tooltip`; выбор прибрежных провинций для укреплений; явные провинциальные узлы снабжения и железные дороги.
- `common/decisions/FIN.txt`, `FIN_prepare_motti_tactics_in_state`: `state_target`, `target_array`, выбранный регион в `FROM`, custom CP cost, отложенный `remove_effect` и отмена при потере контроля.
- `common/decisions/RAJ_GOE.txt`: целевые регионы, `target_root_trigger`, государственный scope `target_trigger` с переходом в `FROM`, режим отображения на карте.
- `common/decisions/SIA.txt`, `SIA_develop_phibunsongkhram`: одноразовый проект, резервирование двух гражданских фабрик и проверка доступных фабрик.
- `common/decisions/PHI.txt`, `PHI_investment_plan_1`: `has_railway_connection` между регионами с передачей scope через `PREV`.
- `common/technologies/electronic_mechanical_engineering.txt`: `radio_detection` открывает первый уровень `radar_station`; предпосылку самого исследования задаёт установленная игра.
- `common/buildings/00_buildings.txt`: реальные названия построек, пределы и провинциальная природа узлов снабжения, портов и укреплений.
- `documentation/effects_documentation.md`, `triggers_documentation.md`, `dynamic_variables_documentation.md`, `modifiers_documentation.md`: `build_railway`, `can_build_railway`, `damage_building`, `damaged_building_level@infrastructure`, опыт, CP и параметры динамических духов.

## Валидация

`tools/validate_mkn_military.py` исполняет фактические скрипты восстановления, наград и проектов в ограниченной модели. Покрыты 263 исторических состояния, частично завершённые укрупнённые институты, восемь сочетаний программ с AAT и без него, сохранность разовых наград, точные пороги 20 XP/10 CP, одноразовость, сериализация проектов, контроль регионов, возврат средств, технологический запрет радара и строительные ограничения.

Общая проверка контента теперь вызывает этот валидатор вместо прежнего контракта «десять основных плюс дополнительные фокусы». Проверки украинских фокусов и миграции сохранены.

Предписанная Windows-команда `python tools/validate_country_content.py --game "D:/Steam/steamapps/common/Hearts of Iron IV"` была выполнена; такого каталога на этой Linux-машине нет. Проверки запущены с реальным локальным путём игры:

```bash
python tools/validate_country_content.py --game "/home/dima00138/.local/share/Steam/steamapps/common/Hearts of Iron IV"
python tools/validate_mkn_military.py --game "/home/dima00138/.local/share/Steam/steamapps/common/Hearts of Iron IV"
python tools/validate_mkn_overhaul.py --game "/home/dima00138/.local/share/Steam/steamapps/common/Hearts of Iron IV"
git diff --check
```

Статическая модель не воспроизводит движок: нужна новая кампания и свежий `error.log`, особенно для выбора провинций, железнодорожного поиска пути, ремонта, отображения подсказок и загрузки реального старого сохранения. Подтверждение исправленного runtime-сбоя не заявляется.
```

## Локализация подсказок, духов и решений

```json
{
  "MKN": {
    "ru": "Махновцы",
    "en": "Makhnovists"
  },
  "MKN_Commune_Guard": {
    "ru": "Коммунальная гвардия",
    "en": "Commune Guard"
  },
  "MKN_EMPEROR_DESC": {
    "ru": "Милостью тачанки — император Степи.",
    "en": "By the grace of tachanka, Emperor of the Steppe."
  },
  "MKN_NESTOR_MAKHNO_DESC": {
    "ru": "Атаман Революционной повстанческой армии Украины.",
    "en": "Ataman of the Revolutionary Insurgent Army of Ukraine."
  },
  "MKN_VOLIN_DESC": {
    "ru": "Теоретик вольных советов и вольных выборов.",
    "en": "Theorist of free soviets and free elections."
  },
  "MKN_accountable_militias": {
    "ru": "Ответственные командиры ополчения",
    "en": "Accountable Militia Commanders"
  },
  "MKN_advisor_agronomist": {
    "ru": "Мария Гордиенко",
    "en": "Maria Hordiienko"
  },
  "MKN_advisor_anti_statist_theorist": {
    "ru": "Марк Мрачный",
    "en": "Mark Mratchnyi"
  },
  "MKN_advisor_arsenal_coordinator": {
    "ru": "Григорий Васильковский",
    "en": "Hryhorii Vasylivskyi"
  },
  "MKN_advisor_commune_secretary": {
    "ru": "Пётр Аршинов",
    "en": "Petro Arshinov"
  },
  "MKN_advisor_cooperative_treasurer": {
    "ru": "Аарон Барон",
    "en": "Aaron Baron"
  },
  "MKN_advisor_education_delegate": {
    "ru": "Всеволод Волин",
    "en": "Vsevolod Volin"
  },
  "MKN_advisor_free_press_editor": {
    "ru": "Анатолий Горелик",
    "en": "Anatolii Horelik"
  },
  "MKN_advisor_frontline_delegate": {
    "ru": "Алексей Марченко",
    "en": "Oleksii Marchenko"
  },
  "MKN_advisor_grain_distributor": {
    "ru": "Федот Козубенко",
    "en": "Fedot Kozubenko"
  },
  "MKN_advisor_industrial_organizer": {
    "ru": "Осип Цебрий",
    "en": "Osyp Tsebriy"
  },
  "MKN_advisor_labor_delegate": {
    "ru": "Елена Коваленко",
    "en": "Olena Kovalenko"
  },
  "MKN_advisor_literacy_organizer": {
    "ru": "Ольга Таратута",
    "en": "Olha Taratuta"
  },
  "MKN_advisor_market_keeper": {
    "ru": "Иван Сытник",
    "en": "Ivan Sytnyk"
  },
  "MKN_advisor_military_orator": {
    "ru": "Михаил Калашников",
    "en": "Mykhailo Kalashnykov"
  },
  "MKN_advisor_militia_delegate": {
    "ru": "Степан Ткаченко",
    "en": "Stepan Tkachenko"
  },
  "MKN_advisor_rail_dispatcher": {
    "ru": "Даниил Бондаренко",
    "en": "Danylo Bondarenko"
  },
  "MKN_advisor_recruiting_commissar": {
    "ru": "Пётр Гавриленко",
    "en": "Petro Havrylenko"
  },
  "MKN_advisor_rural_defender": {
    "ru": "Анна Кравченко",
    "en": "Hanna Kravchenko"
  },
  "MKN_advisor_syndicalist_theorist": {
    "ru": "Андрей Романенко",
    "en": "Andrii Romanenko"
  },
  "MKN_advisor_union_secretary": {
    "ru": "Екатерина Мельник",
    "en": "Kateryna Melnyk"
  },
  "MKN_advisor_veterans_organizer": {
    "ru": "Иван Лютый",
    "en": "Ivan Liutyi"
  },
  "MKN_advisor_village_mediator": {
    "ru": "Михаил Петренко",
    "en": "Mykhailo Petrenko"
  },
  "MKN_advisor_weapons_broker": {
    "ru": "Семён Каретник",
    "en": "Semen Karetnyk"
  },
  "MKN_advisor_workshop_engineer": {
    "ru": "Николай Савченко",
    "en": "Mykola Savchenko"
  },
  "MKN_air_air_accidents_factor_tt": {
    "ru": "$air_accidents_factor_tt$",
    "en": "$air_accidents_factor_tt$"
  },
  "MKN_air_air_ace_generation_chance_factor_tt": {
    "ru": "$air_ace_generation_chance_factor_tt$",
    "en": "$air_ace_generation_chance_factor_tt$"
  },
  "MKN_air_air_agility_factor_tt": {
    "ru": "$air_agility_factor_tt$",
    "en": "$air_agility_factor_tt$"
  },
  "MKN_air_air_attack_factor_tt": {
    "ru": "$air_attack_factor_tt$",
    "en": "$air_attack_factor_tt$"
  },
  "MKN_air_air_cas_efficiency_tt": {
    "ru": "$air_cas_efficiency_tt$",
    "en": "$air_cas_efficiency_tt$"
  },
  "MKN_air_air_fuel_consumption_factor_tt": {
    "ru": "$air_fuel_consumption_factor_tt$",
    "en": "$air_fuel_consumption_factor_tt$"
  },
  "MKN_air_air_home_defence_factor_tt": {
    "ru": "$air_home_defence_factor_tt$",
    "en": "$air_home_defence_factor_tt$"
  },
  "MKN_air_air_intercept_efficiency_tt": {
    "ru": "$air_intercept_efficiency_tt$",
    "en": "$air_intercept_efficiency_tt$"
  },
  "MKN_air_air_interception_detect_factor_tt": {
    "ru": "$air_interception_detect_factor_tt$",
    "en": "$air_interception_detect_factor_tt$"
  },
  "MKN_air_air_mission_efficiency_tt": {
    "ru": "$air_mission_efficiency_tt$",
    "en": "$air_mission_efficiency_tt$"
  },
  "MKN_air_air_range_factor_tt": {
    "ru": "$air_range_factor_tt$",
    "en": "$air_range_factor_tt$"
  },
  "MKN_air_artels_company": {
    "ru": "Авиакооператив «Степной сокол»",
    "en": "Steppe Falcon Aviation Cooperative"
  },
  "MKN_air_artels_company_specialization": {
    "ru": "Авиакооператив «Степной сокол»",
    "en": "Steppe Falcon Aviation Cooperative"
  },
  "MKN_air_artels_organization": {
    "ru": "Авиакооператив «Степной сокол»",
    "en": "Steppe Falcon Aviation Cooperative"
  },
  "MKN_air_artels_organization_initial": {
    "ru": "Артельная специализация: Авиакооператив «Степной сокол»",
    "en": "Artel Specialization: Steppe Falcon Aviation Cooperative"
  },
  "MKN_air_artels_organization_mature": {
    "ru": "Согласованное серийное производство",
    "en": "Coordinated Serial Production"
  },
  "MKN_air_artels_organization_specialization_a": {
    "ru": "Манёвренный перехватчик",
    "en": "Agile Interceptor"
  },
  "MKN_air_artels_organization_specialization_b": {
    "ru": "Высотный скоростной истребитель",
    "en": "Fast High Altitude Fighter"
  },
  "MKN_air_coastal_support": {
    "ru": "Поддержка приморского фронта",
    "en": "Coastal Front Support"
  },
  "MKN_air_development": {
    "ru": "Крылья вольной территории",
    "en": "Wings of the Free Territory"
  },
  "MKN_air_development_summary": {
    "ru": "Улучшения авиации накапливаются в одном духе.",
    "en": "Air improvements accumulate in this single spirit."
  },
  "MKN_air_dispersal": {
    "ru": "Рассредоточенные аэродромы",
    "en": "Dispersed Airfields"
  },
  "MKN_air_ground_liaisons": {
    "ru": "Связные при наземных штабах",
    "en": "Air Ground Liaison Officers"
  },
  "MKN_air_home_defence": {
    "ru": "Защита промышленных районов",
    "en": "Industrial Air Defence"
  },
  "MKN_air_hq_decisions": {
    "ru": "Полевые штабы: авиация",
    "en": "Field Headquarters: Air Force"
  },
  "MKN_air_hq_unlock_tt": {
    "ru": "Открывает решения полевого штаба этого рода войск; тактики требуют выбранной военной программы.",
    "en": "Unlocks this service field headquarters; tactics require a chosen military program."
  },
  "MKN_air_map_bureau": {
    "ru": "Общее картографическое бюро",
    "en": "Shared Aerial Mapping Bureau"
  },
  "MKN_air_naval_strike_attack_factor_tt": {
    "ru": "$naval_strike_attack_factor_tt$",
    "en": "$naval_strike_attack_factor_tt$"
  },
  "MKN_air_radar_school": {
    "ru": "Школа радиолокации",
    "en": "Radar School"
  },
  "MKN_air_recon_factor_tt": {
    "ru": "$recon_factor_tt$",
    "en": "$recon_factor_tt$"
  },
  "MKN_air_rescue": {
    "ru": "Спасение сбитых лётчиков",
    "en": "Downed Pilot Rescue"
  },
  "MKN_air_supply_consumption_factor_tt": {
    "ru": "$supply_consumption_factor_tt$",
    "en": "$supply_consumption_factor_tt$"
  },
  "MKN_air_supply_lift": {
    "ru": "Доставка срочных грузов",
    "en": "Urgent Air Deliveries"
  },
  "MKN_air_warning": {
    "ru": "Единая воздушная тревога",
    "en": "Unified Air Warning"
  },
  "MKN_air_weather_service": {
    "ru": "Степная метеослужба",
    "en": "Steppe Weather Service"
  },
  "MKN_aircraft_artels": {
    "ru": "Артели истребителей",
    "en": "Fighter Artels"
  },
  "MKN_aircraft_recovery": {
    "ru": "Возвращать повреждённые машины",
    "en": "Recover Damaged Aircraft"
  },
  "MKN_aircraft_spares": {
    "ru": "Общий запас авиационных деталей",
    "en": "Shared Aircraft Spares"
  },
  "MKN_airfield_fuel": {
    "ru": "Топливные склады эскадрилий",
    "en": "Squadron Fuel Depots"
  },
  "MKN_airframe_jigs": {
    "ru": "Оснастка для лёгких планеров",
    "en": "Light Airframe Jigs"
  },
  "MKN_anarchic_economy_idea": {
    "ru": "Несогласованное хозяйство коммун",
    "en": "Uncoordinated Communal Economy"
  },
  "MKN_anti_submarine_patrols": {
    "ru": "Противолодочные патрули",
    "en": "Anti Submarine Patrols"
  },
  "MKN_armored_train_commander_tt": {
    "ru": "Бронепоезда: §G+20%§! к броне и зенитной атаке, пока советник занимает должность.",
    "en": "Armored trains: §G+20%§! armor and anti-air attack while this advisor serves."
  },
  "MKN_armored_train_staff_bonus": {
    "ru": "Командование бронепоездами",
    "en": "Armored Train Command"
  },
  "MKN_armoured_manoeuvres": {
    "ru": "Манёвры механизированных колонн",
    "en": "Mechanized Column Manoeuvres"
  },
  "MKN_army_army_armor_attack_factor_tt": {
    "ru": "$army_armor_attack_factor_tt$",
    "en": "$army_armor_attack_factor_tt$"
  },
  "MKN_army_army_attack_factor_tt": {
    "ru": "Атака армии: $RIGHT|+=%1$",
    "en": "Army attack: $RIGHT|+=%1$"
  },
  "MKN_army_army_core_defence_factor_tt": {
    "ru": "Защита национальной территории: $RIGHT|+=%1$",
    "en": "Core territory defense: $RIGHT|+=%1$"
  },
  "MKN_army_army_defence_factor_tt": {
    "ru": "Защита армии: $RIGHT|+=%1$",
    "en": "Army defense: $RIGHT|+=%1$"
  },
  "MKN_army_army_fuel_consumption_factor_tt": {
    "ru": "$army_fuel_consumption_factor_tt$",
    "en": "$army_fuel_consumption_factor_tt$"
  },
  "MKN_army_army_org_factor_tt": {
    "ru": "$army_org_factor_tt$",
    "en": "$army_org_factor_tt$"
  },
  "MKN_army_army_speed_factor_tt": {
    "ru": "$army_speed_factor_tt$",
    "en": "$army_speed_factor_tt$"
  },
  "MKN_army_attrition_tt": {
    "ru": "$attrition_tt$",
    "en": "$attrition_tt$"
  },
  "MKN_army_breakthrough_factor_tt": {
    "ru": "Прорыв армии: $RIGHT|+=%1$",
    "en": "Army breakthrough: $RIGHT|+=%1$"
  },
  "MKN_army_casualty_trickleback_tt": {
    "ru": "$casualty_trickleback_tt$",
    "en": "$casualty_trickleback_tt$"
  },
  "MKN_army_conscription_tt": {
    "ru": "Военнообязанное население: §G+2%§!.",
    "en": "Recruitable population: §G+2%§!."
  },
  "MKN_army_development": {
    "ru": "Армия вольной территории",
    "en": "Army of the Free Territory"
  },
  "MKN_army_development_summary": {
    "ru": "Улучшения армии накапливаются в одном духе.",
    "en": "Army improvements accumulate in this single spirit."
  },
  "MKN_army_dig_in_speed_factor_tt": {
    "ru": "$dig_in_speed_factor_tt$",
    "en": "$dig_in_speed_factor_tt$"
  },
  "MKN_army_enemy_army_bonus_air_superiority_factor_tt": {
    "ru": "Преимущество противника от господства в воздухе: $RIGHT|+=%1$",
    "en": "Enemy air superiority advantage: $RIGHT|+=%1$"
  },
  "MKN_army_enemy_attrition_tt": {
    "ru": "Истощение противника: $RIGHT|+=%1$",
    "en": "Hostile attrition: $RIGHT|+=%1$"
  },
  "MKN_army_hq_decisions": {
    "ru": "Полевые штабы: армия",
    "en": "Field Headquarters: Army"
  },
  "MKN_army_hq_unlock_tt": {
    "ru": "Открывает решения полевого штаба этого рода войск; тактики требуют выбранной военной программы.",
    "en": "Unlocks this service field headquarters; tactics require a chosen military program."
  },
  "MKN_army_land_reinforce_rate_tt": {
    "ru": "$land_reinforce_rate_tt$",
    "en": "$land_reinforce_rate_tt$"
  },
  "MKN_army_max_dig_in_tt": {
    "ru": "$max_dig_in_tt$",
    "en": "$max_dig_in_tt$"
  },
  "MKN_army_max_planning_tt": {
    "ru": "$MODIFIER_MAX_PLANNING$: $RIGHT|+=%1$",
    "en": "$MODIFIER_MAX_PLANNING$: $RIGHT|+=%1$"
  },
  "MKN_army_mobilization_speed_tt": {
    "ru": "$mobilization_speed_tt$",
    "en": "$mobilization_speed_tt$"
  },
  "MKN_army_modifier_army_sub_unit_cavalry_attack_factor_tt": {
    "ru": "Атака кавалерии: $RIGHT|+=%1$",
    "en": "Cavalry attack: $RIGHT|+=%1$"
  },
  "MKN_army_modifier_army_sub_unit_cavalry_defence_factor_tt": {
    "ru": "Защита кавалерии: $RIGHT|+=%1$",
    "en": "Cavalry defence: $RIGHT|+=%1$"
  },
  "MKN_army_modifier_army_sub_unit_cavalry_speed_factor_tt": {
    "ru": "$modifier_army_sub_unit_cavalry_speed_factor_tt$",
    "en": "$modifier_army_sub_unit_cavalry_speed_factor_tt$"
  },
  "MKN_army_modifier_army_sub_unit_infantry_attack_factor_tt": {
    "ru": "Атака пехоты: $RIGHT|+=%1$",
    "en": "Infantry attack: $RIGHT|+=%1$"
  },
  "MKN_army_modifier_army_sub_unit_infantry_defence_factor_tt": {
    "ru": "Защита пехоты: $RIGHT|+=%1$",
    "en": "Infantry defence: $RIGHT|+=%1$"
  },
  "MKN_army_modifier_army_sub_unit_infantry_speed_factor_tt": {
    "ru": "Скорость пехоты: $RIGHT|+=%1$",
    "en": "Infantry speed: $RIGHT|+=%1$"
  },
  "MKN_army_motorized_attack_factor_tt": {
    "ru": "Атака моторизованных батальонов: $RIGHT|+=%1$",
    "en": "Motorized battalion attack: $RIGHT|+=%1$"
  },
  "MKN_army_org_loss_when_moving_tt": {
    "ru": "$org_loss_when_moving_tt$",
    "en": "$org_loss_when_moving_tt$"
  },
  "MKN_army_planning_speed_tt": {
    "ru": "$MODIFIER_PLANNING_SPEED$: $RIGHT|+=%1$",
    "en": "$MODIFIER_PLANNING_SPEED$: $RIGHT|+=%1$"
  },
  "MKN_army_recon_factor_tt": {
    "ru": "$recon_factor_tt$",
    "en": "$recon_factor_tt$"
  },
  "MKN_army_repair_speed_factor_tt": {
    "ru": "$repair_speed_factor_tt$",
    "en": "$repair_speed_factor_tt$"
  },
  "MKN_army_resistance_damage_to_garrison_on_our_occupied_states_tt": {
    "ru": "Урон гарнизонам на нашей оккупированной земле: $RIGHT|+=%1$",
    "en": "Garrison damage on our occupied soil: $RIGHT|+=%1$"
  },
  "MKN_army_send_volunteer_size_tt": {
    "ru": "Лимит дивизий добровольцев: $RIGHT|+=0$",
    "en": "Volunteer division limit: $RIGHT|+=0$"
  },
  "MKN_army_send_volunteers_tension_tt": {
    "ru": "Напряжённость для отправки добровольцев: $RIGHT|+=%1$",
    "en": "Tension required for volunteers: $RIGHT|+=%1$"
  },
  "MKN_army_supply_consumption_factor_tt": {
    "ru": "$supply_consumption_factor_tt$",
    "en": "$supply_consumption_factor_tt$"
  },
  "MKN_army_war_support_factor_tt": {
    "ru": "Поддержка войны от армейских учреждений: §G+10%§!",
    "en": "War support from the army institutions: §G+10%§!"
  },
  "MKN_artel_logistics": {
    "ru": "Обозная взаимопомощь",
    "en": "Mutual Aid Supply Trains"
  },
  "MKN_artillery_artels": {
    "ru": "Артиллерийские артели",
    "en": "Artillery Artels"
  },
  "MKN_artillery_works_company": {
    "ru": "Никопольские орудийные мастерские",
    "en": "Nikopol Ordnance Works"
  },
  "MKN_artillery_works_company_specialization": {
    "ru": "Никопольские орудийные мастерские",
    "en": "Nikopol Ordnance Works"
  },
  "MKN_artillery_works_organization": {
    "ru": "Никопольские орудийные мастерские",
    "en": "Nikopol Ordnance Works"
  },
  "MKN_artillery_works_organization_initial": {
    "ru": "Артельная специализация: Никопольские орудийные мастерские",
    "en": "Artel Specialization: Nikopol Ordnance Works"
  },
  "MKN_artillery_works_organization_mature": {
    "ru": "Согласованное серийное производство",
    "en": "Coordinated Serial Production"
  },
  "MKN_artillery_works_organization_specialization_a": {
    "ru": "Лёгкие полевые орудия",
    "en": "Light Field Guns"
  },
  "MKN_artillery_works_organization_specialization_b": {
    "ru": "Мощный огневой налёт",
    "en": "Concentrated Barrage"
  },
  "MKN_attack_air_artels": {
    "ru": "Артели штурмовой авиации",
    "en": "Attack Aircraft Artels"
  },
  "MKN_attack_air_artels_company": {
    "ru": "Авиакооператив «Днепровское крыло»",
    "en": "Dnieper Wing Aviation Cooperative"
  },
  "MKN_attack_air_artels_company_specialization": {
    "ru": "Авиакооператив «Днепровское крыло»",
    "en": "Dnieper Wing Aviation Cooperative"
  },
  "MKN_attack_air_artels_organization": {
    "ru": "Авиакооператив «Днепровское крыло»",
    "en": "Dnieper Wing Aviation Cooperative"
  },
  "MKN_attack_air_artels_organization_initial": {
    "ru": "Артельная специализация: Авиакооператив «Днепровское крыло»",
    "en": "Artel Specialization: Dnieper Wing Aviation Cooperative"
  },
  "MKN_attack_air_artels_organization_mature": {
    "ru": "Согласованное серийное производство",
    "en": "Coordinated Serial Production"
  },
  "MKN_attack_air_artels_organization_specialization_a": {
    "ru": "Бронированный штурмовик",
    "en": "Armoured Attack Aircraft"
  },
  "MKN_attack_air_artels_organization_specialization_b": {
    "ru": "Дальний лёгкий бомбардировщик",
    "en": "Long Range Light Bomber"
  },
  "MKN_attack_wing_rotations": {
    "ru": "Сменяемые ударные группы",
    "en": "Rotating Strike Groups"
  },
  "MKN_autonomous_rail_crews_idea": {
    "ru": "Самоуправляемые железнодорожные бригады",
    "en": "Autonomous Rail Crews"
  },
  "MKN_batko": {
    "ru": "$MKN$",
    "en": "$MKN$"
  },
  "MKN_batko_cavalry": {
    "ru": "Конница Батьки",
    "en": "Batkos Cavalry"
  },
  "MKN_batko_cavalry_idea": {
    "ru": "Конница Батьки",
    "en": "Batko's Cavalry"
  },
  "MKN_betrayed_twice": {
    "ru": "Преданы дважды",
    "en": "Betrayed Twice"
  },
  "MKN_black_guard_veterans": {
    "ru": "Ветераны Чёрной гвардии",
    "en": "Black Guard Veterans"
  },
  "MKN_black_guard_veterans_idea": {
    "ru": "Ветераны Чёрной гвардии",
    "en": "Veterans of the Black Guard"
  },
  "MKN_black_international_decisions_unlock_tt": {
    "ru": "Открывает четыре одноразовых приглашения Чёрного интернационала: испанские анархисты, немецкие инженеры, итальянские механики и кронштадтские моряки.",
    "en": "Unlocks the four one-time Black International invitations: Spanish anarchists, German engineers, Italian mechanics and Kronstadt sailors."
  },
  "MKN_black_sea_escorts": {
    "ru": "Черноморские эскорты",
    "en": "Black Sea Escorts"
  },
  "MKN_black_sea_flotilla": {
    "ru": "Черноморская флотилия",
    "en": "Black Sea Flotilla"
  },
  "MKN_black_sea_smugglers": {
    "ru": "Школа черноморских рейдеров",
    "en": "Black Sea Raider School"
  },
  "MKN_black_swarm": {
    "ru": "Чёрный рой",
    "en": "Black Swarm"
  },
  "MKN_black_swarm_idea": {
    "ru": "Чёрный рой",
    "en": "The Black Swarm"
  },
  "MKN_bomber_navigation": {
    "ru": "Школа штурманов",
    "en": "Navigator School"
  },
  "MKN_bombing_ranges": {
    "ru": "Полигоны точного бомбометания",
    "en": "Precision Bombing Ranges"
  },
  "MKN_bop_abandoned": {
    "ru": "Аграрный съезд упразднил баланс сил",
    "en": "The agrarian congress abolished the balance of power"
  },
  "MKN_bop_locked": {
    "ru": "Вольные советы получили постоянные полномочия",
    "en": "The free soviets hold permanent authority"
  },
  "MKN_border_fury_buff": {
    "ru": "Приграничная ярость",
    "en": "Border Fury"
  },
  "MKN_border_relaxation_debuff": {
    "ru": "Дозоры возвращаются домой",
    "en": "The Patrols Stand Down"
  },
  "MKN_breakthrough_workshops": {
    "ru": "Мастерские прорыва",
    "en": "Breakthrough Workshops"
  },
  "MKN_bridge_columns": {
    "ru": "Мостовые колонны",
    "en": "Bridging Columns"
  },
  "MKN_broken_supply": {
    "ru": "Перебои степного снабжения",
    "en": "Disrupted Steppe Supply"
  },
  "MKN_buenaventura_durruti": {
    "ru": "Буэнавентура Дуррути",
    "en": "Buenaventura Durruti"
  },
  "MKN_careful_investment": {
    "ru": "Бережливое переоснащение",
    "en": "Careful Retooling"
  },
  "MKN_cas_joint_exercises": {
    "ru": "Учения лётчиков и артиллеристов",
    "en": "Pilot and Artillery Exercises"
  },
  "MKN_cas_maintenance": {
    "ru": "Ремонт штурмовиков у фронта",
    "en": "Frontline Attack Aircraft Repair"
  },
  "MKN_cas_replacement_crews": {
    "ru": "Резерв экипажей штурмовиков",
    "en": "Attack Crew Reserve"
  },
  "MKN_catalogued_workshops": {
    "ru": "Учтённые мастерские",
    "en": "Catalogued Workshops"
  },
  "MKN_civil_war_timer_mission": {
    "ru": "Степь на краю пропасти",
    "en": "The Steppe on the Brink"
  },
  "MKN_close_support_program": {
    "ru": "Авиация поддержки",
    "en": "Support Aviation"
  },
  "MKN_coastal_defense_steppe": {
    "ru": "Береговой защитный пояс",
    "en": "Coastal Defence Belt"
  },
  "MKN_coastal_depots": {
    "ru": "Портовые склады снабжения",
    "en": "Port Supply Depots"
  },
  "MKN_coastal_fleet_exercises": {
    "ru": "Учения береговой флотилии",
    "en": "Coastal Flotilla Exercises"
  },
  "MKN_coastal_signal_posts": {
    "ru": "Береговые сигнальные посты",
    "en": "Coastal Signal Posts"
  },
  "MKN_coastal_watch": {
    "ru": "Постоянный береговой дозор",
    "en": "Permanent Coastal Watch"
  },
  "MKN_collapse_started": {
    "ru": "Вольная территория распалась",
    "en": "The Free Territory has collapsed"
  },
  "MKN_combined_arms": {
    "ru": "Единый боевой порядок",
    "en": "Combined Arms Formation"
  },
  "MKN_communal_federation": {
    "ru": "Договор свободных коммун",
    "en": "Compact of Free Communes"
  },
  "MKN_congress_elected_commanders": {
    "ru": "Мандаты отзывных командиров",
    "en": "Mandates for Recallable Commanders"
  },
  "MKN_congress_mutual_insurance": {
    "ru": "Касса взаимного ремонта",
    "en": "Mutual Repair Fund"
  },
  "MKN_construction_drive": {
    "ru": "Напряжённый строительный сезон",
    "en": "Intensive Construction Season"
  },
  "MKN_convoy_rescue": {
    "ru": "Спасательная служба конвоев",
    "en": "Convoy Rescue Service"
  },
  "MKN_convoy_schedules": {
    "ru": "Расписания зерновых конвоев",
    "en": "Grain Convoy Timetables"
  },
  "MKN_cooperative_production": {
    "ru": "Федерация производственных артелей",
    "en": "Federation of Production Artels"
  },
  "MKN_coordinated_supply": {
    "ru": "Налаживающееся снабжение",
    "en": "Supply Taking Shape"
  },
  "MKN_crisis_active": {
    "ru": "Идёт отсчёт срока урегулирования",
    "en": "The succession deadline is running"
  },
  "MKN_crisis_enabled": {
    "ru": "Действует система преемственности 1936 года",
    "en": "The 1936 succession system is active"
  },
  "MKN_crisis_legacy_settled": {
    "ru": "Сохранено прежнее политическое урегулирование",
    "en": "An earlier political settlement is preserved"
  },
  "MKN_crisis_settled": {
    "ru": "Кризис преемственности разрешён",
    "en": "The succession crisis is settled"
  },
  "MKN_cult_of_railways": {
    "ru": "Культ железных дорог",
    "en": "The Cult of Railways"
  },
  "MKN_decaying_batko": {
    "ru": "Угасающий Батько",
    "en": "The Failing Batko"
  },
  "MKN_deep_reserves": {
    "ru": "Резерв второго эшелона",
    "en": "Second Echelon Reserve"
  },
  "MKN_depth_charge_school": {
    "ru": "Школа глубинных бомб",
    "en": "Depth Charge School"
  },
  "MKN_disrupt_enemy_trade": {
    "ru": "Срыв вражеской торговли",
    "en": "Disrupt Enemy Trade"
  },
  "MKN_dmitruk_tratishov": {
    "ru": "Дмитрук Тратишов",
    "en": "Dmitruk Tratishov"
  },
  "MKN_dneprostroi_power": {
    "ru": "Электросеть Днепростроя",
    "en": "Dnieper Power Network"
  },
  "MKN_dnieper_economy": {
    "ru": "Днепровский хозяйственный договор",
    "en": "Dnieper Economic Compact"
  },
  "MKN_dnieper_gun_flotilla": {
    "ru": "Днепровские канонерки",
    "en": "Dnieper Gunboats"
  },
  "MKN_dnieper_logistics": {
    "ru": "Днепровская транспортная служба",
    "en": "Dnieper Transport Service"
  },
  "MKN_dnieper_patrol": {
    "ru": "Днепровский дозор",
    "en": "Dnieper Patrol"
  },
  "MKN_drilled_militias": {
    "ru": "Ополчение на общих учениях",
    "en": "Militias on Joint Exercises"
  },
  "MKN_economic_congress_unlock_tt": {
    "ru": "Открывает решения §Y«Хозяйственного конгресса»§!: соляные артели, отзывные командиры, ветряки, хлебная политика и взаимное страхование.",
    "en": "Unlocks the §YEconomic Congress§!: salt artels, recallable commanders, windmills, grain policy and mutual insurance."
  },
  "MKN_economic_coordination": {
    "ru": "Первые хозяйственные соглашения",
    "en": "First Economic Agreements"
  },
  "MKN_economic_recovery": {
    "ru": "Хозяйство на пути к восстановлению",
    "en": "An Economy in Recovery"
  },
  "MKN_electrified_steppe": {
    "ru": "Электрифицированная степь",
    "en": "The Electrified Steppe"
  },
  "MKN_escort_crews": {
    "ru": "Школа экипажей эскортов",
    "en": "Escort Crew School"
  },
  "MKN_escort_radio_net": {
    "ru": "Радиосеть охранения",
    "en": "Escort Radio Network"
  },
  "MKN_escort_reserves": {
    "ru": "Резерв портовых экипажей",
    "en": "Port Crew Reserve"
  },
  "MKN_eugen_instructor_courses": {
    "ru": "Курсы взаимовыручки Евгена",
    "en": "Eugen’s Mutual Support Courses"
  },
  "MKN_eugen_no_one_left_behind": {
    "ru": "Никого не оставим в окопах",
    "en": "No One Left in the Trenches"
  },
  "MKN_export_contracts": {
    "ru": "Артельные экспортные договоры",
    "en": "Artel Export Contracts"
  },
  "MKN_expropriated_funds": {
    "ru": "Экспроприированные средства",
    "en": "Expropriated Funds"
  },
  "MKN_expropriated_funds_factories_tt": {
    "ru": "Арендованные внекартовые гражданские фабрики: §G+[?MKN_expropriation_factories|0]§!. Все снимаются по истечении срока духа.",
    "en": "Leased off-map civilian factories: §G+[?MKN_expropriation_factories|0]§!. All are removed when this spirit expires."
  },
  "MKN_extra_workshop_shifts": {
    "ru": "Реквизированные смены мастерских",
    "en": "Requisitioned Workshop Shifts"
  },
  "MKN_fascism_successor_desc": {
    "ru": "Дмитрук Тратишов возглавляет анархо-милитаристов Чёрного штаба. Он обещает связать вольные отряды единым командованием, подчинить мастерские фронту и удержать территорию силой. Его власть требует подготовленного съезда и поддержки не менее 40% населения; армейская дисциплина не заменяет политического мандата.",
    "en": "Dmitruk Tratishov leads the Black Staff’s anarcho-militarists. He promises unified command, workshops serving the front and a territory held together by force. His accession requires a prepared congress and at least 40% public support; military discipline cannot replace a political mandate."
  },
  "MKN_fast_attack_craft": {
    "ru": "Быстрые торпедные катера",
    "en": "Fast Torpedo Craft"
  },
  "MKN_federal_republic": {
    "ru": "Федеративная республика",
    "en": "Federal Republic"
  },
  "MKN_field_veterinary": {
    "ru": "Ветеринарная служба колонн",
    "en": "Column Veterinary Service"
  },
  "MKN_fighter_controllers": {
    "ru": "Диспетчеры воздушного боя",
    "en": "Fighter Controllers"
  },
  "MKN_fighter_conversion": {
    "ru": "Переучивание лётчиков",
    "en": "Pilot Conversion Training"
  },
  "MKN_fighter_instructors": {
    "ru": "Инструкторы воздушного боя",
    "en": "Air Combat Instructors"
  },
  "MKN_fighter_patrols": {
    "ru": "Патрули над переправами",
    "en": "Patrols over River Crossings"
  },
  "MKN_fire_tables": {
    "ru": "Общие таблицы огня",
    "en": "Common Fire Tables"
  },
  "MKN_fleet_damage_control": {
    "ru": "Артели аварийного ремонта",
    "en": "Repair and Salvage Artels"
  },
  "MKN_flexible_orders": {
    "ru": "Задача вместо длинного приказа",
    "en": "Mission over Lengthy Orders"
  },
  "MKN_flying_artillery": {
    "ru": "Летающая артиллерия",
    "en": "Flying Artillery"
  },
  "MKN_focus": {
    "ru": "Махновская вольница",
    "en": "Makhnovist Free Territory"
  },
  "MKN_forward_airstrips": {
    "ru": "Передовые посадочные полосы",
    "en": "Forward Airstrips"
  },
  "MKN_fragmented_workshops": {
    "ru": "Разрозненные мастерские",
    "en": "Fragmented Workshops"
  },
  "MKN_free_airmen": {
    "ru": "Вольные лётчики",
    "en": "Free Airmen"
  },
  "MKN_free_column_exercises": {
    "ru": "Сборы вольных колонн",
    "en": "Free Column Exercises"
  },
  "MKN_free_industry_modifier": {
    "ru": "Хозяйство вольной территории",
    "en": "Economy of the Free Territory"
  },
  "MKN_free_mint_idea": {
    "ru": "Свободный монетный двор",
    "en": "Free Mint"
  },
  "MKN_free_soviets_idea": {
    "ru": "Упорядоченные вольные советы",
    "en": "Organized Free Soviets"
  },
  "MKN_free_soviets_side": {
    "ru": "Вольные советы — Волин",
    "en": "Free Soviets — Volin"
  },
  "MKN_free_territory": {
    "ru": "Вольная территория",
    "en": "Free Territory"
  },
  "MKN_free_workshops": {
    "ru": "Вольные мастерские",
    "en": "Free Workshops"
  },
  "MKN_free_workshops_initial_trait": {
    "ru": "Федерация вольных мастерских",
    "en": "Federation of Free Workshops"
  },
  "MKN_fuel_discipline": {
    "ru": "Учёт горючего в походе",
    "en": "Fuel Accounting on Campaign"
  },
  "MKN_grain_projects_unlock_tt": {
    "ru": "Открывает три §Y60-дневных проекта на карте§!: элеваторы (226), херсонские терминалы (196), посевная (1082).",
    "en": "Unlocks three §Y60-day map projects§!: elevators (226), Kherson terminals (196), steppe sowing (1082)."
  },
  "MKN_gulyaipole_pilot_school": {
    "ru": "Гуляйпольская школа лётчиков",
    "en": "Gulyai Polye Pilot School"
  },
  "MKN_harbour_dredging": {
    "ru": "Расчистка портовых фарватеров",
    "en": "Harbour Channel Dredging"
  },
  "MKN_hidden_anchorages": {
    "ru": "Скрытые рейдерские стоянки",
    "en": "Hidden Raider Anchorages"
  },
  "MKN_hidden_depots": {
    "ru": "Скрытые сельские склады",
    "en": "Hidden Village Depots"
  },
  "MKN_hq_20_cp_cost": {
    "ru": "£command_power §Y20§!",
    "en": "£command_power §Y20§!"
  },
  "MKN_hq_air_cost": {
    "ru": "£air_experience §Y20§!  £command_power §Y10§!",
    "en": "£air_experience §Y20§!  £command_power §Y10§!"
  },
  "MKN_hq_army_cost": {
    "ru": "£army_experience §Y20§!  £command_power §Y10§!",
    "en": "£army_experience §Y20§!  £command_power §Y10§!"
  },
  "MKN_hq_navy_cost": {
    "ru": "£navy_experience §Y20§!  £command_power §Y10§!",
    "en": "£navy_experience §Y20§!  £command_power §Y10§!"
  },
  "MKN_hull_repair_artels": {
    "ru": "Артели судового ремонта",
    "en": "Hull Repair Artels"
  },
  "MKN_imperial_administration": {
    "ru": "Степная администрация",
    "en": "Steppe Administration"
  },
  "MKN_industry_concern_1": {
    "ru": "Концерн «Вольная сталь»",
    "en": "Concern of Free Steel"
  },
  "MKN_industry_concern_2": {
    "ru": "Концерн «Вольная сталь»",
    "en": "Concern of Free Steel"
  },
  "MKN_interceptor_pairs": {
    "ru": "Перехват парами",
    "en": "Paired Interception"
  },
  "MKN_joint_target_planning": {
    "ru": "Совместное планирование ударов",
    "en": "Joint Strike Planning"
  },
  "MKN_kherson_shipyard": {
    "ru": "Херсонские верфи",
    "en": "Kherson Shipyards"
  },
  "MKN_kherson_works_company": {
    "ru": "Херсонская артель судостроителей",
    "en": "Kherson Shipwright Artel"
  },
  "MKN_kherson_works_company_specialization": {
    "ru": "Херсонская артель судостроителей",
    "en": "Kherson Shipwright Artel"
  },
  "MKN_kherson_works_organization": {
    "ru": "Херсонская артель судостроителей",
    "en": "Kherson Shipwright Artel"
  },
  "MKN_kherson_works_organization_initial": {
    "ru": "Артельная специализация: Херсонская артель судостроителей",
    "en": "Artel Specialization: Kherson Shipwright Artel"
  },
  "MKN_kherson_works_organization_mature": {
    "ru": "Согласованное серийное производство",
    "en": "Coordinated Serial Production"
  },
  "MKN_kherson_works_organization_specialization_a": {
    "ru": "Противолодочный эскорт",
    "en": "Anti Submarine Escort"
  },
  "MKN_kherson_works_organization_specialization_b": {
    "ru": "Быстрый охранный корабль",
    "en": "Fast Escort Vessel"
  },
  "MKN_kommunar_company": {
    "ru": "«Коммунар»: бронетракторные мастерские",
    "en": "Kommunar Armour and Tractor Works"
  },
  "MKN_kommunar_company_specialization": {
    "ru": "«Коммунар»: бронетракторные мастерские",
    "en": "Kommunar Armour and Tractor Works"
  },
  "MKN_kommunar_organization": {
    "ru": "«Коммунар»: бронетракторные мастерские",
    "en": "Kommunar Armour and Tractor Works"
  },
  "MKN_kommunar_organization_initial": {
    "ru": "Артельная специализация: «Коммунар»: бронетракторные мастерские",
    "en": "Artel Specialization: Kommunar Armour and Tractor Works"
  },
  "MKN_kommunar_organization_mature": {
    "ru": "Согласованное серийное производство",
    "en": "Coordinated Serial Production"
  },
  "MKN_kommunar_organization_specialization_a": {
    "ru": "Лёгкая ремонтопригодная броня",
    "en": "Repairable Light Armour"
  },
  "MKN_kommunar_organization_specialization_b": {
    "ru": "Защита экипажа",
    "en": "Crew Protection"
  },
  "MKN_local_guides": {
    "ru": "Проводники родной степи",
    "en": "Native Steppe Guides"
  },
  "MKN_local_reserves": {
    "ru": "Местные страховые запасы",
    "en": "Local Insurance Reserves"
  },
  "MKN_machinegun_carts": {
    "ru": "Пулемётные повозки",
    "en": "Machine Gun Carts"
  },
  "MKN_mapped_supply": {
    "ru": "Согласованные маршруты",
    "en": "Agreed Supply Routes"
  },
  "MKN_marusya_assault_training": {
    "ru": "Городская штурмовая подготовка Маруси",
    "en": "Marusya's Urban Assault Training"
  },
  "MKN_marusya_urban_attack_tt": {
    "ru": "Атака в городе: §G+15%§! для боевых сухопутных батальонов.",
    "en": "Urban attack: §G+15%§! for land combat battalions."
  },
  "MKN_marusyas_legacy": {
    "ru": "Наследие Маруси",
    "en": "Marusya's Legacy"
  },
  "MKN_military_command_side": {
    "ru": "Военный штаб — Тратишов",
    "en": "Military Staff — Tratishov"
  },
  "MKN_military_directory": {
    "ru": "Военная директория",
    "en": "Military Directory"
  },
  "MKN_military_program_progress_tt": {
    "ru": "Развивает постоянный национальный дух соответствующего рода войск.",
    "en": "Develops the permanent national spirit of this service."
  },
  "MKN_military_project_idle_tt": {
    "ru": "Другой военный строительный проект сейчас не выполняется",
    "en": "No other military construction project is currently running"
  },
  "MKN_militia_engineers": {
    "ru": "Сапёрные десятки",
    "en": "Engineer Squads"
  },
  "MKN_militia_hospitals": {
    "ru": "Санитарные артели",
    "en": "Medical Artels"
  },
  "MKN_militia_junior_leaders": {
    "ru": "Выборные младшие командиры",
    "en": "Elected Junior Commanders"
  },
  "MKN_militia_signals": {
    "ru": "Связь между волостями",
    "en": "Inter Village Signals"
  },
  "MKN_mobile_medical": {
    "ru": "Подвижные санитарные пункты",
    "en": "Mobile Medical Posts"
  },
  "MKN_mobile_patrols": {
    "ru": "Тачаночные дозорные колонны",
    "en": "Tachanka Patrol Columns"
  },
  "MKN_mobile_rearguard": {
    "ru": "Подвижный арьергард",
    "en": "Mobile Rearguard"
  },
  "MKN_mobile_self_defence_idea": {
    "ru": "Подвижная самооборона коммун",
    "en": "Mobile Communal Self Defence"
  },
  "MKN_mobile_supply_columns": {
    "ru": "Моторизованные обозы",
    "en": "Motorized Supply Columns"
  },
  "MKN_moscow_request_pending": {
    "ru": "Предложение ожидает ответа Москвы",
    "en": "A proposal is awaiting Moscow's reply"
  },
  "MKN_motorized_infantry": {
    "ru": "Пехота вслед за бронёй",
    "en": "Infantry Behind the Armour"
  },
  "MKN_mutual_aid_economy": {
    "ru": "Хозяйство взаимопомощи",
    "en": "Mutual Aid Economy"
  },
  "MKN_naval_intelligence": {
    "ru": "Карты торговых маршрутов",
    "en": "Merchant Route Charts"
  },
  "MKN_navy_convoy_escort_efficiency_tt": {
    "ru": "$convoy_escort_efficiency_tt$",
    "en": "$convoy_escort_efficiency_tt$"
  },
  "MKN_navy_convoy_raiding_efficiency_factor_tt": {
    "ru": "$convoy_raiding_efficiency_factor_tt$",
    "en": "$convoy_raiding_efficiency_factor_tt$"
  },
  "MKN_navy_development": {
    "ru": "Флот вольной территории",
    "en": "Fleet of the Free Territory"
  },
  "MKN_navy_development_summary": {
    "ru": "Улучшения флота накапливаются в одном духе.",
    "en": "Naval improvements accumulate in this single spirit."
  },
  "MKN_navy_hq_decisions": {
    "ru": "Полевые штабы: флот",
    "en": "Field Headquarters: Navy"
  },
  "MKN_navy_hq_unlock_tt": {
    "ru": "Открывает решения полевого штаба этого рода войск; тактики требуют выбранной военной программы.",
    "en": "Unlocks this service field headquarters; tactics require a chosen military program."
  },
  "MKN_navy_industrial_capacity_dockyard_tt": {
    "ru": "$industrial_capacity_dockyard_tt$",
    "en": "$industrial_capacity_dockyard_tt$"
  },
  "MKN_navy_mines_sweeping_by_fleets_factor_tt": {
    "ru": "$MODIFIER_MINES_SWEEPING_BY_FLEETS_FACTOR$: $RIGHT|+=%1$",
    "en": "$MODIFIER_MINES_SWEEPING_BY_FLEETS_FACTOR$: $RIGHT|+=%1$"
  },
  "MKN_navy_naval_coordination_tt": {
    "ru": "$naval_coordination_tt$",
    "en": "$naval_coordination_tt$"
  },
  "MKN_navy_naval_defense_factor_tt": {
    "ru": "$naval_defense_factor_tt$",
    "en": "$naval_defense_factor_tt$"
  },
  "MKN_navy_naval_detection_tt": {
    "ru": "$naval_detection_tt$",
    "en": "$naval_detection_tt$"
  },
  "MKN_navy_naval_retreat_speed_tt": {
    "ru": "$MODIFIER_NAVAL_RETREAT_SPEED$: $RIGHT|+=%1$",
    "en": "$MODIFIER_NAVAL_RETREAT_SPEED$: $RIGHT|+=%1$"
  },
  "MKN_navy_naval_ship_recovery_chance_factor_tt": {
    "ru": "$naval_ship_recovery_chance_factor_tt$",
    "en": "$naval_ship_recovery_chance_factor_tt$"
  },
  "MKN_navy_naval_speed_factor_tt": {
    "ru": "$naval_speed_factor_tt$",
    "en": "$naval_speed_factor_tt$"
  },
  "MKN_navy_naval_torpedo_hit_chance_factor_tt": {
    "ru": "$naval_torpedo_hit_chance_factor_tt$",
    "en": "$naval_torpedo_hit_chance_factor_tt$"
  },
  "MKN_navy_naval_torpedo_reveal_chance_factor_tt": {
    "ru": "$naval_torpedo_reveal_chance_factor_tt$",
    "en": "$naval_torpedo_reveal_chance_factor_tt$"
  },
  "MKN_navy_navy_casualty_on_sink_tt": {
    "ru": "$navy_casualty_on_sink_tt$",
    "en": "$navy_casualty_on_sink_tt$"
  },
  "MKN_navy_navy_fuel_consumption_factor_tt": {
    "ru": "$MODIFIER_NAVY_FUEL_CONSUMPTION_FACTOR$: $RIGHT|-=%1$",
    "en": "$MODIFIER_NAVY_FUEL_CONSUMPTION_FACTOR$: $RIGHT|-=%1$"
  },
  "MKN_navy_navy_submarine_attack_factor_tt": {
    "ru": "$navy_submarine_attack_factor_tt$",
    "en": "$navy_submarine_attack_factor_tt$"
  },
  "MKN_navy_navy_submarine_defence_factor_tt": {
    "ru": "$navy_submarine_defence_factor_tt$",
    "en": "$navy_submarine_defence_factor_tt$"
  },
  "MKN_navy_navy_submarine_detection_factor_tt": {
    "ru": "$navy_submarine_detection_factor_tt$",
    "en": "$navy_submarine_detection_factor_tt$"
  },
  "MKN_navy_repair_speed_factor_tt": {
    "ru": "$repair_speed_factor_tt$",
    "en": "$repair_speed_factor_tt$"
  },
  "MKN_navy_screening_efficiency_tt": {
    "ru": "$screening_efficiency_tt$",
    "en": "$screening_efficiency_tt$"
  },
  "MKN_neighbor_strikes": {
    "ru": "Стачки под чёрным знаменем",
    "en": "Black Flag Strikes"
  },
  "MKN_night_interceptors": {
    "ru": "Ночной перехват",
    "en": "Night Interception"
  },
  "MKN_night_marches": {
    "ru": "Ночные переходы",
    "en": "Night Marches"
  },
  "MKN_night_sorties": {
    "ru": "Ночные выходы",
    "en": "Night Sorties"
  },
  "MKN_observation_posts": {
    "ru": "Сеть наблюдательных постов",
    "en": "Observation Post Network"
  },
  "MKN_osyp_tsebriy": {
    "ru": "Осип Цебрий",
    "en": "Osyp Tsebriy"
  },
  "MKN_planned_economy": {
    "ru": "Плановое хозяйство",
    "en": "Planned Economy"
  },
  "MKN_plenum_pending": {
    "ru": "Харьков рассматривает равноправную автономию",
    "en": "Kharkov is considering equal autonomy"
  },
  "MKN_power_balance": {
    "ru": "Штаб и вольные советы",
    "en": "Staff and Free Soviets"
  },
  "MKN_project_aa_batteries": {
    "ru": "Зенитные батареи",
    "en": "Anti-Aircraft Batteries"
  },
  "MKN_project_aa_batteries_unlock_tt": {
    "ru": "Открывает одноразовый проект на карте: «Зенитные батареи».",
    "en": "Unlocks a one-time map project: Anti-Aircraft Batteries."
  },
  "MKN_project_coastal_battery": {
    "ru": "Береговая батарея",
    "en": "Coastal Battery"
  },
  "MKN_project_coastal_battery_unlock_tt": {
    "ru": "Открывает одноразовый проект на карте: «Береговая батарея».",
    "en": "Unlocks a one-time map project: Coastal Battery."
  },
  "MKN_project_forward_airstrip": {
    "ru": "Степной аэродром",
    "en": "Steppe Airfield"
  },
  "MKN_project_forward_airstrip_unlock_tt": {
    "ru": "Открывает одноразовый проект на карте: «Степной аэродром».",
    "en": "Unlocks a one-time map project: Steppe Airfield."
  },
  "MKN_project_front_railway": {
    "ru": "Укладка рельс к фронту",
    "en": "Lay Rails to the Front"
  },
  "MKN_project_front_railway_unlock_tt": {
    "ru": "Открывает одноразовый проект на карте: «Укладка рельс к фронту».",
    "en": "Unlocks a one-time map project: Lay Rails to the Front."
  },
  "MKN_project_fuel_cache": {
    "ru": "Схрон топлива",
    "en": "Fuel Cache"
  },
  "MKN_project_fuel_cache_unlock_tt": {
    "ru": "Открывает одноразовый проект на карте: «Схрон топлива».",
    "en": "Unlocks a one-time map project: Fuel Cache."
  },
  "MKN_project_hidden_cove": {
    "ru": "Скрытая бухта",
    "en": "Hidden Cove"
  },
  "MKN_project_hidden_cove_unlock_tt": {
    "ru": "Открывает одноразовый проект на карте: «Скрытая бухта».",
    "en": "Unlocks a one-time map project: Hidden Cove."
  },
  "MKN_project_hidden_supply_node": {
    "ru": "Скрытый узел снабжения",
    "en": "Hidden Supply Hub"
  },
  "MKN_project_hidden_supply_node_unlock_tt": {
    "ru": "Открывает одноразовый проект на карте: «Скрытый узел снабжения».",
    "en": "Unlocks a one-time map project: Hidden Supply Hub."
  },
  "MKN_project_observation_posts": {
    "ru": "Наблюдательные посты",
    "en": "Observation Posts"
  },
  "MKN_project_observation_posts_unlock_tt": {
    "ru": "Открывает одноразовый проект на карте: «Наблюдательные посты».",
    "en": "Unlocks a one-time map project: Observation Posts."
  },
  "MKN_project_repair_infrastructure": {
    "ru": "Ремонт инфраструктуры",
    "en": "Repair Infrastructure"
  },
  "MKN_project_repair_infrastructure_unlock_tt": {
    "ru": "Открывает одноразовый проект на карте: «Ремонт инфраструктуры».",
    "en": "Unlocks a one-time map project: Repair Infrastructure."
  },
  "MKN_radio_beacons": {
    "ru": "Радиомаяки полевых полос",
    "en": "Field Airstrip Radio Beacons"
  },
  "MKN_radio_sections": {
    "ru": "Радиостанция в каждом штабе",
    "en": "Radios in Every Headquarters"
  },
  "MKN_raider_dockyard": {
    "ru": "Мастерская малых подлодок",
    "en": "Small Submarine Yard"
  },
  "MKN_raider_escape_routes": {
    "ru": "Маршруты отхода",
    "en": "Escape Routes"
  },
  "MKN_raider_exercises": {
    "ru": "Учения скрытного флота",
    "en": "Stealth Fleet Exercises"
  },
  "MKN_raider_radio_discipline": {
    "ru": "Радиодисциплина рейдеров",
    "en": "Raider Radio Discipline"
  },
  "MKN_raider_replacement_crews": {
    "ru": "Резерв рейдерских экипажей",
    "en": "Raider Crew Reserve"
  },
  "MKN_raider_supply": {
    "ru": "Снабжение в тайных бухтах",
    "en": "Supply in Hidden Bays"
  },
  "MKN_raider_weather": {
    "ru": "Погода как союзник",
    "en": "Weather as an Ally"
  },
  "MKN_railway_guards": {
    "ru": "Железнодорожная стража",
    "en": "Railway Guards"
  },
  "MKN_railway_war": {
    "ru": "Железнодорожная война",
    "en": "Railway Warfare"
  },
  "MKN_recallable_front_delegates": {
    "ru": "Отзывные фронтовые делегаты",
    "en": "Recallable Front Delegates"
  },
  "MKN_recovery_tractors": {
    "ru": "Тягачи для эвакуации",
    "en": "Recovery Tractors"
  },
  "MKN_remount_artels": {
    "ru": "Артели конского резерва",
    "en": "Remount cooperatives"
  },
  "MKN_revkom_terror": {
    "ru": "Террор ревкома",
    "en": "Revkom Terror"
  },
  "MKN_rifle_artels_organization": {
    "ru": "Гуляйпольские оружейные артели",
    "en": "Gulyai Polye Armament Artels"
  },
  "MKN_rifle_artels_organization_initial": {
    "ru": "Артельная специализация: Гуляйпольские оружейные артели",
    "en": "Artel Specialization: Gulyai Polye Armament Artels"
  },
  "MKN_rifle_artels_organization_mature": {
    "ru": "Согласованное серийное производство",
    "en": "Coordinated Serial Production"
  },
  "MKN_rifle_artels_organization_specialization_a": {
    "ru": "Дешёвая массовая винтовка",
    "en": "Affordable Mass Rifle"
  },
  "MKN_rifle_artels_organization_specialization_b": {
    "ru": "Точное артельное оружие",
    "en": "Precision Artel Weapons"
  },
  "MKN_rifle_concern_1": {
    "ru": "Артель стрелкового вооружения",
    "en": "Small Arms Artels"
  },
  "MKN_rifle_concern_2": {
    "ru": "Артель стрелкового вооружения",
    "en": "Small Arms Artels"
  },
  "MKN_river_sea_coordination": {
    "ru": "От реки к морскому эскорту",
    "en": "River Sea Coordination"
  },
  "MKN_rural_reserve": {
    "ru": "Сменяемый сельский резерв",
    "en": "Rotating Village Reserve"
  },
  "MKN_scout_parties": {
    "ru": "Разведка малыми отрядами",
    "en": "Small Reconnaissance Parties"
  },
  "MKN_seed_cooperatives": {
    "ru": "Общинные семенные кооперативы",
    "en": "Communal Seed Cooperatives"
  },
  "MKN_serial_production": {
    "ru": "Серийное производство Днепра",
    "en": "Dnieper Serial Production"
  },
  "MKN_sky_watch_exercises": {
    "ru": "Учения воздушного дозора",
    "en": "Sky Watch Exercises"
  },
  "MKN_smuggling_network": {
    "ru": "Контрабандистские сети",
    "en": "Smuggling Networks"
  },
  "MKN_soviet_front_pending": {
    "ru": "Харьков рассматривает предложение общего фронта",
    "en": "Kharkov is considering the common front"
  },
  "MKN_soviet_supply_agreement": {
    "ru": "Советское соглашение о снабжении",
    "en": "Soviet Supply Agreement"
  },
  "MKN_soviet_trade_accepted": {
    "ru": "Харьков принял соглашение о снабжении",
    "en": "Kharkov accepted the supply agreement"
  },
  "MKN_spartacist_engineers": {
    "ru": "Мастерская спартаковцев",
    "en": "Spartacist Workshop"
  },
  "MKN_spartacist_factory_tt": {
    "ru": "Вне-картовые военные фабрики: §G+1§! на время действия духа.",
    "en": "Off-map military factories: §G+1§! while this spirit is active."
  },
  "MKN_staff_games": {
    "ru": "Штабные игры на Днепре",
    "en": "Dnieper Staff Exercises"
  },
  "MKN_standardized_workshops": {
    "ru": "Мастерские переходного периода",
    "en": "Workshops in Transition"
  },
  "MKN_steel_horses": {
    "ru": "Стальные кони",
    "en": "Iron Horses"
  },
  "MKN_steel_horses_idea": {
    "ru": "Стальные кони",
    "en": "Iron Horses"
  },
  "MKN_steppe_camouflage": {
    "ru": "Степная маскировка",
    "en": "Steppe Camouflage"
  },
  "MKN_steppe_hawks": {
    "ru": "Степные соколы",
    "en": "Steppe Hawks"
  },
  "MKN_steppe_quartermasters": {
    "ru": "Школа степных квартирмейстеров",
    "en": "Steppe Quartermaster School"
  },
  "MKN_steppe_quartermasters_idea": {
    "ru": "Степные интенданты",
    "en": "Steppe Quartermasters"
  },
  "MKN_steppes_freedom": {
    "ru": "Свобода степей",
    "en": "Freedom of the Steppe"
  },
  "MKN_submarine_crews": {
    "ru": "Школа подводных экипажей",
    "en": "Submarine Crew School"
  },
  "MKN_submarine_listening": {
    "ru": "Школа гидроакустиков",
    "en": "Hydrophone School"
  },
  "MKN_submarine_repair": {
    "ru": "Ремонт подводного флота",
    "en": "Submarine Repair"
  },
  "MKN_submarine_works_company": {
    "ru": "Лиманские подводные мастерские",
    "en": "Liman Submarine Workshops"
  },
  "MKN_submarine_works_company_specialization": {
    "ru": "Лиманские подводные мастерские",
    "en": "Liman Submarine Workshops"
  },
  "MKN_submarine_works_organization": {
    "ru": "Лиманские подводные мастерские",
    "en": "Liman Submarine Workshops"
  },
  "MKN_submarine_works_organization_initial": {
    "ru": "Артельная специализация: Лиманские подводные мастерские",
    "en": "Artel Specialization: Liman Submarine Workshops"
  },
  "MKN_submarine_works_organization_mature": {
    "ru": "Согласованное серийное производство",
    "en": "Coordinated Serial Production"
  },
  "MKN_submarine_works_organization_specialization_a": {
    "ru": "Скрытная прибрежная лодка",
    "en": "Stealth Coastal Boat"
  },
  "MKN_submarine_works_organization_specialization_b": {
    "ru": "Дальний торпедный рейдер",
    "en": "Long Range Torpedo Raider"
  },
  "MKN_sweeper_sections": {
    "ru": "Тральные отряды",
    "en": "Minesweeper Sections"
  },
  "MKN_tachanka_columns": {
    "ru": "Тачаночные колонны",
    "en": "Tachanka Columns"
  },
  "MKN_tachanka_tactics": {
    "ru": "Тачанки и пеший заслон",
    "en": "Tachankas and Infantry Screens"
  },
  "MKN_tachanka_warfare": {
    "ru": "Тачаночная война",
    "en": "Tachanka Warfare"
  },
  "MKN_tactic_air_dispersal": {
    "ru": "Рассредоточенные аэродромы",
    "en": "Dispersed Airfields"
  },
  "MKN_tactic_air_rescue": {
    "ru": "Спасение сбитых лётчиков",
    "en": "Downed Pilot Rescue"
  },
  "MKN_tactic_air_supply_lift": {
    "ru": "Доставка срочных грузов",
    "en": "Urgent Air Deliveries"
  },
  "MKN_tactic_armoured_manoeuvres": {
    "ru": "Резерв второго эшелона",
    "en": "Second Echelon Reserve"
  },
  "MKN_tactic_coastal_depots": {
    "ru": "Портовые склады снабжения",
    "en": "Port Supply Depots"
  },
  "MKN_tactic_coastal_fleet_exercises": {
    "ru": "Резерв портовых экипажей",
    "en": "Port Crew Reserve"
  },
  "MKN_tactic_convoy_rescue": {
    "ru": "Противолодочные патрули",
    "en": "Anti Submarine Patrols"
  },
  "MKN_tactic_damage_control": {
    "ru": "Артели аварийного ремонта",
    "en": "Repair and Salvage Artels"
  },
  "MKN_tactic_fighter_conversion": {
    "ru": "Общий запас авиационных деталей",
    "en": "Shared Aircraft Spares"
  },
  "MKN_tactic_flexible_orders": {
    "ru": "Задача вместо длинного приказа",
    "en": "Mission over Lengthy Orders"
  },
  "MKN_tactic_free_column_exercises": {
    "ru": "Сборы вольных колонн",
    "en": "Free Column Exercises"
  },
  "MKN_tactic_fuel_discipline": {
    "ru": "Учёт горючего в походе",
    "en": "Fuel Accounting on Campaign"
  },
  "MKN_tactic_joint_target_planning": {
    "ru": "Совместное планирование ударов",
    "en": "Joint Strike Planning"
  },
  "MKN_tactic_militia_engineers": {
    "ru": "Сапёрные десятки",
    "en": "Engineer Squads"
  },
  "MKN_tactic_mobile_medical": {
    "ru": "Подвижные санитарные пункты",
    "en": "Mobile Medical Posts"
  },
  "MKN_tactic_motorized_infantry": {
    "ru": "Пехота вслед за бронёй",
    "en": "Infantry Behind the Armour"
  },
  "MKN_tactic_night_interceptors": {
    "ru": "Школа радиолокации",
    "en": "Radar School"
  },
  "MKN_tactic_night_marches": {
    "ru": "Ночные переходы",
    "en": "Night Marches"
  },
  "MKN_tactic_radio_discipline": {
    "ru": "Радиодисциплина рейдеров",
    "en": "Raider Radio Discipline"
  },
  "MKN_tactic_raider_escape_routes": {
    "ru": "Маршруты отхода",
    "en": "Escape Routes"
  },
  "MKN_tactic_raider_weather": {
    "ru": "Погода как союзник",
    "en": "Weather as an Ally"
  },
  "MKN_tactic_replacement_crews": {
    "ru": "Резерв экипажей штурмовиков",
    "en": "Attack Crew Reserve"
  },
  "MKN_tactic_sky_watch_exercises": {
    "ru": "Защита промышленных районов",
    "en": "Industrial Air Defence"
  },
  "MKN_tactic_steppe_camouflage": {
    "ru": "Степная маскировка",
    "en": "Steppe Camouflage"
  },
  "MKN_tactic_submarine_listening": {
    "ru": "Школа гидроакустиков",
    "en": "Hydrophone School"
  },
  "MKN_tactic_sweeper_sections": {
    "ru": "Тральные отряды",
    "en": "Minesweeper Sections"
  },
  "MKN_tactic_tachanka_tactics": {
    "ru": "Тачанки и пеший заслон",
    "en": "Tachankas and Infantry Screens"
  },
  "MKN_tactic_tactical_recon": {
    "ru": "Тактическая воздушная разведка",
    "en": "Tactical Aerial Reconnaissance"
  },
  "MKN_tactic_torpedo_ambushes": {
    "ru": "Торпедные засады",
    "en": "Torpedo Ambushes"
  },
  "MKN_tactic_weather_service": {
    "ru": "Топливные склады эскадрилий",
    "en": "Squadron Fuel Depots"
  },
  "MKN_tactical_recon": {
    "ru": "Тактическая воздушная разведка",
    "en": "Tactical Aerial Reconnaissance"
  },
  "MKN_tank_crews": {
    "ru": "Артель танковых экипажей",
    "en": "Tank Crew Artel"
  },
  "MKN_tank_maintenance": {
    "ru": "Полевой ремонт брони",
    "en": "Field Armour Repair"
  },
  "MKN_target_markers": {
    "ru": "Обозначение целей с земли",
    "en": "Ground Target Marking"
  },
  "MKN_torpedo_ambushes": {
    "ru": "Торпедные засады",
    "en": "Torpedo Ambushes"
  },
  "MKN_torpedo_artels": {
    "ru": "Торпедные мастерские",
    "en": "Torpedo Workshops"
  },
  "MKN_torpedo_trials": {
    "ru": "Испытания торпед",
    "en": "Torpedo Trials"
  },
  "MKN_unified_army_org_factor_tt": {
    "ru": "Организация армии: $RIGHT|+=%1$",
    "en": "Army organization: $RIGHT|+=%1$"
  },
  "MKN_unified_army_org_regain_tt": {
    "ru": "Восстановление организации: $RIGHT|+=%1$",
    "en": "Organization regain: $RIGHT|+=%1$"
  },
  "MKN_unified_army_speed_factor_tt": {
    "ru": "Скорость армии: $RIGHT|+=%1$",
    "en": "Army speed: $RIGHT|+=%1$"
  },
  "MKN_unified_attrition_tt": {
    "ru": "Истощение: $RIGHT|-=%1$",
    "en": "Attrition: $RIGHT|-=%1$"
  },
  "MKN_unified_consumer_goods_factor_tt": {
    "ru": "Фактор потребительских товаров: $RIGHT|-=%1$",
    "en": "Consumer goods factor: $RIGHT|-=%1$"
  },
  "MKN_unified_industrial_capacity_factory_tt": {
    "ru": "Выпуск военных заводов: $RIGHT|+=%1$",
    "en": "Military factory output: $RIGHT|+=%1$"
  },
  "MKN_unified_max_planning_tt": {
    "ru": "Максимальное планирование: $RIGHT|+=%1$",
    "en": "Maximum planning: $RIGHT|+=%1$"
  },
  "MKN_unified_political_power_gain_tt": {
    "ru": "Политическая власть в день: $RIGHT|+=2$",
    "en": "Daily political power: $RIGHT|+=2$"
  },
  "MKN_unified_production_factory_efficiency_gain_factor_tt": {
    "ru": "Прирост производственной эффективности: $RIGHT|+=%1$",
    "en": "Production efficiency growth: $RIGHT|+=%1$"
  },
  "MKN_unified_production_speed_buildings_factor_tt": {
    "ru": "Скорость строительства: $RIGHT|+=%1$",
    "en": "Construction speed: $RIGHT|+=%1$"
  },
  "MKN_unified_research_speed_factor_tt": {
    "ru": "Скорость исследований: $RIGHT|+=%1$",
    "en": "Research speed: $RIGHT|+=%1$"
  },
  "MKN_unified_stability_factor_tt": {
    "ru": "Стабильность: $RIGHT|+=%1$",
    "en": "Stability: $RIGHT|+=%1$"
  },
  "MKN_unified_supply_consumption_factor_tt": {
    "ru": "Потребление снабжения: $RIGHT|-=%1$",
    "en": "Supply consumption: $RIGHT|-=%1$"
  },
  "MKN_unified_training_time_army_factor_tt": {
    "ru": "Время подготовки: $RIGHT|-=%1$",
    "en": "Army training time: $RIGHT|-=%1$"
  },
  "MKN_unlock_border_clashes_tt": {
    "ru": "Открывает пограничные столкновения с ЛитБелом и советскими республиками в областях на контролируемой общей границе.",
    "en": "Unlocks state-targeted border clashes with LitBel and the Soviet Republics on a controlled common frontier."
  },
  "MKN_unlock_sabotage_tt": {
    "ru": "Открывает разрушение инфраструктуры и железных дорог в областях под угрозой во время войны.",
    "en": "Unlocks infrastructure and railway demolition in threatened states during war."
  },
  "MKN_unlock_strikes_tt": {
    "ru": "Открывает сети стачек в соседних странах.",
    "en": "Unlocks strike networks in neighboring countries."
  },
  "MKN_unlock_volunteers_tt": {
    "ru": "Открывает повторный набор иностранных добровольцев.",
    "en": "Unlocks repeatable recruitment of foreign volunteers."
  },
  "MKN_untrained_militias": {
    "ru": "Неподготовленное ополчение",
    "en": "Untrained Militias"
  },
  "MKN_village_airfields": {
    "ru": "Сельские аэродромы",
    "en": "Village Airfields"
  },
  "MKN_village_muster": {
    "ru": "Сельские сборные пункты",
    "en": "Village Muster Points"
  },
  "MKN_war_for_the_steppe": {
    "ru": "Война за степь",
    "en": "War for the Steppe"
  },
  "MKN_worker_battalions_idea": {
    "ru": "Подготовленные рабочие батальоны",
    "en": "Trained Worker Battalions"
  },
  "MKN_zaporizhstal_organization": {
    "ru": "Концерн «Вольная сталь»",
    "en": "Free Steel Concern"
  },
  "MKN_zaporizhstal_organization_initial": {
    "ru": "Днепровские сталевары",
    "en": "Dnieper Steelworkers"
  },
  "MKN_zaporizhstal_serial_forging": {
    "ru": "Серийная ковка орудий",
    "en": "Serial Gun Forging"
  },
  "NWW_MKN_andrii_dorosh": {
    "ru": "Андрий Дорош",
    "en": "Andrii Dorosh"
  },
  "NWW_MKN_andrii_dorosh_advisor": {
    "ru": "Андрий Дорош",
    "en": "Andrii Dorosh"
  },
  "NWW_MKN_andrii_dorosh_high_command": {
    "ru": "Андрей Дорош",
    "en": "Andrii Dorosh"
  },
  "NWW_MKN_andrii_dorosh_specialty": {
    "ru": "Организатор территориальной обороны",
    "en": "Territorial Defence Organizer"
  },
  "NWW_MKN_dmytro_savchenko": {
    "ru": "Дмитро Савченко",
    "en": "Dmytro Savchenko"
  },
  "NWW_MKN_dmytro_savchenko_advisor": {
    "ru": "Дмитро Савченко",
    "en": "Dmytro Savchenko"
  },
  "NWW_MKN_dmytro_savchenko_specialty": {
    "ru": "Координатор авиации поддержки",
    "en": "Support Aviation Coordinator"
  },
  "NWW_MKN_eugen": {
    "ru": "Евген",
    "en": "Eugen"
  },
  "NWW_MKN_eugen_high_command": {
    "ru": "Евген",
    "en": "Eugen"
  },
  "NWW_MKN_fedir_shchus": {
    "ru": "Фёдор Щусь",
    "en": "Fedir Shchus"
  },
  "NWW_MKN_fedir_shchus_high_command": {
    "ru": "Фёдор Щусь",
    "en": "Fedir Shchus"
  },
  "NWW_MKN_fedir_shchus_navy_chief": {
    "ru": "Фёдор Щусь",
    "en": "Fedir Shchus"
  },
  "NWW_MKN_ivan_bondarenko": {
    "ru": "Иван Бондаренко",
    "en": "Ivan Bondarenko"
  },
  "NWW_MKN_ivan_bondarenko_specialty": {
    "ru": "Делегат хозяйственных соглашений",
    "en": "Economic Agreements Delegate"
  },
  "NWW_MKN_logistics_delegate": {
    "ru": "Делегат снабженческих артелей",
    "en": "Supply Artel Delegate"
  },
  "NWW_MKN_makhno": {
    "ru": "Нестор Махно",
    "en": "Nestor Makhno"
  },
  "NWW_MKN_makhno_high_command": {
    "ru": "Нестор Махно",
    "en": "Nestor Makhno"
  },
  "NWW_MKN_military_theorist": {
    "ru": "Инструктор повстанческого штаба",
    "en": "Insurgent Staff Instructor"
  },
  "NWW_MKN_mykola_kovalenko": {
    "ru": "Микола Коваленко",
    "en": "Mykola Kovalenko"
  },
  "NWW_MKN_mykola_kovalenko_advisor": {
    "ru": "Микола Коваленко",
    "en": "Mykola Kovalenko"
  },
  "NWW_MKN_mykola_kovalenko_specialty": {
    "ru": "Исследователь подвижной войны",
    "en": "Mobile Warfare Scholar"
  },
  "NWW_MKN_oleksandr_hordiienko": {
    "ru": "Олександр Гордиенко",
    "en": "Oleksandr Hordiienko"
  },
  "NWW_MKN_oleksandr_hordiienko_advisor": {
    "ru": "Олександр Гордиенко",
    "en": "Oleksandr Hordiienko"
  },
  "NWW_MKN_oleksandr_hordiienko_specialty": {
    "ru": "Инженер полевых укреплений",
    "en": "Field Fortification Engineer"
  },
  "NWW_MKN_olena_hrytsenko": {
    "ru": "Олена Гриценко",
    "en": "Olena Hrytsenko"
  },
  "NWW_MKN_olena_hrytsenko_advisor": {
    "ru": "Олена Гриценко",
    "en": "Olena Hrytsenko"
  },
  "NWW_MKN_olena_hrytsenko_specialty": {
    "ru": "Организатор снабжения и санитарных артелей",
    "en": "Supply and Medical Artel Organizer"
  },
  "NWW_MKN_peter_arshinov": {
    "ru": "Пётр Аршинов",
    "en": "Peter Arshinov"
  },
  "NWW_MKN_petro_stepanenko": {
    "ru": "Петро Степаненко",
    "en": "Petro Stepanenko"
  },
  "NWW_MKN_petro_stepanenko_specialty": {
    "ru": "Инженер промышленного совета",
    "en": "Industrial Council Engineer"
  },
  "NWW_MKN_roman_danylenko": {
    "ru": "Роман Даниленко",
    "en": "Roman Danylenko"
  },
  "NWW_MKN_roman_danylenko_advisor": {
    "ru": "Роман Даниленко",
    "en": "Roman Danylenko"
  },
  "NWW_MKN_roman_danylenko_specialty": {
    "ru": "Начальник огневых расчётов",
    "en": "Artillery Fire Coordinator"
  },
  "NWW_MKN_school_delegate": {
    "ru": "Делегат технических коммун",
    "en": "Technical Commune Delegate"
  },
  "NWW_MKN_serhii_melnyk": {
    "ru": "Сергий Мельник",
    "en": "Serhii Melnyk"
  },
  "NWW_MKN_serhii_melnyk_specialty": {
    "ru": "Координатор технических школ",
    "en": "Technical School Coordinator"
  },
  "NWW_MKN_viktor_belash": {
    "ru": "Виктор Белаш",
    "en": "Viktor Belash"
  },
  "NWW_MKN_viktor_belash_army_chief": {
    "ru": "Виктор Белаш",
    "en": "Viktor Belash"
  },
  "NWW_MKN_volin": {
    "ru": "Всеволод Волин",
    "en": "Vsevolod Volin"
  },
  "NWW_MKN_yakiv_levchenko": {
    "ru": "Яков Левченко",
    "en": "Yakiv Levchenko"
  },
  "NWW_MKN_yakiv_levchenko_advisor": {
    "ru": "Яков Левченко",
    "en": "Yakiv Levchenko"
  },
  "NWW_MKN_yakiv_levchenko_specialty": {
    "ru": "Защитник приморских сообщений",
    "en": "Coastal Sea Lane Defender"
  },
  "communism": {
    "ru": "Коммунизм",
    "en": "Communist"
  },
  "democratic": {
    "ru": "Демократия",
    "en": "Democratic"
  },
  "fascism": {
    "ru": "Фашизм",
    "en": "Fascist"
  },
  "mkn_agronomist": {
    "ru": "Агроном",
    "en": "Agronomist"
  },
  "mkn_anti_statist_theorist": {
    "ru": "Теоретик безвластия",
    "en": "Anti Statist Theorist"
  },
  "mkn_armored_train_commander": {
    "ru": "Командующий бронепоездами",
    "en": "Armored Train Commander"
  },
  "mkn_arsenal_coordinator": {
    "ru": "Координатор арсеналов",
    "en": "Arsenal Coordinator"
  },
  "mkn_batko_advisor": {
    "ru": "Батька в штабе",
    "en": "Batko Advisor"
  },
  "mkn_batko_departed": {
    "ru": "Махно умер",
    "en": "Makhno has died"
  },
  "mkn_batko_legend": {
    "ru": "Легенда о Батьке",
    "en": "The Legend of Batko"
  },
  "mkn_commune_secretary": {
    "ru": "Секретарь общин",
    "en": "Commune Secretary"
  },
  "mkn_cooperative_treasurer": {
    "ru": "Казначей кооперативов",
    "en": "Cooperative Treasurer"
  },
  "mkn_education_delegate": {
    "ru": "Делегат просвещения",
    "en": "Education Delegate"
  },
  "mkn_entrenchment_specialist": {
    "ru": "Специалист по укреплениям",
    "en": "Entrenchment Specialist"
  },
  "mkn_eugen_infantry_master": {
    "ru": "Мастер пехотной войны",
    "en": "Master of Infantry Warfare"
  },
  "mkn_free_press_editor": {
    "ru": "Редактор вольной прессы",
    "en": "Free Press Editor"
  },
  "mkn_frontline_delegate": {
    "ru": "Фронтовой делегат",
    "en": "Frontline Delegate"
  },
  "mkn_grain_distributor": {
    "ru": "Распределитель зерна",
    "en": "Grain Distributor"
  },
  "mkn_granary_overseer": {
    "ru": "Хранитель житницы",
    "en": "Granary Overseer"
  },
  "mkn_idealist_philosopher": {
    "ru": "Философ-идеалист",
    "en": "The Idealist Philosopher"
  },
  "mkn_industrial_organizer": {
    "ru": "Организатор промышленности",
    "en": "Industrial Organizer"
  },
  "mkn_infantry_specialist": {
    "ru": "Специалист по пехоте",
    "en": "Infantry Specialist"
  },
  "mkn_iron_warlord": {
    "ru": "Железный воевода",
    "en": "Iron Warlord"
  },
  "mkn_labor_delegate": {
    "ru": "Делегат труда",
    "en": "Labor Delegate"
  },
  "mkn_literacy_organizer": {
    "ru": "Организатор грамотности",
    "en": "Literacy Organizer"
  },
  "mkn_market_keeper": {
    "ru": "Хранитель рынка",
    "en": "Market Keeper"
  },
  "mkn_military_orator": {
    "ru": "Военный оратор",
    "en": "Military Orator"
  },
  "mkn_militia_delegate": {
    "ru": "Делегат ополчения",
    "en": "Militia Delegate"
  },
  "mkn_paralyzed_committee": {
    "ru": "Парализованный комитет",
    "en": "Paralyzed Committee"
  },
  "mkn_rail_dispatcher": {
    "ru": "Железнодорожный диспетчер",
    "en": "Rail Dispatcher"
  },
  "mkn_recruiting_commissar": {
    "ru": "Организатор призыва",
    "en": "Recruiting Commissar"
  },
  "mkn_rural_defender": {
    "ru": "Защитник села",
    "en": "Rural Defender"
  },
  "mkn_steppe_logistics_officer": {
    "ru": "Степной интендант",
    "en": "Steppe Logistics Officer"
  },
  "mkn_syndicalist_organizer": {
    "ru": "Организатор синдикатов",
    "en": "Syndicalist Organizer"
  },
  "mkn_syndicalist_theorist": {
    "ru": "Теоретик синдикализма",
    "en": "Syndicalist Theorist"
  },
  "mkn_tachanka_expert": {
    "ru": "Эксперт по тачанкам",
    "en": "Tachanka Expert"
  },
  "mkn_union_secretary": {
    "ru": "Секретарь профсоюзов",
    "en": "Union Secretary"
  },
  "mkn_veterans_organizer": {
    "ru": "Организатор ветеранов",
    "en": "Veterans Organizer"
  },
  "mkn_village_mediator": {
    "ru": "Сельский посредник",
    "en": "Village Mediator"
  },
  "mkn_weapons_broker": {
    "ru": "Снабженец оружием",
    "en": "Weapons Broker"
  },
  "mkn_workshop_engineer": {
    "ru": "Инженер мастерских",
    "en": "Workshop Engineer"
  },
  "neutrality": {
    "ru": "Нейтралитет",
    "en": "Non-Aligned"
  }
}
```

## Воспроизводимость

Обновление: `python tools/export_mkn_military_focuses.py`. Источником истины служат текущие скрипты. Текст change notes приведён как контекст; при расхождении приоритет у определений. SHA-256 исходников:

```text
e8fb6d1f088c7ba684cc9983335af17d284e565951d434a03c752483821935d6  common/characters/MKN.txt
9c97e35f68d003e95a2f1ff3ec33b441eefc8a21066d0ed730074885ac946ba7  common/characters/MKN_eugen.txt
ae835996da49af348dfdee1ebb27c3c2a8b795a3efb4fb4069b244abc5d1653f  common/characters/nww_MKN.txt
3daf80b27bc8885c7b3669b7022b104e463934961237b8220c7b5a243f768845  common/country_leader/MKN_eugen_traits.txt
885f74300138ec75f573807cda6352764d3a7229feb7ad9a10e06694f3fcfc59  common/country_leader/MKN_overhaul_traits.txt
9a56c802ab0b4248ea5fdb37fb4b5e327d9f7f873fe36d4bd1a96b30323eceb4  common/country_leader/nww_mkn_advisor_traits.txt
8f41ba61861c3d023a4bd4b6b485d602de7bebf5819629d3b2e18e9159862ee6  common/country_leader/nww_mkn_industry_traits.txt
5c1222d4f9931eab8433729e77b617d51698fe6905b5216d7d32a2622f237565  common/decisions/MKN_military_decisions.txt
4d8fd8c88d90c3d90ef595935c39a8c1fc6914335c036bf978f9a3c5a7575d2b  common/decisions/categories/MKN_military_categories.txt
bc6c0b8b25886490ef9c3cf6c47f6eea64377f842898c488953cc913352295d6  common/dynamic_modifiers/nww_dynamic_modifiers.txt
7c8f082895bc53b72830c0ee020fb65ada4a92a5ad25109cf2029c3a90cf16a6  common/ideas/MKN_economic_ideas.txt
611edb2e1a6467a97de569d47f3ee84a35afe1c886e187395e1b222784181f4e  common/ideas/MKN_eugen_ideas.txt
25371b7edaff96981cfd0ed8d0f8e5c574c32184c69e30202d4f86d53a44417f  common/ideas/MKN_ideas.txt
e05c2d6467285c783175b4a05bec616818bd86597ca02aa6d603db9fceae74b4  common/ideas/MKN_international_ideas.txt
3119111b4352dc5d3de3a8ed8c6c06f40882ffcd684009c304528774710fb4c4  common/ideas/MKN_ukr_border_ideas.txt
96dc19b62d8d55f44ffba9f38a6247189c316b315975f526b9e2105ea8934442  common/ideas/nww_MKN_ideas.txt
aeac99efeecc6e47960090e5544759c52a6de443b844e49dd327086f9087a1ac  common/ideas/nww_companies.txt
93e8d6097a158274a8866b67ceec291bfe865ca1b70f5e01bcb15c5455fc5db8  common/military_industrial_organization/organizations/MKN_organizations.txt
6f8beafc8308efe7271982eb738c5194189ca610522eebc34a019f6a4e068e18  common/military_industrial_organization/organizations/nww_organizations.txt
30fb6a1f8409ef550f591384b682956a6f39bd0c16f35baea90ca17e66d7d2bb  common/national_focus/MKN.txt
814826f08a46a8f3918c09bffd69d1f8a7bd08a771c9d33a9c0ed16bf96a9a77  common/national_focus/MKN_ukraine_integration_focuses.txt
94021c1606a809debbc52043c2d86e94ad8337ba8310aa387011c26f7dc702b2  common/on_actions/MKN_international_on_actions.txt
8ba12712b4565cbd2fec4c0b073f4f361d5339b2545caf9bc106cd830f245b6e  common/on_actions/nww_mkn_progression.txt
dd312eb87ff80e0cacbfaaf4330fc3713c9da35b34000c3900dea4e539581e49  common/scripted_effects/MKN_bop_effects.txt
1e97f095e431564a35ea7cc885ce59c024767e131412ef1bd480b89977e36145  common/scripted_effects/MKN_effects.txt
3ac85e3db10933a424a94dcc80809b897c255e5ba4085737bb23c04d92a3a43c  common/scripted_effects/MKN_international_effects.txt
b1a8932fccb7ac88fe653f76e35b762e354b5e3cda46f54cfe0c96c3c89803a3  common/scripted_effects/nww_mkn_progression.txt
21176c3f503751b9a05033d0287d8d530bd56ef939125904bc3e792e7e6601d8  common/scripted_triggers/MKN_ukraine_integration_triggers.txt
064c5d3e7674ae77be75e15958aa5e61649e95e72c30a5da4392b2e2ff3e9212  common/technologies/MKN_technologies.txt
98d662e059bf44cb336c6b305e0cc5c933cf080dd00bf7e2c04a862caeff92ef  docs/MKN_military_programs.json
a27efcccd72881ee0bb85cd5d2ccdf2ac02b3318db6c16cc07051d2556aaac3c  docs/MKN_military_refactor.md
b5c2cf38406ee26a8ed66ffdb00c6040173213661a819df33c938f40676a78b8  history/countries/MKN - Makhnovists.txt
378501a7caba17e5ae897664cdb4fe58c491a3b1ece153201babe9dd4fe14386  history/units/MKN_1936.txt
9afd51cea1377ae0d23ca07f6dd6b7267720e386fc0256b2026e0060edd9eff5  history/units/MKN_black_guard.txt
a915241c7a99bb0f1d9c591cc3efc4be2a5d04805e52e67cbf70d91f54745afa  history/units/MKN_black_guard_oob.txt
a7bda3d97130a5cc8b63ec056d8bb0684a3f00ea2dd34f094b699953b98ef968  localisation/MKN_economic_l_english.yml
b3d8dad65c6b0e8fc9f8b98f188239443442e89dcdd41615b1c4009161f76d6a  localisation/MKN_economic_l_russian.yml
9dd7c7bb9fddede09565d14e05b6a2d808453869b168cd838167d070ea33e7c1  localisation/MKN_ukraine_integration_l_english.yml
5a9b1b9a9f6e3739ed3000bafa55d6071dd2087dfff709145235600a6b5ca1e9  localisation/MKN_ukraine_integration_l_russian.yml
58b0549c4a5585e0a81e9e51b4c2b752f547b87e695eec06e0751ffc77afd2d0  localisation/english/MKN_bop_l_english.yml
e120d4b627a8155563f670904d42200dbf23fece8f0dfe2436fa28c1eda40e48  localisation/english/MKN_flags_l_english.yml
28407387457a3ef6ba18274b323085029bcc5f65ccc8932f7611dcd14f6b9fb6  localisation/english/MKN_focus_l_english.yml
6d99a5ee1b9b47daa73355e27d94c14a8c10806ce99b95f51d6199f35467e30c  localisation/english/MKN_frontier_l_english.yml
d132a9de94be4094ff7ada71e98f1477acb5053f8c5c7139253878f635318f38  localisation/english/MKN_international_l_english.yml
5b27b4568fd0eab3547c0bb5c7bf4322dbd6ced6f0eb13d6a29d0396106a455c  localisation/english/MKN_l_english.yml
58d5167b5d3202d2f3294f47f064b4a972c118e6f8427e6375c72e334a54accc  localisation/english/MKN_military_l_english.yml
1643c863c1cd0fdccd41976b8aff200b136fba518537587f019a341bd12df4b7  localisation/english/MKN_overhaul_l_english.yml
769b325ff62e2a46191dfb0350f30dd9ac8aea18cd6a666363478a9ba1f9de69  localisation/english/MKN_parties_l_english.yml
89fad478ca6237bb406c8ae580b755d900de82f1a93eb30d811c6bf7219e3f55  localisation/english/MKN_personnel_l_english.yml
2f4cf319b759c1b96495c9eed4e127c1a01dece861571ee99ad3c820a89a8544  localisation/nww_MKN_expansion_l_english.yml
02c6aa2b16a72e8380381034fc6e162d62aff3c18aec72544cd78bd6df710a13  localisation/nww_MKN_expansion_l_russian.yml
914bc98236aac458b6bd8c86a65ddd904e0ffd6238001091dca4e67919753161  localisation/nww_MKN_l_english.yml
e6d488b868e13dc5f36d83aebc7e839b99a52301162f24276ce897004abcbdcc  localisation/nww_MKN_l_russian.yml
e2987f7620a518c160bb708b15d877dc4b15bd103cfe589fe8c2ca3160ab47c8  localisation/nww_country_expansion_l_english.yml
ca9b4146311e70fc407906c10a81a006bf6c4a2a18dd6ef4870cf446dc6097d6  localisation/nww_country_expansion_l_russian.yml
cf3a4bd9aba43bb684c0097f4ecff4a1506222de523323ef6859408a6f7d9ef8  localisation/russian/MKN_bop_l_russian.yml
279bb9d9be668925fd01773d7be9506eee21a3d51ce841d757b546ff3bd86e35  localisation/russian/MKN_flags_l_russian.yml
cd0edacae9f202e1d0d7aa0bcc2b43a29320a0163f70fb720fe5fd8d7f24cc27  localisation/russian/MKN_focus_l_russian.yml
dc7665abf73a5ae406a9138f31b2e97b1e5141173a8967721a1064b86985636f  localisation/russian/MKN_frontier_l_russian.yml
a43bdd62180b58db665e13f314a0262c6e4e7d25663f4ba8a4c6d02e724710f3  localisation/russian/MKN_international_l_russian.yml
1a8aa65d623905a15bd0ce44c51f1b3a7517de8444232fb14eaf4b96fd098c20  localisation/russian/MKN_l_russian.yml
f30493700fde2edb3f867ddda443110ecf3e5b130eea5b51162e4068b1d3dc08  localisation/russian/MKN_military_l_russian.yml
b418c7f37e7bfd6179c829a2e2a8d3dd6adcfba7aad06896c41cf1bd83350c07  localisation/russian/MKN_overhaul_l_russian.yml
779612fe406278c6c7bb4ca20bd002d762f7de903309ef7672e7b962a552bdc3  localisation/russian/MKN_parties_l_russian.yml
214fc275a33104ad82fb40343d6dcd4c21d3ea8e0621e47c2df4e6510b3e06bc  localisation/russian/MKN_personnel_l_russian.yml
6a1698fca9a56fd34464a36b4a309ed1595e09290dfe0638623a7bb592b4f3aa  tools/export_mkn_industrial_focuses.py
12e1b72ee8488a52f11040d77749b8e057b71e780d25bddd0b83b6a340f929ab  tools/export_mkn_military_focuses.py
05a0b3facf4d97366afef978722e4e2e1dbb6b7d39bbdbc3c3458d1bd47ecc61  tools/hoi4_script.py
```
