# MKN: промышленность — пакет для анализа другой нейросетью

Этот файл самодостаточен: содержит названия, описания, награды, условия, исходные определения и связанные системы. Это снимок текущих файлов мода, а не проект новых наград.

Основная промышленность: **20 фокусов**, по 10 на взаимоисключающих путях; пять решений конгресса и девять региональных проектов. Дополнительно: **74** связанных фокусов науки, политики, предприятий и военной инфраструктуры. Всего карточек: **94**. Чисто боевые фокусы без промышленного эффекта не включены; их необходимые предки приведены отдельно.

## Контекст и правила интерпретации

- Первая мировая война не происходила. Сохранять действующие ID и лор, монарха Махно и совместимость сохранений.
- Стоимость focus.cost измеряется неделями: 5 = 35 дней, 10 = 70 дней. Несколько блоков prerequisite соединяются И; focus внутри одного блока — ИЛИ. Условия available добавляются к prerequisites. Ветви с mutually_exclusive одновременно пройти нельзя.
- Награды в if/limit и random_owned_controlled_state условны. Числа построек в обзоре — потенциальные суммы по коду, а не обещание фактической выдачи. Проверять владение, контроль, ядра, регион и строительные слоты.
- Общий постоянный экономический дух — MKN_free_industry_modifier. Развивать его через MKN_unified_*; не заменять каждую ступень отдельным духом. Военные, авиационные и морские программы имеют собственные общие духи.
- Значения ниже даны в сырых единицах движка. political_power_gain — плоский прирост в сутки; фактор 0.05 обычно означает 5 процентных пунктов. Не интерпретировать все числовые значения как проценты.
- custom_effect_tooltip/show_mio_tooltip/unlock_mio_trait_tooltip описывают интерфейс, сами по себе ничего не выдают. Реальные разблокировки предприятий находятся в available у предприятия/черты.
- Сохранять паритет Arms Against Tyranny MIO и обычных конструкторов без DLC. Не копировать огромные награды из старого мода. Проверять ресурсную/энергетическую систему установленной версии.
- Восстановление общих переменных в сохранении не должно повторно выдавать заводы, ресурсы, политическую власть или технику. Полный код восстановления включён ниже.
- Эти данные извлечены статически. Реальные сроки кампании, отображение подсказок и выдача наград требуют проверки в игре.

## Основные ветки

### Днепрострой — `MKN_dneprostroi`

10 фокусов; сумма их длительностей: 525 дней. Это сумма всей ветки, а не кратчайший путь к отдельной награде. Проекты выполняются отдельно от национальных фокусов.

Потенциальные постройки при выполнении всех внутренних условий: `arms_factory`: +6, `industrial_complex`: +3.

- Днепрострой — `MKN_dneprostroi`
- Открытые сметы Днепростроя — `MKN_dnieper_audit`
- Ресурсная база Юга — `MKN_southern_resources`
- Индустриальные гиганты степи — `MKN_steppe_industrial_giants`
- Запорожсталь — `MKN_zaporizhstal`
- Единая днепровская логистика — `MKN_dnieper_logistics_hub`
- Рабочие батальоны резерва — `MKN_worker_battalions`
- Электрификация степи — `MKN_steppe_electrification`
- Согласованные производственные циклы — `MKN_production_cycles`
- Стальная вольница — `MKN_steel_volnitsa`

### Вольные кооперативы — `MKN_free_cooperatives`

10 фокусов; сумма их длительностей: 490 дней. Это сумма всей ветки, а не кратчайший путь к отдельной награде. Проекты выполняются отдельно от национальных фокусов.

Потенциальные постройки при выполнении всех внутренних условий: `arms_factory`: +3, `industrial_complex`: +3.

- Вольные кооперативы — `MKN_free_cooperatives`
- Реестр взаимных обязательств — `MKN_artel_register`
- Степные рынки — `MKN_steppe_markets`
- Передвижные мастерские и кузницы — `MKN_mobile_workshops`
- Артели стрелкового вооружения — `MKN_rifle_concern`
- Хлебные биржи и резервы — `MKN_grain_exchanges`
- Гужевая и грузовая логистика — `MKN_freight_logistics`
- Договор о взаимозаменяемости — `MKN_workshop_standards`
- Полевые школы коммун — `MKN_field_schools`
- Хартия хозяйственной взаимопомощи — `MKN_communal_compact`

## Карточки фокусов

### Днепрострой — `MKN_dneprostroi`

Английское название: Dnieper Industrial Program. Категория: Основная промышленная ветка.

Описание RU: Коммуны поручат общему совету крупные стройки, оставив сметы открытыми делегатам. Единый план свяжет металлургию, энергетику и транспорт; путь вольных кооперативов станет недоступен.

Описание EN: Open accounts and elected delegates will oversee a common plan for heavy industry, power and transport. This choice excludes the free cooperatives.

Источник: `common/national_focus/MKN.txt:13`. Стоимость: 5 (35 дней). Координаты: x=4, y=0.

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

### Открытые сметы Днепростроя — `MKN_dnieper_audit`

Английское название: Open Accounts of the Dnieper Program. Категория: Основная промышленная ветка.

Описание RU: Инженеры ответят перед хозяйственным съездом за каждую машину и рабочую смену. Учреждаем проектное бюро и новую фабрику; делегаты выберут строительный сезон или бережливое переоснащение на один год.

Описание EN: Engineers will answer to the congress for every machine and shift. A design office and civilian factory support recovery; delegates choose a year of accelerated construction or careful investment.

Источник: `common/national_focus/MKN.txt:49`. Стоимость: 5 (35 дней). Координаты: x=4, y=1.

Предпосылки: (Днепрострой [MKN_dneprostroi]).

Непосредственные продолжения: MKN_southern_resources.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Потенциальная постройка: industrial_complex +1
- Изменение параметра: MKN_unified_industrial_capacity_factory 0.0500
- Изменение параметра: MKN_unified_production_factory_efficiency_gain_factor 0.1000
- Изменение параметра: MKN_unified_research_speed_factor 0.0500

Полное определение; включает точные награды, условия, взаимоисключения и AI:

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

### Ресурсная база Юга — `MKN_southern_resources`

Английское название: Resource Base of the South. Категория: Основная промышленная ветка.

Описание RU: Никопольский марганец и угольные промыслы войдут в общий договор поставок. Сырьё останется достоянием коммун, а заводы получат устойчивую основу для больших серий.

Описание EN: Nikopol manganese and the southern coal workings will enter a common supply agreement, providing the raw materials for large production runs.

Источник: `common/national_focus/MKN.txt:105`. Стоимость: 5 (35 дней). Координаты: x=4, y=2.

Предпосылки: (Открытые сметы Днепростроя [MKN_dnieper_audit]).

Непосредственные продолжения: MKN_steppe_industrial_giants.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Политическая власть: 50
- Потенциальный ресурс: steel +15
- Потенциальный ресурс: coal +12

Полное определение; включает точные награды, условия, взаимоисключения и AI:

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

### Индустриальные гиганты степи — `MKN_steppe_industrial_giants`

Английское название: Industrial Giants of the Steppe. Категория: Основная промышленная ветка.

Описание RU: «Коммунар», трубные мастерские и алюминиевое производство объединят заказы и инженерные кадры. Новые корпуса дадут фабрику и три военных завода, а собственный алюминий обеспечит машиностроение.

Описание EN: Kommunar, the tube works and aluminium plants pool their orders and engineers. One civilian factory, three military factories and aluminium supplies restore large-scale manufacturing.

Источник: `common/national_focus/MKN.txt:152`. Стоимость: 10 (70 дней). Координаты: x=4, y=3.

Предпосылки: (Ресурсная база Юга [MKN_southern_resources]).

Непосредственные продолжения: MKN_zaporizhstal.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Потенциальная постройка: industrial_complex +1
- Потенциальная постройка: arms_factory +3
- Потенциальный ресурс: aluminium +8
- Изменение параметра: MKN_unified_industrial_capacity_factory 0.1000
- Изменение параметра: MKN_unified_production_factory_efficiency_gain_factor 0.0500

Полное определение; включает точные награды, условия, взаимоисключения и AI:

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

### Запорожсталь — `MKN_zaporizhstal`

Английское название: Zaporizhstal. Категория: Основная промышленная ветка.

Описание RU: Две новые линии и дополнительные плавки станут основой концерна «Вольная сталь». Промышленный совет доступен всем коммунам; с Arms Against Tyranny заводы также образуют артиллерийскую MIO, развиваемую производственными циклами и финальным договором.

Описание EN: Two new production lines and additional steel establish the Free Steel concern. Its industrial council is available with or without DLC; Arms Against Tyranny also enables an artillery MIO developed through production cycles and the final compact.

Источник: `common/national_focus/MKN.txt:213`. Стоимость: 10 (70 дней). Координаты: x=4, y=4.

Предпосылки: (Индустриальные гиганты степи [MKN_steppe_industrial_giants]).

Непосредственные продолжения: MKN_worker_battalions, MKN_dnieper_logistics_hub.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Политическая власть: 50
- Потенциальная постройка: arms_factory +2
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

### Единая днепровская логистика — `MKN_dnieper_logistics_hub`

Английское название: Unified Dnieper Logistics. Категория: Основная промышленная ветка.

Описание RU: Диспетчеры сведут речные, железнодорожные и заводские расписания. На карте станут доступны три проекта: Кичкасский мост, расчистка Днепра и степные узловые станции. Каждая стройка длится 60 дней.

Описание EN: Dispatchers coordinate river, rail and factory schedules. Unlock three 60-day map projects: Kichkas Bridge, Dnieper waterways and steppe junctions.

Источник: `common/national_focus/MKN.txt:315`. Стоимость: 5 (35 дней). Координаты: x=2, y=5.

Предпосылки: (Запорожсталь [MKN_zaporizhstal]).

Непосредственные продолжения: MKN_steppe_electrification.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Политическая власть: 50
- Изменение параметра: MKN_unified_supply_consumption_factor -0.1500
- Изменение параметра: MKN_unified_army_org_regain 0.1000

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_dnieper_logistics_hub
    icon = GFX_focus_generic_railroad
    x = 2
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
        add_political_power = 50
        add_tech_bonus = {
            bonus = 0.5
            uses = 1
            category = train_tech
        }
        custom_effect_tooltip = MKN_logistics_projects_unlock_tt
        add_to_variable = {
            MKN_unified_supply_consumption_factor = -0.1500
            tooltip = MKN_unified_supply_consumption_factor_tt
        }
        add_to_variable = {
            MKN_unified_army_org_regain = 0.1000
            tooltip = MKN_unified_army_org_regain_tt
        }
    }
}
```

### Рабочие батальоны резерва — `MKN_worker_battalions`

Английское название: Workers’ Reserve Battalions. Категория: Основная промышленная ветка.

Описание RU: Выборные бригадиры и заводские инструкторы подготовят резерв без разрыва с производством. Общие сборы улучшат организацию и планирование армии и сократят подготовку новых частей.

Описание EN: Elected brigadiers and factory instructors train a reserve without severing its ties to production. Joint exercises improve organization and planning while reducing training time.

Источник: `common/national_focus/MKN.txt:283`. Стоимость: 5 (35 дней). Координаты: x=6, y=5.

Предпосылки: (Запорожсталь [MKN_zaporizhstal]).

Непосредственные продолжения: MKN_production_cycles.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_unified_army_org_factor 0.2000
- Изменение параметра: MKN_unified_training_time_army_factor -0.2000
- Изменение параметра: MKN_unified_max_planning 0.1500

Полное определение; включает точные награды, условия, взаимоисключения и AI:

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

### Электрификация степи — `MKN_steppe_electrification`

Английское название: Electrification of the Steppe. Категория: Основная промышленная ветка.

Описание RU: Общая сеть уменьшит расход энергии заводами. Открываем три проекта на 60 дней: турбины Днепрогэса, электрификацию Екатеринослава и резервные угольные линии; каждый занимает две гражданские фабрики.

Описание EN: The common grid reduces factory energy demand. Unlock three 60-day projects using two civilian factories each: Dnieper turbines, the Katerynoslav grid and reserve coal lines.

Источник: `common/national_focus/MKN.txt:349`. Стоимость: 10 (70 дней). Координаты: x=2, y=6.

Предпосылки: (Единая днепровская логистика [MKN_dnieper_logistics_hub]).

Непосредственные продолжения: MKN_production_cycles.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Политическая власть: 100
- Изменение параметра: MKN_unified_production_speed_buildings_factor 0.0500
- Изменение параметра: MKN_unified_factory_energy_consumption -0.1000

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_steppe_electrification
    icon = GFX_focus_generic_modernize_industry
    x = 2
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
        focus = MKN_dnieper_logistics_hub
    }
    completion_reward = {
        add_political_power = 100
        custom_effect_tooltip = MKN_energy_projects_unlock_tt
        add_to_variable = {
            MKN_unified_production_speed_buildings_factor = 0.0500
            tooltip = MKN_unified_production_speed_buildings_factor_tt
        }
        add_to_variable = {
            MKN_unified_factory_energy_consumption = -0.1000
            tooltip = MKN_unified_factory_energy_consumption_tt
        }
    }
}
```

### Согласованные производственные циклы — `MKN_production_cycles`

Английское название: Coordinated Production Cycles. Категория: Основная промышленная ветка.

Описание RU: После подготовки резерва и энергосети заводы примут общие допуски, длинные серии и согласованные заказы. Военный завод и повышение предела эффективности закрепят устойчивый выпуск вооружения.

