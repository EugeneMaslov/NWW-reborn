# MKN: промышленность — пакет для анализа другой нейросетью

Этот файл самодостаточен: содержит названия, описания, награды, условия, исходные определения и связанные системы. Это снимок текущих файлов мода, а не проект новых наград.

Основная промышленность: **48 фокусов**, по 24 на взаимоисключающих путях. Дополнительно: **67** связанных фокусов науки, политики, предприятий и военной инфраструктуры. Всего карточек: **115**. Чисто боевые фокусы без промышленного эффекта не включены; их необходимые предки приведены отдельно.

## Контекст и правила интерпретации

- Первая мировая война не происходила. Сохранять действующие ID и лор, монарха Махно и совместимость сохранений.
- Стоимость focus.cost измеряется неделями: 5 = 35 дней. Несколько блоков prerequisite соединяются И; focus внутри одного блока — ИЛИ. Условия available добавляются к prerequisites. Ветви с mutually_exclusive одновременно пройти нельзя.
- Награды в if/limit и random_owned_controlled_state условны. Числа построек в обзоре — потенциальные суммы по коду, а не обещание фактической выдачи. Проверять владение, контроль, ядра, регион и строительные слоты.
- Общий постоянный экономический дух — MKN_free_industry_modifier. Развивать его через MKN_unified_*; не заменять каждую ступень отдельным духом. Военные, авиационные и морские программы имеют собственные общие духи.
- Значения ниже даны в сырых единицах движка. political_power_gain — плоский прирост в сутки; фактор 0.05 обычно означает 5 процентных пунктов. Не интерпретировать все числовые значения как проценты.
- custom_effect_tooltip/show_mio_tooltip/unlock_mio_trait_tooltip описывают интерфейс, сами по себе ничего не выдают. Реальные разблокировки предприятий находятся в available у предприятия/черты.
- Сохранять паритет Arms Against Tyranny MIO и обычных конструкторов без DLC. Не копировать огромные награды из старого мода. Проверять ресурсную/энергетическую систему установленной версии.
- Восстановление общих переменных в сохранении не должно повторно выдавать заводы, ресурсы, политическую власть или технику. Полный код восстановления включён ниже.
- Эти данные извлечены статически. Реальные сроки кампании, отображение подсказок и выдача наград требуют проверки в игре.

## Основные ветки

### Днепрострой — `MKN_dneprostroi`

24 фокуса; сумма их длительностей: 840 дней. Это сумма всей ветки, а не кратчайший путь к отдельной награде.

Потенциальные постройки при выполнении всех внутренних условий: `arms_factory`: +7, `industrial_complex`: +6, `infrastructure`: +3.

- Днепрострой — `MKN_dneprostroi`
- Открытые сметы Днепростроя — `MKN_dnieper_audit`
- Никопольский марганец — `MKN_manganese_nikopol`
- Инженеры с мандатом коммун — `MKN_engineering_delegates`
- Выборные бригадиры — `MKN_elected_brigadiers`
- Кичкасский мост — `MKN_kichkas_bridge`
- Запорожсталь — `MKN_zaporizhstal`
- Инструкторы при заводах — `MKN_factory_instructors`
- Электрификация степи — `MKN_steppe_electrification`
- Тракторный завод «Коммунар» — `MKN_kommunar_tractor`
- Концерн «Вольная сталь» — `MKN_steel_concern`
- Зерновой экспорт — `MKN_grain_export`
- Никопольский трубный завод — `MKN_nikopol_tube_zavod`
- «Союз заводов» — `MKN_steel_concern_union`
- Угольные промыслы степи — `MKN_steppe_coal_contracts`
- Днепровский алюминиевый — `MKN_dnepro_aluminium`
- Рабочие батальоны резерва — `MKN_worker_battalions`
- Единая днепровская диспетчерская — `MKN_dnieper_dispatch`
- Механические заводы волостей — `MKN_steppe_mech_works`
- Общие допуски и калибры — `MKN_dnieper_standards`
- Согласованные производственные циклы — `MKN_production_cycles`
- Кассы рабочих семей — `MKN_workers_welfare`
- Днепровский хозяйственный договор — `MKN_industrial_compact`
- Стальная вольница — `MKN_steel_volnitsa`

### Вольные кооперативы — `MKN_free_cooperatives`

24 фокуса; сумма их длительностей: 840 дней. Это сумма всей ветки, а не кратчайший путь к отдельной награде.

Потенциальные постройки при выполнении всех внутренних условий: `arms_factory`: +4, `industrial_complex`: +7, `infrastructure`: +1.

- Вольные кооперативы — `MKN_free_cooperatives`
- Реестр взаимных обязательств — `MKN_artel_register`
- Соляные артели — `MKN_salt_artsels`
- Сельские кузницы — `MKN_village_smithies`
- Отзывные командиры — `MKN_recallable_commanders`
- Хлебные биржи — `MKN_grain_brokers`
- Передвижные мастерские — `MKN_mobile_workshops`
- Полевые школы коммун — `MKN_field_schools`
- Ветряки вольных хуторов — `MKN_wind_mills_steppe`
- Артель стрелкового вооружения — `MKN_rifle_concern`
- Хлеб для обмена и резерва — `MKN_harvest_reserves`
- Вольные базары — `MKN_free_bazaars`
- Грузовые артели — `MKN_freight_artels`
- Кредит без ростовщика — `MKN_mutual_credit`
- Степной монетный двор — `MKN_steppe_mint`
- Расширение оружейных артелей — `MKN_rifle_concern_union`
- Подвижная самооборона — `MKN_mobile_self_defence`
- Биржи инструмента и ремонта — `MKN_repair_exchanges`
- Договор о взаимозаменяемости — `MKN_workshop_standards`
- Съезд обозных артелей — `MKN_supply_congress`
- Общий портфель заказов — `MKN_shared_orders`
- Страховая касса коммун — `MKN_social_fund`
- Хартия хозяйственной взаимопомощи — `MKN_communal_compact`
- Федерация ремесленных коммун — `MKN_craft_federation`

## Карточки фокусов

### Днепрострой — `MKN_dneprostroi`

Английское название: Dnieper Industrial Program. Категория: Основная промышленная ветка.

Описание RU: Коммуны выберут путь крупных предприятий и общего промышленного плана. Первый договор ослабит хозяйственный кризис; программа вольных кооперативов станет недоступна.

Описание EN: Communes choose major factories and a shared industrial plan. The first agreement eases the economic crisis and excludes the free cooperatives program.

Источник: `common/national_focus/MKN.txt:11`. Стоимость: 5 (35 дней). Координаты: x=4, y=0.

Предпосылки: нет нарисованной предпосылки; см. available.

Непосредственные продолжения: MKN_dnieper_audit.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Политическая власть: 50
- Изменение параметра: MKN_unified_political_power_gain 0.1000
- Изменение параметра: MKN_unified_consumer_goods_factor -0.0500
- Изменение параметра: MKN_unified_production_speed_buildings_factor 0.0500
- Изменение параметра: MKN_unified_industrial_capacity_factory 0.0500

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_dneprostroi
    icon = GFX_focus_generic_hydroelectric_energy
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
            tooltip = MKN_unified_industrial_capacity_factory_tt
            MKN_unified_industrial_capacity_factory = 0.0500
        }
    }
    x = 4
    y = 0
    cost = 5
}
```

### Открытые сметы Днепростроя — `MKN_dnieper_audit`

Английское название: Public Dnieper Budgets. Категория: Основная промышленная ветка.

Описание RU: Съезд проверит расходы прежде, чем начнутся большие стройки. Делегаты выберут напряжённый строительный сезон или бережливое переоснащение; оба решения действуют один год.

Описание EN: The congress audits costs before major construction begins. Delegates choose an intensive building season or careful retooling; either policy lasts one year.

Источник: `common/national_focus/MKN.txt:2690`. Стоимость: 5 (35 дней). Координаты: x=4, y=1.

Предпосылки: (Днепрострой [MKN_dneprostroi]).

Непосредственные продолжения: MKN_manganese_nikopol, MKN_engineering_delegates, MKN_elected_brigadiers.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_unified_industrial_capacity_factory 0.0500

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_dnieper_audit
    icon = GFX_focus_generic_money_for_equipment
    x = 4
    y = 1
    available_if_capitulated = no
    ai_will_do = {
        factor = 1
    }
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    completion_reward = {
        country_event = {
            id = mkn.30
            days = 1
        }
        add_to_variable = {
            tooltip = MKN_unified_industrial_capacity_factory_tt
            MKN_unified_industrial_capacity_factory = 0.0500
        }
    }
    prerequisite = {
        focus = MKN_dneprostroi
    }
    cost = 5
}
```

### Никопольский марганец — `MKN_manganese_nikopol`

Английское название: Nikopol Manganese. Категория: Основная промышленная ветка.

Описание RU: Руды Никопольского бассейна — металл для вольных заводов и валюта для вольных рук.

Описание EN: The ores of the Nikopol basin are metal for free factories and coin for free hands.

Источник: `common/national_focus/MKN.txt:40`. Стоимость: 5 (35 дней). Координаты: x=0, y=2.

Предпосылки: (Открытые сметы Днепростроя [MKN_dnieper_audit]).

Непосредственные продолжения: MKN_kichkas_bridge.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Политическая власть: 50
- Потенциальный ресурс: steel +15

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_manganese_nikopol
    icon = GFX_focus_generic_mining_industry
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
    }
    x = 0
    y = 2
    prerequisite = {
        focus = MKN_dnieper_audit
    }
    cost = 5
}
```

### Инженеры с мандатом коммун — `MKN_engineering_delegates`

Английское название: Engineers with Communal Mandates. Категория: Основная промышленная ветка.

Описание RU: Коммуны направят инженеров с проверяемыми полномочиями. Общий реестр станков станет основой металлургической программы.

Описание EN: Communes send engineers with accountable mandates. A shared machine register becomes the basis of the steel program.

Источник: `common/national_focus/MKN.txt:2717`. Стоимость: 5 (35 дней). Координаты: x=4, y=2.

Предпосылки: (Открытые сметы Днепростроя [MKN_dnieper_audit]).

Непосредственные продолжения: MKN_zaporizhstal.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_unified_production_factory_efficiency_gain_factor 0.0800
- Изменение параметра: MKN_unified_research_speed_factor 0.0200
- Изменение параметра: MKN_unified_industrial_capacity_factory 0.0500
- Потенциальная постройка: industrial_complex +1

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_engineering_delegates
    icon = GFX_focus_research
    x = 4
    y = 2
    available_if_capitulated = no
    ai_will_do = {
        factor = 1
    }
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    completion_reward = {
        add_tech_bonus = {
            bonus = 0.5
            uses = 1
            category = industry
        }
        add_to_variable = {
            MKN_unified_production_factory_efficiency_gain_factor = 0.0800
            tooltip = MKN_unified_production_factory_efficiency_gain_factor_tt
        }
        add_to_variable = {
            MKN_unified_research_speed_factor = 0.0200
            tooltip = MKN_unified_research_speed_factor_tt
        }
        add_to_variable = {
            tooltip = MKN_unified_industrial_capacity_factory_tt
            MKN_unified_industrial_capacity_factory = 0.0500
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
    }
    prerequisite = {
        focus = MKN_dnieper_audit
    }
    cost = 5
}
```

### Выборные бригадиры — `MKN_elected_brigadiers`

Английское название: Elected Brigadiers. Категория: Основная промышленная ветка.

Описание RU: Рабочие и сельские отряды изберут командиров, обязанных регулярно отчитываться. Право отзыва совместимо с ясными обязанностями в бою.

Описание EN: Workers and village detachments elect commanders who report regularly. Recall rights remain compatible with clear responsibilities in battle.

Источник: `common/national_focus/MKN.txt:2769`. Стоимость: 5 (35 дней). Координаты: x=8, y=2.

Предпосылки: (Открытые сметы Днепростроя [MKN_dnieper_audit]).

Непосредственные продолжения: MKN_factory_instructors.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_unified_army_org_factor 0.0500
- Изменение параметра: MKN_unified_training_time_army_factor -0.0800
- Изменение параметра: MKN_unified_max_planning 0.0400

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_elected_brigadiers
    icon = GFX_focus_generic_manpower
    x = 8
    y = 2
    available_if_capitulated = no
    ai_will_do = {
        factor = 1
    }
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    completion_reward = {
        army_experience = 10
        add_to_variable = {
            MKN_unified_army_org_factor = 0.0500
            tooltip = MKN_unified_army_org_factor_tt
        }
        add_to_variable = {
            MKN_unified_training_time_army_factor = -0.0800
            tooltip = MKN_unified_training_time_army_factor_tt
        }
        add_to_variable = {
            MKN_unified_max_planning = 0.0400
            tooltip = MKN_unified_max_planning_tt
        }
    }
    prerequisite = {
        focus = MKN_dnieper_audit
    }
    cost = 5
}
```

### Кичкасский мост — `MKN_kichkas_bridge`

Английское название: Kichkas Bridge. Категория: Основная промышленная ветка.

Описание RU: Восстановим инфраструктуру и согласуем первые сквозные маршруты. Это ослабит перебои снабжения, но не заменит диспетчерскую сеть.

Описание EN: Restore infrastructure and agree through routes. This eases supply disruptions, but a dispatch network is still needed.

Источник: `common/national_focus/MKN.txt:64`. Стоимость: 5 (35 дней). Координаты: x=0, y=3.

Предпосылки: (Никопольский марганец [MKN_manganese_nikopol]).

Непосредственные продолжения: MKN_steppe_electrification.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Политическая власть: 50
- Потенциальная постройка: infrastructure +1
- Потенциальная постройка: infrastructure +1
- Изменение параметра: MKN_unified_supply_consumption_factor -0.0800
- Изменение параметра: MKN_unified_army_org_regain 0.0500

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_kichkas_bridge
    icon = GFX_focus_generic_railroad
    completion_reward = {
        add_political_power = 50
        196 = {
            if = {
                limit = {
                    is_owned_and_controlled_by = ROOT
                }
                add_building_construction = {
                    type = infrastructure
                    level = 1
                    instant_build = yes
                }
            }
        }
        226 = {
            if = {
                limit = {
                    is_owned_and_controlled_by = ROOT
                }
                add_building_construction = {
                    type = infrastructure
                    level = 1
                    instant_build = yes
                }
            }
        }
        add_to_variable = {
            MKN_unified_supply_consumption_factor = -0.0800
            tooltip = MKN_unified_supply_consumption_factor_tt
        }
        add_to_variable = {
            MKN_unified_army_org_regain = 0.0500
            tooltip = MKN_unified_army_org_regain_tt
        }
    }
    x = 0
    y = 3
    prerequisite = {
        focus = MKN_manganese_nikopol
    }
    cost = 5
}
```

### Запорожсталь — `MKN_zaporizhstal`

Английское название: Zaporizhstal. Категория: Основная промышленная ветка.

Описание RU: После восстановления перевозок инженерные делегаты согласуют металлургическую программу. Хозяйственные ограничения уменьшатся ещё на одну ступень.

Описание EN: With transport restored, engineering delegates agree a steel program. Economic penalties fall by another tier.

Источник: `common/national_focus/MKN.txt:109`. Стоимость: 5 (35 дней). Координаты: x=4, y=3.

Предпосылки: (Инженеры с мандатом коммун [MKN_engineering_delegates]).

Непосредственные продолжения: MKN_kommunar_tractor.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Политическая власть: 50
- Потенциальная постройка: arms_factory +1
- Потенциальный ресурс: steel +10
- Изменение параметра: MKN_unified_political_power_gain 0.1000
- Изменение параметра: MKN_unified_consumer_goods_factor -0.0500
- Изменение параметра: MKN_unified_production_speed_buildings_factor 0.0500
- Изменение параметра: MKN_unified_industrial_capacity_factory 0.0500

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_zaporizhstal
    icon = GFX_focus_generic_steel_mill
    completion_reward = {
        add_political_power = 50
        226 = {
            if = {
                limit = {
                    is_owned_and_controlled_by = ROOT
                }
                add_building_construction = {
                    type = arms_factory
                    level = 1
                    instant_build = yes
                }
                add_resource = {
                    type = steel
                    amount = 10
                }
                add_extra_state_shared_building_slots = 1
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
            tooltip = MKN_unified_industrial_capacity_factory_tt
            MKN_unified_industrial_capacity_factory = 0.0500
        }
    }
    x = 4
    y = 3
    prerequisite = {
        focus = MKN_engineering_delegates
    }
    available = {
        has_completed_focus = MKN_kichkas_bridge
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    cost = 5
}
```

### Инструкторы при заводах — `MKN_factory_instructors`

Английское название: Factory Instructors. Категория: Основная промышленная ветка.

Описание RU: Учебные смены дадут ополченцам навыки связи и взаимодействия. Выпускать оружие и уметь им пользоваться должны одни и те же сообщества.

Описание EN: Training shifts teach communications and cooperation. The communities producing weapons must also know how to use them.

Источник: `common/national_focus/MKN.txt:2801`. Стоимость: 5 (35 дней). Координаты: x=8, y=3.

Предпосылки: (Выборные бригадиры [MKN_elected_brigadiers]).

Непосредственные продолжения: MKN_steel_concern.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_unified_army_org_factor 0.0600
- Изменение параметра: MKN_unified_training_time_army_factor -0.0700
- Изменение параметра: MKN_unified_max_planning 0.0300

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_factory_instructors
    icon = GFX_focus_generic_army_doctrines_2
    x = 8
    y = 3
    available_if_capitulated = no
    ai_will_do = {
        factor = 1
    }
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    completion_reward = {
        army_experience = 15
        add_to_variable = {
            MKN_unified_army_org_factor = 0.0600
            tooltip = MKN_unified_army_org_factor_tt
        }
        add_to_variable = {
            MKN_unified_training_time_army_factor = -0.0700
            tooltip = MKN_unified_training_time_army_factor_tt
        }
        add_to_variable = {
            MKN_unified_max_planning = 0.0300
            tooltip = MKN_unified_max_planning_tt
        }
    }
    prerequisite = {
        focus = MKN_elected_brigadiers
    }
    cost = 5
}
```

### Электрификация степи — `MKN_steppe_electrification`

Английское название: Steppe Electrification. Категория: Основная промышленная ветка.

Описание RU: Общая сеть свяжет предприятия и сельские поселения. Дух электрификации снизит потребление энергии заводами.

Описание EN: A shared grid connects factories and villages. Electrification reduces factory energy consumption.

Источник: `common/national_focus/MKN.txt:160`. Стоимость: 5 (35 дней). Координаты: x=0, y=4.

Предпосылки: (Кичкасский мост [MKN_kichkas_bridge]).

Непосредственные продолжения: MKN_grain_export.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Политическая власть: 100
- Потенциальная постройка: industrial_complex +1
- Изменение параметра: MKN_unified_production_speed_buildings_factor 0.0500
- Изменение параметра: MKN_unified_factory_energy_consumption -0.1000

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_steppe_electrification
    icon = GFX_focus_generic_modernize_industry
    completion_reward = {
        add_political_power = 100
        196 = {
            if = {
                limit = {
                    is_owned_and_controlled_by = ROOT
                }
                add_building_construction = {
                    type = industrial_complex
                    level = 1
                    instant_build = yes
                }
                add_extra_state_shared_building_slots = 1
            }
        }
        add_to_variable = {
            MKN_unified_production_speed_buildings_factor = 0.0500
            tooltip = MKN_unified_production_speed_buildings_factor_tt
        }
        add_to_variable = {
            MKN_unified_factory_energy_consumption = -0.1000
            tooltip = MKN_unified_factory_energy_consumption_tt
        }
    }
    x = 0
    y = 4
    prerequisite = {
        focus = MKN_kichkas_bridge
    }
    cost = 5
}
```

### Тракторный завод «Коммунар» — `MKN_kommunar_tractor`

Английское название: Kommunar Tractor Works. Категория: Основная промышленная ветка.

Описание RU: Запорожский «Коммунар» сыграет трактора, а когда потребуется — корпуса для пушек.

Описание EN: Zaporizhzhia's Kommunar will build tractors, and when needed — gun carriages.

Источник: `common/national_focus/MKN.txt:194`. Стоимость: 5 (35 дней). Координаты: x=4, y=4.

Предпосылки: (Запорожсталь [MKN_zaporizhstal]).

Непосредственные продолжения: MKN_nikopol_tube_zavod.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Потенциальная постройка: arms_factory +1
- Изменение параметра: MKN_unified_industrial_capacity_factory 0.0500

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_kommunar_tractor
    icon = GFX_focus_generic_military_industry
    completion_reward = {
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
        add_to_variable = {
            tooltip = MKN_unified_industrial_capacity_factory_tt
            MKN_unified_industrial_capacity_factory = 0.0500
        }
    }
    x = 4
    y = 4
    prerequisite = {
        focus = MKN_zaporizhstal
    }
    cost = 5
}
```

### Концерн «Вольная сталь» — `MKN_steel_concern`

Английское название: Concern of Free Steel. Категория: Основная промышленная ветка.

Описание RU: Ставропольско-никопольские металлурги объединяются в концерн вольных заводов. Веткой промышленности он станет сильнее.\n\n§YДоступен промышленный концерн. Нанимайте его в разделе советников.§!

Описание EN: Steppe steel-masters join into a concern of free factories. Strengthen it through industry focuses.\n\n§YAn industrial concern is available. Hire it in the advisors panel.§!

Источник: `common/national_focus/MKN.txt:373`. Стоимость: 5 (35 дней). Координаты: x=8, y=4.

Предпосылки: (Инструкторы при заводах [MKN_factory_instructors]).

Непосредственные продолжения: MKN_steel_concern_union.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Потенциальная постройка: arms_factory +1

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_steel_concern
    icon = GFX_focus_generic_money_for_equipment
    completion_reward = {
        show_ideas_tooltip = MKN_industry_concern_1
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
    }
    x = 8
    y = 4
    prerequisite = {
        focus = MKN_factory_instructors
    }
    cost = 5
}
```

### Зерновой экспорт — `MKN_grain_export`

Английское название: Grain Export. Категория: Основная промышленная ветка.

Описание RU: Хлеб вольных коммун идёт на экспорт — за станки и наличность.

Описание EN: The communes' grain goes abroad — for machinery and hard cash.

Источник: `common/national_focus/MKN.txt:347`. Стоимость: 5 (35 дней). Координаты: x=0, y=5.

Предпосылки: (Электрификация степи [MKN_steppe_electrification]).

Непосредственные продолжения: MKN_steppe_coal_contracts.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Потенциальная постройка: industrial_complex +1
- Политическая власть: 50

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_grain_export
    icon = GFX_focus_generic_british_trade
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
        add_political_power = 50
    }
    x = 0
    y = 5
    prerequisite = {
        focus = MKN_steppe_electrification
    }
    cost = 5
}
```

### Никопольский трубный завод — `MKN_nikopol_tube_zavod`

Английское название: Nikopol Tube Works. Категория: Основная промышленная ветка.

Описание RU: Унифицируем заготовки и оснастку. Переход к общим деталям ослабит разрозненность мастерских.

Описание EN: Standardize blanks and tooling. Common parts ease workshop fragmentation.

Источник: `common/national_focus/MKN.txt:267`. Стоимость: 5 (35 дней). Координаты: x=4, y=5.

Предпосылки: (Тракторный завод «Коммунар» [MKN_kommunar_tractor]).

Непосредственные продолжения: MKN_dnepro_aluminium.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Потенциальная постройка: arms_factory +1
- Изменение параметра: MKN_unified_industrial_capacity_factory 0.0500
- Изменение параметра: MKN_unified_production_factory_efficiency_gain_factor 0.0700
- Изменение параметра: MKN_unified_research_speed_factor 0.0200

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_nikopol_tube_zavod
    icon = GFX_focus_generic_industry_2
    completion_reward = {
        add_tech_bonus = {
            bonus = 0.5
            uses = 1
            category = artillery
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
        add_to_variable = {
            MKN_unified_industrial_capacity_factory = 0.0500
            tooltip = MKN_unified_industrial_capacity_factory_tt
        }
        add_to_variable = {
            MKN_unified_production_factory_efficiency_gain_factor = 0.0700
            tooltip = MKN_unified_production_factory_efficiency_gain_factor_tt
        }
        add_to_variable = {
            MKN_unified_research_speed_factor = 0.0200
            tooltip = MKN_unified_research_speed_factor_tt
        }
    }
    x = 4
    y = 5
    prerequisite = {
        focus = MKN_kommunar_tractor
    }
    cost = 5
}
```

### «Союз заводов» — `MKN_steel_concern_union`

Английское название: Union of Factories. Категория: Основная промышленная ветка.

Описание RU: Заводы концерна связывает общая ставка и общие склады — концерн становится сильнее.

Описание EN: Linked rates and shared stockpiles make the concern stronger.

Источник: `common/national_focus/MKN.txt:402`. Стоимость: 5 (35 дней). Координаты: x=8, y=5.

Предпосылки: (Концерн «Вольная сталь» [MKN_steel_concern]).

Непосредственные продолжения: MKN_worker_battalions.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Потенциальная постройка: arms_factory +1

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_steel_concern_union
    icon = GFX_focus_generic_american_investments
    completion_reward = {
        if = {
            limit = {
                has_idea = MKN_industry_concern_1
            }
            swap_ideas = {
                remove_idea = MKN_industry_concern_1
                add_idea = MKN_industry_concern_2
            }
        }
        custom_effect_tooltip = MKN_steel_concern_union_tt
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
    }
    x = 8
    y = 5
    prerequisite = {
        focus = MKN_steel_concern
    }
    cost = 5
}
```

### Угольные промыслы степи — `MKN_steppe_coal_contracts`

Английское название: Steppe Coal Workings. Категория: Основная промышленная ветка.

Описание RU: Небольшие промыслы и подвоз топлива обеспечат новые заводы энергией. Развиваем угольную добычу, не подменяя её нефтяными запасами.

Описание EN: Small workings and fuel deliveries provide energy for the new factories. Coal extraction serves industry independently of oil reserves.

Источник: `common/national_focus/MKN.txt:2833`. Стоимость: 5 (35 дней). Координаты: x=0, y=6.

Предпосылки: (Зерновой экспорт [MKN_grain_export]).

Непосредственные продолжения: MKN_dnieper_dispatch.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Потенциальный ресурс: coal +12

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_steppe_coal_contracts
    icon = GFX_focus_generic_mining_industry
    x = 0
    y = 6
    available_if_capitulated = no
    ai_will_do = {
        factor = 1
    }
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    completion_reward = {
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
    prerequisite = {
        focus = MKN_grain_export
    }
    cost = 5
}
```

### Днепровский алюминиевый — `MKN_dnepro_aluminium`

Английское название: Dnieper Aluminium Works. Категория: Основная промышленная ветка.

Описание RU: Токи Днепростроя плавят бокситы. Крылья Вольной территории будут лёгкими.

Описание EN: Dneprostroi's currents smelt bauxite. The Free Territory's wings will be light.

Источник: `common/national_focus/MKN.txt:223`. Стоимость: 5 (35 дней). Координаты: x=4, y=6.

Предпосылки: (Никопольский трубный завод [MKN_nikopol_tube_zavod]).

Непосредственные продолжения: MKN_steppe_mech_works.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Потенциальный ресурс: aluminium +8
- Потенциальная постройка: industrial_complex +1

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_dnepro_aluminium
    icon = GFX_focus_generic_aluminum
    completion_reward = {
        add_tech_bonus = {
            bonus = 0.5
            uses = 1
            category = air_equipment
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
    }
    x = 4
    y = 6
    prerequisite = {
        focus = MKN_nikopol_tube_zavod
    }
    cost = 5
}
```

### Рабочие батальоны резерва — `MKN_worker_battalions`

Английское название: Worker Reserve Battalions. Категория: Основная промышленная ветка.

Описание RU: Закрепим учебные сборы, сменяемость командиров и защиту рабочего места за ополченцем. Подготовленный резерв завершит военную реформу.

Описание EN: Regular exercises, accountable command and protected civilian jobs establish a trained reserve and complete military reform.

Источник: `common/national_focus/MKN.txt:2916`. Стоимость: 5 (35 дней). Координаты: x=8, y=6.

Предпосылки: («Союз заводов» [MKN_steel_concern_union]).

