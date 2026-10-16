# MKN: политические фокусы — пакет для другой нейросети

Снимок текущих файлов NWW Reborn на 16 октября 2026 года. Содержит названия и описания RU/EN, условия, точные награды, взаимоисключения, события, решения, баланс сил и восстановление сохранений. Документ описывает действующее содержимое и не меняет механику.

Основной политический блок: **46 фокусов**, включая общий конгресс, четыре политических пути и Чёрный интернационал. Отдельный связанный блок устройства украинских коммун: **8**. Контекст внешних предпосылок: **27**.

## Контекст для анализа

- Первая мировая война не происходила. Сохранять существующие focus/event IDs, компромисс и преемников LTB, действующий лор. Архивные и скрытые совместимые фокусы не считаются отдельными доступными путями.
- cost — недели: 5 = 35 дней, 10 = 70 дней. Несколько prerequisite-блоков соединяются И; несколько focus в одном блоке — ИЛИ. available добавляет условия; mutually_exclusive исключает другой путь.
- Условия allow_branch, bypass, отмены и продолжения фокуса приведены в полном определении. has_completed_focus в available не рисует стрелку, но остаётся игровым ограничением.
- Дата смерти Махно, кризис, дедлайн и гражданская война определяются событиями и миссией, а не суммой длительностей дерева. Событийный фокус нельзя считать обычным выбираемым узлом.
- Политические входы требуют мандата популярности и подготовительных условий; способы набора поддержки находятся в решениях. Точные пороги и затраты читать в коде, не переносить из старых описаний.
- Национальные ideology groups и их локализованные названия для MKN различаются. Проверять реальные ruling_party и party_popularity, а не только название в интерфейсе.
- Сохранять единые постоянные экономический и служебные духи; значения add_to_variable складываются с прежними ступенями. Сырые факторы 0.05 обычно означают 5 процентных пунктов; политическая власть в день — плоская величина.
- if/limit/else, DLC, поддержка партии, субъектность, контроль и согласие адресата могут ограничивать выдачу. Внешнее предложение не означает автоматического принятия. custom_effect_tooltip сам не выдаёт награду.
- Баланс сил имеет нативную шкалу от −1 до +1. Модификаторы диапазона, блокировка, удаление и восстановление BoP описаны в соответствующих определениях ниже.
- Монарх Махно и его портрет сохраняются для соответствующего контента и сохранений. Коммунистическое ограничение его военных ролей не следует переносить на монархическую роль. Событийная смена лидера после смерти имеет отдельную логику.
- Восстановление сохранений не должно повторять фабрики, смену режима, дипломатию или запуск кризисного таймера. Текущее восстановление включено ниже.
- Это статический экспорт. Окончательная проверка изменений требует новой кампании, проверки tooltip и свежего game log.

## Сводный список

| Раздел | Фокус | ID | Дней |
| --- | --- | --- | --- |
| Общее начало и преемственность | Съезд 1936 года | `MKN_congress_1936` | 35 |
| Общее начало и преемственность | Вопрос снабжения | `MKN_question_of_supply` | 35 |
| Общее начало и преемственность | Вопрос дисциплины | `MKN_question_of_discipline` | 35 |
| Общее начало и преемственность | Уход Батько | `MKN_departure_of_batko` | 35 |
| Милитаристы | Военные берут власть | `MKN_military_takes_charge` | 35 |
| Милитаристы | Арестовать демагогов | `MKN_arrest_demagogues` | 35 |
| Милитаристы | Отменить выборность командиров | `MKN_abolish_election_of_commanders` | 35 |
| Милитаристы | Милитаризовать коммуны | `MKN_militarize_communes` | 35 |
| Милитаристы | Стандартизировать мастерские | `MKN_standardize_workshops` | 35 |
| Милитаристы | Железный кулак на рельсах | `MKN_iron_fist_trains` | 35 |
| Милитаристы | Чёрный экспансионизм | `MKN_black_expansionism` | 35 |
| Милитаристы | Чёрная орда | `MKN_the_black_horde` | 35 |
| Вольные советы / синдикалисты | Торжество вольных советов | `MKN_triumph_of_free_soviets` | 35 |
| Вольные советы / синдикалисты | Пакт вольных коммун | `MKN_pact_of_free_communes` | 35 |
| Вольные советы / синдикалисты | Упразднить генеральный штаб | `MKN_abolish_general_staff` | 35 |
| Вольные советы / синдикалисты | Оружие народу | `MKN_arms_to_the_people` | 35 |
| Вольные советы / синдикалисты | Пропаганда действием | `MKN_propaganda_by_deed` | 35 |
| Вольные советы / синдикалисты | Самоуправляемые железнодорожные бригады | `MKN_autonomous_rail_crews` | 35 |
| Вольные советы / синдикалисты | Маяк безгосударственности | `MKN_beacon_of_statelessness` | 35 |
| Аграрии | Крестьянские делегаты | `MKN_peasant_delegates` | 35 |
| Аграрии | Зерновой ультиматум | `MKN_grain_ultimatum` | 35 |
| Аграрии | Разорвать связи с городом | `MKN_sever_urban_ties` | 35 |
| Аграрии | Каждый хутор — крепость | `MKN_every_farm_a_fortress` | 35 |
| Аграрии | Степные снайперы | `MKN_steppe_snipers` | 35 |
| Аграрии | Железнодорожные диверсии | `MKN_railway_sabotage` | 35 |
| Аграрии | Кавалерийская засада | `MKN_cavalry_ambush` | 35 |
| Аграрии | Неприступная житница | `MKN_impregnable_granary` | 35 |
| Ревком / коммунисты | Чрезвычайный ревком | `MKN_emergency_revkom` | 35 |
| Ревком / коммунисты | Устранить непримиримых | `MKN_purge_irreconcilables` | 35 |
| Ревком / коммунисты | Посольство в Харьков | `MKN_embassy_to_kharkov` | 35 |
| Ревком / коммунисты | Объединить стальные магистрали | `MKN_integrate_steel_lines` | 35 |
| Ревком / коммунисты | Красные военные специалисты | `MKN_red_military_specialists` | 35 |
| Ревком / коммунисты | Тракторы за зерно | `MKN_tractors_for_grain` | 35 |
| Ревком / коммунисты | Антиимпериалистический фронт | `MKN_anti_imperialist_front` | 35 |
| Ревком / коммунисты | Роковой пленум | `MKN_the_fatal_plenum` | 35 |
| Общий Чёрный интернационал и внешняя политика | Чёрный интернационал | `MKN_black_international` | 35 |
| Общий Чёрный интернационал и внешняя политика | Делегаты за рубежом | `MKN_foreign_delegates` | 35 |
| Общий Чёрный интернационал и внешняя политика | Возрождение Набата на рубежах | `MKN_nabat_abroad` | 35 |
| Общий Чёрный интернационал и внешняя политика | Коридоры мастерских | `MKN_workers_corridors` | 70 |
| Общий Чёрный интернационал и внешняя политика | Агитация в ЛитБеле | `MKN_agitation_in_litbel` | 35 |
| Общий Чёрный интернационал и внешняя политика | Защита галицких крестьян | `MKN_galician_peasants` | 35 |
| Общий Чёрный интернационал и внешняя политика | Коммуны взаимной защиты | `MKN_consular_communes` | 35 |
| Общий Чёрный интернационал и внешняя политика | Спонсирование подполья | `MKN_fund_the_underground` | 70 |
| Общий Чёрный интернационал и внешняя политика | Гарантии солидарности | `MKN_solidarity_guarantees` | 70 |
| Общий Чёрный интернационал и внешняя политика | Конгресс вольных народов | `MKN_congress_of_free_peoples` | 35 |
| Общий Чёрный интернационал и внешняя политика | Глобальный синдикалистский пакт | `MKN_global_syndicalist_pact` | 70 |
| Связанное послевоенное устройство украинских коммун | Съезд украинских коммун | `MKN_ukrainian_communes_congress` | 35 |
| Связанное послевоенное устройство украинских коммун | Хартии южных коммун | `MKN_southern_commune_charters` | 35 |
| Связанное послевоенное устройство украинских коммун | Советы Правобережья | `MKN_right_bank_councils` | 70 |
| Связанное послевоенное устройство украинских коммун | Мандаты северных волостей | `MKN_northern_delegates` | 35 |
| Связанное послевоенное устройство украинских коммун | Федерация днепровских мастерских | `MKN_dnieper_workshop_federation` | 70 |
| Связанное послевоенное устройство украинских коммун | Восстановление украинских магистралей | `MKN_ukrainian_rail_reconstruction` | 70 |
| Связанное послевоенное устройство украинских коммун | Киевский научный обмен | `MKN_kyiv_scientific_exchange` | 70 |
| Связанное послевоенное устройство украинских коммун | Федерация вольных советов | `MKN_federation_of_free_councils` | 70 |
| Контекст внешних предпосылок | Днепрострой | `MKN_dneprostroi` | 35 |
| Контекст внешних предпосылок | Вольные кооперативы | `MKN_free_cooperatives` | 35 |
| Контекст внешних предпосылок | Штаб степных армий | `MKN_steppe_general_staff` | 70 |
| Контекст внешних предпосылок | Открытые сметы Днепростроя | `MKN_dnieper_audit` | 35 |
| Контекст внешних предпосылок | Реестр взаимных обязательств | `MKN_artel_register` | 35 |
| Контекст внешних предпосылок | Ресурсная база Юга | `MKN_southern_resources` | 35 |
| Контекст внешних предпосылок | Степные рынки | `MKN_steppe_markets` | 35 |
| Контекст внешних предпосылок | Индустриальные гиганты степи | `MKN_steppe_industrial_giants` | 70 |
| Контекст внешних предпосылок | Передвижные мастерские и кузницы | `MKN_mobile_workshops` | 70 |
| Контекст внешних предпосылок | Запорожсталь | `MKN_zaporizhstal` | 70 |
| Контекст внешних предпосылок | Артели стрелкового вооружения | `MKN_rifle_concern` | 70 |
| Контекст внешних предпосылок | Единая днепровская логистика | `MKN_dnieper_logistics_hub` | 35 |
| Контекст внешних предпосылок | Рабочие батальоны резерва | `MKN_worker_battalions` | 35 |
| Контекст внешних предпосылок | Хлебные биржи и резервы | `MKN_grain_exchanges` | 35 |
| Контекст внешних предпосылок | Гужевая и грузовая логистика | `MKN_freight_logistics` | 35 |
| Контекст внешних предпосылок | Электрификация степи | `MKN_steppe_electrification` | 70 |
| Контекст внешних предпосылок | Договор о взаимозаменяемости | `MKN_workshop_standards` | 70 |
| Контекст внешних предпосылок | Согласованные производственные циклы | `MKN_production_cycles` | 70 |
| Контекст внешних предпосылок | Полевые школы коммун | `MKN_field_schools` | 35 |
| Контекст внешних предпосылок | Стальная вольница | `MKN_steel_volnitsa` | 70 |
| Контекст внешних предпосылок | Хартия хозяйственной взаимопомощи | `MKN_communal_compact` | 70 |
| Контекст внешних предпосылок | Вольные мастерские Екатеринослава и Гуляйполя | `MKN_free_workshops_focus` | 35 |
| Контекст внешних предпосылок | Технические коммуны | `MKN_technical_communes` | 35 |
| Контекст внешних предпосылок | Вольный политехникум | `MKN_polytechnic_institute` | 35 |
| Контекст внешних предпосылок | Сеть исследовательских коммун | `MKN_communal_research_network` | 35 |
| Контекст внешних предпосылок | Артельные авиамастерские | `MKN_workshop_airplane_artels` | 35 |
| Контекст внешних предпосылок | Сеть вольных институтов | `MKN_free_science_network` | 70 |

## Общее начало и преемственность — 4 фокусов

### Съезд 1936 года — `MKN_congress_1936`

EN: The Congress of 1936.

Описание RU: В зале пахнет мокрыми шинелями и типографской краской. Махно ещё способен заставить его замолчать одним взглядом, но никто не верит, что это будет длиться вечно. Дадим делегатам мандат и вынесем спор штаба Тратишова с советами Волина на съезд.

Описание EN: The hall smells of wet greatcoats and printer’s ink. Makhno can still silence it with a glance, but no one believes that he can do so forever. Give the delegates a mandate and bring the struggle between Tratishov’s staff and Volin’s soviets into the open.

Источник: `common/national_focus/MKN.txt:5777`. Стоимость: 5 (35 дней). Координаты: x=86, y=0.

Предпосылки: нет нарисованной предпосылки; см. available.

Взаимоисключения: нет.

Прямые продолжения: MKN_departure_of_batko, MKN_question_of_supply, MKN_question_of_discipline.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- `add_political_power`: 100

Полное определение:

```pdx
focus = {
    id = MKN_congress_1936
    icon = GFX_focus_generic_support_the_left_right
    y = 0
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
    x = 86
}
```

### Вопрос снабжения — `MKN_question_of_supply`

EN: The Question of Supply.

Описание RU: Винтовку не накормишь резолюцией. Коммуны проверят запасы зерна, боеприпасов и железнодорожные поставки; вольные советы усилят влияние на общее военное дело.

Описание EN: A rifle cannot eat a resolution. Let the communes audit grain, ammunition and rail deliveries; the free soviets gain influence over the common war effort.

Источник: `common/national_focus/MKN.txt:5817`. Стоимость: 5 (35 дней). Координаты: x=84, y=1.

Предпосылки: (Съезд 1936 года [MKN_congress_1936]).

Взаимоисключения: нет.

Прямые продолжения: нет.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- `add_power_balance_value`: id = MKN_power_balance; value = 0.15; tooltip_side = MKN_free_soviets_side
- `add_political_power`: 50

Полное определение:

```pdx
focus = {
    id = MKN_question_of_supply
    icon = GFX_focus_generic_railroad
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
    x = 84
}
```

### Вопрос дисциплины — `MKN_question_of_discipline`

EN: The Question of Discipline.

Описание RU: Приказы умирают на пути из зала съезда в окопы. Штаб согласует движение колонн и работу складов, даже если делегаты назовут это первым камнем нового государства.

Описание EN: Orders die between the congress hall and the trenches. Let the staff coordinate marching columns and reserve depots, even if the delegates call that the first stone of a new state.

Источник: `common/national_focus/MKN.txt:5845`. Стоимость: 5 (35 дней). Координаты: x=88, y=1.

Предпосылки: (Съезд 1936 года [MKN_congress_1936]).

Взаимоисключения: нет.

Прямые продолжения: нет.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- `add_power_balance_value`: id = MKN_power_balance; value = -0.15; tooltip_side = MKN_military_command_side
- `add_political_power`: 50

Полное определение:

```pdx
focus = {
    id = MKN_question_of_discipline
    icon = GFX_focus_generic_army_doctrines_2
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
    x = 88
}
```

### Уход Батько — `MKN_departure_of_batko`

EN: The Departure of the Batko.

Описание RU: Этот фокус завершается событием смерти Махно. Его гроб закрывает эпоху, но не спор. У нас 180 дней на решение вопроса о преемственности, прежде чем степь расколется на вооружённые лагеря.

Описание EN: This focus is completed by Makhno’s death event. His coffin closes an age, not an argument. There are 180 days to settle the succession before the steppe splits into armed camps.

Источник: `common/national_focus/MKN.txt:5801`. Стоимость: 5 (35 дней). Координаты: x=86, y=2.

Предпосылки: (Съезд 1936 года [MKN_congress_1936]).

Взаимоисключения: нет.

Прямые продолжения: MKN_military_takes_charge, MKN_triumph_of_free_soviets, MKN_black_international, MKN_peasant_delegates, MKN_emergency_revkom.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- Вызываемые эффекты и полная награда приведены ниже.

Полное определение:

```pdx
focus = {
    id = MKN_departure_of_batko
    prerequisite = {
        focus = MKN_congress_1936
    }
    y = 2
    icon = GFX_focus_MKN_departure_of_batko
    available = {
        always = no
    }
    completion_reward = {

    }
    cost = 5
    x = 86
}
```

## Милитаристы — 8 фокусов

### Военные берут власть — `MKN_military_takes_charge`

EN: The Military Takes Charge.

Описание RU: Тратишов расстилает железнодорожную карту на столе съезда. Революции нужно единое оперативное командование. При поддержке не менее 40% населения и подготовленном съезде правящей программой станет анархо-милитаризм.

Описание EN: Tratishov spreads a railway map over the congress table. The revolution needs a single operational command. With at least 40% public support and a prepared congress, anarcho-militarism becomes the ruling program.

Источник: `common/national_focus/MKN.txt:5873`. Стоимость: 5 (35 дней). Координаты: x=78, y=3.

Предпосылки: (Уход Батько [MKN_departure_of_batko]).

Взаимоисключения: MKN_triumph_of_free_soviets, MKN_peasant_delegates, MKN_emergency_revkom.

Прямые продолжения: MKN_arrest_demagogues.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- `set_politics`: ruling_party = fascism; elections_allowed = no
- `add_stability`: -0.05
- `add_power_balance_value`: id = MKN_power_balance; value = -0.35; tooltip_side = MKN_military_command_side

Полное определение:

```pdx
focus = {
    id = MKN_military_takes_charge
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
    x = 78
}
```

### Арестовать демагогов — `MKN_arrest_demagogues`

EN: Arrest the Demagogues.

Описание RU: Штаб опечатывает фракционные типографии и задерживает организаторов соперничающих командований. Жестокое урегулирование останавливает 180-дневный отсчёт до гражданской войны.

Описание EN: The staff seals the faction presses and detains those organizing rival commands. A brutal settlement ends the 180-day countdown to civil war.

Источник: `common/national_focus/MKN.txt:5929`. Стоимость: 5 (35 дней). Координаты: x=78, y=4.

Предпосылки: (Военные берут власть [MKN_military_takes_charge]).

Взаимоисключения: нет.

Прямые продолжения: MKN_abolish_election_of_commanders.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- `add_stability`: 0.10
- `add_political_power`: 50

Полное определение:

```pdx
focus = {
    id = MKN_arrest_demagogues
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
    x = 78
}
```

### Отменить выборность командиров — `MKN_abolish_election_of_commanders`

EN: Abolish the Election of Commanders.

Описание RU: Бой не может ждать голосования об отзыве. Упраздним баланс сил и закрепим власть военных в существующей армейской организации: постоянный штаб улучшит планирование и сплочённость.

Описание EN: A battle cannot wait for a recall vote. End the balance of power and fold military authority into our existing army organization: stronger planning and cohesion under a permanent staff.

Источник: `common/national_focus/MKN.txt:5958`. Стоимость: 5 (35 дней). Координаты: x=78, y=5.

Предпосылки: (Арестовать демагогов [MKN_arrest_demagogues]).

Взаимоисключения: нет.

Прямые продолжения: MKN_militarize_communes.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- Параметр `MKN_army_planning_speed`: 0.1
- Параметр `MKN_army_army_org_factor`: 0.1

Полное определение:

```pdx
focus = {
    id = MKN_abolish_election_of_commanders
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
    x = 78
}
```

### Милитаризовать коммуны — `MKN_militarize_communes`

EN: Militarize the Communes.

Описание RU: Каждая коммуна будет держать призывной список рядом с зерновой книгой. Расширим набор, заплатив за это новым ударом по доверию общин.

Описание EN: Every commune must keep a muster roll beside its grain ledger. Broaden recruitment, at the price of another wound to communal confidence.

Источник: `common/national_focus/MKN.txt:5990`. Стоимость: 5 (35 дней). Координаты: x=78, y=6.

Предпосылки: (Отменить выборность командиров [MKN_abolish_election_of_commanders]).

Взаимоисключения: нет.

Прямые продолжения: MKN_standardize_workshops.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- Параметр `MKN_army_conscription`: 0.02
- Параметр `MKN_unified_stability_factor`: -0.05

Полное определение:

```pdx
focus = {
    id = MKN_militarize_communes
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
    x = 78
}
```

### Стандартизировать мастерские — `MKN_standardize_workshops`

EN: Standardize the Workshops.

Описание RU: Дюжина несовместимых затворов — дюжина способов проиграть бой. Общие калибры и согласованные заказы повысят выпуск и эффективность производства в артелях.

Описание EN: A dozen incompatible breech blocks are a dozen ways to lose a battle. Give the artels common gauges and coordinated orders to raise output and production efficiency.

Источник: `common/national_focus/MKN.txt:6021`. Стоимость: 5 (35 дней). Координаты: x=78, y=7.

Предпосылки: (Милитаризовать коммуны [MKN_militarize_communes]).

Взаимоисключения: нет.

Прямые продолжения: MKN_iron_fist_trains.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- Параметр `MKN_unified_industrial_capacity_factory`: 0.15
- Параметр `MKN_unified_production_factory_efficiency_gain_factor`: 0.1

Полное определение:

```pdx
focus = {
    id = MKN_standardize_workshops
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
    x = 78
}
```

### Железный кулак на рельсах — `MKN_iron_fist_trains`

EN: The Iron Fist on Rails.

Описание RU: Бронепоезда понесут волю штаба за горизонт. Сохраним культ железных дорог, ускорим изучение поездов и уменьшим потребности армии в снабжении.

Описание EN: Armored trains shall carry the staff’s will beyond the horizon. Preserve the railway cult, accelerate train research and reduce the army’s supply burden.

Источник: `common/national_focus/MKN.txt:6052`. Стоимость: 5 (35 дней). Координаты: x=78, y=8.

Предпосылки: (Стандартизировать мастерские [MKN_standardize_workshops]).

Взаимоисключения: нет.

Прямые продолжения: MKN_black_expansionism.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- `add_ideas`: MKN_cult_of_railways
- `add_tech_bonus`: bonus = 0.5; uses = 1; category = train_tech
- Параметр `MKN_army_supply_consumption_factor`: -0.05

Полное определение:

```pdx
focus = {
    id = MKN_iron_fist_trains
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
    x = 78
}
```

### Чёрный экспансионизм — `MKN_black_expansionism`

EN: Black Expansionism.

Описание RU: Граница, проведённая канцелярией, не священна. Откроем пограничные столкновения с ЛитБелом и советскими республиками там, где наши территории действительно соприкасаются.

Описание EN: A frontier drawn by a chancery is no sacred boundary. Unlock controlled border clashes with LitBel and the Soviet Republics wherever our territories actually meet.

Источник: `common/national_focus/MKN.txt:6092`. Стоимость: 5 (35 дней). Координаты: x=78, y=9.

Предпосылки: (Железный кулак на рельсах [MKN_iron_fist_trains]).

Взаимоисключения: нет.

Прямые продолжения: MKN_the_black_horde.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- `add_war_support`: 0.05

Полное определение:

```pdx
focus = {
    id = MKN_black_expansionism
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
    x = 78
}
```

### Чёрная орда — `MKN_the_black_horde`

EN: The Black Horde.

Описание RU: Под чёрным знаменем поднимаются штыки. Армия получит 25% к атаке и 30% к прорыву; независимые соседи вне нашего альянса станут целями аннексии. Штаб обещает свободу в конце каждого похода.

Описание EN: Bayonets rise beneath the black banner. The army gains 25% attack and 30% breakthrough; sovereign neighbors outside our faction become targets for annexation. The staff promises freedom at the end of every march.

Источник: `common/national_focus/MKN.txt:6117`. Стоимость: 5 (35 дней). Координаты: x=78, y=10.

Предпосылки: (Чёрный экспансионизм [MKN_black_expansionism]).

Взаимоисключения: нет.

Прямые продолжения: нет.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- Параметр `MKN_army_army_attack_factor`: 0.25
- Параметр `MKN_army_breakthrough_factor`: 0.3
- `create_wargoal`: type = annex_everything; target = PREV

Полное определение:

```pdx
focus = {
    id = MKN_the_black_horde
    icon = GFX_focus_MKN_the_black_horde
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
    x = 78
}
```

## Вольные советы / синдикалисты — 7 фокусов

### Торжество вольных советов — `MKN_triumph_of_free_soviets`

EN: The Triumph of the Free Soviets.

Описание RU: Волин спрашивает делегатов, кто дал штабу право править. При подготовленном съезде и поддержке не менее 40% анархо-коммунизм станет правящей программой местных советов с отзывными делегатами.

Описание EN: Volin asks the delegates who gave a staff the right to govern. With a prepared congress and at least 40% support, anarcho-communism becomes the ruling program of recallable local councils.

Источник: `common/national_focus/MKN.txt:6168`. Стоимость: 5 (35 дней). Координаты: x=84, y=3.

Предпосылки: (Уход Батько [MKN_departure_of_batko]).

Взаимоисключения: MKN_military_takes_charge, MKN_peasant_delegates, MKN_emergency_revkom.

Прямые продолжения: MKN_pact_of_free_communes.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- `set_politics`: ruling_party = democratic; elections_allowed = no
- `add_stability`: -0.05
- `add_power_balance_value`: id = MKN_power_balance; value = 0.35; tooltip_side = MKN_free_soviets_side

Полное определение:

```pdx
focus = {
    id = MKN_triumph_of_free_soviets
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
    x = 84
}
```

### Пакт вольных коммун — `MKN_pact_of_free_communes`

EN: The Pact of Free Communes.

Описание RU: Коммуны обязуются разрешать споры без создания соперничающих армий. Ратификация остановит отсчёт до гражданской войны и восстановит доверие к коллективному управлению.

Описание EN: The communes sign a common obligation to settle disputes without rival armies. Ratification stops the civil-war countdown and restores confidence in collective rule.

Источник: `common/national_focus/MKN.txt:6221`. Стоимость: 5 (35 дней). Координаты: x=84, y=4.

Предпосылки: (Торжество вольных советов [MKN_triumph_of_free_soviets]).

Взаимоисключения: нет.

Прямые продолжения: MKN_abolish_general_staff.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- `add_stability`: 0.10
- `add_political_power`: 50

Полное определение:

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
```

### Упразднить генеральный штаб — `MKN_abolish_general_staff`

EN: Abolish the General Staff.

Описание RU: Штаб станет техническим бюро, подотчётным коммунам. Закрепим полный контроль советов на шкале баланса сил и улучшим взаимодействие местных боевых отрядов.

Описание EN: The staff becomes a technical bureau answerable to the communes. Lock the balance at complete soviet control and improve coordination between local fighting detachments.

Источник: `common/national_focus/MKN.txt:6247`. Стоимость: 5 (35 дней). Координаты: x=84, y=5.

Предпосылки: (Пакт вольных коммун [MKN_pact_of_free_communes]).

Взаимоисключения: нет.

Прямые продолжения: MKN_arms_to_the_people.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- `set_country_flag`: MKN_bop_locked
- Параметр `MKN_army_land_reinforce_rate`: 0.05

Полное определение:

```pdx
focus = {
    id = MKN_abolish_general_staff
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
    x = 84
}
```

### Оружие народу — `MKN_arms_to_the_people`

EN: Arms to the People.

Описание RU: Выдадим винтовки из общих складов и сформируем три оснащённых отряда коммунальной гвардии. Расширенная система набора сделает каждое село ответственным за свою оборону.

Описание EN: Issue rifles from the common depots and form three equipped commune guards. A broader recruitment system makes each village responsible for its own defense.

Источник: `common/national_focus/MKN.txt:6286`. Стоимость: 5 (35 дней). Координаты: x=84, y=6.

Предпосылки: (Упразднить генеральный штаб [MKN_abolish_general_staff]).

Взаимоисключения: нет.

Прямые продолжения: MKN_propaganda_by_deed.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- Параметр `MKN_army_conscription`: 0.02

Полное определение:

```pdx
focus = {
    id = MKN_arms_to_the_people
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
    x = 84
}
```

### Пропаганда действием — `MKN_propaganda_by_deed`

EN: Propaganda by Deed.

Описание RU: Погасшая печь говорит громче манифеста. Откроем сети стачек в соседних странах; их правительства должны будут переждать остановку производства или заплатить за её подавление.

Описание EN: A stopped furnace speaks more loudly than a manifesto. Unlock strike networks in neighboring countries; their governments must endure the stoppage or pay to break it.

Источник: `common/national_focus/MKN.txt:6351`. Стоимость: 5 (35 дней). Координаты: x=84, y=7.

Предпосылки: (Оружие народу [MKN_arms_to_the_people]).

Взаимоисключения: нет.

Прямые продолжения: MKN_autonomous_rail_crews.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- `add_political_power`: 75

Полное определение:

```pdx
focus = {
    id = MKN_propaganda_by_deed
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
    x = 84
}
```

### Самоуправляемые железнодорожные бригады — `MKN_autonomous_rail_crews`

EN: Autonomous Rail Crews.

Описание RU: Расписание принадлежит тем, кто обеспечивает движение. Рабочие бригады снизят стоимость поездов и ускорят строительство железных дорог и инфраструктуры.

Описание EN: The timetable belongs to those who keep it running. Worker crews lower train costs and accelerate railway and infrastructure construction.

Источник: `common/national_focus/MKN.txt:6376`. Стоимость: 5 (35 дней). Координаты: x=84, y=8.

Предпосылки: (Пропаганда действием [MKN_propaganda_by_deed]).

Взаимоисключения: нет.

Прямые продолжения: MKN_beacon_of_statelessness.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- `add_ideas`: MKN_autonomous_rail_crews_idea
- Параметр `MKN_unified_production_speed_buildings_factor`: 0.05

Полное определение:

```pdx
focus = {
    id = MKN_autonomous_rail_crews
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
    x = 84
}
```

### Маяк безгосударственности — `MKN_beacon_of_statelessness`

EN: The Beacon of Statelessness.

Описание RU: Они могут занять станцию, но не сельский сход за ней. Получим ещё 35% к защите национальной территории и 75% к урону вражеским гарнизонам на нашей оккупированной земле.

Описание EN: They may occupy a station, but never the village assembly behind it. Add 35% core defense and 75% damage to enemy garrisons on our occupied soil.

Источник: `common/national_focus/MKN.txt:6404`. Стоимость: 5 (35 дней). Координаты: x=84, y=9.

Предпосылки: (Самоуправляемые железнодорожные бригады [MKN_autonomous_rail_crews]).

Взаимоисключения: нет.

Прямые продолжения: нет.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- Параметр `MKN_army_army_core_defence_factor`: 0.35
- Параметр `MKN_army_resistance_damage_to_garrison_on_our_occupied_states`: 0.75

Полное определение:

```pdx
focus = {
    id = MKN_beacon_of_statelessness
    icon = GFX_focus_MKN_beacon_of_statelessness
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
    x = 84
}
```

## Аграрии — 8 фокусов

### Крестьянские делегаты — `MKN_peasant_delegates`

EN: The Peasant Delegates.

Описание RU: Новая корона не заменит шапку Батько. Избранный совет сёл возьмёт на себя ответственность за житницу. Аграрный изоляционизм требует подготовленного съезда и поддержки не менее 40%.

Описание EN: No new crown shall replace the Batko’s hat. An elected council of villages takes responsibility for the granary. Agrarian isolationism requires a prepared congress and at least 40% support.

Источник: `common/national_focus/MKN.txt:6435`. Стоимость: 5 (35 дней). Координаты: x=90, y=3.

Предпосылки: (Уход Батько [MKN_departure_of_batko]).

Взаимоисключения: MKN_military_takes_charge, MKN_triumph_of_free_soviets, MKN_emergency_revkom.

Прямые продолжения: MKN_grain_ultimatum.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- `set_politics`: ruling_party = neutrality; elections_allowed = no
- `add_stability`: -0.05

Полное определение:

```pdx
focus = {
    id = MKN_peasant_delegates
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
    x = 90
}
```

### Зерновой ультиматум — `MKN_grain_ultimatum`

EN: The Grain Ultimatum.

Описание RU: Сёла прокормят общую оборону, но никогда — четыре соперничающих штаба. Их ультиматум разрешит вопрос преемственности и остановит отсчёт до гражданской войны.

Описание EN: The villages will feed a common defense, never four rival headquarters. Their ultimatum settles the succession and stops the civil-war countdown.

Источник: `common/national_focus/MKN.txt:6476`. Стоимость: 5 (35 дней). Координаты: x=90, y=4.

Предпосылки: (Крестьянские делегаты [MKN_peasant_delegates]).

Взаимоисключения: нет.

Прямые продолжения: MKN_sever_urban_ties.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- `add_stability`: 0.10
- `add_political_power`: 50

Полное определение:

```pdx
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
```

### Разорвать связи с городом — `MKN_sever_urban_ties`

EN: Sever Urban Ties.

Описание RU: Закроем экспортные книги и распустим соперничающие делегации. Упраздним баланс сил, введём закрытую экономику и оставим больше продукции сёлам.

Описание EN: Close the export ledgers and dismiss the competing delegations. Abolish the balance of power, adopt a closed economy and reserve more output for the villages.

Источник: `common/national_focus/MKN.txt:6502`. Стоимость: 5 (35 дней). Координаты: x=90, y=5.

Предпосылки: (Зерновой ультиматум [MKN_grain_ultimatum]).

Взаимоисключения: нет.

Прямые продолжения: MKN_every_farm_a_fortress.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- `add_ideas`: closed_economy
- Параметр `MKN_unified_consumer_goods_factor`: -0.05

Полное определение:

```pdx
focus = {
    id = MKN_sever_urban_ties
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
    x = 90
}
```

### Каждый хутор — крепость — `MKN_every_farm_a_fortress`

EN: Every Farm a Fortress.

Описание RU: Подвалы станут складами боеприпасов, изгороди скроют огневые позиции. Построим два уровня сухопутных укреплений вдоль границ принадлежащих нам и контролируемых нами областей.

Описание EN: Cellars become ammunition stores; hedges conceal firing positions. Build two levels of land forts along the borders of states we own and control.

Источник: `common/national_focus/MKN.txt:6531`. Стоимость: 5 (35 дней). Координаты: x=90, y=6.

Предпосылки: (Разорвать связи с городом [MKN_sever_urban_ties]).

Взаимоисключения: нет.

Прямые продолжения: MKN_steppe_snipers.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- Вызываемые эффекты и полная награда приведены ниже.

Полное определение:

```pdx
focus = {
    id = MKN_every_farm_a_fortress
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
    x = 90
}
```

### Степные снайперы — `MKN_steppe_snipers`

EN: Steppe Snipers.

Описание RU: Борозда, терпеливый взгляд и один выстрел. Улучшим защиту и разведку, уменьшив преимущество противника от господства в воздухе.

Описание EN: A furrow, a patient eye and one shot. Improve defense and reconnaissance while reducing the enemy’s advantage from air superiority.

Источник: `common/national_focus/MKN.txt:6555`. Стоимость: 5 (35 дней). Координаты: x=90, y=7.

Предпосылки: (Каждый хутор — крепость [MKN_every_farm_a_fortress]).

Взаимоисключения: нет.

Прямые продолжения: MKN_railway_sabotage.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- Параметр `MKN_army_army_defence_factor`: 0.15
- Параметр `MKN_army_recon_factor`: 0.2
- Параметр `MKN_army_enemy_army_bonus_air_superiority_factor`: -0.15

Полное определение:

```pdx
focus = {
    id = MKN_steppe_snipers
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
    x = 90
}
```

### Железнодорожные диверсии — `MKN_railway_sabotage`

EN: Railway Sabotage.

Описание RU: Подготовим заряды до приказа об отступлении. Откроем намеренное разрушение инфраструктуры и железных дорог в пограничных областях под угрозой; ремонт займёт больше времени.

Описание EN: Prepare the charges before the retreat order comes. Unlock deliberate damage to infrastructure and railways in threatened border states; their repair will take longer.

Источник: `common/national_focus/MKN.txt:6590`. Стоимость: 5 (35 дней). Координаты: x=90, y=8.

Предпосылки: (Степные снайперы [MKN_steppe_snipers]).

Взаимоисключения: нет.

Прямые продолжения: MKN_cavalry_ambush.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- Вызываемые эффекты и полная награда приведены ниже.

Полное определение:

```pdx
focus = {
    id = MKN_railway_sabotage
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
    x = 90
}
```

### Кавалерийская засада — `MKN_cavalry_ambush`

EN: Cavalry Ambush.

Описание RU: Тачанки ждут за холмом, их лошади тихо стоят во ржи. Добавим общему армейскому духу 30% к атаке кавалерийских и моторизованных батальонов.

Описание EN: Tachankas wait behind the rise, their horses silent in the rye. Add 30% cavalry and motorized battalion attack to the common army spirit.

Источник: `common/national_focus/MKN.txt:6614`. Стоимость: 5 (35 дней). Координаты: x=90, y=9.

Предпосылки: (Железнодорожные диверсии [MKN_railway_sabotage]).

Взаимоисключения: нет.

Прямые продолжения: MKN_impregnable_granary.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- Параметр `MKN_army_modifier_army_sub_unit_cavalry_attack_factor`: 0.3
- Параметр `MKN_army_motorized_attack_factor`: 0.3

Полное определение:

```pdx
focus = {
    id = MKN_cavalry_ambush
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
    x = 90
}
```

### Неприступная житница — `MKN_impregnable_granary`

EN: The Impregnable Granary.

Описание RU: Захватчику не достанется лёгкой жатвы. Получим ещё 50% к защите национальной территории и увеличим вражеские потери от истощения на нашей земле на 40%.

Описание EN: There will be no easy harvest for an invader. Add 50% core defense and impose 40% additional hostile attrition in our territory.

Источник: `common/national_focus/MKN.txt:6645`. Стоимость: 5 (35 дней). Координаты: x=90, y=10.

Предпосылки: (Кавалерийская засада [MKN_cavalry_ambush]).

Взаимоисключения: нет.

Прямые продолжения: нет.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- Параметр `MKN_army_army_core_defence_factor`: 0.5
- Параметр `MKN_army_enemy_attrition`: 0.4

Полное определение:

```pdx
focus = {
    id = MKN_impregnable_granary
    icon = GFX_focus_MKN_impregnable_granary
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
    x = 90
}
```

## Ревком / коммунисты — 8 фокусов

### Чрезвычайный ревком — `MKN_emergency_revkom`

EN: The Emergency Revkom.

Описание RU: Красные делегаты требуют администрации, способной пережить своего основателя. При подготовленном съезде и поддержке не менее 40% государственный социализм станет правящей программой.

Описание EN: The red delegates demand an administration that can survive its founder. With a prepared congress and at least 40% support, state socialism becomes the ruling program.

Источник: `common/national_focus/MKN.txt:6676`. Стоимость: 5 (35 дней). Координаты: x=96, y=3.

Предпосылки: (Уход Батько [MKN_departure_of_batko]).

Взаимоисключения: MKN_military_takes_charge, MKN_triumph_of_free_soviets, MKN_peasant_delegates.

Прямые продолжения: MKN_purge_irreconcilables.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- `set_politics`: ruling_party = communism; elections_allowed = no
- `add_stability`: -0.05
- `add_ideas`: MKN_revkom_terror

Полное определение:

```pdx
focus = {
    id = MKN_emergency_revkom
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
    x = 96
}
```

### Устранить непримиримых — `MKN_purge_irreconcilables`

EN: Purge the Irreconcilables.

Описание RU: Ревком прикажет каждому вооружённому комитету сдать оружие и списки. Разрешим вопрос преемственности и остановим 180-дневный отсчёт.

Описание EN: The revkom orders every armed committee to submit its weapons and registers. Resolve the succession and stop the 180-day countdown.

Источник: `common/national_focus/MKN.txt:6720`. Стоимость: 5 (35 дней). Координаты: x=96, y=4.

Предпосылки: (Чрезвычайный ревком [MKN_emergency_revkom]).

Взаимоисключения: нет.

Прямые продолжения: MKN_embassy_to_kharkov.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- `add_stability`: 0.10
- `add_political_power`: 50

Полное определение:

```pdx
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

### Посольство в Харьков — `MKN_embassy_to_kharkov`

EN: An Embassy to Kharkov.

Описание RU: Упраздним баланс сил и отправим делегацию в советские республики. Первое предложение предусматривает взаимный военный транзит и обмен зерна на снабжение; Харьков вправе отказать.

Описание EN: Disband the balance of power and send a delegation to the Soviet Republics. The first proposal offers reciprocal military transit and a grain-for-supply agreement; Kharkov may refuse.

Источник: `common/national_focus/MKN.txt:6750`. Стоимость: 5 (35 дней). Координаты: x=96, y=5.

Предпосылки: (Устранить непримиримых [MKN_purge_irreconcilables]).

Взаимоисключения: нет.

Прямые продолжения: MKN_integrate_steel_lines.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- `country_event`: id = mkn_crisis.20; days = 1

Полное определение:

```pdx
focus = {
    id = MKN_embassy_to_kharkov
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
    x = 96
}
```

### Объединить стальные магистрали — `MKN_integrate_steel_lines`

EN: Integrate the Steel Lines.

Описание RU: С согласия советской стороны и при контролируемой общей границе построим железнодорожное соединение второго уровня. Получим десять локомотивов и два года помощи в организации снабжения.

Описание EN: With Soviet consent and a controlled common border, build a level-two railway connection. Receive ten locomotives and two years of coordinated supply assistance.

Источник: `common/national_focus/MKN.txt:6789`. Стоимость: 5 (35 дней). Координаты: x=96, y=6.

Предпосылки: (Посольство в Харьков [MKN_embassy_to_kharkov]).

Взаимоисключения: нет.

Прямые продолжения: MKN_red_military_specialists.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- `add_timed_idea`: idea = MKN_soviet_supply_agreement; days = 730

Полное определение:

```pdx
focus = {
    id = MKN_integrate_steel_lines
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
    x = 96
}
```

### Красные военные специалисты — `MKN_red_military_specialists`

EN: Red Military Specialists.

Описание RU: Прибывшие инструкторы привезут штатные таблицы, а не проповеди. Улучшим сплочённость и планирование армии, получим опыт и освоение сухопутной доктрины.

Описание EN: The visiting instructors bring tables of organization, not sermons. Improve army cohesion and planning, and gain experience and land doctrine mastery.

Источник: `common/national_focus/MKN.txt:6831`. Стоимость: 5 (35 дней). Координаты: x=96, y=7.

Предпосылки: (Объединить стальные магистрали [MKN_integrate_steel_lines]).

Взаимоисключения: нет.

Прямые продолжения: MKN_tractors_for_grain.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- `army_experience`: 30
- Параметр `MKN_army_army_org_factor`: 0.15
- Параметр `MKN_army_planning_speed`: 0.15

Полное определение:

```pdx
focus = {
    id = MKN_red_military_specialists
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
    x = 96
}
```

### Тракторы за зерно — `MKN_tractors_for_grain`

EN: Tractors for Grain.

Описание RU: Зерновой договор даст нам станки вместе с тракторами. Получим бонусы к промышленным исследованиям, два военных завода и улучшение строительства.

Описание EN: The grain contract buys machine tools as well as tractors. Gain industrial research bonuses, two military factories and stronger construction capacity.

Источник: `common/national_focus/MKN.txt:6867`. Стоимость: 5 (35 дней). Координаты: x=96, y=8.

Предпосылки: (Красные военные специалисты [MKN_red_military_specialists]).

Взаимоисключения: нет.

Прямые продолжения: MKN_anti_imperialist_front.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- `add_tech_bonus`: bonus = 0.5; uses = 2; category = industry
- `add_building_construction`: type = arms_factory; level = 2; instant_build = yes
- Параметр `MKN_unified_production_speed_buildings_factor`: 0.1

Полное определение:

```pdx
focus = {
    id = MKN_tractors_for_grain
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
    x = 96
}
```

### Антиимпериалистический фронт — `MKN_anti_imperialist_front`

EN: The Anti-Imperialist Front.

Описание RU: Предложим оборонительный союз против имперских дворов ЛитБела и Германии. Советское правительство должно дать согласие; ни одна чужая страна не вступит без собственного решения.

Описание EN: Propose a defensive alliance against the imperial courts of LitBel and Germany. The Soviet government must agree; no foreign country joins without its own decision.

Источник: `common/national_focus/MKN.txt:6910`. Стоимость: 5 (35 дней). Координаты: x=96, y=9.

Предпосылки: (Тракторы за зерно [MKN_tractors_for_grain]).

Взаимоисключения: нет.

Прямые продолжения: MKN_the_fatal_plenum.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- `set_country_flag`: MKN_soviet_front_pending
- `country_event`: id = mkn_crisis.23; days = 1

Полное определение:

```pdx
focus = {
    id = MKN_anti_imperialist_front
    y = 9
    completion_reward = {
        set_country_flag = MKN_soviet_front_pending
        SOV = {
            country_event = {
                id = mkn_crisis.23
                days = 1
            }
        }
    }
    prerequisite = {
        focus = MKN_tractors_for_grain
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
        OR = {
            is_in_faction = no
            is_in_faction_with = SOV
        }
        SOV = {
            OR = {
                is_in_faction = no
                is_faction_leader = yes
            }
        }
        NOT = {
            has_country_flag = MKN_soviet_front_pending
        }
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    cost = 5
    icon = GFX_focus_MKN_program_revkom_6
    x = 96
}
```

### Роковой пленум — `MKN_the_fatal_plenum`

EN: The Fatal Plenum.

Описание RU: Последняя хартия ставит наши автономные советы рядом с советским правительством на равных. Харьков может ратифицировать её — или изгнать нас из общего фронта и вторгнуться. Преданная революция будет сражаться с временным духом «Преданы дважды».

Описание EN: The final charter places our autonomous councils beside the Soviet government as equals. Kharkov may ratify it—or expel us from the common front and invade. A betrayed revolution fights with the temporary spirit Betrayed Twice.

Источник: `common/national_focus/MKN.txt:6962`. Стоимость: 5 (35 дней). Координаты: x=96, y=10.

Предпосылки: (Антиимпериалистический фронт [MKN_anti_imperialist_front]).

Взаимоисключения: нет.

Прямые продолжения: нет.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- `set_country_flag`: MKN_plenum_pending
- `country_event`: id = mkn_crisis.40; days = 1

Полное определение:

```pdx
focus = {
    id = MKN_the_fatal_plenum
    icon = GFX_focus_generic_industry_2
    y = 10
    completion_reward = {
        set_country_flag = MKN_plenum_pending
        SOV = {
            country_event = {
                id = mkn_crisis.40
                days = 1
            }
        }
    }
    prerequisite = {
        focus = MKN_anti_imperialist_front
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
        is_in_faction_with = SOV
        NOT = {
            has_country_flag = MKN_plenum_pending
        }
    }
    cancel_if_invalid = yes
    continue_if_invalid = no
    allow_branch = {
        has_country_flag = MKN_crisis_enabled
    }
    cost = 5
    x = 96
}
```

## Общий Чёрный интернационал и внешняя политика — 11 фокусов

### Чёрный интернационал — `MKN_black_international`

EN: The Black International.

Описание RU: После ухода Батьки общий Чёрный Интернационал станет опорой внешней политики при любом правительстве. Открывает четыре приглашения иностранных специалистов, набор добровольцев и общую ветку представительств, хозяйственных соглашений и зарубежного Набата.

Описание EN: After Batko’s departure, a common Black International will support foreign policy under every successor government. Opens four invitations for foreign specialists, volunteer recruitment and a shared branch of diplomatic missions, technical agreements and Nabat networks abroad.

Источник: `common/national_focus/MKN.txt:6314`. Стоимость: 5 (35 дней). Координаты: x=102, y=3.

Предпосылки: (Уход Батько [MKN_departure_of_batko]).

Взаимоисключения: нет.

Прямые продолжения: MKN_nabat_abroad, MKN_foreign_delegates.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- Параметр `MKN_army_send_volunteer_size`: 3
- Параметр `MKN_army_send_volunteers_tension`: -0.5

Полное определение:

```pdx
focus = {
    id = MKN_black_international
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
    cost = 5
    icon = GFX_focus_MKN_program_nabat_4
    x = 102
    y = 3
    prerequisite = {
        focus = MKN_departure_of_batko
    }
    available = {

    }
    ai_will_do = {
        factor = 2
        modifier = {
            factor = 0
            has_country_flag = MKN_crisis_active
        }
    }
}
```

### Делегаты за рубежом — `MKN_foreign_delegates`

EN: Delegates Abroad.

Описание RU: После ухода Батьки за границей должны слышать не отдельную фракцию, а всю Вольную территорию. Сеть сменяемых представителей будет поддерживать постоянные связи при любом правительстве.

Описание EN: After Batko’s departure, our neighbours must hear the Free Territory as a whole. Recallable representatives will maintain foreign contacts under every successor government.

Источник: `common/national_focus/MKN_foreign_focuses.txt:3`. Стоимость: 5 (35 дней). Координаты: x=98, y=4.

Предпосылки: (Чёрный интернационал [MKN_black_international]).

Взаимоисключения: нет.

Прямые продолжения: MKN_workers_corridors.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- `add_political_power`: 50

Полное определение:

```pdx
focus = {
    id = MKN_foreign_delegates
    icon = GFX_focus_generic_conference
    x = 98
    y = 4
    cost = 5
    prerequisite = {
        focus = MKN_black_international
    }
    available_if_capitulated = no
    available = {

    }
    search_filters = {
        FOCUS_FILTER_POLITICAL
    }
    ai_will_do = {
        factor = 2
        modifier = {
            factor = 0
            has_country_flag = MKN_crisis_active
        }
    }
    completion_reward = {
        add_political_power = 50
        hidden_effect = {
            MKN_rebuild_foreign_service = yes
        }
        custom_effect_tooltip = MKN_foreign_delegates_tt
    }
}
```

### Возрождение Набата на рубежах — `MKN_nabat_abroad`

EN: Nabat Beyond the Frontier.

Описание RU: После Великой смуты Набат должен говорить с крестьянами и рабочими по обе стороны границы. Связные создадут сеть солидарности, а не новую государственную канцелярию.

Описание EN: After the Great Tumult, Nabat must reach workers and peasants on both sides of the frontier. Couriers will build solidarity rather than a new state bureaucracy.

Источник: `common/national_focus/MKN_horizons_focuses.txt:3`. Стоимость: 5 (35 дней). Координаты: x=102, y=4.

Предпосылки: (Чёрный интернационал [MKN_black_international]).

Взаимоисключения: нет.

Прямые продолжения: MKN_agitation_in_litbel, MKN_galician_peasants.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- `add_ideas`: MKN_nabat_foreign_cells
- `add_political_power`: 50

Полное определение:

```pdx
focus = {
    id = MKN_nabat_abroad
    icon = GFX_goal_generic_intelligence_exchange
    cost = 5
    available_if_capitulated = no
    cancel_if_invalid = yes
    continue_if_invalid = no
    ai_will_do = {
        factor = 1
    }
    search_filters = {
        FOCUS_FILTER_POLITICAL
        FOCUS_FILTER_RESEARCH
    }
    available = {

    }
    completion_reward = {
        if = {
            limit = {
                has_dlc = "La Resistance"
            }
            add_ideas = MKN_nabat_foreign_cells
        }
        else = {
            add_political_power = 50
        }
        custom_effect_tooltip = MKN_nabat_abroad_unlock_tt
    }
    x = 102
    y = 4
    prerequisite = {
        focus = MKN_black_international
    }
}
```

### Коридоры мастерских — `MKN_workers_corridors`

EN: Workshop Corridors.

Описание RU: Торговля станками и обмен инженерами откроют двери, которых не открыть одной агитацией. Предложим соседям равноправные технические соглашения. Решение остаётся за получателем.

Описание EN: Machine-tool trade and visiting engineers open doors that agitation alone cannot. Offer equal technical agreements to neighbouring states, which remain free to accept or refuse.

Источник: `common/national_focus/MKN_foreign_focuses.txt:34`. Стоимость: 10 (70 дней). Координаты: x=98, y=5.

Предпосылки: (Делегаты за рубежом [MKN_foreign_delegates]).

Взаимоисключения: нет.

Прямые продолжения: MKN_consular_communes.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- Вызываемые эффекты и полная награда приведены ниже.

Полное определение:

```pdx
focus = {
    id = MKN_workers_corridors
    icon = GFX_goal_generic_scientific_exchange
    x = 98
    y = 5
    cost = 10
    prerequisite = {
        focus = MKN_foreign_delegates
    }
    available_if_capitulated = no
    available = {

    }
    search_filters = {
        FOCUS_FILTER_POLITICAL
    }
    ai_will_do = {
        factor = 2
        modifier = {
            factor = 0
            has_country_flag = MKN_crisis_active
        }
    }
    completion_reward = {
        hidden_effect = {
            MKN_rebuild_foreign_service = yes
        }
        custom_effect_tooltip = MKN_workers_corridors_tt
    }
}
```

### Агитация в ЛитБеле — `MKN_agitation_in_litbel`

EN: Agitation in Litbel.

Описание RU: Виленский компромисс не отменяет тяжбы батрака с помещиком. Мы предложим профсоюзам ЛитБела оружие и средства для самостоятельной борьбы.

Описание EN: The Vilnius compromise has not ended the struggle between labourers and landlords. Litbel unions shall receive arms and funds for their own struggle.

Источник: `common/national_focus/MKN_horizons_focuses.txt:38`. Стоимость: 5 (35 дней). Координаты: x=100, y=5.

Предпосылки: (Возрождение Набата на рубежах [MKN_nabat_abroad]).

Взаимоисключения: нет.

Прямые продолжения: MKN_fund_the_underground.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- Вызываемые эффекты и полная награда приведены ниже.

Полное определение:

```pdx
focus = {
    id = MKN_agitation_in_litbel
    icon = GFX_focus_generic_conference
    cost = 5
    available_if_capitulated = no
    cancel_if_invalid = yes
    continue_if_invalid = no
    ai_will_do = {
        factor = 1
    }
    search_filters = {
        FOCUS_FILTER_POLITICAL
        FOCUS_FILTER_RESEARCH
    }
    prerequisite = {
        focus = MKN_nabat_abroad
    }
    available = {
        LTB = {
            exists = yes
        }
    }
    completion_reward = {
        custom_effect_tooltip = MKN_litbel_agitation_unlock_tt
    }
    x = 100
    y = 5
}
```

### Защита галицких крестьян — `MKN_galician_peasants`

EN: Defend the Galician Peasants.

Описание RU: Габсбурги могут собирать коронные земли, но не могут владеть трудом их жителей. Сельские союзы Галиции и Буковины получат нашу помощь.

Описание EN: The Habsburgs may gather crownlands, but they cannot own their inhabitants' labour. Rural unions in Galicia and Bucovina shall receive our support.

Источник: `common/national_focus/MKN_horizons_focuses.txt:66`. Стоимость: 5 (35 дней). Координаты: x=104, y=5.

Предпосылки: (Возрождение Набата на рубежах [MKN_nabat_abroad]).

Взаимоисключения: нет.

Прямые продолжения: MKN_fund_the_underground.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- Вызываемые эффекты и полная награда приведены ниже.

Полное определение:

```pdx
focus = {
    id = MKN_galician_peasants
    icon = GFX_goal_generic_intelligence_exchange
    cost = 5
    available_if_capitulated = no
    cancel_if_invalid = yes
    continue_if_invalid = no
    ai_will_do = {
        factor = 1
    }
    search_filters = {
        FOCUS_FILTER_POLITICAL
        FOCUS_FILTER_RESEARCH
    }
    prerequisite = {
        focus = MKN_nabat_abroad
    }
    available = {
        AUS = {
            exists = yes
        }
    }
    completion_reward = {
        custom_effect_tooltip = MKN_galician_agitation_unlock_tt
    }
    x = 104
    y = 5
}
```

### Коммуны взаимной защиты — `MKN_consular_communes`

EN: Mutual Protection Communes.

Описание RU: Наши моряки, рабочие и переселенцы не должны оставаться без помощи за границей. Постоянные бюро займутся документами, посредничеством и возвращением граждан домой.

Описание EN: Our sailors, workers and emigrants need assistance abroad. Permanent bureaux will arrange documents, mediation and safe passage home.

Источник: `common/national_focus/MKN_foreign_focuses.txt:64`. Стоимость: 5 (35 дней). Координаты: x=98, y=6.

Предпосылки: (Коридоры мастерских [MKN_workers_corridors]).

Взаимоисключения: нет.

Прямые продолжения: MKN_solidarity_guarantees.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- `add_political_power`: 50

Полное определение:

```pdx
focus = {
    id = MKN_consular_communes
    icon = GFX_focus_generic_diplomatic_treaty
    x = 98
    y = 6
    cost = 5
    prerequisite = {
        focus = MKN_workers_corridors
    }
    available_if_capitulated = no
    available = {

    }
    search_filters = {
        FOCUS_FILTER_POLITICAL
    }
    ai_will_do = {
        factor = 2
        modifier = {
            factor = 0
            has_country_flag = MKN_crisis_active
        }
    }
    completion_reward = {
        add_political_power = 50
        hidden_effect = {
            MKN_rebuild_foreign_service = yes
        }
        custom_effect_tooltip = MKN_consular_communes_tt
    }
}
```

### Спонсирование подполья — `MKN_fund_the_underground`

EN: Fund the Underground.

Описание RU: Местные проводники, тайники и добровольные комитеты помогут нашим колоннам действовать за пределами родной земли.

Описание EN: Local guides, caches and voluntary committees will help our columns operate beyond their home territory.

Источник: `common/national_focus/MKN_horizons_focuses.txt:94`. Стоимость: 10 (70 дней). Координаты: x=102, y=6.

Предпосылки: (Агитация в ЛитБеле [MKN_agitation_in_litbel] ИЛИ Защита галицких крестьян [MKN_galician_peasants]).

Взаимоисключения: нет.

Прямые продолжения: MKN_congress_of_free_peoples.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- Вызываемые эффекты и полная награда приведены ниже.

Полное определение:

```pdx
focus = {
    id = MKN_fund_the_underground
    icon = GFX_goal_generic_intelligence_exchange
    cost = 10
    available_if_capitulated = no
    cancel_if_invalid = yes
    continue_if_invalid = no
    ai_will_do = {
        factor = 1
    }
    search_filters = {
        FOCUS_FILTER_POLITICAL
        FOCUS_FILTER_RESEARCH
    }
    prerequisite = {
        focus = MKN_agitation_in_litbel
        focus = MKN_galician_peasants
    }
    available = {
        has_completed_focus = MKN_steppe_general_staff
    }
    completion_reward = {
        hidden_effect = {
            nww_mkn_rebuild_services = yes
        }
        custom_effect_tooltip = MKN_underground_combat_tt
    }
    x = 102
    y = 6
}
```

### Гарантии солидарности — `MKN_solidarity_guarantees`

EN: Guarantees of Solidarity.

Описание RU: Подготовим договорные процедуры защиты независимых соседей. Совет сможет выдавать гарантии обычными дипломатическими средствами, а общий конгресс объединит мирные представительства и зарубежные движения.

Описание EN: Prepare treaty procedures for defending independent neighbours. The council can issue guarantees through normal diplomacy, while a common congress brings together our representatives and overseas movements.

Источник: `common/national_focus/MKN_foreign_focuses.txt:95`. Стоимость: 10 (70 дней). Координаты: x=98, y=7.

Предпосылки: (Коммуны взаимной защиты [MKN_consular_communes]).

Взаимоисключения: нет.

Прямые продолжения: MKN_congress_of_free_peoples.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- Вызываемые эффекты и полная награда приведены ниже.

Полное определение:

```pdx
focus = {
    id = MKN_solidarity_guarantees
    icon = GFX_goal_generic_alliance
    x = 98
    y = 7
    cost = 10
    prerequisite = {
        focus = MKN_consular_communes
    }
    available_if_capitulated = no
    available = {

    }
    search_filters = {
        FOCUS_FILTER_POLITICAL
    }
    ai_will_do = {
        factor = 2
        modifier = {
            factor = 0
            has_country_flag = MKN_crisis_active
        }
    }
    completion_reward = {
        hidden_effect = {
            MKN_rebuild_foreign_service = yes
        }
        custom_effect_tooltip = MKN_solidarity_guarantees_tt
    }
}
```

### Конгресс вольных народов — `MKN_congress_of_free_peoples`

EN: Congress of Free Peoples.

Описание RU: Советы соседних стран не станут нашими филиалами. Общий конгресс установит добровольность соглашений и право каждого отказаться.

Описание EN: Neighbouring councils shall not become our branch offices. A common congress will establish voluntary agreements and the right to refuse.

Источник: `common/national_focus/MKN_horizons_focuses.txt:124`. Стоимость: 5 (35 дней). Координаты: x=100, y=8.

Предпосылки: (Спонсирование подполья [MKN_fund_the_underground] ИЛИ Гарантии солидарности [MKN_solidarity_guarantees]).

Взаимоисключения: нет.

Прямые продолжения: MKN_global_syndicalist_pact.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- `add_political_power`: 75

Полное определение:

```pdx
focus = {
    id = MKN_congress_of_free_peoples
    icon = GFX_focus_generic_conference
    cost = 5
    available_if_capitulated = no
    cancel_if_invalid = yes
    continue_if_invalid = no
    ai_will_do = {
        factor = 1
    }
    search_filters = {
        FOCUS_FILTER_POLITICAL
        FOCUS_FILTER_RESEARCH
    }
    available = {

    }
    completion_reward = {
        add_political_power = 75
        custom_effect_tooltip = MKN_free_peoples_congress_tt
    }
    x = 100
    y = 8
    prerequisite = {
        focus = MKN_fund_the_underground
        focus = MKN_solidarity_guarantees
    }
}
```

### Глобальный синдикалистский пакт — `MKN_global_syndicalist_pact`

EN: Global Syndicalist Pact.

Описание RU: Чёрный Интернационал станет союзом по согласию, а не империей под новым флагом. Наши добровольцы помогут коммунистическим и демократическим участникам гражданских войн.

Описание EN: The Black International shall be a consensual association, not an empire under another flag. Our volunteers will aid communist and democratic participants in civil wars.

Источник: `common/national_focus/MKN_horizons_focuses.txt:152`. Стоимость: 10 (70 дней). Координаты: x=100, y=9.

Предпосылки: (Конгресс вольных народов [MKN_congress_of_free_peoples]).

Взаимоисключения: нет.

Прямые продолжения: нет.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- Вызываемые эффекты и полная награда приведены ниже.

Полное определение:

```pdx
focus = {
    id = MKN_global_syndicalist_pact
    icon = GFX_focus_generic_diplomatic_treaty
    cost = 10
    available_if_capitulated = no
    cancel_if_invalid = yes
    continue_if_invalid = no
    ai_will_do = {
        factor = 1
    }
    search_filters = {
        FOCUS_FILTER_POLITICAL
        FOCUS_FILTER_RESEARCH
    }
    prerequisite = {
        focus = MKN_congress_of_free_peoples
    }
    available = {
        is_subject = no
    }
    completion_reward = {
        hidden_effect = {
            nww_mkn_rebuild_services = yes
            set_rule = {
                can_send_volunteers = yes
            }
            add_relation_rule_override = {
                trigger = MKN_horizons_ineligible_volunteer_target
                can_send_volunteers = no
                usage_desc = MKN_volunteer_recipients_tt
            }
        }
        custom_effect_tooltip = MKN_syndicalist_pact_unlock_tt
    }
    x = 100
    y = 9
}
```

## Связанное послевоенное устройство украинских коммун — 8 фокусов

### Съезд украинских коммун — `MKN_ukrainian_communes_congress`

EN: Congress of Ukrainian Communes.

Описание RU: Война закончилась, но власть над областями ещё не стала общим договором. Созовём делегатов всех бывших украинских земель и определим порядок добровольного самоуправления.

Описание EN: The war is over, but ownership has yet to become a shared compact. Delegates from the former Ukrainian lands will define local self-government.

Источник: `common/national_focus/MKN_ukraine_integration_focuses.txt:3`. Стоимость: 5 (35 дней). Координаты: x=124, y=0.

Предпосылки: нет нарисованной предпосылки; см. available.

Взаимоисключения: нет.

Прямые продолжения: MKN_southern_commune_charters, MKN_right_bank_councils, MKN_northern_delegates.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- `add_political_power`: 100
- `add_stability`: 0.05

Полное определение:

```pdx
focus = {
    id = MKN_ukrainian_communes_congress
    icon = GFX_focus_generic_conference
    x = 124
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

### Хартии южных коммун — `MKN_southern_commune_charters`

EN: Charters of the Southern Communes.

Описание RU: Одесса, Николаев и Балта примут местные хартии и станут национальными областями. Согласованные склады уменьшат потребление снабжения.

Описание EN: Odesa, Mykolaiv and Balta adopt local charters and become core states. Coordinated depots reduce supply consumption.

Источник: `common/national_focus/MKN_ukraine_integration_focuses.txt:30`. Стоимость: 5 (35 дней). Координаты: x=120, y=1.

Предпосылки: (Съезд украинских коммун [MKN_ukrainian_communes_congress]).

Взаимоисключения: нет.

Прямые продолжения: MKN_ukrainian_rail_reconstruction.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- Параметр `MKN_unified_supply_consumption_factor`: -0.0500

Полное определение:

```pdx
focus = {
    id = MKN_southern_commune_charters
    icon = GFX_focus_generic_agricultural_subsidies
    x = 120
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

EN: Councils of the Right Bank.

Описание RU: Советы Житомирщины, Подолии и Правобережья получат признанное представительство. Национализация четырёх областей и постоянная стабильность заменят чрезвычайное управление.

Описание EN: Councils of Zhytomyr, Podillia and the right bank gain recognized representation. Four states become cores and lasting stability replaces emergency administration.

Источник: `common/national_focus/MKN_ukraine_integration_focuses.txt:68`. Стоимость: 10 (70 дней). Координаты: x=124, y=1.

Предпосылки: (Съезд украинских коммун [MKN_ukrainian_communes_congress]).

Взаимоисключения: нет.

Прямые продолжения: MKN_dnieper_workshop_federation.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- `add_political_power`: 50
- Параметр `MKN_unified_stability_factor`: 0.0500

Полное определение:

```pdx
focus = {
    id = MKN_right_bank_councils
    icon = GFX_focus_generic_diplomatic_treaty
    x = 124
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

EN: Mandates of the Northern Districts.

Описание RU: Глухов и бывшая украинская область Лиски отправят своих делегатов. Местные мандаты обеспечат национализацию, добровольцев и политический доход.

Описание EN: Hlukhiv and the former Ukrainian district of Liski send delegates. Local mandates bring cores, volunteers and political income.

Источник: `common/national_focus/MKN_ukraine_integration_focuses.txt:110`. Стоимость: 5 (35 дней). Координаты: x=128, y=1.

Предпосылки: (Съезд украинских коммун [MKN_ukrainian_communes_congress]).

Взаимоисключения: нет.

Прямые продолжения: MKN_ukrainian_rail_reconstruction.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- `add_manpower`: 10000
- Параметр `MKN_unified_political_power_gain`: 0.1000

Полное определение:

```pdx
focus = {
    id = MKN_northern_delegates
    icon = GFX_focus_generic_manpower
    x = 128
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

### Федерация днепровских мастерских — `MKN_dnieper_workshop_federation`

EN: Federation of Dnieper Workshops.

Описание RU: Киев и Черкассы войдут в хозяйственную федерацию на правах национальных областей. Восстановленная оружейная линия и общий портфель заказов усилят выпуск.

Описание EN: Kyiv and Cherkasy join the economic federation as core states. A restored arms line and shared orders improve production.

Источник: `common/national_focus/MKN_ukraine_integration_focuses.txt:146`. Стоимость: 10 (70 дней). Координаты: x=124, y=2.

Предпосылки: (Советы Правобережья [MKN_right_bank_councils]).

Взаимоисключения: нет.

Прямые продолжения: MKN_ukrainian_rail_reconstruction.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- `add_building_construction`: type = arms_factory; level = 1; instant_build = yes
- Параметр `MKN_unified_industrial_capacity_factory`: 0.0500

Полное определение:

```pdx
focus = {
    id = MKN_dnieper_workshop_federation
    icon = GFX_focus_generic_military_industry
    x = 124
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

### Восстановление украинских магистралей — `MKN_ukrainian_rail_reconstruction`

EN: Rebuild the Ukrainian Main Lines.

Описание RU: После согласования всех региональных хартий ремонтные артели свяжут Одессу, Киев и Глухов. Постоянные бонусы строительства и ремонта развивают общий хозяйственный дух.

Описание EN: Once regional charters are agreed, repair artels connect Odesa, Kyiv and Hlukhiv. Permanent construction and repair bonuses develop the shared economic spirit.

Источник: `common/national_focus/MKN_ukraine_integration_focuses.txt:189`. Стоимость: 10 (70 дней). Координаты: x=124, y=3.

Предпосылки: (Хартии южных коммун [MKN_southern_commune_charters]) И (Федерация днепровских мастерских [MKN_dnieper_workshop_federation]) И (Мандаты северных волостей [MKN_northern_delegates]).

Взаимоисключения: нет.

Прямые продолжения: MKN_kyiv_scientific_exchange.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- Параметр `MKN_unified_production_speed_buildings_factor`: 0.1000
- Параметр `MKN_unified_repair_speed_factor`: 0.1000

Полное определение:

```pdx
focus = {
    id = MKN_ukrainian_rail_reconstruction
    icon = GFX_focus_generic_railroad
    x = 124
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

### Киевский научный обмен — `MKN_kyiv_scientific_exchange`

EN: Kyiv Scientific Exchange.

Описание RU: Объединим киевские школы и лаборатории с двумя уже созданными исследовательскими сетями коммун. Этот обмен после интеграции Украины создаёт шестую ячейку исследований. Если она уже получена в старом сохранении, вместо неё будут доступны две промышленные скидки 50%.

Описание EN: Join Kyiv’s schools and laboratories to both existing communal research networks. This exchange after Ukrainian integration establishes the sixth research slot. If an older save already has it, gain two 50% industrial research bonuses instead.

Источник: `common/national_focus/MKN_ukraine_integration_focuses.txt:228`. Стоимость: 10 (70 дней). Координаты: x=124, y=4.

Предпосылки: (Восстановление украинских магистралей [MKN_ukrainian_rail_reconstruction]).

Взаимоисключения: нет.

Прямые продолжения: MKN_federation_of_free_councils.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- `add_tech_bonus`: bonus = 0.5; uses = 2; category = industry

Полное определение:

```pdx
focus = {
    id = MKN_kyiv_scientific_exchange
    icon = GFX_focus_research
    x = 124
    y = 4
    cost = 10
    available_if_capitulated = no
    cancel_if_invalid = yes
    continue_if_invalid = no
    available = {
        MKN_ukraine_integration_ready = yes
        has_completed_focus = MKN_communal_research_network
        has_completed_focus = MKN_free_science_network
        amount_research_slots > 4
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
                amount_research_slots < 6
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

### Федерация вольных советов — `MKN_federation_of_free_councils`

EN: Federation of Free Councils.

Описание RU: Региональные договоры станут общим федеративным уставом. Стабильность, снабжение и производственная эффективность закрепят интеграцию через единый хозяйственный дух.

Описание EN: Regional compacts become a common federal charter. Stability, supply and production efficiency consolidate integration through the shared economic spirit.

Источник: `common/national_focus/MKN_ukraine_integration_focuses.txt:269`. Стоимость: 10 (70 дней). Координаты: x=124, y=5.

Предпосылки: (Киевский научный обмен [MKN_kyiv_scientific_exchange]).

Взаимоисключения: нет.

Прямые продолжения: нет.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- `add_stability`: 0.05
- Параметр `MKN_unified_stability_factor`: 0.0500
- Параметр `MKN_unified_supply_consumption_factor`: -0.0500
- Параметр `MKN_unified_production_factory_max_efficiency_factor`: 0.0500

Полное определение:

```pdx
focus = {
    id = MKN_federation_of_free_councils
    icon = GFX_focus_generic_diplomatic_treaty
    x = 124
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

## Контекст внешних предпосылок — 27 фокусов

### Днепрострой — `MKN_dneprostroi`

EN: Dnieper Industrial Program.

Описание RU: Коммуны поручат общему совету крупные стройки, оставив сметы открытыми делегатам. Единый план свяжет металлургию, энергетику и транспорт; путь вольных кооперативов станет недоступен.

Описание EN: Open accounts and elected delegates will oversee a common plan for heavy industry, power and transport. This choice excludes the free cooperatives.

Источник: `common/national_focus/MKN.txt:12`. Стоимость: 5 (35 дней). Координаты: x=4, y=0.

Предпосылки: нет нарисованной предпосылки; см. available.

Взаимоисключения: MKN_free_cooperatives.

Прямые продолжения: MKN_dnieper_audit.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- `add_political_power`: 50
- Параметр `MKN_unified_political_power_gain`: 0.1000
- Параметр `MKN_unified_consumer_goods_factor`: -0.0500
- Параметр `MKN_unified_production_speed_buildings_factor`: 0.0500
- Параметр `MKN_unified_industrial_capacity_factory`: 0.0500

Полное определение:

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

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- `add_political_power`: 50
- Параметр `MKN_unified_political_power_gain`: 0.1000
- Параметр `MKN_unified_consumer_goods_factor`: -0.0500
- Параметр `MKN_unified_production_speed_buildings_factor`: 0.0500
- Параметр `MKN_unified_industrial_capacity_factory`: 0.0500

Полное определение:

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

### Штаб степных армий — `MKN_steppe_general_staff`

EN: Steppe Army Staff.

Описание RU: Вооружим колонны и введём общий порядок сбора, сохраняя выборных командиров.\n\nСогласованные эшелоны подвезут боеприпасы быстрее случайных крестьянских обозов.\n\nШтаб Белаша свяжет самостоятельные отряды общим планом операций.\n\nОткрывает одноразовые тактики полевого штаба за опыт и командный ресурс.

Описание EN: Equip the columns and establish mustering rules under elected commanders.\n\nScheduled trains will deliver ammunition instead of relying on improvised carts.\n\nBelash's staff will coordinate independent detachments through shared operational plans.\n\nUnlocks one-time field headquarters tactics purchased with experience and command power.

Источник: `common/national_focus/MKN.txt:1010`. Стоимость: 10 (70 дней). Координаты: x=28, y=0.

Предпосылки: нет нарисованной предпосылки; см. available.

Взаимоисключения: нет.

Прямые продолжения: MKN_steppe_horde, MKN_motorized_vanguard, MKN_memory_of_atamansha_marusya.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- Параметр `MKN_army_army_org_factor`: 0.04
- `set_country_flag`: MKN_military_stat_tachanka_columns
- `army_experience`: 20
- `set_country_flag`: MKN_military_reward_tachanka_columns
- Параметр `MKN_army_supply_consumption_factor`: -0.05
- `set_country_flag`: MKN_military_stat_railway_war
- `add_tech_bonus`: name = MKN_railway_war; bonus = 0.5; uses = 1; category = train_tech
- `add_tech_bonus`: name = MKN_railway_war; bonus = 0.5; uses = 1; category = logistics_tech
- `set_country_flag`: MKN_military_reward_railway_war
- Параметр `MKN_army_max_planning`: 0.05
- `set_country_flag`: MKN_military_stat_steppe_general_staff
- `army_experience`: 25
- `set_country_flag`: MKN_military_reward_steppe_general_staff
- `set_country_flag`: MKN_military_bundle_steppe_general_staff

Полное определение:

```pdx
focus = {
    id = MKN_steppe_general_staff
    icon = GFX_focus_generic_military_academy
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
    x = 28
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

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- `country_event`: id = mkn.30; days = 1
- `add_tech_bonus`: bonus = 0.5; uses = 1; category = industry
- `add_building_construction`: type = industrial_complex; level = 1; instant_build = yes
- Параметр `MKN_unified_industrial_capacity_factory`: 0.0500
- Параметр `MKN_unified_production_factory_efficiency_gain_factor`: 0.1000
- Параметр `MKN_unified_research_speed_factor`: 0.0500

Полное определение:

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

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- `add_political_power`: 50
- Параметр `MKN_unified_industrial_capacity_factory`: 0.0500

Полное определение:

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

### Ресурсная база Юга — `MKN_southern_resources`

EN: Resource Base of the South.

Описание RU: Никопольский марганец и угольные промыслы войдут в общий договор поставок. Сырьё останется достоянием коммун, а заводы получат устойчивую основу для больших серий.

Описание EN: Nikopol manganese and the southern coal workings will enter a common supply agreement, providing the raw materials for large production runs.

Источник: `common/national_focus/MKN.txt:104`. Стоимость: 5 (35 дней). Координаты: x=4, y=2.

Предпосылки: (Открытые сметы Днепростроя [MKN_dnieper_audit]).

Взаимоисключения: нет.

Прямые продолжения: MKN_steppe_industrial_giants.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- `add_political_power`: 50
- `add_tech_bonus`: bonus = 0.5; uses = 1; category = excavation_tech

Полное определение:

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

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- `add_political_power`: 150
- `add_stability`: 0.10
- `add_building_construction`: type = industrial_complex; level = 2; instant_build = yes
- Параметр `MKN_unified_political_power_gain`: 0.2000

Полное определение:

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

### Индустриальные гиганты степи — `MKN_steppe_industrial_giants`

EN: Industrial Giants of the Steppe.

Описание RU: «Коммунар», трубные мастерские и алюминиевое производство объединят заказы и инженерные кадры. Новые корпуса дадут фабрику и три военных завода, а собственный алюминий обеспечит машиностроение.

Описание EN: Kommunar, the tube works and aluminium plants pool their orders and engineers. One civilian factory, three military factories and aluminium supplies restore large-scale manufacturing.

Источник: `common/national_focus/MKN.txt:151`. Стоимость: 10 (70 дней). Координаты: x=4, y=3.

Предпосылки: (Ресурсная база Юга [MKN_southern_resources]).

Взаимоисключения: нет.

Прямые продолжения: MKN_zaporizhstal.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- `add_building_construction`: type = industrial_complex; level = 1; instant_build = yes
- `add_building_construction`: type = arms_factory; level = 3; instant_build = yes
- `add_tech_bonus`: bonus = 0.5; uses = 1; category = air_equipment
- Параметр `MKN_unified_industrial_capacity_factory`: 0.1000
- Параметр `MKN_unified_production_factory_efficiency_gain_factor`: 0.0500

Полное определение:

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

### Передвижные мастерские и кузницы — `MKN_mobile_workshops`

EN: Mobile Workshops and Village Smithies.

Описание RU: Сельские кузни войдут в сеть ремонтных поездок и передвижных мастерских. Два военных завода, грузовики и обмен инструментом восстановят выпуск, не собирая всё хозяйство в одном уязвимом центре.

Описание EN: Village smithies join travelling repair teams. Two military factories, trucks and shared tools restore production without concentrating it in one vulnerable industrial centre.

Источник: `common/national_focus/MKN.txt:621`. Стоимость: 10 (70 дней). Координаты: x=16, y=3.

Предпосылки: (Степные рынки [MKN_steppe_markets]).

Взаимоисключения: нет.

Прямые продолжения: MKN_rifle_concern.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- `army_experience`: 20
- `add_building_construction`: type = arms_factory; level = 2; instant_build = yes
- Параметр `MKN_unified_political_power_gain`: 0.1000
- Параметр `MKN_unified_consumer_goods_factor`: -0.0500
- Параметр `MKN_unified_production_speed_buildings_factor`: 0.0500
- Параметр `MKN_unified_industrial_capacity_factory`: 0.1000
- Параметр `MKN_unified_production_factory_efficiency_gain_factor`: 0.1000
- Параметр `MKN_unified_research_speed_factor`: 0.0500

Полное определение:

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

### Запорожсталь — `MKN_zaporizhstal`

EN: Zaporizhstal.

Описание RU: Две новые линии и дополнительные плавки станут основой концерна «Вольная сталь». Промышленный совет доступен всем коммунам; с Arms Against Tyranny заводы также образуют артиллерийскую MIO, развиваемую производственными циклами и финальным договором.

Описание EN: Two new production lines and additional steel establish the Free Steel concern. Its industrial council is available with or without DLC; Arms Against Tyranny also enables an artillery MIO developed through production cycles and the final compact.

Источник: `common/national_focus/MKN.txt:212`. Стоимость: 10 (70 дней). Координаты: x=4, y=4.

Предпосылки: (Индустриальные гиганты степи [MKN_steppe_industrial_giants]).

Взаимоисключения: нет.

Прямые продолжения: MKN_worker_battalions, MKN_dnieper_logistics_hub.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- `add_political_power`: 50
- `add_building_construction`: type = arms_factory; level = 2; instant_build = yes
- Параметр `MKN_unified_political_power_gain`: 0.1000
- Параметр `MKN_unified_consumer_goods_factor`: -0.0500
- Параметр `MKN_unified_production_speed_buildings_factor`: 0.0500
- Параметр `MKN_unified_industrial_capacity_factory`: 0.0500

Полное определение:

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

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- `add_offsite_building`: type = arms_factory; level = 1
- Параметр `MKN_unified_industrial_capacity_factory`: 0.0500

Полное определение:

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

### Единая днепровская логистика — `MKN_dnieper_logistics_hub`

EN: Unified Dnieper Logistics.

Описание RU: Диспетчеры сведут речные, железнодорожные и заводские расписания. На карте станут доступны три проекта: Кичкасский мост, расчистка Днепра и степные узловые станции. Каждая стройка длится 60 дней.

Описание EN: Dispatchers coordinate river, rail and factory schedules. Unlock three 60-day map projects: Kichkas Bridge, Dnieper waterways and steppe junctions.

Источник: `common/national_focus/MKN.txt:314`. Стоимость: 5 (35 дней). Координаты: x=2, y=5.

Предпосылки: (Запорожсталь [MKN_zaporizhstal]).

Взаимоисключения: нет.

Прямые продолжения: MKN_steppe_electrification.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- `add_political_power`: 50
- `add_tech_bonus`: bonus = 0.5; uses = 1; category = train_tech
- Параметр `MKN_unified_supply_consumption_factor`: -0.1500
- Параметр `MKN_unified_army_org_regain`: 0.1000

Полное определение:

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

EN: Workers’ Reserve Battalions.

Описание RU: Выборные бригадиры и заводские инструкторы подготовят резерв без разрыва с производством. Общие сборы улучшат организацию и планирование армии и сократят подготовку новых частей.

Описание EN: Elected brigadiers and factory instructors train a reserve without severing its ties to production. Joint exercises improve organization and planning while reducing training time.

Источник: `common/national_focus/MKN.txt:282`. Стоимость: 5 (35 дней). Координаты: x=6, y=5.

Предпосылки: (Запорожсталь [MKN_zaporizhstal]).

Взаимоисключения: нет.

Прямые продолжения: MKN_production_cycles.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- `army_experience`: 40
- Параметр `MKN_unified_army_org_factor`: 0.2000
- Параметр `MKN_unified_training_time_army_factor`: -0.2000
- Параметр `MKN_unified_max_planning`: 0.1500

Полное определение:

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

### Хлебные биржи и резервы — `MKN_grain_exchanges`

EN: Grain Exchanges and Reserves.

Описание RU: Фабрика в Херсоне поддержит переработку и обмен урожая. На карте открываются три проекта по 60 дней: запорожские элеваторы, херсонские зерновые терминалы и степная посевная. Политику запасов выбирает хозяйственный конгресс.

Описание EN: A Kherson factory supports processing and exchange. Unlock three 60-day map projects: Zaporizhzhia elevators, Kherson grain terminals and steppe sowing. The Economic Congress chooses stockpile policy.

Источник: `common/national_focus/MKN.txt:722`. Стоимость: 5 (35 дней). Координаты: x=14, y=5.

Предпосылки: (Артели стрелкового вооружения [MKN_rifle_concern]).

Взаимоисключения: нет.

Прямые продолжения: MKN_workshop_standards.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- `add_building_construction`: type = industrial_complex; level = 1; instant_build = yes

Полное определение:

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

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- `add_tech_bonus`: bonus = 0.5; uses = 1; category = train_tech
- `add_tech_bonus`: bonus = 0.5; uses = 1; category = motorized_equipment
- Параметр `MKN_unified_supply_consumption_factor`: -0.3000
- Параметр `MKN_unified_army_org_regain`: 0.1500
- Параметр `MKN_unified_attrition`: -0.0500

Полное определение:

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

### Электрификация степи — `MKN_steppe_electrification`

EN: Electrification of the Steppe.

Описание RU: Общая сеть уменьшит расход энергии заводами. Открываем три проекта на 60 дней: турбины Днепрогэса, электрификацию Екатеринослава и резервные угольные линии; каждый занимает две гражданские фабрики.

Описание EN: The common grid reduces factory energy demand. Unlock three 60-day projects using two civilian factories each: Dnieper turbines, the Katerynoslav grid and reserve coal lines.

Источник: `common/national_focus/MKN.txt:348`. Стоимость: 10 (70 дней). Координаты: x=2, y=6.

Предпосылки: (Единая днепровская логистика [MKN_dnieper_logistics_hub]).

Взаимоисключения: нет.

Прямые продолжения: MKN_production_cycles.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- `add_political_power`: 100
- Параметр `MKN_unified_production_speed_buildings_factor`: 0.0500
- Параметр `MKN_unified_factory_energy_consumption`: -0.1000

Полное определение:

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

### Договор о взаимозаменяемости — `MKN_workshop_standards`

EN: Interchangeability Agreement.

Описание RU: Общие калибры, ремонтные образцы и портфель заказов соединят самостоятельные мастерские. Дополнительный военный завод и развитие оружейного предприятия повысят выпуск и эффективность без единственного промышленного центра.

Описание EN: Common calibres, repair patterns and pooled orders unite independent workshops. Another military factory and an upgraded weapons enterprise improve output without a single industrial centre.

Источник: `common/national_focus/MKN.txt:807`. Стоимость: 10 (70 дней). Координаты: x=16, y=6.

Предпосылки: (Хлебные биржи и резервы [MKN_grain_exchanges]) И (Гужевая и грузовая логистика [MKN_freight_logistics]).

Взаимоисключения: нет.

Прямые продолжения: MKN_field_schools.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- `add_tech_bonus`: bonus = 0.5; uses = 1; category = infantry_weapons
- `add_building_construction`: type = arms_factory; level = 1; instant_build = yes
- Параметр `MKN_unified_industrial_capacity_factory`: 0.1500
- Параметр `MKN_unified_production_factory_efficiency_gain_factor`: 0.2500
- Параметр `MKN_unified_research_speed_factor`: 0.0500

Полное определение:

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

### Согласованные производственные циклы — `MKN_production_cycles`

EN: Coordinated Production Cycles.

Описание RU: После подготовки резерва и энергосети заводы примут общие допуски, длинные серии и согласованные заказы. Военный завод и повышение предела эффективности закрепят устойчивый выпуск вооружения.

Описание EN: Prepared reserves and a working grid allow common tolerances and long production runs. Another military factory and a higher efficiency cap secure sustained arms production.

Источник: `common/national_focus/MKN.txt:377`. Стоимость: 10 (70 дней). Координаты: x=4, y=7.

Предпосылки: (Электрификация степи [MKN_steppe_electrification]) И (Рабочие батальоны резерва [MKN_worker_battalions]).

Взаимоисключения: нет.

Прямые продолжения: MKN_steel_volnitsa.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- `add_political_power`: 25
- `add_tech_bonus`: bonus = 0.5; uses = 1; category = industry
- `add_building_construction`: type = arms_factory; level = 1; instant_build = yes
- Параметр `MKN_unified_industrial_capacity_factory`: 0.2000
- Параметр `MKN_unified_production_factory_efficiency_gain_factor`: 0.0500
- Параметр `MKN_unified_production_factory_max_efficiency_factor`: 0.1000

Полное определение:

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

### Полевые школы коммун — `MKN_field_schools`

EN: Commune Field Schools.

Описание RU: Передвижные инструкторы и сменяемые командиры обучат самооборону связи, маскировке и совместному манёвру. Подготовка станет короче, а отряды сохранят подвижность и связь со своими коммунами.

Описание EN: Travelling instructors and recallable commanders train local defence in signals, concealment and coordinated manoeuvre. Units train faster while retaining their mobility and communal ties.

Источник: `common/national_focus/MKN.txt:885`. Стоимость: 5 (35 дней). Координаты: x=16, y=7.

Предпосылки: (Договор о взаимозаменяемости [MKN_workshop_standards]).

Взаимоисключения: нет.

Прямые продолжения: MKN_communal_compact.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- `army_experience`: 30
- Параметр `MKN_unified_army_org_factor`: 0.2000
- Параметр `MKN_unified_training_time_army_factor`: -0.2500
- Параметр `MKN_unified_max_planning`: 0.1000
- Параметр `MKN_unified_army_speed_factor`: 0.0500

Полное определение:

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

### Стальная вольница — `MKN_steel_volnitsa`

EN: A Free Territory of Steel.

Описание RU: Хозяйственный договор соединит промышленный совет, рабочие кассы и единую логистику. Развиваем общий хозяйственный дух и концерн «Вольная сталь», открываем фабрику и расширяем пространство для новых предприятий.

Описание EN: A common compact unites factory councils, workers’ welfare and logistics. Develop the shared economic spirit and Free Steel concern, establish a civilian factory and expand room for further industry.

Источник: `common/national_focus/MKN.txt:442`. Стоимость: 10 (70 дней). Координаты: x=4, y=8.

Предпосылки: (Согласованные производственные циклы [MKN_production_cycles]).

Взаимоисключения: нет.

Прямые продолжения: MKN_free_workshops_focus.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- `add_political_power`: 75
- `add_stability`: 0.05
- `add_building_construction`: type = industrial_complex; level = 1; instant_build = yes
- Параметр `MKN_unified_political_power_gain`: 0.1500
- Параметр `MKN_unified_consumer_goods_factor`: -0.0500
- Параметр `MKN_unified_production_speed_buildings_factor`: 0.1500
- Параметр `MKN_unified_global_building_slots_factor`: 0.3000
- Параметр `MKN_unified_supply_consumption_factor`: -0.1500
- Параметр `MKN_unified_army_org_regain`: 0.1000

Полное определение:

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

### Хартия хозяйственной взаимопомощи — `MKN_communal_compact`

EN: Charter of Economic Mutual Aid.

Описание RU: Договоры кредита, страхования и взаимного ремонта завершат восстановление хозяйства. Рассредоточенные мастерские получат постоянные −20% ущерба промышленности от бомбардировок и +20% скорости ремонта в общем хозяйственном духе.

Описание EN: Credit, insurance and repair agreements complete recovery. Dispersed workshops gain permanent −20% industrial bombing damage and +20% repair speed through the shared economic spirit.

Источник: `common/national_focus/MKN.txt:921`. Стоимость: 10 (70 дней). Координаты: x=16, y=8.

Предпосылки: (Полевые школы коммун [MKN_field_schools]).

Взаимоисключения: нет.

Прямые продолжения: MKN_free_workshops_focus.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- `add_stability`: 0.05
- `add_political_power`: 50
- Параметр `MKN_unified_political_power_gain`: 0.1500
- Параметр `MKN_unified_consumer_goods_factor`: -0.1000
- Параметр `MKN_unified_production_speed_buildings_factor`: 0.0500
- Параметр `MKN_unified_stability_factor`: 0.0500
- Параметр `MKN_unified_global_building_slots_factor`: 0.3000
- Параметр `MKN_unified_industry_air_damage_factor`: -0.2000
- Параметр `MKN_unified_repair_speed_factor`: 0.2000

Полное определение:

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

### Вольные мастерские Екатеринослава и Гуляйполя — `MKN_free_workshops_focus`

EN: Ekaterinoslav & Huliaipole Free Workshops.

Описание RU: После завершения Днепростроя или программы вольных кооперативов объединим мастерские Екатеринослава и Гуляйполя в общую инженерную сеть. Она откроет предприятие и станет основой технических коммун и вольных институтов.

Описание EN: After completing Dneprostroi or the free cooperatives programme, unite the Ekaterinoslav and Huliaipole workshops into a common engineering network, opening the enterprise and the path to technical communes and free institutes.

Источник: `common/national_focus/MKN.txt:7008`. Стоимость: 5 (35 дней). Координаты: x=10, y=10.

Предпосылки: (Стальная вольница [MKN_steel_volnitsa] ИЛИ Хартия хозяйственной взаимопомощи [MKN_communal_compact]).

Взаимоисключения: нет.

Прямые продолжения: MKN_technical_communes.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- Вызываемые эффекты и полная награда приведены ниже.

Полное определение:

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
    prerequisite = {
        focus = MKN_steel_volnitsa
        focus = MKN_communal_compact
    }
    x = 10
    y = 10
}
```

### Технические коммуны — `MKN_technical_communes`

EN: Technical Communes.

Описание RU: Учёные и мастера создадут общую сеть технических школ, доступную при любой форме хозяйства.

Описание EN: Scientists and craftsmen establish a technical school network under either economic model.

Источник: `common/national_focus/MKN.txt:5713`. Стоимость: 5 (35 дней). Координаты: x=10, y=11.

Предпосылки: (Вольные мастерские Екатеринослава и Гуляйполя [MKN_free_workshops_focus]).

Взаимоисключения: нет.

Прямые продолжения: MKN_polytechnic_institute.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- `add_tech_bonus`: bonus = 0.5; uses = 2; category = electronics
- `add_political_power`: 50

Полное определение:

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
    cost = 5
    prerequisite = {
        focus = MKN_free_workshops_focus
    }
    x = 10
    y = 11
}
```

### Вольный политехникум — `MKN_polytechnic_institute`

EN: Free Polytechnic.

Описание RU: Инженерное образование даст артелям свои станки, измерительные приборы и специалистов.

Описание EN: Engineering education supplies the artels with machine tools, instruments and trained specialists.

Источник: `common/national_focus/MKN.txt:5731`. Стоимость: 5 (35 дней). Координаты: x=10, y=12.

Предпосылки: (Технические коммуны [MKN_technical_communes]).

Взаимоисключения: нет.

Прямые продолжения: MKN_communal_research_network.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- `add_tech_bonus`: bonus = 0.5; uses = 2; category = industry

Полное определение:

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
    cost = 5
    x = 10
    y = 12
}
```

### Сеть исследовательских коммун — `MKN_communal_research_network`

EN: Communal Research Network.

Описание RU: Свяжем лаборатории промышленных коммун и создадим дополнительную исследовательскую группу. Общая программа институтов рассчитана на пять ячеек; шестая появится после интеграции Украины и Киевского научного обмена.

Описание EN: Connect the industrial communes’ laboratories and establish an additional research team. The common institute programme provides five slots; Ukrainian integration and Kyiv Scientific Exchange provide the sixth.

Источник: `common/national_focus/MKN.txt:5748`. Стоимость: 5 (35 дней). Координаты: x=10, y=13.

Предпосылки: (Вольный политехникум [MKN_polytechnic_institute]).

Взаимоисключения: нет.

Прямые продолжения: MKN_workshop_airplane_artels.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- `add_tech_bonus`: bonus = 0.5; uses = 1; category = electronics

Полное определение:

```pdx
focus = {
    id = MKN_communal_research_network
    icon = GFX_focus_research
    prerequisite = {
        focus = MKN_polytechnic_institute
    }
    cost = 5
    x = 10
    y = 13
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
                uses = 1
                category = electronics
            }
        }
    }
}
```

### Артельные авиамастерские — `MKN_workshop_airplane_artels`

EN: Artel Aviation Workshops.

Описание RU: Разъездные авиамастерские ремонтируют и сколачивают машины прямо под открытым небом.

Описание EN: Itinerant aviation workshops repair and assemble machines in the open air.

Источник: `common/national_focus/MKN.txt:979`. Стоимость: 5 (35 дней). Координаты: x=10, y=14.

Предпосылки: (Сеть исследовательских коммун [MKN_communal_research_network]).

Взаимоисключения: нет.

Прямые продолжения: MKN_free_science_network.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- `add_building_construction`: type = arms_factory; level = 1; instant_build = yes
- `add_tech_bonus`: bonus = 0.5; uses = 1; category = air_equipment

Полное определение:

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
    cost = 5
    prerequisite = {
        focus = MKN_communal_research_network
    }
    x = 10
    y = 14
}
```

### Сеть вольных институтов — `MKN_free_science_network`

EN: Network of Free Institutes.

Описание RU: Объединим политехникум и исследовательские коммуны в сеть вольных институтов. Вторая дополнительная группа доведёт общую научную мощность до пяти ячеек. Шестую даст Киевский научный обмен после интеграции Украины.

Описание EN: Unite the polytechnic and research communes into a network of free institutes. A second additional team raises scientific capacity to five slots. Kyiv Scientific Exchange will provide the sixth after Ukrainian integration.

Источник: `common/national_focus/MKN_horizons_focuses.txt:360`. Стоимость: 10 (70 дней). Координаты: x=10, y=15.

Предпосылки: (Артельные авиамастерские [MKN_workshop_airplane_artels]).

Взаимоисключения: нет.

Прямые продолжения: MKN_open_peer_review.

Обзор наград (может быть условным; точная область действия и ограничения — в коде):

- `add_tech_bonus`: bonus = 0.5; uses = 1; category = electronics

Полное определение:

```pdx
focus = {
    id = MKN_free_science_network
    icon = GFX_goal_generic_scientific_exchange
    cost = 10
    available_if_capitulated = no
    cancel_if_invalid = yes
    continue_if_invalid = no
    ai_will_do = {
        factor = 1
    }
    search_filters = {
        FOCUS_FILTER_POLITICAL
        FOCUS_FILTER_RESEARCH
    }
    x = 10
    available = {

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
                uses = 1
                category = electronics
            }
        }
    }
    y = 15
    prerequisite = {
        focus = MKN_workshop_airplane_artels
    }
}
```

## Баланс сил, решения, стартовая политика и автоматические события

Полные определения сохраняют стоимость, видимость, доступность, сроки миссий и периодичность. Стартовые идеи и переменные даны как контекст; не все описанные здесь эффекты выдаются политическими фокусами.

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

### `common/ideas/MKN_horizons_ideas.txt`

```pdx
ideas = {
    country = {
        MKN_military_reform_cooldown = {
            picture = generic_army_war_college
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {

            }
        }
        MKN_nabat_foreign_cells = {
            picture = generic_army_war_college
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                operative_slot = 1
                intel_network_gain_factor = 0.1
            }
        }
        MKN_hidden_workshops = {
            picture = generic_industrial_concern_1
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                production_speed_buildings_factor = -0.2
            }
            on_add = {
                if = {
                    limit = {
                        NOT = {
                            has_country_flag = MKN_hidden_workshops_active
                        }
                    }
                    set_country_flag = MKN_hidden_workshops_active
                    add_offsite_building = {
                        type = arms_factory
                        level = 3
                    }
                }
            }
            on_remove = {
                if = {
                    limit = {
                        has_country_flag = MKN_hidden_workshops_active
                    }
                    add_offsite_building = {
                        type = arms_factory
                        level = -3
                    }
                    clr_country_flag = MKN_hidden_workshops_active
                }
            }
        }
        MKN_evacuation_columns = {
            picture = generic_army_war_college
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                casualty_trickleback = 0.1
            }
        }
        MKN_black_vengeance_spirit = {
            picture = generic_army_war_college
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                army_core_attack_factor = 0.2
                army_speed_factor = 0.1
            }
        }
        MKN_open_laboratories = {
            picture = generic_industrial_concern_1
            allowed = {
                original_tag = MKN
            }
            removal_cost = -1
            modifier = {
                research_speed_factor = 0.05
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

### `common/bop/MKN_bop.txt`

```pdx
MKN_power_balance = {
    initial_value = 0
    left_side = MKN_military_command_side
    right_side = MKN_free_soviets_side
    decision_category = MKN_bop_decisions_category
    range = {
        id = MKN_bop_balanced
        min = -0.1
        max = 0.1
        modifier = {
            stability_factor = 0.05
            political_power_gain = 0.15
        }
    }
    side = {
        id = MKN_military_command_side
        icon = GFX_idea_MKN_viktor_belash
        range = {
            id = MKN_bop_total_military
            min = -1
            max = -0.6
            modifier = {
                army_attack_factor = 0.15
                planning_speed = 0.25
                stability_factor = -0.30
                consumer_goods_factor = 0.05
            }
        }
        range = {
            id = MKN_bop_militarist_lean
            min = -0.6
            max = -0.1
            modifier = {
                army_attack_factor = 0.075
                conscription = 0.02
                stability_factor = -0.15
            }
        }
    }
    side = {
        id = MKN_free_soviets_side
        icon = GFX_idea_volin
        range = {
            id = MKN_bop_soviet_lean
            min = 0.1
            max = 0.6
            modifier = {
                army_defence_factor = 0.10
                stability_factor = 0.10
                army_attack_factor = -0.05
            }
        }
        range = {
            id = MKN_bop_total_soviets
            min = 0.6
            max = 1
            modifier = {
                army_core_defence_factor = 0.25
                enemy_attrition = 0.20
                stability_factor = 0.25
                army_org_factor = -0.20
                war_support_factor = -0.15
            }
        }
    }
}
```

### `common/decisions/MKN_decisions.txt`

```pdx
MKN_bop_decisions_category = {
    MKN_empower_atamans = {
        icon = generic_army_support
        cost = 50
        days_re_enable = 60
        available = {
            NOT = {
                has_country_flag = MKN_bop_locked
            }
            power_balance_value = {
                id = MKN_power_balance
                value > -0.95
            }
        }
        complete_effect = {
            add_power_balance_value = {
                id = MKN_power_balance
                value = -0.15
                tooltip_side = MKN_military_command_side
            }
        }
        ai_will_do = {
            base = 0
            modifier = {
                add = 2
                has_completed_focus = MKN_military_takes_charge
            }
        }
    }
    MKN_convene_local_communes = {
        icon = generic_political_discourse
        cost = 50
        days_re_enable = 60
        available = {
            NOT = {
                has_country_flag = MKN_bop_locked
            }
            power_balance_value = {
                id = MKN_power_balance
                value < 0.95
            }
        }
        complete_effect = {
            add_power_balance_value = {
                id = MKN_power_balance
                value = 0.15
                tooltip_side = MKN_free_soviets_side
            }
        }
        ai_will_do = {
            base = 0
            modifier = {
                add = 2
                has_completed_focus = MKN_triumph_of_free_soviets
            }
        }
    }
    MKN_joint_defence_congress = {
        icon = generic_political_discourse
        cost = 50
        days_re_enable = 90
        available = {
            NOT = {
                has_country_flag = MKN_bop_locked
            }
            OR = {
                power_balance_value = {
                    id = MKN_power_balance
                    value < -0.1
                }
                power_balance_value = {
                    id = MKN_power_balance
                    value > 0.1
                }
            }
        }
        complete_effect = {
            if = {
                limit = {
                    power_balance_value = {
                        id = MKN_power_balance
                        value < 0
                    }
                }
                add_power_balance_value = {
                    id = MKN_power_balance
                    value = 0.10
                    tooltip_side = MKN_free_soviets_side
                }
            }
            else = {
                add_power_balance_value = {
                    id = MKN_power_balance
                    value = -0.10
                    tooltip_side = MKN_military_command_side
                }
            }
        }
        ai_will_do = {
            base = 0
        }
    }
    MKN_tachanka_patrols = {
        icon = generic_army_support
        cost = 45
        days_re_enable = 150
        visible = {
            has_power_balance = {
                id = MKN_power_balance
            }
            NOT = {
                has_country_flag = MKN_bop_locked
            }
        }
        available = {
            has_power_balance = {
                id = MKN_power_balance
            }
            NOT = {
                has_country_flag = MKN_bop_locked
            }
            power_balance_value = {
                id = MKN_power_balance
                value > -1
            }
            NOT = {
                has_idea = MKN_mobile_patrols
            }
        }
        complete_effect = {
            if = {
                limit = {
                    has_power_balance = {
                        id = MKN_power_balance
                    }
                    NOT = {
                        has_country_flag = MKN_bop_locked
                    }
                    power_balance_value = {
                        id = MKN_power_balance
                        value > -1
                    }
                    NOT = {
                        has_idea = MKN_mobile_patrols
                    }
                }
                add_power_balance_value = {
                    id = MKN_power_balance
                    value = -0.10
                    tooltip_side = MKN_military_command_side
                }
                add_stability = -0.05
                add_war_support = 0.05
                add_timed_idea = {
                    idea = MKN_mobile_patrols
                    days = 90
                }
            }
            else = {
                add_political_power = 45
            }
        }
        ai_will_do = {
            factor = 0.5
        }
    }
    MKN_communal_seed_reserves = {
        icon = generic_industry
        cost = 40
        days_re_enable = 180
        visible = {
            has_power_balance = {
                id = MKN_power_balance
            }
            NOT = {
                has_country_flag = MKN_bop_locked
            }
        }
        available = {
            has_power_balance = {
                id = MKN_power_balance
            }
            NOT = {
                has_country_flag = MKN_bop_locked
            }
            power_balance_value = {
                id = MKN_power_balance
                value < 1
            }
            NOT = {
                has_idea = MKN_seed_cooperatives
            }
        }
        complete_effect = {
            if = {
                limit = {
                    has_power_balance = {
                        id = MKN_power_balance
                    }
                    NOT = {
                        has_country_flag = MKN_bop_locked
                    }
                    power_balance_value = {
                        id = MKN_power_balance
                        value < 1
                    }
                    NOT = {
                        has_idea = MKN_seed_cooperatives
                    }
                }
                add_power_balance_value = {
                    id = MKN_power_balance
                    value = 0.10
                    tooltip_side = MKN_free_soviets_side
                }
                add_war_support = -0.05
                add_timed_idea = {
                    idea = MKN_seed_cooperatives
                    days = 120
                }
            }
            else = {
                add_political_power = 40
            }
        }
        ai_will_do = {
            factor = 0.5
        }
    }
    MKN_requisition_workshop_shifts = {
        icon = generic_industry
        cost = 50
        days_re_enable = 180
        visible = {
            has_power_balance = {
                id = MKN_power_balance
            }
            NOT = {
                has_country_flag = MKN_bop_locked
            }
        }
        available = {
            has_power_balance = {
                id = MKN_power_balance
            }
            NOT = {
                has_country_flag = MKN_bop_locked
            }
            power_balance_value = {
                id = MKN_power_balance
                value > -1
            }
            NOT = {
                has_idea = MKN_extra_workshop_shifts
            }
        }
        complete_effect = {
            if = {
                limit = {
                    has_power_balance = {
                        id = MKN_power_balance
                    }
                    NOT = {
                        has_country_flag = MKN_bop_locked
                    }
                    power_balance_value = {
                        id = MKN_power_balance
                        value > -1
                    }
                    NOT = {
                        has_idea = MKN_extra_workshop_shifts
                    }
                }
                add_power_balance_value = {
                    id = MKN_power_balance
                    value = -0.05
                    tooltip_side = MKN_military_command_side
                }
                add_stability = -0.05
                add_timed_idea = {
                    idea = MKN_extra_workshop_shifts
                    days = 120
                }
            }
            else = {
                add_political_power = 50
            }
        }
        ai_will_do = {
            factor = 0.5
        }
    }
    MKN_reconcile_village_and_front = {
        icon = generic_political_discourse
        cost = 60
        days_re_enable = 150
        visible = {
            has_power_balance = {
                id = MKN_power_balance
            }
            NOT = {
                has_country_flag = MKN_bop_locked
            }
        }
        available = {
            has_power_balance = {
                id = MKN_power_balance
            }
            NOT = {
                has_country_flag = MKN_bop_locked
            }
            OR = {
                power_balance_value = {
                    id = MKN_power_balance
                    value < -0.10
                }
                power_balance_value = {
                    id = MKN_power_balance
                    value > 0.10
                }
            }
            NOT = {
                has_idea = MKN_recallable_front_delegates
            }
        }
        complete_effect = {
            if = {
                limit = {
                    has_power_balance = {
                        id = MKN_power_balance
                    }
                    NOT = {
                        has_country_flag = MKN_bop_locked
                    }
                    OR = {
                        power_balance_value = {
                            id = MKN_power_balance
                            value < -0.10
                        }
                        power_balance_value = {
                            id = MKN_power_balance
                            value > 0.10
                        }
                    }
                    NOT = {
                        has_idea = MKN_recallable_front_delegates
                    }
                }
                if = {
                    limit = {
                        power_balance_value = {
                            id = MKN_power_balance
                            value < 0
                        }
                    }
                    add_power_balance_value = {
                        id = MKN_power_balance
                        value = 0.10
                        tooltip_side = MKN_free_soviets_side
                    }
                }
                else = {
                    add_power_balance_value = {
                        id = MKN_power_balance
                        value = -0.10
                        tooltip_side = MKN_military_command_side
                    }
                }
                add_stability = 0.05
                army_experience = 10
                add_timed_idea = {
                    idea = MKN_recallable_front_delegates
                    days = 90
                }
            }
            else = {
                add_political_power = 60
            }
        }
        ai_will_do = {
            factor = 0.5
        }
    }
}
MKN_succession_crisis_category = {
    MKN_civil_war_timer_mission = {
        icon = generic_ignite_civil_war
        allowed = {
            tag = MKN
        }
        activation = {
            always = no
        }
        available = {
            always = no
        }
        visible = {
            has_country_flag = MKN_crisis_active
        }
        cancel_if_not_visible = yes
        fire_only_once = yes
        is_good = no
        days_mission_timeout = 180
        timeout_effect = {
            if = {
                limit = {
                    has_country_flag = MKN_crisis_active
                    NOT = {
                        has_country_flag = MKN_crisis_settled
                    }
                    NOT = {
                        has_country_flag = MKN_collapse_started
                    }
                }
                country_event = {
                    id = mkn_crisis.100
                }
            }
        }
    }
}
MKN_steppe_operations_category = {
    MKN_recruit_international_volunteers = {
        icon = generic_army_support
        cost = 50
        days_re_enable = 90
        visible = {
            has_completed_focus = MKN_black_international
        }
        available = {
            has_government = democratic
            has_manpower < 100000
        }
        complete_effect = {
            add_manpower = 5000
            add_equipment_to_stockpile = {
                type = infantry_equipment_0
                amount = 500
                producer = MKN
            }
        }
        ai_will_do = {
            base = 1
        }
    }
    MKN_strike_networks = {
        icon = generic_political_discourse
        cost = 75
        days_re_enable = 120
        visible = {
            has_completed_focus = MKN_propaganda_by_deed
        }
        target_trigger = {
            is_neighbor_of = ROOT
            NOT = {
                original_tag = MKN
            }
        }
        available = {
            FROM = {
                is_subject = no
                NOT = {
                    has_idea = MKN_neighbor_strikes
                }
            }
        }
        complete_effect = {
            FROM = {
                country_event = {
                    id = mkn_crisis.30
                }
            }
        }
        ai_will_do = {
            base = 1
        }
    }
    MKN_scorched_railways = {
        icon = generic_guerilla_base
        cost = 25
        days_re_enable = 90
        visible = {
            has_completed_focus = MKN_railway_sabotage
        }
        state_target = yes
        target_trigger = {
            FROM = {
                is_owned_by = ROOT
                is_controlled_by = ROOT
                any_neighbor_state = {
                    controller = {
                        has_war_with = ROOT
                    }
                }
                infrastructure > 0
            }
        }
        available = {
            has_war = yes
        }
        complete_effect = {
            FROM = {
                damage_building = {
                    type = infrastructure
                    damage = 2
                    repair_speed_modifier = -0.5
                }
                damage_building = {
                    type = rail_way
                    damage = 2
                    repair_speed_modifier = -0.5
                }
            }
        }
        ai_will_do = {
            base = 0
        }
    }
    MKN_clash_LTB = {
        icon = generic_guerilla_base
        cost = 50
        days_re_enable = 120
        state_target = yes
        visible = {
            has_completed_focus = MKN_black_expansionism
            LTB = {
                exists = yes
            }
        }
        target_trigger = {
            FROM = {
                is_owned_and_controlled_by = LTB
                any_neighbor_state = {
                    is_owned_and_controlled_by = ROOT
                }
            }
        }
        available = {
            has_war = no
            NOT = {
                has_country_flag = MKN_border_clash_active
            }
            LTB = {
                has_war = no
                NOT = {
                    is_in_faction_with = ROOT
                }
            }
            FROM = {
                has_border_war = no
            }
            any_owned_state = {
                is_controlled_by = ROOT
                has_border_war = no
                any_neighbor_state = {
                    state = FROM
                }
            }
        }
        complete_effect = {
            set_country_flag = MKN_border_clash_active
            random_owned_state = {
                limit = {
                    is_controlled_by = ROOT
                    has_border_war = no
                    any_neighbor_state = {
                        state = FROM
                    }
                }
                save_event_target_as = MKN_border_attacker
            }
            start_border_war = {
                change_state_after_war = yes
                minimum_duration_in_days = 30
                attacker = {
                    state = event_target:MKN_border_attacker
                    num_provinces = 1
                    on_win = mkn_crisis.50
                    on_lose = mkn_crisis.51
                    on_cancel = mkn_crisis.51
                }
                defender = {
                    state = FROM
                    num_provinces = 1
                    on_win = mkn_crisis.51
                    on_lose = mkn_crisis.50
                    on_cancel = mkn_crisis.51
                }
            }
        }
        ai_will_do = {
            base = 1
        }
    }
    MKN_clash_SOV = {
        icon = generic_guerilla_base
        cost = 50
        days_re_enable = 120
        state_target = yes
        visible = {
            has_completed_focus = MKN_black_expansionism
            SOV = {
                exists = yes
            }
        }
        target_trigger = {
            FROM = {
                is_owned_and_controlled_by = SOV
                any_neighbor_state = {
                    is_owned_and_controlled_by = ROOT
                }
            }
        }
        available = {
            has_war = no
            NOT = {
                has_country_flag = MKN_border_clash_active
            }
            SOV = {
                has_war = no
                NOT = {
                    is_in_faction_with = ROOT
                }
            }
            FROM = {
                has_border_war = no
            }
            any_owned_state = {
                is_controlled_by = ROOT
                has_border_war = no
                any_neighbor_state = {
                    state = FROM
                }
            }
        }
        complete_effect = {
            set_country_flag = MKN_border_clash_active
            random_owned_state = {
                limit = {
                    is_controlled_by = ROOT
                    has_border_war = no
                    any_neighbor_state = {
                        state = FROM
                    }
                }
                save_event_target_as = MKN_border_attacker
            }
            start_border_war = {
                change_state_after_war = yes
                minimum_duration_in_days = 30
                attacker = {
                    state = event_target:MKN_border_attacker
                    num_provinces = 1
                    on_win = mkn_crisis.50
                    on_lose = mkn_crisis.51
                    on_cancel = mkn_crisis.51
                }
                defender = {
                    state = FROM
                    num_provinces = 1
                    on_win = mkn_crisis.51
                    on_lose = mkn_crisis.50
                    on_cancel = mkn_crisis.51
                }
            }
        }
        ai_will_do = {
            base = 1
        }
    }
    MKN_renew_supply_talks = {
        icon = generic_political_discourse
        cost = 50
        days_re_enable = 90
        visible = {
            has_completed_focus = MKN_embassy_to_kharkov
            NOT = {
                has_country_flag = MKN_soviet_trade_accepted
            }
        }
        available = {
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
            NOT = {
                has_country_flag = MKN_plenum_pending
            }
        }
        complete_effect = {
            SOV = {
                country_event = {
                    id = mkn_crisis.20
                    days = 1
                }
            }
        }
        ai_will_do = {
            base = 5
        }
    }
    MKN_renew_front_talks = {
        icon = generic_political_discourse
        cost = 50
        days_re_enable = 90
        visible = {
            has_completed_focus = MKN_anti_imperialist_front
            is_in_faction = no
        }
        available = {
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
            NOT = {
                has_country_flag = MKN_plenum_pending
            }
        }
        complete_effect = {
            SOV = {
                country_event = {
                    id = mkn_crisis.23
                    days = 1
                }
            }
        }
        ai_will_do = {
            base = 5
        }
    }
}
MKN_soviet_intervention_category = {
    MKN_soviet_intervention_mission = {
        icon = generic_ignite_civil_war
        allowed = {
            original_tag = MKN
        }
        activation = {
            always = no
        }
        available = {
            always = no
        }
        visible = {
            has_country_flag = MKN_collapse_started
            has_country_flag = MKN_collapse_participant
            has_country_flag = MKN_soviet_intervention_initialized
            NOT = {
                has_country_flag = MKN_soviet_intervention_resolved
            }
            NOT = {
                has_global_flag = MKN_soviet_intervention_triggered
            }
            NOT = {
                has_global_flag = MKN_collapse_reunified
            }
        }
        cancel_if_not_visible = yes
        fire_only_once = yes
        selectable_mission = no
        is_good = no
        days_mission_timeout = 100
        cancel_trigger = {
            OR = {
                check_variable = {
                    num_owned_states < 1
                }
                has_country_flag = MKN_soviet_intervention_resolved
                has_global_flag = MKN_soviet_intervention_triggered
                has_global_flag = MKN_collapse_reunified
                NOT = {
                    any_other_country = {
                        original_tag = MKN
                        has_country_flag = MKN_collapse_started
                        has_country_flag = MKN_collapse_participant
                        check_variable = {
                            num_owned_states > 0
                        }
                    }
                }
            }
        }
        cancel_effect = {
            MKN_repair_soviet_intervention = yes
        }
        timeout_effect = {
            MKN_request_soviet_intervention = yes
        }
    }
}
```

### `common/decisions/MKN_bop_decisions.txt`

```pdx

```

### `common/decisions/MKN_international_decisions.txt`

```pdx
mkn_black_international_category = {
    MKN_welcome_cnt_fai_exiles = {
        icon = generic_army_support
        cost = 50
        fire_only_once = yes
        available = {
            NOT = {
                has_country_flag = MKN_cnt_fai_exiles_welcomed
            }
            has_completed_focus = MKN_black_international
        }
        complete_effect = {
            if = {
                limit = {
                    NOT = {
                        has_country_flag = MKN_cnt_fai_exiles_welcomed
                    }
                    has_completed_focus = MKN_black_international
                }
                set_country_flag = MKN_cnt_fai_exiles_welcomed
                if = {
                    limit = {
                        NOT = {
                            has_character = MKN_buenaventura_durruti
                        }
                    }
                    recruit_character = MKN_buenaventura_durruti
                }
            }
            else = {
                add_political_power = 50
            }
        }
        ai_will_do = {
            factor = 1
        }
    }
    MKN_harbor_spartacist_engineers = {
        icon = generic_industry
        cost = 50
        fire_only_once = yes
        available = {
            NOT = {
                has_country_flag = MKN_spartacist_engineers_welcomed
            }
            has_completed_focus = MKN_black_international
        }
        complete_effect = {
            if = {
                limit = {
                    NOT = {
                        has_country_flag = MKN_spartacist_engineers_welcomed
                    }
                    has_completed_focus = MKN_black_international
                }
                set_country_flag = MKN_spartacist_engineers_welcomed
                add_timed_idea = {
                    idea = MKN_spartacist_engineers
                    days = 180
                }
            }
            else = {
                add_political_power = 50
            }
        }
        ai_will_do = {
            factor = 1
        }
    }
    MKN_accept_italian_mechanics = {
        icon = generic_research
        cost = 50
        fire_only_once = yes
        available = {
            NOT = {
                has_country_flag = MKN_italian_mechanics_welcomed
            }
            has_completed_focus = MKN_black_international
        }
        complete_effect = {
            if = {
                limit = {
                    NOT = {
                        has_country_flag = MKN_italian_mechanics_welcomed
                    }
                    has_completed_focus = MKN_black_international
                }
                set_country_flag = MKN_italian_mechanics_welcomed
                add_tech_bonus = {
                    name = MKN_italian_mechanics_bonus
                    bonus = 1.0
                    uses = 1
                    category = motorized_equipment
                }
            }
            else = {
                add_political_power = 50
            }
        }
        ai_will_do = {
            factor = 1
        }
    }
    MKN_smuggle_kronstadt_sailors = {
        icon = generic_naval
        cost = 50
        fire_only_once = yes
        available = {
            NOT = {
                has_country_flag = MKN_kronstadt_sailors_welcomed
            }
            has_completed_focus = MKN_black_international
        }
        complete_effect = {
            if = {
                limit = {
                    NOT = {
                        has_country_flag = MKN_kronstadt_sailors_welcomed
                    }
                    has_completed_focus = MKN_black_international
                }
                set_country_flag = MKN_kronstadt_sailors_welcomed
                add_manpower = 10000
                navy_experience = 15
            }
            else = {
                add_political_power = 50
            }
        }
        ai_will_do = {
            factor = 1
        }
    }
}
```

### `common/decisions/MKN_foreign_decisions.txt`

```pdx
mkn_black_international_category = {
    MKN_offer_workshop_exchange = {
        icon = generic_industry
        targets = {
            LTB
            AUS
            GER
            TUR
            HUN
        }
        visible = {
            has_completed_focus = MKN_workers_corridors
        }
        target_trigger = {
            FROM = {
                exists = yes
                OR = {
                    tag = LTB
                    tag = AUS
                    tag = GER
                    tag = TUR
                    tag = HUN
                }
            }
        }
        available = {
            has_capitulated = no
            FROM = {
                exists = yes
                is_subject = no
                has_capitulated = no
                NOT = {
                    has_war_with = ROOT
                }
                NOT = {
                    has_country_flag = MKN_workshop_exchange_pending
                }
                NOT = {
                    has_country_flag = MKN_workshop_exchange_agreed
                }
            }
        }
        cost = 50
        days_re_enable = 180
        complete_effect = {
            if = {
                limit = {
                    has_completed_focus = MKN_workers_corridors
                    has_capitulated = no
                    FROM = {
                        exists = yes
                        is_subject = no
                        has_capitulated = no
                        NOT = {
                            has_war_with = ROOT
                        }
                        NOT = {
                            has_country_flag = MKN_workshop_exchange_pending
                        }
                        NOT = {
                            has_country_flag = MKN_workshop_exchange_agreed
                        }
                    }
                }
                FROM = {
                    set_country_flag = {
                        flag = MKN_workshop_exchange_pending
                        days = 30
                    }
                    country_event = {
                        id = mkn_foreign.1
                        days = 1
                    }
                }
                custom_effect_tooltip = MKN_workshop_exchange_offer_tt
            }
            else = {
                add_political_power = 50
            }
        }
        ai_will_do = {
            factor = 1
            modifier = {
                factor = 0
                has_country_flag = MKN_crisis_active
            }
            modifier = {
                factor = 0
                has_country_flag = mkn_frontier_conflict_active
                NOT = {
                    has_country_flag = mkn_ukr_frontier_concluded
                }
                check_variable = {
                    mkn_ukr_escalation_level > 1
                }
            }
        }
    }
}
```

### `common/decisions/MKN_horizons_decisions.txt`

```pdx
MKN_horizons_international_category = {
    MKN_sponsor_litbel_strike = {
        icon = generic_political_actions
        targets = {
            LTB
        }
        visible = {
            has_completed_focus = MKN_agitation_in_litbel
        }
        target_trigger = {
            FROM = {
                tag = LTB
                exists = yes
            }
        }
        available = {
            MKN_horizons_hostile_target = yes
            has_capitulated = no
            FROM = {
                stability > 0.2
                any_owned_state = {
                    is_controlled_by = PREV
                    arms_factory > 0
                }
            }
        }
        cost = 50
        custom_cost_trigger = {
            has_equipment = {
                infantry_equipment > 199
            }
        }
        custom_cost_text = MKN_horizons_200_rifles
        days_remove = 45
        days_re_enable = 180
        complete_effect = {
            add_equipment_to_stockpile = {
                type = infantry_equipment
                amount = -200
            }
        }
        cancel_trigger = {
            OR = {
                has_capitulated = yes
                NOT = {
                    MKN_horizons_hostile_target = yes
                }
            }
        }
        cancel_effect = {
            add_political_power = 50
            add_equipment_to_stockpile = {
                type = infantry_equipment_0
                amount = 200
            }
        }
        remove_effect = {
            if = {
                limit = {
                    MKN_horizons_hostile_target = yes
                    has_capitulated = no
                }
                FROM = {
                    add_stability = -0.05
                    random_owned_controlled_state = {
                        limit = {
                            arms_factory > 0
                        }
                        damage_building = {
                            type = arms_factory
                            damage = 1
                        }
                    }
                }
            }
            else = {
                add_political_power = 50
                add_equipment_to_stockpile = {
                    type = infantry_equipment_0
                    amount = 200
                }
            }
        }
        ai_will_do = {
            factor = 1
        }
    }
    MKN_support_galician_unions = {
        icon = generic_political_actions
        state_target = yes
        visible = {
            has_completed_focus = MKN_galician_peasants
        }
        target_trigger = {
            FROM = {
                OR = {
                    state = 80
                    state = 89
                    state = 90
                }
                is_owned_and_controlled_by = AUS
            }
        }
        available = {
            has_capitulated = no
            MKN_horizons_hostile_austria = yes
            AUS = {
                exists = yes
                has_war = no
            }
            FROM = {
                is_owned_and_controlled_by = AUS
                NOT = {
                    has_state_flag = MKN_rural_unions_armed
                }
            }
        }
        cost = 50
        custom_cost_trigger = {
            has_equipment = {
                infantry_equipment > 199
            }
        }
        custom_cost_text = MKN_horizons_200_rifles
        days_remove = 45
        days_re_enable = 180
        complete_effect = {
            add_equipment_to_stockpile = {
                type = infantry_equipment
                amount = -200
            }
        }
        cancel_trigger = {
            OR = {
                has_capitulated = yes
                NOT = {
                    MKN_horizons_hostile_austria = yes
                }
                NOT = {
                    FROM = {
                        is_owned_and_controlled_by = AUS
                    }
                }
                AUS = {
                    has_war = yes
                }
            }
        }
        cancel_effect = {
            add_political_power = 50
            add_equipment_to_stockpile = {
                type = infantry_equipment_0
                amount = 200
            }
        }
        remove_effect = {
            if = {
                limit = {
                    has_capitulated = no
                    MKN_horizons_hostile_austria = yes
                    AUS = {
                        exists = yes
                        has_war = no
                    }
                    FROM = {
                        is_owned_and_controlled_by = AUS
                    }
                }
                FROM = {
                    set_state_flag = MKN_rural_unions_armed
                    damage_building = {
                        type = infrastructure
                        damage = 1
                    }
                }
                AUS = {
                    add_stability = -0.05
                }
            }
            else = {
                add_political_power = 50
                add_equipment_to_stockpile = {
                    type = infantry_equipment_0
                    amount = 200
                }
            }
        }
        ai_will_do = {
            factor = 1
        }
    }
    MKN_galician_border_action = {
        icon = generic_army_support
        state_target = yes
        visible = {
            has_completed_focus = MKN_galician_peasants
        }
        target_trigger = {
            FROM = {
                OR = {
                    state = 80
                    state = 89
                    state = 90
                }
                is_owned_and_controlled_by = AUS
            }
        }
        available = {
            MKN_horizons_austrian_border_target = yes
            FROM = {
                has_state_flag = MKN_rural_unions_armed
            }
            NOT = {
                has_country_flag = MKN_galician_border_active
            }
        }
        cost = 100
        days_re_enable = 180
        complete_effect = {
            if = {
                limit = {
                    MKN_horizons_austrian_border_target = yes
                    FROM = {
                        has_state_flag = MKN_rural_unions_armed
                    }
                }
                set_country_flag = {
                    flag = MKN_galician_border_active
                    days = 180
                }
                FROM = {
                    clr_state_flag = MKN_rural_unions_armed
                }
                random_owned_controlled_state = {
                    limit = {
                        has_border_war = no
                        any_neighbor_state = {
                            state = FROM
                        }
                    }
                    save_event_target_as = MKN_galician_attacking_state
                }
                start_border_war = {
                    change_state_after_war = no
                    minimum_duration_in_days = 30
                    attacker = {
                        state = event_target:MKN_galician_attacking_state
                        num_provinces = 1
                        on_win = mkn_horizons.10
                        on_lose = mkn_horizons.11
                        on_cancel = mkn_horizons.11
                    }
                    defender = {
                        state = FROM
                        num_provinces = 1
                    }
                }
            }
            else = {
                add_political_power = 100
            }
        }
        ai_will_do = {
            factor = 1
        }
    }
    MKN_found_black_international = {
        icon = generic_political_actions
        visible = {
            has_completed_focus = MKN_global_syndicalist_pact
            NOT = {
                has_country_flag = MKN_black_international_founded
            }
        }
        available = {
            is_subject = no
            is_in_faction = no
            has_capitulated = no
        }
        cost = 100
        fire_only_once = yes
        complete_effect = {
            set_rule = {
                can_create_factions = yes
            }
            create_faction = MKN_horizons_black_international
            set_country_flag = MKN_black_international_founded
        }
        ai_will_do = {
            factor = 1
        }
    }
    MKN_invite_free_councils = {
        icon = generic_political_actions
        target_root_trigger = {
            has_completed_focus = MKN_global_syndicalist_pact
            is_faction_leader = yes
            has_country_flag = MKN_black_international_founded
        }
        visible = {
            has_completed_focus = MKN_global_syndicalist_pact
        }
        target_trigger = {
            FROM = {
                NOT = {
                    tag = MKN
                }
                exists = yes
                is_subject = no
                is_in_faction = no
                OR = {
                    has_government = democratic
                    has_government = communism
                }
                NOT = {
                    has_war_with = ROOT
                }
            }
        }
        available = {
            FROM = {
                NOT = {
                    has_country_flag = MKN_congress_invitation_pending
                }
            }
        }
        cost = 50
        days_re_enable = 180
        complete_effect = {
            FROM = {
                set_country_flag = {
                    flag = MKN_congress_invitation_pending
                    days = 30
                }
                country_event = {
                    id = mkn_horizons.1
                    days = 1
                }
            }
        }
        ai_will_do = {
            factor = 1
        }
    }
}
MKN_economic_congress_category = {
    MKN_huliaipole_reactor_project = {
        icon = decision_generic_construction
        state_target = yes
        target_array = ROOT.owned_states
        target_trigger = {
            FROM = {
                state = 1082
            }
        }
        visible = {
            has_completed_focus = MKN_the_absolute_argument
            NOT = {
                has_country_flag = MKN_huliaipole_reactor_completed
            }
        }
        available = {
            MKN_horizons_reactor_site = yes
            num_of_civilian_factories_available_for_projects > 4
            NOT = {
                has_country_flag = MKN_huliaipole_reactor_active
            }
        }
        cost = 100
        days_remove = 90
        modifier = {
            civilian_factory_use = 5
        }
        complete_effect = {
            set_country_flag = MKN_huliaipole_reactor_active
        }
        cancel_trigger = {
            NOT = {
                MKN_horizons_reactor_site = yes
            }
        }
        cancel_effect = {
            add_political_power = 100
            clr_country_flag = MKN_huliaipole_reactor_active
        }
        remove_effect = {
            if = {
                limit = {
                    MKN_horizons_reactor_site = yes
                    NOT = {
                        has_country_flag = MKN_huliaipole_reactor_completed
                    }
                }
                FROM = {
                    add_building_construction = {
                        type = nuclear_reactor
                        level = 1
                        instant_build = yes
                    }
                }
                set_country_flag = MKN_huliaipole_reactor_completed
            }
            else = {
                add_political_power = 100
            }
            clr_country_flag = MKN_huliaipole_reactor_active
        }
        ai_will_do = {
            factor = 1
        }
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
    army_non_core_attack_factor = MKN_army_army_non_core_attack_factor
    army_non_core_defence_factor = MKN_army_army_non_core_defence_factor
    army_org_regain = MKN_army_army_org_regain
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
        MKN_army_army_non_core_attack_factor = 0
    }
    set_variable = {
        MKN_army_army_non_core_defence_factor = 0
    }
    set_variable = {
        MKN_army_army_org_regain = 0
    }
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
    MKN_rebuild_horizons_service_stats = yes
    if = {
        limit = {
            has_completed_focus = MKN_column_medical_service
        }
        add_to_variable = {
            MKN_army_casualty_trickleback = 0.05
        }
        add_to_variable = {
            MKN_army_land_reinforce_rate = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_air_warning_network_focus
        }
        add_to_variable = {
            MKN_air_air_interception_detect_factor = 0.1
        }
        add_to_variable = {
            MKN_air_air_home_defence_factor = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_convoy_control_office
        }
        add_to_variable = {
            MKN_navy_convoy_escort_efficiency = 0.1
        }
        add_to_variable = {
            MKN_navy_navy_fuel_consumption_factor = -0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_raider_signal_stations
        }
        add_to_variable = {
            MKN_navy_naval_detection = 0.1
        }
        add_to_variable = {
            MKN_navy_naval_coordination = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_underway_refit_artels
        }
        add_to_variable = {
            MKN_navy_naval_ship_recovery_chance_factor = 0.1
        }
        add_to_variable = {
            MKN_navy_naval_retreat_speed = 0.05
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

### `common/ai_strategy_plans/MKN_historical.txt`

```pdx
MKN_fascism_plan = {
    name = MKN_AI_FASCISM
    desc = MKN_AI_FASCISM_DESC
    allowed = {
        original_tag = MKN
    }
    enable = {
        has_focus_tree = MKN_focus
        has_country_flag = MKN_ai_route_fascism
        has_country_flag = MKN_crisis_enabled
    }
    abort = {
        OR = {
            has_country_flag = MKN_collapse_started
            has_country_flag = MKN_crisis_legacy_settled
        }
    }
    ai_national_focuses = {
        MKN_congress_1936
        MKN_question_of_supply
        MKN_question_of_discipline
        MKN_military_takes_charge
        MKN_arrest_demagogues
        MKN_abolish_election_of_commanders
        MKN_militarize_communes
        MKN_standardize_workshops
        MKN_iron_fist_trains
        MKN_black_expansionism
        MKN_the_black_horde
        MKN_dneprostroi
        MKN_dnieper_audit
        MKN_southern_resources
        MKN_steppe_industrial_giants
        MKN_zaporizhstal
        MKN_worker_battalions
        MKN_dnieper_logistics_hub
        MKN_steppe_electrification
        MKN_production_cycles
        MKN_steel_volnitsa
    }
    weight = {
        factor = 100
    }
    focus_factors = {
        MKN_triumph_of_free_soviets = 0
        MKN_peasant_delegates = 0
        MKN_emergency_revkom = 0
    }
}
MKN_democratic_plan = {
    name = MKN_AI_DEMOCRATIC
    desc = MKN_AI_DEMOCRATIC_DESC
    allowed = {
        original_tag = MKN
    }
    enable = {
        has_focus_tree = MKN_focus
        has_country_flag = MKN_ai_route_democratic
        has_country_flag = MKN_crisis_enabled
    }
    abort = {
        OR = {
            has_country_flag = MKN_collapse_started
            has_country_flag = MKN_crisis_legacy_settled
        }
    }
    ai_national_focuses = {
        MKN_congress_1936
        MKN_question_of_supply
        MKN_question_of_discipline
        MKN_triumph_of_free_soviets
        MKN_pact_of_free_communes
        MKN_abolish_general_staff
        MKN_arms_to_the_people
        MKN_propaganda_by_deed
        MKN_black_international
        MKN_autonomous_rail_crews
        MKN_beacon_of_statelessness
        MKN_free_cooperatives
        MKN_artel_register
        MKN_steppe_markets
        MKN_mobile_workshops
        MKN_rifle_concern
        MKN_grain_exchanges
        MKN_freight_logistics
        MKN_workshop_standards
        MKN_field_schools
        MKN_communal_compact
    }
    weight = {
        factor = 100
    }
    focus_factors = {
        MKN_military_takes_charge = 0
        MKN_peasant_delegates = 0
        MKN_emergency_revkom = 0
    }
}
MKN_neutrality_plan = {
    name = MKN_AI_NEUTRALITY
    desc = MKN_AI_NEUTRALITY_DESC
    allowed = {
        original_tag = MKN
    }
    enable = {
        has_focus_tree = MKN_focus
        has_country_flag = MKN_ai_route_neutrality
        has_country_flag = MKN_crisis_enabled
    }
    abort = {
        OR = {
            has_country_flag = MKN_collapse_started
            has_country_flag = MKN_crisis_legacy_settled
        }
    }
    ai_national_focuses = {
        MKN_congress_1936
        MKN_question_of_supply
        MKN_question_of_discipline
        MKN_peasant_delegates
        MKN_grain_ultimatum
        MKN_sever_urban_ties
        MKN_every_farm_a_fortress
        MKN_steppe_snipers
        MKN_railway_sabotage
        MKN_cavalry_ambush
        MKN_impregnable_granary
        MKN_free_cooperatives
        MKN_artel_register
        MKN_steppe_markets
        MKN_mobile_workshops
        MKN_rifle_concern
        MKN_grain_exchanges
        MKN_freight_logistics
        MKN_workshop_standards
        MKN_field_schools
        MKN_communal_compact
    }
    weight = {
        factor = 100
    }
    focus_factors = {
        MKN_military_takes_charge = 0
        MKN_triumph_of_free_soviets = 0
        MKN_emergency_revkom = 0
    }
}
MKN_historical = {
    name = MKN_AI_COMMUNISM
    desc = MKN_AI_COMMUNISM_DESC
    allowed = {
        original_tag = MKN
    }
    enable = {
        has_focus_tree = MKN_focus
        has_country_flag = MKN_ai_route_communism
        has_country_flag = MKN_crisis_enabled
    }
    abort = {
        OR = {
            has_country_flag = MKN_collapse_started
            has_country_flag = MKN_crisis_legacy_settled
        }
    }
    ai_national_focuses = {
        MKN_congress_1936
        MKN_question_of_supply
        MKN_question_of_discipline
        MKN_emergency_revkom
        MKN_purge_irreconcilables
        MKN_embassy_to_kharkov
        MKN_integrate_steel_lines
        MKN_red_military_specialists
        MKN_tractors_for_grain
        MKN_anti_imperialist_front
        MKN_the_fatal_plenum
        MKN_dneprostroi
        MKN_dnieper_audit
        MKN_southern_resources
        MKN_steppe_industrial_giants
        MKN_zaporizhstal
        MKN_worker_battalions
        MKN_dnieper_logistics_hub
        MKN_steppe_electrification
        MKN_production_cycles
        MKN_steel_volnitsa
    }
    weight = {
        factor = 100
    }
    focus_factors = {
        MKN_military_takes_charge = 0
        MKN_triumph_of_free_soviets = 0
        MKN_peasant_delegates = 0
    }
}
```

### `common/scripted_localisation/MKN_ideology_names.txt`

```pdx
defined_text = {
    name = GetNwwMknFascismName
    text = {
        trigger = {
            tag = MKN
        }
        localization_key = MKN_anarcho_militarism
    }
    text = {
        localization_key = NWW_default_fascism
    }
}
defined_text = {
    name = GetNwwMknDemocraticName
    text = {
        trigger = {
            tag = MKN
        }
        localization_key = MKN_anarcho_communism
    }
    text = {
        localization_key = NWW_default_democratic
    }
}
defined_text = {
    name = GetNwwMknNeutralityName
    text = {
        trigger = {
            tag = MKN
        }
        localization_key = MKN_agrarian_isolationism
    }
    text = {
        localization_key = NWW_default_neutrality
    }
}
defined_text = {
    name = GetNwwMknCommunismName
    text = {
        trigger = {
            tag = MKN
        }
        localization_key = MKN_state_socialism
    }
    text = {
        localization_key = NWW_default_communism
    }
}
defined_text = {
    name = GetNwwMknFascismNameNoun
    text = {
        trigger = {
            tag = MKN
        }
        localization_key = MKN_anarcho_militarism
    }
    text = {
        localization_key = NWW_default_fascism_noun
    }
}
defined_text = {
    name = GetNwwMknDemocraticNameNoun
    text = {
        trigger = {
            tag = MKN
        }
        localization_key = MKN_anarcho_communism
    }
    text = {
        localization_key = NWW_default_democratic_noun
    }
}
defined_text = {
    name = GetNwwMknNeutralityNameNoun
    text = {
        trigger = {
            tag = MKN
        }
        localization_key = MKN_agrarian_isolationism
    }
    text = {
        localization_key = NWW_default_neutrality_noun
    }
}
defined_text = {
    name = GetNwwMknCommunismNameNoun
    text = {
        trigger = {
            tag = MKN
        }
        localization_key = MKN_state_socialism
    }
    text = {
        localization_key = NWW_default_communism_noun
    }
}
defined_text = {
    name = GetNwwMknFascismNameDesc
    text = {
        trigger = {
            tag = MKN
        }
        localization_key = MKN_anarcho_militarism_regime
    }
    text = {
        localization_key = NWW_default_fascism_desc
    }
}
defined_text = {
    name = GetNwwMknDemocraticNameDesc
    text = {
        trigger = {
            tag = MKN
        }
        localization_key = MKN_anarcho_communism_regime
    }
    text = {
        localization_key = NWW_default_democratic_desc
    }
}
defined_text = {
    name = GetNwwMknNeutralityNameDesc
    text = {
        trigger = {
            tag = MKN
        }
        localization_key = MKN_agrarian_isolationism_regime
    }
    text = {
        localization_key = NWW_default_neutrality_desc
    }
}
defined_text = {
    name = GetNwwMknCommunismNameDesc
    text = {
        trigger = {
            tag = MKN
        }
        localization_key = MKN_state_socialism_regime
    }
    text = {
        localization_key = NWW_default_communism_desc
    }
}
```

### `common/decisions/categories/MKN_bop_categories.txt`

```pdx
MKN_bop_decisions_category = {
    icon = GFX_decision_category_power_struggle
    allowed = {
        original_tag = MKN
    }
    priority = 90
    visible = {
        has_power_balance = {
            id = MKN_power_balance
        }
    }
}
MKN_succession_crisis_category = {
    icon = generic_political_actions
    allowed = {
        tag = MKN
    }
    priority = 100
    visible = {
        has_country_flag = mkn_batko_departed
        NOT = {
            has_country_flag = MKN_crisis_legacy_settled
        }
    }
}
MKN_steppe_operations_category = {
    icon = generic_guerilla_base
    allowed = {
        tag = MKN
    }
    visible = {
        OR = {
            has_completed_focus = MKN_black_expansionism
            has_completed_focus = MKN_propaganda_by_deed
            has_completed_focus = MKN_railway_sabotage
            has_completed_focus = MKN_black_international
            has_completed_focus = MKN_embassy_to_kharkov
        }
    }
}
MKN_soviet_intervention_category = {
    icon = GFX_decision_generic_military
    allowed = {
        original_tag = MKN
    }
    visible = {
        has_country_flag = MKN_collapse_started
        has_country_flag = MKN_collapse_participant
        has_country_flag = MKN_soviet_intervention_initialized
        NOT = {
            has_country_flag = MKN_soviet_intervention_resolved
        }
        NOT = {
            has_global_flag = MKN_soviet_intervention_triggered
        }
        NOT = {
            has_global_flag = MKN_collapse_reunified
        }
    }
}
```

### `common/decisions/categories/MKN_horizons_categories.txt`

```pdx
MKN_horizons_international_category = {
    icon = generic_political_actions
    allowed = {
        original_tag = MKN
    }
    visible = {
        has_completed_focus = MKN_nabat_abroad
    }
}
```

### `common/decisions/categories/MKN_international_categories.txt`

```pdx
mkn_black_international_category = {
    icon = generic_political_actions
    allowed = {
        original_tag = MKN
    }
    visible = {
        has_completed_focus = MKN_black_international
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

### `common/on_actions/MKN_ai_on_actions.txt`

```pdx
on_actions = {
    on_startup = {
        effect = {
            MKN = {
                if = {
                    limit = {
                        exists = yes
                    }
                    MKN_initialize_ai_route = yes
                }
            }
        }
    }
    on_daily_MKN = {
        effect = {
            MKN_initialize_ai_route = yes
        }
    }
}
```

### `common/on_actions/MKN_diplomacy_on_actions.txt`

```pdx
on_actions = {
    on_startup = {
        effect = {
            MKN = {
                if = {
                    limit = {
                        exists = yes
                    }
                    MKN_install_allied_war_guard = yes
                    MKN_close_allied_frontier = yes
                }
            }
            UKR = {
                if = {
                    limit = {
                        exists = yes
                    }
                    MKN_install_allied_war_guard = yes
                    UKR_repair_mkn_limited_war = yes
                }
            }
            SOV = {
                if = {
                    limit = {
                        exists = yes
                    }
                    MKN_install_allied_war_guard = yes
                }
            }
        }
    }
    on_daily_MKN = {
        effect = {
            MKN_close_allied_frontier = yes
        }
    }
    on_daily_UKR = {
        effect = {
            UKR_repair_mkn_limited_war = yes
        }
    }
}
```

### `common/on_actions/MKN_flag_on_actions.txt`

```pdx
on_actions = {
    on_startup = {
        effect = {
            every_country = {
                limit = {
                    original_tag = MKN
                    exists = yes
                }
                MKN_update_national_flag = yes
            }
        }
    }
    on_daily = {
        effect = {
            every_country = {
                limit = {
                    original_tag = MKN
                    exists = yes
                }
                MKN_update_national_flag = yes
            }
        }
    }
}
```

### `common/on_actions/MKN_horizons_on_actions.txt`

```pdx
on_actions = {
    on_startup = {
        effect = {
            MKN = {
                if = {
                    limit = {
                        exists = yes
                    }
                    MKN_repair_horizons = yes
                }
            }
        }
    }
    on_daily_MKN = {
        effect = {
            MKN_repair_horizons = yes
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

### `common/on_actions/MKN_intervention_on_actions.txt`

```pdx
on_actions = {
    on_daily = {
        effect = {
            every_country = {
                limit = {
                    original_tag = MKN
                    has_country_flag = MKN_collapse_started
                    has_country_flag = MKN_collapse_participant
                    NOT = {
                        has_country_flag = MKN_duel_participant
                    }
                }
                MKN_repair_soviet_intervention = yes
            }
        }
    }
}
```

### `common/on_actions/MKN_overhaul_on_actions.txt`

```pdx
on_actions = {
    on_startup = {
        effect = {
            every_country = {
                limit = {
                    original_tag = MKN
                    exists = yes
                }
                MKN_repair_overhaul = yes
            }
        }
    }
    on_daily = {
        effect = {
            every_country = {
                limit = {
                    original_tag = MKN
                    exists = yes
                }
                MKN_repair_overhaul = yes
            }
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

## События, выборы ответа, scripted effects и triggers

Цепочки включают предложения другим странам и их ответы. Не считать награду предложения гарантированным положительным ответом.

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

### `MKN_can_move_capital_to_kyiv` — `common/scripted_triggers/MKN_ukraine_integration_triggers.txt`

```pdx
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

### `MKN_close_allied_frontier` — `common/scripted_effects/MKN_diplomacy_effects.txt`

```pdx
MKN_close_allied_frontier = {
    if = {
        limit = {
            MKN_ukr_common_bloc = yes
        }
        mkn_ukr_stop_border_battle = yes
        set_country_flag = mkn_ukr_frontier_concluded
        set_country_flag = mkn_ukr_frontier_allied_settlement
        remove_mission = MKN_passive_escalation_drift
        remove_mission = MKN_frontier_year_countdown_mission
        clr_country_flag = mkn_frontier_conflict_active
        clr_country_flag = mkn_ukr_frontier_unlocked
        clr_country_flag = mkn_ukr_war_pending
        clr_country_flag = mkn_ukr_pact_pending
        clr_country_flag = mkn_frontier_year_running
    }
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

### `MKN_horizons_austrian_border_target` — `common/scripted_triggers/MKN_horizons_triggers.txt`

```pdx
MKN_horizons_austrian_border_target = {
    FROM = {
        OR = {
            state = 89
            state = 90
            state = 80
        }
        is_owned_and_controlled_by = AUS
        has_border_war = no
        any_neighbor_state = {
            is_owned_and_controlled_by = ROOT
            has_border_war = no
        }
    }
    AUS = {
        exists = yes
        has_war = no
        is_subject = no
    }
    has_war = no
    NOT = {
        has_border_war_with = AUS
    }
    MKN_horizons_hostile_austria = yes
}
```

### `MKN_horizons_hostile_austria` — `common/scripted_triggers/MKN_horizons_triggers.txt`

```pdx
MKN_horizons_hostile_austria = {
    NOT = {
        is_ally_with = AUS
    }
    NOT = {
        is_in_faction_with = AUS
    }
    NOT = {
        has_non_aggression_pact_with = AUS
    }
}
```

### `MKN_horizons_hostile_target` — `common/scripted_triggers/MKN_horizons_triggers.txt`

```pdx
MKN_horizons_hostile_target = {
    FROM = {
        exists = yes
        is_subject = no
        NOT = {
            is_ally_with = ROOT
        }
        NOT = {
            is_in_faction_with = ROOT
        }
        NOT = {
            has_non_aggression_pact_with = ROOT
        }
        NOT = {
            has_war_with = ROOT
        }
    }
}
```

### `MKN_horizons_reactor_site` — `common/scripted_triggers/MKN_horizons_triggers.txt`

```pdx
MKN_horizons_reactor_site = {
    has_capitulated = no
    has_completed_focus = MKN_the_absolute_argument
    has_tech = nuclear_reactor
    FROM = {
        state = 1082
        is_owned_and_controlled_by = ROOT
        is_core_of = ROOT
        free_building_slots = {
            building = nuclear_reactor
            size > 0
            include_locked = yes
        }
    }
}
```

### `MKN_initialize_ai_route` — `common/scripted_effects/MKN_ai_effects.txt`

```pdx
MKN_initialize_ai_route = {
    if = {
        limit = {
            is_ai = yes
            has_focus_tree = MKN_focus
            NOT = {
                has_country_flag = MKN_ai_random_default_v2
            }
        }
        if = {
            limit = {
                has_game_rule = {
                    rule = MKN_ai_behavior
                    option = DEFAULT
                }
                NOT = {
                    OR = {
                        has_completed_focus = MKN_military_takes_charge
                        has_completed_focus = MKN_triumph_of_free_soviets
                        has_completed_focus = MKN_peasant_delegates
                        has_completed_focus = MKN_emergency_revkom
                    }
                }
            }
            clr_country_flag = MKN_ai_plan_selected
            clr_country_flag = MKN_ai_route_fascism
            clr_country_flag = MKN_ai_route_democratic
            clr_country_flag = MKN_ai_route_neutrality
            clr_country_flag = MKN_ai_route_communism
        }
        set_country_flag = MKN_ai_random_default_v2
    }
    if = {
        limit = {
            is_ai = yes
            has_focus_tree = MKN_focus
            NOT = {
                has_country_flag = MKN_ai_plan_selected
            }
        }
        if = {
            limit = {
                has_completed_focus = MKN_military_takes_charge
            }
            set_country_flag = MKN_ai_route_fascism
        }
        else_if = {
            limit = {
                has_completed_focus = MKN_triumph_of_free_soviets
            }
            set_country_flag = MKN_ai_route_democratic
        }
        else_if = {
            limit = {
                has_completed_focus = MKN_peasant_delegates
            }
            set_country_flag = MKN_ai_route_neutrality
        }
        else_if = {
            limit = {
                has_completed_focus = MKN_emergency_revkom
            }
            set_country_flag = MKN_ai_route_communism
        }
        else_if = {
            limit = {
                has_game_rule = {
                    rule = MKN_ai_behavior
                    option = FASCISM
                }
            }
            set_country_flag = MKN_ai_route_fascism
        }
        else_if = {
            limit = {
                has_game_rule = {
                    rule = MKN_ai_behavior
                    option = DEMOCRATIC
                }
            }
            set_country_flag = MKN_ai_route_democratic
        }
        else_if = {
            limit = {
                has_game_rule = {
                    rule = MKN_ai_behavior
                    option = NEUTRALITY
                }
            }
            set_country_flag = MKN_ai_route_neutrality
        }
        else_if = {
            limit = {
                has_game_rule = {
                    rule = MKN_ai_behavior
                    option = COMMUNISM
                }
            }
            set_country_flag = MKN_ai_route_communism
        }
        else_if = {
            limit = {
                has_game_rule = {
                    rule = MKN_ai_behavior
                    option = HISTORICAL
                }
            }
            set_country_flag = MKN_ai_route_communism
        }
        else = {
            random_list = {
                seed = random
                25 = {
                    set_country_flag = MKN_ai_route_fascism
                }
                25 = {
                    set_country_flag = MKN_ai_route_democratic
                }
                25 = {
                    set_country_flag = MKN_ai_route_neutrality
                }
                25 = {
                    set_country_flag = MKN_ai_route_communism
                }
            }
        }
        set_country_flag = MKN_ai_plan_selected
    }
}
```

### `MKN_install_allied_war_guard` — `common/scripted_effects/MKN_diplomacy_effects.txt`

```pdx
MKN_install_allied_war_guard = {
    if = {
        limit = {
            tag = UKR
        }
        remove_relation_rule_override = {
            trigger = UKR_mkn_premature_attack
            can_not_declare_war = yes
        }
        add_relation_rule_override = {
            trigger = UKR_mkn_premature_attack
            can_not_declare_war = yes
            usage_desc = UKR_mkn_escalation_required_tt
        }
    }
    remove_relation_rule_override = {
        trigger = MKN_protected_diplomatic_relation
        can_not_declare_war = yes
    }
    add_relation_rule_override = {
        trigger = MKN_protected_diplomatic_relation
        usage_desc = MKN_allied_war_guard_tt
        can_not_declare_war = yes
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

### `MKN_observe_ukrainian_integration` — `common/scripted_effects/MKN_ukraine_integration_effects.txt`

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

### `MKN_rebuild_foreign_service` — `common/scripted_effects/MKN_foreign_effects.txt`

```pdx
MKN_rebuild_foreign_service = {
    set_variable = {
        MKN_foreign_relations_upkeep = 0
    }
    set_variable = {
        MKN_foreign_trade_opinion = 0
    }
    set_variable = {
        MKN_foreign_opinion_gain = 0
    }
    set_variable = {
        MKN_foreign_guarantee_cost = 0
    }
    if = {
        limit = {
            has_completed_focus = MKN_foreign_delegates
        }
        set_variable = {
            MKN_foreign_relations_upkeep = -0.1
        }
        if = {
            limit = {
                NOT = {
                    has_dynamic_modifier = {
                        modifier = MKN_foreign_service
                    }
                }
            }
            add_dynamic_modifier = {
                modifier = MKN_foreign_service
            }
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_workers_corridors
        }
        set_variable = {
            MKN_foreign_trade_opinion = 0.1
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_consular_communes
        }
        set_variable = {
            MKN_foreign_opinion_gain = 0.1
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_solidarity_guarantees
        }
        set_variable = {
            MKN_foreign_guarantee_cost = -0.1
        }
    }
}
```

### `MKN_rebuild_horizons_service_stats` — `common/scripted_effects/MKN_horizons_effects.txt`

```pdx
MKN_rebuild_horizons_service_stats = {
    if = {
        limit = {
            has_completed_focus = MKN_fund_the_underground
        }
        add_to_variable = {
            MKN_army_army_non_core_attack_factor = 0.1
        }
        add_to_variable = {
            MKN_army_army_non_core_defence_factor = 0.1
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_global_syndicalist_pact
        }
        add_to_variable = {
            MKN_army_send_volunteer_size = 3
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_death_or_freedom
        }
        add_to_variable = {
            MKN_army_conscription = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_marusya_womens_battalions
        }
        add_to_variable = {
            MKN_army_army_org_regain = 0.1
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_shadows_in_the_forests
        }
        add_to_variable = {
            MKN_army_resistance_damage_to_garrison_on_our_occupied_states = 1.0
        }
    }
    if = {
        limit = {
            has_completed_focus = MKN_dnieper_jet_falcons
        }
        add_to_variable = {
            MKN_air_air_agility_factor = 0.05
        }
    }
    if = {
        limit = {
            OR = {
                has_completed_focus = MKN_death_or_freedom
                has_completed_focus = MKN_global_syndicalist_pact
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
}
```

### `MKN_repair_horizons` — `common/scripted_effects/MKN_horizons_effects.txt`

```pdx
MKN_repair_horizons = {
    MKN_repair_research_capacity = yes
    MKN_rebuild_foreign_service = yes
    if = {
        limit = {
            has_completed_focus = MKN_global_syndicalist_pact
        }
        remove_relation_rule_override = {
            trigger = MKN_horizons_ineligible_volunteer_target
            can_send_volunteers = no
        }
        add_relation_rule_override = {
            trigger = MKN_horizons_ineligible_volunteer_target
            can_send_volunteers = no
            usage_desc = MKN_volunteer_recipients_tt
        }
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

### `MKN_repair_overhaul` — `common/scripted_effects/MKN_overhaul_effects.txt`

```pdx
MKN_repair_overhaul = {
    if = {
        limit = {
            NOT = {
                has_country_flag = MKN_overhaul_v4
            }
        }
        nww_mkn_rebuild_industry = yes
        nww_mkn_rebuild_services = yes
        set_country_flag = MKN_overhaul_v4
    }
    if = {
        limit = {
            has_completed_focus = MKN_purge_irreconcilables
            has_government = communism
            has_country_leader_with_trait = mkn_paralyzed_committee
        }
        MKN_install_tsebriy = yes
    }
    if = {
        limit = {
            has_country_flag = mkn_ukr_incident_fired
            NOT = {
                has_country_flag = mkn_ukr_frontier_concluded
            }
            NOT = {
                has_completed_focus = MKN_ukrainian_frontier_root
            }
        }
        complete_national_focus = MKN_ukrainian_frontier_root
    }
    if = {
        limit = {
            has_country_flag = mkn_frontier_conflict_active
            NOT = {
                has_country_flag = mkn_ukr_frontier_concluded
            }
            NOT = {
                has_active_mission = MKN_passive_escalation_drift
            }
        }
        activate_mission = MKN_passive_escalation_drift
    }
    if = {
        limit = {
            has_country_flag = mkn_ukr_frontier_concluded
        }
        remove_mission = MKN_passive_escalation_drift
        clr_country_flag = mkn_frontier_conflict_active
        clr_country_flag = mkn_ukr_frontier_unlocked
    }
    if = {
        limit = {
            NOT = {
                has_government = communism
            }
            has_idea = MKN_revkom_terror
        }
        remove_ideas = MKN_revkom_terror
    }
    if = {
        limit = {
            NOT = {
                has_country_flag = MKN_successor_portraits_v1
            }
        }
        if = {
            limit = {
                has_country_leader_with_trait = mkn_syndicalist_organizer
            }
            set_country_leader_portrait = {
                ideology = communism
                portrait = GFX_Portrait_MKN_osyp_tsebriy
            }
        }
        else_if = {
            limit = {
                has_country_leader_with_trait = mkn_paralyzed_committee
            }
            set_country_leader_portrait = {
                ideology = communism
                portrait = GFX_Portrait_MKN_revkom
            }
        }
        if = {
            limit = {
                has_country_leader_with_trait = mkn_granary_overseer
            }
            set_country_leader_portrait = {
                ideology = neutrality
                portrait = GFX_Portrait_MKN_peasant_council
            }
        }
        set_country_flag = MKN_successor_portraits_v1
    }
}
```

### `MKN_repair_soviet_intervention` — `common/scripted_effects/MKN_intervention_effects.txt`

```pdx
MKN_repair_soviet_intervention = {
    if = {
        limit = {
            original_tag = MKN
            has_country_flag = MKN_collapse_started
            has_country_flag = MKN_collapse_participant
        }
        MKN_check_soviet_intervention_unification = yes
        if = {
            limit = {
                OR = {
                    check_variable = {
                        num_owned_states < 1
                    }
                    has_global_flag = MKN_soviet_intervention_triggered
                    has_global_flag = MKN_collapse_reunified
                    has_country_flag = MKN_soviet_intervention_resolved
                }
            }
            set_country_flag = MKN_soviet_intervention_resolved
            remove_mission = MKN_soviet_intervention_mission
        }
        if = {
            limit = {
                check_variable = {
                    num_owned_states > 0
                }
                has_global_flag = MKN_soviet_intervention_pending
                NOT = {
                    has_global_flag = MKN_soviet_intervention_triggered
                }
                NOT = {
                    has_global_flag = MKN_collapse_reunified
                }
                NOT = {
                    any_country = {
                        original_tag = MKN
                        has_country_flag = MKN_collapse_started
                        has_country_flag = MKN_collapse_participant
                        has_country_flag = MKN_soviet_intervention_dispatch_owner
                        check_variable = {
                            num_owned_states > 0
                        }
                    }
                }
            }
            set_country_flag = MKN_soviet_intervention_dispatch_owner
            country_event = {
                id = mkn_crisis.200
            }
        }
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

### `MKN_request_soviet_intervention` — `common/scripted_effects/MKN_intervention_effects.txt`

```pdx
MKN_request_soviet_intervention = {
    MKN_check_soviet_intervention_unification = yes
    if = {
        limit = {
            original_tag = MKN
            has_country_flag = MKN_collapse_started
            has_country_flag = MKN_collapse_participant
            check_variable = {
                num_owned_states > 0
            }
            NOT = {
                has_global_flag = MKN_soviet_intervention_pending
            }
            NOT = {
                has_global_flag = MKN_soviet_intervention_triggered
            }
            NOT = {
                has_global_flag = MKN_collapse_reunified
            }
            any_other_country = {
                original_tag = MKN
                has_country_flag = MKN_collapse_started
                has_country_flag = MKN_collapse_participant
                check_variable = {
                    num_owned_states > 0
                }
            }
        }
        set_global_flag = MKN_soviet_intervention_pending
        set_country_flag = MKN_soviet_intervention_dispatch_owner
        country_event = {
            id = mkn_crisis.200
        }
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

### `MKN_update_national_flag` — `common/scripted_effects/MKN_flag_effects.txt`

```pdx
MKN_update_national_flag = {
    if = {
        limit = {
            original_tag = MKN
            NOT = {
                has_country_flag = mkn_batko_departed
            }
            NOT = {
                has_country_flag = MKN_duel_participant
            }
            NOT = {
                has_cosmetic_tag = MKN_batko
            }
        }
        set_cosmetic_tag = MKN_batko
    }
    else_if = {
        limit = {
            original_tag = MKN
            has_cosmetic_tag = MKN_batko
            OR = {
                has_country_flag = mkn_batko_departed
                has_country_flag = MKN_duel_participant
            }
        }
        drop_cosmetic_tag = yes
    }
}
```

### `UKR_repair_mkn_limited_war` — `common/scripted_effects/MKN_diplomacy_effects.txt`

```pdx
UKR_repair_mkn_limited_war = {
    if = {
        limit = {
            has_offensive_war_with = MKN
            MKN = {
                has_country_flag = mkn_ukr_total_war
            }
        }
        set_country_flag = UKR_mkn_offensive_limited
    }
    if = {
        limit = {
            NOT = {
                has_war_with = MKN
            }
        }
        clr_country_flag = UKR_mkn_offensive_limited
    }
}
```

### `mkn.30` — `events/nww_mkn.txt`

```pdx
country_event = {
    id = mkn.30
    title = mkn.30.t
    desc = mkn.30.d
    picture = GFX_report_event_election_vote
    is_triggered_only = yes
    option = {
        name = mkn.30.a
        ai_chance = {
            factor = 50
        }
        add_timed_idea = {
            idea = MKN_construction_drive
            days = 365
        }
    }
    option = {
        name = mkn.30.b
        ai_chance = {
            factor = 50
        }
        add_timed_idea = {
            idea = MKN_careful_investment
            days = 365
        }
    }
}
```

### `mkn_crisis.100` — `events/MKN_events.txt`

```pdx
country_event = {
    id = mkn_crisis.100
    title = mkn_crisis.100.t
    desc = mkn_crisis.100.d
    picture = GFX_report_event_spr_anarchist_uprising
    is_triggered_only = yes
    trigger = {
        tag = MKN
        has_country_flag = MKN_crisis_active
        NOT = {
            has_country_flag = MKN_crisis_settled
        }
        NOT = {
            has_country_flag = MKN_collapse_started
        }
    }
    immediate = {
        MKN_execute_four_way_collapse = yes
    }
    option = {
        name = mkn_crisis.100.a
    }
}
```

### `mkn_crisis.20` — `events/MKN_events.txt`

```pdx
country_event = {
    id = mkn_crisis.20
    title = mkn_crisis.20.t
    desc = mkn_crisis.20.d
    picture = GFX_report_event_generic_train
    is_triggered_only = yes
    trigger = {
        tag = SOV
        MKN = {
            exists = yes
            is_subject = no
            has_government = communism
            NOT = {
                has_war_with = SOV
            }
        }
        has_government = communism
        is_subject = no
    }
    option = {
        name = mkn_crisis.20.a
        ai_chance = {
            factor = 80
        }
        give_military_access = MKN
        MKN = {
            give_military_access = SOV
            set_country_flag = MKN_soviet_trade_accepted
            country_event = {
                id = mkn_crisis.21
                days = 1
            }
        }
        trigger = {
            tag = SOV
            has_government = communism
            is_subject = no
            MKN = {
                exists = yes
                is_subject = no
                has_government = communism
                NOT = {
                    has_war_with = SOV
                }
            }
        }
    }
    option = {
        name = mkn_crisis.20.b
        ai_chance = {
            factor = 20
        }
        MKN = {
            country_event = {
                id = mkn_crisis.22
                days = 1
            }
        }
    }
}
```

### `mkn_crisis.23` — `events/MKN_events.txt`

```pdx
country_event = {
    id = mkn_crisis.23
    title = mkn_crisis.23.t
    desc = mkn_crisis.23.d
    picture = GFX_report_event_generic_train
    is_triggered_only = yes
    trigger = {
        tag = SOV
        is_subject = no
        has_government = communism
        MKN = {
            exists = yes
            has_government = communism
            is_subject = no
            NOT = {
                has_war_with = SOV
            }
        }
    }
    immediate = {
        MKN = {
            clr_country_flag = MKN_soviet_front_pending
        }
    }
    option = {
        name = mkn_crisis.23.a
        ai_chance = {
            factor = 85
        }
        if = {
            limit = {
                is_in_faction = no
            }
            set_rule = {
                can_create_factions = yes
            }
            create_faction = MKN_red_defence_pact
        }
        add_to_faction = MKN
        MKN = {
            country_event = {
                id = mkn_crisis.24
                days = 1
            }
        }
        trigger = {
            OR = {
                is_in_faction = no
                is_faction_leader = yes
            }
            MKN = {
                OR = {
                    is_in_faction = no
                    is_in_faction_with = SOV
                }
            }
            tag = SOV
            has_government = communism
            is_subject = no
            MKN = {
                exists = yes
                is_subject = no
                has_government = communism
                NOT = {
                    has_war_with = SOV
                }
            }
        }
    }
    option = {
        name = mkn_crisis.23.b
        ai_chance = {
            factor = 15
        }
        MKN = {
            country_event = {
                id = mkn_crisis.25
                days = 1
            }
        }
    }
}
```

### `mkn_crisis.30` — `events/MKN_events.txt`

```pdx
country_event = {
    id = mkn_crisis.30
    title = mkn_crisis.30.t
    desc = mkn_crisis.30.d
    picture = GFX_report_event_DEN_sabotage
    is_triggered_only = yes
    option = {
        name = mkn_crisis.30.a
        add_timed_idea = {
            idea = MKN_neighbor_strikes
            days = 60
        }
    }
    option = {
        name = mkn_crisis.30.b
        trigger = {
            has_political_power > 49
        }
        add_political_power = -50
        add_stability = -0.05
    }
}
```

### `mkn_crisis.40` — `events/MKN_events.txt`

```pdx
country_event = {
    id = mkn_crisis.40
    title = mkn_crisis.40.t
    desc = mkn_crisis.40.d
    picture = GFX_report_event_ITA_grand_council
    is_triggered_only = yes
    trigger = {
        tag = SOV
        has_government = communism
        is_subject = no
        MKN = {
            exists = yes
            is_subject = no
            has_government = communism
            is_in_faction_with = SOV
            NOT = {
                has_war_with = SOV
            }
        }
    }
    immediate = {
        MKN = {
            clr_country_flag = MKN_plenum_pending
        }
    }
    option = {
        name = mkn_crisis.40.a
        MKN = {
            set_country_flag = MKN_equal_autonomy
            country_event = {
                id = mkn_crisis.41
                days = 1
            }
        }
        trigger = {
            tag = SOV
            has_government = communism
            is_subject = no
            MKN = {
                exists = yes
                is_subject = no
                has_government = communism
                NOT = {
                    has_war_with = SOV
                }
            }
            MKN = {
                is_in_faction_with = SOV
            }
        }
        ai_chance = {
            factor = 60
            modifier = {
                factor = 100
                OR = {
                    is_historical_focus_on = yes
                    MKN = {
                        MKN_ai_historical_mode = yes
                    }
                }
            }
        }
    }
    option = {
        name = mkn_crisis.40.b
        trigger = {
            tag = SOV
            has_government = communism
            is_subject = no
            MKN = {
                exists = yes
                is_subject = no
                has_government = communism
                NOT = {
                    has_war_with = SOV
                }
            }
            MKN = {
                is_in_faction_with = SOV
            }
            NOT = {
                has_country_flag = NWW_SOV_MKN_settlement
            }
            MKN = {
                NOT = {
                    has_country_flag = MKN_equal_autonomy
                }
            }
        }
        ai_chance = {
            factor = 40
            modifier = {
                factor = 0
                OR = {
                    is_historical_focus_on = yes
                    MKN = {
                        MKN_ai_historical_mode = yes
                    }
                }
            }
        }
        if = {
            limit = {
                tag = SOV
                has_government = communism
                is_subject = no
                MKN = {
                    exists = yes
                    is_subject = no
                    has_government = communism
                    NOT = {
                        has_war_with = SOV
                    }
                }
                MKN = {
                    is_in_faction_with = SOV
                }
                NOT = {
                    has_country_flag = NWW_SOV_MKN_settlement
                }
                MKN = {
                    NOT = {
                        has_country_flag = MKN_equal_autonomy
                    }
                }
            }
            if = {
                limit = {
                    is_faction_leader = yes
                }
                remove_from_faction = MKN
            }
            else = {
                MKN = {
                    remove_from_faction = SOV
                }
            }
            MKN = {
                set_country_flag = MKN_soviet_betrayal
                add_timed_idea = {
                    idea = MKN_betrayed_twice
                    days = 365
                }
            }
            declare_war_on = {
                target = MKN
                type = annex_everything
            }
            MKN = {
                country_event = {
                    id = mkn_crisis.42
                    days = 1
                }
            }
        }
    }
    option = {
        name = mkn_crisis.40.c
        ai_chance = {
            factor = 100
        }
        trigger = {
            NOT = {
                tag = SOV
                has_government = communism
                is_subject = no
                MKN = {
                    exists = yes
                    is_subject = no
                    has_government = communism
                    NOT = {
                        has_war_with = SOV
                    }
                }
                MKN = {
                    is_in_faction_with = SOV
                }
            }
        }
    }
}
```

### `mkn_foreign.1` — `events/MKN_foreign_events.txt`

```pdx
country_event = {
    id = mkn_foreign.1
    title = mkn_foreign.1.t
    desc = mkn_foreign.1.d
    picture = GFX_report_event_generic_factory
    is_triggered_only = yes
    option = {
        name = mkn_foreign.1.a
        ai_chance = {
            factor = 60
        }
        trigger = {
            has_country_flag = MKN_workshop_exchange_pending
            NOT = {
                has_country_flag = MKN_workshop_exchange_agreed
            }
            is_subject = no
            has_capitulated = no
            NOT = {
                has_war_with = MKN
            }
            MKN = {
                exists = yes
                has_capitulated = no
                has_completed_focus = MKN_workers_corridors
            }
        }
        if = {
            limit = {
                has_country_flag = MKN_workshop_exchange_pending
                NOT = {
                    has_country_flag = MKN_workshop_exchange_agreed
                }
                is_subject = no
                has_capitulated = no
                NOT = {
                    has_war_with = MKN
                }
                MKN = {
                    exists = yes
                    has_capitulated = no
                    has_completed_focus = MKN_workers_corridors
                }
            }
            set_country_flag = MKN_workshop_exchange_agreed
            clr_country_flag = MKN_workshop_exchange_pending
            add_tech_bonus = {
                bonus = 0.5
                uses = 1
                category = industry
            }
            add_opinion_modifier = {
                target = MKN
                modifier = MKN_workshop_exchange_opinion
            }
            MKN = {
                add_tech_bonus = {
                    bonus = 0.5
                    uses = 1
                    category = industry
                }
                add_opinion_modifier = {
                    target = ROOT
                    modifier = MKN_workshop_exchange_opinion
                }
            }
        }
        else = {
            clr_country_flag = MKN_workshop_exchange_pending
        }
    }
    option = {
        name = mkn_foreign.1.b
        ai_chance = {
            factor = 40
        }
        clr_country_flag = MKN_workshop_exchange_pending
    }
}
```

### `mkn_horizons.1` — `events/MKN_horizons_events.txt`

```pdx
country_event = {
    id = mkn_horizons.1
    title = mkn_horizons.1.t
    desc = mkn_horizons.1.d
    picture = GFX_report_event_gathering_protest
    is_triggered_only = yes
    option = {
        name = mkn_horizons.1.a
        ai_chance = {
            factor = 40
        }
        trigger = {
            has_country_flag = MKN_congress_invitation_pending
            is_subject = no
            is_in_faction = no
            OR = {
                has_government = communism
                has_government = democratic
            }
            NOT = {
                has_war_with = MKN
            }
            MKN = {
                exists = yes
                is_faction_leader = yes
                has_country_flag = MKN_black_international_founded
            }
        }
        MKN = {
            add_to_faction = ROOT
        }
        clr_country_flag = MKN_congress_invitation_pending
    }
    option = {
        name = mkn_horizons.1.b
        ai_chance = {
            factor = 60
        }
        clr_country_flag = MKN_congress_invitation_pending
    }
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

### `MKN_ai_historical_mode` — `common/scripted_triggers/MKN_diplomacy_triggers.txt`

```pdx
MKN_ai_historical_mode = {
    OR = {
        has_game_rule = {
            rule = MKN_ai_behavior
            option = HISTORICAL
        }
        AND = {
            has_game_rule = {
                rule = MKN_ai_behavior
                option = DEFAULT
            }
            is_historical_focus_on = yes
        }
    }
}
```

### `MKN_check_soviet_intervention_unification` — `common/scripted_effects/MKN_intervention_effects.txt`

```pdx
MKN_check_soviet_intervention_unification = {
    if = {
        limit = {
            NOT = {
                has_global_flag = MKN_soviet_intervention_triggered
            }
            NOT = {
                has_global_flag = MKN_collapse_reunified
            }
        }
        every_country = {
            limit = {
                original_tag = MKN
                has_country_flag = MKN_collapse_started
                has_country_flag = MKN_collapse_participant
                check_variable = {
                    num_owned_states > 0
                }
                NOT = {
                    any_other_country = {
                        original_tag = MKN
                        has_country_flag = MKN_collapse_started
                        has_country_flag = MKN_collapse_participant
                        check_variable = {
                            num_owned_states > 0
                        }
                    }
                }
            }
            set_global_flag = MKN_collapse_reunified
        }
    }
    if = {
        limit = {
            has_global_flag = MKN_collapse_reunified
        }
        clr_global_flag = MKN_soviet_intervention_pending
        every_country = {
            limit = {
                original_tag = MKN
                has_country_flag = MKN_collapse_started
                has_country_flag = MKN_collapse_participant
            }
            set_country_flag = MKN_soviet_intervention_resolved
            remove_mission = MKN_soviet_intervention_mission
        }
    }
}
```

### `MKN_execute_four_way_collapse` — `common/scripted_effects/MKN_effects.txt`

```pdx
MKN_execute_four_way_collapse = {
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
    set_variable = {
        MKN_duel_best_support = -1
    }
    if = {
        limit = {
            NOT = {
                has_government = fascism
            }
            check_variable = {
                var = party_popularity@fascism
                value = MKN_duel_best_support
                compare = greater_than
            }
        }
        set_variable = {
            MKN_duel_best_support = party_popularity@fascism
        }
        set_variable = {
            MKN_duel_challenger = 0
        }
    }
    if = {
        limit = {
            NOT = {
                has_government = democratic
            }
            check_variable = {
                var = party_popularity@democratic
                value = MKN_duel_best_support
                compare = greater_than
            }
        }
        set_variable = {
            MKN_duel_best_support = party_popularity@democratic
        }
        set_variable = {
            MKN_duel_challenger = 1
        }
    }
    if = {
        limit = {
            NOT = {
                has_government = neutrality
            }
            check_variable = {
                var = party_popularity@neutrality
                value = MKN_duel_best_support
                compare = greater_than
            }
        }
        set_variable = {
            MKN_duel_best_support = party_popularity@neutrality
        }
        set_variable = {
            MKN_duel_challenger = 2
        }
    }
    if = {
        limit = {
            NOT = {
                has_government = communism
            }
            check_variable = {
                var = party_popularity@communism
                value = MKN_duel_best_support
                compare = greater_than
            }
        }
        set_variable = {
            MKN_duel_best_support = party_popularity@communism
        }
        set_variable = {
            MKN_duel_challenger = 3
        }
    }
    if = {
        limit = {
            check_variable = {
                MKN_duel_challenger = 0
            }
        }
        start_civil_war = {
            ideology = fascism
            size = 0.50
            keep_all_characters = yes
            set_country_flag = MKN_crisis_enabled
            set_country_flag = MKN_collapse_started
            set_country_flag = mkn_collapsed
            set_country_flag = MKN_duel_participant
            set_country_flag = MKN_collapse_participant
            set_country_flag = mkn_ukr_frontier_concluded
            load_focus_tree = {
                tree = MKN_focus
                keep_completed = yes
            }
            MKN_install_fascism_successor = yes
            set_politics = {
                ruling_party = fascism
                elections_allowed = no
            }
            save_global_event_target_as = MKN_duel_challenger
        }
    }
    if = {
        limit = {
            check_variable = {
                MKN_duel_challenger = 1
            }
        }
        start_civil_war = {
            ideology = democratic
            size = 0.50
            keep_all_characters = yes
            set_country_flag = MKN_crisis_enabled
            set_country_flag = MKN_collapse_started
            set_country_flag = mkn_collapsed
            set_country_flag = MKN_duel_participant
            set_country_flag = MKN_collapse_participant
            set_country_flag = mkn_ukr_frontier_concluded
            load_focus_tree = {
                tree = MKN_focus
                keep_completed = yes
            }
            MKN_install_democratic_successor = yes
            set_politics = {
                ruling_party = democratic
                elections_allowed = no
            }
            save_global_event_target_as = MKN_duel_challenger
        }
    }
    if = {
        limit = {
            check_variable = {
                MKN_duel_challenger = 2
            }
        }
        start_civil_war = {
            ideology = neutrality
            size = 0.50
            keep_all_characters = yes
            set_country_flag = MKN_crisis_enabled
            set_country_flag = MKN_collapse_started
            set_country_flag = mkn_collapsed
            set_country_flag = MKN_duel_participant
            set_country_flag = MKN_collapse_participant
            set_country_flag = mkn_ukr_frontier_concluded
            load_focus_tree = {
                tree = MKN_focus
                keep_completed = yes
            }
            MKN_install_neutrality_successor = yes
            set_politics = {
                ruling_party = neutrality
                elections_allowed = no
            }
            save_global_event_target_as = MKN_duel_challenger
        }
    }
    if = {
        limit = {
            check_variable = {
                MKN_duel_challenger = 3
            }
        }
        start_civil_war = {
            ideology = communism
            size = 0.50
            keep_all_characters = yes
            set_country_flag = MKN_crisis_enabled
            set_country_flag = MKN_collapse_started
            set_country_flag = mkn_collapsed
            set_country_flag = MKN_duel_participant
            set_country_flag = MKN_collapse_participant
            set_country_flag = mkn_ukr_frontier_concluded
            load_focus_tree = {
                tree = MKN_focus
                keep_completed = yes
            }
            MKN_install_communism_successor = yes
            set_politics = {
                ruling_party = communism
                elections_allowed = no
            }
            save_global_event_target_as = MKN_duel_challenger
        }
    }
    if = {
        limit = {
            is_ai = no
        }
        set_country_flag = MKN_duel_choice_pending
    }
    set_country_flag = MKN_duel_started
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

### `MKN_repair_research_capacity` — `common/scripted_effects/MKN_research_effects.txt`

```pdx
MKN_repair_research_capacity = {
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

### `MKN_ukr_common_bloc` — `common/scripted_triggers/MKN_ukr_border_triggers.txt`

```pdx
MKN_ukr_common_bloc = {
    OR = {
        is_ally_with = UKR
        is_in_faction_with = UKR
        AND = {
            SOV = {
                exists = yes
            }
            is_in_faction_with = SOV
            UKR = {
                is_in_faction_with = SOV
            }
        }
    }
}
```

### `mkn_crisis.1` — `events/MKN_events.txt`

```pdx
country_event = {
    id = mkn_crisis.1
    title = mkn_crisis.1.t
    desc = mkn_crisis.1.d
    picture = GFX_report_event_makhno_funeral
    fire_only_once = yes
    trigger = {
        tag = MKN
        date > 1937.2.28
        has_country_flag = MKN_crisis_enabled
        NOT = {
            has_country_flag = mkn_batko_departed
        }
    }
    mean_time_to_happen = {
        days = 75
        modifier = {
            factor = 0
            date > 1938.1.30
        }
    }
    immediate = {
        set_country_flag = mkn_batko_departed
        MKN_update_national_flag = yes
        remove_ideas = MKN_decaying_batko
        if = {
            limit = {
                has_character = NWW_MKN_makhno
            }
            retire_character = NWW_MKN_makhno
        }
        MKN_install_fascism_successor = yes
        MKN_install_democratic_successor = yes
        MKN_install_neutrality_successor = yes
        MKN_install_communism_successor = yes
        complete_national_focus = MKN_departure_of_batko
        set_country_flag = MKN_crisis_active
        activate_mission = MKN_civil_war_timer_mission
        news_event = {
            id = mkn_news.1
        }
        if = {
            limit = {
                NOT = {
                    has_country_flag = mkn_ukr_incident_fired
                }
                NOT = {
                    has_country_flag = mkn_ukr_incident_scheduled
                }
            }
            set_country_flag = mkn_ukr_incident_scheduled
            country_event = {
                id = mkn_ukr_border.10
                days = 7
            }
        }
    }
    option = {
        name = mkn_crisis.1.a
        hidden_effect = {
            if = {
                limit = {
                    NOT = {
                        has_country_flag = mkn_ukr_incident_fired
                    }
                    NOT = {
                        has_country_flag = mkn_ukr_incident_scheduled
                    }
                }
                set_country_flag = mkn_ukr_incident_scheduled
                country_event = {
                    id = mkn_ukr_border.10
                    days = 7
                }
            }
        }
    }
}
```

### `mkn_crisis.200` — `events/MKN_events.txt`

```pdx
country_event = {
    id = mkn_crisis.200
    title = mkn_crisis.200.t
    desc = mkn_crisis.200.d
    picture = GFX_report_event_spr_anarchist_uprising
    is_triggered_only = yes
    trigger = {
        original_tag = MKN
        has_country_flag = MKN_collapse_started
        has_country_flag = MKN_collapse_participant
        check_variable = {
            num_owned_states > 0
        }
        has_global_flag = MKN_soviet_intervention_pending
        NOT = {
            has_global_flag = MKN_soviet_intervention_triggered
        }
        NOT = {
            has_global_flag = MKN_collapse_reunified
        }
        any_other_country = {
            original_tag = MKN
            has_country_flag = MKN_collapse_started
            has_country_flag = MKN_collapse_participant
            check_variable = {
                num_owned_states > 0
            }
        }
    }
    immediate = {
        MKN_execute_soviet_intervention = yes
    }
    option = {
        name = mkn_crisis.200.a
        custom_effect_tooltip = MKN_soviet_intervention_tt
    }
}
```

### `mkn_crisis.21` — `events/MKN_events.txt`

```pdx
country_event = {
    id = mkn_crisis.21
    title = mkn_crisis.21.t
    desc = mkn_crisis.21.d
    picture = GFX_report_event_generic_train
    is_triggered_only = yes
    option = {
        name = mkn_crisis.21.a
    }
}
```

### `mkn_crisis.22` — `events/MKN_events.txt`

```pdx
country_event = {
    id = mkn_crisis.22
    title = mkn_crisis.22.t
    desc = mkn_crisis.22.d
    picture = GFX_report_event_generic_train
    is_triggered_only = yes
    option = {
        name = mkn_crisis.22.a
        add_political_power = 50
    }
}
```

### `mkn_crisis.24` — `events/MKN_events.txt`

```pdx
country_event = {
    id = mkn_crisis.24
    title = mkn_crisis.24.t
    desc = mkn_crisis.24.d
    picture = GFX_report_event_generic_train
    is_triggered_only = yes
    option = {
        name = mkn_crisis.24.a
    }
}
```

### `mkn_crisis.25` — `events/MKN_events.txt`

```pdx
country_event = {
    id = mkn_crisis.25
    title = mkn_crisis.25.t
    desc = mkn_crisis.25.d
    picture = GFX_report_event_generic_train
    is_triggered_only = yes
    option = {
        name = mkn_crisis.25.a
        add_stability = 0.05
    }
}
```

### `mkn_crisis.41` — `events/MKN_events.txt`

```pdx
country_event = {
    id = mkn_crisis.41
    title = mkn_crisis.41.t
    desc = mkn_crisis.41.d
    picture = GFX_report_event_ITA_grand_council
    is_triggered_only = yes
    option = {
        name = mkn_crisis.41.a
        add_stability = 0.15
        add_political_power = 100
    }
}
```

### `mkn_crisis.42` — `events/MKN_events.txt`

```pdx
country_event = {
    id = mkn_crisis.42
    title = mkn_crisis.42.t
    desc = mkn_crisis.42.d
    picture = GFX_report_event_spr_anarchist_uprising
    is_triggered_only = yes
    option = {
        name = mkn_crisis.42.a
        add_war_support = 0.20
    }
}
```

### `mkn_integration.1` — `events/MKN_ukraine_integration_events.txt`

```pdx
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

### `mkn_ukr_stop_border_battle` — `common/scripted_effects/MKN_ukr_border_effects.txt`

```pdx
mkn_ukr_stop_border_battle = {
    if = {
        limit = {
            OR = {
                has_border_war_with = UKR
                has_border_war_with = SOV
            }
        }
        if = {
            limit = {
                has_variable = mkn_ukr_attacking_state
                has_variable = mkn_ukr_defending_state
            }
            cancel_border_war = {
                attacker = var:mkn_ukr_attacking_state
                defender = var:mkn_ukr_defending_state
                dont_fire_events = yes
            }
        }
        else = {
            every_owned_state = {
                limit = {
                    is_controlled_by = ROOT
                    has_border_war = yes
                }
                MKN = {
                    set_variable = {
                        mkn_ukr_attacking_state = PREV
                    }
                }
                every_neighbor_state = {
                    limit = {
                        OR = {
                            is_owned_and_controlled_by = UKR
                            is_owned_and_controlled_by = SOV
                        }
                        has_border_war = yes
                    }
                    MKN = {
                        set_variable = {
                            mkn_ukr_defending_state = PREV
                        }
                        cancel_border_war = {
                            attacker = var:mkn_ukr_attacking_state
                            defender = var:mkn_ukr_defending_state
                            dont_fire_events = yes
                        }
                    }
                }
            }
        }
    }
    clr_country_flag = mkn_ukr_border_battle_active
}
```

### `MKN_execute_soviet_intervention` — `common/scripted_effects/MKN_intervention_effects.txt`

```pdx
MKN_execute_soviet_intervention = {
    MKN_check_soviet_intervention_unification = yes
    if = {
        limit = {
            original_tag = MKN
            has_country_flag = MKN_collapse_started
            has_country_flag = MKN_collapse_participant
            check_variable = {
                num_owned_states > 0
            }
            NOT = {
                has_global_flag = MKN_soviet_intervention_triggered
            }
            NOT = {
                has_global_flag = MKN_collapse_reunified
            }
            any_other_country = {
                original_tag = MKN
                has_country_flag = MKN_collapse_started
                has_country_flag = MKN_collapse_participant
                check_variable = {
                    num_owned_states > 0
                }
            }
        }
        set_global_flag = MKN_soviet_intervention_triggered
        clr_global_flag = MKN_soviet_intervention_pending
        every_country = {
            limit = {
                original_tag = MKN
                has_country_flag = MKN_collapse_started
                has_country_flag = MKN_collapse_participant
            }
            set_country_flag = MKN_soviet_intervention_resolved
            remove_mission = MKN_soviet_intervention_mission
        }
        if = {
            limit = {
                SOV = {
                    exists = yes
                }
                SOV = {
                    is_subject = no
                }
            }
            SOV = {
                MKN_soviet_intervention_attack_participants = yes
            }
        }
        if = {
            limit = {
                UKR = {
                    exists = yes
                }
                UKR = {
                    is_subject = no
                }
            }
            UKR = {
                MKN_soviet_intervention_attack_participants = yes
            }
        }
    }
}
```

### `MKN_install_communism_successor` — `common/scripted_effects/MKN_effects.txt`

```pdx
MKN_install_communism_successor = {
    retire_ideology_leader = communism
    create_country_leader = {
        name = MKN_revkom_leader
        desc = MKN_communism_successor_desc
        picture = GFX_Portrait_MKN_revkom
        ideology = leninism
        traits = {
            mkn_paralyzed_committee
        }
    }
    if = {
        limit = {
            has_government = communism
        }
        add_ideas = MKN_revkom_terror
    }
}
```

### `MKN_install_democratic_successor` — `common/scripted_effects/MKN_effects.txt`

```pdx
MKN_install_democratic_successor = {
    retire_ideology_leader = democratic
    create_country_leader = {
        name = NWW_MKN_volin
        desc = MKN_democratic_successor_desc
        picture = GFX_Portrait_volin
        ideology = liberalism
        traits = {
            mkn_idealist_philosopher
        }
    }
}
```

### `MKN_install_fascism_successor` — `common/scripted_effects/MKN_effects.txt`

```pdx
MKN_install_fascism_successor = {
    retire_ideology_leader = fascism
    create_country_leader = {
        name = MKN_dmitruk_tratishov
        desc = MKN_fascism_successor_desc
        picture = GFX_Portrait_MKN_dmitruk_tratishov
        ideology = fascism_ideology
        traits = {
            mkn_iron_warlord
        }
    }
}
```

### `MKN_install_neutrality_successor` — `common/scripted_effects/MKN_effects.txt`

```pdx
MKN_install_neutrality_successor = {
    retire_ideology_leader = neutrality
    create_country_leader = {
        name = MKN_peasant_council_leader
        desc = MKN_neutrality_successor_desc
        picture = GFX_Portrait_MKN_peasant_council
        ideology = despotism
        traits = {
            mkn_granary_overseer
        }
    }
}
```

### `mkn_news.1` — `events/MKN_news_events.txt`

```pdx
news_event = {
    id = mkn_news.1
    title = mkn_news.1.t
    desc = mkn_news.1.d
    picture = GFX_news_event_makhno_death
    major = yes
    is_triggered_only = yes
    option = {
        name = mkn_news.1.a
        trigger = {
            tag = MKN
        }
    }
    option = {
        name = mkn_news.1.b
        trigger = {
            tag = SOV
        }
    }
    option = {
        name = mkn_news.1.c
        trigger = {
            tag = GER
        }
    }
    option = {
        name = mkn_news.1.e
        trigger = {
            NOT = {
                tag = MKN
            }
            NOT = {
                tag = SOV
            }
            NOT = {
                tag = GER
            }
        }
    }
}
```

### `mkn_ukr_border.10` — `events/MKN_ukr_border_events.txt`

```pdx
country_event = {
    id = mkn_ukr_border.10
    title = mkn_ukr_border.10.t
    desc = mkn_ukr_border.10.d
    picture = GFX_report_event_spain_civil_war_soldiers
    is_triggered_only = yes
    fire_only_once = yes
    trigger = {
        tag = MKN
        NOT = {
            has_country_flag = mkn_ukr_incident_fired
        }
        NOT = {
            has_country_flag = MKN_collapse_started
        }
        NOT = {
            has_country_flag = mkn_ukr_frontier_concluded
        }
        NOT = {
            MKN_ukr_common_bloc = yes
        }
    }
    immediate = {
        set_country_flag = mkn_ukr_incident_fired
        clr_country_flag = mkn_ukr_incident_scheduled
        if = {
            limit = {
                NOT = {
                    has_war_with = UKR
                }
                NOT = {
                    has_war_with = SOV
                }
                NOT = {
                    has_country_flag = mkn_ukr_frontier_concluded
                }
                UKR = {
                    exists = yes
                }
            }
            set_country_flag = mkn_frontier_conflict_active
            set_variable = {
                mkn_ukr_escalation_level = 2
            }
            set_country_flag = mkn_frontier_year_running
            activate_mission = MKN_frontier_year_countdown_mission
            activate_mission = MKN_passive_escalation_drift
        }
        complete_national_focus = MKN_ukrainian_frontier_root
    }
    option = {
        name = mkn_ukr_border.10.a
    }
}
```

### `MKN_soviet_intervention_attack_participants` — `common/scripted_effects/MKN_intervention_effects.txt`

```pdx
MKN_soviet_intervention_attack_participants = {
    save_event_target_as = MKN_intervention_aggressor
    every_country = {
        limit = {
            original_tag = MKN
            has_country_flag = MKN_collapse_started
            has_country_flag = MKN_collapse_participant
            check_variable = {
                num_owned_states > 0
            }
        }
        save_event_target_as = MKN_intervention_target
        if = {
            limit = {
                is_in_faction_with = event_target:MKN_intervention_aggressor
            }
            if = {
                limit = {
                    is_faction_leader = yes
                }
                remove_from_faction = event_target:MKN_intervention_aggressor
            }
            else = {
                faction_leader = {
                    remove_from_faction = event_target:MKN_intervention_target
                }
            }
        }
        event_target:MKN_intervention_aggressor = {
            if = {
                limit = {
                    NOT = {
                        is_ally_with = event_target:MKN_intervention_target
                    }
                }
                create_wargoal = {
                    type = annex_everything
                    target = event_target:MKN_intervention_target
                }
                if = {
                    limit = {
                        NOT = {
                            has_war_with = event_target:MKN_intervention_target
                        }
                    }
                    declare_war_on = {
                        type = annex_everything
                        target = event_target:MKN_intervention_target
                    }
                }
            }
        }
    }
}
```

## Локализация духов, решений, событий и ответов

```json
{
  "LTB": {
    "ru": "Литва-Беларусь",
    "en": "Lithuania-Belarus"
  },
  "MKN": {
    "ru": "Махновцы",
    "en": "Makhnovists"
  },
  "MKN_AI_COMMUNISM": {
    "ru": "Синдикалистский ревком Цебрия",
    "en": "Tsebriy’s Syndicalist Revkom"
  },
  "MKN_AI_COMMUNISM_DESC": {
    "ru": "Ревком, устранение непримиримых, платные договоры с СССР и переговоры о равной автономии. Для перехода сохраняется требование 40% поддержки.",
    "en": "The Revkom, removal of irreconcilables, negotiated Soviet cooperation and equal autonomy. The 40% mandate requirement remains."
  },
  "MKN_AI_DEMOCRATIC": {
    "ru": "Вольные советы Волина",
    "en": "Volin’s Free Councils"
  },
  "MKN_AI_DEMOCRATIC_DESC": {
    "ru": "Договор свободных коммун, самооборона и Чёрный интернационал. Для перехода ИИ готовит 40% поддержки.",
    "en": "A compact of free communes, self-defence and the Black International. The AI prepares 40% support for transition."
  },
  "MKN_AI_FASCISM": {
    "ru": "Военный штаб Дмитрука Тратишова",
    "en": "Dmitruk Tratishov’s Military Staff"
  },
  "MKN_AI_FASCISM_DESC": {
    "ru": "Выборный военный штаб, устранение демагогов и Чёрная орда. Для перехода ИИ готовит 40% поддержки.",
    "en": "An elected military staff, suppression of demagogues and the Black Horde. The AI prepares 40% support for transition."
  },
  "MKN_AI_NEUTRALITY": {
    "ru": "Крестьянские делегаты",
    "en": "Peasant Delegates"
  },
  "MKN_AI_NEUTRALITY_DESC": {
    "ru": "Хлебный ультиматум, сельская автономия и оборона житницы. Для перехода ИИ готовит 40% поддержки.",
    "en": "The grain ultimatum, rural autonomy and defence of the granary. The AI prepares 40% support for transition."
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
  "MKN_abolish_election_of_commanders_desc": {
    "ru": "Бой не может ждать голосования об отзыве. Упраздним баланс сил и закрепим власть военных в существующей армейской организации: постоянный штаб улучшит планирование и сплочённость.",
    "en": "A battle cannot wait for a recall vote. End the balance of power and fold military authority into our existing army organization: stronger planning and cohesion under a permanent staff."
  },
  "MKN_abolish_general_staff_desc": {
    "ru": "Штаб станет техническим бюро, подотчётным коммунам. Закрепим полный контроль советов на шкале баланса сил и улучшим взаимодействие местных боевых отрядов.",
    "en": "The staff becomes a technical bureau answerable to the communes. Lock the balance at complete soviet control and improve coordination between local fighting detachments."
  },
  "MKN_accept_italian_mechanics": {
    "ru": "Принять итальянских механиков-синдикалистов",
    "en": "Accept Italian Syndicalist Mechanics"
  },
  "MKN_accept_italian_mechanics_desc": {
    "ru": "Итальянские организаторы мастерских делятся опытом работы с двигателями и ремонта машин. Даёт один общий бонус к исследованиям в 100% для моторизованного снаряжения или бронеавтомобилей.",
    "en": "Italian workshop organizers bring expertise in engines and vehicle maintenance. Gain one shared 100% research bonus for motorized equipment or armored cars."
  },
  "MKN_accountable_militias": {
    "ru": "Ответственные командиры ополчения",
    "en": "Accountable Militia Commanders"
  },
  "MKN_accountable_militias_desc": {
    "ru": "Отряды согласовали полномочия командиров. Теперь предстоит обучить их действовать вместе.",
    "en": "Detachments have agreed on commanders' responsibilities. They must now learn to operate together."
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
  "MKN_agitation_in_litbel_desc": {
    "ru": "Виленский компромисс не отменяет тяжбы батрака с помещиком. Мы предложим профсоюзам ЛитБела оружие и средства для самостоятельной борьбы.",
    "en": "The Vilnius compromise has not ended the struggle between labourers and landlords. Litbel unions shall receive arms and funds for their own struggle."
  },
  "MKN_agrarian_isolationism": {
    "ru": "Аграрный изоляционизм",
    "en": "Agrarian Isolationism"
  },
  "MKN_agrarian_isolationism_regime": {
    "ru": "Аграрное покровительство",
    "en": "Agrarian Protectorate"
  },
  "MKN_air_coastal_support": {
    "ru": "Поддержка приморского фронта",
    "en": "Coastal Front Support"
  },
  "MKN_air_coastal_support_desc": {
    "ru": "Приморские эскадрильи прикроют переправы и ударят по кораблям противника.",
    "en": "Coastal squadrons will cover crossings and attack enemy shipping."
  },
  "MKN_air_development": {
    "ru": "Крылья вольной территории",
    "en": "Wings of the Free Territory"
  },
  "MKN_air_development_desc": {
    "ru": "Подготовка кадров, местное производство и согласованные службы укрепляются по мере выполнения военной программы.",
    "en": "Training, local production and coordinated services improve as the military program advances."
  },
  "MKN_air_development_summary": {
    "ru": "Улучшения авиации накапливаются в одном духе.",
    "en": "Air improvements accumulate in this single spirit."
  },
  "MKN_air_dispersal": {
    "ru": "Рассредоточенные аэродромы",
    "en": "Dispersed Airfields"
  },
  "MKN_air_dispersal_desc": {
    "ru": "Рассредоточим самолёты по запасным полосам и защитим домашнее небо.",
    "en": "Disperse aircraft among reserve strips and strengthen home air defence."
  },
  "MKN_air_ground_coordination_focus_desc": {
    "ru": "Карты, фотосъёмка и единая сетка координат избавят экипажи от поиска цели вслепую.\\n\\nДымовые сигналы и условные полотнища обозначат передний край.",
    "en": "Maps, photographs and shared coordinates will prevent blind target searches.\\n\\nSmoke signals and recognition panels will mark the front line."
  },
  "MKN_air_ground_liaisons": {
    "ru": "Связные при наземных штабах",
    "en": "Air Ground Liaison Officers"
  },
  "MKN_air_ground_liaisons_desc": {
    "ru": "Связные передадут запросы пехоты прямо на аэродром.",
    "en": "Liaison teams will carry infantry requests directly to the airfields."
  },
  "MKN_air_home_defence": {
    "ru": "Защита промышленных районов",
    "en": "Industrial Air Defence"
  },
  "MKN_air_home_defence_desc": {
    "ru": "Зенитные батареи и истребители разделят зоны защиты промышленных коммун.",
    "en": "Anti-aircraft batteries and fighters will share the defence of industrial communes."
  },
  "MKN_air_map_bureau": {
    "ru": "Общее картографическое бюро",
    "en": "Shared Aerial Mapping Bureau"
  },
  "MKN_air_map_bureau_desc": {
    "ru": "Карты, фотосъёмка и единая сетка координат избавят экипажи от поиска цели вслепую.",
    "en": "Maps, photographs and shared coordinates will prevent blind target searches."
  },
  "MKN_air_radar_school": {
    "ru": "Школа радиолокации",
    "en": "Radar School"
  },
  "MKN_air_radar_school_desc": {
    "ru": "Радиолокационная школа научит расчёты сопровождать цели и наводить истребители.",
    "en": "Radar schooling will train crews to track targets and direct fighters."
  },
  "MKN_air_rescue": {
    "ru": "Спасение сбитых лётчиков",
    "en": "Downed Pilot Rescue"
  },
  "MKN_air_rescue_desc": {
    "ru": "Спасённый лётчик вернётся к полётам и передаст опыт новым экипажам.",
    "en": "Rescued pilots will return to flying and train new crews."
  },
  "MKN_air_supply_lift": {
    "ru": "Доставка срочных грузов",
    "en": "Urgent Air Deliveries"
  },
  "MKN_air_supply_lift_desc": {
    "ru": "Воздушные перевозки восполнят самые срочные нужды оторвавшихся колонн.",
    "en": "Air transport will meet the urgent needs of isolated columns."
  },
  "MKN_air_support_compact_desc": {
    "ru": "Колонны получили воздушную поддержку; дальние и морские операции можно развивать отдельно. Дополнительные тактики приобретаются отдельно в полевом штабе.",
    "en": "Columns now have air support, with long-range and maritime operations available as extensions. Further tactics can be purchased separately at the field headquarters."
  },
  "MKN_air_warning": {
    "ru": "Единая воздушная тревога",
    "en": "Unified Air Warning"
  },
  "MKN_air_warning_desc": {
    "ru": "Единая тревога поднимет нужные звенья вместо всей авиации сразу.",
    "en": "A shared warning system will scramble the right flights without exhausting the whole air force."
  },
  "MKN_air_warning_network_focus_desc": {
    "ru": "Наземные наблюдатели, телефонные посты и дежурные пары сведут донесения в одну сеть. Перехватчики будут раньше замечать налёт и лучше защищать родное небо.",
    "en": "Ground observers, telephone posts and ready sections will share one warning network, detecting raids earlier and defending home skies more effectively."
  },
  "MKN_air_weather_service": {
    "ru": "Степная метеослужба",
    "en": "Steppe Weather Service"
  },
  "MKN_air_weather_service_desc": {
    "ru": "Метеопосты помогут выбирать окно для удара вместо отмены всей операции.",
    "en": "Weather stations will help select a strike window instead of cancelling the operation."
  },
  "MKN_aircraft_artels": {
    "ru": "Артели истребителей",
    "en": "Fighter Artels"
  },
  "MKN_aircraft_artels_desc": {
    "ru": "Лёгкие планеры артели «Степной сокол» приспособят для манёвренного перехвата.",
    "en": "Steppe Falcon cooperatives will adapt light airframes for agile interception."
  },
  "MKN_aircraft_recovery": {
    "ru": "Возвращать повреждённые машины",
    "en": "Recover Damaged Aircraft"
  },
  "MKN_aircraft_recovery_desc": {
    "ru": "Эвакуационные бригады вернут повреждённые машины и спасут ремонтный фонд.",
    "en": "Recovery teams will retrieve damaged aircraft for repair."
  },
  "MKN_aircraft_spares": {
    "ru": "Общий запас авиационных деталей",
    "en": "Shared Aircraft Spares"
  },
  "MKN_aircraft_spares_desc": {
    "ru": "Общий запас моторов сократит простои и аварии изношенных самолётов.",
    "en": "Shared engine reserves will reduce downtime and failures."
  },
  "MKN_airfield_fuel": {
    "ru": "Топливные склады эскадрилий",
    "en": "Squadron Fuel Depots"
  },
  "MKN_airfield_fuel_desc": {
    "ru": "Наладим заправку, чтобы ударные группы не пропускали решающий вылет.",
    "en": "Organize refuelling so strike groups can fly at the decisive moment."
  },
  "MKN_airframe_jigs": {
    "ru": "Оснастка для лёгких планеров",
    "en": "Light Airframe Jigs"
  },
  "MKN_airframe_jigs_desc": {
    "ru": "Серийная оснастка обеспечит точную сборку и вооружение истребителей.",
    "en": "Production jigs will improve fighter assembly and armament."
  },
  "MKN_airframe_standardization_focus_desc": {
    "ru": "Радиомаяки помогут перехватчикам вернуться даже в плохую погоду.\\n\\nСерийная оснастка обеспечит точную сборку и вооружение истребителей.\\n\\nЭвакуационные бригады вернут повреждённые машины и спасут ремонтный фонд.",
    "en": "Radio beacons will guide interceptors home in poor weather.\\n\\nProduction jigs will improve fighter assembly and armament.\\n\\nRecovery teams will retrieve damaged aircraft for repair."
  },
  "MKN_allied_war_guard_tt": {
    "ru": "Нельзя объявить войну союзнику по общему блоку или нарушить принятый договор равной автономии MKN.",
    "en": "War cannot be declared against a common-bloc ally or in violation of MKN’s accepted equal-autonomy agreement."
  },
  "MKN_anarchic_economy_idea": {
    "ru": "Несогласованное хозяйство коммун",
    "en": "Uncoordinated Communal Economy"
  },
  "MKN_anarchic_economy_idea_desc": {
    "ru": "Каждая коммуна решает за себя, но общего учёта и надёжных расчётов нет. Съезды должны выработать работающие хозяйственные соглашения.",
    "en": "Each commune decides for itself, but shared accounting and reliable settlement are absent. Congresses must establish workable economic agreements."
  },
  "MKN_anarcho_communism": {
    "ru": "Анархо-коммунизм",
    "en": "Anarcho-Communism"
  },
  "MKN_anarcho_communism_regime": {
    "ru": "Федерация вольных советов",
    "en": "Federation of Free Soviets"
  },
  "MKN_anarcho_militarism": {
    "ru": "Анархо-милитаризм",
    "en": "Anarcho-Militarism"
  },
  "MKN_anarcho_militarism_regime": {
    "ru": "Военная директория",
    "en": "Military Directorate"
  },
  "MKN_anti_imperialist_front_desc": {
    "ru": "Предложим оборонительный союз против имперских дворов ЛитБела и Германии. Советское правительство должно дать согласие; ни одна чужая страна не вступит без собственного решения.",
    "en": "Propose a defensive alliance against the imperial courts of LitBel and Germany. The Soviet government must agree; no foreign country joins without its own decision."
  },
  "MKN_anti_submarine_patrols": {
    "ru": "Противолодочные патрули",
    "en": "Anti Submarine Patrols"
  },
  "MKN_anti_submarine_patrols_desc": {
    "ru": "Охотничьи группы будут прочёсывать район перед выходом конвоев.",
    "en": "Hunting groups will sweep the area before convoys sail."
  },
  "MKN_armored_train_staff_bonus": {
    "ru": "Командование бронепоездами",
    "en": "Armored Train Command"
  },
  "MKN_armored_train_staff_bonus_desc": {
    "ru": "Пока командующий состоит в штабе, бронепоезда получают +20% к броне и эффективности ПВО. Бронепоезда относятся к логистическому оснащению.",
    "en": "While the train commander serves, armored trains receive +20% armor and anti-air effectiveness. Trains are logistical equipment rather than divisions."
  },
  "MKN_armored_trains_and_repair_focus_desc": {
    "ru": "Эвакуационные тягачи вернут повреждённые машины в мастерские.\\n\\nРемонтная база Днепра обеспечит запасные узлы и восстановление техники.",
    "en": "Recovery tractors will retrieve damaged vehicles for the workshops.\\n\\nA Dnipro repair plant will provide replacement assemblies and equipment repairs."
  },
  "MKN_armoured_manoeuvres": {
    "ru": "Манёвры механизированных колонн",
    "en": "Mechanized Column Manoeuvres"
  },
  "MKN_armoured_manoeuvres_desc": {
    "ru": "Большие манёвры отработают смену направления без потери управления.",
    "en": "Large manoeuvres will rehearse changes of direction without losing cohesion."
  },
  "MKN_arms_to_the_people_desc": {
    "ru": "Выдадим винтовки из общих складов и сформируем три оснащённых отряда коммунальной гвардии. Расширенная система набора сделает каждое село ответственным за свою оборону.",
    "en": "Issue rifles from the common depots and form three equipped commune guards. A broader recruitment system makes each village responsible for its own defense."
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
  "MKN_army_army_org_factor_tt": {
    "ru": "$army_org_factor_tt$",
    "en": "$army_org_factor_tt$"
  },
  "MKN_army_breakthrough_factor_tt": {
    "ru": "Прорыв армии: $RIGHT|+=%1$",
    "en": "Army breakthrough: $RIGHT|+=%1$"
  },
  "MKN_army_conscription_tt": {
    "ru": "Военнообязанное население: §G+2%§!.",
    "en": "Recruitable population: §G+2%§!."
  },
  "MKN_army_development": {
    "ru": "Армия вольной территории",
    "en": "Army of the Free Territory"
  },
  "MKN_army_development_desc": {
    "ru": "Подготовка кадров, местное производство и согласованные службы укрепляются по мере выполнения военной программы.",
    "en": "Training, local production and coordinated services improve as the military program advances."
  },
  "MKN_army_development_summary": {
    "ru": "Улучшения армии накапливаются в одном духе.",
    "en": "Army improvements accumulate in this single spirit."
  },
  "MKN_army_enemy_army_bonus_air_superiority_factor_tt": {
    "ru": "Преимущество противника от господства в воздухе: $RIGHT|+=%1$",
    "en": "Enemy air superiority advantage: $RIGHT|+=%1$"
  },
  "MKN_army_enemy_attrition_tt": {
    "ru": "Истощение противника: $RIGHT|+=%1$",
    "en": "Hostile attrition: $RIGHT|+=%1$"
  },
  "MKN_army_hq_unlock_tt": {
    "ru": "Открывает решения полевого штаба этого рода войск; тактики требуют выбранной военной программы.",
    "en": "Unlocks this service field headquarters; tactics require a chosen military program."
  },
  "MKN_army_land_reinforce_rate_tt": {
    "ru": "$land_reinforce_rate_tt$",
    "en": "$land_reinforce_rate_tt$"
  },
  "MKN_army_max_planning_tt": {
    "ru": "$MODIFIER_MAX_PLANNING$: $RIGHT|+=%1$",
    "en": "$MODIFIER_MAX_PLANNING$: $RIGHT|+=%1$"
  },
  "MKN_army_modifier_army_sub_unit_cavalry_attack_factor_tt": {
    "ru": "Атака кавалерии: $RIGHT|+=%1$",
    "en": "Cavalry attack: $RIGHT|+=%1$"
  },
  "MKN_army_motorized_attack_factor_tt": {
    "ru": "Атака моторизованных батальонов: $RIGHT|+=%1$",
    "en": "Motorized battalion attack: $RIGHT|+=%1$"
  },
  "MKN_army_planning_speed_tt": {
    "ru": "$MODIFIER_PLANNING_SPEED$: $RIGHT|+=%1$",
    "en": "$MODIFIER_PLANNING_SPEED$: $RIGHT|+=%1$"
  },
  "MKN_army_recon_factor_tt": {
    "ru": "$recon_factor_tt$",
    "en": "$recon_factor_tt$"
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
  "MKN_arrest_demagogues_desc": {
    "ru": "Штаб опечатывает фракционные типографии и задерживает организаторов соперничающих командований. Жестокое урегулирование останавливает 180-дневный отсчёт до гражданской войны.",
    "en": "The staff seals the faction presses and detains those organizing rival commands. A brutal settlement ends the 180-day countdown to civil war."
  },
  "MKN_artel_logistics": {
    "ru": "Обозная взаимопомощь",
    "en": "Mutual Aid Supply Trains"
  },
  "MKN_artel_logistics_desc": {
    "ru": "Артели держат запасные маршруты и ремонтные пункты, уменьшая потери техники в полевых условиях.",
    "en": "Artels maintain alternate routes and repair posts, reducing equipment losses in the field."
  },
  "MKN_artel_register_desc": {
    "ru": "Артели запишут свои запасы, инструменты и обещания соседям. Хозяйственный конгресс получит право оплачивать соляные промыслы, ветряки, обучение командиров, хлебную политику и взаимное страхование.",
    "en": "Artels record their stocks, tools and promises. The Economic Congress can fund salt workings, windmills, elected commanders, grain policy and mutual insurance."
  },
  "MKN_artillery_artels": {
    "ru": "Артиллерийские артели",
    "en": "Artillery Artels"
  },
  "MKN_artillery_artels_desc": {
    "ru": "Никопольские артели наладят орудия для сопровождения наступающей пехоты.",
    "en": "Nikopol workshops will manufacture guns to support advancing infantry."
  },
  "MKN_ataman_directorate": {
    "ru": "Директория атаманов",
    "en": "The Ataman Directorate"
  },
  "MKN_ataman_directorate_desc": {
    "ru": "Директория учреждает постоянный совет командования. Требуется более 80% военного контроля; политические решения сохраняют возможность изменять баланс.",
    "en": "The directorate establishes a permanent command council. It requires more than 80% military control; the balance remains adjustable through political decisions."
  },
  "MKN_attack_air_artels": {
    "ru": "Артели штурмовой авиации",
    "en": "Attack Aircraft Artels"
  },
  "MKN_attack_air_artels_desc": {
    "ru": "«Днепровское крыло» приспособит лёгкие самолёты для ударов по наземным целям.",
    "en": "Dnipro Wing cooperatives will adapt light aircraft for ground attack."
  },
  "MKN_attack_wing_rotations": {
    "ru": "Сменяемые ударные группы",
    "en": "Rotating Strike Groups"
  },
  "MKN_attack_wing_rotations_desc": {
    "ru": "Сменяемые группы распределят нагрузку между людьми, машинами и складами горючего.",
    "en": "Rotating wings will balance demands on crews, machines and fuel depots."
  },
  "MKN_autonomous_rail_crews_desc": {
    "ru": "Расписание принадлежит тем, кто обеспечивает движение. Рабочие бригады снизят стоимость поездов и ускорят строительство железных дорог и инфраструктуры.",
    "en": "The timetable belongs to those who keep it running. Worker crews lower train costs and accelerate railway and infrastructure construction."
  },
  "MKN_autonomous_rail_crews_idea": {
    "ru": "Самоуправляемые железнодорожные бригады",
    "en": "Autonomous Rail Crews"
  },
  "MKN_autonomous_rail_crews_idea_desc": {
    "ru": "Выборные бригады обмениваются чертежами и инструментами. Все поезда дешевле на 25%; строительство железных дорог и инфраструктуры ускорено на 25% и 20%.",
    "en": "Elected crews share designs and repair tools. All trains cost 25% less; railway and infrastructure construction gain 25% and 20%."
  },
  "MKN_batko": {
    "ru": "$MKN$",
    "en": "$MKN$"
  },
  "MKN_batko_cavalry": {
    "ru": "Конница Батьки",
    "en": "Batkos Cavalry"
  },
  "MKN_batko_cavalry_desc": {
    "ru": "Сохраним мобильность конницы, вложившись в вооружение и связь вместо дорогой брони.",
    "en": "Preserve cavalry mobility by investing in weapons and communications rather than expensive armour."
  },
  "MKN_batko_cavalry_idea": {
    "ru": "Конница Батьки",
    "en": "Batko's Cavalry"
  },
  "MKN_batko_cavalry_idea_desc": {
    "ru": "Конные сотни волости — глаза, уши и оружие степи.",
    "en": "Mounted hundreds of the volost: the steppe's eyes, ears and gun."
  },
  "MKN_beacon_of_statelessness_desc": {
    "ru": "Они могут занять станцию, но не сельский сход за ней. Получим ещё 35% к защите национальной территории и 75% к урону вражеским гарнизонам на нашей оккупированной земле.",
    "en": "They may occupy a station, but never the village assembly behind it. Add 35% core defense and 75% damage to enemy garrisons on our occupied soil."
  },
  "MKN_betrayed_twice": {
    "ru": "Преданы дважды",
    "en": "Betrayed Twice"
  },
  "MKN_betrayed_twice_desc": {
    "ru": "Они обещали общий фронт, а привели оккупационную армию. В течение года советы и бойцы будут вместе противостоять предательству.",
    "en": "They promised a common front and brought an occupying army. For one year, the councils and soldiers stand together against the betrayal."
  },
  "MKN_black_expansionism_desc": {
    "ru": "Граница, проведённая канцелярией, не священна. Откроем пограничные столкновения с ЛитБелом и советскими республиками там, где наши территории действительно соприкасаются.",
    "en": "A frontier drawn by a chancery is no sacred boundary. Unlock controlled border clashes with LitBel and the Soviet Republics wherever our territories actually meet."
  },
  "MKN_black_guard_veterans": {
    "ru": "Ветераны Чёрной гвардии",
    "en": "Black Guard Veterans"
  },
  "MKN_black_guard_veterans_desc": {
    "ru": "Ветераны передадут опыт молодым экипажам вместо формирования отдельной привилегированной гвардии.",
    "en": "Veterans will train replacements rather than form a privileged separate guard."
  },
  "MKN_black_guard_veterans_idea": {
    "ru": "Ветераны Чёрной гвардии",
    "en": "Veterans of the Black Guard"
  },
  "MKN_black_guard_veterans_idea_desc": {
    "ru": "Те, кто выжил в цепях и на тачанках, ведут за собой новые сотни.",
    "en": "Those who survived the chains and the tachankas lead the new hundreds."
  },
  "MKN_black_hundreds": {
    "ru": "Власть атаманов",
    "en": "The Atamans Take Command"
  },
  "MKN_black_hundreds_desc": {
    "ru": "При поддержке не менее 40% и после подготовки общественного мандата атаманы устанавливают анархо-милитаризм. Баланс смещается на 0,45 к командованию; согласие общин уступает место военным приказам.",
    "en": "With at least 40% support and a mandate from the communal press, the atamans establish anarcho-militarism. Army command gains 0.45 on the native balance scale; village consent gives way to military orders."
  },
  "MKN_black_international_decisions_unlock_tt": {
    "ru": "Открывает четыре одноразовых приглашения Чёрного интернационала: испанские анархисты, немецкие инженеры, итальянские механики и кронштадтские моряки.",
    "en": "Unlocks the four one-time Black International invitations: Spanish anarchists, German engineers, Italian mechanics and Kronstadt sailors."
  },
  "MKN_black_international_desc": {
    "ru": "После ухода Батьки общий Чёрный Интернационал станет опорой внешней политики при любом правительстве. Открывает четыре приглашения иностранных специалистов, набор добровольцев и общую ветку представительств, хозяйственных соглашений и зарубежного Набата.",
    "en": "After Batko’s departure, a common Black International will support foreign policy under every successor government. Opens four invitations for foreign specialists, volunteer recruitment and a shared branch of diplomatic missions, technical agreements and Nabat networks abroad."
  },
  "MKN_black_sea_escorts": {
    "ru": "Черноморские эскорты",
    "en": "Black Sea Escorts"
  },
  "MKN_black_sea_escorts_desc": {
    "ru": "Лёгкие эскорты Херсонской артели будут держать строй вокруг конвоя.",
    "en": "Light escorts from the Kherson cooperative will hold formation around convoys."
  },
  "MKN_black_sea_flotilla": {
    "ru": "Черноморская флотилия",
    "en": "Black Sea Flotilla"
  },
  "MKN_black_sea_flotilla_and_yards_desc": {
    "ru": "Создадим малую флотилию с задачами, посильными бюджету коммун.\\n\\nДнепровские дозоры станут школой будущих морских экипажей.\\n\\nХерсонские верфи дадут флотилии собственную строительную и ремонтную базу.\\n\\nОткрывает одноразовые тактики полевого штаба за опыт и командный ресурс.",
    "en": "Establish a small flotilla with missions the communes can afford.\\n\\nDnieper patrols will train the future sea-going crews.\\n\\nKherson yards will give the flotilla its own construction and repair base.\\n\\nUnlocks one-time field headquarters tactics purchased with experience and command power."
  },
  "MKN_black_sea_flotilla_desc": {
    "ru": "Создадим малую флотилию с задачами, посильными бюджету коммун.",
    "en": "Establish a small flotilla with missions the communes can afford."
  },
  "MKN_black_sea_smugglers": {
    "ru": "Школа черноморских рейдеров",
    "en": "Black Sea Raider School"
  },
  "MKN_black_sea_smugglers_desc": {
    "ru": "Малые подлодки и рейдеры сделают вражеские перевозки уязвимыми без гонки линкоров.",
    "en": "Small submarines and raiders will threaten enemy shipping without a battleship race."
  },
  "MKN_black_swarm": {
    "ru": "Чёрный рой",
    "en": "Black Swarm"
  },
  "MKN_black_swarm_desc": {
    "ru": "Истребители станут щитом коммун; ударная авиация останется второстепенной.",
    "en": "Fighters will shield the communes while strike aviation remains secondary."
  },
  "MKN_black_swarm_idea": {
    "ru": "Чёрный рой",
    "en": "The Black Swarm"
  },
  "MKN_black_swarm_idea_desc": {
    "ru": "Медленно — но над всем и всюду.",
    "en": "Slow — but above everything, everywhere."
  },
  "MKN_black_vengeance_spirit": {
    "ru": "Порыв Чёрной Мести",
    "en": "The Black Vengeance Offensive"
  },
  "MKN_black_vengeance_spirit_desc": {
    "ru": "На 180 дней: +20% к атаке на национальной территории и +10% к скорости армии.",
    "en": "For 180 days: +20% attack on core territory and +10% army speed."
  },
  "MKN_bomber_navigation": {
    "ru": "Школа штурманов",
    "en": "Navigator School"
  },
  "MKN_bomber_navigation_desc": {
    "ru": "Штурманы обеспечат поддержку за пределами знакомых аэродромов.",
    "en": "Navigators will extend support beyond familiar airfields."
  },
  "MKN_bombing_ranges": {
    "ru": "Полигоны точного бомбометания",
    "en": "Precision Bombing Ranges"
  },
  "MKN_bombing_ranges_desc": {
    "ru": "На полигонах экипажи научатся поражать цель рядом со своими войсками.",
    "en": "Range training will teach crews to strike targets close to friendly troops."
  },
  "MKN_bop_abandoned": {
    "ru": "Аграрный съезд упразднил баланс сил",
    "en": "The agrarian congress abolished the balance of power"
  },
  "MKN_bop_balanced": {
    "ru": "Съезд удерживает равновесие",
    "en": "The Congress Holds the Balance"
  },
  "MKN_bop_decisions_category": {
    "ru": "Мандат Вольной территории",
    "en": "The Mandate of the Free Territory"
  },
  "MKN_bop_decisions_category_desc": {
    "ru": "Три повторяемых решения за 50 политической власти меняют баланс сил. Принятая хартия полного контроля советов запрещает дальнейшие изменения.",
    "en": "Three repeatable 50-PP decisions adjust the balance. A locked constitution prevents further changes."
  },
  "MKN_bop_locked": {
    "ru": "Вольные советы получили постоянные полномочия",
    "en": "The free soviets hold permanent authority"
  },
  "MKN_bop_militarist_lean": {
    "ru": "Перевес атаманов",
    "en": "The Atamans’ Ascendancy"
  },
  "MKN_bop_soviet_lean": {
    "ru": "Перевес коммун",
    "en": "The Communes’ Ascendancy"
  },
  "MKN_bop_total_military": {
    "ru": "Штаб командует всем",
    "en": "The Staff Commands Everything"
  },
  "MKN_bop_total_soviets": {
    "ru": "Вся власть вольным советам",
    "en": "All Power to the Free Soviets"
  },
  "MKN_border_clash_active": {
    "ru": "Идёт пограничное столкновение",
    "en": "A frontier clash is underway"
  },
  "MKN_breakthrough_workshops": {
    "ru": "Мастерские прорыва",
    "en": "Breakthrough Workshops"
  },
  "MKN_breakthrough_workshops_desc": {
    "ru": "Мастерские прорыва будут выпускать бронетехнику по требованиям полевых экипажей.",
    "en": "Breakthrough workshops will build armour to field crews' specifications."
  },
  "MKN_bridge_columns": {
    "ru": "Мостовые колонны",
    "en": "Bridging Columns"
  },
  "MKN_bridge_columns_desc": {
    "ru": "Сборные мосты позволят колоннам продолжать наступление за Днепром.",
    "en": "Portable bridges will keep the columns advancing beyond the Dnieper."
  },
  "MKN_broken_supply": {
    "ru": "Перебои степного снабжения",
    "en": "Disrupted Steppe Supply"
  },
  "MKN_broken_supply_desc": {
    "ru": "Поезда простаивают, обозы расходятся по местным соглашениям, а склады не знают потребностей соседних отрядов.",
    "en": "Trains stand idle, local agreements scatter wagon convoys and depots cannot anticipate neighbouring detachments' needs."
  },
  "MKN_buenaventura_durruti": {
    "ru": "Буэнавентура Дуррути",
    "en": "Buenaventura Durruti"
  },
  "MKN_careful_investment": {
    "ru": "Бережливое переоснащение",
    "en": "Careful Retooling"
  },
  "MKN_careful_investment_desc": {
    "ru": "Предприятия переоснащаются постепенно, без чрезвычайных сборов.",
    "en": "Factories retool gradually without emergency collections."
  },
  "MKN_cas_joint_exercises": {
    "ru": "Учения лётчиков и артиллеристов",
    "en": "Pilot and Artillery Exercises"
  },
  "MKN_cas_joint_exercises_desc": {
    "ru": "Совместные учения проверят взаимодействие пилотов, артиллеристов и передовых наблюдателей.",
    "en": "Joint exercises will test cooperation between pilots, gunners and forward observers."
  },
  "MKN_cas_maintenance": {
    "ru": "Ремонт штурмовиков у фронта",
    "en": "Frontline Attack Aircraft Repair"
  },
  "MKN_cas_maintenance_desc": {
    "ru": "Прифронтовые мастерские восстановят повреждения от наземного огня.",
    "en": "Front-line workshops will repair damage inflicted by ground fire."
  },
  "MKN_cas_replacement_crews": {
    "ru": "Резерв экипажей штурмовиков",
    "en": "Attack Crew Reserve"
  },
  "MKN_cas_replacement_crews_desc": {
    "ru": "Резерв подготовленных экипажей позволит сохранять темп вылетов.",
    "en": "Trained replacement crews will sustain the sortie rate."
  },
  "MKN_cas_workshop_network_focus_desc": {
    "ru": "Прифронтовые мастерские восстановят повреждения от наземного огня.",
    "en": "Front-line workshops will repair damage inflicted by ground fire."
  },
  "MKN_catalogued_workshops": {
    "ru": "Учтённые мастерские",
    "en": "Catalogued Workshops"
  },
  "MKN_catalogued_workshops_desc": {
    "ru": "Станки и специалисты внесены в общий реестр, но детали ещё не взаимозаменяемы.",
    "en": "Machines and specialists have entered a shared register, but parts are still incompatible."
  },
  "MKN_cavalry_ambush_desc": {
    "ru": "Тачанки ждут за холмом, их лошади тихо стоят во ржи. Добавим общему армейскому духу 30% к атаке кавалерийских и моторизованных батальонов.",
    "en": "Tachankas wait behind the rise, their horses silent in the rye. Add 30% cavalry and motorized battalion attack to the common army spirit."
  },
  "MKN_civil_war_timer_mission": {
    "ru": "Степь на краю пропасти",
    "en": "The Steppe on the Brink"
  },
  "MKN_civil_war_timer_mission_desc": {
    "ru": "У нас 180 дней, чтобы завершить «Арестовать демагогов», «Пакт вольных коммун», «Зерновой ультиматум» или «Устранить непримиримых». Одной смены правящей партии недостаточно. Если время истечёт, соперничающие лагеря разделят области и вооружённые силы по долям поддержки населения, с округлением до целых областей и минимальной территорией для каждого лагеря.",
    "en": "We have 180 days to complete Arrest the Demagogues, Pact of Free Communes, Grain Ultimatum or Purge the Irreconcilables. Changing the ruling party alone does not avert collapse. If time runs out, rival camps divide our states and armed forces according to popular support, with whole-state rounding and a minimum foothold for each camp."
  },
  "MKN_clash_LTB": {
    "ru": "Рейд на границу ЛитБела: [From.GetName]",
    "en": "Raid LitBel’s Border: [From.GetName]"
  },
  "MKN_clash_LTB_desc": {
    "ru": "За 50 политической власти начнём настоящий пограничный бой. Победа передаст спорную область; обе страны должны быть в мире, а граница — общей и контролируемой.",
    "en": "Spend 50 PP to begin a real border battle. Victory transfers the contested state; both countries must be at peace and the border must be contiguous and controlled."
  },
  "MKN_clash_SOV": {
    "ru": "Рейд на советскую границу: [From.GetName]",
    "en": "Raid the Soviet Border: [From.GetName]"
  },
  "MKN_clash_SOV_desc": {
    "ru": "За 50 политической власти начнём настоящий пограничный бой. Победа передаст спорную область; обе страны должны быть в мире и не состоять в одном альянсе.",
    "en": "Spend 50 PP to begin a real border battle. Victory transfers the contested state; both countries must be at peace and outside a common faction."
  },
  "MKN_close_support_program": {
    "ru": "Авиация поддержки",
    "en": "Support Aviation"
  },
  "MKN_close_support_program_desc": {
    "ru": "Авиация станет летающей артиллерией для вольных колонн.",
    "en": "Aviation will become flying artillery for the free columns."
  },
  "MKN_coastal_defense_steppe": {
    "ru": "Береговой защитный пояс",
    "en": "Coastal Defence Belt"
  },
  "MKN_coastal_defense_steppe_desc": {
    "ru": "Защитим подходы к портам и сделаем зерновую торговлю главной задачей флота.",
    "en": "Defend port approaches and make grain shipping the navy's main mission."
  },
  "MKN_coastal_depots": {
    "ru": "Портовые склады снабжения",
    "en": "Port Supply Depots"
  },
  "MKN_coastal_depots_desc": {
    "ru": "Прибрежные склады поддержат длительное патрулирование без дальних переходов на заправку.",
    "en": "Coastal depots will sustain patrols without long refuelling trips."
  },
  "MKN_coastal_fleet_exercises": {
    "ru": "Учения береговой флотилии",
    "en": "Coastal Flotilla Exercises"
  },
  "MKN_coastal_fleet_exercises_desc": {
    "ru": "Проверим охранение торгового каравана в условиях учебной атаки.",
    "en": "Test merchant convoy protection against a simulated attack."
  },
  "MKN_coastal_fortifications_focus_desc": {
    "ru": "Речные экипажи перейдут на лёгкие мореходные корабли для прибрежной службы.\\n\\nБереговые посты предупредят капитанов о появлении противника.",
    "en": "River crews will move to light sea-going ships for coastal service.\\n\\nCoastal stations will warn captains of enemy movements."
  },
  "MKN_coastal_signal_posts": {
    "ru": "Береговые сигнальные посты",
    "en": "Coastal Signal Posts"
  },
  "MKN_coastal_signal_posts_desc": {
    "ru": "Береговые посты предупредят капитанов о появлении противника.",
    "en": "Coastal stations will warn captains of enemy movements."
  },
  "MKN_coastal_watch": {
    "ru": "Постоянный береговой дозор",
    "en": "Permanent Coastal Watch"
  },
  "MKN_coastal_watch_desc": {
    "ru": "Постоянный дозор закроет промежутки между портовыми районами.",
    "en": "Permanent patrols will close gaps between port districts."
  },
  "MKN_collapse_started": {
    "ru": "Вольная территория распалась",
    "en": "The Free Territory has collapsed"
  },
  "MKN_collectivize_the_steppe": {
    "ru": "Коллективизировать степь",
    "en": "Collectivize the Steppe"
  },
  "MKN_collectivize_the_steppe_desc": {
    "ru": "Добровольно. Преимущественно.",
    "en": "Voluntarily. Mostly."
  },
  "MKN_column_medical_service_desc": {
    "ru": "Полевые лазареты и запасные сотни свяжут вольные колонны с родными коммунами. Раненые получат помощь, а подкрепления быстрее займут места в бою.",
    "en": "Field hospitals and reserve companies will connect free columns to their home communes, recovering wounded fighters and bringing replacements into battle sooner."
  },
  "MKN_combined_arms": {
    "ru": "Единый боевой порядок",
    "en": "Combined Arms Formation"
  },
  "MKN_combined_arms_command_focus_desc": {
    "ru": "Радиосвязь позволит подкреплениям вступать в бой по команде штаба.",
    "en": "Radios will bring reinforcements into battle when the staff needs them."
  },
  "MKN_combined_arms_desc": {
    "ru": "Броня, артиллерия и пехота научатся действовать в одном боевом порядке.",
    "en": "Armour, artillery and infantry will learn to fight as one formation."
  },
  "MKN_communal_aa_defense_focus_desc": {
    "ru": "Наблюдатели передадут предупреждение до появления бомбардировщиков над городами.\\n\\nЕдиная тревога поднимет нужные звенья вместо всей авиации сразу.",
    "en": "Observers will report bombers before they reach the towns.\\n\\nA shared warning system will scramble the right flights without exhausting the whole air force."
  },
  "MKN_communal_compact_desc": {
    "ru": "Договоры кредита, страхования и взаимного ремонта завершат восстановление хозяйства. Рассредоточенные мастерские получат постоянные −20% ущерба промышленности от бомбардировок и +20% скорости ремонта в общем хозяйственном духе.",
    "en": "Credit, insurance and repair agreements complete recovery. Dispersed workshops gain permanent −20% industrial bombing damage and +20% repair speed through the shared economic spirit."
  },
  "MKN_communal_federation": {
    "ru": "Договор свободных коммун",
    "en": "Compact of Free Communes"
  },
  "MKN_communal_federation_desc": {
    "ru": "Политическая программа завершена: новое устройство закрепляет порядок и распределение полномочий.",
    "en": "The completed political programme establishes a durable division of powers and responsibilities."
  },
  "MKN_communal_fire_support_focus_desc": {
    "ru": "Никопольские артели наладят орудия для сопровождения наступающей пехоты.\\n\\nЕдиные таблицы стрельбы свяжут огонь батарей с планами танковых командиров.",
    "en": "Nikopol workshops will manufacture guns to support advancing infantry.\\n\\nCommon firing tables will align battery fire with armoured commanders' plans."
  },
  "MKN_communal_research_network_desc": {
    "ru": "Свяжем лаборатории промышленных коммун и создадим дополнительную исследовательскую группу. Общая программа институтов рассчитана на пять ячеек; шестая появится после интеграции Украины и Киевского научного обмена.",
    "en": "Connect the industrial communes’ laboratories and establish an additional research team. The common institute programme provides five slots; Ukrainian integration and Kyiv Scientific Exchange provide the sixth."
  },
  "MKN_communal_seed_reserves": {
    "ru": "Объединить общинные семенные резервы",
    "en": "Pool the Communal Seed Reserves"
  },
  "MKN_communal_seed_reserves_desc": {
    "ru": "Поручим сельским сходам согласовать запасы семян и заказы мастерским. Усиливает советы и хозяйственную кооперацию, снижая военный энтузиазм.",
    "en": "Let village assemblies coordinate seed stocks and workshop orders. Strengthen the councils and economic cooperation while reducing enthusiasm for war."
  },
  "MKN_commune_federation": {
    "ru": "Федерация коммун",
    "en": "Commune Federation"
  },
  "MKN_commune_federation_desc": {
    "ru": "Тысяча коммун — одна федерация.",
    "en": "A thousand communes, one federation."
  },
  "MKN_communism_successor_desc": {
    "ru": "Революционный комитет координирует самостоятельную государственно-социалистическую администрацию.",
    "en": "The revolutionary committee coordinates an independent state-socialist administration."
  },
  "MKN_congress_1936_desc": {
    "ru": "В зале пахнет мокрыми шинелями и типографской краской. Махно ещё способен заставить его замолчать одним взглядом, но никто не верит, что это будет длиться вечно. Дадим делегатам мандат и вынесем спор штаба Тратишова с советами Волина на съезд.",
    "en": "The hall smells of wet greatcoats and printer’s ink. Makhno can still silence it with a glance, but no one believes that he can do so forever. Give the delegates a mandate and bring the struggle between Tratishov’s staff and Volin’s soviets into the open."
  },
  "MKN_congress_of_free_peoples_desc": {
    "ru": "Советы соседних стран не станут нашими филиалами. Общий конгресс установит добровольность соглашений и право каждого отказаться.",
    "en": "Neighbouring councils shall not become our branch offices. A common congress will establish voluntary agreements and the right to refuse."
  },
  "MKN_constituent_assembly": {
    "ru": "Съезд вольных советов",
    "en": "The Congress of Free Soviets"
  },
  "MKN_constituent_assembly_desc": {
    "ru": "Для передачи власти отзывным делегатам советов нужна поддержка не менее 40%. Анархо-коммунизм использует демократическую группу идеологий, но общегосударственные парламентские выборы отключены. Баланс смещается на 0,45 к вольным советам.",
    "en": "At least 40% support is required to entrust authority to recallable council delegates. Anarcho-communism uses the democratic ideology group, while national parliamentary elections remain disabled. The balance shifts by 0.45 toward the free soviets."
  },
  "MKN_construction_drive": {
    "ru": "Напряжённый строительный сезон",
    "en": "Intensive Construction Season"
  },
  "MKN_construction_drive_desc": {
    "ru": "Съезд временно направил дополнительные средства на стройки. Потребительский сектор оплачивает ускорение.",
    "en": "The congress temporarily commits extra resources to construction. Consumer production bears the cost of acceleration."
  },
  "MKN_consular_communes_desc": {
    "ru": "Наши моряки, рабочие и переселенцы не должны оставаться без помощи за границей. Постоянные бюро займутся документами, посредничеством и возвращением граждан домой.",
    "en": "Our sailors, workers and emigrants need assistance abroad. Permanent bureaux will arrange documents, mediation and safe passage home."
  },
  "MKN_consular_communes_tt": {
    "ru": "Внешняя служба коммун: ежемесячное улучшение отношений §G+10%§!.",
    "en": "Communal Foreign Service: monthly opinion gain §G+10%§!."
  },
  "MKN_convene_local_communes": {
    "ru": "Созвать местные коммуны",
    "en": "Convene Local Communes"
  },
  "MKN_convene_local_communes_desc": {
    "ru": "За 50 политической власти сдвиньте баланс на 0,15 к вольным советам. Можно повторить через 60 дней.",
    "en": "Spend 50 PP to move the balance 0.15 toward the free soviets. Repeatable after 60 days."
  },
  "MKN_convoy_control_office_desc": {
    "ru": "Диспетчеры портовых коммун согласуют выходы транспортов, смену охранения и заправку. Хлебные караваны получат надёжный эскорт при меньшем расходе топлива.",
    "en": "Port commune dispatchers will coordinate sailing times, escort rotations and refuelling, protecting grain shipments while using less fuel."
  },
  "MKN_convoy_rescue": {
    "ru": "Спасательная служба конвоев",
    "en": "Convoy Rescue Service"
  },
  "MKN_convoy_rescue_desc": {
    "ru": "Спасательные суда подберут людей и возьмут повреждённые транспорты на буксир.",
    "en": "Rescue vessels will recover crews and tow damaged transports."
  },
  "MKN_convoy_schedules": {
    "ru": "Расписания зерновых конвоев",
    "en": "Grain Convoy Timetables"
  },
  "MKN_convoy_schedules_desc": {
    "ru": "Общие расписания и новые транспорты позволят сопровождать торговлю организованными группами.",
    "en": "Shared schedules and new transports will organize shipping into escorted groups."
  },
  "MKN_cooperative_production": {
    "ru": "Федерация производственных артелей",
    "en": "Federation of Production Artels"
  },
  "MKN_cooperative_production_desc": {
    "ru": "Общие заказы и обмен оснасткой позволяют мастерским быстро осваивать новые образцы.",
    "en": "Shared orders and exchanged tooling let workshops adopt new designs quickly."
  },
  "MKN_coordinated_supply": {
    "ru": "Налаживающееся снабжение",
    "en": "Supply Taking Shape"
  },
  "MKN_coordinated_supply_desc": {
    "ru": "Регулярные рейсы приходят вовремя. Резервные склады и правила военных перевозок завершат реформу.",
    "en": "Regular services arrive on time. Reserve depots and military transport rules will complete the reform."
  },
  "MKN_council_communism": {
    "ru": "Синдикалистская программа",
    "en": "The Syndicalist Program"
  },
  "MKN_council_communism_desc": {
    "ru": "Заводские собрания и крестьянские коммуны согласуют производство через выборных делегатов. Этот вариант анархо-коммунизма усиливает советы на 0,20 без подчинения Москве.",
    "en": "Factory assemblies and peasant communes coordinate production through elected delegates. This alternative within anarcho-communism strengthens the soviets by 0.20 without submitting to Moscow."
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
  "MKN_cult_of_railways_desc": {
    "ru": "Рельсы связывают разрозненные коммуны в сражающуюся территорию. Бронепоезда дешевле на 35%, железнодорожные орудия — на 25%, а их обстрел эффективнее на 25%; строительство железных дорог и узлов снабжения ускорено на 35%.",
    "en": "The rails bind scattered communes into a fighting territory. Armored trains cost 35% less, railway guns cost 25% less and bombard 25% more effectively; railway and supply-hub construction gain 35%."
  },
  "MKN_death_or_freedom_desc": {
    "ru": "Мажор наступает, родные коммуны заняты врагом. Чрезвычайный призыв потребует тяжёлых жертв и расколет мирные собрания.",
    "en": "A great power advances and our home communes are occupied. Emergency recruitment will demand sacrifices and divide the peaceful assemblies."
  },
  "MKN_decaying_batko": {
    "ru": "Угасающий Батько",
    "en": "The Failing Batko"
  },
  "MKN_decaying_batko_desc": {
    "ru": "Ухудшение здоровья основателя стало болезнью самой революции. Приказы запаздывают, советы ссорятся, походные колонны теряют сплочённость. Этот дух исчезнет со смертью Махно.",
    "en": "The founder’s failing health has become the failing health of the revolution. Orders stall, councils quarrel and marching columns lose cohesion. This spirit ends with Makhno’s death."
  },
  "MKN_deep_reserves": {
    "ru": "Резерв второго эшелона",
    "en": "Second Echelon Reserve"
  },
  "MKN_deep_reserves_desc": {
    "ru": "Второй эшелон получит оружие заранее, чтобы поддерживать прорыв без пауз.",
    "en": "Arm the second echelon early to sustain a breakthrough without pauses."
  },
  "MKN_democratic_successor_desc": {
    "ru": "Волин выступает от имени отзывных местных делегатов и свободных объединений.",
    "en": "Volin speaks for recallable local delegates and free association."
  },
  "MKN_departure_of_batko_desc": {
    "ru": "Этот фокус завершается событием смерти Махно. Его гроб закрывает эпоху, но не спор. У нас 180 дней на решение вопроса о преемственности, прежде чем степь расколется на вооружённые лагеря.",
    "en": "This focus is completed by Makhno’s death event. His coffin closes an age, not an argument. There are 180 days to settle the succession before the steppe splits into armed camps."
  },
  "MKN_depth_charge_school": {
    "ru": "Школа глубинных бомб",
    "en": "Depth Charge School"
  },
  "MKN_depth_charge_school_desc": {
    "ru": "Гидроакустики и расчёты глубинных бомб будут работать одной командой.",
    "en": "Sonar operators and depth-charge crews will work as one team."
  },
  "MKN_disrupt_enemy_trade": {
    "ru": "Срыв вражеской торговли",
    "en": "Disrupt Enemy Trade"
  },
  "MKN_disrupt_enemy_trade_desc": {
    "ru": "Распределим районы охоты, чтобы лишать противника снабжения систематически.",
    "en": "Assign hunting areas to disrupt enemy supplies systematically."
  },
  "MKN_dmitruk_tratishov": {
    "ru": "Дмитрук Тратишов",
    "en": "Dmitruk Tratishov"
  },
  "MKN_dneprostroi_desc": {
    "ru": "Коммуны поручат общему совету крупные стройки, оставив сметы открытыми делегатам. Единый план свяжет металлургию, энергетику и транспорт; путь вольных кооперативов станет недоступен.",
    "en": "Open accounts and elected delegates will oversee a common plan for heavy industry, power and transport. This choice excludes the free cooperatives."
  },
  "MKN_dneprostroi_power": {
    "ru": "Электросеть Днепростроя",
    "en": "Dnieper Power Network"
  },
  "MKN_dneprostroi_power_desc": {
    "ru": "Общая электросеть снижает потребление энергии заводами и ускоряет строительство.",
    "en": "A shared grid reduces factory energy consumption and speeds construction."
  },
  "MKN_dnieper_audit_desc": {
    "ru": "Инженеры ответят перед хозяйственным съездом за каждую машину и рабочую смену. Учреждаем проектное бюро и новую фабрику; делегаты выберут строительный сезон или бережливое переоснащение на один год.",
    "en": "Engineers will answer to the congress for every machine and shift. A design office and civilian factory support recovery; delegates choose a year of accelerated construction or careful investment."
  },
  "MKN_dnieper_economy": {
    "ru": "Днепровский хозяйственный договор",
    "en": "Dnieper Economic Compact"
  },
  "MKN_dnieper_economy_desc": {
    "ru": "Общий план основан на мандатах коммун, открытых сметах и обеспечении семей. Крупные проекты больше не питаются случайными сборами.",
    "en": "A shared plan rests on communal mandates, public budgets and family support. Major projects no longer depend on improvised collections."
  },
  "MKN_dnieper_gun_flotilla": {
    "ru": "Днепровские канонерки",
    "en": "Dnieper Gunboats"
  },
  "MKN_dnieper_gun_flotilla_desc": {
    "ru": "Речные экипажи перейдут на лёгкие мореходные корабли для прибрежной службы.",
    "en": "River crews will move to light sea-going ships for coastal service."
  },
  "MKN_dnieper_jet_falcons_desc": {
    "ru": "Днепровские мастерские переходят от поршней к реактивной тяге. Общая программа даст скидку на реактивные технологии и улучшит манёвренность авиации.",
    "en": "Dnieper workshops move from pistons to jet propulsion. A common programme will accelerate jet research and improve aircraft agility."
  },
  "MKN_dnieper_logistics": {
    "ru": "Днепровская транспортная служба",
    "en": "Dnieper Transport Service"
  },
  "MKN_dnieper_logistics_desc": {
    "ru": "Диспетчерская сеть и зерновые резервы поддерживают большие соединения на дальних маршрутах.",
    "en": "A dispatch network and grain reserves sustain large formations on distant routes."
  },
  "MKN_dnieper_logistics_hub_desc": {
    "ru": "Диспетчеры сведут речные, железнодорожные и заводские расписания. На карте станут доступны три проекта: Кичкасский мост, расчистка Днепра и степные узловые станции. Каждая стройка длится 60 дней.",
    "en": "Dispatchers coordinate river, rail and factory schedules. Unlock three 60-day map projects: Kichkas Bridge, Dnieper waterways and steppe junctions."
  },
  "MKN_dnieper_patrol": {
    "ru": "Днепровский дозор",
    "en": "Dnieper Patrol"
  },
  "MKN_dnieper_patrol_desc": {
    "ru": "Днепровские дозоры станут школой будущих морских экипажей.",
    "en": "Dnieper patrols will train the future sea-going crews."
  },
  "MKN_dnieper_workshop_federation_desc": {
    "ru": "Киев и Черкассы войдут в хозяйственную федерацию на правах национальных областей. Восстановленная оружейная линия и общий портфель заказов усилят выпуск.",
    "en": "Kyiv and Cherkasy join the economic federation as core states. A restored arms line and shared orders improve production."
  },
  "MKN_drilled_militias": {
    "ru": "Ополчение на общих учениях",
    "en": "Militias on Joint Exercises"
  },
  "MKN_drilled_militias_desc": {
    "ru": "Инструкторы дали отрядам общую подготовку. Постоянная организация резерва закрепит результат.",
    "en": "Instructors have provided common training. A permanent reserve organization will secure these gains."
  },
  "MKN_economic_congress_category": {
    "ru": "Хозяйственный конгресс",
    "en": "Economic Congress"
  },
  "MKN_economic_congress_category_desc": {
    "ru": "Артели оплачивают общие программы из собственных средств. Каждая инициатива принимается один раз; длительные стройки выдают награду по завершении.",
    "en": "Artels pay for common programmes. Each initiative may be completed once; construction rewards arrive when the work ends."
  },
  "MKN_economic_congress_unlock_tt": {
    "ru": "Открывает решения §Y«Хозяйственного конгресса»§!: соляные артели, отзывные командиры, ветряки, хлебная политика и взаимное страхование.",
    "en": "Unlocks the §YEconomic Congress§!: salt artels, recallable commanders, windmills, grain policy and mutual insurance."
  },
  "MKN_economic_coordination": {
    "ru": "Первые хозяйственные соглашения",
    "en": "First Economic Agreements"
  },
  "MKN_economic_coordination_desc": {
    "ru": "Коммуны признали общие обязательства, но хлеб, станки и труд ещё распределяются с задержками.",
    "en": "The communes recognize shared obligations, but grain, machinery and labour still arrive late."
  },
  "MKN_economic_recovery": {
    "ru": "Хозяйство на пути к восстановлению",
    "en": "An Economy in Recovery"
  },
  "MKN_economic_recovery_desc": {
    "ru": "Согласованные заказы сокращают потери. Остаётся закрепить правила расчётов и обеспечить семьи работников.",
    "en": "Agreed orders reduce waste. Settlement rules and support for workers' families still need lasting institutions."
  },
  "MKN_electrified_steppe": {
    "ru": "Электрифицированная степь",
    "en": "The Electrified Steppe"
  },
  "MKN_electrified_steppe_desc": {
    "ru": "Хата с лампой и грамота в каждой волости.",
    "en": "A hut with a lamp and an alphabet book in every volost."
  },
  "MKN_embassy_to_kharkov_desc": {
    "ru": "Упраздним баланс сил и отправим делегацию в советские республики. Первое предложение предусматривает взаимный военный транзит и обмен зерна на снабжение; Харьков вправе отказать.",
    "en": "Disband the balance of power and send a delegation to the Soviet Republics. The first proposal offers reciprocal military transit and a grain-for-supply agreement; Kharkov may refuse."
  },
  "MKN_emergency_revkom_desc": {
    "ru": "Красные делегаты требуют администрации, способной пережить своего основателя. При подготовленном съезде и поддержке не менее 40% государственный социализм станет правящей программой.",
    "en": "The red delegates demand an administration that can survive its founder. With a prepared congress and at least 40% support, state socialism becomes the ruling program."
  },
  "MKN_empower_atamans": {
    "ru": "Усилить атаманов",
    "en": "Empower the Atamans"
  },
  "MKN_empower_atamans_desc": {
    "ru": "За 50 политической власти сдвиньте баланс на 0,15 к военному командованию. Можно повторить через 60 дней.",
    "en": "Spend 50 PP to move the balance 0.15 toward the military command. Repeatable after 60 days."
  },
  "MKN_energy_projects_unlock_tt": {
    "ru": "Открывает три §Y60-дневных проекта§!: турбины (226), электросеть (200), угольные линии (196). Каждый временно занимает §Y2 гражданские фабрики§!.",
    "en": "Unlocks three §Y60-day projects§!: turbines (226), power grid (200), coal lines (196). Each temporarily uses §Y2 civilian factories§!."
  },
  "MKN_equal_autonomy": {
    "ru": "Равноправная автономия ратифицирована",
    "en": "Equal autonomy was ratified"
  },
  "MKN_escort_compact_desc": {
    "ru": "Основная система эскорта готова; противолодочные и спасательные службы можно расширять дальше. Дополнительные тактики приобретаются отдельно в полевом штабе.",
    "en": "The core escort system is ready, with room to expand anti-submarine and rescue services. Further tactics can be purchased separately at the field headquarters."
  },
  "MKN_escort_crews": {
    "ru": "Школа экипажей эскортов",
    "en": "Escort Crew School"
  },
  "MKN_escort_crews_desc": {
    "ru": "Экипажи отработают охранение медленных транспортов вместо погони за славой.",
    "en": "Crews will train to protect slow transports rather than chase glory."
  },
  "MKN_escort_radio_net": {
    "ru": "Радиосеть охранения",
    "en": "Escort Radio Network"
  },
  "MKN_escort_radio_net_desc": {
    "ru": "Общая частота охранения позволит быстро перестроить защитный экран.",
    "en": "A shared escort frequency will help ships reorganize their protective screen."
  },
  "MKN_escort_repair_network_focus_desc": {
    "ru": "Расчищенные фарватеры ускорят оборот кораблей и портовое снабжение.\\n\\nСудоремонтные артели освоят замену повреждённых секций и переоборудование.\\n\\nОбщие расписания и новые транспорты позволят сопровождать торговлю организованными группами.",
    "en": "Dredged channels will improve ship turnaround and harbour logistics.\\n\\nRepair cooperatives will learn hull repairs and refitting.\\n\\nShared schedules and new transports will organize shipping into escorted groups."
  },
  "MKN_escort_reserves": {
    "ru": "Резерв портовых экипажей",
    "en": "Port Crew Reserve"
  },
  "MKN_escort_reserves_desc": {
    "ru": "Резерв экипажей и дополнительная верфь обеспечат замену потерь.",
    "en": "Reserve crews and an additional yard will replace losses."
  },
  "MKN_evacuation_columns": {
    "ru": "Санитарные колонны советов",
    "en": "Council Medical Columns"
  },
  "MKN_evacuation_columns_desc": {
    "ru": "В течение 180 дней советы возвращают больше раненых бойцов домой.",
    "en": "For 180 days, local councils bring more wounded fighters home."
  },
  "MKN_everlasting_makhnovshchina": {
    "ru": "Махновская традиция",
    "en": "The Makhnovist Tradition"
  },
  "MKN_everlasting_makhnovshchina_desc": {
    "ru": "Съезд может вновь пригласить Махно как гражданского делегата без восстановления его военной должности. Добровольная оборона и автономия общин усиливают советы на 0,20.",
    "en": "The congress may invite Makhno back as a civilian delegate, without restoring his military office. Voluntary defence and communal autonomy strengthen the soviets by 0.20."
  },
  "MKN_every_farm_a_fortress_desc": {
    "ru": "Подвалы станут складами боеприпасов, изгороди скроют огневые позиции. Построим два уровня сухопутных укреплений вдоль границ принадлежащих нам и контролируемых нами областей.",
    "en": "Cellars become ammunition stores; hedges conceal firing positions. Build two levels of land forts along the borders of states we own and control."
  },
  "MKN_export_contracts": {
    "ru": "Артельные экспортные договоры",
    "en": "Artel Export Contracts"
  },
  "MKN_export_contracts_desc": {
    "ru": "Экспорт оплачивает оборудование, но переговоры и проверки связывают силы делегатов.",
    "en": "Exports pay for machinery, but negotiations and inspections occupy the delegates."
  },
  "MKN_expropriated_funds": {
    "ru": "Экспроприированные средства",
    "en": "Expropriated Funds"
  },
  "MKN_expropriated_funds_desc": {
    "ru": "Зарубежные экспроприации оплачивают заказы независимым мастерским. Успешные налёты на разные страны суммируют аренду фабрик; каждый следующий успех во время её действия добавляет девяносто дней.",
    "en": "Foreign expropriations finance contracts with independent workshops. Successful raids on different countries accumulate factory leases; each further success during the lease adds ninety days."
  },
  "MKN_expropriated_funds_factories_tt": {
    "ru": "Арендованные внекартовые гражданские фабрики: §G+[?MKN_expropriation_factories|0]§!. Все снимаются по истечении срока духа.",
    "en": "Leased off-map civilian factories: §G+[?MKN_expropriation_factories|0]§!. All are removed when this spirit expires."
  },
  "MKN_extra_workshop_shifts": {
    "ru": "Реквизированные смены мастерских",
    "en": "Requisitioned Workshop Shifts"
  },
  "MKN_extra_workshop_shifts_desc": {
    "ru": "Выпуск вооружения растёт, пока общины несут дополнительные гражданские обязательства.",
    "en": "Military output rises as the communes shoulder additional civilian obligations."
  },
  "MKN_fascism_successor_desc": {
    "ru": "Дмитрук Тратишов возглавляет анархо-милитаристов Чёрного штаба. Он обещает связать вольные отряды единым командованием, подчинить мастерские фронту и удержать территорию силой. Его власть требует подготовленного съезда и поддержки не менее 40% населения; армейская дисциплина не заменяет политического мандата.",
    "en": "Dmitruk Tratishov leads the Black Staff’s anarcho-militarists. He promises unified command, workshops serving the front and a territory held together by force. His accession requires a prepared congress and at least 40% public support; military discipline cannot replace a political mandate."
  },
  "MKN_fast_attack_craft": {
    "ru": "Быстрые торпедные катера",
    "en": "Fast Torpedo Craft"
  },
  "MKN_fast_attack_craft_desc": {
    "ru": "Быстрые катера прикроют выход рейдеров и атакуют в тесных прибрежных водах.",
    "en": "Fast craft will cover raider departures and fight in restricted coastal waters."
  },
  "MKN_federal_republic": {
    "ru": "Федеративная республика",
    "en": "Federal Republic"
  },
  "MKN_federal_republic_desc": {
    "ru": "Политическая программа завершена: новое устройство закрепляет порядок и распределение полномочий.",
    "en": "The completed political programme establishes a durable division of powers and responsibilities."
  },
  "MKN_federation_of_free_councils_desc": {
    "ru": "Региональные договоры станут общим федеративным уставом. Стабильность, снабжение и производственная эффективность закрепят интеграцию через единый хозяйственный дух.",
    "en": "Regional compacts become a common federal charter. Stability, supply and production efficiency consolidate integration through the shared economic spirit."
  },
  "MKN_field_schools_desc": {
    "ru": "Передвижные инструкторы и сменяемые командиры обучат самооборону связи, маскировке и совместному манёвру. Подготовка станет короче, а отряды сохранят подвижность и связь со своими коммунами.",
    "en": "Travelling instructors and recallable commanders train local defence in signals, concealment and coordinated manoeuvre. Units train faster while retaining their mobility and communal ties."
  },
  "MKN_field_veterinary": {
    "ru": "Ветеринарная служба колонн",
    "en": "Column Veterinary Service"
  },
  "MKN_field_veterinary_desc": {
    "ru": "Ветеринарная служба снизит потери лошадей в длительных переходах.",
    "en": "Veterinary teams will reduce horse losses on long marches."
  },
  "MKN_fighter_controllers": {
    "ru": "Диспетчеры воздушного боя",
    "en": "Fighter Controllers"
  },
  "MKN_fighter_controllers_desc": {
    "ru": "Диспетчеры распределят звенья по целям, исключая бесполезное дублирование.",
    "en": "Controllers will assign flights to targets without wasteful duplication."
  },
  "MKN_fighter_conversion": {
    "ru": "Переучивание лётчиков",
    "en": "Pilot Conversion Training"
  },
  "MKN_fighter_conversion_desc": {
    "ru": "Переучивание позволит быстро освоить следующее поколение истребителей.",
    "en": "Conversion training will speed adoption of the next fighter generation."
  },
  "MKN_fighter_instructors": {
    "ru": "Инструкторы воздушного боя",
    "en": "Air Combat Instructors"
  },
  "MKN_fighter_instructors_desc": {
    "ru": "Лучшие инструкторы покажут молодым пилотам приёмы боя в паре.",
    "en": "Veteran instructors will teach new pilots how to fight in pairs."
  },
  "MKN_fighter_patrols": {
    "ru": "Патрули над переправами",
    "en": "Patrols over River Crossings"
  },
  "MKN_fighter_patrols_desc": {
    "ru": "Патрули над переправами прикроют связь между промышленными районами.",
    "en": "Patrols over crossings will protect links between industrial districts."
  },
  "MKN_fire_tables": {
    "ru": "Общие таблицы огня",
    "en": "Common Fire Tables"
  },
  "MKN_fire_tables_desc": {
    "ru": "Единые таблицы стрельбы свяжут огонь батарей с планами танковых командиров.",
    "en": "Common firing tables will align battery fire with armoured commanders' plans."
  },
  "MKN_fleet_damage_control": {
    "ru": "Артели аварийного ремонта",
    "en": "Repair and Salvage Artels"
  },
  "MKN_fleet_damage_control_desc": {
    "ru": "Аварийные команды спасут корабль после попадания и вернут его в порт.",
    "en": "Damage-control teams will save hit ships and bring them home."
  },
  "MKN_flexible_orders": {
    "ru": "Задача вместо длинного приказа",
    "en": "Mission over Lengthy Orders"
  },
  "MKN_flexible_orders_desc": {
    "ru": "Командир получит цель и свободу исполнения вместо цепочки мелких приказов.",
    "en": "Commanders will receive objectives and freedom of execution rather than constant detailed orders."
  },
  "MKN_flying_artillery": {
    "ru": "Летающая артиллерия",
    "en": "Flying Artillery"
  },
  "MKN_flying_artillery_desc": {
    "ru": "Тяжёлое вооружение штурмовиков поможет разрушать узлы сопротивления.",
    "en": "Heavier aircraft armament will break enemy strongpoints."
  },
  "MKN_flying_artillery_focus_desc": {
    "ru": "Авиация станет летающей артиллерией для вольных колонн.\\n\\n«Днепровское крыло» приспособит лёгкие самолёты для ударов по наземным целям.\\n\\nТяжёлое вооружение штурмовиков поможет разрушать узлы сопротивления.\\n\\nНа полигонах экипажи научатся поражать цель рядом со своими войсками.",
    "en": "Aviation will become flying artillery for the free columns.\\n\\nDnipro Wing cooperatives will adapt light aircraft for ground attack.\\n\\nHeavier aircraft armament will break enemy strongpoints.\\n\\nRange training will teach crews to strike targets close to friendly troops."
  },
  "MKN_focus": {
    "ru": "Махновская вольница",
    "en": "Makhnovist Free Territory"
  },
  "MKN_focus_desc": {
    "ru": "Дерево фокусов Махновской вольной территории.",
    "en": "The national focus tree of the Makhnovist Free Territory."
  },
  "MKN_foreign_delegates_desc": {
    "ru": "После ухода Батьки за границей должны слышать не отдельную фракцию, а всю Вольную территорию. Сеть сменяемых представителей будет поддерживать постоянные связи при любом правительстве.",
    "en": "After Batko’s departure, our neighbours must hear the Free Territory as a whole. Recallable representatives will maintain foreign contacts under every successor government."
  },
  "MKN_foreign_delegates_tt": {
    "ru": "Постоянный дух §YВнешняя служба коммун§!: стоимость поддержания улучшения отношений §G−10%§!.",
    "en": "Permanent §YCommunal Foreign Service§!: improve relations maintenance cost §G−10%§!."
  },
  "MKN_foreign_service": {
    "ru": "Внешняя служба коммун",
    "en": "Communal Foreign Service"
  },
  "MKN_foreign_service_desc": {
    "ru": "Общая сеть представителей, технических связей и взаимной защиты. Её возможности последовательно расширяются внешнеполитическими фокусами.",
    "en": "A common network of representatives, technical contacts and mutual protection, developed through successive foreign policy focuses."
  },
  "MKN_forward_airstrips": {
    "ru": "Передовые посадочные полосы",
    "en": "Forward Airstrips"
  },
  "MKN_forward_airstrips_desc": {
    "ru": "Передовые полосы сократят время между запросом поддержки и ударом.",
    "en": "Forward strips will shorten the delay between a support request and the strike."
  },
  "MKN_forward_airstrips_focus_desc": {
    "ru": "Передовые полосы сократят время между запросом поддержки и ударом.\\n\\nСвязные передадут запросы пехоты прямо на аэродром.",
    "en": "Forward strips will shorten the delay between a support request and the strike.\\n\\nLiaison teams will carry infantry requests directly to the airfields."
  },
  "MKN_found_black_international": {
    "ru": "Учредить Чёрный Интернационал",
    "en": "Found the Black International"
  },
  "MKN_found_black_international_desc": {
    "ru": "За 100 PP создадим собственный альянс, если свободны от обязательств перед другой фракцией. Мы не разрываем существующие союзы за другие страны.",
    "en": "For 100 PP, establish our own faction if we are independent and outside any existing faction."
  },
  "MKN_fragmented_workshops": {
    "ru": "Разрозненные мастерские",
    "en": "Fragmented Workshops"
  },
  "MKN_fragmented_workshops_desc": {
    "ru": "Каждая артель использует свои чертежи и калибры. Серийное производство буксует, а технические знания редко выходят за ворота мастерской.",
    "en": "Each artel uses its own drawings and calibres. Serial production stalls and technical knowledge rarely leaves the workshop."
  },
  "MKN_free_airmen": {
    "ru": "Вольные лётчики",
    "en": "Free Airmen"
  },
  "MKN_free_airmen_desc": {
    "ru": "Ловить воздушные течения, а не приказы.",
    "en": "Chase air currents, not orders."
  },
  "MKN_free_army_compact_desc": {
    "ru": "Вольные колонны готовы к походу; дополнительные службы можно развивать по нуждам фронта. Дополнительные тактики приобретаются отдельно в полевом штабе.",
    "en": "The free columns are ready; additional services can develop according to front-line needs. Further tactics can be purchased separately at the field headquarters."
  },
  "MKN_free_column_command_focus_desc": {
    "ru": "Разведывательные партии расчистят путь основной колонне.\\n\\nСигнальные команды свяжут волости и выведут резерв на нужный участок.",
    "en": "Small scouting parties will clear the route for the main column.\\n\\nSignals teams will connect districts and bring reserves to the right sector."
  },
  "MKN_free_column_exercises": {
    "ru": "Сборы вольных колонн",
    "en": "Free Column Exercises"
  },
  "MKN_free_column_exercises_desc": {
    "ru": "Сборы сведут конные и пешие отряды в согласованные колонны.",
    "en": "Joint exercises will coordinate mounted and dismounted detachments."
  },
  "MKN_free_cooperatives_desc": {
    "ru": "Артели сохранят самостоятельность и примут взаимные обязательства по снабжению и заказам. Хозяйственный кризис ослабнет; централизованный путь Днепростроя станет недоступен.",
    "en": "Independent artels accept mutual supply and production obligations. The economic crisis eases; this choice excludes the Dnieper industrial program."
  },
  "MKN_free_elections_steppe": {
    "ru": "Отзывные мандаты общин",
    "en": "Recallable Communal Mandates"
  },
  "MKN_free_elections_steppe_desc": {
    "ru": "Каждая коммуна избирает и отзывает своих делегатов. Федерация получает устойчивые мандаты без постоянного парламента. Вольные советы получают ещё 0,20 на шкале баланса.",
    "en": "Each commune elects and may recall its delegates. The federation receives reliable mandates without creating a permanent parliament. Free soviets gain another 0.20 on the balance scale."
  },
  "MKN_free_industry_modifier": {
    "ru": "Хозяйство вольной территории",
    "en": "Economy of the Free Territory"
  },
  "MKN_free_industry_modifier_desc": {
    "ru": "Хозяйственные соглашения, производство и снабжение коммун развиваются вместе. Съезды постепенно преодолевают стартовые ограничения и закрепляют преимущества выбранной программы.",
    "en": "Communal agreements, production and supply develop together. Congresses overcome initial limitations and secure the benefits of their chosen program."
  },
  "MKN_free_mint_idea": {
    "ru": "Свободный монетный двор",
    "en": "Free Mint"
  },
  "MKN_free_mint_idea_desc": {
    "ru": "Вольная валюта степи даёт вольной земле власть и ловкость жонглёра.",
    "en": "The free currency of the steppe gives the free land agility and a juggling treasurer."
  },
  "MKN_free_peoples_congress_tt": {
    "ru": "Подготавливает добровольный пакт. Вступление других стран потребует отдельного приглашения и их согласия.",
    "en": "Prepares a voluntary pact. Other countries must receive an invitation and consent to membership."
  },
  "MKN_free_science_network_desc": {
    "ru": "Объединим политехникум и исследовательские коммуны в сеть вольных институтов. Вторая дополнительная группа доведёт общую научную мощность до пяти ячеек. Шестую даст Киевский научный обмен после интеграции Украины.",
    "en": "Unite the polytechnic and research communes into a network of free institutes. A second additional team raises scientific capacity to five slots. Kyiv Scientific Exchange will provide the sixth after Ukrainian integration."
  },
  "MKN_free_sky_compact_desc": {
    "ru": "Основная система перехвата готова; ночные и радиолокационные службы останутся дополнительными. Дополнительные тактики приобретаются отдельно в полевом штабе.",
    "en": "The core interception system is ready, with night and radar services available as extensions. Further tactics can be purchased separately at the field headquarters."
  },
  "MKN_free_soviets_idea": {
    "ru": "Упорядоченные вольные советы",
    "en": "Organized Free Soviets"
  },
  "MKN_free_soviets_idea_desc": {
    "ru": "Отзывные делегаты укрепляют доверие к общим решениям, сохраняя самостоятельность коммун.",
    "en": "Recallable delegates build trust in common decisions while preserving communal autonomy."
  },
  "MKN_free_soviets_side": {
    "ru": "Вольные советы — Волин",
    "en": "Free Soviets — Volin"
  },
  "MKN_free_territory": {
    "ru": "Вольная территория",
    "en": "Free Territory"
  },
  "MKN_free_territory_desc": {
    "ru": "Взаимопомощь и добровольная защита объединяют коммуны. Отряды знают родную степь и сражаются за свою землю; съездам предстоит сделать общие обязательства столь же надёжными.",
    "en": "Mutual aid and voluntary defence unite the communes. The detachments know their native steppe and fight for their land; congresses must make shared obligations equally reliable."
  },
  "MKN_free_workshops": {
    "ru": "Вольные мастерские",
    "en": "Free Workshops"
  },
  "MKN_free_workshops_focus_desc": {
    "ru": "После завершения Днепростроя или программы вольных кооперативов объединим мастерские Екатеринослава и Гуляйполя в общую инженерную сеть. Она откроет предприятие и станет основой технических коммун и вольных институтов.",
    "en": "After completing Dneprostroi or the free cooperatives programme, unite the Ekaterinoslav and Huliaipole workshops into a common engineering network, opening the enterprise and the path to technical communes and free institutes."
  },
  "MKN_free_workshops_unlock_tt": {
    "ru": "Открывает промышленный концерн и военно-промышленную организацию «Вольные мастерские».",
    "en": "Unlocks the Free Workshops industrial concern and military industrial organization."
  },
  "MKN_freight_logistics_desc": {
    "ru": "Обозные артели и ремонтные биржи распределят склады между хуторами. Договоры подвоза резко сократят расход снабжения и истощение, а резервный уголь обеспечит мастерские.",
    "en": "Freight artels and repair exchanges distribute depots among the villages. Supply agreements sharply reduce consumption and attrition while reserve coal keeps workshops running."
  },
  "MKN_frontier_year_countdown_mission": {
    "ru": "Год на рубеже",
    "en": "One Year on the Frontier"
  },
  "MKN_frontier_year_countdown_mission_desc": {
    "ru": "Первая провокация Советской Украины начинает §Y365 дней§! приграничного кризиса. При полной войне с UKR или SOV отсчёт прекращается. Иначе по истечении срока вводится пакт о ненападении с UKR на §Y730 дней§!, сохраняются все захваченные национальные регионы MKN и замораживаются дальнейшие столкновения.",
    "en": "The first Soviet Ukrainian provocation starts §Y365 days§! of frontier crisis. If full war with UKR or SOV begins, this countdown ends. Otherwise the deadline imposes a §Y730-day§! non-aggression pact with UKR, preserves every captured MKN core and freezes further skirmishes."
  },
  "MKN_fuel_discipline": {
    "ru": "Учёт горючего в походе",
    "en": "Fuel Accounting on Campaign"
  },
  "MKN_fuel_discipline_desc": {
    "ru": "Запас горючего и маршруты заправки избавят наступление от пустых баков.",
    "en": "Fuel reserves and refuelling routes will prevent stalled offensives."
  },
  "MKN_fund_the_underground_desc": {
    "ru": "Местные проводники, тайники и добровольные комитеты помогут нашим колоннам действовать за пределами родной земли.",
    "en": "Local guides, caches and voluntary committees will help our columns operate beyond their home territory."
  },
  "MKN_galician_agitation_unlock_tt": {
    "ru": "Открывает помощь сельским союзам Галиции и Буковины: 50 PP и 200 винтовок на 45 дней. Подготовленный австрийский регион при общей границе может стать целью пограничного конфликта за 100 PP.",
    "en": "Unlocks support for rural unions in Galicia and Bucovina: 50 PP and 200 rifles for 45 days. A prepared Austrian state bordering us can then be contested for 100 PP."
  },
  "MKN_galician_border_action": {
    "ru": "Поддержать восстание: [FROM.GetName]",
    "en": "Support the Rising: [FROM.GetName]"
  },
  "MKN_galician_border_action_desc": {
    "ru": "100 PP. Требуются вооружённые сельские союзы, австрийское владение и контроль региона, общая граница и мир между сторонами. Победа в пограничном конфликте передаёт спорный регион без национализации.",
    "en": "100 PP. Requires armed rural unions, Austrian ownership and control, a shared border and peace between both sides. Winning the border conflict transfers the contested state without granting a core."
  },
  "MKN_galician_peasants_desc": {
    "ru": "Габсбурги могут собирать коронные земли, но не могут владеть трудом их жителей. Сельские союзы Галиции и Буковины получат нашу помощь.",
    "en": "The Habsburgs may gather crownlands, but they cannot own their inhabitants' labour. Rural unions in Galicia and Bucovina shall receive our support."
  },
  "MKN_global_syndicalist_pact_desc": {
    "ru": "Чёрный Интернационал станет союзом по согласию, а не империей под новым флагом. Наши добровольцы помогут коммунистическим и демократическим участникам гражданских войн.",
    "en": "The Black International shall be a consensual association, not an empire under another flag. Our volunteers will aid communist and democratic participants in civil wars."
  },
  "MKN_grain_exchanges_desc": {
    "ru": "Фабрика в Херсоне поддержит переработку и обмен урожая. На карте открываются три проекта по 60 дней: запорожские элеваторы, херсонские зерновые терминалы и степная посевная. Политику запасов выбирает хозяйственный конгресс.",
    "en": "A Kherson factory supports processing and exchange. Unlock three 60-day map projects: Zaporizhzhia elevators, Kherson grain terminals and steppe sowing. The Economic Congress chooses stockpile policy."
  },
  "MKN_grain_projects_unlock_tt": {
    "ru": "Открывает три §Y60-дневных проекта на карте§!: элеваторы (226), херсонские терминалы (196), посевная (1082).",
    "en": "Unlocks three §Y60-day map projects§!: elevators (226), Kherson terminals (196), steppe sowing (1082)."
  },
  "MKN_grain_ultimatum_desc": {
    "ru": "Сёла прокормят общую оборону, но никогда — четыре соперничающих штаба. Их ультиматум разрешит вопрос преемственности и остановит отсчёт до гражданской войны.",
    "en": "The villages will feed a common defense, never four rival headquarters. Their ultimatum settles the succession and stops the civil-war countdown."
  },
  "MKN_gulyaipole_pilot_school": {
    "ru": "Гуляйпольская школа лётчиков",
    "en": "Gulyai Polye Pilot School"
  },
  "MKN_gulyaipole_pilot_school_desc": {
    "ru": "Школа лётчиков даст общую подготовку перед выбором боевой специализации.",
    "en": "The pilot school will provide common training before combat specialization."
  },
  "MKN_harbor_spartacist_engineers": {
    "ru": "Укрыть немецких инженеров-спартаковцев",
    "en": "Harbor German Spartacist Engineers"
  },
  "MKN_harbor_spartacist_engineers_desc": {
    "ru": "Инженеры, спасающиеся от политического преследования, организуют оружейную мастерскую: одна вне-картовая военная фабрика на 180 дней.",
    "en": "Engineers escaping political persecution will organize a temporary armaments workshop: one off-map military factory for 180 days."
  },
  "MKN_harbour_dredging": {
    "ru": "Расчистка портовых фарватеров",
    "en": "Harbour Channel Dredging"
  },
  "MKN_harbour_dredging_desc": {
    "ru": "Расчищенные фарватеры ускорят оборот кораблей и портовое снабжение.",
    "en": "Dredged channels will improve ship turnaround and harbour logistics."
  },
  "MKN_hidden_anchorages": {
    "ru": "Скрытые рейдерские стоянки",
    "en": "Hidden Raider Anchorages"
  },
  "MKN_hidden_anchorages_desc": {
    "ru": "Тайные стоянки позволят подготовить выход, не выдавая расположение рейдеров.",
    "en": "Concealed anchorages will prepare sorties without exposing raider positions."
  },
  "MKN_hidden_depots": {
    "ru": "Скрытые сельские склады",
    "en": "Hidden Village Depots"
  },
  "MKN_hidden_depots_desc": {
    "ru": "Сеть тайных складов поддержит колонны вдали от железной дороги.",
    "en": "Hidden depots will sustain columns operating far from the railway."
  },
  "MKN_hidden_smuggler_bases_focus_desc": {
    "ru": "Тайные стоянки позволят подготовить выход, не выдавая расположение рейдеров.\\n\\nКарты торговых маршрутов укажут ценные цели и безопасные районы ожидания.\\n\\nЛиманские мастерские наладят серийное строительство малых подлодок.\\n\\nНочные выходы сократят время, когда рейдер виден береговым наблюдателям.\\n\\nСкрытые топливные запасы увеличат время охоты на торговых путях.",
    "en": "Concealed anchorages will prepare sorties without exposing raider positions.\\n\\nShipping intelligence will identify valuable targets and safe waiting areas.\\n\\nEstuary workshops will organize serial construction of small submarines.\\n\\nNight sorties will reduce exposure to coastal observers.\\n\\nConcealed fuel reserves will extend patrols along shipping routes."
  },
  "MKN_hidden_supply_bases_focus_desc": {
    "ru": "Местные проводники найдут броды и обходные тропы раньше противника.\\n\\nВетеринарная служба снизит потери лошадей в длительных переходах.",
    "en": "Local guides will locate fords and flanking routes before the enemy.\\n\\nVeterinary teams will reduce horse losses on long marches."
  },
  "MKN_hidden_workshops": {
    "ru": "Подпольные арсеналы",
    "en": "Underground Arsenals"
  },
  "MKN_hidden_workshops_desc": {
    "ru": "Три внекарточных военных завода работают в укрытиях. Строительство замедлено на 20%. Дух сохраняет производство и строительный штраф после окончания войны.",
    "en": "Three off-map military factories operate in hiding. Construction is 20% slower. The factories and construction penalty persist after peace returns."
  },
  "MKN_historical": {
    "ru": "MKN: красный компромисс",
    "en": "MKN: the Red Compromise"
  },
  "MKN_historical_desc": {
    "ru": "Подготовить съезд, урегулировать преемственность и договориться о равноправном сотрудничестве с советскими республиками.",
    "en": "Prepare the congress, settle the succession and negotiate equal cooperation with the Soviet Republics."
  },
  "MKN_horizons_200_rifles": {
    "ru": "£infantry_equipment_text_icon §Y200§!",
    "en": "£infantry_equipment_text_icon §Y200§!"
  },
  "MKN_horizons_black_international": {
    "ru": "Чёрный Интернационал",
    "en": "Black International"
  },
  "MKN_horizons_international_category": {
    "ru": "Набат за рубежом",
    "en": "Nabat Abroad"
  },
  "MKN_horizons_international_category_desc": {
    "ru": "Стачки, сельские союзы и добровольная дипломатия Чёрного Интернационала. Вооружённая поддержка требует средств и времени; друзья и участники пактов защищены.",
    "en": "Strikes, rural unions and voluntary diplomacy for the Black International. Armed support costs time and resources; allies and pact partners are protected."
  },
  "MKN_huliaipole_reactor_project": {
    "ru": "Реакторный проект Гуляйполя",
    "en": "Huliaipole Reactor Project"
  },
  "MKN_huliaipole_reactor_project_desc": {
    "ru": "Один проект за кампанию: 100 PP и 5 гражданских фабрик на 90 дней. По завершении в Гуляйполе появится один ядерный реактор. Потеря владения, контроля или места отменяет проект с возвратом PP; фабрики освобождаются.",
    "en": "One completed project per campaign: 100 PP and 5 civilian factories for 90 days. Builds one nuclear reactor in Huliaipole. Loss of ownership, control or space cancels the project, refunds PP and releases the factories."
  },
  "MKN_hull_repair_artels": {
    "ru": "Артели судового ремонта",
    "en": "Hull Repair Artels"
  },
  "MKN_hull_repair_artels_desc": {
    "ru": "Судоремонтные артели освоят замену повреждённых секций и переоборудование.",
    "en": "Repair cooperatives will learn hull repairs and refitting."
  },
  "MKN_imperial_administration": {
    "ru": "Степная администрация",
    "en": "Steppe Administration"
  },
  "MKN_imperial_administration_desc": {
    "ru": "Политическая программа завершена: новое устройство закрепляет порядок и распределение полномочий.",
    "en": "The completed political programme establishes a durable division of powers and responsibilities."
  },
  "MKN_imperial_coronation": {
    "ru": "Императорская коронация",
    "en": "Imperial Coronation"
  },
  "MKN_imperial_coronation_desc": {
    "ru": "Корона из пшеницы и стали.",
    "en": "A crown of wheat and steel."
  },
  "MKN_impregnable_granary_desc": {
    "ru": "Захватчику не достанется лёгкой жатвы. Получим ещё 50% к защите национальной территории и увеличим вражеские потери от истощения на нашей земле на 40%.",
    "en": "There will be no easy harvest for an invader. Add 50% core defense and impose 40% additional hostile attrition in our territory."
  },
  "MKN_industry_concern_1": {
    "ru": "Концерн «Вольная сталь»",
    "en": "Concern of Free Steel"
  },
  "MKN_industry_concern_2": {
    "ru": "Концерн «Вольная сталь»",
    "en": "Concern of Free Steel"
  },
  "MKN_integrate_steel_lines_desc": {
    "ru": "С согласия советской стороны и при контролируемой общей границе построим железнодорожное соединение второго уровня. Получим десять локомотивов и два года помощи в организации снабжения.",
    "en": "With Soviet consent and a controlled common border, build a level-two railway connection. Receive ten locomotives and two years of coordinated supply assistance."
  },
  "MKN_interceptor_cooperatives_desc": {
    "ru": "Истребители станут щитом коммун; ударная авиация останется второстепенной.\\n\\nЛёгкие планеры артели «Степной сокол» приспособят для манёвренного перехвата.\\n\\nЛучшие инструкторы покажут молодым пилотам приёмы боя в паре.\\n\\nВедущий прикрывает ведомого: одиночный герой уступит место слаженной паре.",
    "en": "Fighters will shield the communes while strike aviation remains secondary.\\n\\nSteppe Falcon cooperatives will adapt light airframes for agile interception.\\n\\nVeteran instructors will teach new pilots how to fight in pairs.\\n\\nLeaders and wingmen will replace lone heroics with coordinated pairs."
  },
  "MKN_interceptor_pairs": {
    "ru": "Перехват парами",
    "en": "Paired Interception"
  },
  "MKN_interceptor_pairs_desc": {
    "ru": "Ведущий прикрывает ведомого: одиночный герой уступит место слаженной паре.",
    "en": "Leaders and wingmen will replace lone heroics with coordinated pairs."
  },
  "MKN_invite_free_councils": {
    "ru": "Пригласить [FROM.GetName] в Интернационал",
    "en": "Invite [FROM.GetName] to the International"
  },
  "MKN_invite_free_councils_desc": {
    "ru": "50 PP за дипломатическую миссию. Независимая коммунистическая или демократическая страна вне альянса сама решит, принимать ли приглашение.",
    "en": "50 PP funds a diplomatic mission. An independent communist or democratic country outside any faction decides whether to accept."
  },
  "MKN_iron_fist_trains_desc": {
    "ru": "Бронепоезда понесут волю штаба за горизонт. Сохраним культ железных дорог, ускорим изучение поездов и уменьшим потребности армии в снабжении.",
    "en": "Armored trains shall carry the staff’s will beyond the horizon. Preserve the railway cult, accelerate train research and reduce the army’s supply burden."
  },
  "MKN_italian_mechanics_bonus": {
    "ru": "Итальянские механики-синдикалисты",
    "en": "Italian Syndicalist Mechanics"
  },
  "MKN_joint_defence_congress": {
    "ru": "Общий оборонительный съезд",
    "en": "Joint Defense Congress"
  },
  "MKN_joint_defence_congress_desc": {
    "ru": "За 50 политической власти сдвиньте баланс на 0,10 к центру, не пересекая его. Можно повторить через 90 дней.",
    "en": "Spend 50 PP to move the balance 0.10 toward the center without crossing it. Repeatable after 90 days."
  },
  "MKN_joint_target_planning": {
    "ru": "Совместное планирование ударов",
    "en": "Joint Strike Planning"
  },
  "MKN_joint_target_planning_desc": {
    "ru": "Штабы армии и авиации составят общие списки целей перед наступлением.",
    "en": "Army and air staffs will prepare common target lists before an offensive."
  },
  "MKN_kherson_shipyard": {
    "ru": "Херсонские верфи",
    "en": "Kherson Shipyards"
  },
  "MKN_kherson_shipyard_desc": {
    "ru": "Херсонские верфи дадут флотилии собственную строительную и ремонтную базу.",
    "en": "Kherson yards will give the flotilla its own construction and repair base."
  },
  "MKN_kyiv_scientific_exchange_desc": {
    "ru": "Объединим киевские школы и лаборатории с двумя уже созданными исследовательскими сетями коммун. Этот обмен после интеграции Украины создаёт шестую ячейку исследований. Если она уже получена в старом сохранении, вместо неё будут доступны две промышленные скидки 50%.",
    "en": "Join Kyiv’s schools and laboratories to both existing communal research networks. This exchange after Ukrainian integration establishes the sixth research slot. If an older save already has it, gain two 50% industrial research bonuses instead."
  },
  "MKN_litbel_agitation_unlock_tt": {
    "ru": "Открывает спонсирование стачек в ЛитБеле: 50 PP и 200 винтовок, 45 дней. Успех снижает стабильность на 5 п.п. и повреждает один военный завод. Союзники и партнёры по пакту исключены.",
    "en": "Unlocks Litbel strike funding: 50 PP and 200 rifles for 45 days. Completion reduces stability by 5 percentage points and damages one military factory. Allies and non-aggression partners are excluded."
  },
  "MKN_local_guides": {
    "ru": "Проводники родной степи",
    "en": "Native Steppe Guides"
  },
  "MKN_local_guides_desc": {
    "ru": "Местные проводники найдут броды и обходные тропы раньше противника.",
    "en": "Local guides will locate fords and flanking routes before the enemy."
  },
  "MKN_local_reserves": {
    "ru": "Местные страховые запасы",
    "en": "Local Insurance Reserves"
  },
  "MKN_local_reserves_desc": {
    "ru": "Излишки остаются в общих кладовых до следующего урожая.",
    "en": "Surpluses remain in shared granaries until the next harvest."
  },
  "MKN_logistics_projects_unlock_tt": {
    "ru": "Открывает три §Y60-дневных проекта на карте§!: Кичкасский мост (196), расчистка Днепра (226; морская база в Херсоне, 196), узловые станции (1082).",
    "en": "Unlocks three §Y60-day map projects§!: Kichkas Bridge (196), Dnieper waterways (226; naval base in Kherson, 196), steppe junctions (1082)."
  },
  "MKN_machinegun_carts": {
    "ru": "Пулемётные повозки",
    "en": "Machine Gun Carts"
  },
  "MKN_machinegun_carts_desc": {
    "ru": "Пулемётные тачанки дадут конным отрядам огневую опору.",
    "en": "Machine-gun carts will provide cavalry detachments with sustained firepower."
  },
  "MKN_mapped_supply": {
    "ru": "Согласованные маршруты",
    "en": "Agreed Supply Routes"
  },
  "MKN_mapped_supply_desc": {
    "ru": "Известны станции и склады, но диспетчеры и артели ещё спорят об очередности перевозок.",
    "en": "Stations and depots have been mapped, but dispatchers and artels still dispute transport priorities."
  },
  "MKN_marusya_assault_training": {
    "ru": "Городская штурмовая подготовка Маруси",
    "en": "Marusya's Urban Assault Training"
  },
  "MKN_marusya_assault_training_desc": {
    "ru": "Специальная штурмовая подготовка, предоставляемая национальным духом «Наследие Маруси».",
    "en": "Special assault training granted by the national spirit Marusya's Legacy."
  },
  "MKN_marusya_urban_attack_tt": {
    "ru": "Атака в городе: §G+15%§! для боевых сухопутных батальонов.",
    "en": "Urban attack: §G+15%§! for land combat battalions."
  },
  "MKN_marusya_womens_battalions_desc": {
    "ru": "Маруся стала символом для нового поколения доброволиц. Тридцать тысяч защитниц коммун вступят в строй, а их отряды научат армию быстрее собираться после боя.",
    "en": "Marusya has become a symbol for a new generation of volunteers. Thirty thousand defenders of the communes will join the ranks and help the army recover after battle."
  },
  "MKN_marusyas_legacy": {
    "ru": "Наследие Маруси",
    "en": "Marusya's Legacy"
  },
  "MKN_marusyas_legacy_desc": {
    "ru": "Память о Марусе вдохновляет штурмовые группы, способные прорвать оборону улицы и перегруппироваться прежде, чем противник придёт в себя.",
    "en": "The memory of Marusya inspires disciplined assault groups able to breach a defended street and regroup before the enemy recovers."
  },
  "MKN_mechanized_compact_desc": {
    "ru": "Основные службы готовы: коммуны располагают механизированной армией, а дальнейшие специализации остаются добровольными. Дополнительные тактики приобретаются отдельно в полевом штабе.",
    "en": "The core services are ready: communes now field a mechanized army with optional further specializations. Further tactics can be purchased separately at the field headquarters."
  },
  "MKN_memory_of_atamansha_marusya_desc": {
    "ru": "Маруся Никифорова превратила дерзость и инициативу в оружие повстанцев. Сохраним её наследие в постоянной подготовке к уличным боям, прорывам и быстрому восстановлению сил.",
    "en": "Marusya Nikiforova made audacity and initiative a weapon of the insurgency. Preserve her legacy through permanent training in street fighting, breakthrough tactics and rapid recovery."
  },
  "MKN_militarize_communes_desc": {
    "ru": "Каждая коммуна будет держать призывной список рядом с зерновой книгой. Расширим набор, заплатив за это новым ударом по доверию общин.",
    "en": "Every commune must keep a muster roll beside its grain ledger. Broaden recruitment, at the price of another wound to communal confidence."
  },
  "MKN_military_command_side": {
    "ru": "Военный штаб — Тратишов",
    "en": "Military Staff — Tratishov"
  },
  "MKN_military_directory": {
    "ru": "Военная директория",
    "en": "Military Directory"
  },
  "MKN_military_directory_desc": {
    "ru": "Политическая программа завершена: новое устройство закрепляет порядок и распределение полномочий.",
    "en": "The completed political programme establishes a durable division of powers and responsibilities."
  },
  "MKN_military_reform_cooldown": {
    "ru": "Внедрение военной реформы",
    "en": "Military Reform Implementation"
  },
  "MKN_military_reform_cooldown_desc": {
    "ru": "Штаб занят внедрением текущей реформы. Мы пока не можем начать новые масштабные преобразования в других родах войск.",
    "en": "The staff is implementing the current reform. We cannot yet begin further major reforms in the armed services."
  },
  "MKN_military_takes_charge_desc": {
    "ru": "Тратишов расстилает железнодорожную карту на столе съезда. Революции нужно единое оперативное командование. При поддержке не менее 40% населения и подготовленном съезде правящей программой станет анархо-милитаризм.",
    "en": "Tratishov spreads a railway map over the congress table. The revolution needs a single operational command. With at least 40% public support and a prepared congress, anarcho-militarism becomes the ruling program."
  },
  "MKN_militia_engineers": {
    "ru": "Сапёрные десятки",
    "en": "Engineer Squads"
  },
  "MKN_militia_engineers_desc": {
    "ru": "Сапёрные десятки подготовят переправы и укрытия лёгкими средствами.",
    "en": "Small engineer teams will prepare crossings and field shelters."
  },
  "MKN_militia_hospitals": {
    "ru": "Санитарные артели",
    "en": "Medical Artels"
  },
  "MKN_militia_hospitals_desc": {
    "ru": "Общины организуют эвакуацию раненых и восстановление бойцов.",
    "en": "Communes will organize casualty evacuation and rehabilitation."
  },
  "MKN_militia_junior_leaders": {
    "ru": "Выборные младшие командиры",
    "en": "Elected Junior Commanders"
  },
  "MKN_militia_junior_leaders_desc": {
    "ru": "Выборный командир тоже нуждается в тактической школе и понятной ответственности.",
    "en": "Elected junior commanders need tactical schooling and clear responsibilities."
  },
  "MKN_militia_signals": {
    "ru": "Связь между волостями",
    "en": "Inter Village Signals"
  },
  "MKN_militia_signals_desc": {
    "ru": "Сигнальные команды свяжут волости и выведут резерв на нужный участок.",
    "en": "Signals teams will connect districts and bring reserves to the right sector."
  },
  "MKN_mobile_medical": {
    "ru": "Подвижные санитарные пункты",
    "en": "Mobile Medical Posts"
  },
  "MKN_mobile_medical_desc": {
    "ru": "Санитарные автомобили вернут раненых в строй и сохранят кадры.",
    "en": "Medical vehicles will recover wounded soldiers and preserve trained personnel."
  },
  "MKN_mobile_patrols": {
    "ru": "Тачаночные дозорные колонны",
    "en": "Tachanka Patrol Columns"
  },
  "MKN_mobile_patrols_desc": {
    "ru": "Рассредоточенные дозоры быстро перемещаются, но требуют дополнительного снабжения.",
    "en": "Dispersed patrols move quickly but require additional supplies."
  },
  "MKN_mobile_rearguard": {
    "ru": "Подвижный арьергард",
    "en": "Mobile Rearguard"
  },
  "MKN_mobile_rearguard_desc": {
    "ru": "Подвижный арьергард задержит врага, пока обозы меняют стоянку.",
    "en": "Mobile rearguards will delay the enemy while supply trains relocate."
  },
  "MKN_mobile_self_defence_idea": {
    "ru": "Подвижная самооборона коммун",
    "en": "Mobile Communal Self Defence"
  },
  "MKN_mobile_self_defence_idea_desc": {
    "ru": "Сельские резервы регулярно собираются на учения и быстро соединяются в мобильные отряды.",
    "en": "Village reserves train regularly and assemble quickly into mobile detachments."
  },
  "MKN_mobile_supply_columns": {
    "ru": "Моторизованные обозы",
    "en": "Motorized Supply Columns"
  },
  "MKN_mobile_supply_columns_desc": {
    "ru": "Грузовики и заправщики будут следовать за наступающей бронёй.",
    "en": "Trucks and fuel tenders will follow advancing armoured units."
  },
  "MKN_mobile_workshops_desc": {
    "ru": "Сельские кузни войдут в сеть ремонтных поездок и передвижных мастерских. Два военных завода, грузовики и обмен инструментом восстановят выпуск, не собирая всё хозяйство в одном уязвимом центре.",
    "en": "Village smithies join travelling repair teams. Two military factories, trucks and shared tools restore production without concentrating it in one vulnerable industrial centre."
  },
  "MKN_moscow_request_pending": {
    "ru": "Предложение ожидает ответа Москвы",
    "en": "A proposal is awaiting Moscow's reply"
  },
  "MKN_motorized_infantry": {
    "ru": "Пехота вслед за бронёй",
    "en": "Infantry Behind the Armour"
  },
  "MKN_motorized_infantry_desc": {
    "ru": "Подвижная пехота закрепит захваченные танками переправы и населённые пункты.",
    "en": "Mobile infantry will secure crossings and settlements taken by tanks."
  },
  "MKN_motorized_vanguard_desc": {
    "ru": "Тракторные артели освоят бронетехнику для прорыва, но ей нужны экипажи и горючее.\\n\\nЭкипаж должен уметь чинить машину и действовать вместе с пехотой.\\n\\nКвартирмейстеры сведут потребности моторизованных частей в единый реестр.\\n\\nГрузовики и заправщики будут следовать за наступающей бронёй.",
    "en": "Tractor cooperatives will develop breakthrough armour that needs trained crews and fuel.\\n\\nCrews must repair their vehicles and cooperate with infantry.\\n\\nQuartermasters will reconcile the supply requirements of motorized formations.\\n\\nTrucks and fuel tenders will follow advancing armoured units."
  },
  "MKN_move_capital_to_kyiv": {
    "ru": "Перенести столицу в Киев",
    "en": "Move the Capital to Kyiv"
  },
  "MKN_move_capital_to_kyiv_desc": {
    "ru": "Перевезём общие учреждения и съезд делегатов из Гуляй-Поля в Киев. Решение стоит 50 политической власти и доступно после исчезновения UKR, если мы владеем Киевом и полностью контролируем его область. Прохождение всей ветки интеграции не требуется.",
    "en": "Move the common institutions and congress of delegates from Huliaipole to Kyiv. This decision costs 50 political power and is available after UKR ceases to exist, provided we own Kyiv and fully control its state. Completing the integration branch is not required."
  },
  "MKN_mutual_aid_economy": {
    "ru": "Хозяйство взаимопомощи",
    "en": "Mutual Aid Economy"
  },
  "MKN_mutual_aid_economy_desc": {
    "ru": "Кредит, страхование урожая и прозрачные договоры связывают самостоятельные артели без принудительного подчинения.",
    "en": "Credit, harvest insurance and transparent contracts unite independent artels without compulsory subordination."
  },
  "MKN_nabat_abroad_desc": {
    "ru": "После Великой смуты Набат должен говорить с крестьянами и рабочими по обе стороны границы. Связные создадут сеть солидарности, а не новую государственную канцелярию.",
    "en": "After the Great Tumult, Nabat must reach workers and peasants on both sides of the frontier. Couriers will build solidarity rather than a new state bureaucracy."
  },
  "MKN_nabat_abroad_unlock_tt": {
    "ru": "Открывает зарубежную работу Набата и связанные решения.",
    "en": "Unlocks Nabat work abroad and its decisions."
  },
  "MKN_nabat_foreign_cells": {
    "ru": "Зарубежные ячейки Набата",
    "en": "Foreign Nabat Cells"
  },
  "MKN_nabat_foreign_cells_desc": {
    "ru": "Связные коммун прокладывают агентурные сети за границей. Доступно при La Résistance.",
    "en": "Communal couriers establish intelligence networks abroad. Requires La Résistance."
  },
  "MKN_naval_intelligence": {
    "ru": "Карты торговых маршрутов",
    "en": "Merchant Route Charts"
  },
  "MKN_naval_intelligence_desc": {
    "ru": "Карты торговых маршрутов укажут ценные цели и безопасные районы ожидания.",
    "en": "Shipping intelligence will identify valuable targets and safe waiting areas."
  },
  "MKN_navy_development": {
    "ru": "Флот вольной территории",
    "en": "Fleet of the Free Territory"
  },
  "MKN_navy_development_desc": {
    "ru": "Подготовка кадров, местное производство и согласованные службы укрепляются по мере выполнения военной программы.",
    "en": "Training, local production and coordinated services improve as the military program advances."
  },
  "MKN_navy_development_summary": {
    "ru": "Улучшения флота накапливаются в одном духе.",
    "en": "Naval improvements accumulate in this single spirit."
  },
  "MKN_neighbor_strikes": {
    "ru": "Стачки под чёрным знаменем",
    "en": "Black Flag Strikes"
  },
  "MKN_neighbor_strikes_desc": {
    "ru": "Печи остывают, пока рабочие обсуждают листовку из Вольной территории. Выпуск продукции и строительство замедлятся на шестьдесят дней.",
    "en": "The furnaces cool while workers debate a pamphlet from the Free Territory. Production and construction slow for sixty days."
  },
  "MKN_nestor_the_first": {
    "ru": "Крестьянский покровитель",
    "en": "The Peasant Protector"
  },
  "MKN_nestor_the_first_desc": {
    "ru": "При поддержке не менее 40% крестьянский съезд выбирает аграрный изоляционизм под покровительством Нестора I. Спор командования с советами упраздняется вместе со шкалой баланса и её модификаторами. Махно сохраняет корону и портрет, а его военные должности остаются доступны только при коммунизме.",
    "en": "With at least 40% support, the peasant congress chooses agrarian isolationism under Nestor I. The dispute between command and soviets is abolished, removing the balance of power and its modifiers. Makhno retains his crown and portrait, while his military offices remain restricted to communism."
  },
  "MKN_neutrality_successor_desc": {
    "ru": "Выборный совет сёл управляет без монарха и постоянной городской бюрократии.",
    "en": "An elected village council governs without a monarch or a permanent urban bureaucracy."
  },
  "MKN_night_interceptors": {
    "ru": "Ночной перехват",
    "en": "Night Interception"
  },
  "MKN_night_interceptors_desc": {
    "ru": "Ночные звенья отработают перехват по командам с земли.",
    "en": "Night flights will practise ground-directed interception."
  },
  "MKN_night_marches": {
    "ru": "Ночные переходы",
    "en": "Night Marches"
  },
  "MKN_night_marches_desc": {
    "ru": "Отряды научатся уходить из-под удара ночью без распада колонны.",
    "en": "Detachments will withdraw at night without losing cohesion."
  },
  "MKN_night_sorties": {
    "ru": "Ночные выходы",
    "en": "Night Sorties"
  },
  "MKN_night_sorties_desc": {
    "ru": "Ночные выходы сократят время, когда рейдер виден береговым наблюдателям.",
    "en": "Night sorties will reduce exposure to coastal observers."
  },
  "MKN_northern_delegates_desc": {
    "ru": "Глухов и бывшая украинская область Лиски отправят своих делегатов. Местные мандаты обеспечат национализацию, добровольцев и политический доход.",
    "en": "Hlukhiv and the former Ukrainian district of Liski send delegates. Local mandates bring cores, volunteers and political income."
  },
  "MKN_observation_posts": {
    "ru": "Сеть наблюдательных постов",
    "en": "Observation Post Network"
  },
  "MKN_observation_posts_desc": {
    "ru": "Наблюдатели передадут предупреждение до появления бомбардировщиков над городами.",
    "en": "Observers will report bombers before they reach the towns."
  },
  "MKN_offer_workshop_exchange": {
    "ru": "Предложить обмен специалистами: [FROM.GetNameDef]",
    "en": "Offer a technical exchange to [FROM.GetNameDef]"
  },
  "MKN_offer_workshop_exchange_desc": {
    "ru": "За 50 PP предложим независимому партнёру взаимный обмен промышленными специалистами. Он может согласиться или отказать. Для каждой страны соглашение заключается один раз; повторное предложение после отказа доступно через 180 дней.",
    "en": "Spend 50 PP to propose a reciprocal industrial exchange to an independent partner. They may accept or decline. Each country can sign once; rejected offers may be repeated after 180 days."
  },
  "MKN_open_laboratories": {
    "ru": "Открытые лаборатории коммун",
    "en": "Open Communal Laboratories"
  },
  "MKN_open_laboratories_desc": {
    "ru": "Свободный обмен результатами ускоряет исследования на 5%.",
    "en": "Free exchange of results increases research speed by 5%."
  },
  "MKN_osyp_tsebriy": {
    "ru": "Осип Цебрий",
    "en": "Osyp Tsebriy"
  },
  "MKN_pact_of_free_communes_desc": {
    "ru": "Коммуны обязуются разрешать споры без создания соперничающих армий. Ратификация остановит отсчёт до гражданской войны и восстановит доверие к коллективному управлению.",
    "en": "The communes sign a common obligation to settle disputes without rival armies. Ratification stops the civil-war countdown and restores confidence in collective rule."
  },
  "MKN_passive_escalation_drift": {
    "ru": "Нарастание напряжённости на границе",
    "en": "Mounting Frontier Tension"
  },
  "MKN_passive_escalation_drift_desc": {
    "ru": "Каждые 30 дней напряжённость повышается на один уровень до завершения пограничного кризиса.",
    "en": "Tension rises by one level every 30 days until the frontier crisis ends."
  },
  "MKN_peasant_charter": {
    "ru": "Крестьянская хартия",
    "en": "The Peasant Charter"
  },
  "MKN_peasant_charter_desc": {
    "ru": "Нестор I признаёт деревенские собрания, общинные земельные соглашения и ограничения внешних обязательств. Корона гарантирует аграрную замкнутость и не даёт права на завоевания.",
    "en": "Nestor I recognizes the village assemblies, communal land agreements and limits on foreign commitments. The crown becomes a guarantor of agrarian isolation rather than a claim to conquest."
  },
  "MKN_peasant_council_leader": {
    "ru": "Совет крестьянских делегатов",
    "en": "Council of Peasant Delegates"
  },
  "MKN_peasant_delegates_desc": {
    "ru": "Новая корона не заменит шапку Батько. Избранный совет сёл возьмёт на себя ответственность за житницу. Аграрный изоляционизм требует подготовленного съезда и поддержки не менее 40%.",
    "en": "No new crown shall replace the Batko’s hat. An elected council of villages takes responsibility for the granary. Agrarian isolationism requires a prepared congress and at least 40% support."
  },
  "MKN_planned_economy": {
    "ru": "Плановое хозяйство",
    "en": "Planned Economy"
  },
  "MKN_planned_economy_desc": {
    "ru": "Политическая программа завершена: новое устройство закрепляет порядок и распределение полномочий.",
    "en": "The completed political programme establishes a durable division of powers and responsibilities."
  },
  "MKN_plenum_pending": {
    "ru": "Харьков рассматривает равноправную автономию",
    "en": "Kharkov is considering equal autonomy"
  },
  "MKN_polytechnic_institute_desc": {
    "ru": "Инженерное образование даст артелям свои станки, измерительные приборы и специалистов.",
    "en": "Engineering education supplies the artels with machine tools, instruments and trained specialists."
  },
  "MKN_power_balance": {
    "ru": "Штаб и вольные советы",
    "en": "Staff and Free Soviets"
  },
  "MKN_power_balance_desc": {
    "ru": "Оперативное командование Тратишова и советы Волина с отзывными делегатами спорят о власти. Доля контроля стороны равна (1 ± значение баланса) / 2; середина означает 45–55% контроля для каждой стороны.",
    "en": "Tratishov’s operational command and Volin’s recallable councils contend for authority. Each side’s control is (1 ± balance value) / 2; the middle represents 45–55% control on either side."
  },
  "MKN_production_cycles_desc": {
    "ru": "После подготовки резерва и энергосети заводы примут общие допуски, длинные серии и согласованные заказы. Военный завод и повышение предела эффективности закрепят устойчивый выпуск вооружения.",
    "en": "Prepared reserves and a working grid allow common tolerances and long production runs. Another military factory and a higher efficiency cap secure sustained arms production."
  },
  "MKN_propaganda_by_deed_desc": {
    "ru": "Погасшая печь говорит громче манифеста. Откроем сети стачек в соседних странах; их правительства должны будут переждать остановку производства или заплатить за её подавление.",
    "en": "A stopped furnace speaks more loudly than a manifesto. Unlock strike networks in neighboring countries; their governments must endure the stoppage or pay to break it."
  },
  "MKN_purge_irreconcilables_desc": {
    "ru": "Ревком прикажет каждому вооружённому комитету сдать оружие и списки. Разрешим вопрос преемственности и остановим 180-дневный отсчёт.",
    "en": "The revkom orders every armed committee to submit its weapons and registers. Resolve the succession and stop the 180-day countdown."
  },
  "MKN_question_of_discipline_desc": {
    "ru": "Приказы умирают на пути из зала съезда в окопы. Штаб согласует движение колонн и работу складов, даже если делегаты назовут это первым камнем нового государства.",
    "en": "Orders die between the congress hall and the trenches. Let the staff coordinate marching columns and reserve depots, even if the delegates call that the first stone of a new state."
  },
  "MKN_question_of_supply_desc": {
    "ru": "Винтовку не накормишь резолюцией. Коммуны проверят запасы зерна, боеприпасов и железнодорожные поставки; вольные советы усилят влияние на общее военное дело.",
    "en": "A rifle cannot eat a resolution. Let the communes audit grain, ammunition and rail deliveries; the free soviets gain influence over the common war effort."
  },
  "MKN_radio_beacons": {
    "ru": "Радиомаяки полевых полос",
    "en": "Field Airstrip Radio Beacons"
  },
  "MKN_radio_beacons_desc": {
    "ru": "Радиомаяки помогут перехватчикам вернуться даже в плохую погоду.",
    "en": "Radio beacons will guide interceptors home in poor weather."
  },
  "MKN_radio_sections": {
    "ru": "Радиостанция в каждом штабе",
    "en": "Radios in Every Headquarters"
  },
  "MKN_radio_sections_desc": {
    "ru": "Радиосвязь позволит подкреплениям вступать в бой по команде штаба.",
    "en": "Radios will bring reinforcements into battle when the staff needs them."
  },
  "MKN_raider_compact_desc": {
    "ru": "Рейдерская система готова; дополнительные катера, ремонт и тактику засад можно развивать по обстановке. Дополнительные тактики приобретаются отдельно в полевом штабе.",
    "en": "The raiding system is ready, with craft, repair and ambush tactics available as extensions. Further tactics can be purchased separately at the field headquarters."
  },
  "MKN_raider_dockyard": {
    "ru": "Мастерская малых подлодок",
    "en": "Small Submarine Yard"
  },
  "MKN_raider_dockyard_desc": {
    "ru": "Лиманские мастерские наладят серийное строительство малых подлодок.",
    "en": "Estuary workshops will organize serial construction of small submarines."
  },
  "MKN_raider_escape_routes": {
    "ru": "Маршруты отхода",
    "en": "Escape Routes"
  },
  "MKN_raider_escape_routes_desc": {
    "ru": "Заранее рассчитанные маршруты отхода спасут рейдеров от превосходящего флота.",
    "en": "Planned escape routes will help raiders evade superior fleets."
  },
  "MKN_raider_exercises": {
    "ru": "Учения скрытного флота",
    "en": "Stealth Fleet Exercises"
  },
  "MKN_raider_exercises_desc": {
    "ru": "Совместные учения подготовят группы подлодок к согласованной атаке.",
    "en": "Joint exercises will prepare submarine groups for coordinated attacks."
  },
  "MKN_raider_radio_discipline": {
    "ru": "Радиодисциплина рейдеров",
    "en": "Raider Radio Discipline"
  },
  "MKN_raider_radio_discipline_desc": {
    "ru": "Короткие зашифрованные передачи затруднят поиск рейдерских групп.",
    "en": "Short encrypted transmissions will make raider groups harder to locate."
  },
  "MKN_raider_replacement_crews": {
    "ru": "Резерв рейдерских экипажей",
    "en": "Raider Crew Reserve"
  },
  "MKN_raider_replacement_crews_desc": {
    "ru": "Резервные экипажи отработают аварийное погружение и уклонение от охотников.",
    "en": "Replacement crews will practise emergency dives and evasion."
  },
  "MKN_raider_signal_stations_desc": {
    "ru": "Береговые связные и радиопосты передадут флотилии сведения о чужих караванах. Разрозненные экипажи научатся сходиться для общего удара.",
    "en": "Coastal couriers and radio posts will report enemy shipping and help scattered crews assemble for coordinated attacks."
  },
  "MKN_raider_supply": {
    "ru": "Снабжение в тайных бухтах",
    "en": "Supply in Hidden Bays"
  },
  "MKN_raider_supply_desc": {
    "ru": "Скрытые топливные запасы увеличат время охоты на торговых путях.",
    "en": "Concealed fuel reserves will extend patrols along shipping routes."
  },
  "MKN_raider_weather": {
    "ru": "Погода как союзник",
    "en": "Weather as an Ally"
  },
  "MKN_raider_weather_desc": {
    "ru": "Метеосводки помогут использовать плохую видимость для подхода к цели.",
    "en": "Weather reports will help crews approach targets under poor visibility."
  },
  "MKN_railway_guards": {
    "ru": "Железнодорожная стража",
    "en": "Railway Guards"
  },
  "MKN_railway_guards_desc": {
    "ru": "Кто держит рельсы, тот держит юг.",
    "en": "Who holds the rails holds the south."
  },
  "MKN_railway_sabotage_desc": {
    "ru": "Подготовим заряды до приказа об отступлении. Откроем намеренное разрушение инфраструктуры и железных дорог в пограничных областях под угрозой; ремонт займёт больше времени.",
    "en": "Prepare the charges before the retreat order comes. Unlock deliberate damage to infrastructure and railways in threatened border states; their repair will take longer."
  },
  "MKN_railway_war": {
    "ru": "Железнодорожная война",
    "en": "Railway Warfare"
  },
  "MKN_railway_war_desc": {
    "ru": "Согласованные эшелоны подвезут боеприпасы быстрее случайных крестьянских обозов.",
    "en": "Scheduled trains will deliver ammunition instead of relying on improvised carts."
  },
  "MKN_recallable_delegates": {
    "ru": "Хартия отзыва",
    "en": "The Charter of Recall"
  },
  "MKN_recallable_delegates_desc": {
    "ru": "При махновской традиции или синдикалистском согласовании съезд гарантирует право отзыва каждого делегата. Хартия требует более 80% контроля вольных советов.",
    "en": "Whether the congress follows the Makhnovist tradition or syndicalist coordination, it guarantees the right to recall every delegate. The charter requires more than 80% control by the free soviets."
  },
  "MKN_recallable_front_delegates": {
    "ru": "Отзывные фронтовые делегаты",
    "en": "Recallable Front Delegates"
  },
  "MKN_recallable_front_delegates_desc": {
    "ru": "Постоянный обмен между деревнями и частями улучшает восстановление, но требует политических усилий.",
    "en": "A standing exchange between villages and units improves recovery but demands political effort."
  },
  "MKN_reconcile_village_and_front": {
    "ru": "Примирить деревню и фронт",
    "en": "Reconcile Village and Front"
  },
  "MKN_reconcile_village_and_front_desc": {
    "ru": "Направим отзывных деревенских делегатов в части. Приближает баланс к центру, обобщает военный опыт и улучшает восстановление ценой политических усилий.",
    "en": "Bring recallable delegates from the villages to the units. Move the balance toward the center, share military experience and improve recovery through political effort."
  },
  "MKN_recovery_tractors": {
    "ru": "Тягачи для эвакуации",
    "en": "Recovery Tractors"
  },
  "MKN_recovery_tractors_desc": {
    "ru": "Эвакуационные тягачи вернут повреждённые машины в мастерские.",
    "en": "Recovery tractors will retrieve damaged vehicles for the workshops."
  },
  "MKN_recruit_international_volunteers": {
    "ru": "Принять иностранных добровольцев",
    "en": "Welcome Foreign Volunteers"
  },
  "MKN_recruit_international_volunteers_desc": {
    "ru": "За 50 политической власти примем 5000 добровольцев и 500 винтовок. Можно повторять каждые 90 дней, пока резерв людских ресурсов меньше 100 000.",
    "en": "Spend 50 PP to welcome 5,000 volunteers with 500 rifles. Repeatable every 90 days while the manpower reserve is below 100,000."
  },
  "MKN_red_banner_steppe": {
    "ru": "Красный компромисс",
    "en": "The Red Compromise"
  },
  "MKN_red_banner_steppe_desc": {
    "ru": "При поддержке не менее 40% государственные социалисты создают центральное управление, признавая местные советы. Баланс смещается на 0,35 к советам. Независимая коммунистическая Москва получает предложение об оборонительном союзе, если страны не воюют друг с другом и Вольная территория не состоит в альянсе.",
    "en": "With at least 40% support, state socialists establish a central administration while recognizing local councils. The balance shifts by 0.35 toward the soviets. An independent communist Moscow receives a proposal for a defence pact if neither country is already fighting the other and the Free Territory is outside a faction."
  },
  "MKN_red_compromise_institutions": {
    "ru": "Советская администрация",
    "en": "The Council Administration"
  },
  "MKN_red_compromise_institutions_desc": {
    "ru": "Местные советы проводят государственно-социалистическую программу через постоянное гражданское управление. Эти учреждения сохраняют жизнеспособность при отказе Москвы или её предательстве.",
    "en": "Local councils implement the state socialist program through a permanent civil administration. These institutions remain viable even if Moscow rejects or betrays the pact."
  },
  "MKN_red_defence_pact": {
    "ru": "Красный оборонительный пакт",
    "en": "Red Defence Pact"
  },
  "MKN_red_military_specialists_desc": {
    "ru": "Прибывшие инструкторы привезут штатные таблицы, а не проповеди. Улучшим сплочённость и планирование армии, получим опыт и освоение сухопутной доктрины.",
    "en": "The visiting instructors bring tables of organization, not sermons. Improve army cohesion and planning, and gain experience and land doctrine mastery."
  },
  "MKN_remount_artels": {
    "ru": "Артели конского резерва",
    "en": "Remount cooperatives"
  },
  "MKN_remount_artels_desc": {
    "ru": "Общие конюшни и запас верховых лошадей поддержат темп похода.",
    "en": "Shared stables and remount reserves will sustain the march."
  },
  "MKN_renew_front_talks": {
    "ru": "Возобновить переговоры о фронте",
    "en": "Renew the Front Negotiations"
  },
  "MKN_renew_front_talks_desc": {
    "ru": "Попросим советские республики пересмотреть вопрос общего оборонительного союза.",
    "en": "Ask the Soviet Republics to reconsider a common defensive alliance."
  },
  "MKN_renew_supply_talks": {
    "ru": "Возобновить зерновые переговоры",
    "en": "Renew the Grain Negotiations"
  },
  "MKN_renew_supply_talks_desc": {
    "ru": "Попросим Харьков пересмотреть вопрос взаимного транзита и снабжения.",
    "en": "Ask Kharkov to reconsider reciprocal transit and supplies."
  },
  "MKN_requisition_workshop_shifts": {
    "ru": "Реквизировать дополнительные смены мастерских",
    "en": "Requisition Extra Workshop Shifts"
  },
  "MKN_requisition_workshop_shifts_desc": {
    "ru": "Командиры требуют от мастерских больше оружия. Военное производство растёт ценой стабильности и гражданского потребления.",
    "en": "Commanders demand additional arms from the workshops. Military production rises at the cost of stability and civilian consumption."
  },
  "MKN_revkom_leader": {
    "ru": "Чрезвычайный революционный комитет",
    "en": "Emergency Revolutionary Committee"
  },
  "MKN_revkom_terror": {
    "ru": "Террор ревкома",
    "en": "Revkom Terror"
  },
  "MKN_revkom_terror_desc": {
    "ru": "Чрезвычайный комитет парализует производство реквизициями и арестами. После устранения непримиримых власть перейдёт к Осипу Цебрию.",
    "en": "An emergency committee paralyses production through requisitions and arrests. The purge of irreconcilables will transfer authority to Osyp Tsebriy."
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
  "MKN_rifle_concern_desc": {
    "ru": "Оружейные артели получат защищённую внекарточную производственную линию. С Arms Against Tyranny доступна пехотная MIO; без дополнения — оружейный конструктор. Договор о взаимозаменяемости позволит развить выбранное предприятие.",
    "en": "The rifle artels receive a protected off-map military factory. Arms Against Tyranny enables an infantry MIO; without it, a weapons designer is available. Workshop standards develop the enterprise further."
  },
  "MKN_right_bank_councils_desc": {
    "ru": "Советы Житомирщины, Подолии и Правобережья получат признанное представительство. Национализация четырёх областей и постоянная стабильность заменят чрезвычайное управление.",
    "en": "Councils of Zhytomyr, Podillia and the right bank gain recognized representation. Four states become cores and lasting stability replaces emergency administration."
  },
  "MKN_river_sea_coordination": {
    "ru": "От реки к морскому эскорту",
    "en": "River Sea Coordination"
  },
  "MKN_river_sea_coordination_desc": {
    "ru": "Согласуем речные перевозки, морской эскорт и береговую разведку.",
    "en": "Coordinate river transport, sea escorts and coastal reconnaissance."
  },
  "MKN_rural_reserve": {
    "ru": "Сменяемый сельский резерв",
    "en": "Rotating Village Reserve"
  },
  "MKN_rural_reserve_desc": {
    "ru": "Сменяемый резерв позволит сельским общинам содержать армию и продолжать посевную.",
    "en": "Rotating reserves will let rural communes field troops while maintaining the harvest."
  },
  "MKN_scorched_railways": {
    "ru": "Уничтожить пути в области [From.GetName]",
    "en": "Destroy Routes in [From.GetName]"
  },
  "MKN_scorched_railways_desc": {
    "ru": "За 25 политической власти повредим два уровня инфраструктуры и железных дорог в этой области под угрозой. Ремонт замедлится на 50%. Повреждения сохранятся после смены контроля.",
    "en": "Spend 25 PP to damage two levels of infrastructure and railways in this threatened state. Repairs are 50% slower. The damage remains after control changes."
  },
  "MKN_scout_parties": {
    "ru": "Разведка малыми отрядами",
    "en": "Small Reconnaissance Parties"
  },
  "MKN_scout_parties_desc": {
    "ru": "Разведывательные партии расчистят путь основной колонне.",
    "en": "Small scouting parties will clear the route for the main column."
  },
  "MKN_sea_escort_service_desc": {
    "ru": "Защитим подходы к портам и сделаем зерновую торговлю главной задачей флота.\\n\\nЛёгкие эскорты Херсонской артели будут держать строй вокруг конвоя.\\n\\nЭкипажи отработают охранение медленных транспортов вместо погони за славой.\\n\\nГидроакустики и расчёты глубинных бомб будут работать одной командой.",
    "en": "Defend port approaches and make grain shipping the navy's main mission.\\n\\nLight escorts from the Kherson cooperative will hold formation around convoys.\\n\\nCrews will train to protect slow transports rather than chase glory.\\n\\nSonar operators and depth-charge crews will work as one team."
  },
  "MKN_seed_cooperatives": {
    "ru": "Общинные семенные кооперативы",
    "en": "Communal Seed Cooperatives"
  },
  "MKN_seed_cooperatives_desc": {
    "ru": "Общие резервы и устойчивое расписание мастерских смягчают гражданский дефицит.",
    "en": "Shared reserves and reliable workshop schedules ease civilian shortages."
  },
  "MKN_serial_production": {
    "ru": "Серийное производство Днепра",
    "en": "Dnieper Serial Production"
  },
  "MKN_serial_production_desc": {
    "ru": "Общие допуски и производственные циклы дают крупным предприятиям устойчивые серии вооружения.",
    "en": "Common tolerances and production cycles sustain long armament runs at major factories."
  },
  "MKN_sever_urban_ties_desc": {
    "ru": "Закроем экспортные книги и распустим соперничающие делегации. Упраздним баланс сил, введём закрытую экономику и оставим больше продукции сёлам.",
    "en": "Close the export ledgers and dismiss the competing delegations. Abolish the balance of power, adopt a closed economy and reserve more output for the villages."
  },
  "MKN_shadows_in_the_forests_desc": {
    "ru": "Оккупационные гарнизоны не получат спокойного тыла. Лесные связные и подпольные советы удвоят урон сопротивления на нашей занятой земле.",
    "en": "Occupation garrisons shall have no quiet rear. Forest couriers and underground councils will double resistance damage on our occupied soil."
  },
  "MKN_sky_watch_exercises": {
    "ru": "Учения воздушного дозора",
    "en": "Sky Watch Exercises"
  },
  "MKN_sky_watch_exercises_desc": {
    "ru": "Учения проверят цепочку от обнаружения цели до посадки перехватчика.",
    "en": "Exercises will test the whole interception chain from detection to landing."
  },
  "MKN_smuggle_kronstadt_sailors": {
    "ru": "Тайно переправить кронштадтских моряков",
    "en": "Smuggle Kronstadt Sailors"
  },
  "MKN_smuggle_kronstadt_sailors_desc": {
    "ru": "Переправим оппозиционно настроенных моряков и их семьи на вольную территорию тайными балтийскими маршрутами. Даёт 10 000 людских ресурсов и 15 единиц опыта флота.",
    "en": "Bring dissident sailors and their families to the free territory through clandestine Baltic routes. Gain 10,000 manpower and 15 naval experience."
  },
  "MKN_smuggling_network": {
    "ru": "Контрабандистские сети",
    "en": "Smuggling Networks"
  },
  "MKN_smuggling_network_desc": {
    "ru": "Чёрное море кормит Вольную территорию в обход любых блокад.",
    "en": "The Black Sea feeds the Free Territory around every blockade."
  },
  "MKN_solidarity_guarantees_desc": {
    "ru": "Подготовим договорные процедуры защиты независимых соседей. Совет сможет выдавать гарантии обычными дипломатическими средствами, а общий конгресс объединит мирные представительства и зарубежные движения.",
    "en": "Prepare treaty procedures for defending independent neighbours. The council can issue guarantees through normal diplomacy, while a common congress brings together our representatives and overseas movements."
  },
  "MKN_solidarity_guarantees_tt": {
    "ru": "Внешняя служба коммун: стоимость гарантий независимости §G−10%§!. Открывается мирный путь к Конгрессу свободных народов.",
    "en": "Communal Foreign Service: independence guarantee cost §G−10%§!. Opens a peaceful route to the Congress of Free Peoples."
  },
  "MKN_southern_commune_charters_desc": {
    "ru": "Одесса, Николаев и Балта примут местные хартии и станут национальными областями. Согласованные склады уменьшат потребление снабжения.",
    "en": "Odesa, Mykolaiv and Balta adopt local charters and become core states. Coordinated depots reduce supply consumption."
  },
  "MKN_southern_resources_desc": {
    "ru": "Никопольский марганец и угольные промыслы войдут в общий договор поставок. Сырьё останется достоянием коммун, а заводы получат устойчивую основу для больших серий.",
    "en": "Nikopol manganese and the southern coal workings will enter a common supply agreement, providing the raw materials for large production runs."
  },
  "MKN_soviet_betrayal": {
    "ru": "Советское правительство предало хартию",
    "en": "The Soviet government betrayed the charter"
  },
  "MKN_soviet_front_pending": {
    "ru": "Харьков рассматривает предложение общего фронта",
    "en": "Kharkov is considering the common front"
  },
  "MKN_soviet_intervention_category": {
    "ru": "Тень интервенции",
    "en": "The Shadow of Intervention"
  },
  "MKN_soviet_intervention_category_desc": {
    "ru": "Четыре съезда сражаются за наследство Вольной территории, пока Москва и Харьков готовят свои требования. У нас сто дней на объединение степи, прежде чем чужие армии превратят нашу гражданскую войну в собственное завоевание.",
    "en": "The four congresses fight over the inheritance of the Free Territory while Moscow and Kharkiv assemble their demands. We have one hundred days to reunite the steppe before outside armies turn our civil war into their conquest."
  },
  "MKN_soviet_intervention_mission": {
    "ru": "Угроза советской интервенции",
    "en": "Threat of Soviet Intervention"
  },
  "MKN_soviet_intervention_mission_desc": {
    "ru": "Пока братья убивают братьев, Красная армия собирается у границы. Если Вольная территория не объединится за §Y100 дней§!, Советы вмешаются, чтобы «восстановить порядок». Все уцелевшие стороны должны объединиться в одну — тогда миссия завершится. Иначе независимые SOV и UKR получат цели войны на аннексию и объявят войну каждому уцелевшему участнику раскола.",
    "en": "While brothers slaughter brothers, the Red Army gathers along the border. If the Free Territory is not united within §Y100 days§!, the Soviets will intervene to restore order. All surviving factions must be reunited into one; then this mission ends. Otherwise independent SOV and UKR receive annexation goals and declare war on every surviving faction."
  },
  "MKN_soviet_intervention_tt": {
    "ru": "Существующие независимые §YСоветская Россия§! и §YСоветская Украина§! получают цели войны на аннексию и объявляют войну всем уцелевшим участникам раскола Вольной территории. Общие альянсы разрываются перед интервенцией.",
    "en": "Existing independent §YSoviet Russia§! and §YSoviet Ukraine§! receive annexation war goals and declare war on every surviving participant in the Free Territory's collapse. Shared factions are broken before intervention."
  },
  "MKN_soviet_supply_agreement": {
    "ru": "Советское соглашение о снабжении",
    "en": "Soviet Supply Agreement"
  },
  "MKN_soviet_supply_agreement_desc": {
    "ru": "Совместные диспетчеры и снабженцы будут координировать поставки в течение двух лет.",
    "en": "Joint dispatchers and supply officers coordinate deliveries for two years."
  },
  "MKN_soviet_trade_accepted": {
    "ru": "Харьков принял соглашение о снабжении",
    "en": "Kharkov accepted the supply agreement"
  },
  "MKN_soviets_forever": {
    "ru": "Советы навсегда",
    "en": "Soviets Forever"
  },
  "MKN_soviets_forever_desc": {
    "ru": "Коммуна вечна.",
    "en": "The commune is eternal."
  },
  "MKN_spartacist_engineers": {
    "ru": "Мастерская спартаковцев",
    "en": "Spartacist Workshop"
  },
  "MKN_spartacist_engineers_desc": {
    "ru": "Немецкие специалисты создали временный кооператив по выпуску вооружения.",
    "en": "German specialists have established a temporary cooperative for arms production."
  },
  "MKN_spartacist_factory_tt": {
    "ru": "Вне-картовые военные фабрики: §G+1§! на время действия духа.",
    "en": "Off-map military factories: §G+1§! while this spirit is active."
  },
  "MKN_sponsor_litbel_strike": {
    "ru": "Спонсировать стачку в ЛитБеле",
    "en": "Sponsor a Litbel Strike"
  },
  "MKN_sponsor_litbel_strike_desc": {
    "ru": "45 дней, 50 PP и 200 винтовок: −5 п.п. стабильности и повреждение одного военного завода. Повторное финансирование — через 180 дней. Отмена возвращает PP и оружие базового образца.",
    "en": "45 days, 50 PP and 200 rifles: −5 percentage points stability and damage to one military factory. Can be funded again after 180 days. Cancellation refunds PP and basic rifles."
  },
  "MKN_staff_games": {
    "ru": "Штабные игры на Днепре",
    "en": "Dnieper Staff Exercises"
  },
  "MKN_staff_games_desc": {
    "ru": "Проверим планы на штабных играх прежде, чем проверять их людьми.",
    "en": "Test operational plans in staff exercises before risking lives."
  },
  "MKN_standardize_workshops_desc": {
    "ru": "Дюжина несовместимых затворов — дюжина способов проиграть бой. Общие калибры и согласованные заказы повысят выпуск и эффективность производства в артелях.",
    "en": "A dozen incompatible breech blocks are a dozen ways to lose a battle. Give the artels common gauges and coordinated orders to raise output and production efficiency."
  },
  "MKN_standardized_workshops": {
    "ru": "Мастерские переходного периода",
    "en": "Workshops in Transition"
  },
  "MKN_standardized_workshops_desc": {
    "ru": "Общие чертежи уже работают. Последние узкие места требуют постоянной системы заказов и контроля качества.",
    "en": "Shared drawings are in use. The remaining bottlenecks need a lasting system of orders and quality control."
  },
  "MKN_state_socialism": {
    "ru": "Государственный синдикализм",
    "en": "State Socialism"
  },
  "MKN_state_socialism_regime": {
    "ru": "Государственно-социалистическая администрация",
    "en": "State Socialist Administration"
  },
  "MKN_steel_horses": {
    "ru": "Стальные кони",
    "en": "Iron Horses"
  },
  "MKN_steel_horses_desc": {
    "ru": "Тракторные артели освоят бронетехнику для прорыва, но ей нужны экипажи и горючее.",
    "en": "Tractor cooperatives will develop breakthrough armour that needs trained crews and fuel."
  },
  "MKN_steel_horses_idea": {
    "ru": "Стальные кони",
    "en": "Iron Horses"
  },
  "MKN_steel_horses_idea_desc": {
    "ru": "Броня и скорость вместо конского мяса.",
    "en": "Armor and speed instead of horseflesh."
  },
  "MKN_steel_volnitsa_desc": {
    "ru": "Хозяйственный договор соединит промышленный совет, рабочие кассы и единую логистику. Развиваем общий хозяйственный дух и концерн «Вольная сталь», открываем фабрику и расширяем пространство для новых предприятий.",
    "en": "A common compact unites factory councils, workers’ welfare and logistics. Develop the shared economic spirit and Free Steel concern, establish a civilian factory and expand room for further industry."
  },
  "MKN_steppe_camouflage": {
    "ru": "Степная маскировка",
    "en": "Steppe Camouflage"
  },
  "MKN_steppe_camouflage_desc": {
    "ru": "Маскировка степных позиций поможет переждать превосходство противника в огне.",
    "en": "Camouflaged steppe positions will help troops survive superior enemy firepower."
  },
  "MKN_steppe_electrification_desc": {
    "ru": "Общая сеть уменьшит расход энергии заводами. Открываем три проекта на 60 дней: турбины Днепрогэса, электрификацию Екатеринослава и резервные угольные линии; каждый занимает две гражданские фабрики.",
    "en": "The common grid reduces factory energy demand. Unlock three 60-day projects using two civilian factories each: Dnieper turbines, the Katerynoslav grid and reserve coal lines."
  },
  "MKN_steppe_general_staff_desc": {
    "ru": "Вооружим колонны и введём общий порядок сбора, сохраняя выборных командиров.\\n\\nСогласованные эшелоны подвезут боеприпасы быстрее случайных крестьянских обозов.\\n\\nШтаб Белаша свяжет самостоятельные отряды общим планом операций.\\n\\nОткрывает одноразовые тактики полевого штаба за опыт и командный ресурс.",
    "en": "Equip the columns and establish mustering rules under elected commanders.\\n\\nScheduled trains will deliver ammunition instead of relying on improvised carts.\\n\\nBelash's staff will coordinate independent detachments through shared operational plans.\\n\\nUnlocks one-time field headquarters tactics purchased with experience and command power."
  },
  "MKN_steppe_hawks": {
    "ru": "Степные соколы",
    "en": "Steppe Hawks"
  },
  "MKN_steppe_hawks_and_schools_desc": {
    "ru": "Создадим воздушную службу коммун с общей диспетчерской и правилами полётов.\\n\\nПолевые полосы приблизят авиацию к войскам и сократят бесполезные перелёты.\\n\\nШкола лётчиков даст общую подготовку перед выбором боевой специализации.\\n\\nОткрывает одноразовые тактики полевого штаба за опыт и командный ресурс.",
    "en": "Establish a communal air service with shared flight control and operating rules.\\n\\nForward strips will bring aircraft closer to troops and reduce ferry flights.\\n\\nThe pilot school will provide common training before combat specialization.\\n\\nUnlocks one-time field headquarters tactics purchased with experience and command power."
  },
  "MKN_steppe_hawks_desc": {
    "ru": "Создадим воздушную службу коммун с общей диспетчерской и правилами полётов.",
    "en": "Establish a communal air service with shared flight control and operating rules."
  },
  "MKN_steppe_horde_desc": {
    "ru": "Сохраним мобильность конницы, вложившись в вооружение и связь вместо дорогой брони.\\n\\nСельские сборные пункты заранее распределят людей по отрядам.\\n\\nОбщие конюшни и запас верховых лошадей поддержат темп похода.\\n\\nПулемётные тачанки дадут конным отрядам огневую опору.",
    "en": "Preserve cavalry mobility by investing in weapons and communications rather than expensive armour.\\n\\nVillage mustering stations will assign recruits to detachments in advance.\\n\\nShared stables and remount reserves will sustain the march.\\n\\nMachine-gun carts will provide cavalry detachments with sustained firepower."
  },
  "MKN_steppe_industrial_giants_desc": {
    "ru": "«Коммунар», трубные мастерские и алюминиевое производство объединят заказы и инженерные кадры. Новые корпуса дадут фабрику и три военных завода, а собственный алюминий обеспечит машиностроение.",
    "en": "Kommunar, the tube works and aluminium plants pool their orders and engineers. One civilian factory, three military factories and aluminium supplies restore large-scale manufacturing."
  },
  "MKN_steppe_legions": {
    "ru": "Степные легионы",
    "en": "The Steppe Legions"
  },
  "MKN_steppe_legions_desc": {
    "ru": "Постоянные соединения заменяют слабо согласованные отряды. Для этого учреждения требуется более 80% контроля командования; баланс смещается ещё на 0,10 к военным.",
    "en": "Permanent formations replace the loosely coordinated detachments. This institution requires more than 80% military control and shifts the balance another 0.10 toward command."
  },
  "MKN_steppe_markets_desc": {
    "ru": "Базары, монетный двор и кредитные кассы примут общий расчёт без ростовщичества. Две фабрики и устойчивый политический доход закрепят доверие к договорам между коммунами.",
    "en": "Bazaars, the mint and mutual credit funds agree on common settlement without usury. Two civilian factories and a lasting political income strengthen confidence between communes."
  },
  "MKN_steppe_operations_category": {
    "ru": "За околицей",
    "en": "Beyond the Village Gate"
  },
  "MKN_steppe_operations_category_desc": {
    "ru": "Железнодорожные бригады, добровольцы и подпольщики выносят борьбу коммуны за пределы её полей.",
    "en": "Rail crews, volunteers and underground organizers carry the commune’s struggle beyond its fields."
  },
  "MKN_steppe_quartermasters": {
    "ru": "Школа степных квартирмейстеров",
    "en": "Steppe Quartermaster School"
  },
  "MKN_steppe_quartermasters_desc": {
    "ru": "Квартирмейстеры сведут потребности моторизованных частей в единый реестр.",
    "en": "Quartermasters will reconcile the supply requirements of motorized formations."
  },
  "MKN_steppe_quartermasters_idea": {
    "ru": "Степные интенданты",
    "en": "Steppe Quartermasters"
  },
  "MKN_steppe_quartermasters_idea_desc": {
    "ru": "С обозом Маркса, а без обоза и Маркс воюет вполсилы. Мы — наоборот.",
    "en": "An army marches on its stomach, ours also."
  },
  "MKN_steppe_snipers_desc": {
    "ru": "Борозда, терпеливый взгляд и один выстрел. Улучшим защиту и разведку, уменьшив преимущество противника от господства в воздухе.",
    "en": "A furrow, a patient eye and one shot. Improve defense and reconnaissance while reducing the enemy’s advantage from air superiority."
  },
  "MKN_steppes_freedom": {
    "ru": "Свобода степей",
    "en": "Freedom of the Steppe"
  },
  "MKN_steppes_freedom_desc": {
    "ru": "Быстрая кавалерия и моторизованные колонны опираются на местное снабжение. Пять последовательных промышленных реформ снимают штраф разрозненных мастерских к выпуску продукции, каждый раз улучшая общий экономический дух на пять процентных пунктов.",
    "en": "Fast cavalry and motor columns rely on local supply networks. Five successive industrial milestones remove the scattered workshops’ output penalty, improving the shared economy spirit by five percentage points at each step."
  },
  "MKN_strike_networks": {
    "ru": "Организовать стачки в [From.GetNameDef]",
    "en": "Organize Strikes in [From.GetNameDef]"
  },
  "MKN_strike_networks_desc": {
    "ru": "За 75 политической власти отправим призыв к стачке. Цель может переждать шестьдесят дней сбоев или потратить 50 политической власти и потерять 5% стабильности для подавления.",
    "en": "Spend 75 PP to send a strike call. The target may endure sixty days of disruption or spend 50 PP and lose 5% stability to suppress it."
  },
  "MKN_submarine_crews": {
    "ru": "Школа подводных экипажей",
    "en": "Submarine Crew School"
  },
  "MKN_submarine_crews_desc": {
    "ru": "Экипажи научатся выбирать цель и момент атаки, а не искать открытого боя.",
    "en": "Crews will choose targets and timing rather than seek open battle."
  },
  "MKN_submarine_listening": {
    "ru": "Школа гидроакустиков",
    "en": "Hydrophone School"
  },
  "MKN_submarine_listening_desc": {
    "ru": "Гидроакустики услышат цель раньше, чем противник заметит подлодку.",
    "en": "Hydrophone crews will hear targets before enemies detect the submarine."
  },
  "MKN_submarine_repair": {
    "ru": "Ремонт подводного флота",
    "en": "Submarine Repair"
  },
  "MKN_submarine_repair_desc": {
    "ru": "Ремонтные бригады восстановят механизмы между боевыми походами.",
    "en": "Repair crews will overhaul machinery between patrols."
  },
  "MKN_succession_crisis_category": {
    "ru": "После Батько",
    "en": "After the Batko"
  },
  "MKN_succession_crisis_category_desc": {
    "ru": "Похороны окончены; спор только начался. Завершите фокус урегулирования до истечения срока задания.",
    "en": "The funeral is over; the argument has only begun. Complete a settlement focus before the mission expires."
  },
  "MKN_support_galician_unions": {
    "ru": "Вооружить сельские союзы: [FROM.GetName]",
    "en": "Arm Rural Unions: [FROM.GetName]"
  },
  "MKN_support_galician_unions_desc": {
    "ru": "За 45 дней, 50 PP и 200 винтовок подготовим союзы против Габсбургов: −5 п.п. стабильности Австрии, повреждение инфраструктуры и подготовка региона к пограничному выступлению. Отмена возвращает PP и базовое оружие.",
    "en": "45 days, 50 PP and 200 rifles prepare rural unions against the Habsburgs: Austrian stability falls by 5 percentage points, infrastructure is damaged and the state is prepared for a border action. Cancellation refunds PP and basic rifles."
  },
  "MKN_sweeper_sections": {
    "ru": "Тральные отряды",
    "en": "Minesweeper Sections"
  },
  "MKN_sweeper_sections_desc": {
    "ru": "Тральные команды очистят торговые фарватеры от мин.",
    "en": "Minesweeping teams will clear the shipping lanes."
  },
  "MKN_syndicalist_pact_unlock_tt": {
    "ru": "Общий дух армии: +3 к размеру добровольческих сил. Открывает создание Чёрного Интернационала за 100 PP и приглашения за 50 PP. Добровольцев можно отправлять коммунистическим и демократическим участникам гражданской войны.",
    "en": "Shared army spirit: +3 volunteer capacity. Unlocks founding the Black International for 100 PP and invitations for 50 PP. Volunteers may be sent to communist and democratic participants in civil wars."
  },
  "MKN_tachanka_columns": {
    "ru": "Тачаночные колонны",
    "en": "Tachanka Columns"
  },
  "MKN_tachanka_columns_desc": {
    "ru": "Вооружим колонны и введём общий порядок сбора, сохраняя выборных командиров.",
    "en": "Equip the columns and establish mustering rules under elected commanders."
  },
  "MKN_tachanka_patrols": {
    "ru": "Вывести тачанки в степные дозоры",
    "en": "Send Tachankas on Steppe Patrol"
  },
  "MKN_tachanka_patrols_desc": {
    "ru": "Расширим полномочия полевых командиров для патрулирования степи. Подвижность и поддержка войны растут вместе с расходами снабжения и общественным недовольством.",
    "en": "Empower field commanders to patrol the steppe. Mobility and war support improve, while supply demands and unrest grow."
  },
  "MKN_tachanka_tactics": {
    "ru": "Тачанки и пеший заслон",
    "en": "Tachankas and Infantry Screens"
  },
  "MKN_tachanka_tactics_desc": {
    "ru": "Пеший заслон прикроет отход тачанок и сорвёт преследование.",
    "en": "Dismounted screens will cover the carts' withdrawal and break pursuit."
  },
  "MKN_tachanka_warfare": {
    "ru": "Тачаночная война",
    "en": "Tachanka Warfare"
  },
  "MKN_tachanka_warfare_desc": {
    "ru": "Скорость — броня в степи.",
    "en": "Speed is armor on the steppe."
  },
  "MKN_tactical_recon": {
    "ru": "Тактическая воздушная разведка",
    "en": "Tactical Aerial Reconnaissance"
  },
  "MKN_tactical_recon_desc": {
    "ru": "Воздушная разведка укажет колоннам обходные пути и вражеские резервы.",
    "en": "Aerial scouts will identify flanking routes and enemy reserves."
  },
  "MKN_tank_crews": {
    "ru": "Артель танковых экипажей",
    "en": "Tank Crew Artel"
  },
  "MKN_tank_crews_desc": {
    "ru": "Экипаж должен уметь чинить машину и действовать вместе с пехотой.",
    "en": "Crews must repair their vehicles and cooperate with infantry."
  },
  "MKN_tank_maintenance": {
    "ru": "Полевой ремонт брони",
    "en": "Field Armour Repair"
  },
  "MKN_tank_maintenance_desc": {
    "ru": "Ремонтная база Днепра обеспечит запасные узлы и восстановление техники.",
    "en": "A Dnipro repair plant will provide replacement assemblies and equipment repairs."
  },
  "MKN_target_markers": {
    "ru": "Обозначение целей с земли",
    "en": "Ground Target Marking"
  },
  "MKN_target_markers_desc": {
    "ru": "Дымовые сигналы и условные полотнища обозначат передний край.",
    "en": "Smoke signals and recognition panels will mark the front line."
  },
  "MKN_technical_communes_desc": {
    "ru": "Учёные и мастера создадут общую сеть технических школ, доступную при любой форме хозяйства.",
    "en": "Scientists and craftsmen establish a technical school network under either economic model."
  },
  "MKN_the_absolute_argument_desc": {
    "ru": "Империи должны знать цену вторжения. Исследования реактора откроют проект в Гуляйполе; до настоящего ядерного оружия ещё предстоит пройти научный и промышленный путь.",
    "en": "Empires must know the cost of invasion. Reactor research will open a project in Huliaipole; actual nuclear weapons will still require further scientific and industrial work."
  },
  "MKN_the_black_horde_desc": {
    "ru": "Под чёрным знаменем поднимаются штыки. Армия получит 25% к атаке и 30% к прорыву; независимые соседи вне нашего альянса станут целями аннексии. Штаб обещает свободу в конце каждого похода.",
    "en": "Bayonets rise beneath the black banner. The army gains 25% attack and 30% breakthrough; sovereign neighbors outside our faction become targets for annexation. The staff promises freedom at the end of every march."
  },
  "MKN_the_fatal_plenum_desc": {
    "ru": "Последняя хартия ставит наши автономные советы рядом с советским правительством на равных. Харьков может ратифицировать её — или изгнать нас из общего фронта и вторгнуться. Преданная революция будет сражаться с временным духом «Преданы дважды».",
    "en": "The final charter places our autonomous councils beside the Soviet government as equals. Kharkov may ratify it—or expel us from the common front and invade. A betrayed revolution fights with the temporary spirit Betrayed Twice."
  },
  "MKN_torpedo_ambushes": {
    "ru": "Торпедные засады",
    "en": "Torpedo Ambushes"
  },
  "MKN_torpedo_ambushes_desc": {
    "ru": "Засады у узких проходов позволят сосредоточить торпедный залп.",
    "en": "Ambushes near narrow passages will concentrate torpedo salvos."
  },
  "MKN_torpedo_artels": {
    "ru": "Торпедные мастерские",
    "en": "Torpedo Workshops"
  },
  "MKN_torpedo_artels_desc": {
    "ru": "Торпедные мастерские займутся качеством оружия для скрытных атак.",
    "en": "Torpedo workshops will improve weapons for concealed attacks."
  },
  "MKN_torpedo_artels_focus_desc": {
    "ru": "Малые подлодки и рейдеры сделают вражеские перевозки уязвимыми без гонки линкоров.\\n\\nТорпедные мастерские займутся качеством оружия для скрытных атак.\\n\\nЭкипажи научатся выбирать цель и момент атаки, а не искать открытого боя.\\n\\nИспытания устранят отказы и уточнят дистанцию атаки.",
    "en": "Small submarines and raiders will threaten enemy shipping without a battleship race.\\n\\nTorpedo workshops will improve weapons for concealed attacks.\\n\\nCrews will choose targets and timing rather than seek open battle.\\n\\nTrials will eliminate failures and establish attack ranges."
  },
  "MKN_torpedo_trials": {
    "ru": "Испытания торпед",
    "en": "Torpedo Trials"
  },
  "MKN_torpedo_trials_desc": {
    "ru": "Испытания устранят отказы и уточнят дистанцию атаки.",
    "en": "Trials will eliminate failures and establish attack ranges."
  },
  "MKN_tractors_for_grain_desc": {
    "ru": "Зерновой договор даст нам станки вместе с тракторами. Получим бонусы к промышленным исследованиям, два военных завода и улучшение строительства.",
    "en": "The grain contract buys machine tools as well as tractors. Gain industrial research bonuses, two military factories and stronger construction capacity."
  },
  "MKN_triumph_of_free_soviets_desc": {
    "ru": "Волин спрашивает делегатов, кто дал штабу право править. При подготовленном съезде и поддержке не менее 40% анархо-коммунизм станет правящей программой местных советов с отзывными делегатами.",
    "en": "Volin asks the delegates who gave a staff the right to govern. With a prepared congress and at least 40% support, anarcho-communism becomes the ruling program of recallable local councils."
  },
  "MKN_ukrainian_administration_category": {
    "ru": "Украинское самоуправление",
    "en": "Ukrainian Self-Government"
  },
  "MKN_ukrainian_administration_category_desc": {
    "ru": "После исчезновения Советской Украины делегаты могут определить место общего политического центра Вольной территории.",
    "en": "After Soviet Ukraine ceases to exist, delegates can choose the political centre of the Free Territory."
  },
  "MKN_ukrainian_communes_congress_desc": {
    "ru": "Война закончилась, но власть над областями ещё не стала общим договором. Созовём делегатов всех бывших украинских земель и определим порядок добровольного самоуправления.",
    "en": "The war is over, but ownership has yet to become a shared compact. Delegates from the former Ukrainian lands will define local self-government."
  },
  "MKN_ukrainian_frontier_root_desc": {
    "ru": "Между сходами Гуляйполя и комиссариатами Харькова каждый железнодорожный узел стал предметом спора о самой революции. Съезд должен определить общую политику приграничных коммун, пока за него это не сделала винтовка случайного дозорного.",
    "en": "Between Huliaipole's assemblies and Kharkiv's commissariats, every railway junction has become an argument about the revolution itself. The Congress must give the frontier communes a common policy before a patrol's rifle decides it for them."
  },
  "MKN_ukrainian_rail_reconstruction_desc": {
    "ru": "После согласования всех региональных хартий ремонтные артели свяжут Одессу, Киев и Глухов. Постоянные бонусы строительства и ремонта развивают общий хозяйственный дух.",
    "en": "Once regional charters are agreed, repair artels connect Odesa, Kyiv and Hlukhiv. Permanent construction and repair bonuses develop the shared economic spirit."
  },
  "MKN_underground_combat_tt": {
    "ru": "Общий дух армии: +10% к атаке и защите на чужой, ненациональной для нас территории.",
    "en": "Shared army spirit: +10% attack and defence on territory that is not our core."
  },
  "MKN_underway_refit_artels_desc": {
    "ru": "Плавмастерские и тайные рейды позволят спасать повреждённые суда и отрывать их от преследования. Рейдеры вернутся к делу после ремонта, а не останутся на дне.",
    "en": "Floating workshops and concealed anchorages will recover damaged vessels and help them escape pursuit, returning raiders to service."
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
  "MKN_untrained_militias_desc": {
    "ru": "Храбрость не заменяет связи, подготовки и ответственности командиров. Сельские отряды умеют сражаться поодиночке, но теряются в общей операции.",
    "en": "Courage cannot replace communications, training and accountable command. Village detachments fight well alone but struggle in joint operations."
  },
  "MKN_village_airfields": {
    "ru": "Сельские аэродромы",
    "en": "Village Airfields"
  },
  "MKN_village_airfields_desc": {
    "ru": "Полевые полосы приблизят авиацию к войскам и сократят бесполезные перелёты.",
    "en": "Forward strips will bring aircraft closer to troops and reduce ferry flights."
  },
  "MKN_village_muster": {
    "ru": "Сельские сборные пункты",
    "en": "Village Muster Points"
  },
  "MKN_village_muster_desc": {
    "ru": "Сельские сборные пункты заранее распределят людей по отрядам.",
    "en": "Village mustering stations will assign recruits to detachments in advance."
  },
  "MKN_volunteer_recipients_tt": {
    "ru": "Добровольческая солидарность: получатель ведёт гражданскую войну и имеет коммунистическое или демократическое правительство.",
    "en": "Volunteer solidarity requires a communist or democratic recipient fighting a civil war."
  },
  "MKN_welcome_cnt_fai_exiles": {
    "ru": "Принять испанских изгнанников НКТ–ФАИ",
    "en": "Welcome Spanish CNT-FAI Exiles"
  },
  "MKN_welcome_cnt_fai_exiles_desc": {
    "ru": "Предоставим убежище испанским анархистам, изгнанным репрессиями. Буэнавентура Дуррути станет генералом 4-го уровня — специалистом по городским штурмам, горным боям и диверсионным действиям.",
    "en": "Offer refuge to Spanish anarchists driven into exile by repression. Buenaventura Durruti joins as a level 4 general, an urban assault specialist, mountaineer and commando."
  },
  "MKN_worker_battalions_desc": {
    "ru": "Выборные бригадиры и заводские инструкторы подготовят резерв без разрыва с производством. Общие сборы улучшат организацию и планирование армии и сократят подготовку новых частей.",
    "en": "Elected brigadiers and factory instructors train a reserve without severing its ties to production. Joint exercises improve organization and planning while reducing training time."
  },
  "MKN_worker_battalions_idea": {
    "ru": "Подготовленные рабочие батальоны",
    "en": "Trained Worker Battalions"
  },
  "MKN_worker_battalions_idea_desc": {
    "ru": "Заводские смены и военные сборы согласованы. Избранные командиры отвечают за подготовку и совместные операции.",
    "en": "Factory shifts and military training are coordinated. Elected commanders are accountable for readiness and joint operations."
  },
  "MKN_workers_corridors_desc": {
    "ru": "Торговля станками и обмен инженерами откроют двери, которых не открыть одной агитацией. Предложим соседям равноправные технические соглашения. Решение остаётся за получателем.",
    "en": "Machine-tool trade and visiting engineers open doors that agitation alone cannot. Offer equal technical agreements to neighbouring states, which remain free to accept or refuse."
  },
  "MKN_workers_corridors_tt": {
    "ru": "Внешняя служба коммун: влияние отношений на торговлю §G+10%§!. Открываются предложения обмена промышленными специалистами с Литвой-Беларусью, Австрией, Германией, Османской империей и Венгрией за §Y50 PP§!. При согласии обе стороны получают одну скидку §G50%§! на промышленное исследование и §G+30§! к взаимному мнению.",
    "en": "Communal Foreign Service: trade opinion factor §G+10%§!. Unlock §Y50 PP§! technical exchange offers to Lithuania–Belarus, Austria, Germany, the Ottoman Empire and Hungary. Acceptance grants each party one §G50%§! industrial research bonus and §G+30§! mutual opinion."
  },
  "MKN_workshop_airplane_artels_desc": {
    "ru": "Разъездные авиамастерские ремонтируют и сколачивают машины прямо под открытым небом.",
    "en": "Itinerant aviation workshops repair and assemble machines in the open air."
  },
  "MKN_workshop_exchange_offer_tt": {
    "ru": "Партнёр получит предложение: при согласии обе стороны получат одну промышленную скидку §G50%§! и §G+30§! к взаимному мнению.",
    "en": "The recipient may accept: both countries then receive one §G50%§! industrial research bonus and §G+30§! mutual opinion."
  },
  "MKN_workshop_exchange_opinion": {
    "ru": "Обмен промышленными специалистами",
    "en": "Industrial Technical Exchange"
  },
  "MKN_workshop_standards_desc": {
    "ru": "Общие калибры, ремонтные образцы и портфель заказов соединят самостоятельные мастерские. Дополнительный военный завод и развитие оружейного предприятия повысят выпуск и эффективность без единственного промышленного центра.",
    "en": "Common calibres, repair patterns and pooled orders unite independent workshops. Another military factory and an upgraded weapons enterprise improve output without a single industrial centre."
  },
  "MKN_zaporizhstal_desc": {
    "ru": "Две новые линии и дополнительные плавки станут основой концерна «Вольная сталь». Промышленный совет доступен всем коммунам; с Arms Against Tyranny заводы также образуют артиллерийскую MIO, развиваемую производственными циклами и финальным договором.",
    "en": "Two new production lines and additional steel establish the Free Steel concern. Its industrial council is available with or without DLC; Arms Against Tyranny also enables an artillery MIO developed through production cycles and the final compact."
  },
  "MKN_zaporizhstal_organization": {
    "ru": "Концерн «Вольная сталь»",
    "en": "Free Steel Concern"
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
  "NWW_MKN_andrii_dorosh_desc": {
    "ru": "Персонаж альтернативного лора: специалист местных служб вольной территории.",
    "en": "An alternate lore character serving the Free Territorys local institutions."
  },
  "NWW_MKN_andrii_dorosh_high_command": {
    "ru": "Андрей Дорош",
    "en": "Andrii Dorosh"
  },
  "NWW_MKN_andrii_dorosh_specialty": {
    "ru": "Организатор территориальной обороны",
    "en": "Territorial Defence Organizer"
  },
  "NWW_MKN_andrii_dorosh_specialty_desc": {
    "ru": "Опыт местных служб превращён в практическую специализацию советника.",
    "en": "Experience in local services becomes a practical advisor specialization."
  },
  "NWW_MKN_dmytro_savchenko": {
    "ru": "Дмитро Савченко",
    "en": "Dmytro Savchenko"
  },
  "NWW_MKN_dmytro_savchenko_advisor": {
    "ru": "Дмитро Савченко",
    "en": "Dmytro Savchenko"
  },
  "NWW_MKN_dmytro_savchenko_desc": {
    "ru": "Персонаж альтернативного лора: специалист местных служб вольной территории.",
    "en": "An alternate lore character serving the Free Territorys local institutions."
  },
  "NWW_MKN_dmytro_savchenko_specialty": {
    "ru": "Координатор авиации поддержки",
    "en": "Support Aviation Coordinator"
  },
  "NWW_MKN_dmytro_savchenko_specialty_desc": {
    "ru": "Опыт местных служб превращён в практическую специализацию советника.",
    "en": "Experience in local services becomes a practical advisor specialization."
  },
  "NWW_MKN_eugen": {
    "ru": "Евген",
    "en": "Eugen"
  },
  "NWW_MKN_eugen_desc": {
    "ru": "Молодой командир, выросший из пехотных отрядов Вольной территории. Для Евгена взаимодействие отделений, разведка и вынос раненых важнее красивой атаки. Он может одновременно командовать армией и служить советником высшего командования.",
    "en": "A young commander who rose through the Free Territory’s infantry detachments. Eugen values squad coordination, reconnaissance and casualty evacuation above a spectacular charge. He can command an army while serving in the high command."
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
  "NWW_MKN_ivan_bondarenko_desc": {
    "ru": "Персонаж альтернативного лора: специалист местных служб вольной территории.",
    "en": "An alternate lore character serving the Free Territorys local institutions."
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
  "NWW_MKN_mykola_kovalenko_desc": {
    "ru": "Персонаж альтернативного лора: специалист местных служб вольной территории.",
    "en": "An alternate lore character serving the Free Territorys local institutions."
  },
  "NWW_MKN_mykola_kovalenko_specialty": {
    "ru": "Исследователь подвижной войны",
    "en": "Mobile Warfare Scholar"
  },
  "NWW_MKN_mykola_kovalenko_specialty_desc": {
    "ru": "Опыт местных служб превращён в практическую специализацию советника.",
    "en": "Experience in local services becomes a practical advisor specialization."
  },
  "NWW_MKN_oleksandr_hordiienko": {
    "ru": "Олександр Гордиенко",
    "en": "Oleksandr Hordiienko"
  },
  "NWW_MKN_oleksandr_hordiienko_advisor": {
    "ru": "Олександр Гордиенко",
    "en": "Oleksandr Hordiienko"
  },
  "NWW_MKN_oleksandr_hordiienko_desc": {
    "ru": "Персонаж альтернативного лора: специалист местных служб вольной территории.",
    "en": "An alternate lore character serving the Free Territorys local institutions."
  },
  "NWW_MKN_olena_hrytsenko": {
    "ru": "Олена Гриценко",
    "en": "Olena Hrytsenko"
  },
  "NWW_MKN_olena_hrytsenko_advisor": {
    "ru": "Олена Гриценко",
    "en": "Olena Hrytsenko"
  },
  "NWW_MKN_olena_hrytsenko_desc": {
    "ru": "Персонаж альтернативного лора: специалист местных служб вольной территории.",
    "en": "An alternate lore character serving the Free Territorys local institutions."
  },
  "NWW_MKN_peter_arshinov": {
    "ru": "Пётр Аршинов",
    "en": "Peter Arshinov"
  },
  "NWW_MKN_petro_stepanenko": {
    "ru": "Петро Степаненко",
    "en": "Petro Stepanenko"
  },
  "NWW_MKN_petro_stepanenko_desc": {
    "ru": "Персонаж альтернативного лора: специалист местных служб вольной территории.",
    "en": "An alternate lore character serving the Free Territorys local institutions."
  },
  "NWW_MKN_roman_danylenko": {
    "ru": "Роман Даниленко",
    "en": "Roman Danylenko"
  },
  "NWW_MKN_roman_danylenko_advisor": {
    "ru": "Роман Даниленко",
    "en": "Roman Danylenko"
  },
  "NWW_MKN_roman_danylenko_desc": {
    "ru": "Персонаж альтернативного лора: специалист местных служб вольной территории.",
    "en": "An alternate lore character serving the Free Territorys local institutions."
  },
  "NWW_MKN_school_delegate": {
    "ru": "Делегат технических коммун",
    "en": "Technical Commune Delegate"
  },
  "NWW_MKN_serhii_melnyk": {
    "ru": "Сергий Мельник",
    "en": "Serhii Melnyk"
  },
  "NWW_MKN_serhii_melnyk_desc": {
    "ru": "Персонаж альтернативного лора: специалист местных служб вольной территории.",
    "en": "An alternate lore character serving the Free Territorys local institutions."
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
  "NWW_MKN_yakiv_levchenko_desc": {
    "ru": "Персонаж альтернативного лора: специалист местных служб вольной территории.",
    "en": "An alternate lore character serving the Free Territorys local institutions."
  },
  "NWW_MKN_yakiv_levchenko_specialty": {
    "ru": "Защитник приморских сообщений",
    "en": "Coastal Sea Lane Defender"
  },
  "NWW_MKN_yakiv_levchenko_specialty_desc": {
    "ru": "Опыт местных служб превращён в практическую специализацию советника.",
    "en": "Experience in local services becomes a practical advisor specialization."
  },
  "NWW_SOV_MKN_settlement": {
    "ru": "Заключён Гуляйпольский хозяйственный протокол",
    "en": "The Huliaipole economic protocol is in force"
  },
  "NWW_default_communism": {
    "ru": "Коммунизм",
    "en": "Communist"
  },
  "NWW_default_communism_desc": {
    "ru": "Тоталитарный режим",
    "en": "Totalitarian Regime"
  },
  "NWW_default_communism_noun": {
    "ru": "Коммунизм",
    "en": "Communism"
  },
  "NWW_default_democratic": {
    "ru": "Демократия",
    "en": "Democratic"
  },
  "NWW_default_democratic_desc": {
    "ru": "Демократическое государство",
    "en": "Democratic State"
  },
  "NWW_default_democratic_noun": {
    "ru": "Демократия",
    "en": "Democracy"
  },
  "NWW_default_fascism": {
    "ru": "Фашизм",
    "en": "Fascist"
  },
  "NWW_default_fascism_desc": {
    "ru": "Тоталитарный режим",
    "en": "Totalitarian Regime"
  },
  "NWW_default_fascism_noun": {
    "ru": "Фашизм",
    "en": "Fascism"
  },
  "NWW_default_neutrality": {
    "ru": "Нейтралитет",
    "en": "Non-Aligned"
  },
  "NWW_default_neutrality_desc": {
    "ru": "Авторитарный режим",
    "en": "Authoritarian Regime"
  },
  "NWW_default_neutrality_noun": {
    "ru": "Нейтралитет",
    "en": "Non-Aligned"
  },
  "UKR_mkn_escalation_required_tt": {
    "ru": "Нападение на Махновщину возможно только после завершения пограничной эскалации.",
    "en": "An attack on the Free Territory requires the conclusion of frontier escalation."
  },
  "communism": {
    "ru": "Коммунизм",
    "en": "Communist"
  },
  "communism_desc": {
    "ru": "Тоталитарный режим",
    "en": "Totalitarian Regime"
  },
  "democratic": {
    "ru": "Демократия",
    "en": "Democratic"
  },
  "democratic_desc": {
    "ru": "Демократическое государство",
    "en": "Democratic State"
  },
  "fascism": {
    "ru": "Фашизм",
    "en": "Fascist"
  },
  "fascism_desc": {
    "ru": "Тоталитарный режим",
    "en": "Totalitarian Regime"
  },
  "mkn.30.a": {
    "ru": "Ускорить строительство, приняв расходы.",
    "en": "Accelerate construction and accept the cost."
  },
  "mkn.30.b": {
    "ru": "Переоснащать предприятия постепенно.",
    "en": "Retool factories gradually."
  },
  "mkn.30.d": {
    "ru": "Делегаты Днепростроя проверили сметы. Ускоренный сезон даст больше строек, но потребует дополнительных средств от потребительского сектора. Постепенное переоснащение поможет осваивать производство без чрезвычайных сборов. Какой порядок мы принимаем на ближайший год?",
    "en": "Dnieper delegates have audited the budgets. An intensive season speeds construction but requires more resources from consumer production. Gradual retooling improves production efficiency without emergency collections. Which policy shall govern the coming year?"
  },
  "mkn.30.t": {
    "ru": "Смета принадлежит съезду",
    "en": "The Budget Belongs to the Congress"
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
  "mkn_black_international_category": {
    "ru": "Чёрный интернационал",
    "en": "The Black International"
  },
  "mkn_black_international_category_desc": {
    "ru": "Иностранных товарищей можно принять после фокуса «Чёрный интернационал» в синдикалистской или аграрной программе. Каждая группа стоит 50 единиц политической власти и принимается лишь один раз.",
    "en": "Foreign comrades can be welcomed after completing The Black International through either the syndicalist or agrarian programme. Each group costs 50 political power and can be welcomed only once."
  },
  "mkn_commune_secretary": {
    "ru": "Секретарь общин",
    "en": "Commune Secretary"
  },
  "mkn_cooperative_treasurer": {
    "ru": "Казначей кооперативов",
    "en": "Cooperative Treasurer"
  },
  "mkn_crisis.1.a": {
    "ru": "Приспустить чёрный флаг. Созвать делегатов.",
    "en": "Lower the black flag. Convene the delegates."
  },
  "mkn_crisis.1.d": {
    "ru": "Перед рассветом посыльный из Гуляйполя добрался до здания съезда. Он принёс не приказ, а потёртую шапку Махно. Батько умер. На станциях гудят паровозы, которые никуда не отправляются; в сёлах сходы стоят молча. Тратишов требует общего командования, Волин — федерации вольных советов, крестьяне — закрытой житницы, красные делегаты — революционной администрации. Похороны дали нам тишину, но не согласие. У нас 180 дней.",
    "en": "Before dawn, the runner from Huliaipole reached the congress building. He carried no order, only Makhno’s worn cap. The Batko is dead. At the stations, whistles sound without a departure; in the villages, the assemblies stand in silence. Tratishov wants a common command, Volin a federation of free councils, the peasants a closed granary, and the red delegates a revolutionary administration. The funeral has bought us silence, not agreement. We have 180 days."
  },
  "mkn_crisis.1.t": {
    "ru": "Последний вздох Батько",
    "en": "The Last Breath of the Batko"
  },
  "mkn_crisis.100.a": {
    "ru": "Удержать свою землю.",
    "en": "Hold our ground."
  },
  "mkn_crisis.100.d": {
    "ru": "Срок урегулирования преемственности истёк. Сильнейшая оппозиционная партия бросила вызов действующей власти: Вольная территория раскололась на два вооружённых лагеря. В решениях можно поддержать действующее правительство или перейти к повстанцам. Победа откроет политическую программу победителя.",
    "en": "The succession deadline has expired. The strongest opposition party has challenged the incumbent government, dividing the Free Territory into two armed camps. Use the decisions to remain with the established order or rally to the insurgents. Victory will open the winning political program."
  },
  "mkn_crisis.100.t": {
    "ru": "Степь горит: распад на четыре лагеря",
    "en": "The Steppe Burns: Four-Way Collapse"
  },
  "mkn_crisis.20.a": {
    "ru": "Открыть транзит и переговоры о снабжении.",
    "en": "Open the transit and supply talks."
  },
  "mkn_crisis.20.b": {
    "ru": "Мы не заключим такого соглашения.",
    "en": "We will make no such agreement."
  },
  "mkn_crisis.20.d": {
    "ru": "Ревком Вольной территории предлагает зерновые поставки и взаимный военный транзит. Он просит локомотивы, помощь диспетчеров и железнодорожное соединение. Принятие первого соглашения не создаёт альянса или протектората.",
    "en": "The Free Territory’s revkom offers grain deliveries and reciprocal military transit. It asks for locomotives, dispatching expertise and a railway connection. Accepting this first agreement does not create an alliance or a protectorate."
  },
  "mkn_crisis.20.t": {
    "ru": "Посольство из степи",
    "en": "An Embassy from the Steppe"
  },
  "mkn_crisis.200.a": {
    "ru": "Степь ответит огнём.",
    "en": "The steppe will answer with fire."
  },
  "mkn_crisis.200.d": {
    "ru": "Сто дней соперничающие съезды объявляли себя наследниками чёрного знамени, а сёла переходили из рук одних братьев в руки других. Теперь предупреждение советских республик стало приказом о наступлении. Москва говорит о восстановлении революционного порядка; Харьков требует обезопасить границу. Их колонны выступают против всех уцелевших претендентов на Вольную территорию, разрывая даже союзы, которые мешают походу. Наш раздор дал комиссарам возможность вмешаться. Степи предстоит встретить чужую войну прежде, чем закончится её собственная.",
    "en": "For a hundred days, rival congresses have claimed the black banner while villages changed hands between brothers. Now the warning from the Soviet republics has become a marching order. Moscow speaks of restoring revolutionary order; Kharkiv demands that the frontier be secured. Their columns move against every surviving claimant to the Free Territory, repudiating even alliances that stand in their way. Our quarrel has given the commissars their opening. The steppe must face a foreign war before its own war is over."
  },
  "mkn_crisis.200.t": {
    "ru": "Красная Армия переходит Днепр",
    "en": "The Red Army Crosses the Dnieper"
  },
  "mkn_crisis.21.a": {
    "ru": "Пусть диспетчеры приступают к работе.",
    "en": "Let the dispatchers get to work."
  },
  "mkn_crisis.21.d": {
    "ru": "Советские республики приняли взаимный транзит. Наши инженеры теперь могут подготовить железнодорожное соединение через контролируемую общую границу, после чего начнутся два года сотрудничества в снабжении.",
    "en": "The Soviet Republics have accepted reciprocal transit. Our engineers may now prepare a railway connection across a controlled common border, followed by two years of supply cooperation."
  },
  "mkn_crisis.21.t": {
    "ru": "Харьков открывает разъезды",
    "en": "Kharkov Opens the Sidings"
  },
  "mkn_crisis.22.a": {
    "ru": "Житница остаётся нашей.",
    "en": "The granary remains ours."
  },
  "mkn_crisis.22.d": {
    "ru": "Делегация вернулась с вежливыми словами, но без соглашения. Мы сохраняем независимость и можем возобновить переговоры через решение.",
    "en": "The delegation returned with polite phrases and no agreement. We retain our independence and may reopen negotiations through a decision."
  },
  "mkn_crisis.22.t": {
    "ru": "Советские ворота остаются закрытыми",
    "en": "The Soviet Gates Stay Closed"
  },
  "mkn_crisis.23.a": {
    "ru": "Принять равноправных союзников.",
    "en": "Welcome equal allies."
  },
  "mkn_crisis.23.b": {
    "ru": "Отказаться от фронта.",
    "en": "Decline the front."
  },
  "mkn_crisis.23.d": {
    "ru": "Вольная территория предлагает равноправный оборонительный союз против ЛитБела и имперской Германии. Её советы сохранят собственную администрацию и вооружённые силы. Примем ли мы предложение?",
    "en": "The Free Territory proposes an equal defensive alliance against LitBel and Imperial Germany. Its councils will keep their own administration and armed forces. Shall we accept?"
  },
  "mkn_crisis.23.t": {
    "ru": "Общий антиимпериалистический фронт?",
    "en": "A Common Anti-Imperialist Front?"
  },
  "mkn_crisis.24.a": {
    "ru": "Ратифицировать общую оборону.",
    "en": "Ratify the common defense."
  },
  "mkn_crisis.24.d": {
    "ru": "Советское правительство приняло нас в общий оборонительный фронт. Наш флаг по-прежнему реет над съездом; следующий вопрос — переживёт ли равноправие свою письменную хартию.",
    "en": "The Soviet government has admitted us to the common defensive front. Our flag still flies above our congress; the next question is whether equality will survive its written charter."
  },
  "mkn_crisis.24.t": {
    "ru": "Общий фронт подписан",
    "en": "The Common Front Is Signed"
  },
  "mkn_crisis.25.a": {
    "ru": "Придётся опираться на себя.",
    "en": "We must rely on ourselves."
  },
  "mkn_crisis.25.d": {
    "ru": "Советское правительство отказало в союзе. Наши советы остаются независимыми, а посланники смогут повторить предложение, когда обстоятельства изменятся.",
    "en": "The Soviet government has declined the alliance. Our councils remain independent, and our envoys may ask again when circumstances change."
  },
  "mkn_crisis.25.t": {
    "ru": "Общего фронта не будет",
    "en": "No Common Front"
  },
  "mkn_crisis.30.a": {
    "ru": "Переждать остановку.",
    "en": "Endure the stoppage."
  },
  "mkn_crisis.30.b": {
    "ru": "Разгромить стачечные комитеты.",
    "en": "Break the strike committees."
  },
  "mkn_crisis.30.d": {
    "ru": "Листовки из Вольной территории всю ночную смену переходили из рук в руки. Рабочие требуют выборных комитетов мастерских и угрожают шестьюдесятью днями стачек. Мы можем переждать остановку или потратить политический капитал на подавление.",
    "en": "Pamphlets from the Free Territory have passed from hand to hand through the night shift. The workers demand elected workshop committees and threaten sixty days of industrial action. We can endure the stoppage or spend political capital on a crackdown."
  },
  "mkn_crisis.30.t": {
    "ru": "Чёрный флаг над заводскими воротами",
    "en": "A Black Flag above the Factory Gate"
  },
  "mkn_crisis.40.a": {
    "ru": "Ратифицировать равноправную автономию.",
    "en": "Ratify equal autonomy."
  },
  "mkn_crisis.40.b": {
    "ru": "Изгнать их. Принудить к подчинению.",
    "en": "Expel them. Force their submission."
  },
  "mkn_crisis.40.c": {
    "ru": "Переговоры стали невозможны.",
    "en": "The negotiations have become impossible."
  },
  "mkn_crisis.40.d": {
    "ru": "Делегаты Вольной территории представили пленуму хартию автономии. Она требует равноправного суверенитета в общем фронте: никаких назначенных губернаторов, реквизиций без согласия и иностранной оккупации. Мы можем ратифицировать равноправие или изгнать территорию и навязать подчинение войной.",
    "en": "The Free Territory’s delegates have placed an autonomy charter before the plenum. It demands equal sovereignty inside our common front: no appointed governors, no requisitions without consent, no foreign occupation. We may ratify this equality or expel the territory and enforce submission by war."
  },
  "mkn_crisis.40.t": {
    "ru": "Роковой пленум",
    "en": "The Fatal Plenum"
  },
  "mkn_crisis.41.a": {
    "ru": "Пусть хартия висит над каждым столом.",
    "en": "Keep the charter above every desk."
  },
  "mkn_crisis.41.d": {
    "ru": "Пленум принял хартию. Наши советы сохраняют свою администрацию и суверенитет в общем фронте. На этот раз революционное обещание дошло до протокола без искажений.",
    "en": "The plenum accepted the charter. Our councils retain their administration and sovereignty within the common front. For once, a revolutionary promise has reached the ledger intact."
  },
  "mkn_crisis.41.t": {
    "ru": "Хартия равных",
    "en": "A Charter between Equals"
  },
  "mkn_crisis.42.a": {
    "ru": "Они не найдут беззащитного села.",
    "en": "They shall find no undefended village."
  },
  "mkn_crisis.42.d": {
    "ru": "Посланники задержаны. За границей советские колонны идут к станциям, которые сами помогли соединить. Союз разорван, война началась. На съезде старый повстанец открывает зерновую книгу и пишет поперёк неё одно слово: предательство. Целый год каждое село будет давать на него ответ.",
    "en": "The envoys have been detained. Across the frontier, Soviet columns advance toward the stations they helped connect. The alliance is broken and the war has begun. At the congress, one old insurgent opens the grain ledger and writes a single word across it: betrayal. For a year, every village shall answer."
  },
  "mkn_crisis.42.t": {
    "ru": "Преданы дважды",
    "en": "Betrayed Twice"
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
  "mkn_eugen_infantry_master_desc": {
    "ru": "Сочетает огонь и движение, бережёт пехоту и быстро возвращает подразделения в строй. Назначение требует создания степного генерального штаба.",
    "en": "Combines fire and movement, preserves his infantry and quickly returns units to action. Appointment requires the Steppe General Staff."
  },
  "mkn_foreign.1.a": {
    "ru": "Принять предложение.",
    "en": "Accept the exchange."
  },
  "mkn_foreign.1.b": {
    "ru": "Отказаться от обмена.",
    "en": "Decline the exchange."
  },
  "mkn_foreign.1.d": {
    "ru": "Представители коммун предлагают взаимный обмен промышленными инженерами. Каждая сторона сохранит собственные предприятия и получит доступ к опыту партнёра. Соглашение улучшит отношения и даст обеим сторонам скидку 50% на одно промышленное исследование.",
    "en": "Communal representatives propose an exchange of industrial engineers. Each country retains its own enterprises while learning from its partner. The agreement improves relations and grants both parties one 50% industrial research bonus."
  },
  "mkn_foreign.1.t": {
    "ru": "Специалисты из Вольной территории",
    "en": "Specialists from the Free Territory"
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
  "mkn_horizons.1.a": {
    "ru": "Примем приглашение.",
    "en": "Accept the invitation."
  },
  "mkn_horizons.1.b": {
    "ru": "Мы выберем свой путь.",
    "en": "We will choose our own course."
  },
  "mkn_horizons.1.d": {
    "ru": "Делегаты Вольной территории предлагают нам место в общем конгрессе и оборонном союзе. Они обещают равное представительство, но принятие приглашения свяжет нашу внешнюю политику с судьбой коммун. Решение остаётся за нами.",
    "en": "Delegates of the Free Territory offer us a seat in their congress and defensive association. They promise equal representation, but membership would bind our foreign policy to the communes. The decision is ours."
  },
  "mkn_horizons.1.t": {
    "ru": "Приглашение Чёрного Интернационала",
    "en": "An Invitation from the Black International"
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
  "mkn_integration.1.a": {
    "ru": "Созвать делегатов областей.",
    "en": "Summon the regional delegates."
  },
  "mkn_integration.1.d": {
    "ru": "Все земли бывшей Советской Украины находятся под нашим владением и контролем. Теперь предстоит договориться о представительстве, восстановить хозяйство и заменить военное управление местными хартиями. В дереве открыта ветка украинской интеграции.",
    "en": "All lands of former Soviet Ukraine are now owned and controlled by us. Representation, reconstruction and local charters must replace military administration. The Ukrainian integration focus branch is now visible."
  },
  "mkn_integration.1.t": {
    "ru": "Украина после войны",
    "en": "Ukraine after the War"
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
  "mkn_news.1.a": {
    "ru": "Батько ушёл. Коммуны остаются.",
    "en": "The Batko is gone. The communes remain."
  },
  "mkn_news.1.b": {
    "ru": "Будущее степи теперь в руках советов.",
    "en": "The steppe’s future now lies in the councils’ hands."
  },
  "mkn_news.1.c": {
    "ru": "Внимательно следить за преемственностью.",
    "en": "Observe the succession closely."
  },
  "mkn_news.1.d": {
    "ru": "В Гуляйполе Нестор Махно лежит в гробу под чёрным флагом. Гроб установлен на простых досках в зале, где сельские делегаты когда-то спорили с ним до рассвета. Железнодорожники принесли паровозный свисток; крестьянка оставила хлеб рядом с его потёртой шапкой. Церковные колокола не отсчитывают час. Это делают станционные гудки.\\n\\nПо всей украинской степи смерть основателя оставляет тишину, которую каждая фракция надеется заполнить. Штаб Тратишова говорит о дисциплине, вольные советы Волина — о нерушимом обещании; сельские делегаты считают зерно, красные комитеты — винтовки. Жизнь Махно окончена. Спор о том, чем должна стать его революция, — нет. Иностранные канцелярии следят за похоронной процессией, гадая, долго ли чёрный флаг останется единым знаменем.",
    "en": "At Huliaipole, Nestor Makhno lies in state beneath a black flag. The casket stands on plain boards in the hall where village delegates once argued with him until dawn. Railway workers have brought a locomotive whistle; a peasant woman has left a loaf of bread beside his worn cap. No church bell marks the hour. The station whistles do.\\n\\nAcross the Ukrainian steppe, the founder’s death leaves a silence that every faction hopes to fill. Tratishov’s staff speaks of discipline, Volin’s free soviets of an unbroken promise; village delegates count the grain, and red committees count the rifles. Makhno’s life has ended. The quarrel over what his revolution must become has not. Foreign chancelleries watch the funeral procession, wondering how long the black flag will remain one banner."
  },
  "mkn_news.1.e": {
    "ru": "Ещё один тревожный рассвет над степью.",
    "en": "Another uncertain dawn for the steppe."
  },
  "mkn_news.1.t": {
    "ru": "Чёрный флаг приспущен: смерть Нестора Махно",
    "en": "Black Flag at Half-Mast: The Death of Nestor Makhno"
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
  "mkn_ukr_border.10.a": {
    "ru": "Коммуны сохранят дозор.",
    "en": "The communes will keep their watch."
  },
  "mkn_ukr_border.10.d": {
    "ru": "Через семь дней после того, как Гуляйполе приспустило чёрные знамёна, советская разведка подтвердила смерть Батьки. Дозоры Советской Украины проверяют дороги вдоль нашего рубежа; донесения идут между Харьковом и штабами Красной армии. У часового отбирают оружие, зерновую повозку поворачивают назад, на предупредительный выстрел отвечают выстрелом. Советы встречают первую тревогу без Махно. У рубежа один год, прежде чем война или истощение определят его будущее.",
    "en": "Seven days after Huliaipole lowered its black flags, Soviet intelligence has confirmed the Batko's passing. Patrols of Soviet Ukraine test the roads along our frontier, backed by reports passed between Kharkiv and the Red Army staff. A sentry is disarmed; a grain cart is turned back; a warning shot answers a warning shot. The councils face their first alarm without Makhno. The frontier has one year before either war or exhaustion decides its future."
  },
  "mkn_ukr_border.10.t": {
    "ru": "Советы почуяли слабость",
    "en": "Soviets Sense Weakness"
  },
  "mkn_ukr_frontier_concluded": {
    "ru": "Кризис на рубеже завершён",
    "en": "The frontier crisis has ended"
  },
  "mkn_ukr_total_war": {
    "ru": "На рубеже началась полномасштабная война",
    "en": "Full war has begun on the frontier"
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
  },
  "neutrality_desc": {
    "ru": "Авторитарный режим",
    "en": "Authoritarian Regime"
  }
}
```

## Воспроизводимость

Обновить файл: `python tools/export_mkn_political_focuses.py`. Разворачиваются только действующие direct/shared_focus; ID событий и провинций не превращаются в фокусы. SHA-256 источников:

```text
1110643a56453c6a81fb276386a267eb0c3ef72f0ef7c862bcce9b2749787327  common/ai_strategy_plans/MKN_historical.txt
e0ddaac0730379f5a32bae24bc0139c376fc4d679bb50c41f67d47c49379f682  common/bop/MKN_bop.txt
e8fb6d1f088c7ba684cc9983335af17d284e565951d434a03c752483821935d6  common/characters/MKN.txt
9c97e35f68d003e95a2f1ff3ec33b441eefc8a21066d0ed730074885ac946ba7  common/characters/MKN_eugen.txt
ae835996da49af348dfdee1ebb27c3c2a8b795a3efb4fb4069b244abc5d1653f  common/characters/nww_MKN.txt
97a1ce993e5183d05fd9ddb36052b770e6889fae6f45992c27076fa8f1a85529  common/decisions/MKN_bop_decisions.txt
1c44816adb57d2dad4e7a2d1d8334d8738e4a90c5fb47b24d78693459832808b  common/decisions/MKN_decisions.txt
2f768f1a3ad2a14441b8c046840ce2464872b82bf956f11da15859eb067c32b2  common/decisions/MKN_foreign_decisions.txt
16e88b8e583b36bd80457c328860f0eaec43e220408cd51e701f192f4e6f6dc7  common/decisions/MKN_horizons_decisions.txt
f98fe9038c9fd578b8580bdad4ef77eb9d1df7d91d574d3a293a53151a56b2cb  common/decisions/MKN_international_decisions.txt
a3623a7987696c30fdc35e9936cce71ffcfa91bde6f12dd924c9d4e65f574857  common/decisions/MKN_ukraine_integration_decisions.txt
7e631c3cda7136c7ce75e86efd093d5259ae8fa263fe6c21d9a308d2adf9fc85  common/decisions/categories/MKN_bop_categories.txt
248409773d090369fb992f7001aba00df1f98e5a381d645c4d41a4ec34cfa730  common/decisions/categories/MKN_horizons_categories.txt
88e1ee6b797e66433a75093514936f2c690320642d2cd7b72bec69fbf564a2a5  common/decisions/categories/MKN_international_categories.txt
7eb399ea1a4c2f724c9614e5e92aa4258ba38c26e340469c016867de4885a5a5  common/decisions/categories/MKN_ukraine_integration_categories.txt
a63efd94457fbb21e8b62cc29a2f94dcfd4c4ddd1bbb6c1d32f40db9b4fe68f4  common/dynamic_modifiers/nww_dynamic_modifiers.txt
7a13b7399fd46a039bc9b0750dc93d154268e3ec903b5a965f305bccbe592675  common/ideas/MKN_horizons_ideas.txt
25371b7edaff96981cfd0ed8d0f8e5c574c32184c69e30202d4f86d53a44417f  common/ideas/MKN_ideas.txt
e05c2d6467285c783175b4a05bec616818bd86597ca02aa6d603db9fceae74b4  common/ideas/MKN_international_ideas.txt
96dc19b62d8d55f44ffba9f38a6247189c316b315975f526b9e2105ea8934442  common/ideas/nww_MKN_ideas.txt
1735eabf212c41c9ad4a3d5f071d4b50b43d830530125bebaf652d8c1e545e03  common/national_focus/MKN.txt
fed0b51e7277a49ca2a9a510bd3e5ec0ace054616aef437b03056bb929fa34ac  common/national_focus/MKN_foreign_focuses.txt
4e39c73ed5232c8e112138cc7144576438c75285d4a69c4910a3e768cfe65e47  common/national_focus/MKN_horizons_focuses.txt
dbcfa07e090dcbdb2a48944dcb1bdfec39cf0641d4cb846d9f7b4708b5ec13c0  common/national_focus/MKN_ukraine_integration_focuses.txt
f1d41e2efcad84f6895063dd2513592a2f8ed9721fab3dfc9c774c48929fff38  common/on_actions/MKN_ai_on_actions.txt
25c971beb1d448945d80e1be27ce8d424669a482446028b6e66a74699cb4d54d  common/on_actions/MKN_diplomacy_on_actions.txt
1b4c3198c243d4a947502ddbe6d0dcc80f6f2a44aea693c5806707e5f90b6baa  common/on_actions/MKN_flag_on_actions.txt
99bbdff54b5336459600253aae4f5820d132356233ada7c8c918d09ab7b0729b  common/on_actions/MKN_horizons_on_actions.txt
94021c1606a809debbc52043c2d86e94ad8337ba8310aa387011c26f7dc702b2  common/on_actions/MKN_international_on_actions.txt
b23bc4ec1f93fc3bda6fe537fc93bb4cca1159eedad338558f2c8adac5963a84  common/on_actions/MKN_intervention_on_actions.txt
46a5ddfed624b0d9f01b26b0aa16156e3b1fdcfbebfc3dcdf84db3a4387f4111  common/on_actions/MKN_overhaul_on_actions.txt
6d314a2713657a66015820f504d8430c0f6b538279e13fe5f7c6ba8a2b58aded  common/on_actions/MKN_ukraine_integration_on_actions.txt
8ba12712b4565cbd2fec4c0b073f4f361d5339b2545caf9bc106cd830f245b6e  common/on_actions/nww_mkn_progression.txt
8dced1e3e7b7bd159d0e85eefc0feef3d427a373bdfff9bbcb25563db12760c6  common/scripted_effects/MKN_ai_effects.txt
dd312eb87ff80e0cacbfaaf4330fc3713c9da35b34000c3900dea4e539581e49  common/scripted_effects/MKN_bop_effects.txt
b47b550819e67a2e0449cccbf3fbe0b6c8b7a6c11318572661f5ca013f6f369f  common/scripted_effects/MKN_diplomacy_effects.txt
1e97f095e431564a35ea7cc885ce59c024767e131412ef1bd480b89977e36145  common/scripted_effects/MKN_effects.txt
d9ab534a992666991426f07f60e50c1adc68852e6beb2b5c3d6f2c5850573c76  common/scripted_effects/MKN_flag_effects.txt
4f84723fed9625ecb635524860c7d904083cb9a14e1c96875319c9f7c90c9c50  common/scripted_effects/MKN_foreign_effects.txt
083ddc189318c367f61d837e0f07399c4c16a0ee378934fafb8f17dbd52f2353  common/scripted_effects/MKN_horizons_effects.txt
3ac85e3db10933a424a94dcc80809b897c255e5ba4085737bb23c04d92a3a43c  common/scripted_effects/MKN_international_effects.txt
98844eb72d4ac511ffdbe432070ebc7d9b653c243e76403f378dcf6564ca132b  common/scripted_effects/MKN_intervention_effects.txt
5e4676c26684230d6988daa8ea66ae0609968f2c9c9ca82e7d21e73b214aa5af  common/scripted_effects/MKN_overhaul_effects.txt
2fba7ad1b7578a1df55642e9d3e2b5e60803576f71d3c27073e1082a090858bc  common/scripted_effects/MKN_research_effects.txt
8849a0de9fa5f9580d965b008551a273f573b90ec9fe81df19dd086120bbc91d  common/scripted_effects/MKN_ukr_border_effects.txt
13cffd84d32871baaf7b37611b06e0d781064ee4a54c1d9804952e5229ac9db1  common/scripted_effects/MKN_ukraine_integration_effects.txt
5a85c46700f94a4f44712baff05fbeb96c04e3a9178af3cbc6fe6ece0ac75cfc  common/scripted_effects/nww_mkn_progression.txt
43365ce7510b5555334c5bd4ca630878bde6f82bc8680b72786c071bcf4dc7d3  common/scripted_localisation/MKN_ideology_names.txt
8a45fc52e627d16b16e5da59bcfffb6abc8d5d04c35e4f43aba71d4e4953e9d7  common/scripted_triggers/MKN_diplomacy_triggers.txt
d7eae994496d635b4ffc9f48cbeca82d1f114ae0b9cb7fb29d1af9028c413b5b  common/scripted_triggers/MKN_horizons_triggers.txt
c26e01cf28cd943d6bb9209acecb06dc69487e17ae7ce69370156f0db44052a4  common/scripted_triggers/MKN_ukr_border_triggers.txt
21176c3f503751b9a05033d0287d8d530bd56ef939125904bc3e792e7e6601d8  common/scripted_triggers/MKN_ukraine_integration_triggers.txt
9b7ed0adb7a6d34d7747e197d7a6348d5c646a9e7c30642555e012157e10414d  events/MKN_events.txt
7d6be8d42387198ac5ad27a2b7cc5f747a1cf0779d397751ad39ba11c2bfd816  events/MKN_foreign_events.txt
9441962374174649d0477671f323fdea0e4b303d50e8e4a79a821eddbdc5c8cc  events/MKN_horizons_events.txt
1d8cf5098f9dc9d411136fb24fca50cdaacb05bf314e936153f48501221f322e  events/MKN_news_events.txt
7ae0632a44ff7ab6f0298f7ebc32a1565baf632999598c3b058e2d64eb2042e7  events/MKN_ukr_border_events.txt
8893e818324096deba4aee35b50849c7086905756418f7da44c217ba2afae4ce  events/MKN_ukraine_integration_events.txt
8fa94528ca3ff6f4f18b44c6fa23ac940a33c7d7995836d658e923d37e9a3a84  events/nww_mkn.txt
b5c2cf38406ee26a8ed66ffdb00c6040173213661a819df33c938f40676a78b8  history/countries/MKN - Makhnovists.txt
a7bda3d97130a5cc8b63ec056d8bb0684a3f00ea2dd34f094b699953b98ef968  localisation/MKN_economic_l_english.yml
b3d8dad65c6b0e8fc9f8b98f188239443442e89dcdd41615b1c4009161f76d6a  localisation/MKN_economic_l_russian.yml
64f377d8e10711f10391520bbc2c18d1f42c04d9ae435da573e6965b715960f9  localisation/MKN_ukraine_integration_l_english.yml
d6047724edbd2564503af21352ec97cf1a6d6dfd3cb68f5f92ef1bc8a6f100ee  localisation/MKN_ukraine_integration_l_russian.yml
58b0549c4a5585e0a81e9e51b4c2b752f547b87e695eec06e0751ffc77afd2d0  localisation/english/MKN_bop_l_english.yml
e120d4b627a8155563f670904d42200dbf23fece8f0dfe2436fa28c1eda40e48  localisation/english/MKN_flags_l_english.yml
28407387457a3ef6ba18274b323085029bcc5f65ccc8932f7611dcd14f6b9fb6  localisation/english/MKN_focus_l_english.yml
1508b5c234a64f71bd346c17d785164c09916ad57276bc480a6d1e5345999520  localisation/english/MKN_foreign_l_english.yml
364f90f511b2b7f37e5eba9476357d366234596c08de424483ab453aca408cb6  localisation/english/MKN_frontier_l_english.yml
985e3150a6471d26e2f6a6db256c61fa07cb8aedf74f816de78acaebf7136678  localisation/english/MKN_horizons_l_english.yml
d132a9de94be4094ff7ada71e98f1477acb5053f8c5c7139253878f635318f38  localisation/english/MKN_international_l_english.yml
1b28d2ded81af430f21211499ed6ff51a7fc9c6d84d53a3aaa19a9b8af6804d1  localisation/english/MKN_l_english.yml
58d5167b5d3202d2f3294f47f064b4a972c118e6f8427e6375c72e334a54accc  localisation/english/MKN_military_l_english.yml
a262bf322ffe339f4832053404bc8acaef192bfbc7e42bf9bd09f27973d4aeec  localisation/english/MKN_overhaul_l_english.yml
769b325ff62e2a46191dfb0350f30dd9ac8aea18cd6a666363478a9ba1f9de69  localisation/english/MKN_parties_l_english.yml
89fad478ca6237bb406c8ae580b755d900de82f1a93eb30d811c6bf7219e3f55  localisation/english/MKN_personnel_l_english.yml
e0c605abde2619ef5b17054e724352cbb8a21fa85a7ff9f7914902ca0c99b1d8  localisation/english/MKN_tree_consolidation_l_english.yml
836619e11268066723b123ca7d75a78edb836c0404e1da156079cb566160374b  localisation/mod_focus_l_english.yml
c900e99e0e5aa12a2a26affe735af52610677f543cfee120ec10a89629fa242f  localisation/mod_focus_l_russian.yml
2f4cf319b759c1b96495c9eed4e127c1a01dece861571ee99ad3c820a89a8544  localisation/nww_MKN_expansion_l_english.yml
02c6aa2b16a72e8380381034fc6e162d62aff3c18aec72544cd78bd6df710a13  localisation/nww_MKN_expansion_l_russian.yml
914bc98236aac458b6bd8c86a65ddd904e0ffd6238001091dca4e67919753161  localisation/nww_MKN_l_english.yml
e6d488b868e13dc5f36d83aebc7e839b99a52301162f24276ce897004abcbdcc  localisation/nww_MKN_l_russian.yml
ac8a8a1be33943edbcc7c3fbbe987bcd5b336f3a9563b0332f4c1d23d5eddcc1  localisation/nww_country_expansion_l_english.yml
76bec50391d55afb0ca9f201d6f22768bf7d426bfe47e0c125a822a6b1c4705f  localisation/nww_country_expansion_l_russian.yml
cf3a4bd9aba43bb684c0097f4ecff4a1506222de523323ef6859408a6f7d9ef8  localisation/russian/MKN_bop_l_russian.yml
279bb9d9be668925fd01773d7be9506eee21a3d51ce841d757b546ff3bd86e35  localisation/russian/MKN_flags_l_russian.yml
cd0edacae9f202e1d0d7aa0bcc2b43a29320a0163f70fb720fe5fd8d7f24cc27  localisation/russian/MKN_focus_l_russian.yml
79a3deff54f5207742c20a65c8b047138abb26dc1d7169d9658d9e96fb56d2e7  localisation/russian/MKN_foreign_l_russian.yml
b2ec8a0cc8c934909fc6fddb3e131525cc56631624f64e6a0597a4fc92b15aeb  localisation/russian/MKN_frontier_l_russian.yml
ec5199f08870091e677918a6cfe883e5aabc6ff725ae360e6b480be6489dd2ba  localisation/russian/MKN_horizons_l_russian.yml
a43bdd62180b58db665e13f314a0262c6e4e7d25663f4ba8a4c6d02e724710f3  localisation/russian/MKN_international_l_russian.yml
d9218c913a924f879c37305761f96f1372f37812d495651e09234530dad33565  localisation/russian/MKN_l_russian.yml
f30493700fde2edb3f867ddda443110ecf3e5b130eea5b51162e4068b1d3dc08  localisation/russian/MKN_military_l_russian.yml
aaedfd0b843be97290880116deaaed60f79b03545aee9bb40a7287262eb4cc99  localisation/russian/MKN_overhaul_l_russian.yml
779612fe406278c6c7bb4ca20bd002d762f7de903309ef7672e7b962a552bdc3  localisation/russian/MKN_parties_l_russian.yml
214fc275a33104ad82fb40343d6dcd4c21d3ea8e0621e47c2df4e6510b3e06bc  localisation/russian/MKN_personnel_l_russian.yml
1f27eb12f3151934033d913762ca84d3affe8ed3f81a50d3b19ccc9ebef43104  localisation/russian/MKN_tree_consolidation_l_russian.yml
6a1698fca9a56fd34464a36b4a309ed1595e09290dfe0638623a7bb592b4f3aa  tools/export_mkn_industrial_focuses.py
0de71609f35dfe1aafde5d1343d798e18f8641c5f84a0f2c5d7626156d9cc582  tools/export_mkn_political_focuses.py
05a0b3facf4d97366afef978722e4e2e1dbb6b7d39bbdbc3c3458d1bd47ecc61  tools/hoi4_script.py
```