Описание EN: Prepared reserves and a working grid allow common tolerances and long production runs. Another military factory and a higher efficiency cap secure sustained arms production.

Источник: `common/national_focus/MKN.txt:378`. Стоимость: 10 (70 дней). Координаты: x=4, y=7.

Предпосылки: (Электрификация степи [MKN_steppe_electrification]) И (Рабочие батальоны резерва [MKN_worker_battalions]).

Непосредственные продолжения: MKN_steel_volnitsa.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Политическая власть: 25
- Потенциальная постройка: arms_factory +1
- Изменение параметра: MKN_unified_industrial_capacity_factory 0.2000
- Изменение параметра: MKN_unified_production_factory_efficiency_gain_factor 0.0500
- Изменение параметра: MKN_unified_production_factory_max_efficiency_factor 0.1000

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_production_cycles
    icon = GFX_focus_generic_military_industry
    x = 4
    y = 7
    cost = 10
    available_if_capitulated = no
    ai_will_do = {
        factor = 2
    }
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    prerequisite = {
        focus = MKN_steppe_electrification
    }
    prerequisite = {
        focus = MKN_worker_battalions
    }
    completion_reward = {
        add_political_power = 25
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
                type = arms_factory
                level = 1
                instant_build = yes
            }
        }
        add_to_variable = {
            MKN_unified_industrial_capacity_factory = 0.2000
            tooltip = MKN_unified_industrial_capacity_factory_tt
        }
        add_to_variable = {
            MKN_unified_production_factory_efficiency_gain_factor = 0.0500
            tooltip = MKN_unified_production_factory_efficiency_gain_factor_tt
        }
        add_to_variable = {
            MKN_unified_production_factory_max_efficiency_factor = 0.1000
            tooltip = MKN_unified_production_factory_max_efficiency_factor_tt
        }
        if = {
            limit = {
                has_dlc = "Arms Against Tyranny"
            }
            mio:MKN_zaporizhstal_organization = {
                add_mio_size = 1
                unlock_mio_trait_tooltip = MKN_zaporizhstal_serial_forging
            }
        }
    }
}
```

### Стальная вольница — `MKN_steel_volnitsa`

Английское название: A Free Territory of Steel. Категория: Основная промышленная ветка.

Описание RU: Хозяйственный договор соединит промышленный совет, рабочие кассы и единую логистику. Развиваем общий хозяйственный дух и концерн «Вольная сталь», открываем фабрику и расширяем пространство для новых предприятий.

Описание EN: A common compact unites factory councils, workers’ welfare and logistics. Develop the shared economic spirit and Free Steel concern, establish a civilian factory and expand room for further industry.

Источник: `common/national_focus/MKN.txt:443`. Стоимость: 10 (70 дней). Координаты: x=4, y=8.

Предпосылки: (Согласованные производственные циклы [MKN_production_cycles]).

Непосредственные продолжения: нет.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Политическая власть: 75
- add_stability: 0.05
- Потенциальная постройка: industrial_complex +1
- Изменение параметра: MKN_unified_political_power_gain 0.1500
- Изменение параметра: MKN_unified_consumer_goods_factor -0.0500
- Изменение параметра: MKN_unified_production_speed_buildings_factor 0.1500
- Изменение параметра: MKN_unified_global_building_slots_factor 0.3000
- Изменение параметра: MKN_unified_supply_consumption_factor -0.1500
- Изменение параметра: MKN_unified_army_org_regain 0.1000

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_steel_volnitsa
    icon = GFX_focus_generic_stalinist_industry
    x = 4
    y = 8
    cost = 10
    available_if_capitulated = no
    ai_will_do = {
        factor = 2
    }
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    prerequisite = {
        focus = MKN_production_cycles
    }
    completion_reward = {
        add_political_power = 75
        add_stability = 0.05
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
        if = {
            limit = {
                has_idea = MKN_industry_concern_1
            }
            swap_ideas = {
                remove_idea = MKN_industry_concern_1
                add_idea = MKN_industry_concern_2
            }
        }
        show_ideas_tooltip = MKN_industry_concern_2
        if = {
            limit = {
                has_dlc = "Arms Against Tyranny"
            }
            mio:MKN_zaporizhstal_organization = {
                add_mio_size = 1
                add_mio_research_bonus = 0.05
            }
        }
        add_to_variable = {
            MKN_unified_political_power_gain = 0.1500
            tooltip = MKN_unified_political_power_gain_tt
        }
        add_to_variable = {
            MKN_unified_consumer_goods_factor = -0.0500
            tooltip = MKN_unified_consumer_goods_factor_tt
        }
        add_to_variable = {
            MKN_unified_production_speed_buildings_factor = 0.1500
            tooltip = MKN_unified_production_speed_buildings_factor_tt
        }
        add_to_variable = {
            MKN_unified_global_building_slots_factor = 0.3000
            tooltip = MKN_unified_global_building_slots_factor_tt
        }
        add_to_variable = {
            MKN_unified_supply_consumption_factor = -0.1500
            tooltip = MKN_unified_supply_consumption_factor_tt
        }
        add_to_variable = {
            MKN_unified_army_org_regain = 0.1000
            tooltip = MKN_unified_army_org_regain_tt
        }
    }
}
```

### Вольные кооперативы — `MKN_free_cooperatives`

Английское название: Free Cooperatives. Категория: Основная промышленная ветка.

Описание RU: Артели сохранят самостоятельность и примут взаимные обязательства по снабжению и заказам. Хозяйственный кризис ослабнет; централизованный путь Днепростроя станет недоступен.

Описание EN: Independent artels accept mutual supply and production obligations. The economic crisis eases; this choice excludes the Dnieper industrial program.

Источник: `common/national_focus/MKN.txt:520`. Стоимость: 5 (35 дней). Координаты: x=16, y=0.

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

### Реестр взаимных обязательств — `MKN_artel_register`

Английское название: Register of Mutual Obligations. Категория: Основная промышленная ветка.

Описание RU: Артели запишут свои запасы, инструменты и обещания соседям. Хозяйственный конгресс получит право оплачивать соляные промыслы, ветряки, обучение командиров, хлебную политику и взаимное страхование.

Описание EN: Artels record their stocks, tools and promises. The Economic Congress can fund salt workings, windmills, elected commanders, grain policy and mutual insurance.

Источник: `common/national_focus/MKN.txt:556`. Стоимость: 5 (35 дней). Координаты: x=16, y=1.

Предпосылки: (Вольные кооперативы [MKN_free_cooperatives]).

Непосредственные продолжения: MKN_steppe_markets.

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

### Степные рынки — `MKN_steppe_markets`

Английское название: Steppe Markets. Категория: Основная промышленная ветка.

Описание RU: Базары, монетный двор и кредитные кассы примут общий расчёт без ростовщичества. Две фабрики и устойчивый политический доход закрепят доверие к договорам между коммунами.

Описание EN: Bazaars, the mint and mutual credit funds agree on common settlement without usury. Two civilian factories and a lasting political income strengthen confidence between communes.

Источник: `common/national_focus/MKN.txt:581`. Стоимость: 5 (35 дней). Координаты: x=16, y=2.

Предпосылки: (Реестр взаимных обязательств [MKN_artel_register]).

Непосредственные продолжения: MKN_mobile_workshops.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Политическая власть: 150
- add_stability: 0.10
- Потенциальная постройка: industrial_complex +2
- Изменение параметра: MKN_unified_political_power_gain 0.2000

Полное определение; включает точные награды, условия, взаимоисключения и AI:

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

### Передвижные мастерские и кузницы — `MKN_mobile_workshops`

Английское название: Mobile Workshops and Village Smithies. Категория: Основная промышленная ветка.

Описание RU: Сельские кузни войдут в сеть ремонтных поездок и передвижных мастерских. Два военных завода, грузовики и обмен инструментом восстановят выпуск, не собирая всё хозяйство в одном уязвимом центре.

Описание EN: Village smithies join travelling repair teams. Two military factories, trucks and shared tools restore production without concentrating it in one vulnerable industrial centre.

Источник: `common/national_focus/MKN.txt:622`. Стоимость: 10 (70 дней). Координаты: x=16, y=3.

Предпосылки: (Степные рынки [MKN_steppe_markets]).

Непосредственные продолжения: MKN_rifle_concern.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Потенциальная постройка: arms_factory +2
- Изменение параметра: MKN_unified_political_power_gain 0.1000
- Изменение параметра: MKN_unified_consumer_goods_factor -0.0500
- Изменение параметра: MKN_unified_production_speed_buildings_factor 0.0500
- Изменение параметра: MKN_unified_industrial_capacity_factory 0.1000
- Изменение параметра: MKN_unified_production_factory_efficiency_gain_factor 0.1000
- Изменение параметра: MKN_unified_research_speed_factor 0.0500

Полное определение; включает точные награды, условия, взаимоисключения и AI:

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

### Артели стрелкового вооружения — `MKN_rifle_concern`

Английское название: Rifle Artels. Категория: Основная промышленная ветка.

Описание RU: Оружейные артели получат защищённую внекарточную производственную линию. С Arms Against Tyranny доступна пехотная MIO; без дополнения — оружейный конструктор. Договор о взаимозаменяемости позволит развить выбранное предприятие.

Описание EN: The rifle artels receive a protected off-map military factory. Arms Against Tyranny enables an infantry MIO; without it, a weapons designer is available. Workshop standards develop the enterprise further.

Источник: `common/national_focus/MKN.txt:687`. Стоимость: 10 (70 дней). Координаты: x=16, y=4.

Предпосылки: (Передвижные мастерские и кузницы [MKN_mobile_workshops]).

Непосредственные продолжения: MKN_grain_exchanges, MKN_freight_logistics.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_unified_industrial_capacity_factory 0.0500

Полное определение; включает точные награды, условия, взаимоисключения и AI:

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

### Хлебные биржи и резервы — `MKN_grain_exchanges`

Английское название: Grain Exchanges and Reserves. Категория: Основная промышленная ветка.

Описание RU: Фабрика в Херсоне поддержит переработку и обмен урожая. На карте открываются три проекта по 60 дней: запорожские элеваторы, херсонские зерновые терминалы и степная посевная. Политику запасов выбирает хозяйственный конгресс.

Описание EN: A Kherson factory supports processing and exchange. Unlock three 60-day map projects: Zaporizhzhia elevators, Kherson grain terminals and steppe sowing. The Economic Congress chooses stockpile policy.

Источник: `common/national_focus/MKN.txt:723`. Стоимость: 5 (35 дней). Координаты: x=14, y=5.

Предпосылки: (Артели стрелкового вооружения [MKN_rifle_concern]).

Непосредственные продолжения: MKN_workshop_standards.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Потенциальная постройка: industrial_complex +1

Полное определение; включает точные награды, условия, взаимоисключения и AI:

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

Английское название: Wagon and Truck Logistics. Категория: Основная промышленная ветка.

Описание RU: Обозные артели и ремонтные биржи распределят склады между хуторами. Договоры подвоза резко сократят расход снабжения и истощение, а резервный уголь обеспечит мастерские.

Описание EN: Freight artels and repair exchanges distribute depots among the villages. Supply agreements sharply reduce consumption and attrition while reserve coal keeps workshops running.

Источник: `common/national_focus/MKN.txt:756`. Стоимость: 5 (35 дней). Координаты: x=18, y=5.

Предпосылки: (Артели стрелкового вооружения [MKN_rifle_concern]).

Непосредственные продолжения: MKN_workshop_standards.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Потенциальный ресурс: coal +8
- Изменение параметра: MKN_unified_supply_consumption_factor -0.3000
- Изменение параметра: MKN_unified_army_org_regain 0.1500
- Изменение параметра: MKN_unified_attrition -0.0500

Полное определение; включает точные награды, условия, взаимоисключения и AI:

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

### Договор о взаимозаменяемости — `MKN_workshop_standards`

Английское название: Interchangeability Agreement. Категория: Основная промышленная ветка.

Описание RU: Общие калибры, ремонтные образцы и портфель заказов соединят самостоятельные мастерские. Дополнительный военный завод и развитие оружейного предприятия повысят выпуск и эффективность без единственного промышленного центра.

Описание EN: Common calibres, repair patterns and pooled orders unite independent workshops. Another military factory and an upgraded weapons enterprise improve output without a single industrial centre.

Источник: `common/national_focus/MKN.txt:808`. Стоимость: 10 (70 дней). Координаты: x=16, y=6.

Предпосылки: (Хлебные биржи и резервы [MKN_grain_exchanges]) И (Гужевая и грузовая логистика [MKN_freight_logistics]).

Непосредственные продолжения: MKN_field_schools.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Потенциальная постройка: arms_factory +1
- Изменение параметра: MKN_unified_industrial_capacity_factory 0.1500
- Изменение параметра: MKN_unified_production_factory_efficiency_gain_factor 0.2500
- Изменение параметра: MKN_unified_research_speed_factor 0.0500

Полное определение; включает точные награды, условия, взаимоисключения и AI:

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

### Полевые школы коммун — `MKN_field_schools`

Английское название: Commune Field Schools. Категория: Основная промышленная ветка.

Описание RU: Передвижные инструкторы и сменяемые командиры обучат самооборону связи, маскировке и совместному манёвру. Подготовка станет короче, а отряды сохранят подвижность и связь со своими коммунами.

Описание EN: Travelling instructors and recallable commanders train local defence in signals, concealment and coordinated manoeuvre. Units train faster while retaining their mobility and communal ties.

Источник: `common/national_focus/MKN.txt:886`. Стоимость: 5 (35 дней). Координаты: x=16, y=7.