Непосредственные продолжения: MKN_dnieper_standards.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_unified_army_org_factor 0.1000
- Изменение параметра: MKN_unified_training_time_army_factor -0.0500
- Изменение параметра: MKN_unified_max_planning 0.0800

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_worker_battalions
    icon = GFX_focus_generic_manpower
    x = 8
    y = 6
    available_if_capitulated = no
    ai_will_do = {
        factor = 1
    }
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    completion_reward = {
        army_experience = 15
        add_to_variable = {
            MKN_unified_army_org_factor = 0.1000
            tooltip = MKN_unified_army_org_factor_tt
        }
        add_to_variable = {
            MKN_unified_training_time_army_factor = -0.0500
            tooltip = MKN_unified_training_time_army_factor_tt
        }
        add_to_variable = {
            MKN_unified_max_planning = 0.0800
            tooltip = MKN_unified_max_planning_tt
        }
    }
    prerequisite = {
        focus = MKN_steel_concern_union
    }
    cost = 5
}
```

### Единая днепровская диспетчерская — `MKN_dnieper_dispatch`

Английское название: Dnieper Dispatch Network. Категория: Основная промышленная ветка.

Описание RU: Станции согласуют расписания, приоритеты угольных составов и воинских эшелонов. Общая связь уменьшит перебои снабжения.

Описание EN: Stations agree timetables and priorities for coal and military trains. Shared communications reduce supply disruptions.

Источник: `common/national_focus/MKN.txt:2868`. Стоимость: 5 (35 дней). Координаты: x=0, y=7.

Предпосылки: (Угольные промыслы степи [MKN_steppe_coal_contracts]).

Непосредственные продолжения: MKN_production_cycles.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_unified_supply_consumption_factor -0.0700
- Изменение параметра: MKN_unified_army_org_regain 0.0600
- Потенциальная постройка: industrial_complex +1

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_dnieper_dispatch
    icon = GFX_focus_generic_railroad
    x = 0
    y = 7
    available_if_capitulated = no
    ai_will_do = {
        factor = 1
    }
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    completion_reward = {
        add_tech_bonus = {
            bonus = 0.5
            uses = 1
            category = train_tech
        }
        add_to_variable = {
            MKN_unified_supply_consumption_factor = -0.0700
            tooltip = MKN_unified_supply_consumption_factor_tt
        }
        add_to_variable = {
            MKN_unified_army_org_regain = 0.0600
            tooltip = MKN_unified_army_org_regain_tt
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
    }
    prerequisite = {
        focus = MKN_steppe_coal_contracts
    }
    cost = 5
}
```

### Механические заводы волостей — `MKN_steppe_mech_works`

Английское название: Volost Machine Workshops. Категория: Основная промышленная ветка.

Описание RU: Станки на вольной земле, вольными руками.

Описание EN: Machine tools on free land, run by free hands.

Источник: `common/national_focus/MKN.txt:309`. Стоимость: 5 (35 дней). Координаты: x=4, y=7.

Предпосылки: (Днепровский алюминиевый [MKN_dnepro_aluminium]).

Непосредственные продолжения: MKN_workers_welfare.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Потенциальная постройка: arms_factory +1
- Потенциальная постройка: infrastructure +1

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_steppe_mech_works
    icon = GFX_focus_generic_industry_3
    completion_reward = {
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
        196 = {
            if = {
                limit = {
                    is_owned_and_controlled_by = ROOT
                }
                add_building_construction = {
                    type = infrastructure
                    level = 1
                    instant_build = yes
                }
                add_extra_state_shared_building_slots = 1
            }
        }
    }
    x = 4
    y = 7
    prerequisite = {
        focus = MKN_dnepro_aluminium
    }
    cost = 5
}
```

### Общие допуски и калибры — `MKN_dnieper_standards`

Английское название: Common Tolerances and Calibres. Категория: Основная промышленная ветка.

Описание RU: Заводские советы примут общие стандарты вместо несовместимых партий деталей. Артели сохранят свои мастерские, но будут работать по понятным чертежам.

Описание EN: Factory councils adopt common standards to end incompatible batches. Artels retain their workshops while using shared drawings.

Источник: `common/national_focus/MKN.txt:2948`. Стоимость: 5 (35 дней). Координаты: x=8, y=7.

Предпосылки: (Рабочие батальоны резерва [MKN_worker_battalions]).

Непосредственные продолжения: MKN_industrial_compact.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Политическая власть: 25
- Потенциальная постройка: arms_factory +1

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_dnieper_standards
    icon = GFX_focus_generic_industry_2
    x = 8
    y = 7
    available_if_capitulated = no
    ai_will_do = {
        factor = 1
    }
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    completion_reward = {
        add_tech_bonus = {
            bonus = 0.5
            uses = 1
            category = industry
        }
        add_political_power = 25
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
    }
    prerequisite = {
        focus = MKN_worker_battalions
    }
    cost = 5
}
```

### Согласованные производственные циклы — `MKN_production_cycles`

Английское название: Coordinated Production Cycles. Категория: Основная промышленная ветка.

Описание RU: После налаживания подвоза и принятия стандартов заводы перейдут к длинным сериям. Разрозненное производство уступит устойчивому выпуску вооружения.

Описание EN: Reliable deliveries and common standards enable long production runs. Fragmented workshops become a stable armaments industry.

Источник: `common/national_focus/MKN.txt:2989`. Стоимость: 5 (35 дней). Координаты: x=0, y=8.

Предпосылки: (Единая днепровская диспетчерская [MKN_dnieper_dispatch]).

Непосредственные продолжения: MKN_steel_volnitsa.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_unified_industrial_capacity_factory 0.1500
- Изменение параметра: MKN_unified_production_factory_efficiency_gain_factor 0.0500
- Изменение параметра: MKN_unified_research_speed_factor 0.0100
- Изменение параметра: MKN_unified_production_factory_max_efficiency_factor 0.1000

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_production_cycles
    icon = GFX_focus_generic_military_industry
    x = 0
    y = 8
    available_if_capitulated = no
    ai_will_do = {
        factor = 1
    }
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    completion_reward = {
        add_to_variable = {
            MKN_unified_industrial_capacity_factory = 0.1500
            tooltip = MKN_unified_industrial_capacity_factory_tt
        }
        add_to_variable = {
            MKN_unified_production_factory_efficiency_gain_factor = 0.0500
            tooltip = MKN_unified_production_factory_efficiency_gain_factor_tt
        }
        add_to_variable = {
            MKN_unified_research_speed_factor = 0.0100
            tooltip = MKN_unified_research_speed_factor_tt
        }
        add_to_variable = {
            MKN_unified_production_factory_max_efficiency_factor = 0.1000
            tooltip = MKN_unified_production_factory_max_efficiency_factor_tt
        }
    }
    prerequisite = {
        focus = MKN_dnieper_dispatch
    }
    available = {
        has_completed_focus = MKN_nikopol_tube_zavod
        has_completed_focus = MKN_dnieper_standards
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    cost = 5
}
```

### Кассы рабочих семей — `MKN_workers_welfare`

Английское название: Workers Family Funds. Категория: Основная промышленная ветка.

Описание RU: Общие кассы поддержат семьи строителей и резервистов. Промышленный договор не получит доверия, если его успех измеряется только тоннажем стали.

Описание EN: Shared funds support builders and reservists' families. The industrial compact needs measures of success beyond tonnes of steel.

Источник: `common/national_focus/MKN.txt:3030`. Стоимость: 5 (35 дней). Координаты: x=4, y=8.

Предпосылки: (Механические заводы волостей [MKN_steppe_mech_works]).

Непосредственные продолжения: MKN_steel_volnitsa.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- add_stability: 0.03
- Политическая власть: 25

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_workers_welfare
    icon = GFX_focus_generic_agricultural_subsidies
    x = 4
    y = 8
    available_if_capitulated = no
    ai_will_do = {
        factor = 1
    }
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    completion_reward = {
        add_stability = 0.03
        add_political_power = 25
    }
    prerequisite = {
        focus = MKN_steppe_mech_works
    }
    cost = 5
}
```

### Днепровский хозяйственный договор — `MKN_industrial_compact`

Английское название: Dnieper Economic Compact. Категория: Основная промышленная ветка.

Описание RU: Утвердим открытый план заказов, обязательства предприятий и защиту семей. Съезд снимет последние хозяйственные ограничения и закрепит преимущества крупной промышленности.

Описание EN: Ratify a public order plan, factory obligations and family protections. The congress removes the last economic penalties and secures the benefits of major industry.

Источник: `common/national_focus/MKN.txt:3051`. Стоимость: 5 (35 дней). Координаты: x=8, y=8.

Предпосылки: (Общие допуски и калибры [MKN_dnieper_standards]).

Непосредственные продолжения: MKN_steel_volnitsa.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_unified_political_power_gain 0.1500
- Изменение параметра: MKN_unified_consumer_goods_factor -0.0500
- Изменение параметра: MKN_unified_production_speed_buildings_factor 0.1300
- Изменение параметра: MKN_unified_global_building_slots_factor 0.3000

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_industrial_compact
    icon = GFX_focus_generic_diplomatic_treaty
    x = 8
    y = 8
    available_if_capitulated = no
    ai_will_do = {
        factor = 1
    }
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    completion_reward = {
        add_to_variable = {
            MKN_unified_political_power_gain = 0.1500
            tooltip = MKN_unified_political_power_gain_tt
        }
        add_to_variable = {
            MKN_unified_consumer_goods_factor = -0.0500
            tooltip = MKN_unified_consumer_goods_factor_tt
        }
        add_to_variable = {
            MKN_unified_production_speed_buildings_factor = 0.1300
            tooltip = MKN_unified_production_speed_buildings_factor_tt
        }
        add_to_variable = {
            MKN_unified_global_building_slots_factor = 0.3000
            tooltip = MKN_unified_global_building_slots_factor_tt
        }
    }
    prerequisite = {
        focus = MKN_dnieper_standards
    }
    available = {
        has_completed_focus = MKN_workers_welfare
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    cost = 5
}
```

### Стальная вольница — `MKN_steel_volnitsa`

Английское название: Steel Free Territory. Категория: Основная промышленная ветка.

Описание RU: Завершим промышленную программу после реформы производства, семейных касс и хозяйственного договора. Подготовленные склады и расписания превратят перебои снабжения в преимущество.

Описание EN: Complete the industrial program after production reform, family funds and an economic compact. Prepared depots and timetables turn supply disruptions into an advantage.

Источник: `common/national_focus/MKN.txt:440`. Стоимость: 5 (35 дней). Координаты: x=4, y=9.

Предпосылки: (Согласованные производственные циклы [MKN_production_cycles]) И (Кассы рабочих семей [MKN_workers_welfare]) И (Днепровский хозяйственный договор [MKN_industrial_compact]).

Непосредственные продолжения: нет.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Потенциальная постройка: industrial_complex +1
- add_stability: 0.03
- Изменение параметра: MKN_unified_supply_consumption_factor -0.1500
- Изменение параметра: MKN_unified_army_org_regain 0.0900

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_steel_volnitsa
    icon = GFX_focus_generic_stalinist_industry
    completion_reward = {
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
        add_stability = 0.03
        add_to_variable = {
            MKN_unified_supply_consumption_factor = -0.1500
            tooltip = MKN_unified_supply_consumption_factor_tt
        }
        add_to_variable = {
            MKN_unified_army_org_regain = 0.0900
            tooltip = MKN_unified_army_org_regain_tt
        }
    }
    x = 4
    y = 9
    prerequisite = {
        focus = MKN_production_cycles
    }
    prerequisite = {
        focus = MKN_workers_welfare
    }
    prerequisite = {
        focus = MKN_industrial_compact
    }
    cost = 5
}
```

### Вольные кооперативы — `MKN_free_cooperatives`

Английское название: Free Cooperatives. Категория: Основная промышленная ветка.

Описание RU: Сеть самостоятельных артелей примет взаимные обязательства. Хозяйственный кризис ослабнет; путь Днепростроя станет недоступен.

Описание EN: Independent artels accept mutual obligations. The economic crisis eases and the Dnieper industrial program becomes unavailable.

Источник: `common/national_focus/MKN.txt:480`. Стоимость: 5 (35 дней). Координаты: x=16, y=0.

Предпосылки: нет нарисованной предпосылки; см. available.

Непосредственные продолжения: MKN_artel_register.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Политическая власть: 50
- Изменение параметра: MKN_unified_political_power_gain 0.1000
- Изменение параметра: MKN_unified_consumer_goods_factor -0.0500
- Изменение параметра: MKN_unified_production_speed_buildings_factor 0.0500
- Изменение параметра: MKN_unified_industrial_capacity_factory 0.0500

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_free_cooperatives
    icon = GFX_focus_generic_agricultural_subsidies
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
            tooltip = MKN_unified_industrial_capacity_factory_tt
            MKN_unified_industrial_capacity_factory = 0.0500
        }
    }
    x = 16
    y = 0
    cost = 5
}
```

### Реестр взаимных обязательств — `MKN_artel_register`

Английское название: Register of Mutual Obligations. Категория: Основная промышленная ветка.

Описание RU: Артели запишут, чем располагают и что обещают соседям. Учёт не требует начальника над каждой мастерской.

Описание EN: Artels record their resources and promises to neighbours. Accounting needs no overseer above every workshop.

Источник: `common/national_focus/MKN.txt:3091`. Стоимость: 5 (35 дней). Координаты: x=16, y=1.

Предпосылки: (Вольные кооперативы [MKN_free_cooperatives]).

Непосредственные продолжения: MKN_salt_artsels, MKN_village_smithies, MKN_recallable_commanders.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Политическая власть: 50
- Изменение параметра: MKN_unified_industrial_capacity_factory 0.0500

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_artel_register
    icon = GFX_focus_generic_money_for_equipment
    x = 16
    y = 1
    available_if_capitulated = no
    ai_will_do = {
        factor = 1
    }
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    completion_reward = {
        add_political_power = 50
        add_to_variable = {
            tooltip = MKN_unified_industrial_capacity_factory_tt
            MKN_unified_industrial_capacity_factory = 0.0500
        }
    }
    prerequisite = {
        focus = MKN_free_cooperatives
    }
    cost = 5
}
```

### Соляные артели — `MKN_salt_artsels`

Английское название: Salt Artels. Категория: Основная промышленная ветка.

Описание RU: Соль степи — верная валюта волостей.

Описание EN: Steppe salt is the volosts' trusted currency.

Источник: `common/national_focus/MKN.txt:509`. Стоимость: 5 (35 дней). Координаты: x=12, y=2.

Предпосылки: (Реестр взаимных обязательств [MKN_artel_register]).

Непосредственные продолжения: MKN_grain_brokers.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Политическая власть: 75
- Потенциальная постройка: industrial_complex +1

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_salt_artsels
    icon = GFX_focus_generic_mineral_prospecting
    completion_reward = {
        add_political_power = 75
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
    }
    x = 12
    y = 2
    prerequisite = {
        focus = MKN_artel_register
    }
    cost = 5
}
```

### Сельские кузницы — `MKN_village_smithies`

Английское название: Village Smithies. Категория: Основная промышленная ветка.

Описание RU: Учтём станки и навыки сельских мастеров. Оружейные артели станут первым звеном реформы разрозненного производства.

Описание EN: Catalogue village machines and skills. Armament artels begin the reform of fragmented production.

Источник: `common/national_focus/MKN.txt:564`. Стоимость: 5 (35 дней). Координаты: x=16, y=2.

Предпосылки: (Реестр взаимных обязательств [MKN_artel_register]).

Непосредственные продолжения: MKN_mobile_workshops.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Потенциальная постройка: arms_factory +1
- Изменение параметра: MKN_unified_production_factory_efficiency_gain_factor 0.0800
- Изменение параметра: MKN_unified_research_speed_factor 0.0200
- Изменение параметра: MKN_unified_industrial_capacity_factory 0.0500

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_village_smithies
    icon = GFX_focus_generic_industry_1
    completion_reward = {
        army_experience = 10
        196 = {
            if = {
                limit = {
                    is_owned_and_controlled_by = ROOT
                }
                add_building_construction = {
                    type = arms_factory
                    level = 1
                    instant_build = yes
                }
                add_extra_state_shared_building_slots = 1
            }
        }
        add_to_variable = {
            MKN_unified_production_factory_efficiency_gain_factor = 0.0800
            tooltip = MKN_unified_production_factory_efficiency_gain_factor_tt
        }
        add_to_variable = {
            MKN_unified_research_speed_factor = 0.0200
            tooltip = MKN_unified_research_speed_factor_tt
        }
        add_to_variable = {
            tooltip = MKN_unified_industrial_capacity_factory_tt
            MKN_unified_industrial_capacity_factory = 0.0500
        }
    }
    x = 16
    y = 2
    prerequisite = {
        focus = MKN_artel_register
    }
    cost = 5
}
```

### Отзывные командиры — `MKN_recallable_commanders`

Английское название: Recallable Commanders. Категория: Основная промышленная ветка.

Описание RU: Сельские сходы установят сроки мандатов и ответственность полевых командиров. Добровольность службы не означает неопределённости приказа.

Описание EN: Village assemblies set terms and responsibilities for field commanders. Voluntary service still needs clear orders.

Источник: `common/national_focus/MKN.txt:3115`. Стоимость: 5 (35 дней). Координаты: x=20, y=2.

Предпосылки: (Реестр взаимных обязательств [MKN_artel_register]).

Непосредственные продолжения: MKN_field_schools.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_unified_army_org_factor 0.0500
- Изменение параметра: MKN_unified_training_time_army_factor -0.0800
- Изменение параметра: MKN_unified_max_planning 0.0400

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_recallable_commanders
    icon = GFX_focus_generic_manpower
    x = 20
    y = 2
    available_if_capitulated = no
    ai_will_do = {
        factor = 1
    }
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    completion_reward = {
        army_experience = 10
        add_to_variable = {
            MKN_unified_army_org_factor = 0.0500
            tooltip = MKN_unified_army_org_factor_tt
        }
        add_to_variable = {
            MKN_unified_training_time_army_factor = -0.0800
            tooltip = MKN_unified_training_time_army_factor_tt
        }
        add_to_variable = {
            MKN_unified_max_planning = 0.0400
            tooltip = MKN_unified_max_planning_tt
        }
    }
    prerequisite = {
        focus = MKN_artel_register
    }
    cost = 5
}
```

### Хлебные биржи — `MKN_grain_brokers`

Английское название: Grain Exchanges. Категория: Основная промышленная ветка.

Описание RU: Хлеб — это тоже политика.

Описание EN: Grain is politics too.

Источник: `common/national_focus/MKN.txt:538`. Стоимость: 5 (35 дней). Координаты: x=12, y=3.

Предпосылки: (Соляные артели [MKN_salt_artsels]).

Непосредственные продолжения: MKN_wind_mills_steppe.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Политическая власть: 50
- Потенциальная постройка: industrial_complex +1

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_grain_brokers
    icon = GFX_focus_generic_arms_trade
    completion_reward = {
        add_political_power = 50
        196 = {
            if = {
                limit = {
                    is_owned_and_controlled_by = ROOT
                }
                add_building_construction = {
                    type = industrial_complex
                    level = 1
                    instant_build = yes
                }
                add_extra_state_shared_building_slots = 1
            }
        }
    }
    x = 12
    y = 3
    prerequisite = {
        focus = MKN_salt_artsels
    }
    cost = 5
}
```

### Передвижные мастерские — `MKN_mobile_workshops`

Английское название: Mobile Workshops. Категория: Основная промышленная ветка.

Описание RU: Обмен инструментом и ремонтные поездки укрепят общие договоры. Хозяйственный кризис ослабнет ещё на одну ступень.

Описание EN: Exchanged tools and travelling repair teams strengthen shared contracts. Economic penalties fall by another tier.

Источник: `common/national_focus/MKN.txt:633`. Стоимость: 5 (35 дней). Координаты: x=16, y=3.

Предпосылки: (Сельские кузницы [MKN_village_smithies]).

Непосредственные продолжения: MKN_rifle_concern.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_unified_political_power_gain 0.1000
- Изменение параметра: MKN_unified_consumer_goods_factor -0.0500
- Изменение параметра: MKN_unified_production_speed_buildings_factor 0.0500
- Изменение параметра: MKN_unified_industrial_capacity_factory 0.0500
- Потенциальная постройка: arms_factory +1

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_mobile_workshops
    icon = GFX_focus_generic_industry_2
    completion_reward = {
        add_equipment_to_stockpile = {
            type = motorized_equipment_1
            amount = 100
            producer = MKN
        }
        army_experience = 10
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
            tooltip = MKN_unified_industrial_capacity_factory_tt
            MKN_unified_industrial_capacity_factory = 0.0500
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
    }
    x = 16
    y = 3
    prerequisite = {
        focus = MKN_village_smithies
    }
    cost = 5
}
```

### Полевые школы коммун — `MKN_field_schools`

Английское название: Communal Field Schools. Категория: Основная промышленная ветка.

Описание RU: Передвижные инструкторы обучат отряды связи, маскировке и совместному манёвру, не отрывая деревни от посевной на месяцы.

Описание EN: Travelling instructors teach communications, concealment and joint manoeuvres without keeping villages away from sowing for months.

Источник: `common/national_focus/MKN.txt:3147`. Стоимость: 5 (35 дней). Координаты: x=20, y=3.

Предпосылки: (Отзывные командиры [MKN_recallable_commanders]).

Непосредственные продолжения: MKN_harvest_reserves.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_unified_army_org_factor 0.0600
- Изменение параметра: MKN_unified_training_time_army_factor -0.0700
- Изменение параметра: MKN_unified_max_planning 0.0300

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_field_schools
    icon = GFX_focus_generic_army_doctrines_2
    x = 20
    y = 3
    available_if_capitulated = no
    ai_will_do = {
        factor = 1
    }
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    completion_reward = {
        army_experience = 15
        add_to_variable = {
            MKN_unified_army_org_factor = 0.0600
            tooltip = MKN_unified_army_org_factor_tt
        }
        add_to_variable = {
            MKN_unified_training_time_army_factor = -0.0700
            tooltip = MKN_unified_training_time_army_factor_tt
        }
        add_to_variable = {
            MKN_unified_max_planning = 0.0300
            tooltip = MKN_unified_max_planning_tt
        }
    }
    prerequisite = {
        focus = MKN_recallable_commanders
    }
    cost = 5
}
```

### Ветряки вольных хуторов — `MKN_wind_mills_steppe`

Английское название: Windmills of Free Khutors. Категория: Основная промышленная ветка.

Описание RU: Ветер в степи бесплатный, как свобода.

Описание EN: Steppe wind is free, like freedom.

Источник: `common/national_focus/MKN.txt:602`. Стоимость: 5 (35 дней). Координаты: x=12, y=4.

Предпосылки: (Хлебные биржи [MKN_grain_brokers]).

Непосредственные продолжения: MKN_free_bazaars.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- add_stability: 0.03
- Потенциальная постройка: industrial_complex +1

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_wind_mills_steppe
    icon = GFX_focus_generic_hydroelectric_energy
    completion_reward = {
        add_stability = 0.03
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
    }
    x = 12
    y = 4
    prerequisite = {
        focus = MKN_grain_brokers
    }
    available = {
        has_completed_focus = MKN_mobile_workshops
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    cost = 5
}
```

### Артель стрелкового вооружения — `MKN_rifle_concern`

Английское название: Small Arms Artels. Категория: Основная промышленная ветка.

Описание RU: Кузни и оружейные артели Гуляй-Поля объединяются под одним качеством. Их мастерство можно расширять.\n\n§YДоступен концерн пехотного вооружения. Нанимайте его в разделе советников.§!

Описание EN: The gunsmith artels of Gulyai-Polye unite under a single standard of quality.\n\n§YAn infantry weapons concern is available. Hire it in the advisors panel.§!

Источник: `common/national_focus/MKN.txt:709`. Стоимость: 5 (35 дней). Координаты: x=16, y=4.

Предпосылки: (Передвижные мастерские [MKN_mobile_workshops]).

Непосредственные продолжения: MKN_freight_artels.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_unified_industrial_capacity_factory 0.0500
- Потенциальная постройка: arms_factory +1

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_rifle_concern
    icon = GFX_focus_generic_anti_tank_guns
    completion_reward = {
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
            tooltip = MKN_unified_industrial_capacity_factory_tt
            MKN_unified_industrial_capacity_factory = 0.0500
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
    }
    x = 16
    y = 4
    prerequisite = {
        focus = MKN_mobile_workshops
    }
    cost = 5
}
```

### Хлеб для обмена и резерва — `MKN_harvest_reserves`

Английское название: Grain for Trade and Reserves. Категория: Основная промышленная ветка.

Описание RU: Съезд решит, направить излишки на экспортные договоры или оставить их в страховых кладовых. Выбранная мера действует один год.

Описание EN: The congress chooses export contracts or insurance granaries for the surplus. The selected measure lasts one year.

Источник: `common/national_focus/MKN.txt:3179`. Стоимость: 5 (35 дней). Координаты: x=20, y=4.

Предпосылки: (Полевые школы коммун [MKN_field_schools]).

Непосредственные продолжения: MKN_mutual_credit.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- См. полную награду в completion_reward.

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_harvest_reserves
    icon = GFX_focus_generic_agricultural_subsidies
    x = 20
    y = 4
    available_if_capitulated = no
    ai_will_do = {
        factor = 1
    }
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    completion_reward = {
        country_event = {
            id = mkn.31
            days = 1
        }
    }
    prerequisite = {
        focus = MKN_field_schools
    }
    cost = 5
}
```

### Вольные базары — `MKN_free_bazaars`

Английское название: Free Bazaars. Категория: Основная промышленная ветка.

Описание RU: Торговля без газетных гонок размещает содержание страны. Все ждут базарного дня.

Описание EN: Trade without the state settles daily life. Everyone waits for market day.

Источник: `common/national_focus/MKN.txt:683`. Стоимость: 5 (35 дней). Координаты: x=12, y=5.

Предпосылки: (Ветряки вольных хуторов [MKN_wind_mills_steppe]).

Непосредственные продолжения: MKN_steppe_mint.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- add_stability: 0.03
- Потенциальная постройка: industrial_complex +1

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_free_bazaars
    icon = GFX_focus_generic_industry_investment
    completion_reward = {
        add_stability = 0.03
        226 = {
            if = {
                limit = {
                    is_owned_and_controlled_by = ROOT
                }
                add_building_construction = {
                    type = industrial_complex
                    level = 1
                    instant_build = yes
                }
                add_extra_state_shared_building_slots = 1
            }
        }
    }
    x = 12
    y = 5
    prerequisite = {
        focus = MKN_wind_mills_steppe
    }
    cost = 5
}
```

### Грузовые артели — `MKN_freight_artels`

Английское название: Freight Artels. Категория: Основная промышленная ветка.

Описание RU: Перевозчики нанесут склады и маршруты на общую карту. Перебои снабжения уменьшатся, но съезд ещё должен согласовать регулярные рейсы.

Описание EN: Carriers map depots and routes together. Supply disruptions ease, while the congress must still agree regular services.

Источник: `common/national_focus/MKN.txt:782`. Стоимость: 5 (35 дней). Координаты: x=16, y=5.

Предпосылки: (Артель стрелкового вооружения [MKN_rifle_concern]).

Непосредственные продолжения: MKN_rifle_concern_union.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Потенциальная постройка: infrastructure +1
- Изменение параметра: MKN_unified_supply_consumption_factor -0.0800
- Изменение параметра: MKN_unified_army_org_regain 0.0500

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_freight_artels
    icon = GFX_focus_generic_supply_line
    completion_reward = {
        226 = {
            if = {
                limit = {
                    is_owned_and_controlled_by = ROOT
                }
                if = {
                    limit = {
                        infrastructure < 5
                    }
                    add_building_construction = {
                        type = infrastructure
                        level = 1
                        instant_build = yes
                    }
                }
            }
        }
        add_to_variable = {
            MKN_unified_supply_consumption_factor = -0.0800
            tooltip = MKN_unified_supply_consumption_factor_tt
        }
        add_to_variable = {
            MKN_unified_army_org_regain = 0.0500
            tooltip = MKN_unified_army_org_regain_tt
        }
    }
    x = 16
    y = 5
    prerequisite = {
        focus = MKN_rifle_concern
    }
    cost = 5
}
```

### Кредит без ростовщика — `MKN_mutual_credit`

Английское название: Credit without Usury. Категория: Основная промышленная ветка.

Описание RU: Кассы взаимопомощи выдадут артельные ссуды под проверяемые договоры. Урожай и инструменты послужат основой расчётов.

Описание EN: Mutual aid funds lend against accountable artel contracts. Harvests and tools provide a basis for settlement.

Источник: `common/national_focus/MKN.txt:3202`. Стоимость: 5 (35 дней). Координаты: x=20, y=5.

Предпосылки: (Хлеб для обмена и резерва [MKN_harvest_reserves]).

Непосредственные продолжения: MKN_mobile_self_defence.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Политическая власть: 50
- add_stability: 0.02

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_mutual_credit
    icon = GFX_focus_generic_money_for_equipment
    x = 20
    y = 5
    available_if_capitulated = no
    ai_will_do = {
        factor = 1
    }
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    completion_reward = {
        add_political_power = 50
        add_stability = 0.02
    }
    prerequisite = {
        focus = MKN_harvest_reserves
    }
    cost = 5
}
```

### Степной монетный двор — `MKN_steppe_mint`

Английское название: Steppe Mint. Категория: Основная промышленная ветка.

Описание RU: Свободная чеканка на свободной земле. Никто не мешает печатать собственные билеты...

Описание EN: Free coinage on free land — and a reserve of bootleg bills when Moscow's money fails.

Источник: `common/national_focus/MKN.txt:750`. Стоимость: 5 (35 дней). Координаты: x=12, y=6.

Предпосылки: (Вольные базары [MKN_free_bazaars]).