Предпосылки: (Договор о взаимозаменяемости [MKN_workshop_standards]).

Непосредственные продолжения: MKN_communal_compact.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_unified_army_org_factor 0.2000
- Изменение параметра: MKN_unified_training_time_army_factor -0.2500
- Изменение параметра: MKN_unified_max_planning 0.1000
- Изменение параметра: MKN_unified_army_speed_factor 0.0500

Полное определение; включает точные награды, условия, взаимоисключения и AI:

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

### Хартия хозяйственной взаимопомощи — `MKN_communal_compact`

Английское название: Charter of Economic Mutual Aid. Категория: Основная промышленная ветка.

Описание RU: Договоры кредита, страхования и взаимного ремонта завершат восстановление хозяйства. Рассредоточенные мастерские получат постоянные −20% ущерба промышленности от бомбардировок и +20% скорости ремонта в общем хозяйственном духе.

Описание EN: Credit, insurance and repair agreements complete recovery. Dispersed workshops gain permanent −20% industrial bombing damage and +20% repair speed through the shared economic spirit.

Источник: `common/national_focus/MKN.txt:922`. Стоимость: 10 (70 дней). Координаты: x=16, y=8.

Предпосылки: (Полевые школы коммун [MKN_field_schools]).

Непосредственные продолжения: нет.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- add_stability: 0.05
- Политическая власть: 50
- Изменение параметра: MKN_unified_political_power_gain 0.1500
- Изменение параметра: MKN_unified_consumer_goods_factor -0.1000
- Изменение параметра: MKN_unified_production_speed_buildings_factor 0.0500
- Изменение параметра: MKN_unified_stability_factor 0.0500
- Изменение параметра: MKN_unified_global_building_slots_factor 0.3000
- Изменение параметра: MKN_unified_industry_air_damage_factor -0.2000
- Изменение параметра: MKN_unified_repair_speed_factor 0.2000

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_communal_compact
    icon = GFX_focus_generic_diplomatic_treaty
    x = 16
    y = 8
    cost = 10
    available_if_capitulated = no
    ai_will_do = {
        factor = 2
    }
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    prerequisite = {
        focus = MKN_field_schools
    }
    completion_reward = {
        add_stability = 0.05
        add_political_power = 50
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
        add_to_variable = {
            MKN_unified_industry_air_damage_factor = -0.2000
            tooltip = MKN_unified_industry_air_damage_factor_tt
        }
        add_to_variable = {
            MKN_unified_repair_speed_factor = 0.2000
            tooltip = MKN_unified_repair_speed_factor_tt
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
}
```

### Технические коммуны — `MKN_technical_communes`

Английское название: Technical Communes. Категория: Бонус промышленным технологиям.

Описание RU: Учёные и мастера создадут общую сеть технических школ, доступную при любой форме хозяйства.

Описание EN: Scientists and craftsmen establish a technical school network under either economic model.

Источник: `common/national_focus/MKN.txt:2571`. Стоимость: 5 (35 дней). Координаты: x=27, y=1.

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

Источник: `common/national_focus/MKN.txt:2277`. Стоимость: 5 (35 дней). Координаты: x=66, y=1.

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

### Хартии южных коммун — `MKN_southern_commune_charters`

Английское название: Charters of the Southern Communes. Категория: Изменяет общий экономический дух MKN.

Описание RU: Одесса, Николаев и Балта примут местные хартии и станут национальными областями. Согласованные склады уменьшат потребление снабжения.

Описание EN: Odesa, Mykolaiv and Balta adopt local charters and become core states. Coordinated depots reduce supply consumption.

Источник: `common/national_focus/MKN_ukraine_integration_focuses.txt:30`. Стоимость: 5 (35 дней). Координаты: x=142, y=1.

Предпосылки: (Съезд украинских коммун [MKN_ukrainian_communes_congress]).

Непосредственные продолжения: MKN_ukrainian_rail_reconstruction.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_unified_supply_consumption_factor -0.0500

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_southern_commune_charters
    icon = GFX_focus_generic_agricultural_subsidies
    x = 142
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
        192 = {
            add_core_of = ROOT
        }
        197 = {
            add_core_of = ROOT
        }
        834 = {
            add_core_of = ROOT
        }
        add_to_variable = {
            MKN_unified_supply_consumption_factor = -0.0500
            tooltip = MKN_unified_supply_consumption_factor_tt
        }
    }
    prerequisite = {
        focus = MKN_ukrainian_communes_congress
    }
}
```

### Советы Правобережья — `MKN_right_bank_councils`

Английское название: Councils of the Right Bank. Категория: Изменяет общий экономический дух MKN.

Описание RU: Советы Житомирщины, Подолии и Правобережья получат признанное представительство. Национализация четырёх областей и постоянная стабильность заменят чрезвычайное управление.

Описание EN: Councils of Zhytomyr, Podillia and the right bank gain recognized representation. Four states become cores and lasting stability replaces emergency administration.

Источник: `common/national_focus/MKN_ukraine_integration_focuses.txt:68`. Стоимость: 10 (70 дней). Координаты: x=146, y=1.

Предпосылки: (Съезд украинских коммун [MKN_ukrainian_communes_congress]).

Непосредственные продолжения: MKN_dnieper_workshop_federation.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Политическая власть: 50
- Изменение параметра: MKN_unified_stability_factor 0.0500

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_right_bank_councils
    icon = GFX_focus_generic_diplomatic_treaty
    x = 146
    y = 1
    cost = 10
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
        add_political_power = 50
        193 = {
            add_core_of = ROOT
        }
        198 = {
            add_core_of = ROOT
        }
        199 = {
            add_core_of = ROOT
        }
        201 = {
            add_core_of = ROOT
        }
        add_to_variable = {
            MKN_unified_stability_factor = 0.0500
            tooltip = MKN_unified_stability_factor_tt
        }
    }
    prerequisite = {
        focus = MKN_ukrainian_communes_congress
    }
}
```

### Мандаты северных волостей — `MKN_northern_delegates`

Английское название: Mandates of the Northern Districts. Категория: Изменяет общий экономический дух MKN.

Описание RU: Глухов и бывшая украинская область Лиски отправят своих делегатов. Местные мандаты обеспечат национализацию, добровольцев и политический доход.

Описание EN: Hlukhiv and the former Ukrainian district of Liski send delegates. Local mandates bring cores, volunteers and political income.

Источник: `common/national_focus/MKN_ukraine_integration_focuses.txt:110`. Стоимость: 5 (35 дней). Координаты: x=150, y=1.

Предпосылки: (Съезд украинских коммун [MKN_ukrainian_communes_congress]).

Непосредственные продолжения: MKN_ukrainian_rail_reconstruction.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_unified_political_power_gain 0.1000

Полное определение; включает точные награды, условия, взаимоисключения и AI:

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

### Вольный политехникум — `MKN_polytechnic_institute`

Английское название: Free Polytechnic. Категория: Бонус промышленным технологиям.

Описание RU: Инженерное образование даст артелям свои станки, измерительные приборы и специалистов.

Описание EN: Engineering education supplies the artels with machine tools, instruments and trained specialists.

Источник: `common/national_focus/MKN.txt:2586`. Стоимость: 5 (35 дней). Координаты: x=27, y=2.

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

Источник: `common/national_focus/MKN.txt:2428`. Стоимость: 5 (35 дней). Координаты: x=82, y=2.

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

### Федерация днепровских мастерских — `MKN_dnieper_workshop_federation`

Английское название: Federation of Dnieper Workshops. Категория: Строительство, ресурсы или исследовательская мощность; Изменяет общий экономический дух MKN.

Описание RU: Киев и Черкассы войдут в хозяйственную федерацию на правах национальных областей. Восстановленная оружейная линия и общий портфель заказов усилят выпуск.

Описание EN: Kyiv and Cherkasy join the economic federation as core states. A restored arms line and shared orders improve production.

Источник: `common/national_focus/MKN_ukraine_integration_focuses.txt:146`. Стоимость: 10 (70 дней). Координаты: x=146, y=2.

Предпосылки: (Советы Правобережья [MKN_right_bank_councils]).

Непосредственные продолжения: MKN_ukrainian_rail_reconstruction.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Потенциальная постройка: arms_factory +1
- Изменение параметра: MKN_unified_industrial_capacity_factory 0.0500

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_dnieper_workshop_federation
    icon = GFX_focus_generic_military_industry
    x = 146
    y = 2
    cost = 10
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
        202 = {
            add_extra_state_shared_building_slots = 1
            add_building_construction = {
                type = arms_factory
                level = 1
                instant_build = yes
            }
        }
        202 = {
            add_core_of = ROOT
        }
        203 = {
            add_core_of = ROOT
        }
        add_to_variable = {
            MKN_unified_industrial_capacity_factory = 0.0500
            tooltip = MKN_unified_industrial_capacity_factory_tt
        }
    }
    prerequisite = {
        focus = MKN_right_bank_councils
    }
}
```

### Сеть исследовательских коммун — `MKN_communal_research_network`

Английское название: Communal Research Network. Категория: Строительство, ресурсы или исследовательская мощность.

Описание RU: Объединим лаборатории в постоянную исследовательскую сеть.

Описание EN: Link local laboratories into a permanent research network.

Источник: `common/national_focus/MKN.txt:2603`. Стоимость: 5 (35 дней). Координаты: x=27, y=3.

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

Источник: `common/national_focus/MKN.txt:1058`. Стоимость: 5 (35 дней). Координаты: x=36, y=3.

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

Источник: `common/national_focus/MKN.txt:2146`. Стоимость: 5 (35 дней). Координаты: x=46, y=3.

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

Источник: `common/national_focus/MKN.txt:2468`. Стоимость: 5 (35 дней). Координаты: x=78, y=3.

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

### Восстановление украинских магистралей — `MKN_ukrainian_rail_reconstruction`

Английское название: Rebuild the Ukrainian Main Lines. Категория: Изменяет общий экономический дух MKN.

Описание RU: После согласования всех региональных хартий ремонтные артели свяжут Одессу, Киев и Глухов. Постоянные бонусы строительства и ремонта развивают общий хозяйственный дух.

Описание EN: Once regional charters are agreed, repair artels connect Odesa, Kyiv and Hlukhiv. Permanent construction and repair bonuses develop the shared economic spirit.

Источник: `common/national_focus/MKN_ukraine_integration_focuses.txt:189`. Стоимость: 10 (70 дней). Координаты: x=146, y=3.

Предпосылки: (Хартии южных коммун [MKN_southern_commune_charters]) И (Федерация днепровских мастерских [MKN_dnieper_workshop_federation]) И (Мандаты северных волостей [MKN_northern_delegates]).

Непосредственные продолжения: MKN_kyiv_scientific_exchange.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- Изменение параметра: MKN_unified_production_speed_buildings_factor 0.1000
- Изменение параметра: MKN_unified_repair_speed_factor 0.1000

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_ukrainian_rail_reconstruction
    icon = GFX_focus_generic_railroad
    x = 146
    y = 3
    cost = 10
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
        add_to_variable = {
            MKN_unified_production_speed_buildings_factor = 0.1000
            tooltip = MKN_unified_production_speed_buildings_factor_tt
        }
        add_to_variable = {
            MKN_unified_repair_speed_factor = 0.1000
            tooltip = MKN_unified_repair_speed_factor_tt
        }
    }
    prerequisite = {
        focus = MKN_southern_commune_charters
    }
    prerequisite = {
        focus = MKN_dnieper_workshop_federation
    }
    prerequisite = {
        focus = MKN_northern_delegates
    }
}
```

### Артельные авиамастерские — `MKN_workshop_airplane_artels`

Английское название: Artel Aviation Workshops. Категория: Строительство, ресурсы или исследовательская мощность.

Описание RU: Разъездные авиамастерские ремонтируют и сколачивают машины прямо под открытым небом.

Описание EN: Itinerant aviation workshops repair and assemble machines in the open air.

Источник: `common/national_focus/MKN.txt:980`. Стоимость: 5 (35 дней). Координаты: x=27, y=4.

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

Источник: `common/national_focus/MKN.txt:1076`. Стоимость: 5 (35 дней). Координаты: x=32, y=4.

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

Источник: `common/national_focus/MKN.txt:1094`. Стоимость: 5 (35 дней). Координаты: x=34, y=4.

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

Источник: `common/national_focus/MKN.txt:3244`. Стоимость: 5 (35 дней). Координаты: x=52, y=4.

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

Источник: `common/national_focus/MKN.txt:2690`. Стоимость: 5 (35 дней). Координаты: x=60, y=4.

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

Источник: `common/national_focus/MKN.txt:4348`. Стоимость: 5 (35 дней). Координаты: x=68, y=4.

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

Источник: `common/national_focus/MKN.txt:5524`. Стоимость: 5 (35 дней). Координаты: x=88, y=4.

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

### Киевский научный обмен — `MKN_kyiv_scientific_exchange`

Английское название: Kyiv Scientific Exchange. Категория: Строительство, ресурсы или исследовательская мощность; Бонус промышленным технологиям.

Описание RU: Киевские школы и лаборатории получат общие средства. Создадим дополнительный исследовательский коллектив, если слотов меньше пяти; при достигнутом пределе оплатим два промышленных исследования.

Описание EN: Kyiv schools and laboratories receive common funding. Gain a research slot if below five; otherwise fund two industrial research bonuses.

Источник: `common/national_focus/MKN_ukraine_integration_focuses.txt:228`. Стоимость: 10 (70 дней). Координаты: x=146, y=4.

Предпосылки: (Восстановление украинских магистралей [MKN_ukrainian_rail_reconstruction]).

Непосредственные продолжения: MKN_federation_of_free_councils.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- add_research_slot: 1

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_kyiv_scientific_exchange
    icon = GFX_focus_research
    x = 146
    y = 4
    cost = 10
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
        if = {
            limit = {
                amount_research_slots < 5
            }
            add_research_slot = 1
        }
        else = {
            add_tech_bonus = {
                bonus = 0.5
                uses = 2
                category = industry
            }
        }
    }
    prerequisite = {
        focus = MKN_ukrainian_rail_reconstruction
    }
}
```

### Высшая техническая школа — `MKN_advanced_research`

Английское название: Advanced Technical School. Категория: Строительство, ресурсы или исследовательская мощность.

Описание RU: Новые кафедры авиации и металлургии создадут вторую исследовательскую группу.

Описание EN: New aviation and metallurgy departments establish a second research team.

Источник: `common/national_focus/MKN.txt:2621`. Стоимость: 5 (35 дней). Координаты: x=27, y=5.

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

Источник: `common/national_focus/MKN.txt:1139`. Стоимость: 5 (35 дней). Координаты: x=34, y=5.

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

Источник: `common/national_focus/MKN.txt:3299`. Стоимость: 5 (35 дней). Координаты: x=52, y=5.

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

Источник: `common/national_focus/MKN.txt:3831`. Стоимость: 5 (35 дней). Координаты: x=64, y=5.

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

Источник: `common/national_focus/MKN.txt:4430`. Стоимость: 5 (35 дней). Координаты: x=72, y=5.

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

Источник: `common/national_focus/MKN.txt:5551`. Стоимость: 5 (35 дней). Координаты: x=84, y=5.

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

Источник: `common/national_focus/MKN.txt:6955`. Стоимость: 5 (35 дней). Координаты: x=112, y=5.

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

### Федерация вольных советов — `MKN_federation_of_free_councils`

Английское название: Federation of Free Councils. Категория: Изменяет общий экономический дух MKN.

Описание RU: Региональные договоры станут общим федеративным уставом. Стабильность, снабжение и производственная эффективность закрепят интеграцию через единый хозяйственный дух.

Описание EN: Regional compacts become a common federal charter. Stability, supply and production efficiency consolidate integration through the shared economic spirit.

Источник: `common/national_focus/MKN_ukraine_integration_focuses.txt:266`. Стоимость: 10 (70 дней). Координаты: x=146, y=5.

Предпосылки: (Киевский научный обмен [MKN_kyiv_scientific_exchange]).

Непосредственные продолжения: нет.

Обзор награды (условия и остальные эффекты полностью в коде ниже):

- add_stability: 0.05
- Изменение параметра: MKN_unified_stability_factor 0.0500
- Изменение параметра: MKN_unified_supply_consumption_factor -0.0500
- Изменение параметра: MKN_unified_production_factory_max_efficiency_factor 0.0500

Полное определение; включает точные награды, условия, взаимоисключения и AI:

```pdx
focus = {
    id = MKN_federation_of_free_councils
    icon = GFX_focus_generic_diplomatic_treaty
    x = 146
    y = 5
    cost = 10
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
        add_stability = 0.05
        add_to_variable = {
            MKN_unified_stability_factor = 0.0500
            tooltip = MKN_unified_stability_factor_tt
        }
        add_to_variable = {
            MKN_unified_supply_consumption_factor = -0.0500
            tooltip = MKN_unified_supply_consumption_factor_tt
        }
        add_to_variable = {
            MKN_unified_production_factory_max_efficiency_factor = 0.0500
            tooltip = MKN_unified_production_factory_max_efficiency_factor_tt
        }
    }
    prerequisite = {
        focus = MKN_kyiv_scientific_exchange
    }
}
```

### Полевой ремонт брони — `MKN_tank_maintenance`

Английское название: Field Armour Repair. Категория: Строительство, ресурсы или исследовательская мощность; Открывает/развивает предприятие или MIO.

Описание RU: Ремонтная база Днепра обеспечит запасные узлы и восстановление техники.

Описание EN: A Dnipro repair plant will provide replacement assemblies and equipment repairs.

Источник: `common/national_focus/MKN.txt:2848`. Стоимость: 5 (35 дней). Координаты: x=48, y=6.

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

Источник: `common/national_focus/MKN.txt:3883`. Стоимость: 5 (35 дней). Координаты: x=64, y=6.

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

Источник: `common/national_focus/MKN.txt:4501`. Стоимость: 5 (35 дней). Координаты: x=72, y=6.

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

Источник: `common/national_focus/MKN.txt:4996`. Стоимость: 5 (35 дней). Координаты: x=76, y=6.

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

Источник: `common/national_focus/MKN.txt:5610`. Стоимость: 5 (35 дней). Координаты: x=84, y=6.

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

Источник: `common/national_focus/MKN.txt:6444`. Стоимость: 5 (35 дней). Координаты: x=100, y=6.

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

Источник: `common/national_focus/MKN.txt:2639`. Стоимость: 5 (35 дней). Координаты: x=44, y=7.

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

Источник: `common/national_focus/MKN.txt:2899`. Стоимость: 5 (35 дней). Координаты: x=48, y=7.

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

Источник: `common/national_focus/MKN.txt:3916`. Стоимость: 5 (35 дней). Координаты: x=60, y=7.

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

Источник: `common/national_focus/MKN.txt:4555`. Стоимость: 5 (35 дней). Координаты: x=72, y=7.

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

Источник: `common/national_focus/MKN.txt:5068`. Стоимость: 5 (35 дней). Координаты: x=76, y=7.

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

Источник: `common/national_focus/MKN.txt:5683`. Стоимость: 5 (35 дней). Координаты: x=84, y=7.

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

Источник: `common/national_focus/MKN.txt:5722`. Стоимость: 5 (35 дней). Координаты: x=88, y=7.

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

Источник: `common/national_focus/MKN.txt:6475`. Стоимость: 5 (35 дней). Координаты: x=100, y=7.

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

Источник: `common/national_focus/MKN.txt:3180`. Стоимость: 5 (35 дней). Координаты: x=46, y=8.

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

Источник: `common/national_focus/MKN.txt:3723`. Стоимость: 5 (35 дней). Координаты: x=54, y=8.

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

Источник: `common/national_focus/MKN.txt:4264`. Стоимость: 5 (35 дней). Координаты: x=62, y=8.

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

Источник: `common/national_focus/MKN.txt:4888`. Стоимость: 5 (35 дней). Координаты: x=70, y=8.

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

Источник: `common/national_focus/MKN.txt:5422`. Стоимость: 5 (35 дней). Координаты: x=78, y=8.

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

Источник: `common/national_focus/MKN.txt:6037`. Стоимость: 5 (35 дней). Координаты: x=86, y=8.

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

Источник: `common/national_focus/MKN.txt:6829`. Стоимость: 5 (35 дней). Координаты: x=106, y=8.

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

Источник: `common/national_focus/MKN.txt:7320`. Стоимость: 5 (35 дней). Координаты: x=118, y=8.

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

Источник: `common/national_focus/MKN.txt:1535`. Стоимость: 5 (35 дней). Координаты: x=33, y=9.

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

Источник: `common/national_focus/MKN.txt:1999`. Стоимость: 5 (35 дней). Координаты: x=41, y=9.

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

Источник: `common/national_focus/MKN.txt:3987`. Стоимость: 5 (35 дней). Координаты: x=60, y=9.

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

Источник: `common/national_focus/MKN.txt:4612`. Стоимость: 5 (35 дней). Координаты: x=68, y=9.

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

Источник: `common/national_focus/MKN.txt:1583`. Стоимость: 5 (35 дней). Координаты: x=33, y=10.

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

Источник: `common/national_focus/MKN.txt:1357`. Стоимость: 5 (35 дней). Координаты: x=35, y=10.

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

Источник: `common/national_focus/MKN.txt:1739`. Стоимость: 5 (35 дней). Координаты: x=38, y=10.

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

Источник: `common/national_focus/MKN.txt:2990`. Стоимость: 5 (35 дней). Координаты: x=48, y=10.

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

Источник: `common/national_focus/MKN.txt:5224`. Стоимость: 5 (35 дней). Координаты: x=80, y=10.

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

Источник: `common/national_focus/MKN.txt:1301`. Стоимость: 5 (35 дней). Координаты: x=31, y=11.

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

Источник: `common/national_focus/MKN.txt:1417`. Стоимость: 5 (35 дней). Координаты: x=35, y=11.

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

Источник: `common/national_focus/MKN.txt:6244`. Стоимость: 5 (35 дней). Координаты: x=38, y=11.

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

Источник: `common/national_focus/MKN.txt:6217`. Стоимость: 5 (35 дней). Координаты: x=41, y=11.

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

Источник: `common/national_focus/MKN.txt:5250`. Стоимость: 5 (35 дней). Координаты: x=76, y=11.

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

Источник: `common/national_focus/MKN.txt:5884`. Стоимость: 5 (35 дней). Координаты: x=84, y=11.

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

Источник: `common/national_focus/MKN.txt:1449`. Стоимость: 5 (35 дней). Координаты: x=35, y=12.

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

Источник: `common/national_focus/MKN.txt:4808`. Стоимость: 5 (35 дней). Координаты: x=72, y=12.

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

Источник: `common/national_focus/MKN.txt:7461`. Стоимость: 5 (35 дней). Координаты: x=14, y=13.

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
            has_completed_focus = MKN_steel_volnitsa
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

Источник: `common/national_focus/MKN.txt:6178`. Стоимость: 5 (35 дней). Координаты: x=33, y=13.

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

Источник: `common/national_focus/MKN.txt:3126`. Стоимость: 5 (35 дней). Координаты: x=44, y=13.

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

Источник: `common/national_focus/MKN.txt:4205`. Стоимость: 5 (35 дней). Координаты: x=60, y=13.

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

Источник: `common/national_focus/MKN.txt:5356`. Стоимость: 5 (35 дней). Координаты: x=76, y=13.

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

### Съезд украинских коммун — `MKN_ukrainian_communes_congress`

Война закончилась, но власть над областями ещё не стала общим договором. Созовём делегатов всех бывших украинских земель и определим порядок добровольного самоуправления.

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
                            has_country_flag = MKN_industry_integration_v4
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

### `common/decisions/MKN_economic_decisions.txt`