Непосредственные продолжения: MKN_repair_exchanges.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_unified_political_power_gain 0.2000
- Потенциальная постройка: industrial_complex +1

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_steppe_mint
    icon = GFX_focus_generic_money_for_equipment
    completion_reward = {
        add_to_variable = {
            MKN_unified_political_power_gain = 0.2000
            tooltip = MKN_unified_political_power_gain_tt
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
    }
    x = 12
    y = 6
    prerequisite = {
        focus = MKN_free_bazaars
    }
    cost = 5
}
```

### Расширение оружейных артелей — `MKN_rifle_concern_union`

Английское название: Expand the Gunsmith Artels. Категория: Основная промышленная ветка.

Описание RU: Артели получили общий инструмент и школы мастеров.

Описание EN: Shared tooling and master schools upgrade the artels.

Источник: `common/national_focus/MKN.txt:819`. Стоимость: 5 (35 дней). Координаты: x=16, y=6.

Предпосылки: (Грузовые артели [MKN_freight_artels]).

Непосредственные продолжения: MKN_workshop_standards.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Потенциальная постройка: arms_factory +1

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_rifle_concern_union
    icon = GFX_focus_generic_money_for_equipment
    completion_reward = {
        if = {
            limit = {
                has_idea = MKN_rifle_concern_1
            }
            swap_ideas = {
                remove_idea = MKN_rifle_concern_1
                add_idea = MKN_rifle_concern_2
            }
        }
        if = {
            limit = {
                has_dlc = "Arms Against Tyranny"
            }
            mio:MKN_rifle_artels_organization = {
                add_mio_size = 1
                add_mio_research_bonus = 0.05
            }
        }
        if = {
            limit = {
                NOT = {
                    has_dlc = "Arms Against Tyranny"
                }
            }
            custom_effect_tooltip = MKN_rifle_concern_union_tt
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
    }
    x = 16
    y = 6
    prerequisite = {
        focus = MKN_freight_artels
    }
    cost = 5
}
```

### Подвижная самооборона — `MKN_mobile_self_defence`

Английское название: Mobile Self Defence. Категория: Основная промышленная ветка.

Описание RU: Сельские резервы объединятся в подготовленные мобильные отряды с общими сборами и сменяемым командованием.

Описание EN: Village reserves become trained mobile detachments with joint exercises and accountable command.

Источник: `common/national_focus/MKN.txt:3223`. Стоимость: 5 (35 дней). Координаты: x=20, y=6.

Предпосылки: (Кредит без ростовщика [MKN_mutual_credit]).

Непосредственные продолжения: MKN_supply_congress.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_unified_army_org_factor 0.0800
- Изменение параметра: MKN_unified_training_time_army_factor -0.1000
- Изменение параметра: MKN_unified_max_planning 0.0300
- Изменение параметра: MKN_unified_army_speed_factor 0.0500

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_mobile_self_defence
    icon = GFX_focus_generic_horse_studs
    x = 20
    y = 6
    available_if_capitulated = no
    ai_will_do = {
        factor = 1
    }
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    completion_reward = {
        army_experience = 15
        add_to_variable = {
            MKN_unified_army_org_factor = 0.0800
            tooltip = MKN_unified_army_org_factor_tt
        }
        add_to_variable = {
            MKN_unified_training_time_army_factor = -0.1000
            tooltip = MKN_unified_training_time_army_factor_tt
        }
        add_to_variable = {
            MKN_unified_max_planning = 0.0300
            tooltip = MKN_unified_max_planning_tt
        }
        add_to_variable = {
            MKN_unified_army_speed_factor = 0.0500
            tooltip = MKN_unified_army_speed_factor_tt
        }
    }
    prerequisite = {
        focus = MKN_mutual_credit
    }
    cost = 5
}
```

### Биржи инструмента и ремонта — `MKN_repair_exchanges`

Английское название: Tool and Repair Exchanges. Категория: Основная промышленная ветка.

Описание RU: Артели обменяются оснасткой, запчастями и топливом для мастерских. Малые угольные промыслы поддержат местную энергетику.

Описание EN: Artels exchange tooling, spare parts and workshop fuel. Small coal workings support local energy supplies.

Источник: `common/national_focus/MKN.txt:3259`. Стоимость: 5 (35 дней). Координаты: x=12, y=7.

Предпосылки: (Степной монетный двор [MKN_steppe_mint]).

Непосредственные продолжения: MKN_shared_orders.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Потенциальный ресурс: coal +8
- Потенциальная постройка: industrial_complex +1

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_repair_exchanges
    icon = GFX_focus_generic_industry_1
    x = 12
    y = 7
    available_if_capitulated = no
    ai_will_do = {
        factor = 1
    }
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    completion_reward = {
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
    }
    prerequisite = {
        focus = MKN_steppe_mint
    }
    cost = 5
}
```

### Договор о взаимозаменяемости — `MKN_workshop_standards`

Английское название: Interchangeability Agreement. Категория: Основная промышленная ветка.

Описание RU: Оружейные артели примут общие калибры и образцы деталей. Стандарт станет договором производителей, а не приказом единственного завода.

Описание EN: Armament artels adopt common calibres and parts. Standards become an agreement among producers rather than a single factory's command.

Источник: `common/national_focus/MKN.txt:3310`. Стоимость: 5 (35 дней). Координаты: x=16, y=7.

Предпосылки: (Расширение оружейных артелей [MKN_rifle_concern_union]).

Непосредственные продолжения: MKN_social_fund.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_unified_industrial_capacity_factory 0.0500
- Изменение параметра: MKN_unified_production_factory_efficiency_gain_factor 0.0700
- Изменение параметра: MKN_unified_research_speed_factor 0.0200

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_workshop_standards
    icon = GFX_focus_generic_industry_2
    x = 16
    y = 7
    available_if_capitulated = no
    ai_will_do = {
        factor = 1
    }
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    completion_reward = {
        add_tech_bonus = {
            bonus = 0.5
            uses = 1
            category = infantry_weapons
        }
        add_to_variable = {
            MKN_unified_industrial_capacity_factory = 0.0500
            tooltip = MKN_unified_industrial_capacity_factory_tt
        }
        add_to_variable = {
            MKN_unified_production_factory_efficiency_gain_factor = 0.0700
            tooltip = MKN_unified_production_factory_efficiency_gain_factor_tt
        }
        add_to_variable = {
            MKN_unified_research_speed_factor = 0.0200
            tooltip = MKN_unified_research_speed_factor_tt
        }
    }
    prerequisite = {
        focus = MKN_rifle_concern_union
    }
    cost = 5
}
```

### Съезд обозных артелей — `MKN_supply_congress`

Английское название: Congress of Supply Artels. Категория: Основная промышленная ветка.

Описание RU: Перевозчики согласуют резервные маршруты и помощь пострадавшим обозам. Военные перевозки получат устойчивый порядок.

Описание EN: Carriers agree alternate routes and assistance for damaged supply trains. Military transport gains reliable procedures.

Источник: `common/national_focus/MKN.txt:3346`. Стоимость: 5 (35 дней). Координаты: x=20, y=7.

Предпосылки: (Подвижная самооборона [MKN_mobile_self_defence]).

Непосредственные продолжения: MKN_communal_compact.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_unified_supply_consumption_factor -0.0700
- Изменение параметра: MKN_unified_army_org_regain 0.0600

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_supply_congress
    icon = GFX_focus_generic_supply_line
    x = 20
    y = 7
    available_if_capitulated = no
    ai_will_do = {
        factor = 1
    }
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    completion_reward = {
        add_tech_bonus = {
            bonus = 0.5
            uses = 1
            category = train_tech
        }
        add_to_variable = {
            MKN_unified_supply_consumption_factor = -0.0700
            tooltip = MKN_unified_supply_consumption_factor_tt
        }
        add_to_variable = {
            MKN_unified_army_org_regain = 0.0600
            tooltip = MKN_unified_army_org_regain_tt
        }
    }
    prerequisite = {
        focus = MKN_mobile_self_defence
    }
    available = {
        has_completed_focus = MKN_freight_artels
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    cost = 5
}
```

### Общий портфель заказов — `MKN_shared_orders`

Английское название: Shared Order Book. Категория: Основная промышленная ветка.

Описание RU: Общие стандарты и обмен инструментом позволят распределять заказы между мастерскими. Разрозненность сменится гибким освоением производства.

Описание EN: Common standards and exchanged tooling allow orders to be shared among workshops. Fragmentation gives way to flexible production.

Источник: `common/national_focus/MKN.txt:3383`. Стоимость: 5 (35 дней). Координаты: x=12, y=8.

Предпосылки: (Биржи инструмента и ремонта [MKN_repair_exchanges]).

Непосредственные продолжения: MKN_craft_federation.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_unified_industrial_capacity_factory 0.1100
- Изменение параметра: MKN_unified_production_factory_efficiency_gain_factor 0.2000
- Изменение параметра: MKN_unified_research_speed_factor 0.0400

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_shared_orders
    icon = GFX_focus_generic_military_industry
    x = 12
    y = 8
    available_if_capitulated = no
    ai_will_do = {
        factor = 1
    }
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    completion_reward = {
        add_to_variable = {
            MKN_unified_industrial_capacity_factory = 0.1100
            tooltip = MKN_unified_industrial_capacity_factory_tt
        }
        add_to_variable = {
            MKN_unified_production_factory_efficiency_gain_factor = 0.2000
            tooltip = MKN_unified_production_factory_efficiency_gain_factor_tt
        }
        add_to_variable = {
            MKN_unified_research_speed_factor = 0.0400
            tooltip = MKN_unified_research_speed_factor_tt
        }
    }
    prerequisite = {
        focus = MKN_repair_exchanges
    }
    available = {
        has_completed_focus = MKN_workshop_standards
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    cost = 5
}
```

### Страховая касса коммун — `MKN_social_fund`

Английское название: Communal Insurance Fund. Категория: Основная промышленная ветка.

Описание RU: Взносы артелей защитят семьи от неурожая, травм и потери кормильца. Общая безопасность сделает взаимопомощь надёжнее случайных пожертвований.

Описание EN: Artel contributions protect families against failed harvests, injuries and lost earners. Shared security makes mutual aid more reliable than occasional donations.

Источник: `common/national_focus/MKN.txt:3419`. Стоимость: 5 (35 дней). Координаты: x=16, y=8.

Предпосылки: (Договор о взаимозаменяемости [MKN_workshop_standards]).

Непосредственные продолжения: MKN_craft_federation.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- add_stability: 0.03
- Политическая власть: 25

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_social_fund
    icon = GFX_focus_generic_agricultural_subsidies
    x = 16
    y = 8
    available_if_capitulated = no
    ai_will_do = {
        factor = 1
    }
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    completion_reward = {
        add_stability = 0.03
        add_political_power = 25
    }
    prerequisite = {
        focus = MKN_workshop_standards
    }
    cost = 5
}
```

### Хартия хозяйственной взаимопомощи — `MKN_communal_compact`

Английское название: Charter of Economic Mutual Aid. Категория: Основная промышленная ветка.

Описание RU: Закрепим добровольные договоры, кредитные кассы и страхование. Хозяйственный кризис уступит устойчивой сети самостоятельных коммун.

Описание EN: Voluntary contracts, credit funds and insurance establish a lasting network of independent communes and resolve the economic crisis.

Источник: `common/national_focus/MKN.txt:3440`. Стоимость: 5 (35 дней). Координаты: x=20, y=8.

Предпосылки: (Съезд обозных артелей [MKN_supply_congress]).

Непосредственные продолжения: MKN_craft_federation.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_unified_political_power_gain 0.1500
- Изменение параметра: MKN_unified_consumer_goods_factor -0.1000
- Изменение параметра: MKN_unified_production_speed_buildings_factor 0.0500
- Изменение параметра: MKN_unified_stability_factor 0.0500
- Изменение параметра: MKN_unified_global_building_slots_factor 0.3000

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_communal_compact
    icon = GFX_focus_generic_diplomatic_treaty
    x = 20
    y = 8
    available_if_capitulated = no
    ai_will_do = {
        factor = 1
    }
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    completion_reward = {
        add_to_variable = {
            MKN_unified_political_power_gain = 0.1500
            tooltip = MKN_unified_political_power_gain_tt
        }
        add_to_variable = {
            MKN_unified_consumer_goods_factor = -0.1000
            tooltip = MKN_unified_consumer_goods_factor_tt
        }
        add_to_variable = {
            MKN_unified_production_speed_buildings_factor = 0.0500
            tooltip = MKN_unified_production_speed_buildings_factor_tt
        }
        add_to_variable = {
            MKN_unified_stability_factor = 0.0500
            tooltip = MKN_unified_stability_factor_tt
        }
        add_to_variable = {
            MKN_unified_global_building_slots_factor = 0.3000
            tooltip = MKN_unified_global_building_slots_factor_tt
        }
    }
    prerequisite = {
        focus = MKN_supply_congress
    }
    available = {
        has_completed_focus = MKN_social_fund
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    cost = 5
}
```

### Федерация ремесленных коммун — `MKN_craft_federation`

Английское название: Federation of Craft Communes. Категория: Основная промышленная ветка.

Описание RU: Общий заказ, страховая касса и хартия взаимопомощи завершат программу. Обозная сеть снимет последние перебои снабжения и уменьшит потери техники.

Описание EN: Shared orders, insurance and a mutual aid charter complete the program. The supply network removes remaining disruptions and reduces equipment losses.

Источник: `common/national_focus/MKN.txt:904`. Стоимость: 5 (35 дней). Координаты: x=16, y=9.

Предпосылки: (Общий портфель заказов [MKN_shared_orders]) И (Страховая касса коммун [MKN_social_fund]) И (Хартия хозяйственной взаимопомощи [MKN_communal_compact]).

Непосредственные продолжения: нет.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Потенциальная постройка: industrial_complex +1
- add_stability: 0.03
- Изменение параметра: MKN_unified_supply_consumption_factor -0.1300
- Изменение параметра: MKN_unified_army_org_regain 0.0400
- Изменение параметра: MKN_unified_attrition -0.0500

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_craft_federation
    icon = GFX_focus_generic_industry_investment
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
        add_stability = 0.03
        add_to_variable = {
            MKN_unified_supply_consumption_factor = -0.1300
            tooltip = MKN_unified_supply_consumption_factor_tt
        }
        add_to_variable = {
            MKN_unified_army_org_regain = 0.0400
            tooltip = MKN_unified_army_org_regain_tt
        }
        add_to_variable = {
            MKN_unified_attrition = -0.0500
            tooltip = MKN_unified_attrition_tt
        }
    }
    x = 16
    y = 9
    prerequisite = {
        focus = MKN_shared_orders
    }
    prerequisite = {
        focus = MKN_social_fund
    }
    prerequisite = {
        focus = MKN_communal_compact
    }
    cost = 5
}
```

### Технические коммуны — `MKN_technical_communes`

Английское название: Technical Communes. Категория: Бонус промышленным технологиям.

Описание RU: Учёные и мастера создадут общую сеть технических школ, доступную при любой форме хозяйства.

Описание EN: Scientists and craftsmen establish a technical school network under either economic model.

Источник: `common/national_focus/MKN.txt:2507`. Стоимость: 5 (35 дней). Координаты: x=27, y=1.

Предпосылки: нет нарисованной предпосылки; см. available.

Непосредственные продолжения: MKN_workshop_airplane_artels, MKN_polytechnic_institute.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Политическая власть: 50

Полное определение; включает точные награды, условия, взаимоисключения и AI:

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

### Сельские аэродромы — `MKN_village_airfields`

Английское название: Village Airfields. Категория: Строительство, ресурсы или исследовательская мощность.

Описание RU: Полевые полосы приблизят авиацию к войскам и сократят бесполезные перелёты.

Описание EN: Forward strips will bring aircraft closer to troops and reduce ferry flights.

Источник: `common/national_focus/MKN.txt:2213`. Стоимость: 5 (35 дней). Координаты: x=66, y=1.

Предпосылки: (Степные соколы [MKN_steppe_hawks]).

Непосредственные продолжения: MKN_gulyaipole_pilot_school.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_air_air_range_factor 0.05
- Потенциальная постройка: air_base +2

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_village_airfields
    x = 66
    y = 1
    available_if_capitulated = no
    ai_will_do = {
        factor = 1
    }
    prerequisite = {
        focus = MKN_steppe_hawks
    }
    icon = GFX_focus_generic_air_bases
    completion_reward = {
        add_to_variable = {
            MKN_air_air_range_factor = 0.05
            tooltip = MKN_air_air_range_factor_tt
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
    }
    cost = 5
}
```

### Вольный политехникум — `MKN_polytechnic_institute`

Английское название: Free Polytechnic. Категория: Бонус промышленным технологиям.

Описание RU: Инженерное образование даст артелям свои станки, измерительные приборы и специалистов.

Описание EN: Engineering education supplies the artels with machine tools, instruments and trained specialists.

Источник: `common/national_focus/MKN.txt:2522`. Стоимость: 5 (35 дней). Координаты: x=27, y=2.

Предпосылки: (Технические коммуны [MKN_technical_communes]).

Непосредственные продолжения: MKN_communal_research_network.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- См. полную награду в completion_reward.

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_polytechnic_institute
    icon = GFX_focus_research
    prerequisite = {
        focus = MKN_technical_communes
    }
    completion_reward = {
        add_tech_bonus = {
            bonus = 0.5
            uses = 2
            category = industry
        }
    }
    x = 27
    y = 2
    cost = 5
}
```

### Херсонские верфи — `MKN_kherson_shipyard`

Английское название: Kherson Shipyards. Категория: Строительство, ресурсы или исследовательская мощность; Открывает/развивает предприятие или MIO.

Описание RU: Херсонские верфи дадут флотилии собственную строительную и ремонтную базу.

Описание EN: Kherson yards will give the flotilla its own construction and repair base.

Источник: `common/national_focus/MKN.txt:2364`. Стоимость: 5 (35 дней). Координаты: x=82, y=2.

Предпосылки: (Днепровский дозор [MKN_dnieper_patrol]).