```pdx
MKN_economic_congress_category = {
    MKN_congress_salt_artels = {
        icon = decision_generic_construction
        allowed = {
            original_tag = MKN
        }
        visible = {
            has_completed_focus = MKN_artel_register
            NOT = {
                has_country_flag = MKN_congress_salt_artels_done
            }
        }
        available = {
            has_capitulated = no
            any_owned_state = {
                is_controlled_by = ROOT
                is_core_of = ROOT
            }
        }
        cost = 30
        days_remove = 30
        days_re_enable = 0
        cancel_trigger = {
            OR = {
                has_capitulated = yes
                NOT = {
                    any_owned_state = {
                        is_controlled_by = ROOT
                        is_core_of = ROOT
                    }
                }
            }
        }
        cancel_effect = {
            add_political_power = 30
        }
        remove_effect = {
            if = {
                limit = {
                    has_capitulated = no
                    any_owned_state = {
                        is_controlled_by = ROOT
                        is_core_of = ROOT
                    }
                    NOT = {
                        has_country_flag = MKN_congress_salt_artels_done
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
                set_country_flag = MKN_congress_salt_artels_done
            }
        }
        ai_will_do = {
            factor = 1
        }
    }
    MKN_congress_recallable_commanders = {
        icon = decision_generic_construction
        allowed = {
            original_tag = MKN
        }
        visible = {
            has_completed_focus = MKN_artel_register
            NOT = {
                has_country_flag = MKN_congress_recallable_commanders_done
            }
        }
        available = {
            has_capitulated = no
        }
        cost = 0
        custom_cost_trigger = {
            NOT = {
                command_power < 25
            }
        }
        custom_cost_text = MKN_economic_25_cp
        complete_effect = {
            add_command_power = -25
            army_experience = 10
            add_timed_idea = {
                idea = MKN_congress_elected_commanders
                days = 90
            }
            set_country_flag = MKN_congress_recallable_commanders_done
        }
        ai_will_do = {
            factor = 1
        }
    }
    MKN_congress_windmills = {
        icon = decision_generic_construction
        allowed = {
            original_tag = MKN
        }
        visible = {
            has_completed_focus = MKN_artel_register
            NOT = {
                has_country_flag = MKN_congress_windmills_done
            }
        }
        available = {
            has_capitulated = no
            any_owned_state = {
                is_controlled_by = ROOT
                is_core_of = ROOT
            }
        }
        cost = 20
        days_remove = 30
        days_re_enable = 0
        cancel_trigger = {
            OR = {
                has_capitulated = yes
                NOT = {
                    any_owned_state = {
                        is_controlled_by = ROOT
                        is_core_of = ROOT
                    }
                }
            }
        }
        cancel_effect = {
            add_political_power = 20
        }
        remove_effect = {
            if = {
                limit = {
                    has_capitulated = no
                    any_owned_state = {
                        is_controlled_by = ROOT
                        is_core_of = ROOT
                    }
                    NOT = {
                        has_country_flag = MKN_congress_windmills_done
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
                add_stability = 0.05
                set_country_flag = MKN_congress_windmills_done
            }
        }
        ai_will_do = {
            factor = 1
        }
    }
    MKN_congress_harvest_policy = {
        icon = decision_generic_construction
        allowed = {
            original_tag = MKN
        }
        visible = {
            has_completed_focus = MKN_artel_register
            NOT = {
                has_country_flag = MKN_congress_harvest_policy_done
            }
        }
        available = {
            has_capitulated = no
        }
        cost = 35
        complete_effect = {
            country_event = {
                id = mkn.31
                days = 1
            }
            set_country_flag = MKN_congress_harvest_policy_done
        }
        ai_will_do = {
            factor = 1
        }
    }
    MKN_congress_workers_welfare = {
        icon = decision_generic_construction
        allowed = {
            original_tag = MKN
        }
        visible = {
            has_completed_focus = MKN_artel_register
            NOT = {
                has_country_flag = MKN_congress_workers_welfare_done
            }
        }
        available = {
            has_capitulated = no
        }
        cost = 25
        complete_effect = {
            add_stability = 0.05
            add_timed_idea = {
                idea = MKN_congress_mutual_insurance
                days = 120
            }
            set_country_flag = MKN_congress_workers_welfare_done
        }
        ai_will_do = {
            factor = 1
        }
    }
}
MKN_economic_projects_category = {
    MKN_project_kichkas_bridge = {
        icon = decision_generic_construction
        allowed = {
            original_tag = MKN
        }
        state_target = yes
        targets = {
            196
        }
        on_map_mode = map_and_decisions_view
        visible = {
            has_completed_focus = MKN_dnieper_logistics_hub
            NOT = {
                has_country_flag = MKN_project_kichkas_bridge_done
            }
        }
        target_root_trigger = {
            has_completed_focus = MKN_dnieper_logistics_hub
            NOT = {
                has_country_flag = MKN_project_kichkas_bridge_done
            }
        }
        target_trigger = {
            FROM = {
                is_owned_and_controlled_by = ROOT
                is_core_of = ROOT
            }
        }
        available = {
            FROM = {
                is_owned_and_controlled_by = ROOT
                is_core_of = ROOT
            }
            has_capitulated = no
        }
        cost = 30
        days_remove = 60
        days_re_enable = 0
        cancel_trigger = {
            OR = {
                has_capitulated = yes
                FROM = {
                    OR = {
                        NOT = {
                            is_owned_and_controlled_by = ROOT
                        }
                        NOT = {
                            is_core_of = ROOT
                        }
                    }
                }
            }
        }
        remove_effect = {
            if = {
                limit = {
                    FROM = {
                        is_owned_and_controlled_by = ROOT
                        is_core_of = ROOT
                    }
                    has_capitulated = no
                    NOT = {
                        has_country_flag = MKN_project_kichkas_bridge_done
                    }
                }
                FROM = {
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
                FROM = {
                    if = {
                        limit = {
                            anti_air_building < 5
                        }
                        add_building_construction = {
                            type = anti_air_building
                            level = 1
                            instant_build = yes
                        }
                    }
                }
                set_country_flag = MKN_project_kichkas_bridge_done
            }
        }
        cancel_effect = {
            add_political_power = 30
        }
        ai_will_do = {
            factor = 2
        }
    }
    MKN_project_dnieper_waterways = {
        icon = decision_generic_construction
        allowed = {
            original_tag = MKN
        }
        state_target = yes
        targets = {
            226
        }
        on_map_mode = map_and_decisions_view
        visible = {
            has_completed_focus = MKN_dnieper_logistics_hub
            NOT = {
                has_country_flag = MKN_project_dnieper_waterways_done
            }
        }
        target_root_trigger = {
            has_completed_focus = MKN_dnieper_logistics_hub
            NOT = {
                has_country_flag = MKN_project_dnieper_waterways_done
            }
        }
        target_trigger = {
            FROM = {
                is_owned_and_controlled_by = ROOT
                is_core_of = ROOT
            }
        }
        available = {
            FROM = {
                is_owned_and_controlled_by = ROOT
                is_core_of = ROOT
            }
            has_capitulated = no
            196 = {
                is_owned_and_controlled_by = ROOT
            }
        }
        cost = 35
        days_remove = 60
        days_re_enable = 0
        cancel_trigger = {
            OR = {
                has_capitulated = yes
                FROM = {
                    OR = {
                        NOT = {
                            is_owned_and_controlled_by = ROOT
                        }
                        NOT = {
                            is_core_of = ROOT
                        }
                    }
                }
                196 = {
                    NOT = {
                        is_owned_and_controlled_by = ROOT
                    }
                }
            }
        }
        remove_effect = {
            if = {
                limit = {
                    FROM = {
                        is_owned_and_controlled_by = ROOT
                        is_core_of = ROOT
                    }
                    has_capitulated = no
                    196 = {
                        is_owned_and_controlled_by = ROOT
                    }
                    NOT = {
                        has_country_flag = MKN_project_dnieper_waterways_done
                    }
                }
                FROM = {
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
                196 = {
                    if = {
                        limit = {
                            free_building_slots = {
                                building = naval_base
                                size > 0
                                province = 721
                            }
                        }
                        add_building_construction = {
                            type = naval_base
                            level = 1
                            province = 721
                            instant_build = yes
                        }
                    }
                }
                set_country_flag = MKN_project_dnieper_waterways_done
            }
        }
        cancel_effect = {
            add_political_power = 35
        }
        ai_will_do = {
            factor = 2
        }
    }
    MKN_project_steppe_junctions = {
        icon = decision_generic_construction
        allowed = {
            original_tag = MKN
        }
        state_target = yes
        targets = {
            1082
        }
        on_map_mode = map_and_decisions_view
        visible = {
            has_completed_focus = MKN_dnieper_logistics_hub
            NOT = {
                has_country_flag = MKN_project_steppe_junctions_done
            }
        }
        target_root_trigger = {
            has_completed_focus = MKN_dnieper_logistics_hub
            NOT = {
                has_country_flag = MKN_project_steppe_junctions_done
            }
        }
        target_trigger = {
            FROM = {
                is_owned_and_controlled_by = ROOT
                is_core_of = ROOT
            }
        }
        available = {
            FROM = {
                is_owned_and_controlled_by = ROOT
                is_core_of = ROOT
            }
            has_capitulated = no
        }
        cost = 35
        days_remove = 60
        days_re_enable = 0
        cancel_trigger = {
            OR = {
                has_capitulated = yes
                FROM = {
                    OR = {
                        NOT = {
                            is_owned_and_controlled_by = ROOT
                        }
                        NOT = {
                            is_core_of = ROOT
                        }
                    }
                }
            }
        }
        remove_effect = {
            if = {
                limit = {
                    FROM = {
                        is_owned_and_controlled_by = ROOT
                        is_core_of = ROOT
                    }
                    has_capitulated = no
                    NOT = {
                        has_country_flag = MKN_project_steppe_junctions_done
                    }
                }
                FROM = {
                    if = {
                        limit = {
                            free_building_slots = {
                                building = supply_node
                                size > 0
                                province = 429
                            }
                        }
                        add_building_construction = {
                            type = supply_node
                            level = 1
                            province = 429
                            instant_build = yes
                        }
                    }
                }
                build_railway = {
                    level = 1
                    build_only_on_allied = yes
                    start_province = 429
                    target_province = 9571
                }
                set_country_flag = MKN_project_steppe_junctions_done
            }
        }
        cancel_effect = {
            add_political_power = 35
        }
        ai_will_do = {
            factor = 2
        }
    }
    MKN_project_dnieper_turbines = {
        icon = decision_generic_construction
        allowed = {
            original_tag = MKN
        }
        state_target = yes
        targets = {
            226
        }
        on_map_mode = map_and_decisions_view
        visible = {
            has_completed_focus = MKN_steppe_electrification
            NOT = {
                has_country_flag = MKN_project_dnieper_turbines_done
            }
        }
        target_root_trigger = {
            has_completed_focus = MKN_steppe_electrification
            NOT = {
                has_country_flag = MKN_project_dnieper_turbines_done
            }
        }
        target_trigger = {
            FROM = {
                is_owned_and_controlled_by = ROOT
                is_core_of = ROOT
            }
        }
        available = {
            FROM = {
                is_owned_and_controlled_by = ROOT
                is_core_of = ROOT
            }
            has_capitulated = no
            num_of_civilian_factories_available_for_projects > 1
        }
        cost = 0
        days_remove = 60
        days_re_enable = 0
        cancel_trigger = {
            OR = {
                has_capitulated = yes
                FROM = {
                    OR = {
                        NOT = {
                            is_owned_and_controlled_by = ROOT
                        }
                        NOT = {
                            is_core_of = ROOT
                        }
                    }
                }
            }
        }
        modifier = {
            civilian_factory_use = 2
        }
        remove_effect = {
            if = {
                limit = {
                    FROM = {
                        is_owned_and_controlled_by = ROOT
                        is_core_of = ROOT
                    }
                    has_capitulated = no
                    NOT = {
                        has_country_flag = MKN_project_dnieper_turbines_done
                    }
                }
                FROM = {
                    add_extra_state_shared_building_slots = 2
                    add_building_construction = {
                        type = industrial_complex
                        level = 2
                        instant_build = yes
                    }
                }
                add_to_variable = {
                    MKN_unified_energy_gain_factor = 0.1000
                    tooltip = MKN_unified_energy_gain_factor_tt
                }
                set_country_flag = MKN_project_dnieper_turbines_done
            }
        }
        ai_will_do = {
            factor = 2
        }
    }
    MKN_project_katerynoslav_grid = {
        icon = decision_generic_construction
        allowed = {
            original_tag = MKN
        }
        state_target = yes
        targets = {
            200
        }
        on_map_mode = map_and_decisions_view
        visible = {
            has_completed_focus = MKN_steppe_electrification
            NOT = {
                has_country_flag = MKN_project_katerynoslav_grid_done
            }
        }
        target_root_trigger = {
            has_completed_focus = MKN_steppe_electrification
            NOT = {
                has_country_flag = MKN_project_katerynoslav_grid_done
            }
        }
        target_trigger = {
            FROM = {
                is_owned_and_controlled_by = ROOT
                is_core_of = ROOT
            }
        }
        available = {
            FROM = {
                is_owned_and_controlled_by = ROOT
                is_core_of = ROOT
            }
            has_capitulated = no
            num_of_civilian_factories_available_for_projects > 1
        }
        cost = 0
        days_remove = 60
        days_re_enable = 0
        cancel_trigger = {
            OR = {
                has_capitulated = yes
                FROM = {
                    OR = {
                        NOT = {
                            is_owned_and_controlled_by = ROOT
                        }
                        NOT = {
                            is_core_of = ROOT
                        }
                    }
                }
            }
        }
        modifier = {
            civilian_factory_use = 2
        }
        remove_effect = {
            if = {
                limit = {
                    FROM = {
                        is_owned_and_controlled_by = ROOT
                        is_core_of = ROOT
                    }
                    has_capitulated = no
                    NOT = {
                        has_country_flag = MKN_project_katerynoslav_grid_done
                    }
                }
                FROM = {
                    add_extra_state_shared_building_slots = 2
                    add_building_construction = {
                        type = industrial_complex
                        level = 1
                        instant_build = yes
                    }
                    add_building_construction = {
                        type = arms_factory
                        level = 1
                        instant_build = yes
                    }
                }
                set_country_flag = MKN_project_katerynoslav_grid_done
            }
        }
        ai_will_do = {
            factor = 2
        }
    }
    MKN_project_reserve_coal = {
        icon = decision_generic_construction
        allowed = {
            original_tag = MKN
        }
        state_target = yes
        targets = {
            196
        }
        on_map_mode = map_and_decisions_view
        visible = {
            has_completed_focus = MKN_steppe_electrification
            NOT = {
                has_country_flag = MKN_project_reserve_coal_done
            }
        }
        target_root_trigger = {
            has_completed_focus = MKN_steppe_electrification
            NOT = {
                has_country_flag = MKN_project_reserve_coal_done
            }
        }
        target_trigger = {
            FROM = {
                is_owned_and_controlled_by = ROOT
                is_core_of = ROOT
            }
        }
        available = {
            FROM = {
                is_owned_and_controlled_by = ROOT
                is_core_of = ROOT
            }
            has_capitulated = no
            num_of_civilian_factories_available_for_projects > 1
        }
        cost = 0
        days_remove = 60
        days_re_enable = 0
        cancel_trigger = {
            OR = {
                has_capitulated = yes
                FROM = {
                    OR = {
                        NOT = {
                            is_owned_and_controlled_by = ROOT
                        }
                        NOT = {
                            is_core_of = ROOT
                        }
                    }
                }
            }
        }
        modifier = {
            civilian_factory_use = 2
        }
        remove_effect = {
            if = {
                limit = {
                    FROM = {
                        is_owned_and_controlled_by = ROOT
                        is_core_of = ROOT
                    }
                    has_capitulated = no
                    NOT = {
                        has_country_flag = MKN_project_reserve_coal_done
                    }
                }
                FROM = {
                    add_resource = {
                        type = coal
                        amount = 12
                    }
                }
                set_country_flag = MKN_project_reserve_coal_done
            }
        }
        ai_will_do = {
            factor = 2
        }
    }
    MKN_project_zaporizhzhia_elevators = {
        icon = decision_generic_construction
        allowed = {
            original_tag = MKN
        }
        state_target = yes
        targets = {
            226
        }
        on_map_mode = map_and_decisions_view
        visible = {
            has_completed_focus = MKN_grain_exchanges
            NOT = {
                has_country_flag = MKN_project_zaporizhzhia_elevators_done
            }
        }
        target_root_trigger = {
            has_completed_focus = MKN_grain_exchanges
            NOT = {
                has_country_flag = MKN_project_zaporizhzhia_elevators_done
            }
        }
        target_trigger = {
            FROM = {
                is_owned_and_controlled_by = ROOT
                is_core_of = ROOT
            }
        }
        available = {
            FROM = {
                is_owned_and_controlled_by = ROOT
                is_core_of = ROOT
            }
            has_capitulated = no
        }
        cost = 40
        days_remove = 60
        days_re_enable = 0
        cancel_trigger = {
            OR = {
                has_capitulated = yes
                FROM = {
                    OR = {
                        NOT = {
                            is_owned_and_controlled_by = ROOT
                        }
                        NOT = {
                            is_core_of = ROOT
                        }
                    }
                }
            }
        }
        remove_effect = {
            if = {
                limit = {
                    FROM = {
                        is_owned_and_controlled_by = ROOT
                        is_core_of = ROOT
                    }
                    has_capitulated = no
                    NOT = {
                        has_country_flag = MKN_project_zaporizhzhia_elevators_done
                    }
                }
                add_stability = 0.05
                add_offsite_building = {
                    type = industrial_complex
                    level = 1
                }
                set_country_flag = MKN_project_zaporizhzhia_elevators_done
            }
        }
        cancel_effect = {
            add_political_power = 40
        }
        ai_will_do = {
            factor = 2
        }
    }
    MKN_project_kherson_terminals = {
        icon = decision_generic_construction
        allowed = {
            original_tag = MKN
        }
        state_target = yes
        targets = {
            196
        }
        on_map_mode = map_and_decisions_view
        visible = {
            has_completed_focus = MKN_grain_exchanges
            NOT = {
                has_country_flag = MKN_project_kherson_terminals_done
            }
        }
        target_root_trigger = {
            has_completed_focus = MKN_grain_exchanges
            NOT = {
                has_country_flag = MKN_project_kherson_terminals_done
            }
        }
        target_trigger = {
            FROM = {
                is_owned_and_controlled_by = ROOT
                is_core_of = ROOT
            }
        }
        available = {
            FROM = {
                is_owned_and_controlled_by = ROOT
                is_core_of = ROOT
            }
            has_capitulated = no
        }
        cost = 30
        days_remove = 60
        days_re_enable = 0
        cancel_trigger = {
            OR = {
                has_capitulated = yes
                FROM = {
                    OR = {
                        NOT = {
                            is_owned_and_controlled_by = ROOT
                        }
                        NOT = {
                            is_core_of = ROOT
                        }
                    }
                }
            }
        }
        remove_effect = {
            if = {
                limit = {
                    FROM = {
                        is_owned_and_controlled_by = ROOT
                        is_core_of = ROOT
                    }
                    has_capitulated = no
                    NOT = {
                        has_country_flag = MKN_project_kherson_terminals_done
                    }
                }
                FROM = {
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
                add_to_variable = {
                    MKN_unified_convoy_retreat_speed = 0.1000
                    tooltip = MKN_unified_convoy_retreat_speed_tt
                }
                set_country_flag = MKN_project_kherson_terminals_done
            }
        }
        cancel_effect = {
            add_political_power = 30
        }
        ai_will_do = {
            factor = 2
        }
    }
    MKN_project_steppe_sowing = {
        icon = decision_generic_construction
        allowed = {
            original_tag = MKN
        }
        state_target = yes
        targets = {
            1082
        }
        on_map_mode = map_and_decisions_view
        visible = {
            has_completed_focus = MKN_grain_exchanges
            NOT = {
                has_country_flag = MKN_project_steppe_sowing_done
            }
        }
        target_root_trigger = {
            has_completed_focus = MKN_grain_exchanges
            NOT = {
                has_country_flag = MKN_project_steppe_sowing_done
            }
        }
        target_trigger = {
            FROM = {
                is_owned_and_controlled_by = ROOT
                is_core_of = ROOT
            }
        }
        available = {
            FROM = {
                is_owned_and_controlled_by = ROOT
                is_core_of = ROOT
            }
            has_capitulated = no
        }
        cost = 40
        days_remove = 60
        days_re_enable = 0
        cancel_trigger = {
            OR = {
                has_capitulated = yes
                FROM = {
                    OR = {
                        NOT = {
                            is_owned_and_controlled_by = ROOT
                        }
                        NOT = {
                            is_core_of = ROOT
                        }
                    }
                }
            }
        }
        remove_effect = {
            if = {
                limit = {
                    FROM = {
                        is_owned_and_controlled_by = ROOT
                        is_core_of = ROOT
                    }
                    has_capitulated = no
                    NOT = {
                        has_country_flag = MKN_project_steppe_sowing_done
                    }
                }
                add_manpower = 10000
                FROM = {
                    add_extra_state_shared_building_slots = 1
                    add_building_construction = {
                        type = industrial_complex
                        level = 1
                        instant_build = yes
                    }
                }
                set_country_flag = MKN_project_steppe_sowing_done
            }
        }
        cancel_effect = {
            add_political_power = 40
        }
        ai_will_do = {
            factor = 2
        }
    }
}
```