Непосредственные продолжения: MKN_coastal_defense_steppe, MKN_black_sea_smugglers.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_navy_industrial_capacity_dockyard 0.05
- Потенциальная постройка: dockyard +1

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_kherson_shipyard
    x = 82
    y = 2
    available_if_capitulated = no
    ai_will_do = {
        factor = 1
    }
    prerequisite = {
        focus = MKN_dnieper_patrol
    }
    icon = GFX_goal_generic_construct_naval_dockyard
    completion_reward = {
        add_to_variable = {
            MKN_navy_industrial_capacity_dockyard = 0.05
            tooltip = MKN_navy_industrial_capacity_dockyard_tt
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
    }
    available = {
        196 = {
            is_owned_and_controlled_by = ROOT
        }
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    cost = 5
}
```

### Сеть исследовательских коммун — `MKN_communal_research_network`

Английское название: Communal Research Network. Категория: Строительство, ресурсы или исследовательская мощность.

Описание RU: Объединим лаборатории в постоянную исследовательскую сеть.

Описание EN: Link local laboratories into a permanent research network.

Источник: `common/national_focus/MKN.txt:2539`. Стоимость: 5 (35 дней). Координаты: x=27, y=3.

Предпосылки: (Вольный политехникум [MKN_polytechnic_institute]).

Непосредственные продолжения: нет.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- add_research_slot: 1

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_communal_research_network
    icon = GFX_focus_research
    prerequisite = {
        focus = MKN_polytechnic_institute
    }
    completion_reward = {
        if = {
            limit = {
                amount_research_slots < 5
            }
            add_research_slot = 1
        }
    }
    x = 27
    y = 3
    cost = 5
}
```

### Федерация «Набат» — `MKN_nabat_federation`

Английское название: The Nabat Federation. Категория: Бонус промышленным технологиям.

Описание RU: Анархистские федерации от Харькова до Одессы смотрят на Гуляй-Поле.

Описание EN: Anarchist federations from Kharkov to Odessa look to Gulyai-Polye.

Источник: `common/national_focus/MKN.txt:994`. Стоимость: 5 (35 дней). Координаты: x=36, y=3.

Предпосылки: (Вольная территория [MKN_the_free_territory]).

Непосредственные продолжения: MKN_black_banner_east.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Политическая власть: 80

Полное определение; включает точные награды, условия, взаимоисключения и AI:

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

### Стальные кони — `MKN_steel_horses`

Английское название: Iron Horses. Категория: Открывает/развивает предприятие или MIO.

Описание RU: Тракторные артели освоят бронетехнику для прорыва, но ей нужны экипажи и горючее.

Описание EN: Tractor cooperatives will develop breakthrough armour that needs trained crews and fuel.

Источник: `common/national_focus/MKN.txt:2082`. Стоимость: 5 (35 дней). Координаты: x=46, y=3.

Предпосылки: (Штаб степных армий [MKN_steppe_general_staff]).

Непосредственные продолжения: MKN_steppe_quartermasters, MKN_tank_crews.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_army_army_armor_attack_factor 0.05

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_steel_horses
    x = 46
    y = 3
    available_if_capitulated = no
    prerequisite = {
        focus = MKN_steppe_general_staff
    }
    mutually_exclusive = {
        focus = MKN_batko_cavalry
    }
    icon = GFX_focus_MKN_company_kommunar
    completion_reward = {
        add_to_variable = {
            MKN_army_army_armor_attack_factor = 0.05
            tooltip = MKN_army_army_armor_attack_factor_tt
        }
        add_tech_bonus = {
            name = MKN_steel_horses
            bonus = 0.75
            uses = 1
            category = armor
        }
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Береговой защитный пояс — `MKN_coastal_defense_steppe`

Английское название: Coastal Defence Belt. Категория: Строительство, ресурсы или исследовательская мощность.

Описание RU: Защитим подходы к портам и сделаем зерновую торговлю главной задачей флота.

Описание EN: Defend port approaches and make grain shipping the navy's main mission.

Источник: `common/national_focus/MKN.txt:2404`. Стоимость: 5 (35 дней). Координаты: x=78, y=3.

Предпосылки: (Херсонские верфи [MKN_kherson_shipyard]).

Непосредственные продолжения: MKN_dnieper_gun_flotilla, MKN_black_sea_escorts.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_navy_convoy_escort_efficiency 0.1
- Потенциальная постройка: coastal_bunker +1

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_coastal_defense_steppe
    x = 78
    y = 3
    available_if_capitulated = no
    prerequisite = {
        focus = MKN_kherson_shipyard
    }
    mutually_exclusive = {
        focus = MKN_black_sea_smugglers
    }
    icon = GFX_focus_generic_coastal_fort
    completion_reward = {
        add_to_variable = {
            MKN_navy_convoy_escort_efficiency = 0.1
            tooltip = MKN_navy_convoy_escort_efficiency_tt
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
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Артельные авиамастерские — `MKN_workshop_airplane_artels`

Английское название: Artel Aviation Workshops. Категория: Строительство, ресурсы или исследовательская мощность.

Описание RU: Разъездные авиамастерские ремонтируют и сколачивают машины прямо под открытым небом.

Описание EN: Itinerant aviation workshops repair and assemble machines in the open air.

Источник: `common/national_focus/MKN.txt:873`. Стоимость: 5 (35 дней). Координаты: x=27, y=4.

Предпосылки: (Технические коммуны [MKN_technical_communes]).

Непосредственные продолжения: MKN_advanced_research.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Потенциальная постройка: arms_factory +1

Полное определение; включает точные награды, условия, взаимоисключения и AI:

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

Английское название: Shadow Republic. Категория: Бонус промышленным технологиям.

Описание RU: Государство, которое почти никогда не спорит вслух, но всегда чувствуется в воздухе.

Описание EN: The state that never quite appears, but is always felt.

Источник: `common/national_focus/MKN.txt:1012`. Стоимость: 5 (35 дней). Координаты: x=32, y=4.

Предпосылки: (Крестьяне и рабочие [MKN_farmers_and_workers]).

Непосредственные продолжения: нет.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- См. полную награду в completion_reward.

Полное определение; включает точные награды, условия, взаимоисключения и AI:

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

### Гуляйпольская коммуна — `MKN_gulyai_polye_commune`

Английское название: Gulyai-Polye Commune. Категория: Строительство, ресурсы или исследовательская мощность.

Описание RU: Столица анархии покажет миру иной способ жить.

Описание EN: The capital of anarchy will show the world a different way to live.

Источник: `common/national_focus/MKN.txt:1030`. Стоимость: 5 (35 дней). Координаты: x=34, y=4.

Предпосылки: (Вольные советы [MKN_free_soviets]).

Непосредственные продолжения: MKN_anarchist_schools.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Политическая власть: 50
- Потенциальная постройка: industrial_complex +1

Полное определение; включает точные награды, условия, взаимоисключения и AI:

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

### Сельские сборные пункты — `MKN_village_muster`

Английское название: Village Muster Points. Категория: Открывает/развивает предприятие или MIO.

Описание RU: Сельские сборные пункты заранее распределят людей по отрядам.

Описание EN: Village mustering stations will assign recruits to detachments in advance.

Источник: `common/national_focus/MKN.txt:3973`. Стоимость: 5 (35 дней). Координаты: x=52, y=4.

Предпосылки: (Конница Батьки [MKN_batko_cavalry]).

Непосредственные продолжения: MKN_machinegun_carts.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_army_mobilization_speed 0.15

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_village_muster
    available_if_capitulated = no
    icon = GFX_focus_generic_manpower
    completion_reward = {
        add_to_variable = {
            MKN_army_mobilization_speed = 0.15
            tooltip = MKN_army_mobilization_speed_tt
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
    }
    x = 52
    y = 4
    prerequisite = {
        focus = MKN_batko_cavalry
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Артели истребителей — `MKN_aircraft_artels`

Английское название: Fighter Artels. Категория: Открывает/развивает предприятие или MIO.

Описание RU: Лёгкие планеры артели «Степной сокол» приспособят для манёвренного перехвата.

Описание EN: Steppe Falcon cooperatives will adapt light airframes for agile interception.

Источник: `common/national_focus/MKN.txt:2626`. Стоимость: 5 (35 дней). Координаты: x=60, y=4.

Предпосылки: (Чёрный рой [MKN_black_swarm]).

Непосредственные продолжения: MKN_fighter_instructors.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_air_air_agility_factor 0.04

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_aircraft_artels
    available_if_capitulated = no
    icon = GFX_focus_MKN_company_air_artels
    completion_reward = {
        add_to_variable = {
            MKN_air_air_agility_factor = 0.04
            tooltip = MKN_air_air_agility_factor_tt
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
    }
    x = 60
    y = 4
    prerequisite = {
        focus = MKN_black_swarm
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Артели штурмовой авиации — `MKN_attack_air_artels`

Английское название: Attack Aircraft Artels. Категория: Открывает/развивает предприятие или MIO.

Описание RU: «Днепровское крыло» приспособит лёгкие самолёты для ударов по наземным целям.

Описание EN: Dnipro Wing cooperatives will adapt light aircraft for ground attack.

Источник: `common/national_focus/MKN.txt:5077`. Стоимость: 5 (35 дней). Координаты: x=68, y=4.

Предпосылки: (Авиация поддержки [MKN_close_support_program]).

Непосредственные продолжения: MKN_bombing_ranges.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_air_air_attack_factor 0.04

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_attack_air_artels
    available_if_capitulated = no
    icon = GFX_focus_MKN_company_attack_air_artels
    completion_reward = {
        add_to_variable = {
            MKN_air_air_attack_factor = 0.04
            tooltip = MKN_air_air_attack_factor_tt
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
    }
    x = 68
    y = 4
    prerequisite = {
        focus = MKN_close_support_program
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Школа подводных экипажей — `MKN_submarine_crews`

Английское название: Submarine Crew School. Категория: Открывает/развивает предприятие или MIO.

Описание RU: Экипажи научатся выбирать цель и момент атаки, а не искать открытого боя.

Описание EN: Crews will choose targets and timing rather than seek open battle.

Источник: `common/national_focus/MKN.txt:6253`. Стоимость: 5 (35 дней). Координаты: x=88, y=4.

Предпосылки: (Школа черноморских рейдеров [MKN_black_sea_smugglers]).

Непосредственные продолжения: MKN_naval_intelligence.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_navy_navy_submarine_attack_factor 0.05

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_submarine_crews
    available_if_capitulated = no
    icon = GFX_focus_MKN_company_submarine_works
    completion_reward = {
        add_to_variable = {
            MKN_navy_navy_submarine_attack_factor = 0.05
            tooltip = MKN_navy_navy_submarine_attack_factor_tt
        }
        navy_experience = 20
        add_doctrine_cost_reduction = {
            name = MKN_submarine_crews
            cost_reduction = 0.5
            uses = 1
            category = naval_doctrine
        }
    }
    x = 88
    y = 4
    prerequisite = {
        focus = MKN_black_sea_smugglers
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Высшая техническая школа — `MKN_advanced_research`

Английское название: Advanced Technical School. Категория: Строительство, ресурсы или исследовательская мощность.

Описание RU: Новые кафедры авиации и металлургии создадут вторую исследовательскую группу.

Описание EN: New aviation and metallurgy departments establish a second research team.

Источник: `common/national_focus/MKN.txt:2557`. Стоимость: 5 (35 дней). Координаты: x=27, y=5.

Предпосылки: (Артельные авиамастерские [MKN_workshop_airplane_artels]).

Непосредственные продолжения: нет.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- add_research_slot: 1

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_advanced_research
    icon = GFX_focus_research
    prerequisite = {
        focus = MKN_workshop_airplane_artels
    }
    completion_reward = {
        if = {
            limit = {
                amount_research_slots < 5
            }
            add_research_slot = 1
        }
    }
    x = 27
    y = 5
    cost = 5
}
```

### Анархистские школы — `MKN_anarchist_schools`

Английское название: Anarchist Schools. Категория: Бонус промышленным технологиям.

Описание RU: Школы Феррера для свободных детей.

Описание EN: Ferrer schools for free children.

Источник: `common/national_focus/MKN.txt:1075`. Стоимость: 5 (35 дней). Координаты: x=34, y=5.

Предпосылки: (Гуляйпольская коммуна [MKN_gulyai_polye_commune]).

Непосредственные продолжения: MKN_peasant_militias, MKN_the_steppe_holds.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- См. полную награду в completion_reward.

Полное определение; включает точные награды, условия, взаимоисключения и AI:

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

### Пулемётные повозки — `MKN_machinegun_carts`

Английское название: Machine Gun Carts. Категория: Открывает/развивает предприятие или MIO.

Описание RU: Пулемётные тачанки дадут конным отрядам огневую опору.

Описание EN: Machine-gun carts will provide cavalry detachments with sustained firepower.

Источник: `common/national_focus/MKN.txt:4028`. Стоимость: 5 (35 дней). Координаты: x=52, y=5.

Предпосылки: (Сельские сборные пункты [MKN_village_muster]).

Непосредственные продолжения: MKN_scout_parties.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_army_modifier_army_sub_unit_cavalry_attack_factor 0.07

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_machinegun_carts
    available_if_capitulated = no
    icon = GFX_goal_generic_small_arms
    completion_reward = {
        add_to_variable = {
            MKN_army_modifier_army_sub_unit_cavalry_attack_factor = 0.07
            tooltip = MKN_army_modifier_army_sub_unit_cavalry_attack_factor_tt
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
    }
    x = 52
    y = 5
    prerequisite = {
        focus = MKN_village_muster
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Единая воздушная тревога — `MKN_air_warning`

Английское название: Unified Air Warning. Категория: Бонус промышленным технологиям.

Описание RU: Единая тревога поднимет нужные звенья вместо всей авиации сразу.

Описание EN: A shared warning system will scramble the right flights without exhausting the whole air force.

Источник: `common/national_focus/MKN.txt:4560`. Стоимость: 5 (35 дней). Координаты: x=64, y=5.

Предпосылки: (Сеть наблюдательных постов [MKN_observation_posts]).

Непосредственные продолжения: MKN_airframe_jigs.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_air_air_intercept_efficiency 0.05

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_air_warning
    available_if_capitulated = no
    icon = GFX_focus_generic_radio_communication
    completion_reward = {
        add_to_variable = {
            MKN_air_air_intercept_efficiency = 0.05
            tooltip = MKN_air_air_intercept_efficiency_tt
        }
        add_tech_bonus = {
            name = MKN_air_warning
            bonus = 0.5
            uses = 1
            category = electronics
        }
    }
    x = 64
    y = 5
    prerequisite = {
        focus = MKN_observation_posts
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Передовые посадочные полосы — `MKN_forward_airstrips`

Английское название: Forward Airstrips. Категория: Строительство, ресурсы или исследовательская мощность.

Описание RU: Передовые полосы сократят время между запросом поддержки и ударом.

Описание EN: Forward strips will shorten the delay between a support request and the strike.

Источник: `common/national_focus/MKN.txt:5159`. Стоимость: 5 (35 дней). Координаты: x=72, y=5.

Предпосылки: (Связные при наземных штабах [MKN_air_ground_liaisons]).

Непосредственные продолжения: MKN_cas_maintenance.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_air_air_range_factor 0.08
- Потенциальная постройка: air_base +2

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_forward_airstrips
    available_if_capitulated = no
    icon = GFX_focus_generic_air_bases
    completion_reward = {
        add_to_variable = {
            MKN_air_air_range_factor = 0.08
            tooltip = MKN_air_air_range_factor_tt
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
    }
    x = 72
    y = 5
    prerequisite = {
        focus = MKN_air_ground_liaisons
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Скрытые рейдерские стоянки — `MKN_hidden_anchorages`

Английское название: Hidden Raider Anchorages. Категория: Строительство, ресурсы или исследовательская мощность.

Описание RU: Тайные стоянки позволят подготовить выход, не выдавая расположение рейдеров.

Описание EN: Concealed anchorages will prepare sorties without exposing raider positions.

Источник: `common/national_focus/MKN.txt:6280`. Стоимость: 5 (35 дней). Координаты: x=84, y=5.

Предпосылки: (Торпедные мастерские [MKN_torpedo_artels]).

Непосредственные продолжения: MKN_raider_dockyard.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_navy_naval_torpedo_reveal_chance_factor -0.08
- Потенциальная постройка: naval_base +1

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_hidden_anchorages
    available_if_capitulated = no
    icon = GFX_focus_generic_infiltration
    completion_reward = {
        add_to_variable = {
            MKN_navy_naval_torpedo_reveal_chance_factor = -0.08
            tooltip = MKN_navy_naval_torpedo_reveal_chance_factor_tt
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
    }
    x = 84
    y = 5
    prerequisite = {
        focus = MKN_torpedo_artels
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Разорвать связи с городом — `MKN_sever_urban_ties`

Английское название: Sever Urban Ties. Категория: Изменяет общий экономический дух MKN.

Описание RU: Закроем экспортные книги и распустим соперничающие делегации. Упраздним баланс сил, введём закрытую экономику и оставим больше продукции сёлам.

Описание EN: Close the export ledgers and dismiss the competing delegations. Abolish the balance of power, adopt a closed economy and reserve more output for the villages.

Источник: `common/national_focus/MKN.txt:7684`. Стоимость: 5 (35 дней). Координаты: x=112, y=5.

Предпосылки: (Зерновой ультиматум [MKN_grain_ultimatum]).

Непосредственные продолжения: MKN_every_farm_a_fortress.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- add_ideas: closed_economy
- Изменение параметра: MKN_unified_consumer_goods_factor -0.05

Полное определение; включает точные награды, условия, взаимоисключения и AI:

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

### Полевой ремонт брони — `MKN_tank_maintenance`

Английское название: Field Armour Repair. Категория: Строительство, ресурсы или исследовательская мощность; Открывает/развивает предприятие или MIO.

Описание RU: Ремонтная база Днепра обеспечит запасные узлы и восстановление техники.

Описание EN: A Dnipro repair plant will provide replacement assemblies and equipment repairs.

Источник: `common/national_focus/MKN.txt:3577`. Стоимость: 5 (35 дней). Координаты: x=48, y=6.

Предпосылки: (Моторизованные обозы [MKN_mobile_supply_columns]).

Непосредственные продолжения: MKN_fire_tables.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_army_repair_speed_factor 0.1
- Потенциальная постройка: arms_factory +1

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_tank_maintenance
    available_if_capitulated = no
    icon = GFX_focus_generic_industrial_experts
    completion_reward = {
        add_to_variable = {
            MKN_army_repair_speed_factor = 0.1
            tooltip = MKN_army_repair_speed_factor_tt
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
    }
    x = 48
    y = 6
    prerequisite = {
        focus = MKN_mobile_supply_columns
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Оснастка для лёгких планеров — `MKN_airframe_jigs`

Английское название: Light Airframe Jigs. Категория: Строительство, ресурсы или исследовательская мощность.

Описание RU: Серийная оснастка обеспечит точную сборку и вооружение истребителей.

Описание EN: Production jigs will improve fighter assembly and armament.

Источник: `common/national_focus/MKN.txt:4612`. Стоимость: 5 (35 дней). Координаты: x=64, y=6.

Предпосылки: (Единая воздушная тревога [MKN_air_warning]).

Непосредственные продолжения: MKN_aircraft_recovery.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_air_air_attack_factor 0.04
- Потенциальная постройка: arms_factory +1

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_airframe_jigs
    available_if_capitulated = no
    icon = GFX_focus_generic_aircraft_production
    completion_reward = {
        add_to_variable = {
            MKN_air_air_attack_factor = 0.04
            tooltip = MKN_air_air_attack_factor_tt
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
    }
    x = 64
    y = 6
    prerequisite = {
        focus = MKN_air_warning
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Ремонт штурмовиков у фронта — `MKN_cas_maintenance`

Английское название: Frontline Attack Aircraft Repair. Категория: Строительство, ресурсы или исследовательская мощность.

Описание RU: Прифронтовые мастерские восстановят повреждения от наземного огня.

Описание EN: Front-line workshops will repair damage inflicted by ground fire.

Источник: `common/national_focus/MKN.txt:5230`. Стоимость: 5 (35 дней). Координаты: x=72, y=6.

Предпосылки: (Передовые посадочные полосы [MKN_forward_airstrips]).

Непосредственные продолжения: MKN_flying_artillery.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_air_air_accidents_factor -0.08
- Потенциальная постройка: arms_factory +1

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_cas_maintenance
    available_if_capitulated = no
    icon = GFX_focus_generic_industrial_experts
    completion_reward = {
        add_to_variable = {
            MKN_air_air_accidents_factor = -0.08
            tooltip = MKN_air_air_accidents_factor_tt
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
    }
    x = 72
    y = 6
    prerequisite = {
        focus = MKN_forward_airstrips
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Расчистка портовых фарватеров — `MKN_harbour_dredging`

Английское название: Harbour Channel Dredging. Категория: Строительство, ресурсы или исследовательская мощность.

Описание RU: Расчищенные фарватеры ускорят оборот кораблей и портовое снабжение.

Описание EN: Dredged channels will improve ship turnaround and harbour logistics.

Источник: `common/national_focus/MKN.txt:5725`. Стоимость: 5 (35 дней). Координаты: x=76, y=6.

Предпосылки: (Береговые сигнальные посты [MKN_coastal_signal_posts]).

Непосредственные продолжения: MKN_depth_charge_school.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_navy_navy_fuel_consumption_factor -0.08
- Потенциальная постройка: naval_base +1

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_harbour_dredging
    available_if_capitulated = no
    icon = GFX_focus_generic_public_works
    completion_reward = {
        add_to_variable = {
            MKN_navy_navy_fuel_consumption_factor = -0.08
            tooltip = MKN_navy_navy_fuel_consumption_factor_tt
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
    }
    x = 76
    y = 6
    prerequisite = {
        focus = MKN_coastal_signal_posts
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Мастерская малых подлодок — `MKN_raider_dockyard`

Английское название: Small Submarine Yard. Категория: Строительство, ресурсы или исследовательская мощность.

Описание RU: Лиманские мастерские наладят серийное строительство малых подлодок.

Описание EN: Estuary workshops will organize serial construction of small submarines.

Источник: `common/national_focus/MKN.txt:6339`. Стоимость: 5 (35 дней). Координаты: x=84, y=6.

Предпосылки: (Скрытые рейдерские стоянки [MKN_hidden_anchorages]).

Непосредственные продолжения: MKN_night_sorties.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_navy_industrial_capacity_dockyard 0.05
- Потенциальная постройка: dockyard +1

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_raider_dockyard
    available_if_capitulated = no
    icon = GFX_goal_generic_construct_naval_dockyard
    completion_reward = {
        add_to_variable = {
            MKN_navy_industrial_capacity_dockyard = 0.05
            tooltip = MKN_navy_industrial_capacity_dockyard_tt
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
    }
    x = 84
    y = 6
    prerequisite = {
        focus = MKN_hidden_anchorages
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Милитаризовать коммуны — `MKN_militarize_communes`

Английское название: Militarize the Communes. Категория: Изменяет общий экономический дух MKN.

Описание RU: Каждая коммуна будет держать призывной список рядом с зерновой книгой. Расширим набор, заплатив за это новым ударом по доверию общин.

Описание EN: Every commune must keep a muster roll beside its grain ledger. Broaden recruitment, at the price of another wound to communal confidence.

Источник: `common/national_focus/MKN.txt:7173`. Стоимость: 5 (35 дней). Координаты: x=100, y=6.

Предпосылки: (Отменить выборность командиров [MKN_abolish_election_of_commanders]).

Непосредственные продолжения: MKN_standardize_workshops.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_army_conscription 0.02
- Изменение параметра: MKN_unified_stability_factor -0.05

Полное определение; включает точные награды, условия, взаимоисключения и AI:

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

### Утвердить Харьковский договор — `MKN_conclude_kharkiv_treaty`

Английское название: Ratify the Kharkiv Treaty. Категория: Строительство, ресурсы или исследовательская мощность.

Описание RU: Подписи из Харькова не вернут погибших, но дадут уцелевшим приграничным сёлам два года мирного сева. Мастерские вернутся к гражданским заказам, а делегаты повезут договор домой по тем же путям, по которым прежде доставляли боеприпасы.

Описание EN: The signatures from Kharkiv cannot erase the dead, but they can give the surviving frontier villages two years to sow in peace. Workshops will return to civilian orders, and delegates will carry the pact home along the same tracks that once brought ammunition.

Источник: `common/national_focus/MKN_frontier_focuses.txt:259`. Стоимость: 5 (35 дней). Координаты: x=134, y=6.

Предпосылки: нет нарисованной предпосылки; см. available.

Непосредственные продолжения: нет.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- add_stability: 0.10
- Потенциальная постройка: industrial_complex +2

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_conclude_kharkiv_treaty
    icon = GFX_focus_MKN_conclude_kharkiv_treaty
    mutually_exclusive = {
        focus = MKN_conclude_total_war
    }
    x = 134
    y = 6
    available_if_capitulated = no
    cancel_if_invalid = yes
    continue_if_invalid = no
    available = {
        has_completed_focus = MKN_ukrainian_frontier_root
        has_country_flag = mkn_ukr_frontier_concluded
        has_country_flag = mkn_ukr_pact_signed
        NOT = {
            has_war_with = UKR
        }
        NOT = {
            has_war_with = SOV
        }
        any_owned_state = {
            is_controlled_by = ROOT
            is_core_of = ROOT
        }
    }
    cancel = {
        OR = {
            NOT = {
                has_country_flag = mkn_ukr_pact_signed
            }
            has_war_with = UKR
            has_war_with = SOV
        }
    }
    search_filters = {
        FOCUS_FILTER_INDUSTRY
        FOCUS_FILTER_STABILITY
    }
    completion_reward = {
        add_stability = 0.10
        random_owned_controlled_state = {
            limit = {
                is_core_of = ROOT
            }
            prioritize = {
                1082
                226
                196
                225
            }
            add_extra_state_shared_building_slots = 2
            add_building_construction = {
                type = industrial_complex
                level = 2
                instant_build = yes
            }
        }
        set_country_flag = mkn_ukr_treaty_reconstruction_completed
    }
    ai_will_do = {
        factor = 5
    }
    cost = 5
}
```

### Артиллерийские артели — `MKN_artillery_artels`

Английское название: Artillery Artels. Категория: Открывает/развивает предприятие или MIO.

Описание RU: Никопольские артели наладят орудия для сопровождения наступающей пехоты.

Описание EN: Nikopol workshops will manufacture guns to support advancing infantry.

Источник: `common/national_focus/MKN.txt:2575`. Стоимость: 5 (35 дней). Координаты: x=44, y=7.

Предпосылки: (Тягачи для эвакуации [MKN_recovery_tractors]).

Непосредственные продолжения: MKN_bridge_columns, MKN_mechanized_compact.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_army_modifier_army_sub_unit_infantry_attack_factor 0.04

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_artillery_artels
    available_if_capitulated = no
    icon = GFX_focus_MKN_company_artillery_works
    completion_reward = {
        add_to_variable = {
            MKN_army_modifier_army_sub_unit_infantry_attack_factor = 0.04
            tooltip = MKN_army_modifier_army_sub_unit_infantry_attack_factor_tt
        }
        add_tech_bonus = {
            name = MKN_artillery_artels
            bonus = 0.75
            uses = 1
            category = artillery
        }
    }
    x = 44
    y = 7
    prerequisite = {
        focus = MKN_recovery_tractors
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Общие таблицы огня — `MKN_fire_tables`

Английское название: Common Fire Tables. Категория: Открывает/развивает предприятие или MIO.

Описание RU: Единые таблицы стрельбы свяжут огонь батарей с планами танковых командиров.

Описание EN: Common firing tables will align battery fire with armoured commanders' plans.

Источник: `common/national_focus/MKN.txt:3628`. Стоимость: 5 (35 дней). Координаты: x=48, y=7.

Предпосылки: (Полевой ремонт брони [MKN_tank_maintenance]).

Непосредственные продолжения: MKN_motorized_infantry, MKN_mechanized_compact.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_army_max_planning 0.05

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_fire_tables
    available_if_capitulated = no
    icon = GFX_goal_generic_army_artillery2
    completion_reward = {
        add_to_variable = {
            MKN_army_max_planning = 0.05
            tooltip = MKN_army_max_planning_tt
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
    }
    x = 48
    y = 7
    prerequisite = {
        focus = MKN_tank_maintenance
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Перехват парами — `MKN_interceptor_pairs`

Английское название: Paired Interception. Категория: Открывает/развивает предприятие или MIO.

Описание RU: Ведущий прикрывает ведомого: одиночный герой уступит место слаженной паре.

Описание EN: Leaders and wingmen will replace lone heroics with coordinated pairs.

Источник: `common/national_focus/MKN.txt:4645`. Стоимость: 5 (35 дней). Координаты: x=60, y=7.

Предпосылки: (Радиомаяки полевых полос [MKN_radio_beacons]).

Непосредственные продолжения: MKN_air_dispersal, MKN_free_sky_compact.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_air_air_agility_factor 0.04

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_interceptor_pairs
    available_if_capitulated = no
    icon = GFX_goal_generic_air_fighter2
    completion_reward = {
        add_to_variable = {
            MKN_air_air_agility_factor = 0.04
            tooltip = MKN_air_air_agility_factor_tt
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
    }
    x = 60
    y = 7
    prerequisite = {
        focus = MKN_radio_beacons
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Летающая артиллерия — `MKN_flying_artillery`

Английское название: Flying Artillery. Категория: Открывает/развивает предприятие или MIO.

Описание RU: Тяжёлое вооружение штурмовиков поможет разрушать узлы сопротивления.

Описание EN: Heavier aircraft armament will break enemy strongpoints.

Источник: `common/national_focus/MKN.txt:5284`. Стоимость: 5 (35 дней). Координаты: x=72, y=7.

Предпосылки: (Ремонт штурмовиков у фронта [MKN_cas_maintenance]).

Непосредственные продолжения: MKN_tactical_recon, MKN_air_support_compact.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_air_air_cas_efficiency 0.05

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_flying_artillery
    available_if_capitulated = no
    icon = GFX_focus_generic_armored_air_support
    completion_reward = {
        add_to_variable = {
            MKN_air_air_cas_efficiency = 0.05
            tooltip = MKN_air_air_cas_efficiency_tt
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
    }
    x = 72
    y = 7
    prerequisite = {
        focus = MKN_cas_maintenance
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Школа глубинных бомб — `MKN_depth_charge_school`

Английское название: Depth Charge School. Категория: Открывает/развивает предприятие или MIO.

Описание RU: Гидроакустики и расчёты глубинных бомб будут работать одной командой.

Описание EN: Sonar operators and depth-charge crews will work as one team.

Источник: `common/national_focus/MKN.txt:5797`. Стоимость: 5 (35 дней). Координаты: x=76, y=7.

Предпосылки: (Расчистка портовых фарватеров [MKN_harbour_dredging]).

Непосредственные продолжения: MKN_fleet_damage_control, MKN_escort_compact.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_navy_navy_submarine_detection_factor 0.15

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_depth_charge_school
    available_if_capitulated = no
    icon = GFX_goal_generic_navy_anti_submarine
    completion_reward = {
        add_to_variable = {
            MKN_navy_navy_submarine_detection_factor = 0.15
            tooltip = MKN_navy_navy_submarine_detection_factor_tt
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
    }
    x = 76
    y = 7
    prerequisite = {
        focus = MKN_harbour_dredging
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Ночные выходы — `MKN_night_sorties`

Английское название: Night Sorties. Категория: Открывает/развивает предприятие или MIO.

Описание RU: Ночные выходы сократят время, когда рейдер виден береговым наблюдателям.

Описание EN: Night sorties will reduce exposure to coastal observers.

Источник: `common/national_focus/MKN.txt:6412`. Стоимость: 5 (35 дней). Координаты: x=84, y=7.

Предпосылки: (Мастерская малых подлодок [MKN_raider_dockyard]).

Непосредственные продолжения: MKN_submarine_listening, MKN_raider_compact.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_navy_naval_torpedo_reveal_chance_factor -0.07

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_night_sorties
    available_if_capitulated = no
    icon = GFX_focus_generic_nighttime_bombing
    completion_reward = {
        add_to_variable = {
            MKN_navy_naval_torpedo_reveal_chance_factor = -0.07
            tooltip = MKN_navy_naval_torpedo_reveal_chance_factor_tt
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
    }
    x = 84
    y = 7
    prerequisite = {
        focus = MKN_raider_dockyard
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Снабжение в тайных бухтах — `MKN_raider_supply`

Английское название: Supply in Hidden Bays. Категория: Строительство, ресурсы или исследовательская мощность.

Описание RU: Скрытые топливные запасы увеличат время охоты на торговых путях.

Описание EN: Concealed fuel reserves will extend patrols along shipping routes.

Источник: `common/national_focus/MKN.txt:6451`. Стоимость: 5 (35 дней). Координаты: x=88, y=7.

Предпосылки: (Испытания торпед [MKN_torpedo_trials]).

Непосредственные продолжения: MKN_fast_attack_craft, MKN_raider_compact.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_navy_navy_fuel_consumption_factor -0.1
- Потенциальная постройка: fuel_silo +1

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_raider_supply
    available_if_capitulated = no
    icon = GFX_focus_generic_stockpile_fuel
    completion_reward = {
        add_to_variable = {
            MKN_navy_navy_fuel_consumption_factor = -0.1
            tooltip = MKN_navy_navy_fuel_consumption_factor_tt
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
    }
    x = 88
    y = 7
    prerequisite = {
        focus = MKN_torpedo_trials
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Стандартизировать мастерские — `MKN_standardize_workshops`

Английское название: Standardize the Workshops. Категория: Изменяет общий экономический дух MKN.

Описание RU: Дюжина несовместимых затворов — дюжина способов проиграть бой. Общие калибры и согласованные заказы повысят выпуск и эффективность производства в артелях.

Описание EN: A dozen incompatible breech blocks are a dozen ways to lose a battle. Give the artels common gauges and coordinated orders to raise output and production efficiency.

Источник: `common/national_focus/MKN.txt:7204`. Стоимость: 5 (35 дней). Координаты: x=100, y=7.

Предпосылки: (Милитаризовать коммуны [MKN_militarize_communes]).

Непосредственные продолжения: MKN_iron_fist_trains.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_unified_industrial_capacity_factory 0.15
- Изменение параметра: MKN_unified_production_factory_efficiency_gain_factor 0.1

Полное определение; включает точные награды, условия, взаимоисключения и AI:

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

### Механизированная армия коммун — `MKN_mechanized_compact`

Английское название: Mechanized Communal Army. Категория: Открывает/развивает предприятие или MIO.

Описание RU: Основные службы готовы: коммуны располагают механизированной армией, а дальнейшие специализации остаются добровольными. Основная программа: десять фокусов, включая этот итог. Дополнительные специализации не обязательны.

Описание EN: The core services are ready: communes now field a mechanized army with optional further specializations. The core programme has ten focuses including its capstone. Further specializations are optional.

Источник: `common/national_focus/MKN.txt:3909`. Стоимость: 5 (35 дней). Координаты: x=46, y=8.

Предпосылки: (Артиллерийские артели [MKN_artillery_artels]) И (Общие таблицы огня [MKN_fire_tables]).

Непосредственные продолжения: нет.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_army_army_armor_attack_factor 0.06
- Изменение параметра: MKN_army_army_org_factor 0.05

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_mechanized_compact
    available_if_capitulated = no
    cancel_if_invalid = yes
    continue_if_invalid = no
    icon = GFX_focus_generic_mechanized
    completion_reward = {
        add_to_variable = {
            MKN_army_army_armor_attack_factor = 0.06
            tooltip = MKN_army_army_armor_attack_factor_tt
        }
        add_to_variable = {
            MKN_army_army_org_factor = 0.05
            tooltip = MKN_army_army_org_factor_tt
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
    }
    x = 46
    y = 8
    prerequisite = {
        focus = MKN_artillery_artels
    }
    prerequisite = {
        focus = MKN_fire_tables
    }
    available = {
        has_completed_focus = MKN_steel_horses
        has_completed_focus = MKN_tank_crews
        has_completed_focus = MKN_steppe_quartermasters
        has_completed_focus = MKN_radio_sections
        has_completed_focus = MKN_mobile_supply_columns
        has_completed_focus = MKN_recovery_tractors
        has_completed_focus = MKN_tank_maintenance
        has_completed_focus = MKN_artillery_artels
        has_completed_focus = MKN_fire_tables
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Армия вольных колонн — `MKN_free_army_compact`

Английское название: Army of Free Columns. Категория: Открывает/развивает предприятие или MIO.

Описание RU: Вольные колонны готовы к походу; дополнительные службы можно развивать по нуждам фронта. Основная программа: десять фокусов, включая этот итог. Дополнительные специализации не обязательны.

Описание EN: The free columns are ready; additional services can develop according to front-line needs. The core programme has ten focuses including its capstone. Further specializations are optional.

Источник: `common/national_focus/MKN.txt:4452`. Стоимость: 5 (35 дней). Координаты: x=54, y=8.

Предпосылки: (Связь между волостями [MKN_militia_signals]) И (Ночные переходы [MKN_night_marches]).

Непосредственные продолжения: нет.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_army_modifier_army_sub_unit_cavalry_attack_factor 0.05
- Изменение параметра: MKN_army_supply_consumption_factor -0.05

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_free_army_compact
    available_if_capitulated = no
    cancel_if_invalid = yes
    continue_if_invalid = no
    icon = GFX_focus_generic_freedom_council
    completion_reward = {
        add_to_variable = {
            MKN_army_modifier_army_sub_unit_cavalry_attack_factor = 0.05
            tooltip = MKN_army_modifier_army_sub_unit_cavalry_attack_factor_tt
        }
        add_to_variable = {
            MKN_army_supply_consumption_factor = -0.05
            tooltip = MKN_army_supply_consumption_factor_tt
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
    }
    x = 54
    y = 8
    prerequisite = {
        focus = MKN_militia_signals
    }
    prerequisite = {
        focus = MKN_night_marches
    }
    available = {
        has_completed_focus = MKN_batko_cavalry
        has_completed_focus = MKN_village_muster
        has_completed_focus = MKN_remount_artels
        has_completed_focus = MKN_machinegun_carts
        has_completed_focus = MKN_local_guides
        has_completed_focus = MKN_scout_parties
        has_completed_focus = MKN_field_veterinary
        has_completed_focus = MKN_militia_signals
        has_completed_focus = MKN_night_marches
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Небо под защитой коммун — `MKN_free_sky_compact`

Английское название: Communal Sky Defence. Категория: Открывает/развивает предприятие или MIO.

Описание RU: Основная система перехвата готова; ночные и радиолокационные службы останутся дополнительными. Основная программа: десять фокусов, включая этот итог. Дополнительные специализации не обязательны.

Описание EN: The core interception system is ready, with night and radar services available as extensions. The core programme has ten focuses including its capstone. Further specializations are optional.

Источник: `common/national_focus/MKN.txt:4993`. Стоимость: 5 (35 дней). Координаты: x=62, y=8.

Предпосылки: (Перехват парами [MKN_interceptor_pairs]) И (Возвращать повреждённые машины [MKN_aircraft_recovery]).

Непосредственные продолжения: нет.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_air_air_intercept_efficiency 0.1
- Изменение параметра: MKN_air_air_agility_factor 0.04

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_free_sky_compact
    available_if_capitulated = no
    cancel_if_invalid = yes
    continue_if_invalid = no
    icon = GFX_goal_generic_build_airforce
    completion_reward = {
        add_to_variable = {
            MKN_air_air_intercept_efficiency = 0.1
            tooltip = MKN_air_air_intercept_efficiency_tt
        }
        add_to_variable = {
            MKN_air_air_agility_factor = 0.04
            tooltip = MKN_air_air_agility_factor_tt
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
    }
    x = 62
    y = 8
    prerequisite = {
        focus = MKN_interceptor_pairs
    }
    prerequisite = {
        focus = MKN_aircraft_recovery
    }
    available = {
        has_completed_focus = MKN_black_swarm
        has_completed_focus = MKN_aircraft_artels
        has_completed_focus = MKN_observation_posts
        has_completed_focus = MKN_fighter_instructors
        has_completed_focus = MKN_air_warning
        has_completed_focus = MKN_radio_beacons
        has_completed_focus = MKN_airframe_jigs
        has_completed_focus = MKN_interceptor_pairs
        has_completed_focus = MKN_aircraft_recovery
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Крылья над вольными колоннами — `MKN_air_support_compact`

Английское название: Wings over Free Columns. Категория: Открывает/развивает предприятие или MIO.

Описание RU: Колонны получили воздушную поддержку; дальние и морские операции можно развивать отдельно. Основная программа: десять фокусов, включая этот итог. Дополнительные специализации не обязательны.

Описание EN: Columns now have air support, with long-range and maritime operations available as extensions. The core programme has ten focuses including its capstone. Further specializations are optional.

Источник: `common/national_focus/MKN.txt:5617`. Стоимость: 5 (35 дней). Координаты: x=70, y=8.

Предпосылки: (Обозначение целей с земли [MKN_target_markers]) И (Летающая артиллерия [MKN_flying_artillery]).

Непосредственные продолжения: нет.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_air_air_cas_efficiency 0.05
- Изменение параметра: MKN_air_air_mission_efficiency 0.05

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_air_support_compact
    available_if_capitulated = no
    cancel_if_invalid = yes
    continue_if_invalid = no
    icon = GFX_goal_generic_CAS
    completion_reward = {
        add_to_variable = {
            MKN_air_air_cas_efficiency = 0.05
            tooltip = MKN_air_air_cas_efficiency_tt
        }
        add_to_variable = {
            MKN_air_air_mission_efficiency = 0.05
            tooltip = MKN_air_air_mission_efficiency_tt
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
    }
    x = 70
    y = 8
    prerequisite = {
        focus = MKN_target_markers
    }
    prerequisite = {
        focus = MKN_flying_artillery
    }
    available = {
        has_completed_focus = MKN_close_support_program
        has_completed_focus = MKN_attack_air_artels
        has_completed_focus = MKN_air_ground_liaisons
        has_completed_focus = MKN_bombing_ranges
        has_completed_focus = MKN_forward_airstrips
        has_completed_focus = MKN_air_map_bureau
        has_completed_focus = MKN_cas_maintenance
        has_completed_focus = MKN_target_markers
        has_completed_focus = MKN_flying_artillery
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Море для хлебных конвоев — `MKN_escort_compact`

Английское название: Sea Lanes for Grain Convoys. Категория: Открывает/развивает предприятие или MIO.

Описание RU: Основная система эскорта готова; противолодочные и спасательные службы можно расширять дальше. Основная программа: десять фокусов, включая этот итог. Дополнительные специализации не обязательны.

Описание EN: The core escort system is ready, with room to expand anti-submarine and rescue services. The core programme has ten focuses including its capstone. Further specializations are optional.

Источник: `common/national_focus/MKN.txt:6151`. Стоимость: 5 (35 дней). Координаты: x=78, y=8.

Предпосылки: (Школа глубинных бомб [MKN_depth_charge_school]) И (Расписания зерновых конвоев [MKN_convoy_schedules]).

Непосредственные продолжения: нет.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_navy_convoy_escort_efficiency 0.05
- Изменение параметра: MKN_navy_screening_efficiency 0.05

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_escort_compact
    available_if_capitulated = no
    cancel_if_invalid = yes
    continue_if_invalid = no
    icon = GFX_focus_generic_merchant_fleet
    completion_reward = {
        add_to_variable = {
            MKN_navy_convoy_escort_efficiency = 0.05
            tooltip = MKN_navy_convoy_escort_efficiency_tt
        }
        add_to_variable = {
            MKN_navy_screening_efficiency = 0.05
            tooltip = MKN_navy_screening_efficiency_tt
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
    }
    x = 78
    y = 8
    prerequisite = {
        focus = MKN_depth_charge_school
    }
    prerequisite = {
        focus = MKN_convoy_schedules
    }
    available = {
        has_completed_focus = MKN_coastal_defense_steppe
        has_completed_focus = MKN_dnieper_gun_flotilla
        has_completed_focus = MKN_black_sea_escorts
        has_completed_focus = MKN_coastal_signal_posts
        has_completed_focus = MKN_escort_crews
        has_completed_focus = MKN_harbour_dredging
        has_completed_focus = MKN_hull_repair_artels
        has_completed_focus = MKN_depth_charge_school
        has_completed_focus = MKN_convoy_schedules
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Море для вольных рейдеров — `MKN_raider_compact`

Английское название: Sea for Free Raiders. Категория: Открывает/развивает предприятие или MIO.

Описание RU: Рейдерская система готова; дополнительные катера, ремонт и тактику засад можно развивать по обстановке. Основная программа: десять фокусов, включая этот итог. Дополнительные специализации не обязательны.

Описание EN: The raiding system is ready, with craft, repair and ambush tactics available as extensions. The core programme has ten focuses including its capstone. Further specializations are optional.

Источник: `common/national_focus/MKN.txt:6766`. Стоимость: 5 (35 дней). Координаты: x=86, y=8.

Предпосылки: (Ночные выходы [MKN_night_sorties]) И (Снабжение в тайных бухтах [MKN_raider_supply]).

Непосредственные продолжения: нет.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_navy_convoy_raiding_efficiency_factor 0.1
- Изменение параметра: MKN_navy_navy_submarine_attack_factor 0.05

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_raider_compact
    available_if_capitulated = no
    cancel_if_invalid = yes
    continue_if_invalid = no
    icon = GFX_goal_generic_navy_submarine
    completion_reward = {
        add_to_variable = {
            MKN_navy_convoy_raiding_efficiency_factor = 0.1
            tooltip = MKN_navy_convoy_raiding_efficiency_factor_tt
        }
        add_to_variable = {
            MKN_navy_navy_submarine_attack_factor = 0.05
            tooltip = MKN_navy_navy_submarine_attack_factor_tt
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
    }
    x = 86
    y = 8
    prerequisite = {
        focus = MKN_night_sorties
    }
    prerequisite = {
        focus = MKN_raider_supply
    }
    available = {
        has_completed_focus = MKN_black_sea_smugglers
        has_completed_focus = MKN_torpedo_artels
        has_completed_focus = MKN_submarine_crews
        has_completed_focus = MKN_hidden_anchorages
        has_completed_focus = MKN_naval_intelligence
        has_completed_focus = MKN_raider_dockyard
        has_completed_focus = MKN_torpedo_trials
        has_completed_focus = MKN_night_sorties
        has_completed_focus = MKN_raider_supply
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Самоуправляемые железнодорожные бригады — `MKN_autonomous_rail_crews`

Английское название: Autonomous Rail Crews. Категория: Изменяет общий экономический дух MKN.

Описание RU: Расписание принадлежит тем, кто обеспечивает движение. Рабочие бригады снизят стоимость поездов и ускорят строительство железных дорог и инфраструктуры.

Описание EN: The timetable belongs to those who keep it running. Worker crews lower train costs and accelerate railway and infrastructure construction.

Источник: `common/national_focus/MKN.txt:7558`. Стоимость: 5 (35 дней). Координаты: x=106, y=8.

Предпосылки: (Пропаганда действием [MKN_propaganda_by_deed]).

Непосредственные продолжения: MKN_beacon_of_statelessness.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- add_ideas: MKN_autonomous_rail_crews_idea
- Изменение параметра: MKN_unified_production_speed_buildings_factor 0.05

Полное определение; включает точные награды, условия, взаимоисключения и AI:

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

### Тракторы за зерно — `MKN_tractors_for_grain`

Английское название: Tractors for Grain. Категория: Строительство, ресурсы или исследовательская мощность; Изменяет общий экономический дух MKN; Бонус промышленным технологиям.

Описание RU: Зерновой договор даст нам станки вместе с тракторами. Получим бонусы к промышленным исследованиям, два военных завода и улучшение строительства.

Описание EN: The grain contract buys machine tools as well as tractors. Gain industrial research bonuses, two military factories and stronger construction capacity.

Источник: `common/national_focus/MKN.txt:8049`. Стоимость: 5 (35 дней). Координаты: x=118, y=8.

Предпосылки: (Красные военные специалисты [MKN_red_military_specialists]).

Непосредственные продолжения: MKN_anti_imperialist_front.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Потенциальная постройка: arms_factory +2
- Изменение параметра: MKN_unified_production_speed_buildings_factor 0.1

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_tractors_for_grain
    x = 118
    y = 8
    completion_reward = {
        add_tech_bonus = {
            bonus = 0.5
            uses = 2
            category = industry
        }
        random_owned_state = {
            limit = {
                is_controlled_by = ROOT
            }
            add_extra_state_shared_building_slots = 2
            add_building_construction = {
                type = arms_factory
                level = 2
                instant_build = yes
            }
        }
        add_to_variable = {
            MKN_unified_production_speed_buildings_factor = 0.1
            tooltip = MKN_unified_production_speed_buildings_factor_tt
        }
    }
    prerequisite = {
        focus = MKN_red_military_specialists
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
    icon = GFX_focus_MKN_program_revkom_5
}
```

### Отзывные мандаты общин — `MKN_free_elections_steppe`

Английское название: Recallable Communal Mandates. Категория: Изменяет общий экономический дух MKN.

Описание RU: Каждая коммуна избирает и отзывает своих делегатов. Федерация получает устойчивые мандаты без постоянного парламента. Вольные советы получают ещё 0,20 на шкале баланса.

Описание EN: Each commune elects and may recall its delegates. The federation receives reliable mandates without creating a permanent parliament. Free soviets gain another 0.20 on the balance scale.

Источник: `common/national_focus/MKN.txt:1471`. Стоимость: 5 (35 дней). Координаты: x=33, y=9.

Предпосылки: (Съезд вольных советов [MKN_constituent_assembly]).

Непосредственные продолжения: MKN_everlasting_makhnovshchina, MKN_council_communism, MKN_open_markets.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- add_stability: 0.1
- Политическая власть: 100
- Изменение параметра: MKN_unified_stability_factor 0.1
- Изменение параметра: MKN_unified_political_power_gain 0.1

Полное определение; включает точные награды, условия, взаимоисключения и AI:

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

Английское название: Imperial Coronation. Категория: Изменяет общий экономический дух MKN.

Описание RU: Корона из пшеницы и стали.

Описание EN: A crown of wheat and steel.

Источник: `common/national_focus/MKN.txt:1935`. Стоимость: 5 (35 дней). Координаты: x=41, y=9.

Предпосылки: (Крестьянский покровитель [MKN_nestor_the_first]).

Непосредственные продолжения: MKN_steppe_empire.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Политическая власть: 150
- add_war_support: 0.1
- Изменение параметра: MKN_unified_stability_factor 0.1
- Изменение параметра: MKN_unified_political_power_gain 0.15

Полное определение; включает точные награды, условия, взаимоисключения и AI:

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

### Рассредоточенные аэродромы — `MKN_air_dispersal`

Английское название: Dispersed Airfields. Категория: Строительство, ресурсы или исследовательская мощность.

Описание RU: Рассредоточим самолёты по запасным полосам и защитим домашнее небо.

Описание EN: Disperse aircraft among reserve strips and strengthen home air defence.

Источник: `common/national_focus/MKN.txt:4716`. Стоимость: 5 (35 дней). Координаты: x=60, y=9.

Предпосылки: (Перехват парами [MKN_interceptor_pairs]).

Непосредственные продолжения: MKN_air_radar_school.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_air_air_home_defence_factor 0.1
- Потенциальная постройка: air_base +2

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_air_dispersal
    available_if_capitulated = no
    icon = GFX_focus_generic_air_bases
    completion_reward = {
        add_to_variable = {
            MKN_air_air_home_defence_factor = 0.1
            tooltip = MKN_air_air_home_defence_factor_tt
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
    }
    x = 60
    y = 9
    prerequisite = {
        focus = MKN_interceptor_pairs
    }
    ai_will_do = {
        factor = 1
    }
    cost = 5
}
```

### Топливные склады эскадрилий — `MKN_airfield_fuel`

Английское название: Squadron Fuel Depots. Категория: Строительство, ресурсы или исследовательская мощность.

Описание RU: Наладим заправку, чтобы ударные группы не пропускали решающий вылет.

Описание EN: Organize refuelling so strike groups can fly at the decisive moment.

Источник: `common/national_focus/MKN.txt:5341`. Стоимость: 5 (35 дней). Координаты: x=68, y=9.

Предпосылки: (Обозначение целей с земли [MKN_target_markers]).

Непосредственные продолжения: MKN_bomber_navigation.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_air_air_fuel_consumption_factor -0.1
- Потенциальная постройка: fuel_silo +1

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_airfield_fuel
    available_if_capitulated = no
    icon = GFX_focus_generic_stockpile_fuel
    completion_reward = {
        add_to_variable = {
            MKN_air_air_fuel_consumption_factor = -0.1
            tooltip = MKN_air_air_fuel_consumption_factor_tt
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
    }
    x = 68
    y = 9
    prerequisite = {
        focus = MKN_target_markers
    }
    ai_will_do = {
        factor = 1
    }
    cost = 5
}
```

### Кооперативный обмен — `MKN_open_markets`

Английское название: Cooperative Exchange. Категория: Бонус промышленным технологиям.

Описание RU: Общинные мастерские обмениваются излишками через кооперативные договоры и общие технические стандарты.

Описание EN: Communal workshops exchange their surplus through cooperative agreements and shared technical standards.

Источник: `common/national_focus/MKN.txt:1519`. Стоимость: 5 (35 дней). Координаты: x=33, y=10.

Предпосылки: (Отзывные мандаты общин [MKN_free_elections_steppe]).

Непосредственные продолжения: нет.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Политическая власть: 50

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_open_markets
    icon = GFX_focus_generic_industry_2
    completion_reward = {
        add_tech_bonus = {
            bonus = 0.5
            uses = 2
            category = industry
        }
        add_political_power = 50
    }
    prerequisite = {
        focus = MKN_free_elections_steppe
    }
    x = 33
    y = 10
    allow_branch = {
        NOT = {
            has_country_flag = MKN_crisis_enabled
        }
    }
    cost = 5
}
```

### Синдикалистская программа — `MKN_council_communism`

Английское название: The Syndicalist Program. Категория: Бонус промышленным технологиям.

Описание RU: Заводские собрания и крестьянские коммуны согласуют производство через выборных делегатов. Этот вариант анархо-коммунизма усиливает советы на 0,20 без подчинения Москве.

Описание EN: Factory assemblies and peasant communes coordinate production through elected delegates. This alternative within anarcho-communism strengthens the soviets by 0.20 without submitting to Moscow.

Источник: `common/national_focus/MKN.txt:1293`. Стоимость: 5 (35 дней). Координаты: x=35, y=10.

Предпосылки: (Отзывные мандаты общин [MKN_free_elections_steppe]).

Непосредственные продолжения: MKN_workers_control.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- См. полную награду в completion_reward.

Полное определение; включает точные награды, условия, взаимоисключения и AI:

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

### Коллективизировать степь — `MKN_collectivize_the_steppe`

Английское название: Collectivize the Steppe. Категория: Изменяет общий экономический дух MKN.

Описание RU: Добровольно. Преимущественно.

Описание EN: Voluntarily. Mostly.

Источник: `common/national_focus/MKN.txt:1675`. Стоимость: 5 (35 дней). Координаты: x=38, y=10.

Предпосылки: (Красный компромисс [MKN_red_banner_steppe]).

Непосредственные продолжения: MKN_red_compromise_institutions.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- add_stability: 0.05
- Изменение параметра: MKN_unified_industrial_capacity_factory 0.08
- Изменение параметра: MKN_unified_consumer_goods_factor -0.03

Полное определение; включает точные награды, условия, взаимоисключения и AI:

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

### Учёт горючего в походе — `MKN_fuel_discipline`

Английское название: Fuel Accounting on Campaign. Категория: Строительство, ресурсы или исследовательская мощность.

Описание RU: Запас горючего и маршруты заправки избавят наступление от пустых баков.

Описание EN: Fuel reserves and refuelling routes will prevent stalled offensives.

Источник: `common/national_focus/MKN.txt:3719`. Стоимость: 5 (35 дней). Координаты: x=48, y=10.

Предпосылки: (Пехота вслед за бронёй [MKN_motorized_infantry]).

Непосредственные продолжения: MKN_mobile_medical.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_army_army_fuel_consumption_factor -0.1
- Потенциальная постройка: fuel_silo +1

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_fuel_discipline
    available_if_capitulated = no
    icon = GFX_focus_generic_stockpile_fuel
    completion_reward = {
        add_to_variable = {
            MKN_army_army_fuel_consumption_factor = -0.1
            tooltip = MKN_army_army_fuel_consumption_factor_tt
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
    }
    x = 48
    y = 10
    prerequisite = {
        focus = MKN_motorized_infantry
    }
    ai_will_do = {
        factor = 1
    }
    cost = 5
}
```

### Радиосеть охранения — `MKN_escort_radio_net`

Английское название: Escort Radio Network. Категория: Бонус промышленным технологиям.

Описание RU: Общая частота охранения позволит быстро перестроить защитный экран.

Описание EN: A shared escort frequency will help ships reorganize their protective screen.

Источник: `common/national_focus/MKN.txt:5953`. Стоимость: 5 (35 дней). Координаты: x=80, y=10.

Предпосылки: (Постоянный береговой дозор [MKN_coastal_watch]).

Непосредственные продолжения: MKN_river_sea_coordination.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_navy_screening_efficiency 0.07

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_escort_radio_net
    available_if_capitulated = no
    icon = GFX_focus_generic_phone
    completion_reward = {
        add_to_variable = {
            MKN_navy_screening_efficiency = 0.07
            tooltip = MKN_navy_screening_efficiency_tt
        }
        add_tech_bonus = {
            name = MKN_escort_radio_net
            bonus = 0.5
            uses = 1
            category = electronics
        }
    }
    x = 80
    y = 10
    prerequisite = {
        focus = MKN_coastal_watch
    }
    ai_will_do = {
        factor = 1
    }
    cost = 5
}
```

### Советы навсегда — `MKN_soviets_forever`

Английское название: Soviets Forever. Категория: Изменяет общий экономический дух MKN.

Описание RU: Коммуна вечна.

Описание EN: The commune is eternal.

Источник: `common/national_focus/MKN.txt:1237`. Стоимость: 5 (35 дней). Координаты: x=31, y=11.

Предпосылки: (Махновская традиция [MKN_everlasting_makhnovshchina]).

Непосредственные продолжения: MKN_tachanka_guards.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- add_stability: 0.1
- Политическая власть: 100
- add_ideas: MKN_free_soviets_idea
- Изменение параметра: MKN_unified_stability_factor 0.05
- Изменение параметра: MKN_unified_production_speed_buildings_factor 0.05

Полное определение; включает точные награды, условия, взаимоисключения и AI:

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

Английское название: Workers Control. Категория: Строительство, ресурсы или исследовательская мощность.

Описание RU: Завод — тем, кто на нём работает.

Описание EN: The factory to those who work it.

Источник: `common/national_focus/MKN.txt:1353`. Стоимость: 5 (35 дней). Координаты: x=35, y=11.

Предпосылки: (Синдикалистская программа [MKN_council_communism]).

Непосредственные продолжения: MKN_commune_federation.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- add_stability: 0.05
- Политическая власть: 80
- Потенциальная постройка: industrial_complex +1

Полное определение; включает точные награды, условия, взаимоисключения и AI:

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

### Советская администрация — `MKN_red_compromise_institutions`

Английское название: The Council Administration. Категория: Изменяет общий экономический дух MKN.

Описание RU: Местные советы проводят государственно-социалистическую программу через постоянное гражданское управление. Эти учреждения сохраняют жизнеспособность при отказе Москвы или её предательстве.

Описание EN: Local councils implement the state socialist program through a permanent civil administration. These institutions remain viable even if Moscow rejects or betrays the pact.

Источник: `common/national_focus/MKN.txt:6973`. Стоимость: 5 (35 дней). Координаты: x=38, y=11.

Предпосылки: (Коллективизировать степь [MKN_collectivize_the_steppe]).

Непосредственные продолжения: нет.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- add_stability: 0.05
- Политическая власть: 50
- Изменение параметра: MKN_unified_production_factory_efficiency_gain_factor 0.05
- Изменение параметра: MKN_unified_political_power_gain 0.05

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_red_compromise_institutions
    icon = GFX_focus_generic_diplomatic_treaty
    x = 38
    y = 11
    prerequisite = {
        focus = MKN_collectivize_the_steppe
    }
    completion_reward = {
        add_stability = 0.05
        add_political_power = 50
        add_to_variable = {
            MKN_unified_production_factory_efficiency_gain_factor = 0.05
            tooltip = MKN_unified_production_factory_efficiency_gain_factor_tt
        }
        add_to_variable = {
            MKN_unified_political_power_gain = 0.05
            tooltip = MKN_unified_political_power_gain_tt
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

### Крестьянская хартия — `MKN_peasant_charter`

Английское название: The Peasant Charter. Категория: Изменяет общий экономический дух MKN.

Описание RU: Нестор I признаёт деревенские собрания, общинные земельные соглашения и ограничения внешних обязательств. Корона гарантирует аграрную замкнутость и не даёт права на завоевания.

Описание EN: Nestor I recognizes the village assemblies, communal land agreements and limits on foreign commitments. The crown becomes a guarantor of agrarian isolation rather than a claim to conquest.

Источник: `common/national_focus/MKN.txt:6946`. Стоимость: 5 (35 дней). Координаты: x=41, y=11.

Предпосылки: (Оборона крестьянского края [MKN_steppe_empire]).

Непосредственные продолжения: нет.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- add_stability: 0.05
- Политическая власть: 100
- Изменение параметра: MKN_unified_consumer_goods_factor -0.02
- Изменение параметра: MKN_unified_stability_factor 0.03

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_peasant_charter
    icon = GFX_focus_generic_support_the_left_right
    x = 41
    y = 11
    prerequisite = {
        focus = MKN_steppe_empire
    }
    completion_reward = {
        add_stability = 0.05
        add_political_power = 100
        add_to_variable = {
            MKN_unified_consumer_goods_factor = -0.02
            tooltip = MKN_unified_consumer_goods_factor_tt
        }
        add_to_variable = {
            MKN_unified_stability_factor = 0.03
            tooltip = MKN_unified_stability_factor_tt
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

### Портовые склады снабжения — `MKN_coastal_depots`

Английское название: Port Supply Depots. Категория: Строительство, ресурсы или исследовательская мощность.

Описание RU: Прибрежные склады поддержат длительное патрулирование без дальних переходов на заправку.

Описание EN: Coastal depots will sustain patrols without long refuelling trips.

Источник: `common/national_focus/MKN.txt:5979`. Стоимость: 5 (35 дней). Координаты: x=76, y=11.

Предпосылки: (Тральные отряды [MKN_sweeper_sections]).

Непосредственные продолжения: MKN_anti_submarine_patrols.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_navy_navy_fuel_consumption_factor -0.1
- Потенциальная постройка: fuel_silo +1

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_coastal_depots
    available_if_capitulated = no
    icon = GFX_focus_generic_supply_line
    completion_reward = {
        add_to_variable = {
            MKN_navy_navy_fuel_consumption_factor = -0.1
            tooltip = MKN_navy_navy_fuel_consumption_factor_tt
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
    }
    x = 76
    y = 11
    prerequisite = {
        focus = MKN_sweeper_sections
    }
    ai_will_do = {
        factor = 1
    }
    cost = 5
}
```

### Погода как союзник — `MKN_raider_weather`

Английское название: Weather as an Ally. Категория: Бонус промышленным технологиям.

Описание RU: Метеосводки помогут использовать плохую видимость для подхода к цели.

Описание EN: Weather reports will help crews approach targets under poor visibility.

Источник: `common/national_focus/MKN.txt:6613`. Стоимость: 5 (35 дней). Координаты: x=84, y=11.

Предпосылки: (Радиодисциплина рейдеров [MKN_raider_radio_discipline]).

Непосредственные продолжения: MKN_torpedo_ambushes.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_navy_naval_detection 0.05

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_raider_weather
    available_if_capitulated = no
    icon = GFX_focus_generic_long_range_aircraft
    completion_reward = {
        add_to_variable = {
            MKN_navy_naval_detection = 0.05
            tooltip = MKN_navy_naval_detection_tt
        }
        add_tech_bonus = {
            name = MKN_raider_weather
            bonus = 0.5
            uses = 1
            category = electronics
        }
    }
    x = 84
    y = 11
    prerequisite = {
        focus = MKN_raider_radio_discipline
    }
    ai_will_do = {
        factor = 1
    }
    cost = 5
}
```

### Федерация коммун — `MKN_commune_federation`

Английское название: Commune Federation. Категория: Изменяет общий экономический дух MKN.

Описание RU: Тысяча коммун — одна федерация.

Описание EN: A thousand communes, one federation.

Источник: `common/national_focus/MKN.txt:1385`. Стоимость: 5 (35 дней). Координаты: x=35, y=12.

Предпосылки: (Рабочий контроль [MKN_workers_control]).

Непосредственные продолжения: MKN_recallable_delegates.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- add_war_support: 0.05
- add_ideas: MKN_free_soviets_idea
- Изменение параметра: MKN_unified_stability_factor 0.05
- Изменение параметра: MKN_unified_production_speed_buildings_factor 0.05

Полное определение; включает точные награды, условия, взаимоисключения и AI:

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

### Степная метеослужба — `MKN_air_weather_service`

Английское название: Steppe Weather Service. Категория: Бонус промышленным технологиям.

Описание RU: Метеопосты помогут выбирать окно для удара вместо отмены всей операции.

Описание EN: Weather stations will help select a strike window instead of cancelling the operation.

Источник: `common/national_focus/MKN.txt:5537`. Стоимость: 5 (35 дней). Координаты: x=72, y=12.

Предпосылки: (Резерв экипажей штурмовиков [MKN_cas_replacement_crews]).

Непосредственные продолжения: MKN_cas_joint_exercises.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_air_air_mission_efficiency 0.04

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_air_weather_service
    available_if_capitulated = no
    icon = GFX_focus_generic_air_research_boost
    completion_reward = {
        add_to_variable = {
            MKN_air_air_mission_efficiency = 0.04
            tooltip = MKN_air_air_mission_efficiency_tt
        }
        add_tech_bonus = {
            name = MKN_air_weather_service
            bonus = 0.5
            uses = 1
            category = electronics
        }
    }
    x = 72
    y = 12
    prerequisite = {
        focus = MKN_cas_replacement_crews
    }
    ai_will_do = {
        factor = 1
    }
    cost = 5
}
```

### Вольные мастерские Екатеринослава и Гуляйполя — `MKN_free_workshops_focus`

Английское название: Ekaterinoslav & Huliaipole Free Workshops. Категория: Открывает/развивает предприятие или MIO.

Описание RU: Объединим городские и сельские мастерские в общую инженерную сеть.

Описание EN: Federate the urban and rural workshops into a common engineering network.

Источник: `common/national_focus/MKN.txt:8190`. Стоимость: 5 (35 дней). Координаты: x=14, y=13.

Предпосылки: нет нарисованной предпосылки; см. available.

Непосредственные продолжения: нет.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- См. полную награду в completion_reward.

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_free_workshops_focus
    icon = GFX_idea_MKN_free_workshops
    cost = 5
    available = {
        OR = {
            has_completed_focus = MKN_industrial_compact
            has_completed_focus = MKN_communal_compact
        }
    }
    completion_reward = {
        custom_effect_tooltip = MKN_free_workshops_unlock_tt
    }
    ai_will_do = {
        factor = 3
    }
    x = 14
    y = 13
}
```

### Хартия отзыва — `MKN_recallable_delegates`

Английское название: The Charter of Recall. Категория: Изменяет общий экономический дух MKN.

Описание RU: При махновской традиции или синдикалистском согласовании съезд гарантирует право отзыва каждого делегата. Хартия требует более 80% контроля вольных советов.

Описание EN: Whether the congress follows the Makhnovist tradition or syndicalist coordination, it guarantees the right to recall every delegate. The charter requires more than 80% control by the free soviets.

Источник: `common/national_focus/MKN.txt:6907`. Стоимость: 5 (35 дней). Координаты: x=33, y=13.

Предпосылки: (Тачаночная гвардия [MKN_tachanka_guards] ИЛИ Федерация коммун [MKN_commune_federation]).

Непосредственные продолжения: нет.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- add_stability: 0.05
- Политическая власть: 75
- Изменение параметра: MKN_unified_political_power_gain 0.1
- Изменение параметра: MKN_unified_stability_factor 0.03

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_recallable_delegates
    icon = GFX_focus_generic_diplomatic_treaty
    x = 33
    y = 13
    prerequisite = {
        focus = MKN_tachanka_guards
        focus = MKN_commune_federation
    }
    available = {
        has_power_balance = {
            id = MKN_power_balance
        }
        power_balance_value = {
            id = MKN_power_balance
            value > 0.6
        }
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    completion_reward = {
        add_stability = 0.05
        add_political_power = 75
        add_to_variable = {
            MKN_unified_political_power_gain = 0.1
            tooltip = MKN_unified_political_power_gain_tt
        }
        add_to_variable = {
            MKN_unified_stability_factor = 0.03
            tooltip = MKN_unified_stability_factor_tt
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

### Мастерские прорыва — `MKN_breakthrough_workshops`

Английское название: Breakthrough Workshops. Категория: Строительство, ресурсы или исследовательская мощность.

Описание RU: Мастерские прорыва будут выпускать бронетехнику по требованиям полевых экипажей.

Описание EN: Breakthrough workshops will build armour to field crews' specifications.

Источник: `common/national_focus/MKN.txt:3855`. Стоимость: 5 (35 дней). Координаты: x=44, y=13.

Предпосылки: (Единый боевой порядок [MKN_combined_arms]).

Непосредственные продолжения: нет.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_army_army_armor_attack_factor 0.04
- Потенциальная постройка: arms_factory +1

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_breakthrough_workshops
    available_if_capitulated = no
    icon = GFX_focus_generic_tank_production
    completion_reward = {
        add_to_variable = {
            MKN_army_army_armor_attack_factor = 0.04
            tooltip = MKN_army_army_armor_attack_factor_tt
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
    }
    x = 44
    y = 13
    prerequisite = {
        focus = MKN_combined_arms
    }
    ai_will_do = {
        factor = 1
    }
    cost = 5
}
```

### Защита промышленных районов — `MKN_air_home_defence`

Английское название: Industrial Air Defence. Категория: Строительство, ресурсы или исследовательская мощность.

Описание RU: Зенитные батареи и истребители разделят зоны защиты промышленных коммун.

Описание EN: Anti-aircraft batteries and fighters will share the defence of industrial communes.

Источник: `common/national_focus/MKN.txt:4934`. Стоимость: 5 (35 дней). Координаты: x=60, y=13.

Предпосылки: (Спасение сбитых лётчиков [MKN_air_rescue]).

Непосредственные продолжения: нет.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_air_air_home_defence_factor 0.1
- Потенциальная постройка: anti_air +2

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_air_home_defence
    available_if_capitulated = no
    icon = GFX_focus_generic_home_defense
    completion_reward = {
        add_to_variable = {
            MKN_air_air_home_defence_factor = 0.1
            tooltip = MKN_air_air_home_defence_factor_tt
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
    }
    x = 60
    y = 13
    prerequisite = {
        focus = MKN_air_rescue
    }
    ai_will_do = {
        factor = 1
    }
    cost = 5
}
```

### Резерв портовых экипажей — `MKN_escort_reserves`

Английское название: Port Crew Reserve. Категория: Строительство, ресурсы или исследовательская мощность.

Описание RU: Резерв экипажей и дополнительная верфь обеспечат замену потерь.

Описание EN: Reserve crews and an additional yard will replace losses.

Источник: `common/national_focus/MKN.txt:6085`. Стоимость: 5 (35 дней). Координаты: x=76, y=13.

Предпосылки: (Противолодочные патрули [MKN_anti_submarine_patrols]).

Непосредственные продолжения: нет.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_navy_naval_defense_factor 0.05
- Потенциальная постройка: dockyard +1

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_escort_reserves
    available_if_capitulated = no
    icon = GFX_focus_generic_manpower
    completion_reward = {
        add_to_variable = {
            MKN_navy_naval_defense_factor = 0.05
            tooltip = MKN_navy_naval_defense_factor_tt
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
    }
    x = 76
    y = 13
    prerequisite = {
        focus = MKN_anti_submarine_patrols
    }
    ai_will_do = {
        factor = 1
    }
    cost = 5
}
```

## Необходимые предки вне промышленного каталога

Для проверки достижимости, политических и военных ограничений. Эти фокусы не входят в число промышленных карточек.

### Тачаночные колонны — `MKN_tachanka_columns`

Вооружим колонны и введём общий порядок сбора, сохраняя выборных командиров.

```pdx
focus = {
    id = MKN_tachanka_columns
    x = 50
    y = 0
    available_if_capitulated = no
    ai_will_do = {
        factor = 1
    }
    icon = GFX_goal_generic_cavalry
    completion_reward = {
        add_to_variable = {
            MKN_army_army_org_factor = 0.04
            tooltip = MKN_army_army_org_factor_tt
        }
        army_experience = 20
        add_equipment_to_stockpile = {
            type = infantry_equipment_0
            amount = 800
            producer = ROOT
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
    cost = 5
}
```

### Степные соколы — `MKN_steppe_hawks`

Создадим воздушную службу коммун с общей диспетчерской и правилами полётов.

```pdx
focus = {
    id = MKN_steppe_hawks
    x = 66
    y = 0
    available_if_capitulated = no
    ai_will_do = {
        factor = 1
    }
    icon = GFX_focus_generic_swooping_falcon
    completion_reward = {
        add_to_variable = {
            MKN_air_air_mission_efficiency = 0.03
            tooltip = MKN_air_air_mission_efficiency_tt
        }
        air_experience = 20
        if = {
            limit = {
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
    }
    cost = 5
}
```

### Черноморская флотилия — `MKN_black_sea_flotilla`

Создадим малую флотилию с задачами, посильными бюджету коммун.

```pdx
focus = {
    id = MKN_black_sea_flotilla
    x = 82
    y = 0
    available_if_capitulated = no
    ai_will_do = {
        factor = 1
    }
    icon = GFX_focus_generic_black_sea_focus
    completion_reward = {
        add_to_variable = {
            MKN_navy_naval_defense_factor = 0.03
            tooltip = MKN_navy_naval_defense_factor_tt
        }
        navy_experience = 20
        if = {
            limit = {
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
    }
    available = {
        196 = {
            is_owned_and_controlled_by = ROOT
        }
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    cost = 5
}
```

### Съезд 1936 года — `MKN_congress_1936`

В зале пахнет мокрыми шинелями и типографской краской. Махно ещё способен заставить его замолчать одним взглядом, но никто не верит, что это будет длиться вечно. Дадим делегатам мандат и вынесем спор штаба Тратишова с советами Волина на съезд.

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

### Железнодорожная война — `MKN_railway_war`

Согласованные эшелоны подвезут боеприпасы быстрее случайных крестьянских обозов.

```pdx
focus = {
    id = MKN_railway_war
    x = 50
    y = 1
    available_if_capitulated = no
    ai_will_do = {
        factor = 1
    }
    prerequisite = {
        focus = MKN_tachanka_columns
    }
    icon = GFX_focus_generic_railroad
    completion_reward = {
        add_to_variable = {
            MKN_army_supply_consumption_factor = -0.05
            tooltip = MKN_army_supply_consumption_factor_tt
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
    }
    cost = 5
}
```

### Днепровский дозор — `MKN_dnieper_patrol`

Днепровские дозоры станут школой будущих морских экипажей.

```pdx
focus = {
    id = MKN_dnieper_patrol
    x = 82
    y = 1
    available_if_capitulated = no
    ai_will_do = {
        factor = 1
    }
    prerequisite = {
        focus = MKN_black_sea_flotilla
    }
    icon = GFX_goal_generic_navy_doctrines_tactics
    completion_reward = {
        add_to_variable = {
            MKN_navy_naval_detection = 0.05
            tooltip = MKN_navy_naval_detection_tt
        }
        add_tech_bonus = {
            name = MKN_dnieper_patrol
            bonus = 0.5
            uses = 1
            category = dd_tech
        }
    }
    cost = 5
}
```

### Вольная территория — `MKN_the_free_territory`

Ни господ, ни государств — только вольные советы крестьян и рабочих.

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

### Штаб степных армий — `MKN_steppe_general_staff`

Штаб Белаша свяжет самостоятельные отряды общим планом операций.

```pdx
focus = {
    id = MKN_steppe_general_staff
    x = 50
    y = 2
    available_if_capitulated = no
    ai_will_do = {
        factor = 1
    }
    prerequisite = {
        focus = MKN_railway_war
    }
    icon = GFX_focus_generic_military_academy
    completion_reward = {
        add_to_variable = {
            MKN_army_max_planning = 0.05
            tooltip = MKN_army_max_planning_tt
        }
        army_experience = 25
        add_command_power = 20
        add_doctrine_cost_reduction = {
            name = MKN_steppe_general_staff
            cost_reduction = 0.35
            uses = 2
            category = land_doctrine
        }
    }
    cost = 5
}
```

### Гуляйпольская школа лётчиков — `MKN_gulyaipole_pilot_school`

Школа лётчиков даст общую подготовку перед выбором боевой специализации.

```pdx
focus = {
    id = MKN_gulyaipole_pilot_school
    x = 66
    y = 2
    available_if_capitulated = no
    ai_will_do = {
        factor = 1
    }
    prerequisite = {
        focus = MKN_village_airfields
    }
    icon = GFX_focus_generic_pilot_training
    completion_reward = {
        add_to_variable = {
            MKN_air_air_accidents_factor = -0.05
            tooltip = MKN_air_air_accidents_factor_tt
        }
        air_experience = 25
        add_doctrine_cost_reduction = {
            name = MKN_gulyaipole_pilot_school
            cost_reduction = 0.35
            uses = 2
            category = air_doctrine
        }
    }
    cost = 5
}
```

### Уход Батько — `MKN_departure_of_batko`

Этот фокус завершается событием смерти Махно. Его гроб закрывает эпоху, но не спор. У нас 180 дней на решение вопроса о преемственности, прежде чем степь расколется на вооружённые лагеря.

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

### Крестьяне и рабочие — `MKN_farmers_and_workers`

Вольная территория держится на руках труда, а не на коронах старого мира.

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

Каждому селу — свою коммуну, каждой коммуне — свой голос.

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

### Конница Батьки — `MKN_batko_cavalry`

Сохраним мобильность конницы, вложившись в вооружение и связь вместо дорогой брони.

```pdx
focus = {
    id = MKN_batko_cavalry
    x = 54
    y = 3
    available_if_capitulated = no
    prerequisite = {
        focus = MKN_steppe_general_staff
    }
    mutually_exclusive = {
        focus = MKN_steel_horses
    }
    icon = GFX_goal_generic_cavalry
    completion_reward = {
        add_to_variable = {
            MKN_army_modifier_army_sub_unit_cavalry_attack_factor = 0.08
            tooltip = MKN_army_modifier_army_sub_unit_cavalry_attack_factor_tt
        }
        add_equipment_to_stockpile = {
            type = infantry_equipment_0
            amount = 600
            producer = ROOT
        }
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Чёрный рой — `MKN_black_swarm`

Истребители станут щитом коммун; ударная авиация останется второстепенной.

```pdx
focus = {
    id = MKN_black_swarm
    x = 62
    y = 3
    available_if_capitulated = no
    prerequisite = {
        focus = MKN_gulyaipole_pilot_school
    }
    mutually_exclusive = {
        focus = MKN_close_support_program
    }
    icon = GFX_goal_generic_air_fighter
    completion_reward = {
        add_to_variable = {
            MKN_air_air_intercept_efficiency = 0.1
            tooltip = MKN_air_air_intercept_efficiency_tt
        }
        add_tech_bonus = {
            name = MKN_black_swarm
            bonus = 0.75
            uses = 1
            category = light_fighter
        }
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Авиация поддержки — `MKN_close_support_program`

Авиация станет летающей артиллерией для вольных колонн.

```pdx
focus = {
    id = MKN_close_support_program
    x = 70
    y = 3
    available_if_capitulated = no
    prerequisite = {
        focus = MKN_gulyaipole_pilot_school
    }
    mutually_exclusive = {
        focus = MKN_black_swarm
    }
    icon = GFX_focus_generic_cas_aircraft
    completion_reward = {
        add_to_variable = {
            MKN_air_air_cas_efficiency = 0.1
            tooltip = MKN_air_air_cas_efficiency_tt
        }
        add_tech_bonus = {
            name = MKN_close_support_program
            bonus = 0.75
            uses = 1
            category = cas_bomber
        }
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Школа черноморских рейдеров — `MKN_black_sea_smugglers`

Малые подлодки и рейдеры сделают вражеские перевозки уязвимыми без гонки линкоров.

```pdx
focus = {
    id = MKN_black_sea_smugglers
    x = 86
    y = 3
    available_if_capitulated = no
    prerequisite = {
        focus = MKN_kherson_shipyard
    }
    mutually_exclusive = {
        focus = MKN_coastal_defense_steppe
    }
    icon = GFX_focus_generic_smugglers
    completion_reward = {
        add_to_variable = {
            MKN_navy_convoy_raiding_efficiency_factor = 0.1
            tooltip = MKN_navy_convoy_raiding_efficiency_factor_tt
        }
        add_tech_bonus = {
            name = MKN_black_sea_smugglers
            bonus = 0.75
            uses = 1
            category = ss_tech
        }
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Военные берут власть — `MKN_military_takes_charge`

Тратишов расстилает железнодорожную карту на столе съезда. Революции нужно единое оперативное командование. При поддержке не менее 40% населения и подготовленном съезде правящей программой станет анархо-милитаризм.

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

Волин спрашивает делегатов, кто дал штабу право править. При подготовленном съезде и поддержке не менее 40% анархо-коммунизм станет правящей программой местных советов с отзывными делегатами.

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

Новая корона не заменит шапку Батько. Избранный совет сёл возьмёт на себя ответственность за житницу. Аграрный изоляционизм требует подготовленного съезда и поддержки не менее 40%.

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

Красные делегаты требуют администрации, способной пережить своего основателя. При подготовленном съезде и поддержке не менее 40% государственный социализм станет правящей программой.

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

### Чёрное знамя на восток — `MKN_black_banner_east`

Киев кланяется Москве. Восток надо освободить от обоих.

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

### Артель танковых экипажей — `MKN_tank_crews`

Экипаж должен уметь чинить машину и действовать вместе с пехотой.

```pdx
focus = {
    id = MKN_tank_crews
    available_if_capitulated = no
    icon = GFX_focus_generic_tank_assembly
    completion_reward = {
        add_to_variable = {
            MKN_army_army_org_factor = 0.04
            tooltip = MKN_army_army_org_factor_tt
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
    }
    x = 44
    y = 4
    prerequisite = {
        focus = MKN_steel_horses
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Школа степных квартирмейстеров — `MKN_steppe_quartermasters`

Квартирмейстеры сведут потребности моторизованных частей в единый реестр.

```pdx
focus = {
    id = MKN_steppe_quartermasters
    available_if_capitulated = no
    icon = GFX_focus_generic_reinforcing_the_supply_network
    completion_reward = {
        add_to_variable = {
            MKN_army_supply_consumption_factor = -0.05
            tooltip = MKN_army_supply_consumption_factor_tt
        }
        add_tech_bonus = {
            name = MKN_steppe_quartermasters
            bonus = 0.5
            uses = 1
            category = logistics_tech
        }
    }
    x = 48
    y = 4
    prerequisite = {
        focus = MKN_steel_horses
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Артели конского резерва — `MKN_remount_artels`

Общие конюшни и запас верховых лошадей поддержат темп похода.

```pdx
focus = {
    id = MKN_remount_artels
    available_if_capitulated = no
    icon = GFX_focus_generic_horse_studs
    completion_reward = {
        add_to_variable = {
            MKN_army_modifier_army_sub_unit_cavalry_speed_factor = 0.08
            tooltip = MKN_army_modifier_army_sub_unit_cavalry_speed_factor_tt
        }
        add_tech_bonus = {
            name = MKN_remount_artels
            bonus = 0.5
            uses = 1
            category = logistics_tech
        }
    }
    x = 56
    y = 4
    prerequisite = {
        focus = MKN_batko_cavalry
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Сеть наблюдательных постов — `MKN_observation_posts`

Наблюдатели передадут предупреждение до появления бомбардировщиков над городами.

```pdx
focus = {
    id = MKN_observation_posts
    available_if_capitulated = no
    icon = GFX_focus_generic_air_defense
    completion_reward = {
        add_to_variable = {
            MKN_air_air_interception_detect_factor = 0.1
            tooltip = MKN_air_air_interception_detect_factor_tt
        }
        add_tech_bonus = {
            name = MKN_observation_posts
            bonus = 0.5
            uses = 1
            category = radar_tech
        }
    }
    x = 64
    y = 4
    prerequisite = {
        focus = MKN_black_swarm
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Связные при наземных штабах — `MKN_air_ground_liaisons`

Связные передадут запросы пехоты прямо на аэродром.

```pdx
focus = {
    id = MKN_air_ground_liaisons
    available_if_capitulated = no
    icon = GFX_focus_generic_radio_communication
    completion_reward = {
        add_to_variable = {
            MKN_air_air_cas_efficiency = 0.05
            tooltip = MKN_air_air_cas_efficiency_tt
        }
        air_experience = 20
    }
    x = 72
    y = 4
    prerequisite = {
        focus = MKN_close_support_program
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Днепровские канонерки — `MKN_dnieper_gun_flotilla`

Речные экипажи перейдут на лёгкие мореходные корабли для прибрежной службы.

```pdx
focus = {
    id = MKN_dnieper_gun_flotilla
    available_if_capitulated = no
    icon = GFX_goal_generic_navy_cruiser
    completion_reward = {
        add_to_variable = {
            MKN_navy_naval_defense_factor = 0.05
            tooltip = MKN_navy_naval_defense_factor_tt
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
    }
    x = 76
    y = 4
    prerequisite = {
        focus = MKN_coastal_defense_steppe
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Черноморские эскорты — `MKN_black_sea_escorts`

Лёгкие эскорты Херсонской артели будут держать строй вокруг конвоя.

```pdx
focus = {
    id = MKN_black_sea_escorts
    available_if_capitulated = no
    icon = GFX_focus_MKN_company_kherson_works
    completion_reward = {
        add_to_variable = {
            MKN_navy_screening_efficiency = 0.08
            tooltip = MKN_navy_screening_efficiency_tt
        }
        add_tech_bonus = {
            name = MKN_black_sea_escorts
            bonus = 0.5
            uses = 1
            category = asw_tech
        }
    }
    x = 80
    y = 4
    prerequisite = {
        focus = MKN_coastal_defense_steppe
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Торпедные мастерские — `MKN_torpedo_artels`

Торпедные мастерские займутся качеством оружия для скрытных атак.

```pdx
focus = {
    id = MKN_torpedo_artels
    available_if_capitulated = no
    icon = GFX_focus_generic_torpedo_production
    completion_reward = {
        add_to_variable = {
            MKN_navy_naval_torpedo_hit_chance_factor = 0.05
            tooltip = MKN_navy_naval_torpedo_hit_chance_factor_tt
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
    }
    x = 84
    y = 4
    prerequisite = {
        focus = MKN_black_sea_smugglers
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Арестовать демагогов — `MKN_arrest_demagogues`

Штаб опечатывает фракционные типографии и задерживает организаторов соперничающих командований. Жестокое урегулирование останавливает 180-дневный отсчёт до гражданской войны.

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

Коммуны обязуются разрешать споры без создания соперничающих армий. Ратификация остановит отсчёт до гражданской войны и восстановит доверие к коллективному управлению.

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

Сёла прокормят общую оборону, но никогда — четыре соперничающих штаба. Их ультиматум разрешит вопрос преемственности и остановит отсчёт до гражданской войны.

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

Ревком прикажет каждому вооружённому комитету сдать оружие и списки. Разрешим вопрос преемственности и остановим 180-дневный отсчёт.

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

### Махно идёт на юг — `MKN_makhno_moves_south`

К морю, к портам, к кораблям, что везут наш хлеб.

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

### Радиостанция в каждом штабе — `MKN_radio_sections`

Радиосвязь позволит подкреплениям вступать в бой по команде штаба.

```pdx
focus = {
    id = MKN_radio_sections
    available_if_capitulated = no
    icon = GFX_focus_generic_radio_communication
    completion_reward = {
        add_to_variable = {
            MKN_army_land_reinforce_rate = 0.02
            tooltip = MKN_army_land_reinforce_rate_tt
        }
        add_tech_bonus = {
            name = MKN_radio_sections
            bonus = 0.5
            uses = 1
            category = signal_company_tech
        }
    }
    x = 44
    y = 5
    prerequisite = {
        focus = MKN_tank_crews
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Моторизованные обозы — `MKN_mobile_supply_columns`

Грузовики и заправщики будут следовать за наступающей бронёй.

```pdx
focus = {
    id = MKN_mobile_supply_columns
    available_if_capitulated = no
    icon = GFX_focus_generic_truck
    completion_reward = {
        add_to_variable = {
            MKN_army_army_fuel_consumption_factor = -0.08
            tooltip = MKN_army_army_fuel_consumption_factor_tt
        }
        add_equipment_to_stockpile = {
            type = motorized_equipment_1
            amount = 120
            producer = ROOT
        }
    }
    x = 48
    y = 5
    prerequisite = {
        focus = MKN_steppe_quartermasters
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Проводники родной степи — `MKN_local_guides`

Местные проводники найдут броды и обходные тропы раньше противника.

```pdx
focus = {
    id = MKN_local_guides
    available_if_capitulated = no
    icon = GFX_focus_generic_infiltration
    completion_reward = {
        add_to_variable = {
            MKN_army_recon_factor = 0.1
            tooltip = MKN_army_recon_factor_tt
        }
        add_tech_bonus = {
            name = MKN_local_guides
            bonus = 0.5
            uses = 1
            category = recon_tech
        }
    }
    x = 56
    y = 5
    prerequisite = {
        focus = MKN_remount_artels
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Инструкторы воздушного боя — `MKN_fighter_instructors`

Лучшие инструкторы покажут молодым пилотам приёмы боя в паре.

```pdx
focus = {
    id = MKN_fighter_instructors
    available_if_capitulated = no
    icon = GFX_focus_generic_flight_instructors
    completion_reward = {
        add_to_variable = {
            MKN_air_air_ace_generation_chance_factor = 0.15
            tooltip = MKN_air_air_ace_generation_chance_factor_tt
        }
        air_experience = 20
        add_ace = {
            name = Stepan
            surname = Koval
            callsign = Sokil
            type = fighter_genius
        }
    }
    x = 60
    y = 5
    prerequisite = {
        focus = MKN_aircraft_artels
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Полигоны точного бомбометания — `MKN_bombing_ranges`

На полигонах экипажи научатся поражать цель рядом со своими войсками.

```pdx
focus = {
    id = MKN_bombing_ranges
    available_if_capitulated = no
    icon = GFX_goal_generic_air_bomber
    completion_reward = {
        add_to_variable = {
            MKN_air_air_mission_efficiency = 0.04
            tooltip = MKN_air_air_mission_efficiency_tt
        }
        air_experience = 20
        add_doctrine_cost_reduction = {
            name = MKN_bombing_ranges
            cost_reduction = 0.5
            uses = 1
            category = air_doctrine
        }
    }
    x = 68
    y = 5
    prerequisite = {
        focus = MKN_attack_air_artels
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Береговые сигнальные посты — `MKN_coastal_signal_posts`

Береговые посты предупредят капитанов о появлении противника.

```pdx
focus = {
    id = MKN_coastal_signal_posts
    available_if_capitulated = no
    icon = GFX_focus_generic_radio_communication
    completion_reward = {
        add_to_variable = {
            MKN_navy_naval_detection = 0.08
            tooltip = MKN_navy_naval_detection_tt
        }
        add_tech_bonus = {
            name = MKN_coastal_signal_posts
            bonus = 0.5
            uses = 1
            category = radar_tech
        }
    }
    x = 76
    y = 5
    prerequisite = {
        focus = MKN_dnieper_gun_flotilla
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Школа экипажей эскортов — `MKN_escort_crews`

Экипажи отработают охранение медленных транспортов вместо погони за славой.

```pdx
focus = {
    id = MKN_escort_crews
    available_if_capitulated = no
    icon = GFX_focus_generic_naval_discipline
    completion_reward = {
        add_to_variable = {
            MKN_navy_convoy_escort_efficiency = 0.05
            tooltip = MKN_navy_convoy_escort_efficiency_tt
        }
        navy_experience = 20
        add_doctrine_cost_reduction = {
            name = MKN_escort_crews
            cost_reduction = 0.5
            uses = 1
            category = naval_doctrine
        }
    }
    x = 80
    y = 5
    prerequisite = {
        focus = MKN_black_sea_escorts
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Карты торговых маршрутов — `MKN_naval_intelligence`

Карты торговых маршрутов укажут ценные цели и безопасные районы ожидания.

```pdx
focus = {
    id = MKN_naval_intelligence
    available_if_capitulated = no
    icon = GFX_goal_generic_intelligence_exchange
    completion_reward = {
        add_to_variable = {
            MKN_navy_naval_detection = 0.08
            tooltip = MKN_navy_naval_detection_tt
        }
        add_tech_bonus = {
            name = MKN_naval_intelligence
            bonus = 0.5
            uses = 1
            category = decryption_tech
        }
    }
    x = 88
    y = 5
    prerequisite = {
        focus = MKN_submarine_crews
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Отменить выборность командиров — `MKN_abolish_election_of_commanders`

Бой не может ждать голосования об отзыве. Упраздним баланс сил и закрепим власть военных в существующей армейской организации: постоянный штаб улучшит планирование и сплочённость.

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

Штаб станет техническим бюро, подотчётным коммунам. Закрепим полный контроль советов на шкале баланса сил и улучшим взаимодействие местных боевых отрядов.

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

### Посольство в Харьков — `MKN_embassy_to_kharkov`

Упраздним баланс сил и отправим делегацию в советские республики. Первое предложение предусматривает взаимный военный транзит и обмен зерна на снабжение; Харьков вправе отказать.

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

### Степь держится — `MKN_the_steppe_holds`

Три года войны, а Вольная территория стоит. Пусть приходят.

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

### Тягачи для эвакуации — `MKN_recovery_tractors`

Эвакуационные тягачи вернут повреждённые машины в мастерские.

```pdx
focus = {
    id = MKN_recovery_tractors
    available_if_capitulated = no
    icon = GFX_focus_generic_purchase_mechanized_equipment
    completion_reward = {
        add_to_variable = {
            MKN_army_attrition = -0.08
            tooltip = MKN_army_attrition_tt
        }
        add_tech_bonus = {
            name = MKN_recovery_tractors
            bonus = 0.5
            uses = 1
            category = maintenance_company_tech
        }
    }
    x = 44
    y = 6
    prerequisite = {
        focus = MKN_radio_sections
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Разведка малыми отрядами — `MKN_scout_parties`

Разведывательные партии расчистят путь основной колонне.

```pdx
focus = {
    id = MKN_scout_parties
    available_if_capitulated = no
    icon = GFX_focus_generic_forest_brothers
    completion_reward = {
        add_to_variable = {
            MKN_army_army_speed_factor = 0.05
            tooltip = MKN_army_army_speed_factor_tt
        }
        army_experience = 15
    }
    x = 52
    y = 6
    prerequisite = {
        focus = MKN_machinegun_carts
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Ветеринарная служба колонн — `MKN_field_veterinary`

Ветеринарная служба снизит потери лошадей в длительных переходах.

```pdx
focus = {
    id = MKN_field_veterinary
    available_if_capitulated = no
    icon = GFX_focus_generic_agricultural_subsidies
    completion_reward = {
        add_to_variable = {
            MKN_army_attrition = -0.08
            tooltip = MKN_army_attrition_tt
        }
        add_tech_bonus = {
            name = MKN_field_veterinary
            bonus = 0.5
            uses = 1
            category = logistics_tech
        }
    }
    x = 56
    y = 6
    prerequisite = {
        focus = MKN_local_guides
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Радиомаяки полевых полос — `MKN_radio_beacons`

Радиомаяки помогут перехватчикам вернуться даже в плохую погоду.

```pdx
focus = {
    id = MKN_radio_beacons
    available_if_capitulated = no
    icon = GFX_focus_generic_phone
    completion_reward = {
        add_to_variable = {
            MKN_air_air_mission_efficiency = 0.05
            tooltip = MKN_air_air_mission_efficiency_tt
        }
        add_tech_bonus = {
            name = MKN_radio_beacons
            bonus = 0.5
            uses = 1
            category = signal_company_tech
        }
    }
    x = 60
    y = 6
    prerequisite = {
        focus = MKN_fighter_instructors
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Общее картографическое бюро — `MKN_air_map_bureau`

Карты, фотосъёмка и единая сетка координат избавят экипажи от поиска цели вслепую.

```pdx
focus = {
    id = MKN_air_map_bureau
    available_if_capitulated = no
    icon = GFX_focus_generic_advanced_military_studies
    completion_reward = {
        add_to_variable = {
            MKN_air_air_mission_efficiency = 0.04
            tooltip = MKN_air_air_mission_efficiency_tt
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
    }
    x = 68
    y = 6
    prerequisite = {
        focus = MKN_bombing_ranges
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Артели судового ремонта — `MKN_hull_repair_artels`

Судоремонтные артели освоят замену повреждённых секций и переоборудование.

```pdx
focus = {
    id = MKN_hull_repair_artels
    available_if_capitulated = no
    icon = GFX_focus_generic_refit_civilian_ships
    completion_reward = {
        add_to_variable = {
            MKN_navy_repair_speed_factor = 0.15
            tooltip = MKN_navy_repair_speed_factor_tt
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
    }
    x = 80
    y = 6
    prerequisite = {
        focus = MKN_escort_crews
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Испытания торпед — `MKN_torpedo_trials`

Испытания устранят отказы и уточнят дистанцию атаки.

```pdx
focus = {
    id = MKN_torpedo_trials
    available_if_capitulated = no
    icon = GFX_focus_generic_navy_research_bonus
    completion_reward = {
        add_to_variable = {
            MKN_navy_naval_torpedo_hit_chance_factor = 0.05
            tooltip = MKN_navy_naval_torpedo_hit_chance_factor_tt
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
    }
    x = 88
    y = 6
    prerequisite = {
        focus = MKN_naval_intelligence
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Оружие народу — `MKN_arms_to_the_people`

Выдадим винтовки из общих складов и сформируем три оснащённых отряда коммунальной гвардии. Расширенная система набора сделает каждое село ответственным за свою оборону.

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

### Объединить стальные магистрали — `MKN_integrate_steel_lines`

С согласия советской стороны и при контролируемой общей границе построим железнодорожное соединение второго уровня. Получим десять локомотивов и два года помощи в организации снабжения.

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

«Набат» и «Голос» ежедневно печатают правду.

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

### Связь между волостями — `MKN_militia_signals`

Сигнальные команды свяжут волости и выведут резерв на нужный участок.

```pdx
focus = {
    id = MKN_militia_signals
    available_if_capitulated = no
    icon = GFX_focus_generic_radio_communication
    completion_reward = {
        add_to_variable = {
            MKN_army_land_reinforce_rate = 0.02
            tooltip = MKN_army_land_reinforce_rate_tt
        }
        add_tech_bonus = {
            name = MKN_militia_signals
            bonus = 0.5
            uses = 1
            category = signal_company_tech
        }
    }
    x = 52
    y = 7
    prerequisite = {
        focus = MKN_scout_parties
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Ночные переходы — `MKN_night_marches`

Отряды научатся уходить из-под удара ночью без распада колонны.

```pdx
focus = {
    id = MKN_night_marches
    available_if_capitulated = no
    icon = GFX_focus_generic_nighttime_bombing
    completion_reward = {
        add_to_variable = {
            MKN_army_org_loss_when_moving = -0.1
            tooltip = MKN_army_org_loss_when_moving_tt
        }
        army_experience = 20
    }
    x = 56
    y = 7
    prerequisite = {
        focus = MKN_field_veterinary
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Возвращать повреждённые машины — `MKN_aircraft_recovery`

Эвакуационные бригады вернут повреждённые машины и спасут ремонтный фонд.

```pdx
focus = {
    id = MKN_aircraft_recovery
    available_if_capitulated = no
    icon = GFX_focus_generic_industrial_experts
    completion_reward = {
        add_to_variable = {
            MKN_air_air_accidents_factor = -0.05
            tooltip = MKN_air_air_accidents_factor_tt
        }
        add_tech_bonus = {
            name = MKN_aircraft_recovery
            bonus = 0.5
            uses = 1
            category = maintenance_company_tech
        }
    }
    x = 64
    y = 7
    prerequisite = {
        focus = MKN_airframe_jigs
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Обозначение целей с земли — `MKN_target_markers`

Дымовые сигналы и условные полотнища обозначат передний край.

```pdx
focus = {
    id = MKN_target_markers
    available_if_capitulated = no
    icon = GFX_focus_generic_daytime_bombing
    completion_reward = {
        add_to_variable = {
            MKN_air_air_cas_efficiency = 0.05
            tooltip = MKN_air_air_cas_efficiency_tt
        }
        air_experience = 15
    }
    x = 68
    y = 7
    prerequisite = {
        focus = MKN_air_map_bureau
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Расписания зерновых конвоев — `MKN_convoy_schedules`

Общие расписания и новые транспорты позволят сопровождать торговлю организованными группами.

```pdx
focus = {
    id = MKN_convoy_schedules
    available_if_capitulated = no
    icon = GFX_focus_generic_merchant_fleet
    completion_reward = {
        add_to_variable = {
            MKN_navy_convoy_escort_efficiency = 0.05
            tooltip = MKN_navy_convoy_escort_efficiency_tt
        }
        add_equipment_to_stockpile = {
            type = convoy_1
            amount = 20
            producer = ROOT
        }
    }
    x = 80
    y = 7
    prerequisite = {
        focus = MKN_hull_repair_artels
    }
    ai_will_do = {
        factor = 3
    }
    cost = 5
}
```

### Пропаганда действием — `MKN_propaganda_by_deed`

Погасшая печь говорит громче манифеста. Откроем сети стачек в соседних странах; их правительства должны будут переждать остановку производства или заплатить за её подавление.

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

### Красные военные специалисты — `MKN_red_military_specialists`

Прибывшие инструкторы привезут штатные таблицы, а не проповеди. Улучшим сплочённость и планирование армии, получим опыт и освоение сухопутной доктрины.

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

### Съезд вольных советов — `MKN_constituent_assembly`

Для передачи власти отзывным делегатам советов нужна поддержка не менее 40%. Анархо-коммунизм использует демократическую группу идеологий, но общегосударственные парламентские выборы отключены. Баланс смещается на 0,45 к вольным советам.

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

### Красный компромисс — `MKN_red_banner_steppe`

При поддержке не менее 40% государственные социалисты создают центральное управление, признавая местные советы. Баланс смещается на 0,35 к советам. Независимая коммунистическая Москва получает предложение об оборонительном союзе, если страны не воюют друг с другом и Вольная территория не состоит в альянсе.

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

### Крестьянский покровитель — `MKN_nestor_the_first`

При поддержке не менее 40% крестьянский съезд выбирает аграрный изоляционизм под покровительством Нестора I. Спор командования с советами упраздняется вместе со шкалой баланса и её модификаторами. Махно сохраняет корону и портрет, а его военные должности остаются доступны только при коммунизме.

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

### Пехота вслед за бронёй — `MKN_motorized_infantry`

Подвижная пехота закрепит захваченные танками переправы и населённые пункты.

```pdx
focus = {
    id = MKN_motorized_infantry
    available_if_capitulated = no
    icon = GFX_goal_generic_army_motorized
    completion_reward = {
        add_to_variable = {
            MKN_army_modifier_army_sub_unit_infantry_speed_factor = 0.05
            tooltip = MKN_army_modifier_army_sub_unit_infantry_speed_factor_tt
        }
        add_tech_bonus = {
            name = MKN_motorized_infantry
            bonus = 0.75
            uses = 1
            category = cat_mechanized_equipment
        }
    }
    x = 48
    y = 9
    prerequisite = {
        focus = MKN_fire_tables
    }
    ai_will_do = {
        factor = 1
    }
    cost = 5
}
```

### Тактическая воздушная разведка — `MKN_tactical_recon`

Воздушная разведка укажет колоннам обходные пути и вражеские резервы.

```pdx
focus = {
    id = MKN_tactical_recon
    available_if_capitulated = no
    icon = GFX_focus_generic_swooping_falcon
    completion_reward = {
        add_to_variable = {
            MKN_air_recon_factor = 0.1
            tooltip = MKN_air_recon_factor_tt
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
    }
    x = 72
    y = 9
    prerequisite = {
        focus = MKN_flying_artillery
    }
    ai_will_do = {
        factor = 1
    }
    cost = 5
}
```

### Артели аварийного ремонта — `MKN_fleet_damage_control`

Аварийные команды спасут корабль после попадания и вернут его в порт.

```pdx
focus = {
    id = MKN_fleet_damage_control
    available_if_capitulated = no
    icon = GFX_focus_generic_industrial_experts
    completion_reward = {
        add_to_variable = {
            MKN_navy_naval_ship_recovery_chance_factor = 0.1
            tooltip = MKN_navy_naval_ship_recovery_chance_factor_tt
        }
        navy_experience = 15
    }
    x = 76
    y = 9
    prerequisite = {
        focus = MKN_depth_charge_school
    }
    ai_will_do = {
        factor = 1
    }
    cost = 5
}
```

### Постоянный береговой дозор — `MKN_coastal_watch`

Постоянный дозор закроет промежутки между портовыми районами.

```pdx
focus = {
    id = MKN_coastal_watch
    available_if_capitulated = no
    icon = GFX_goal_generic_radar
    completion_reward = {
        add_to_variable = {
            MKN_navy_naval_detection = 0.08
            tooltip = MKN_navy_naval_detection_tt
        }
        add_tech_bonus = {
            name = MKN_coastal_watch
            bonus = 0.75
            uses = 1
            category = radar_tech
        }
    }
    x = 80
    y = 9
    prerequisite = {
        focus = MKN_convoy_schedules
    }
    ai_will_do = {
        factor = 1
    }
    cost = 5
}
```

### Школа гидроакустиков — `MKN_submarine_listening`

Гидроакустики услышат цель раньше, чем противник заметит подлодку.

```pdx
focus = {
    id = MKN_submarine_listening
    available_if_capitulated = no
    icon = GFX_focus_generic_radio_communication
    completion_reward = {
        add_to_variable = {
            MKN_navy_naval_detection = 0.08
            tooltip = MKN_navy_naval_detection_tt
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
    }
    x = 84
    y = 9
    prerequisite = {
        focus = MKN_night_sorties
    }
    ai_will_do = {
        factor = 1
    }
    cost = 5
}
```

### Махновская традиция — `MKN_everlasting_makhnovshchina`

Съезд может вновь пригласить Махно как гражданского делегата без восстановления его военной должности. Добровольная оборона и автономия общин усиливают советы на 0,20.

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

### Оборона крестьянского края — `MKN_steppe_empire`

Покровительство готовится защищать деревни, не стремясь к внешним завоеваниям. Нестор остаётся монархом, связанным соглашениями крестьянского съезда.

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

### Мостовые колонны — `MKN_bridge_columns`

Сборные мосты позволят колоннам продолжать наступление за Днепром.

```pdx
focus = {
    id = MKN_bridge_columns
    available_if_capitulated = no
    icon = GFX_focus_generic_land_reclamation
    completion_reward = {
        add_to_variable = {
            MKN_army_army_speed_factor = 0.04
            tooltip = MKN_army_army_speed_factor_tt
        }
        add_tech_bonus = {
            name = MKN_bridge_columns
            bonus = 0.5
            uses = 1
            category = engineers_tech
        }
    }
    x = 44
    y = 10
    ai_will_do = {
        factor = 1
    }
    cost = 5
    prerequisite = {
        focus = MKN_artillery_artels
    }
}
```

### Школа радиолокации — `MKN_air_radar_school`

Радиолокационная школа научит расчёты сопровождать цели и наводить истребители.

```pdx
focus = {
    id = MKN_air_radar_school
    available_if_capitulated = no
    icon = GFX_goal_generic_radar
    completion_reward = {
        add_to_variable = {
            MKN_air_air_interception_detect_factor = 0.1
            tooltip = MKN_air_air_interception_detect_factor_tt
        }
        add_tech_bonus = {
            name = MKN_air_radar_school
            bonus = 0.75
            uses = 1
            category = radar_tech
        }
    }
    x = 60
    y = 10
    prerequisite = {
        focus = MKN_air_dispersal
    }
    ai_will_do = {
        factor = 1
    }
    cost = 5
}
```

### Доставка срочных грузов — `MKN_air_supply_lift`

Воздушные перевозки восполнят самые срочные нужды оторвавшихся колонн.

```pdx
focus = {
    id = MKN_air_supply_lift
    available_if_capitulated = no
    icon = GFX_focus_generic_supply_line
    completion_reward = {
        add_to_variable = {
            MKN_air_supply_consumption_factor = -0.03
            tooltip = MKN_air_supply_consumption_factor_tt
        }
        add_tech_bonus = {
            name = MKN_air_supply_lift
            bonus = 0.5
            uses = 1
            category = air_equipment
        }
    }
    x = 72
    y = 10
    prerequisite = {
        focus = MKN_tactical_recon
    }
    ai_will_do = {
        factor = 1
    }
    cost = 5
}
```

### Тральные отряды — `MKN_sweeper_sections`

Тральные команды очистят торговые фарватеры от мин.

```pdx
focus = {
    id = MKN_sweeper_sections
    available_if_capitulated = no
    icon = GFX_focus_generic_mine_warfare
    completion_reward = {
        add_to_variable = {
            MKN_navy_mines_sweeping_by_fleets_factor = 0.25
            tooltip = MKN_navy_mines_sweeping_by_fleets_factor_tt
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
    }
    x = 76
    y = 10
    prerequisite = {
        focus = MKN_fleet_damage_control
    }
    ai_will_do = {
        factor = 1
    }
    cost = 5
}
```

### Радиодисциплина рейдеров — `MKN_raider_radio_discipline`

Короткие зашифрованные передачи затруднят поиск рейдерских групп.

```pdx
focus = {
    id = MKN_raider_radio_discipline
    available_if_capitulated = no
    icon = GFX_focus_generic_phone
    completion_reward = {
        add_to_variable = {
            MKN_navy_naval_torpedo_reveal_chance_factor = -0.08
            tooltip = MKN_navy_naval_torpedo_reveal_chance_factor_tt
        }
        add_tech_bonus = {
            name = MKN_raider_radio_discipline
            bonus = 0.5
            uses = 1
            category = encryption_tech
        }
    }
    x = 84
    y = 10
    prerequisite = {
        focus = MKN_submarine_listening
    }
    ai_will_do = {
        factor = 1
    }
    cost = 5
}
```

### Штабные игры на Днепре — `MKN_staff_games`

Проверим планы на штабных играх прежде, чем проверять их людьми.

```pdx
focus = {
    id = MKN_staff_games
    available_if_capitulated = no
    icon = GFX_focus_generic_advanced_military_studies
    completion_reward = {
        add_to_variable = {
            MKN_army_planning_speed = 0.15
            tooltip = MKN_army_planning_speed_tt
        }
        add_doctrine_cost_reduction = {
            name = MKN_staff_games
            cost_reduction = 0.5
            uses = 2
            category = land_doctrine
        }
    }
    x = 44
    y = 11
    prerequisite = {
        focus = MKN_bridge_columns
    }
    ai_will_do = {
        factor = 1
    }
    cost = 5
}
```

### Общий запас авиационных деталей — `MKN_aircraft_spares`

Общий запас моторов сократит простои и аварии изношенных самолётов.

```pdx
focus = {
    id = MKN_aircraft_spares
    available_if_capitulated = no
    icon = GFX_focus_generic_mass_production
    completion_reward = {
        add_to_variable = {
            MKN_air_air_accidents_factor = -0.05
            tooltip = MKN_air_air_accidents_factor_tt
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
    }
    x = 60
    y = 11
    prerequisite = {
        focus = MKN_air_radar_school
    }
    ai_will_do = {
        factor = 1
    }
    cost = 5
}
```

### Резерв экипажей штурмовиков — `MKN_cas_replacement_crews`

Резерв подготовленных экипажей позволит сохранять темп вылетов.

```pdx
focus = {
    id = MKN_cas_replacement_crews
    available_if_capitulated = no
    icon = GFX_focus_generic_pilot_training
    completion_reward = {
        add_to_variable = {
            MKN_air_air_accidents_factor = -0.05
            tooltip = MKN_air_air_accidents_factor_tt
        }
        air_experience = 20
    }
    x = 72
    y = 11
    prerequisite = {
        focus = MKN_air_supply_lift
    }
    ai_will_do = {
        factor = 1
    }
    cost = 5
}
```

### Тачаночная гвардия — `MKN_tachanka_guards`

Элита Повстанческой армии.

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

### Единый боевой порядок — `MKN_combined_arms`

Броня, артиллерия и пехота научатся действовать в одном боевом порядке.

```pdx
focus = {
    id = MKN_combined_arms
    available_if_capitulated = no
    icon = GFX_focus_generic_combined_arms
    completion_reward = {
        add_to_variable = {
            MKN_army_army_armor_attack_factor = 0.05
            tooltip = MKN_army_army_armor_attack_factor_tt
        }
        army_experience = 25
        add_doctrine_cost_reduction = {
            name = MKN_combined_arms
            cost_reduction = 0.5
            uses = 1
            category = land_doctrine
        }
    }
    x = 44
    y = 12
    prerequisite = {
        focus = MKN_staff_games
    }
    ai_will_do = {
        factor = 1
    }
    cost = 5
}
```

### Спасение сбитых лётчиков — `MKN_air_rescue`

Спасённый лётчик вернётся к полётам и передаст опыт новым экипажам.

```pdx
focus = {
    id = MKN_air_rescue
    available_if_capitulated = no
    icon = GFX_focus_generic_field_hostpital
    completion_reward = {
        add_to_variable = {
            MKN_air_air_ace_generation_chance_factor = 0.1
            tooltip = MKN_air_air_ace_generation_chance_factor_tt
        }
        air_experience = 15
    }
    x = 60
    y = 12
    prerequisite = {
        focus = MKN_aircraft_spares
    }
    ai_will_do = {
        factor = 1
    }
    cost = 5
}
```

### Противолодочные патрули — `MKN_anti_submarine_patrols`

Охотничьи группы будут прочёсывать район перед выходом конвоев.

```pdx
focus = {
    id = MKN_anti_submarine_patrols
    available_if_capitulated = no
    icon = GFX_goal_generic_navy_anti_submarine
    completion_reward = {
        add_to_variable = {
            MKN_navy_navy_submarine_detection_factor = 0.15
            tooltip = MKN_navy_navy_submarine_detection_factor_tt
        }
        add_tech_bonus = {
            name = MKN_anti_submarine_patrols
            bonus = 0.5
            uses = 1
            category = asw_tech
        }
        navy_experience = 20
    }
    x = 76
    y = 12
    prerequisite = {
        focus = MKN_coastal_depots
    }
    ai_will_do = {
        factor = 1
    }
    cost = 5
}
```

## Общая экономика: исходные значения и восстановление

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
    }
    if = {
        limit = {
            has_completed_focus = MKN_craft_federation
        }
        add_to_variable = {
            MKN_unified_supply_consumption_factor = -0.1300
        }
        add_to_variable = {
            MKN_unified_army_org_regain = 0.0400
        }
        add_to_variable = {
            MKN_unified_attrition = -0.0500
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
            has_completed_focus = MKN_dnieper_dispatch
        }
        add_to_variable = {
            MKN_unified_supply_consumption_factor = -0.0700
        }
        add_to_variable = {
            MKN_unified_army_org_regain = 0.0600
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_elected_brigadiers
        }
        add_to_variable = {
            MKN_unified_army_org_factor = 0.0500
        }
        add_to_variable = {
            MKN_unified_training_time_army_factor = -0.0800
        }
        add_to_variable = {
            MKN_unified_max_planning = 0.0400
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_engineering_delegates
        }
        add_to_variable = {
            MKN_unified_production_factory_efficiency_gain_factor = 0.0800
        }
        add_to_variable = {
            MKN_unified_research_speed_factor = 0.0200
        }
        add_to_variable = {
            MKN_unified_industrial_capacity_factory = 0.0500
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_factory_instructors
        }
        add_to_variable = {
            MKN_unified_army_org_factor = 0.0600
        }
        add_to_variable = {
            MKN_unified_training_time_army_factor = -0.0700
        }
        add_to_variable = {
            MKN_unified_max_planning = 0.0300
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_field_schools
        }
        add_to_variable = {
            MKN_unified_army_org_factor = 0.0600
        }
        add_to_variable = {
            MKN_unified_training_time_army_factor = -0.0700
        }
        add_to_variable = {
            MKN_unified_max_planning = 0.0300
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
            has_completed_focus = MKN_freight_artels
        }
        add_to_variable = {
            MKN_unified_supply_consumption_factor = -0.0800
        }
        add_to_variable = {
            MKN_unified_army_org_regain = 0.0500
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_industrial_compact
        }
        add_to_variable = {
            MKN_unified_political_power_gain = 0.1500
        }
        add_to_variable = {
            MKN_unified_consumer_goods_factor = -0.0500
        }
        add_to_variable = {
            MKN_unified_production_speed_buildings_factor = 0.1300
        }
        add_to_variable = {
            MKN_unified_global_building_slots_factor = 0.3000
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_kichkas_bridge
        }
        add_to_variable = {
            MKN_unified_supply_consumption_factor = -0.0800
        }
        add_to_variable = {
            MKN_unified_army_org_regain = 0.0500
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_mobile_self_defence
        }
        add_to_variable = {
            MKN_unified_army_org_factor = 0.0800
        }
        add_to_variable = {
            MKN_unified_training_time_army_factor = -0.1000
        }
        add_to_variable = {
            MKN_unified_max_planning = 0.0300
        }
        add_to_variable = {
            MKN_unified_army_speed_factor = 0.0500
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
            MKN_unified_industrial_capacity_factory = 0.0500
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_nikopol_tube_zavod
        }
        add_to_variable = {
            MKN_unified_industrial_capacity_factory = 0.0500
        }
        add_to_variable = {
            MKN_unified_production_factory_efficiency_gain_factor = 0.0700
        }
        add_to_variable = {
            MKN_unified_research_speed_factor = 0.0200
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_production_cycles
        }
        add_to_variable = {
            MKN_unified_industrial_capacity_factory = 0.1500
        }
        add_to_variable = {
            MKN_unified_production_factory_efficiency_gain_factor = 0.0500
        }
        add_to_variable = {
            MKN_unified_research_speed_factor = 0.0100
        }
        add_to_variable = {
            MKN_unified_production_factory_max_efficiency_factor = 0.1000
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_recallable_commanders
        }
        add_to_variable = {
            MKN_unified_army_org_factor = 0.0500
        }
        add_to_variable = {
            MKN_unified_training_time_army_factor = -0.0800
        }
        add_to_variable = {
            MKN_unified_max_planning = 0.0400
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_shared_orders
        }
        add_to_variable = {
            MKN_unified_industrial_capacity_factory = 0.1100
        }
        add_to_variable = {
            MKN_unified_production_factory_efficiency_gain_factor = 0.2000
        }
        add_to_variable = {
            MKN_unified_research_speed_factor = 0.0400
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_steel_volnitsa
        }
        add_to_variable = {
            MKN_unified_supply_consumption_factor = -0.1500
        }
        add_to_variable = {
            MKN_unified_army_org_regain = 0.0900
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
            has_completed_focus = MKN_steppe_mint
        }
        add_to_variable = {
            MKN_unified_political_power_gain = 0.2000
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_supply_congress
        }
        add_to_variable = {
            MKN_unified_supply_consumption_factor = -0.0700
        }
        add_to_variable = {
            MKN_unified_army_org_regain = 0.0600
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_village_smithies
        }
        add_to_variable = {
            MKN_unified_production_factory_efficiency_gain_factor = 0.0800
        }
        add_to_variable = {
            MKN_unified_research_speed_factor = 0.0200
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
            MKN_unified_army_org_factor = 0.1000
        }
        add_to_variable = {
            MKN_unified_training_time_army_factor = -0.0500
        }
        add_to_variable = {
            MKN_unified_max_planning = 0.0800
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_workshop_standards
        }
        add_to_variable = {
            MKN_unified_industrial_capacity_factory = 0.0500
        }
        add_to_variable = {
            MKN_unified_production_factory_efficiency_gain_factor = 0.0700
        }
        add_to_variable = {
            MKN_unified_research_speed_factor = 0.0200
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
    set_country_flag = MKN_industry_unified_v2
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
            has_completed_focus = MKN_artel_register
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
    }
    if = {
        limit = {
            has_completed_focus = MKN_kommunar_tractor
        }
        add_to_variable = {
            MKN_unified_industrial_capacity_factory = 0.0500
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
}
nww_mkn_rebuild_services = {
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
    if = {
        limit = {
            has_completed_focus = MKN_tachanka_columns
        }
        add_to_variable = {
            MKN_army_army_org_factor = 0.04
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_railway_war
        }
        add_to_variable = {
            MKN_army_supply_consumption_factor = -0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_steppe_general_staff
        }
        add_to_variable = {
            MKN_army_max_planning = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_steel_horses
        }
        add_to_variable = {
            MKN_army_army_armor_attack_factor = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_batko_cavalry
        }
        add_to_variable = {
            MKN_army_modifier_army_sub_unit_cavalry_attack_factor = 0.08
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_steppe_quartermasters
        }
        add_to_variable = {
            MKN_army_supply_consumption_factor = -0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_artillery_artels
        }
        add_to_variable = {
            MKN_army_modifier_army_sub_unit_infantry_attack_factor = 0.04
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_mobile_supply_columns
        }
        add_to_variable = {
            MKN_army_army_fuel_consumption_factor = -0.08
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_tank_crews
        }
        add_to_variable = {
            MKN_army_army_org_factor = 0.04
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_radio_sections
        }
        add_to_variable = {
            MKN_army_land_reinforce_rate = 0.02
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_recovery_tractors
        }
        add_to_variable = {
            MKN_army_attrition = -0.08
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_tank_maintenance
        }
        add_to_variable = {
            MKN_army_repair_speed_factor = 0.1
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_fire_tables
        }
        add_to_variable = {
            MKN_army_max_planning = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_motorized_infantry
        }
        add_to_variable = {
            MKN_army_modifier_army_sub_unit_infantry_speed_factor = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_bridge_columns
        }
        add_to_variable = {
            MKN_army_army_speed_factor = 0.04
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_fuel_discipline
        }
        add_to_variable = {
            MKN_army_army_fuel_consumption_factor = -0.1
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_staff_games
        }
        add_to_variable = {
            MKN_army_planning_speed = 0.15
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_mobile_medical
        }
        add_to_variable = {
            MKN_army_casualty_trickleback = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_combined_arms
        }
        add_to_variable = {
            MKN_army_army_armor_attack_factor = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_deep_reserves
        }
        add_to_variable = {
            MKN_army_land_reinforce_rate = 0.02
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_breakthrough_workshops
        }
        add_to_variable = {
            MKN_army_army_armor_attack_factor = 0.04
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_armoured_manoeuvres
        }
        add_to_variable = {
            MKN_army_org_loss_when_moving = -0.1
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_mechanized_compact
        }
        add_to_variable = {
            MKN_army_army_armor_attack_factor = 0.06
        }
        add_to_variable = {
            MKN_army_army_org_factor = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_village_muster
        }
        add_to_variable = {
            MKN_army_mobilization_speed = 0.15
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_remount_artels
        }
        add_to_variable = {
            MKN_army_modifier_army_sub_unit_cavalry_speed_factor = 0.08
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_machinegun_carts
        }
        add_to_variable = {
            MKN_army_modifier_army_sub_unit_cavalry_attack_factor = 0.07
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_local_guides
        }
        add_to_variable = {
            MKN_army_recon_factor = 0.1
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_scout_parties
        }
        add_to_variable = {
            MKN_army_army_speed_factor = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_field_veterinary
        }
        add_to_variable = {
            MKN_army_attrition = -0.08
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_militia_signals
        }
        add_to_variable = {
            MKN_army_land_reinforce_rate = 0.02
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_night_marches
        }
        add_to_variable = {
            MKN_army_org_loss_when_moving = -0.1
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_militia_junior_leaders
        }
        add_to_variable = {
            MKN_army_army_org_factor = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_hidden_depots
        }
        add_to_variable = {
            MKN_army_supply_consumption_factor = -0.08
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_militia_engineers
        }
        add_to_variable = {
            MKN_army_dig_in_speed_factor = 0.2
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_militia_hospitals
        }
        add_to_variable = {
            MKN_army_casualty_trickleback = 0.06
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_flexible_orders
        }
        add_to_variable = {
            MKN_army_planning_speed = 0.15
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_rural_reserve
        }
        add_to_variable = {
            MKN_army_conscription = 0.02
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_tachanka_tactics
        }
        add_to_variable = {
            MKN_army_modifier_army_sub_unit_cavalry_defence_factor = 0.08
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_steppe_camouflage
        }
        add_to_variable = {
            MKN_army_max_dig_in = 2.0
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_mobile_rearguard
        }
        add_to_variable = {
            MKN_army_modifier_army_sub_unit_infantry_defence_factor = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_free_column_exercises
        }
        add_to_variable = {
            MKN_army_army_org_factor = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_free_army_compact
        }
        add_to_variable = {
            MKN_army_modifier_army_sub_unit_cavalry_attack_factor = 0.05
        }
        add_to_variable = {
            MKN_army_supply_consumption_factor = -0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_tachanka_columns
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
    if = {
        limit = {
            has_completed_focus = MKN_steppe_hawks
        }
        add_to_variable = {
            MKN_air_air_mission_efficiency = 0.03
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_village_airfields
        }
        add_to_variable = {
            MKN_air_air_range_factor = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_gulyaipole_pilot_school
        }
        add_to_variable = {
            MKN_air_air_accidents_factor = -0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_black_swarm
        }
        add_to_variable = {
            MKN_air_air_intercept_efficiency = 0.1
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_aircraft_artels
        }
        add_to_variable = {
            MKN_air_air_agility_factor = 0.04
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_observation_posts
        }
        add_to_variable = {
            MKN_air_air_interception_detect_factor = 0.1
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_fighter_instructors
        }
        add_to_variable = {
            MKN_air_air_ace_generation_chance_factor = 0.15
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_air_warning
        }
        add_to_variable = {
            MKN_air_air_intercept_efficiency = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_radio_beacons
        }
        add_to_variable = {
            MKN_air_air_mission_efficiency = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_airframe_jigs
        }
        add_to_variable = {
            MKN_air_air_attack_factor = 0.04
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_interceptor_pairs
        }
        add_to_variable = {
            MKN_air_air_agility_factor = 0.04
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_aircraft_recovery
        }
        add_to_variable = {
            MKN_air_air_accidents_factor = -0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_air_dispersal
        }
        add_to_variable = {
            MKN_air_air_home_defence_factor = 0.1
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_fighter_patrols
        }
        add_to_variable = {
            MKN_air_air_range_factor = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_air_radar_school
        }
        add_to_variable = {
            MKN_air_air_interception_detect_factor = 0.1
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_night_interceptors
        }
        add_to_variable = {
            MKN_air_air_intercept_efficiency = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_aircraft_spares
        }
        add_to_variable = {
            MKN_air_air_accidents_factor = -0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_fighter_conversion
        }
        add_to_variable = {
            MKN_air_air_agility_factor = 0.04
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_air_rescue
        }
        add_to_variable = {
            MKN_air_air_ace_generation_chance_factor = 0.1
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_fighter_controllers
        }
        add_to_variable = {
            MKN_air_air_mission_efficiency = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_air_home_defence
        }
        add_to_variable = {
            MKN_air_air_home_defence_factor = 0.1
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_sky_watch_exercises
        }
        add_to_variable = {
            MKN_air_air_attack_factor = 0.04
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_free_sky_compact
        }
        add_to_variable = {
            MKN_air_air_intercept_efficiency = 0.1
        }
        add_to_variable = {
            MKN_air_air_agility_factor = 0.04
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_close_support_program
        }
        add_to_variable = {
            MKN_air_air_cas_efficiency = 0.1
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_attack_air_artels
        }
        add_to_variable = {
            MKN_air_air_attack_factor = 0.04
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_air_ground_liaisons
        }
        add_to_variable = {
            MKN_air_air_cas_efficiency = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_bombing_ranges
        }
        add_to_variable = {
            MKN_air_air_mission_efficiency = 0.04
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_forward_airstrips
        }
        add_to_variable = {
            MKN_air_air_range_factor = 0.08
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_air_map_bureau
        }
        add_to_variable = {
            MKN_air_air_mission_efficiency = 0.04
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_cas_maintenance
        }
        add_to_variable = {
            MKN_air_air_accidents_factor = -0.08
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_target_markers
        }
        add_to_variable = {
            MKN_air_air_cas_efficiency = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_flying_artillery
        }
        add_to_variable = {
            MKN_air_air_cas_efficiency = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_airfield_fuel
        }
        add_to_variable = {
            MKN_air_air_fuel_consumption_factor = -0.1
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_tactical_recon
        }
        add_to_variable = {
            MKN_air_recon_factor = 0.1
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_bomber_navigation
        }
        add_to_variable = {
            MKN_air_air_range_factor = 0.07
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_air_supply_lift
        }
        add_to_variable = {
            MKN_air_supply_consumption_factor = -0.03
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_air_coastal_support
        }
        add_to_variable = {
            MKN_air_naval_strike_attack_factor = 0.1
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_cas_replacement_crews
        }
        add_to_variable = {
            MKN_air_air_accidents_factor = -0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_joint_target_planning
        }
        add_to_variable = {
            MKN_air_air_cas_efficiency = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_air_weather_service
        }
        add_to_variable = {
            MKN_air_air_mission_efficiency = 0.04
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_attack_wing_rotations
        }
        add_to_variable = {
            MKN_air_air_fuel_consumption_factor = -0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_cas_joint_exercises
        }
        add_to_variable = {
            MKN_air_air_cas_efficiency = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_air_support_compact
        }
        add_to_variable = {
            MKN_air_air_cas_efficiency = 0.05
        }
        add_to_variable = {
            MKN_air_air_mission_efficiency = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_steppe_hawks
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
            has_completed_focus = MKN_black_sea_flotilla
        }
        add_to_variable = {
            MKN_navy_naval_defense_factor = 0.03
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_dnieper_patrol
        }
        add_to_variable = {
            MKN_navy_naval_detection = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_kherson_shipyard
        }
        add_to_variable = {
            MKN_navy_industrial_capacity_dockyard = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_coastal_defense_steppe
        }
        add_to_variable = {
            MKN_navy_convoy_escort_efficiency = 0.1
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_black_sea_smugglers
        }
        add_to_variable = {
            MKN_navy_convoy_raiding_efficiency_factor = 0.1
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_dnieper_gun_flotilla
        }
        add_to_variable = {
            MKN_navy_naval_defense_factor = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_black_sea_escorts
        }
        add_to_variable = {
            MKN_navy_screening_efficiency = 0.08
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_coastal_signal_posts
        }
        add_to_variable = {
            MKN_navy_naval_detection = 0.08
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_escort_crews
        }
        add_to_variable = {
            MKN_navy_convoy_escort_efficiency = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_harbour_dredging
        }
        add_to_variable = {
            MKN_navy_navy_fuel_consumption_factor = -0.08
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_hull_repair_artels
        }
        add_to_variable = {
            MKN_navy_repair_speed_factor = 0.15
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_depth_charge_school
        }
        add_to_variable = {
            MKN_navy_navy_submarine_detection_factor = 0.15
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_convoy_schedules
        }
        add_to_variable = {
            MKN_navy_convoy_escort_efficiency = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_fleet_damage_control
        }
        add_to_variable = {
            MKN_navy_naval_ship_recovery_chance_factor = 0.1
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_coastal_watch
        }
        add_to_variable = {
            MKN_navy_naval_detection = 0.08
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_sweeper_sections
        }
        add_to_variable = {
            MKN_navy_mines_sweeping_by_fleets_factor = 0.25
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_escort_radio_net
        }
        add_to_variable = {
            MKN_navy_screening_efficiency = 0.07
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_coastal_depots
        }
        add_to_variable = {
            MKN_navy_navy_fuel_consumption_factor = -0.1
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_river_sea_coordination
        }
        add_to_variable = {
            MKN_navy_naval_coordination = 0.08
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_anti_submarine_patrols
        }
        add_to_variable = {
            MKN_navy_navy_submarine_detection_factor = 0.15
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_convoy_rescue
        }
        add_to_variable = {
            MKN_navy_navy_casualty_on_sink = -0.1
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_escort_reserves
        }
        add_to_variable = {
            MKN_navy_naval_defense_factor = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_coastal_fleet_exercises
        }
        add_to_variable = {
            MKN_navy_convoy_escort_efficiency = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_escort_compact
        }
        add_to_variable = {
            MKN_navy_convoy_escort_efficiency = 0.05
        }
        add_to_variable = {
            MKN_navy_screening_efficiency = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_torpedo_artels
        }
        add_to_variable = {
            MKN_navy_naval_torpedo_hit_chance_factor = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_submarine_crews
        }
        add_to_variable = {
            MKN_navy_navy_submarine_attack_factor = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_hidden_anchorages
        }
        add_to_variable = {
            MKN_navy_naval_torpedo_reveal_chance_factor = -0.08
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_naval_intelligence
        }
        add_to_variable = {
            MKN_navy_naval_detection = 0.08
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_raider_dockyard
        }
        add_to_variable = {
            MKN_navy_industrial_capacity_dockyard = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_torpedo_trials
        }
        add_to_variable = {
            MKN_navy_naval_torpedo_hit_chance_factor = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_night_sorties
        }
        add_to_variable = {
            MKN_navy_naval_torpedo_reveal_chance_factor = -0.07
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_raider_supply
        }
        add_to_variable = {
            MKN_navy_navy_fuel_consumption_factor = -0.1
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_submarine_listening
        }
        add_to_variable = {
            MKN_navy_naval_detection = 0.08
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_fast_attack_craft
        }
        add_to_variable = {
            MKN_navy_naval_speed_factor = 0.08
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_raider_radio_discipline
        }
        add_to_variable = {
            MKN_navy_naval_torpedo_reveal_chance_factor = -0.08
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_submarine_repair
        }
        add_to_variable = {
            MKN_navy_repair_speed_factor = 0.15
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_raider_weather
        }
        add_to_variable = {
            MKN_navy_naval_detection = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_raider_replacement_crews
        }
        add_to_variable = {
            MKN_navy_navy_submarine_defence_factor = 0.08
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_torpedo_ambushes
        }
        add_to_variable = {
            MKN_navy_naval_torpedo_hit_chance_factor = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_disrupt_enemy_trade
        }
        add_to_variable = {
            MKN_navy_convoy_raiding_efficiency_factor = 0.1
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_raider_escape_routes
        }
        add_to_variable = {
            MKN_navy_naval_retreat_speed = 0.15
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_raider_exercises
        }
        add_to_variable = {
            MKN_navy_navy_submarine_attack_factor = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_raider_compact
        }
        add_to_variable = {
            MKN_navy_convoy_raiding_efficiency_factor = 0.1
        }
        add_to_variable = {
            MKN_navy_navy_submarine_attack_factor = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_black_sea_flotilla
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
    if = {
        limit = {
            has_completed_focus = MKN_steppe_legions
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
    set_country_flag = MKN_services_redesign_v4
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
                            has_country_flag = MKN_industry_unified_v2
                        }
                    }
                    nww_mkn_rebuild_industry = yes
                }
                if = {
                    limit = {
                        exists = yes
                        NOT = {
                            has_country_flag = MKN_services_redesign_v4
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
                        has_country_flag = MKN_industry_unified_v2
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
                        has_country_flag = MKN_services_redesign_v4
                    }
                }
                nww_mkn_rebuild_services = yes
            }
            MKN_repair_succession_crisis = yes
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

## Предприятия и производственные организации

### `common/military_industrial_organization/organizations/nww_organizations.txt`

```pdx
MKN_kommunar_organization = {
    include = generic_mobile_tank_organization
    icon = GFX_idea_MKN_company_kommunar
    allowed = {
        original_tag = MKN
    }
    available = {
        FROM = {
            has_completed_focus = MKN_steel_horses
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
                has_completed_focus = MKN_tank_maintenance
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
                has_completed_focus = MKN_tank_maintenance
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
    }
    available = {
        FROM = {
            OR = {
                has_completed_focus = MKN_village_muster
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
                has_completed_focus = MKN_machinegun_carts
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
                has_completed_focus = MKN_machinegun_carts
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
                has_completed_focus = MKN_free_army_compact
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
    }
    available = {
        FROM = {
            OR = {
                has_completed_focus = MKN_artillery_artels
                has_completed_focus = MKN_machinegun_carts
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
                has_completed_focus = MKN_fire_tables
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
                has_completed_focus = MKN_fire_tables
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
    }
    available = {
        FROM = {
            has_completed_focus = MKN_aircraft_artels
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
                has_completed_focus = MKN_interceptor_pairs
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
                has_completed_focus = MKN_interceptor_pairs
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
    }
    available = {
        FROM = {
            has_completed_focus = MKN_attack_air_artels
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
                has_completed_focus = MKN_flying_artillery
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
                has_completed_focus = MKN_flying_artillery
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
    }
    available = {
        FROM = {
            has_completed_focus = MKN_kherson_shipyard
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
                has_completed_focus = MKN_depth_charge_school
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
                has_completed_focus = MKN_depth_charge_school
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
    }
    available = {
        FROM = {
            has_completed_focus = MKN_submarine_crews
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
                has_completed_focus = MKN_night_sorties
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
                has_completed_focus = MKN_night_sorties
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
        has_completed_focus = MKN_steel_horses
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
            has_completed_focus = MKN_artillery_artels
            has_completed_focus = MKN_machinegun_carts
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
        has_completed_focus = MKN_aircraft_artels
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
        has_completed_focus = MKN_attack_air_artels
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
        has_completed_focus = MKN_kherson_shipyard
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
        has_completed_focus = MKN_submarine_crews
    }
    research_bonus = {
        naval_equipment = 0.10
    }
    traits = {
        MKN_submarine_works_company_specialization
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

### Вспомогательный эффект `MKN_build_soviet_rail_link` (`common/scripted_effects/MKN_effects.txt`)

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

### Вспомогательный эффект `MKN_dismantle_bop` (`common/scripted_effects/MKN_effects.txt`)

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

### Вспомогательный эффект `MKN_install_tsebriy` (`common/scripted_effects/MKN_effects.txt`)

```pdx
MKN_install_tsebriy = {
    retire_ideology_leader = communism
    create_country_leader = {
        name = MKN_osyp_tsebriy
        picture = GFX_Portrait_MKN_revkom
        ideology = leninism
        traits = {
            mkn_syndicalist_organizer
        }
    }
    remove_ideas = MKN_revkom_terror
}
```

### Вспомогательный эффект `MKN_raise_communal_militias` (`common/scripted_effects/MKN_effects.txt`)

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

### Вспомогательный эффект `MKN_resolve_succession_crisis` (`common/scripted_effects/MKN_effects.txt`)

```pdx
MKN_resolve_succession_crisis = {
    set_country_flag = MKN_crisis_settled
    clr_country_flag = MKN_crisis_active
    remove_mission = MKN_civil_war_timer_mission
}
```

## Регионы, затронутые наградами / стартовая территория

Полные определения модифицированных регионов: исходный владелец, ядра, постройки, ресурсы и население. Датированные записи history не равны стартовому состоянию.

### `history/states/1082-Huliaipole.txt`

```pdx
state = {
    id = 1082
    name = STATE_1082
    manpower = 300000
    history = {
        owner = MKN
        add_core_of = MKN
        add_core_of = SOV
        add_core_of = UKR
        victory_points = {
            429
            1
        }
        buildings = {
            industrial_complex = 3
            arms_factory = 2
            infrastructure = 3
        }
    }
    provinces = {
        429
        9571
    }
    local_supplies = 0.0
    state_category = town
}
```

### `history/states/196-Kherson.txt`

```pdx
state = {
    id = 196
    name = STATE_196
    manpower = 728363
    state_category = rural
    resources = {
        chromium = 15
    }
    history = {
        owner = MKN
        add_core_of = MKN
        add_core_of = SOV
        add_core_of = UKR
        add_core_of = CRI
        victory_points = {
            721
            1
        }
        buildings = {
            infrastructure = 3
            air_base = 3
        }
    }
    provinces = {
        568
        721
        737
        767
        3573
        6771
        9712
        11715
    }
    local_supplies = 0.0
}
```

### `history/states/200-Rivne.txt`

```pdx
state = {
    id = 200
    name = STATE_200
    manpower = 994082
    state_category = town
    history = {
        owner = MKN
        add_core_of = MKN
        add_core_of = SOV
        add_core_of = UKR
        victory_points = {
            11405
            1
        }
        buildings = {
            infrastructure = 3
            air_base = 3
            11405 = {
                dam = 1
            }
        }
        1939.1.1 = {
            buildings = {
                industrial_complex = 1
            }
        }
    }
    provinces = {
        588
        3399
        3767
        6596
        9729
        11405
        11700
    }
    local_supplies = 0.0
}
```

### `history/states/225-Glukhov.txt`

```pdx
state = {
    id = 225
    name = STATE_225
    manpower = 1338280
    state_category = town
    history = {
        victory_points = {
            3520
            3
        }
        victory_points = {
            9566
            1
        }
        owner = UKR
        buildings = {
            infrastructure = 3
        }
        add_core_of = SOV
        add_core_of = UKR
    }
    provinces = {
        463
        501
        522
        3225
        3455
        3520
        6565
        9477
        9566
        11462
        11553
    }
    local_supplies = 0.0
}
```

### `history/states/226-Nikopol.txt`

```pdx
state = {
    id = 226
    name = STATE_226
    manpower = 2391047
    state_category = town
    resources = {
        oil = 4
    }
    history = {
        owner = MKN
        add_core_of = MKN
        victory_points = {
            11437
            10
        }
        victory_points = {
            11561
            1
        }
        buildings = {
            infrastructure = 3
            industrial_complex = 2
            air_base = 2
            arms_factory = 1
        }
        add_core_of = SOV
        add_core_of = UKR
    }
    provinces = {
        453
        472
        486
        6423
        9419
        9433
        9463
        9479
        11422
        11437
        11452
        11561
    }
    local_supplies = 0.0
}
```

## Локализация подсказок, духов и бонусов из определений

```json
{
  "MKN": {
    "ru": "Махновцы",
    "en": "Makhnovists"
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
  "MKN_air_development": {
    "ru": "Крылья вольной территории",
    "en": "Wings of the Free Territory"
  },
  "MKN_air_recon_factor_tt": {
    "ru": "$recon_factor_tt$",
    "en": "$recon_factor_tt$"
  },
  "MKN_air_supply_consumption_factor_tt": {
    "ru": "$supply_consumption_factor_tt$",
    "en": "$supply_consumption_factor_tt$"
  },
  "MKN_army_army_armor_attack_factor_tt": {
    "ru": "$army_armor_attack_factor_tt$",
    "en": "$army_armor_attack_factor_tt$"
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
  "MKN_army_conscription_tt": {
    "ru": "Военнообязанное население: §G+2%§!.",
    "en": "Recruitable population: §G+2%§!."
  },
  "MKN_army_development": {
    "ru": "Армия вольной территории",
    "en": "Army of the Free Territory"
  },
  "MKN_army_land_reinforce_rate_tt": {
    "ru": "$land_reinforce_rate_tt$",
    "en": "$land_reinforce_rate_tt$"
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
  "MKN_army_modifier_army_sub_unit_cavalry_speed_factor_tt": {
    "ru": "$modifier_army_sub_unit_cavalry_speed_factor_tt$",
    "en": "$modifier_army_sub_unit_cavalry_speed_factor_tt$"
  },
  "MKN_army_modifier_army_sub_unit_infantry_attack_factor_tt": {
    "ru": "Атака пехоты: $RIGHT|+=%1$",
    "en": "Infantry attack: $RIGHT|+=%1$"
  },
  "MKN_army_modifier_army_sub_unit_infantry_speed_factor_tt": {
    "ru": "Скорость пехоты: $RIGHT|+=%1$",
    "en": "Infantry speed: $RIGHT|+=%1$"
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
  "MKN_army_supply_consumption_factor_tt": {
    "ru": "$supply_consumption_factor_tt$",
    "en": "$supply_consumption_factor_tt$"
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
  "MKN_autonomous_rail_crews_idea": {
    "ru": "Самоуправляемые железнодорожные бригады",
    "en": "Autonomous Rail Crews"
  },
  "MKN_bop_abandoned": {
    "ru": "Аграрный съезд упразднил баланс сил",
    "en": "The agrarian congress abolished the balance of power"
  },
  "MKN_bop_locked": {
    "ru": "Вольные советы получили постоянные полномочия",
    "en": "The free soviets hold permanent authority"
  },
  "MKN_crisis_enabled": {
    "ru": "Действует система преемственности 1936 года",
    "en": "The 1936 succession system is active"
  },
  "MKN_crisis_legacy_settled": {
    "ru": "Сохранено прежнее политическое урегулирование",
    "en": "An earlier political settlement is preserved"
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
  "MKN_free_workshops_unlock_tt": {
    "ru": "Открывает промышленный концерн и военно-промышленную организацию «Вольные мастерские».",
    "en": "Unlocks the Free Workshops industrial concern and military industrial organization."
  },
  "MKN_industry_concern_1": {
    "ru": "Концерн «Вольная сталь»",
    "en": "Concern of Free Steel"
  },
  "MKN_industry_concern_2": {
    "ru": "Концерн «Вольная сталь»",
    "en": "Concern of Free Steel"
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
  "MKN_military_command_side": {
    "ru": "Военный штаб — Тратишов",
    "en": "Military Staff — Tratishov"
  },
  "MKN_moscow_request_pending": {
    "ru": "Предложение ожидает ответа Москвы",
    "en": "A proposal is awaiting Moscow's reply"
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
  "MKN_navy_industrial_capacity_dockyard_tt": {
    "ru": "$industrial_capacity_dockyard_tt$",
    "en": "$industrial_capacity_dockyard_tt$"
  },
  "MKN_navy_mines_sweeping_by_fleets_factor_tt": {
    "ru": "$MODIFIER_MINES_SWEEPING_BY_FLEETS_FACTOR$: $RIGHT|+=%1$",
    "en": "$MODIFIER_MINES_SWEEPING_BY_FLEETS_FACTOR$: $RIGHT|+=%1$"
  },
  "MKN_navy_naval_defense_factor_tt": {
    "ru": "$naval_defense_factor_tt$",
    "en": "$naval_defense_factor_tt$"
  },
  "MKN_navy_naval_detection_tt": {
    "ru": "$naval_detection_tt$",
    "en": "$naval_detection_tt$"
  },
  "MKN_navy_naval_ship_recovery_chance_factor_tt": {
    "ru": "$naval_ship_recovery_chance_factor_tt$",
    "en": "$naval_ship_recovery_chance_factor_tt$"
  },
  "MKN_navy_naval_torpedo_hit_chance_factor_tt": {
    "ru": "$naval_torpedo_hit_chance_factor_tt$",
    "en": "$naval_torpedo_hit_chance_factor_tt$"
  },
  "MKN_navy_naval_torpedo_reveal_chance_factor_tt": {
    "ru": "$naval_torpedo_reveal_chance_factor_tt$",
    "en": "$naval_torpedo_reveal_chance_factor_tt$"
  },
  "MKN_navy_navy_fuel_consumption_factor_tt": {
    "ru": "$MODIFIER_NAVY_FUEL_CONSUMPTION_FACTOR$: $RIGHT|-=%1$",
    "en": "$MODIFIER_NAVY_FUEL_CONSUMPTION_FACTOR$: $RIGHT|-=%1$"
  },
  "MKN_navy_navy_submarine_attack_factor_tt": {
    "ru": "$navy_submarine_attack_factor_tt$",
    "en": "$navy_submarine_attack_factor_tt$"
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
  "MKN_power_balance": {
    "ru": "Штаб и вольные советы",
    "en": "Staff and Free Soviets"
  },
  "MKN_revkom_terror": {
    "ru": "Террор ревкома",
    "en": "Revkom Terror"
  },
  "MKN_rifle_artels_organization": {
    "ru": "Гуляйпольские оружейные артели",
    "en": "Gulyai Polye Armament Artels"
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
  "MKN_rifle_concern_union_tt": {
    "ru": "§GАртель стрелкового вооружения улучшена:§! исследования пехотного вооружения +5%, производительность фабрик +3%",
    "en": "§GSmall Arms Artels improved:§! infantry weapons research +5%, factory output +3%"
  },
  "MKN_soviet_supply_agreement": {
    "ru": "Советское соглашение о снабжении",
    "en": "Soviet Supply Agreement"
  },
  "MKN_soviet_trade_accepted": {
    "ru": "Харьков принял соглашение о снабжении",
    "en": "Kharkov accepted the supply agreement"
  },
  "MKN_steel_concern_union_tt": {
    "ru": "§GКонцерн «Вольная сталь» улучшен:§! исследования промышленности +5%, скорость строительства +3%, производительность фабрик +5%",
    "en": "§GConcern of Free Steel improved:§! industry research +5%, construction speed +3%, factory output +5%"
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
  "MKN_unified_factory_energy_consumption_tt": {
    "ru": "Потребление энергии заводами: $RIGHT|-=%1$",
    "en": "Factory energy consumption: $RIGHT|-=%1$"
  },
  "MKN_unified_global_building_slots_factor_tt": {
    "ru": "Максимум предприятий в национальных регионах: +30%.",
    "en": "Maximum factories in core states: +30%."
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
  "MKN_unified_production_factory_max_efficiency_factor_tt": {
    "ru": "Предел производственной эффективности: $RIGHT|+=%1$",
    "en": "Production efficiency cap: $RIGHT|+=%1$"
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
  "MKN_unlock_strikes_tt": {
    "ru": "Открывает сети стачек в соседних странах.",
    "en": "Unlocks strike networks in neighboring countries."
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
  "mkn_ukr_frontier_concluded": {
    "ru": "Кризис на рубеже завершён",
    "en": "The frontier crisis has ended"
  },
  "mkn_ukr_pact_signed": {
    "ru": "Харьковский пакт подписан",
    "en": "The Kharkiv Pact has been signed"
  },
  "neutrality": {
    "ru": "Нейтралитет",
    "en": "Non-Aligned"
  }
}
```

## Проверяемость снимка

Генератор: `python tools/export_mkn_industrial_focuses.py`. Источником наград являются текущие скрипты, не старые проектные JSON. Хеши позволяют обнаружить устаревание после правок.

```text
8f41ba61861c3d023a4bd4b6b485d602de7bebf5819629d3b2e18e9159862ee6  common/country_leader/nww_mkn_industry_traits.txt
b3e566edfcd3ca1076c5d61335bb4781a2a849c288bb1168243a18e6bf17808a  common/dynamic_modifiers/nww_dynamic_modifiers.txt
25371b7edaff96981cfd0ed8d0f8e5c574c32184c69e30202d4f86d53a44417f  common/ideas/MKN_ideas.txt
1e61a393b99617160dc763426e39330e5ab40375589b62d545b9eabc4461ba31  common/ideas/nww_companies.txt
7864d2463029f3ec4cc3b8dbfaf4fe79d0fbc82cf192cbff249b05e4064e360d  common/military_industrial_organization/organizations/nww_organizations.txt
239fedfee7a10c0665e5d1edeb2a967fdb594c543f67d6dca94755a13393c2dd  common/national_focus/MKN.txt
3bed671cf921f30d3c07f813fdcd6e99ffaa757b402bc622161cb580fbce6fdd  common/national_focus/MKN_frontier_focuses.txt
6eafe57e9d8958db3491f61253d0560d237b7c017b8fbc4d439ce9b798b88306  common/on_actions/nww_mkn_progression.txt
63a04eff33df1fd684abc52b31df158905b0ff9033821bc7349dbb3648156d4d  common/scripted_effects/MKN_effects.txt
f48d3062f63de36a5d3ac8989646b5ed1e0f9038e9c59d089f4be3a31e5b5a56  common/scripted_effects/nww_mkn_progression.txt
b5c2cf38406ee26a8ed66ffdb00c6040173213661a819df33c938f40676a78b8  history/countries/MKN - Makhnovists.txt
39c55a7167712a40eabba5750eba273fd7423386deecbcbbd8faa53c387341e8  history/states/1082-Huliaipole.txt
91d865ee54d2caa0d25cb3933b53b6e45e2bba938d0ca338517e5638e8d191c3  history/states/196-Kherson.txt
b61eeaffba0a8e3653b6466473e0e57bf919c305b60bf456c2a58e6e90429772  history/states/200-Rivne.txt
d43dcd1f900ed3daa563276c2d07a75362d1b37e1febfb9aeb49dc1622ab6ce3  history/states/225-Glukhov.txt
6b0b1143b745a2190f3419d69b8ab10dbeca40e75c23d3c20161dca8e20804c9  history/states/226-Nikopol.txt
58b0549c4a5585e0a81e9e51b4c2b752f547b87e695eec06e0751ffc77afd2d0  localisation/english/MKN_bop_l_english.yml
e120d4b627a8155563f670904d42200dbf23fece8f0dfe2436fa28c1eda40e48  localisation/english/MKN_flags_l_english.yml
28407387457a3ef6ba18274b323085029bcc5f65ccc8932f7611dcd14f6b9fb6  localisation/english/MKN_focus_l_english.yml
48efc637da621b0e02731f75b9f0d74fa112c58c4b3712969d80cc3a31f80807  localisation/english/MKN_frontier_l_english.yml
d132a9de94be4094ff7ada71e98f1477acb5053f8c5c7139253878f635318f38  localisation/english/MKN_international_l_english.yml
5b27b4568fd0eab3547c0bb5c7bf4322dbd6ced6f0eb13d6a29d0396106a455c  localisation/english/MKN_l_english.yml
1643c863c1cd0fdccd41976b8aff200b136fba518537587f019a341bd12df4b7  localisation/english/MKN_overhaul_l_english.yml
769b325ff62e2a46191dfb0350f30dd9ac8aea18cd6a666363478a9ba1f9de69  localisation/english/MKN_parties_l_english.yml
89fad478ca6237bb406c8ae580b755d900de82f1a93eb30d811c6bf7219e3f55  localisation/english/MKN_personnel_l_english.yml
99c6a7c335115746a50bf6dda6aa7770fb11b65e2d0d4fc2148ae7a4f8633557  localisation/nww_MKN_expansion_l_english.yml
df53911e9fd8a39df6c99043ec43464d6a776a11fdbbc39b84e0839cee81fef9  localisation/nww_MKN_expansion_l_russian.yml
a5f22a19297a8cb033feb0a2634ab140f3dca8ccb85213479376733fe45f9485  localisation/nww_MKN_l_english.yml
74e00ac6087b844c8d097553f108a6f40e42f64411a5213a802e855c8d7879e7  localisation/nww_MKN_l_russian.yml
e2987f7620a518c160bb708b15d877dc4b15bd103cfe589fe8c2ca3160ab47c8  localisation/nww_country_expansion_l_english.yml
ca9b4146311e70fc407906c10a81a006bf6c4a2a18dd6ef4870cf446dc6097d6  localisation/nww_country_expansion_l_russian.yml
cf3a4bd9aba43bb684c0097f4ecff4a1506222de523323ef6859408a6f7d9ef8  localisation/russian/MKN_bop_l_russian.yml
279bb9d9be668925fd01773d7be9506eee21a3d51ce841d757b546ff3bd86e35  localisation/russian/MKN_flags_l_russian.yml
cd0edacae9f202e1d0d7aa0bcc2b43a29320a0163f70fb720fe5fd8d7f24cc27  localisation/russian/MKN_focus_l_russian.yml
33740d5d1e54bdae597217d72f7c9e138194cb22d752242624ce5ea039bf205b  localisation/russian/MKN_frontier_l_russian.yml
a43bdd62180b58db665e13f314a0262c6e4e7d25663f4ba8a4c6d02e724710f3  localisation/russian/MKN_international_l_russian.yml
1a8aa65d623905a15bd0ce44c51f1b3a7517de8444232fb14eaf4b96fd098c20  localisation/russian/MKN_l_russian.yml
b418c7f37e7bfd6179c829a2e2a8d3dd6adcfba7aad06896c41cf1bd83350c07  localisation/russian/MKN_overhaul_l_russian.yml
779612fe406278c6c7bb4ca20bd002d762f7de903309ef7672e7b962a552bdc3  localisation/russian/MKN_parties_l_russian.yml
214fc275a33104ad82fb40343d6dcd4c21d3ea8e0621e47c2df4e6510b3e06bc  localisation/russian/MKN_personnel_l_russian.yml
```