### `common/decisions/categories/MKN_economic_categories.txt`

```pdx
MKN_economic_congress_category = {
    icon = generic_industry
    allowed = {
        original_tag = MKN
    }
    visible = {
        has_completed_focus = MKN_artel_register
    }
}
MKN_economic_projects_category = {
    icon = generic_industry
    allowed = {
        original_tag = MKN
    }
    visible = {
        OR = {
            has_completed_focus = MKN_dnieper_logistics_hub
            has_completed_focus = MKN_steppe_electrification
            has_completed_focus = MKN_grain_exchanges
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

### `common/scripted_triggers/MKN_ukraine_integration_triggers.txt`

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
MKN_can_move_capital_to_kyiv = {
    tag = MKN
    NOT = {
        UKR = {
            exists = yes
        }
    }
    has_capitulated = no
    NOT = {
        has_country_flag = MKN_capital_moved_to_kyiv
    }
    202 = {
        is_owned_and_controlled_by = MKN
        is_capital = no
    }
    has_full_control_of_state = 202
}
```

### `common/scripted_effects/MKN_ukraine_integration_effects.txt`

```pdx
MKN_observe_ukrainian_integration = {
    if = {
        limit = {
            MKN_ukraine_integration_ready = yes
            NOT = {
                has_country_flag = MKN_ukraine_integration_unlocked
            }
        }
        set_country_flag = MKN_ukraine_integration_unlocked
        mark_focus_tree_layout_dirty = yes
        country_event = {
            id = mkn_integration.1
            days = 1
        }
    }
}
```

### `common/on_actions/MKN_ukraine_integration_on_actions.txt`

```pdx
on_actions = {
    on_startup = {
        effect = {
            MKN = {
                if = {
                    limit = {
                        exists = yes
                    }
                    MKN_observe_ukrainian_integration = yes
                }
            }
        }
    }
    on_daily_MKN = {
        effect = {
            MKN_observe_ukrainian_integration = yes
        }
    }
}
```

### `events/MKN_ukraine_integration_events.txt`

```pdx
add_namespace = mkn_integration
country_event = {
    id = mkn_integration.1
    title = mkn_integration.1.t
    desc = mkn_integration.1.d
    picture = GFX_report_event_election_vote
    is_triggered_only = yes
    option = {
        name = mkn_integration.1.a
    }
}
```

### `common/decisions/MKN_ukraine_integration_decisions.txt`

```pdx
MKN_ukrainian_administration_category = {
    MKN_move_capital_to_kyiv = {
        icon = GFX_decision_SOV_place_hq
        allowed = {
            original_tag = MKN
        }
        visible = {
            tag = MKN
            NOT = {
                UKR = {
                    exists = yes
                }
            }
            NOT = {
                has_country_flag = MKN_capital_moved_to_kyiv
            }
            202 = {
                is_capital = no
            }
        }
        available = {
            MKN_can_move_capital_to_kyiv = yes
        }
        cost = 50
        fire_only_once = yes
        complete_effect = {
            if = {
                limit = {
                    MKN_can_move_capital_to_kyiv = yes
                }
                set_capital = {
                    state = 202
                    remember_old_capital = no
                }
                set_country_flag = MKN_capital_moved_to_kyiv
            }
        }
        ai_will_do = {
            factor = 2
        }
    }
}
```

### `common/decisions/categories/MKN_ukraine_integration_categories.txt`

```pdx
MKN_ukrainian_administration_category = {
    icon = generic_political_actions
    allowed = {
        original_tag = MKN
    }
    visible = {
        tag = MKN
        NOT = {
            UKR = {
                exists = yes
            }
        }
        202 = {
            is_owned_by = MKN
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
                OR = {
                    has_completed_focus = MKN_machinegun_carts
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
                    has_completed_focus = MKN_machinegun_carts
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

### `common/ideas/nww_MKN_ideas.txt`

```pdx
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
            has_completed_focus = MKN_village_muster
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
            has_completed_focus = MKN_village_muster
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

## Локализация новых хозяйственных решений, проектов и предприятий

### `localisation/MKN_economic_l_russian.yml`

```yaml
l_russian:
 MKN_southern_resources: "Ресурсная база Юга"
 MKN_southern_resources_desc: "Никопольский марганец и угольные промыслы войдут в общий договор поставок. Сырьё останется достоянием коммун, а заводы получат устойчивую основу для больших серий."
 MKN_steppe_industrial_giants: "Индустриальные гиганты степи"
 MKN_steppe_industrial_giants_desc: "«Коммунар», трубные мастерские и алюминиевое производство объединят заказы и инженерные кадры. Новые корпуса дадут фабрику и три военных завода, а собственный алюминий обеспечит машиностроение."
 MKN_dnieper_logistics_hub: "Единая днепровская логистика"
 MKN_dnieper_logistics_hub_desc: "Диспетчеры сведут речные, железнодорожные и заводские расписания. На карте станут доступны три проекта: Кичкасский мост, расчистка Днепра и степные узловые станции. Каждая стройка длится 60 дней."
 MKN_steppe_markets: "Степные рынки"
 MKN_steppe_markets_desc: "Базары, монетный двор и кредитные кассы примут общий расчёт без ростовщичества. Две фабрики и устойчивый политический доход закрепят доверие к договорам между коммунами."
 MKN_grain_exchanges: "Хлебные биржи и резервы"
 MKN_grain_exchanges_desc: "Фабрика в Херсоне поддержит переработку и обмен урожая. На карте открываются три проекта по 60 дней: запорожские элеваторы, херсонские зерновые терминалы и степная посевная. Политику запасов выбирает хозяйственный конгресс."
 MKN_freight_logistics: "Гужевая и грузовая логистика"
 MKN_freight_logistics_desc: "Обозные артели и ремонтные биржи распределят склады между хуторами. Договоры подвоза резко сократят расход снабжения и истощение, а резервный уголь обеспечит мастерские."
 MKN_economic_congress_category: "Хозяйственный конгресс"
 MKN_economic_congress_category_desc: "Артели оплачивают общие программы из собственных средств. Каждая инициатива принимается один раз; длительные стройки выдают награду по завершении."
 MKN_economic_projects_category: "Региональные хозяйственные проекты"
 MKN_economic_projects_category_desc: "Выберите проект на карте. Работы длятся 60 дней и требуют политической власти либо двух гражданских фабрик. Потеря владения или контроля отменяет стройку с возвратом PP. Завершённые проекты повторять нельзя."
 MKN_economic_25_cp: "£command_power §Y25§!"
 MKN_congress_elected_commanders: "Мандаты отзывных командиров"
 MKN_congress_elected_commanders_desc: "Обученные выборные командиры укрепляют организацию ополчения на 90 дней."
 MKN_congress_mutual_insurance: "Касса взаимного ремонта"
 MKN_congress_mutual_insurance_desc: "Коммуны страхуют инструменты и оплачивают общий ремонт в течение 120 дней."
 MKN_zaporizhstal_organization: "Концерн «Вольная сталь»"
 MKN_zaporizhstal_organization_initial: "Днепровские сталевары"
 MKN_zaporizhstal_serial_forging: "Серийная ковка орудий"
 MKN_logistics_projects_unlock_tt: "Открывает три §Y60-дневных проекта на карте§!: Кичкасский мост (196), расчистка Днепра (226; морская база в Херсоне, 196), узловые станции (1082)."
 MKN_energy_projects_unlock_tt: "Открывает три §Y60-дневных проекта§!: турбины (226), электросеть (200), угольные линии (196). Каждый временно занимает §Y2 гражданские фабрики§!."
 MKN_grain_projects_unlock_tt: "Открывает три §Y60-дневных проекта на карте§!: элеваторы (226), херсонские терминалы (196), посевная (1082)."
 MKN_economic_congress_unlock_tt: "Открывает решения §Y«Хозяйственного конгресса»§!: соляные артели, отзывные командиры, ветряки, хлебная политика и взаимное страхование."
 MKN_unified_industry_air_damage_factor_tt: "Ущерб промышленности от бомбардировок: $RIGHT|-=%1$"
 MKN_unified_repair_speed_factor_tt: "Скорость ремонта: $RIGHT|+=%1$"
 MKN_unified_energy_gain_factor_tt: "Получаемая энергия: $RIGHT|+=%1$"
 MKN_unified_convoy_retreat_speed_tt: "Скорость отступления конвоев: $RIGHT|+=%1$"
 MKN_congress_salt_artels: "Соляные артели"
 MKN_congress_salt_artels_desc: "Оплатим соляные промыслы и переработку: за 30 дней появится фабрика в принадлежащем нам и контролируемом национальном регионе."
 MKN_congress_recallable_commanders: "Отзывные командиры"
 MKN_congress_recallable_commanders_desc: "Потратим 25 командного ресурса на общие сборы: получим 10 опыта армии и +5% организации на 90 дней."
 MKN_congress_windmills: "Ветряки вольных хуторов"
 MKN_congress_windmills_desc: "За 30 дней поставим мельничное оборудование и откроем фабрику в национальном регионе; договор добавит 5% стабильности."
 MKN_congress_harvest_policy: "Хлеб для обмена и резерва"
 MKN_congress_harvest_policy_desc: "Хозяйственный съезд выберет экспортные договоры или местные запасы на один год."
 MKN_congress_workers_welfare: "Страховая касса коммун"
 MKN_congress_workers_welfare_desc: "Общая касса даст 5% стабильности и ускорит ремонт на 10% в течение 120 дней."
 MKN_project_kichkas_bridge: "Восстановление Кичкасского моста"
 MKN_project_kichkas_bridge_desc: "Две ступени инфраструктуры (до предела 5) и одна ступень ПВО в Херсоне (196). Работы длятся 60 дней."
 MKN_project_dnieper_waterways: "Расчистка речных путей Днепра"
 MKN_project_dnieper_waterways_desc: "Инфраструктура в штате 226 и морская база в прибрежном Херсоне (196, провинция 721). Для всего проекта необходимо удерживать оба региона. Работы длятся 60 дней."
 MKN_project_steppe_junctions: "Степные узловые станции"
 MKN_project_steppe_junctions_desc: "Узел снабжения в Гуляй-Поле (1082, провинция 429), если его ещё нет, и железнодорожное соединение с побережьем (9571). Работы длятся 60 дней."
 MKN_project_dnieper_turbines: "Восстановление турбин Днепрогэса"
 MKN_project_dnieper_turbines_desc: "Две фабрики в штате 226 и постоянные +10% получаемой энергии. На время работ заняты две гражданские фабрики. Работы длятся 60 дней."
 MKN_project_katerynoslav_grid: "Электрификация Екатеринослава"
 MKN_project_katerynoslav_grid_desc: "Фабрика и военный завод в штате 200. На время работ заняты две гражданские фабрики. Работы длятся 60 дней."
 MKN_project_reserve_coal: "Резервные угольные линии"
 MKN_project_reserve_coal_desc: "Дополнительные 12 единиц угля в Херсоне (196). На время работ заняты две гражданские фабрики. Работы длятся 60 дней."
 MKN_project_zaporizhzhia_elevators: "Элеваторы Запорожья"
 MKN_project_zaporizhzhia_elevators_desc: "После устройства элеваторов в штате 226: +5% стабильности и одна внекарточная гражданская фабрика от зерновой торговли. Работы длятся 60 дней."
 MKN_project_kherson_terminals: "Зерновые терминалы Херсона"
 MKN_project_kherson_terminals_desc: "Инфраструктура в Херсоне (196) и постоянные +10% скорости отступления конвоев. Работы длятся 60 дней."
 MKN_project_steppe_sowing: "Посевные кампании степи"
 MKN_project_steppe_sowing_desc: "Организация посевной в Гуляй-Поле (1082) освободит 10 000 рекрутов и даст одну фабрику. Работы длятся 60 дней."
```

### `localisation/MKN_economic_l_english.yml`

```yaml
l_english:
 MKN_southern_resources: "Resource Base of the South"
 MKN_southern_resources_desc: "Nikopol manganese and the southern coal workings will enter a common supply agreement, providing the raw materials for large production runs."
 MKN_steppe_industrial_giants: "Industrial Giants of the Steppe"
 MKN_steppe_industrial_giants_desc: "Kommunar, the tube works and aluminium plants pool their orders and engineers. One civilian factory, three military factories and aluminium supplies restore large-scale manufacturing."
 MKN_dnieper_logistics_hub: "Unified Dnieper Logistics"
 MKN_dnieper_logistics_hub_desc: "Dispatchers coordinate river, rail and factory schedules. Unlock three 60-day map projects: Kichkas Bridge, Dnieper waterways and steppe junctions."
 MKN_steppe_markets: "Steppe Markets"
 MKN_steppe_markets_desc: "Bazaars, the mint and mutual credit funds agree on common settlement without usury. Two civilian factories and a lasting political income strengthen confidence between communes."
 MKN_grain_exchanges: "Grain Exchanges and Reserves"
 MKN_grain_exchanges_desc: "A Kherson factory supports processing and exchange. Unlock three 60-day map projects: Zaporizhzhia elevators, Kherson grain terminals and steppe sowing. The Economic Congress chooses stockpile policy."
 MKN_freight_logistics: "Wagon and Truck Logistics"
 MKN_freight_logistics_desc: "Freight artels and repair exchanges distribute depots among the villages. Supply agreements sharply reduce consumption and attrition while reserve coal keeps workshops running."
 MKN_economic_congress_category: "Economic Congress"
 MKN_economic_congress_category_desc: "Artels pay for common programmes. Each initiative may be completed once; construction rewards arrive when the work ends."
 MKN_economic_projects_category: "Regional Economic Projects"
 MKN_economic_projects_category_desc: "Select a project on the map. Work takes 60 days and requires political power or two civilian factories. Losing ownership or control cancels work and refunds PP. Completed projects cannot be repeated."
 MKN_economic_25_cp: "£command_power §Y25§!"
 MKN_congress_elected_commanders: "Mandates for Recallable Commanders"
 MKN_congress_elected_commanders_desc: "Trained elected commanders improve militia organization for 90 days."
 MKN_congress_mutual_insurance: "Mutual Repair Fund"
 MKN_congress_mutual_insurance_desc: "Communes insure their tools and fund joint repairs for 120 days."
 MKN_zaporizhstal_organization: "Free Steel Concern"
 MKN_zaporizhstal_organization_initial: "Dnieper Steelworkers"
 MKN_zaporizhstal_serial_forging: "Serial Gun Forging"
 MKN_logistics_projects_unlock_tt: "Unlocks three §Y60-day map projects§!: Kichkas Bridge (196), Dnieper waterways (226; naval base in Kherson, 196), steppe junctions (1082)."
 MKN_energy_projects_unlock_tt: "Unlocks three §Y60-day projects§!: turbines (226), power grid (200), coal lines (196). Each temporarily uses §Y2 civilian factories§!."
 MKN_grain_projects_unlock_tt: "Unlocks three §Y60-day map projects§!: elevators (226), Kherson terminals (196), steppe sowing (1082)."
 MKN_economic_congress_unlock_tt: "Unlocks the §YEconomic Congress§!: salt artels, recallable commanders, windmills, grain policy and mutual insurance."
 MKN_unified_industry_air_damage_factor_tt: "Industrial bombing damage: $RIGHT|-=%1$"
 MKN_unified_repair_speed_factor_tt: "Repair speed: $RIGHT|+=%1$"
 MKN_unified_energy_gain_factor_tt: "Energy gain: $RIGHT|+=%1$"
 MKN_unified_convoy_retreat_speed_tt: "Convoy retreat speed: $RIGHT|+=%1$"
 MKN_congress_salt_artels: "Salt Artels"
 MKN_congress_salt_artels_desc: "Fund salt workings and processing: after 30 days, gain a civilian factory in an owned and controlled core state."
 MKN_congress_recallable_commanders: "Recallable Commanders"
 MKN_congress_recallable_commanders_desc: "Spend 25 command power on joint exercises: gain 10 army experience and +5% organization for 90 days."
 MKN_congress_windmills: "Windmills of the Free Farms"
 MKN_congress_windmills_desc: "Install milling equipment over 30 days, gaining a civilian factory in a core state and 5% stability."
 MKN_congress_harvest_policy: "Grain for Exchange and Reserve"
 MKN_congress_harvest_policy_desc: "The congress chooses export contracts or local reserves for one year."
 MKN_congress_workers_welfare: "Communal Mutual Insurance"
 MKN_congress_workers_welfare_desc: "A shared fund grants 5% stability and +10% repair speed for 120 days."
 MKN_project_kichkas_bridge: "Restore Kichkas Bridge"
 MKN_project_kichkas_bridge_desc: "Two infrastructure levels (up to level 5) and one anti-air level in Kherson (196). Work takes 60 days."
 MKN_project_dnieper_waterways: "Clear the Dnieper Waterways"
 MKN_project_dnieper_waterways_desc: "Infrastructure in state 226 and a naval base in coastal Kherson (196, province 721). Both states must remain owned and controlled throughout the project. Work takes 60 days."
 MKN_project_steppe_junctions: "Steppe Rail Junctions"
 MKN_project_steppe_junctions_desc: "A supply hub in Huliaipole (1082, province 429), if absent, and a rail connection to the coast (9571). Work takes 60 days."
 MKN_project_dnieper_turbines: "Restore the Dnieper Turbines"
 MKN_project_dnieper_turbines_desc: "Two civilian factories in state 226 and permanent +10% energy gain. Two civilian factories are committed during construction. Work takes 60 days."
 MKN_project_katerynoslav_grid: "Electrify Katerynoslav"
 MKN_project_katerynoslav_grid_desc: "A civilian factory and military factory in state 200. Two civilian factories are committed during construction. Work takes 60 days."
 MKN_project_reserve_coal: "Reserve Coal Lines"
 MKN_project_reserve_coal_desc: "An additional 12 coal in Kherson (196). Two civilian factories are committed during construction. Work takes 60 days."
 MKN_project_zaporizhzhia_elevators: "Zaporizhzhia Grain Elevators"
 MKN_project_zaporizhzhia_elevators_desc: "Build elevators in state 226 to gain 5% stability and one off-map civilian factory from grain trade. Work takes 60 days."
 MKN_project_kherson_terminals: "Kherson Grain Terminals"
 MKN_project_kherson_terminals_desc: "Infrastructure in Kherson (196) and permanent +10% convoy retreat speed. Work takes 60 days."
 MKN_project_steppe_sowing: "Steppe Sowing Campaigns"
 MKN_project_steppe_sowing_desc: "Organize sowing in Huliaipole (1082), freeing 10,000 manpower and establishing one civilian factory. Work takes 60 days."
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
        picture = GFX_Portrait_MKN_osyp_tsebriy
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

### `history/states/192-Odessa.txt`

```pdx
state = {
    id = 192
    name = STATE_192
    manpower = 1286238
    state_category = city
    history = {
        owner = UKR
        victory_points = {
            11670
            10
        }
        buildings = {
            infrastructure = 3
            industrial_complex = 1
            air_base = 6
            11670 = {
                naval_base = 3
                coastal_bunker = 1
            }
        }
        add_core_of = SOV
        add_core_of = UKR
        1939.1.1 = {
            buildings = {
                industrial_complex = 2
            }
        }
    }
    provinces = {
        3575
        3738
        9698
        9714
        11670
        11703
    }
    local_supplies = 6.0
}
```

### `history/states/193-Kiev.txt`

```pdx
state = {
    id = 193
    name = STATE_193
    manpower = 1373637
    state_category = city
    history = {
        victory_points = {
            3568
            3
        }
        owner = UKR
        buildings = {
            infrastructure = 3
            air_base = 8
        }
        add_core_of = SOV
        add_core_of = UKR
    }
    provinces = {
        238
        546
        3480
        3542
        3568
        3584
        6458
        6508
        6532
        6589
        9437
        9506
        11425
        11489
    }
    local_supplies = 0.0
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

### `history/states/197-Mykolaiv.txt`

```pdx
state = {
    id = 197
    name = STATE_197
    manpower = 896311
    state_category = rural
    history = {
        victory_points = {
            11683
            3
        }
        owner = UKR
        buildings = {
            infrastructure = 3
            dockyard = 1
        }
        add_core_of = SOV
        add_core_of = UKR
        1939.1.1 = {
            buildings = {
                dockyard = 2
            }
        }
    }
    provinces = {
        409
        574
        3403
        3755
        6597
        9573
        11546
        11683
    }
    local_supplies = 5.0
}
```

### `history/states/198-Vinnytsia.txt`

```pdx
state = {
    id = 198
    name = STATE_198
    manpower = 1893391
    state_category = large_town
    history = {
        victory_points = {
            476
            3
        }
        owner = UKR
        buildings = {
            infrastructure = 3
            air_base = 3
        }
        add_core_of = SOV
        add_core_of = UKR
    }
    provinces = {
        476
        6455
        6480
        9423
        9435
        9481
    }
    local_supplies = 0.0
}
```

### `history/states/199-Khmelnytskyi.txt`

```pdx
state = {
    id = 199
    name = STATE_199
    manpower = 1424022
    state_category = town
    history = {
        victory_points = {
            3457
            3
        }
        owner = UKR
        buildings = {
            infrastructure = 3
            industrial_complex = 1
            air_base = 3
        }
        add_core_of = SOV
        add_core_of = UKR
    }
    provinces = {
        462
        3430
        3457
        3511
        6429
        6509
    }
    local_supplies = 4.0
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

### `history/states/201-Zhytomyr.txt`

```pdx
state = {
    id = 201
    name = STATE_201
    manpower = 1417834
    state_category = town
    history = {
        victory_points = {
            6593
            3
        }
        owner = UKR
        buildings = {
            infrastructure = 3
            air_base = 3
        }
        add_core_of = SOV
        add_core_of = UKR
    }
    provinces = {
        441
        550
        3470
        3570
        6593
        9466
        9493
        9533
        11464
        11477
        11490
        11514
    }
    local_supplies = 7.0
}
```

### `history/states/202-Western Kiev.txt`

```pdx
state = {
    id = 202
    name = STATE_202
    manpower = 2495352
    resources = {
        oil = 8
        aluminium = 7
    }
    state_category = city
    history = {
        owner = UKR
        victory_points = {
            525
            25
        }
        buildings = {
            infrastructure = 4
            arms_factory = 2
            industrial_complex = 3
            fuel_silo = 1
            air_base = 8
        }
        add_core_of = SOV
        add_core_of = UKR
        1939.1.1 = {
            buildings = {
                arms_factory = 3
                industrial_complex = 3
            }
        }
    }
    provinces = {
        489
        504
        525
        582
        3494
        3543
        6497
        9465
        9543
        9568
        11557
    }
    local_supplies = 0.0
}
```

### `history/states/203-Cherkasy.txt`

```pdx
state = {
    id = 203
    name = STATE_203
    manpower = 2405190
    state_category = large_town
    history = {
        victory_points = {
            488
            5
        }
        owner = UKR
        buildings = {
            infrastructure = 3
            industrial_complex = 1
        }
        add_core_of = SOV
        add_core_of = UKR
    }
    provinces = {
        434
        458
        488
        3452
        3468
        6451
        6478
        9451
        9491
        11409
        11424
        11438
        11454
        11530
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

### `history/states/259-Liski.txt`

```pdx
state = {
    id = 259
    name = STATE_259
    manpower = 1442584
    state_category = rural
    history = {
        victory_points = {
            11504
            3
        }
        owner = UKR
        buildings = {
            infrastructure = 3
        }
        add_core_of = SOV
        add_core_of = UKR
    }
    provinces = {
        511
        559
        3557
        6495
        6507
        6578
        6605
        9413
        9519
        11504
    }
    local_supplies = 10.0
}
```

### `history/states/834 - Balta.txt`

```pdx
state = {
    id = 834
    name = STATE_834
    manpower = 183748
    state_category = rural
    history = {
        owner = UKR
        victory_points = {
            3757
            2
        }
        victory_points = {
            741
            1
        }
        buildings = {
            infrastructure = 2
        }
        add_core_of = SOV
        add_core_of = UKR
        add_core_of = MOL
        1939.1.1 = {
            buildings = {
                industrial_complex = 2
            }
        }
    }
    provinces = {
        741
        754
        3757
        9576
    }
    local_supplies = 6.0
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
  "MKN_economic_congress_unlock_tt": {
    "ru": "Открывает решения §Y«Хозяйственного конгресса»§!: соляные артели, отзывные командиры, ветряки, хлебная политика и взаимное страхование.",
    "en": "Unlocks the §YEconomic Congress§!: salt artels, recallable commanders, windmills, grain policy and mutual insurance."
  },
  "MKN_energy_projects_unlock_tt": {
    "ru": "Открывает три §Y60-дневных проекта§!: турбины (226), электросеть (200), угольные линии (196). Каждый временно занимает §Y2 гражданские фабрики§!.",
    "en": "Unlocks three §Y60-day projects§!: turbines (226), power grid (200), coal lines (196). Each temporarily uses §Y2 civilian factories§!."
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
  "MKN_grain_projects_unlock_tt": {
    "ru": "Открывает три §Y60-дневных проекта на карте§!: элеваторы (226), херсонские терминалы (196), посевная (1082).",
    "en": "Unlocks three §Y60-day map projects§!: elevators (226), Kherson terminals (196), steppe sowing (1082)."
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
  "MKN_logistics_projects_unlock_tt": {
    "ru": "Открывает три §Y60-дневных проекта на карте§!: Кичкасский мост (196), расчистка Днепра (226; морская база в Херсоне, 196), узловые станции (1082).",
    "en": "Unlocks three §Y60-day map projects§!: Kichkas Bridge (196), Dnieper waterways (226; naval base in Kherson, 196), steppe junctions (1082)."
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
  "MKN_soviet_supply_agreement": {
    "ru": "Советское соглашение о снабжении",
    "en": "Soviet Supply Agreement"
  },
  "MKN_soviet_trade_accepted": {
    "ru": "Харьков принял соглашение о снабжении",
    "en": "Kharkov accepted the supply agreement"
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
  "MKN_unified_industry_air_damage_factor_tt": {
    "ru": "Ущерб промышленности от бомбардировок: $RIGHT|-=%1$",
    "en": "Industrial bombing damage: $RIGHT|-=%1$"
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
  "MKN_unified_repair_speed_factor_tt": {
    "ru": "Скорость ремонта: $RIGHT|+=%1$",
    "en": "Repair speed: $RIGHT|+=%1$"
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
  "MKN_zaporizhstal_organization": {
    "ru": "Концерн «Вольная сталь»",
    "en": "Free Steel Concern"
  },
  "MKN_zaporizhstal_serial_forging": {
    "ru": "Серийная ковка орудий",
    "en": "Serial Gun Forging"
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
39e02fa676c16e1764e086e3f22a275aa46c8127f878fe17ed561e8dde631732  common/decisions/MKN_economic_decisions.txt
a3623a7987696c30fdc35e9936cce71ffcfa91bde6f12dd924c9d4e65f574857  common/decisions/MKN_ukraine_integration_decisions.txt
fca14f0fa91cee44c24ed97edf53f6ca018b2b221f055905b60a11d778330ace  common/decisions/categories/MKN_economic_categories.txt
7eb399ea1a4c2f724c9614e5e92aa4258ba38c26e340469c016867de4885a5a5  common/decisions/categories/MKN_ukraine_integration_categories.txt
bc6c0b8b25886490ef9c3cf6c47f6eea64377f842898c488953cc913352295d6  common/dynamic_modifiers/nww_dynamic_modifiers.txt
7c8f082895bc53b72830c0ee020fb65ada4a92a5ad25109cf2029c3a90cf16a6  common/ideas/MKN_economic_ideas.txt
25371b7edaff96981cfd0ed8d0f8e5c574c32184c69e30202d4f86d53a44417f  common/ideas/MKN_ideas.txt
b2fe46157438e39c7d1498a9ab5d9c39aaa0fff951af247d08638e3492ef368b  common/ideas/nww_MKN_ideas.txt
1e61a393b99617160dc763426e39330e5ab40375589b62d545b9eabc4461ba31  common/ideas/nww_companies.txt
93e8d6097a158274a8866b67ceec291bfe865ca1b70f5e01bcb15c5455fc5db8  common/military_industrial_organization/organizations/MKN_organizations.txt
fa474265f4032fdd87839fd44863d8aea5edb32ce52759d84d594d9f78f648fe  common/military_industrial_organization/organizations/nww_organizations.txt
7c2383a8b34d3a0d9379ca7b19ec12515152047c30dee5fdf4bb9478c4526fa5  common/national_focus/MKN.txt
3bed671cf921f30d3c07f813fdcd6e99ffaa757b402bc622161cb580fbce6fdd  common/national_focus/MKN_frontier_focuses.txt
814826f08a46a8f3918c09bffd69d1f8a7bd08a771c9d33a9c0ed16bf96a9a77  common/national_focus/MKN_ukraine_integration_focuses.txt
6d314a2713657a66015820f504d8430c0f6b538279e13fe5f7c6ba8a2b58aded  common/on_actions/MKN_ukraine_integration_on_actions.txt
89c201f38bf10a4667f7a8c1412b08ac1ce6e85da9846e2f3a1d12805a672c3b  common/on_actions/nww_mkn_progression.txt
1e97f095e431564a35ea7cc885ce59c024767e131412ef1bd480b89977e36145  common/scripted_effects/MKN_effects.txt
13cffd84d32871baaf7b37611b06e0d781064ee4a54c1d9804952e5229ac9db1  common/scripted_effects/MKN_ukraine_integration_effects.txt
fc1d21ed8e131cd3cd44485ba295cd93c932c0845ed9191341b9e4241c301daf  common/scripted_effects/nww_mkn_progression.txt
21176c3f503751b9a05033d0287d8d530bd56ef939125904bc3e792e7e6601d8  common/scripted_triggers/MKN_ukraine_integration_triggers.txt
8893e818324096deba4aee35b50849c7086905756418f7da44c217ba2afae4ce  events/MKN_ukraine_integration_events.txt
b5c2cf38406ee26a8ed66ffdb00c6040173213661a819df33c938f40676a78b8  history/countries/MKN - Makhnovists.txt
39c55a7167712a40eabba5750eba273fd7423386deecbcbbd8faa53c387341e8  history/states/1082-Huliaipole.txt
a3f985c3690c550e8e3a9941542dece7c72c00abd7427b7bafc648b6a97955bd  history/states/192-Odessa.txt
d93f8e527858dc95db8980bec956664ecabd57eeda9e661a2ef3da6c14ffe49a  history/states/193-Kiev.txt
91d865ee54d2caa0d25cb3933b53b6e45e2bba938d0ca338517e5638e8d191c3  history/states/196-Kherson.txt
74984c1e4f202a47d9470156d3d3ee26e5742fa0330f32c2f4acb53a89f11a06  history/states/197-Mykolaiv.txt
0ca083257897785d22ae4197d73c4e0ae7272d33e98951cdbed430051195cc65  history/states/198-Vinnytsia.txt
cc54725110514fea96473e7e18f38901af27ad553ac2640f2624ccf3c0c45f39  history/states/199-Khmelnytskyi.txt
b61eeaffba0a8e3653b6466473e0e57bf919c305b60bf456c2a58e6e90429772  history/states/200-Rivne.txt
9ab498f6a43083b59fb5e9606afbe5420c0187727150dde6523aeaac4f8b61ff  history/states/201-Zhytomyr.txt
9ed5662e3a7d68f2cea8189a58df8dfca7a6285a3e124ea636a479a95f86231b  history/states/202-Western Kiev.txt
8c0b98af00b81ff295b68e3b6ee6db65d2f1749169b5c911b59bc72454e2d5ae  history/states/203-Cherkasy.txt
d43dcd1f900ed3daa563276c2d07a75362d1b37e1febfb9aeb49dc1622ab6ce3  history/states/225-Glukhov.txt
6b0b1143b745a2190f3419d69b8ab10dbeca40e75c23d3c20161dca8e20804c9  history/states/226-Nikopol.txt
7a24333fe35fa5108849e02eafbe92d7674f6e5a810d88b6b7d7fd25feddbe4e  history/states/259-Liski.txt
d93bf73d05189e804c1191474b989f6a71a1e4e98c4966da272d24b1ff430c6c  history/states/834 - Balta.txt
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
1643c863c1cd0fdccd41976b8aff200b136fba518537587f019a341bd12df4b7  localisation/english/MKN_overhaul_l_english.yml
769b325ff62e2a46191dfb0350f30dd9ac8aea18cd6a666363478a9ba1f9de69  localisation/english/MKN_parties_l_english.yml
89fad478ca6237bb406c8ae580b755d900de82f1a93eb30d811c6bf7219e3f55  localisation/english/MKN_personnel_l_english.yml
99c6a7c335115746a50bf6dda6aa7770fb11b65e2d0d4fc2148ae7a4f8633557  localisation/nww_MKN_expansion_l_english.yml
df53911e9fd8a39df6c99043ec43464d6a776a11fdbbc39b84e0839cee81fef9  localisation/nww_MKN_expansion_l_russian.yml
6eddc70643fe91181e56aacdd65013dd96db24dcef22eebeea4b9c57c52d25a0  localisation/nww_MKN_l_english.yml
6f2171dfcb4b9ed5a81c897e14dcd59b54e5d52e4d1aa821f1db20ac839c2f92  localisation/nww_MKN_l_russian.yml
e2987f7620a518c160bb708b15d877dc4b15bd103cfe589fe8c2ca3160ab47c8  localisation/nww_country_expansion_l_english.yml
ca9b4146311e70fc407906c10a81a006bf6c4a2a18dd6ef4870cf446dc6097d6  localisation/nww_country_expansion_l_russian.yml
cf3a4bd9aba43bb684c0097f4ecff4a1506222de523323ef6859408a6f7d9ef8  localisation/russian/MKN_bop_l_russian.yml
279bb9d9be668925fd01773d7be9506eee21a3d51ce841d757b546ff3bd86e35  localisation/russian/MKN_flags_l_russian.yml
cd0edacae9f202e1d0d7aa0bcc2b43a29320a0163f70fb720fe5fd8d7f24cc27  localisation/russian/MKN_focus_l_russian.yml
dc7665abf73a5ae406a9138f31b2e97b1e5141173a8967721a1064b86985636f  localisation/russian/MKN_frontier_l_russian.yml
a43bdd62180b58db665e13f314a0262c6e4e7d25663f4ba8a4c6d02e724710f3  localisation/russian/MKN_international_l_russian.yml
1a8aa65d623905a15bd0ce44c51f1b3a7517de8444232fb14eaf4b96fd098c20  localisation/russian/MKN_l_russian.yml
b418c7f37e7bfd6179c829a2e2a8d3dd6adcfba7aad06896c41cf1bd83350c07  localisation/russian/MKN_overhaul_l_russian.yml
779612fe406278c6c7bb4ca20bd002d762f7de903309ef7672e7b962a552bdc3  localisation/russian/MKN_parties_l_russian.yml
214fc275a33104ad82fb40343d6dcd4c21d3ea8e0621e47c2df4e6510b3e06bc  localisation/russian/MKN_personnel_l_russian.yml
```
