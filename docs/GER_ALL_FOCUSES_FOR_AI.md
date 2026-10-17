# Германия (GER): все фокусы NWW Reborn — пакет для другой нейросети

Дата снимка: **2026-10-17**. Источник — текущие игровые скрипты проекта. Самодостаточный файл содержит названия и описания RU/EN, награды, условия, зависимости, взаимоисключения, события, решения, духи, BoP и восстановление сохранений. Игровые файлы при экспорте не меняются.

Количество фокусов в игровом дереве `GER_focus`: **76** — 40 политических, 31 промышленных/научных/разведывательных и 5 прочих военных/государственных. Число direct-focus: 36; импортированных shared-focus: 40.

## Контекст и правила для улучшения

- Первая мировая война не происходила. Германия 1936 года — старая имперская гегемония с внутренним застоем и внешними обязательствами. Не возвращать ванильную историю послевоенной Германии.
- Сохранять существующие focus/event IDs, компромисс LTB и его преемников. GER_1–GER_10 — действующие импортированные фокусы, включённые в каталог, а не удалённые заглушки.
- cost — недели: 5 = 35 дней, 10 = 70 дней; cost=0 у событийного узла не означает свободный обычный фокус. available/bypass и событие определяют его выполнение.
- prerequisite: разные блоки соединяются И; несколько focus внутри одного блока — ИЛИ. available добавляет ограничения; mutually_exclusive исключает альтернативу. Полные allow_branch, bypass и AI-поля сохранены ниже.
- До 1 января 1939 года сохранять универсальные восточные ограничения против LTB, POL, UKR, MKN и SOV, включая события, решения и объявления войны. Исторические AI-ограничения могут быть строже общих; проверять оба уровня.
- Исторические даты из старых заметок — расчётные ориентиры, не наблюдение игры. Текущие условия и планы AI ниже являются источником для анализа.
- Кайзерский австрийский ультиматум имеет отдельный нижний временной порог. Не считать отсутствие восточного тега разрешением игнорировать австрийские условия.
- Германия не должна начинать с Осью. Не активировать MEFO, conquest-economy debt, продление векселей и штрафы погашения. Старые сохранения имеют защищённую очистку.
- Промышленность развивает один постоянный динамический дух GER_nww_industrial_program. Повторный пересчёт параметров не должен повторять фабрики, ресурсы, технику и слоты исследований.
- Параметры приведены в сырых единицах движка: factor=0.05 обычно означает 5 процентных пунктов; political_power_gain — плоский прирост в сутки. Не переводить все числа автоматически в проценты.
- if/limit/else, DLC, контроль/владение, субъектность и согласие получателя ограничивают выдачу. Не суммировать альтернативные награды как гарантированные. custom_effect_tooltip и show_mio_tooltip сами не выдают награду.
- Колониальные награды требуют фактического владения/контроля. Сохранять 19 заморских регионов из GER_overseas_setup.json и местные ядра; не выдавать германские колониальные ядра.
- Родные ванильные заглушки совместимости не импортированы и не входят в число игровых фокусов. Контент для Германии принадлежит GER; двусторонние богемские определения имеют документированного владельца GER.
- Это статический снимок. Проверки синтаксиса не заменяют новую кампанию, фактические tooltips и свежий лог игры.

## Сводный список

| Раздел | Название | ID | Дней |
| --- | --- | --- | --- |
| Общее политическое начало | Позолоченный колосс | `GER_the_gilded_colossus` | 35 |
| Общее политическое начало | Финансировать рейхсвер | `GER_fund_the_reichswehr` | 35 |
| Общее политическое начало | Расширить полномочия канцлера | `GER_empower_the_chancellor` | 35 |
| Общее политическое начало | Пангерманские союзы | `GER_pan_german_leagues` | 35 |
| Общее политическое начало | Организовать рабочих Рура | `GER_organize_ruhr_workers` | 35 |
| Общее политическое начало | Конец эпохи | `GER_end_of_an_era` | 0 |
| Авторитарный путь / Железный кайзеррейх | Потсдамский переворот | `GER_the_potsdam_coup` | 70 |
| Авторитарный путь / Железный кайзеррейх | Распустить рейхстаг | `GER_dissolve_the_reichstag` | 70 |
| Авторитарный путь / Железный кайзеррейх | Обуздать Миттельевропу | `GER_reign_in_mitteleuropa` | 70 |
| Авторитарный путь / Железный кайзеррейх | Австрийский вопрос | `GER_the_austrian_question` | 70 |
| Авторитарный путь / Железный кайзеррейх | Разгромить восточные синдикаты | `GER_crush_eastern_syndicates` | 70 |
| Авторитарный путь / Железный кайзеррейх | С нами Бог | `GER_gott_mit_uns` | 70 |
| Авторитарный путь / Железный кайзеррейх | План Шлиффена 2.0 | `GER_schlieffen_reborn` | 70 |
| Авторитарный путь / Железный кайзеррейх | Удар на Запад | `GER_strike_the_west` | 70 |
| Авторитарный путь / Железный кайзеррейх | Вторая морская гонка | `GER_the_second_naval_race` | 70 |
| Демократический путь / Парламентская весна | Парламентская весна | `GER_parliamentary_spring` | 70 |
| Демократический путь / Парламентская весна | Подлинная конституционная монархия | `GER_true_constitutional_monarchy` | 70 |
| Демократический путь / Парламентская весна | Экономическое сообщество Миттельевропы | `GER_mitteleuropa_economic_community` | 70 |
| Демократический путь / Парламентская весна | Австрийский референдум | `GER_the_austrian_referendum` | 70 |
| Демократический путь / Парламентская весна | Арсенал демократии | `GER_arsenal_of_democracy` | 70 |
| Демократический путь / Парламентская весна | Европейская федерация | `GER_european_federation` | 70 |
| Демократический путь / Парламентская весна | Поход против империализма | `GER_anti_imperialist_crusade` | 70 |
| Демократический путь / Парламентская весна | Щит против красных | `GER_shield_against_the_reds` | 70 |
| Пангерманский путь | Пангерманский триумф | `GER_the_pan_germanic_triumph` | 70 |
| Пангерманский путь | Упразднить власть Гогенцоллернов | `GER_abolish_the_hohenzollerns` | 70 |
| Пангерманский путь | Аншлюс силой | `GER_anschluss_by_force` | 70 |
| Пангерманский путь | Экспансия на Восток | `GER_lebensraum_in_the_east` | 70 |
| Пангерманский путь | Новый рейх | `GER_the_new_reich` | 70 |
| Пангерманский путь | Расширить натиск на Восток | `GER_drang_nach_osten_expanded` | 70 |
| Пангерманский путь | Тотальная ассимиляция | `GER_total_assimilation` | 70 |
| Пангерманский путь | Гегемония над Европой | `GER_hegemony_over_europe_focus` | 70 |
| Спартакистский путь | Спартакистское восстание | `GER_the_spartacist_uprising` | 70 |
| Спартакистский путь | Германская советская республика | `GER_german_soviet_republic` | 70 |
| Спартакистский путь | Рабочие ополчения | `GER_workers_militias` | 70 |
| Спартакистский путь | Демонтировать имперские границы | `GER_dismantle_imperial_borders` | 70 |
| Спартакистский путь | Ось Берлин — Москва | `GER_berlin_moscow_axis` | 70 |
| Спартакистский путь | Мировая революция | `GER_world_revolution` | 70 |
| Спартакистский путь | Красный Рейн | `GER_red_rhine` | 70 |
| Спартакистский путь | Массовая мобилизация ННА | `GER_nva_mass_mobilization` | 70 |
| Спартакистский путь | Бросить вызов Москве | `GER_challenge_moscow` | 70 |
| Промышленность, наука, торговля и разведка | Имперский промышленный совет | `GER_krupp_and_thyssen` | 70 |
| Промышленность, наука, торговля и разведка | Модернизировать Рурский бассейн | `GER_1` | 70 |
| Промышленность, наука, торговля и разведка | Рейнские инвестиционные банки | `GER_5` | 70 |
| Промышленность, наука, торговля и разведка | Торговые палаты Миттельевропы | `GER_mitteleuropa_trade` | 70 |
| Промышленность, наука, торговля и разведка | Соединить региональные энергосистемы | `GER_nww_electrical_grid` | 70 |
| Промышленность, наука, торговля и разведка | Промышленные облигации земель | `GER_6` | 70 |
| Промышленность, наука, торговля и разведка | Жильё для промышленных рабочих | `GER_nww_worker_housing` | 70 |
| Промышленность, наука, торговля и разведка | Концессии заморских предприятий | `GER_2` | 70 |
| Промышленность, наука, торговля и разведка | Связи с богемскими автономистами | `GER_nww_prague_network` | 35 |
| Промышленность, наука, торговля и разведка | Энергетическая инфраструктура Рура | `GER_nww_energy_keystones` | 70 |
| Промышленность, наука, торговля и разведка | Силезская металлургия | `GER_nww_silesian_steel` | 70 |
| Промышленность, наука, торговля и разведка | Культура точного производства | `GER_7` | 70 |
| Промышленность, наука, торговля и разведка | Грузовые коридоры империи | `GER_nww_freight_corridors` | 70 |
| Промышленность, наука, торговля и разведка | Восточные промышленные заказы | `GER_3` | 70 |
| Промышленность, наука, торговля и разведка | Станкостроительная кооперация | `GER_nww_machine_tools` | 70 |
| Промышленность, наука, торговля и разведка | Контракты торгового флота | `GER_nww_merchant_contracts` | 70 |
| Промышленность, наука, торговля и разведка | Долгосрочные контракты арсеналов | `GER_nww_arsenal_contracts` | 70 |
| Промышленность, наука, торговля и разведка | Общегерманские технические нормы | `GER_nww_industrial_standards` | 70 |
| Промышленность, наука, торговля и разведка | Электромеханические лаборатории | `GER_nww_electromechanical_labs` | 70 |
| Промышленность, наука, торговля и разведка | Экспортное кредитование | `GER_nww_export_credit` | 70 |
| Промышленность, наука, торговля и разведка | Единые стандарты вооружения | `GER_4` | 70 |
| Промышленность, наука, торговля и разведка | Технические училища земель | `GER_nww_technical_colleges` | 70 |
| Промышленность, наука, торговля и разведка | Гарантии долгосрочных вложений | `GER_nww_investment_guarantees` | 70 |
| Промышленность, наука, торговля и разведка | Согласовать промышленную программу | `GER_8` | 70 |
| Промышленность, наука, торговля и разведка | Синтетическое топливо из угля | `GER_nww_synthetic_fuels` | 70 |
| Промышленность, наука, торговля и разведка | Арсеналы нового поколения | `GER_9` | 70 |
| Промышленность, наука, торговля и разведка | Автоматизация оружейных линий | `GER_10` | 70 |
| Промышленность, наука, торговля и разведка | Складские узлы заморских портов | `GER_nww_colonial_ports` | 70 |
| Промышленность, наука, торговля и разведка | Имперское исследовательское объединение | `GER_nww_industrial_research` | 70 |
| Промышленность, наука, торговля и разведка | Устойчивые цепочки поставок | `GER_nww_supply_resilience` | 70 |
| Промышленность, наука, торговля и разведка | Сбалансированная система заказов | `GER_nww_balanced_orders` | 70 |
| Прочие военные и государственные фокусы | GER_the_kaiser_endures | `GER_the_kaiser_endures` | 35 |
| Прочие военные и государственные фокусы | GER_the_fleet_question | `GER_the_fleet_question` | 35 |
| Прочие военные и государственные фокусы | GER_prussian_traditions | `GER_prussian_traditions` | 35 |
| Прочие военные и государственные фокусы | GER_guardians_of_the_reich | `GER_guardians_of_the_reich` | 35 |
| Прочие военные и государственные фокусы | GER_the_eastern_question | `GER_the_eastern_question` | 70 |

## Общее политическое начало — 6

### Позолоченный колосс — `GER_the_gilded_colossus`

EN: The Gilded Colossus.

Описание RU: Империя распоряжается рынками и колониями по всему миру, но её учреждения закоснели, а обязательства превышают возможности. Короне предстоит решить, как управлять этой неповоротливой гегемонией.

Описание EN: The empire commands markets and colonies across the world, yet its institutions have grown rigid and its commitments exceed its means. The crown must decide how this unwieldy hegemony will be governed.

Источник: `common/national_focus/GER_political.txt:2`. Стоимость: 5 (35 дней). Координаты: x=18, y=0. Иконка: `GFX_focus_GER_our_place_in_the_sun`.

Предпосылки: нет нарисованной предпосылки; см. available.

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: GER_fund_the_reichswehr, GER_empower_the_chancellor, GER_end_of_an_era, GER_pan_german_leagues, GER_organize_ruhr_workers.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- `add_political_power`: 75

Полное определение фокуса:

```pdx
focus = {
    id = GER_the_gilded_colossus
    icon = GFX_focus_GER_our_place_in_the_sun
    cost = 5
    completion_reward = {
        add_political_power = 75
    }
    ai_will_do = {
        factor = 10
    }
    x = 18
    y = 0
}
```

### Финансировать рейхсвер — `GER_fund_the_reichswehr`

EN: Fund the Reichswehr.

Описание RU: Предоставим имперской армии требуемые средства и доступ к власти. Генеральный штаб усилит влияние за счёт парламентского контроля. Начать реформу штабов и заменить имперское перенапряжение облегчённой версией без штрафа к организации.

Описание EN: Give the imperial army the funds and access it demands. The General Staff gains influence at the expense of parliamentary oversight. Begin staff reform and replace Imperial Overstretch with its reduced version, removing the organisation penalty.

Источник: `common/national_focus/GER_political.txt:15`. Стоимость: 5 (35 дней). Координаты: x=10, y=1. Иконка: `GFX_focus_GER_prussian_legacy`.

Предпосылки: (Позолоченный колосс [GER_the_gilded_colossus]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: нет.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- `army_experience`: 15
- `add_power_balance_value`: id = GER_kaiser_vs_reichstag; value = -0.20; tooltip_side = GER_ohl_and_crown_side

Полное определение фокуса:

```pdx
focus = {
    id = GER_fund_the_reichswehr
    icon = GFX_focus_GER_prussian_legacy
    cost = 5
    prerequisite = {
        focus = GER_the_gilded_colossus
    }
    available = {
        NOT = {
            has_country_flag = ger_bop_frozen
        }
    }
    completion_reward = {
        GER_nww_partial_army_reform = yes
        army_experience = 15
        if = {
            limit = {
                NOT = {
                    has_country_flag = ger_bop_frozen
                }
            }
            add_power_balance_value = {
                id = GER_kaiser_vs_reichstag
                value = -0.20
                tooltip_side = GER_ohl_and_crown_side
            }
        }
    }
    ai_will_do = {
        factor = 10
    }
    x = 10
    y = 1
}
```

### Расширить полномочия канцлера — `GER_empower_the_chancellor`

EN: Empower the Chancellor.

Описание RU: Канцлер должен согласовывать бюджет с рейхстагом, а не подчиняться двору и Генеральному штабу. Гражданские учреждения получат более весомый голос.

Описание EN: The chancellor must negotiate budgets through the Reichstag rather than defer to the court and General Staff. Civilian institutions gain a stronger voice.

Источник: `common/national_focus/GER_political.txt:49`. Стоимость: 5 (35 дней). Координаты: x=14, y=1. Иконка: `GFX_focus_GER_monarchy_compromise`.

Предпосылки: (Позолоченный колосс [GER_the_gilded_colossus]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: нет.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- `add_political_power`: 50
- `add_power_balance_value`: id = GER_kaiser_vs_reichstag; value = 0.20; tooltip_side = GER_reichstag_side

Полное определение фокуса:

```pdx
focus = {
    id = GER_empower_the_chancellor
    icon = GFX_focus_GER_monarchy_compromise
    cost = 5
    prerequisite = {
        focus = GER_the_gilded_colossus
    }
    available = {
        NOT = {
            has_country_flag = ger_bop_frozen
        }
    }
    completion_reward = {
        add_political_power = 50
        if = {
            limit = {
                NOT = {
                    has_country_flag = ger_bop_frozen
                }
            }
            add_power_balance_value = {
                id = GER_kaiser_vs_reichstag
                value = 0.20
                tooltip_side = GER_reichstag_side
            }
        }
    }
    ai_will_do = {
        factor = 1
        modifier = {
            factor = 0
            is_historical_focus_on = yes
        }
    }
    x = 14
    y = 1
}
```

### Пангерманские союзы — `GER_pan_german_leagues`

EN: The Pan-German Leagues.

Описание RU: Объединим националистические общества в организованное движение. Их митинги позволят собрать необходимые 40% поддержки для выхода из парламентского тупика.

Описание EN: Organise nationalist associations into a coherent political movement. Their rallies can build the 40% mandate needed to break a parliamentary deadlock.

Источник: `common/national_focus/GER_political.txt:325`. Стоимость: 5 (35 дней). Координаты: x=22, y=1. Иконка: `GFX_focus_GER_brothers_in_arms`.

Предпосылки: (Позолоченный колосс [GER_the_gilded_colossus]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: нет.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- Награда вызывает вспомогательные эффекты: см. completion_reward и раздел определений.

Полное определение фокуса:

```pdx
focus = {
    id = GER_pan_german_leagues
    icon = GFX_focus_GER_brothers_in_arms
    x = 22
    y = 1
    cost = 5
    prerequisite = {
        focus = GER_the_gilded_colossus
    }
    available = {
        nww_GER_no_political_path = yes
    }
    completion_reward = {
        add_popularity = {
            ideology = fascism
            popularity = 0.10
        }
    }
    ai_will_do = {
        factor = 1
        modifier = {
            factor = 0
            is_historical_focus_on = yes
        }
    }
}
```

### Организовать рабочих Рура — `GER_organize_ruhr_workers`

EN: Organise the Ruhr Workers.

Описание RU: Восстановим рабочие советы и подготовим спартакистский вызов имперскому порядку. Через советы можно нарастить поддержку будущего восстания.

Описание EN: Rebuild the workers councils and prepare a Spartacist challenge to the imperial order. Councils can raise support for the coming uprising.

Источник: `common/national_focus/GER_political.txt:351`. Стоимость: 5 (35 дней). Координаты: x=26, y=1. Иконка: `GFX_focus_GER_legacy_of_the_spartacus_league`.

Предпосылки: (Позолоченный колосс [GER_the_gilded_colossus]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: нет.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- Награда вызывает вспомогательные эффекты: см. completion_reward и раздел определений.

Полное определение фокуса:

```pdx
focus = {
    id = GER_organize_ruhr_workers
    icon = GFX_focus_GER_legacy_of_the_spartacus_league
    x = 26
    y = 1
    cost = 5
    prerequisite = {
        focus = GER_the_gilded_colossus
    }
    available = {
        nww_GER_no_political_path = yes
    }
    completion_reward = {
        add_popularity = {
            ideology = communism
            popularity = 0.10
        }
    }
    ai_will_do = {
        factor = 1
        modifier = {
            factor = 0
            is_historical_focus_on = yes
        }
    }
}
```

### Конец эпохи — `GER_end_of_an_era`

EN: End of an Era.

Описание RU: Вильгельм II олицетворял империю, не знавшую мировой войны. Его смерть положит конец долгому политическому застою и откроет борьбу за наследство. Фокус завершается только событием престолонаследия между августом и концом 1936 года.

Описание EN: Wilhelm II personified an empire that never faced a world war. His death will end its long political suspension and open the struggle over the succession. This focus is completed only by the succession event, between August and the end of 1936.

Источник: `common/national_focus/GER_political.txt:86`. Стоимость: 0 (0 дней). Координаты: x=18, y=3. Иконка: `GFX_focus_GER_tend_to_the_future`.

Предпосылки: (Позолоченный колосс [GER_the_gilded_colossus]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: GER_the_potsdam_coup, GER_parliamentary_spring, GER_the_pan_germanic_triumph, GER_the_spartacist_uprising.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- Награда вызывает вспомогательные эффекты: см. completion_reward и раздел определений.

Полное определение фокуса:

```pdx
focus = {
    id = GER_end_of_an_era
    icon = GFX_focus_GER_tend_to_the_future
    cost = 0
    prerequisite = {
        focus = GER_the_gilded_colossus
    }
    available = {
        always = no
    }
    completion_reward = {

    }
    ai_will_do = {
        factor = 0
    }
    x = 18
    y = 3
}
```

## Авторитарный путь / Железный кайзеррейх — 9

### Потсдамский переворот — `GER_the_potsdam_coup`

EN: The Potsdam Coup.

Описание RU: Опираясь на Генеральный штаб, Вильгельм III сосредоточит в своих руках власть, ослабевшую при его отце. Необходимы предварительная поддержка армии, смещение баланса более чем на 10% влево от центра и не менее 40% поддержки монархистов.

Описание EN: With the General Staff behind him, Wilhelm III will seize the powers his father allowed to decay. The army must already have received our backing; military influence must exceed 10% to the left of centre, and the monarchists need at least 40% support.

Источник: `common/national_focus/GER_political.txt:105`. Стоимость: 10 (70 дней). Координаты: x=6, y=4. Иконка: `GFX_focus_GER_glory_to_the_imperial_army`.

Предпосылки: (Конец эпохи [GER_end_of_an_era]).

Взаимоисключения: GER_parliamentary_spring, GER_the_pan_germanic_triumph, GER_the_spartacist_uprising.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): GER_fund_the_reichswehr, GER_the_gilded_colossus.

Прямые продолжения: GER_dissolve_the_reichstag.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- `set_politics`: ruling_party = neutrality; elections_allowed = no; election_frequency = 48
- `set_country_flag`: ger_iron_kaiserreich
- `add_stability`: -0.10
- `add_war_support`: 0.20

Полное определение фокуса:

```pdx
focus = {
    id = GER_the_potsdam_coup
    icon = GFX_focus_GER_glory_to_the_imperial_army
    cost = 10
    prerequisite = {
        focus = GER_end_of_an_era
    }
    available = {
        has_completed_focus = GER_the_gilded_colossus
        has_completed_focus = GER_fund_the_reichswehr
        has_country_flag = ger_wilhelm_ii_dead
        NOT = {
            neutrality < 0.40
        }
        power_balance_value = {
            id = GER_kaiser_vs_reichstag
            value < -0.10
        }
        nww_GER_no_political_path = yes
        NOT = {
            has_civil_war = yes
        }
    }
    completion_reward = {
        set_politics = {
            ruling_party = neutrality
            elections_allowed = no
            election_frequency = 48
        }
        GER_wilhelm_iii = {
            promote_character = yes
        }
        set_country_flag = ger_iron_kaiserreich
        add_stability = -0.10
        add_war_support = 0.20
    }
    ai_will_do = {
        factor = 10
    }
    x = 6
    y = 4
    mutually_exclusive = {
        focus = GER_parliamentary_spring
        focus = GER_the_pan_germanic_triumph
        focus = GER_the_spartacist_uprising
    }
}
```

### Распустить рейхстаг — `GER_dissolve_the_reichstag`

EN: Dissolve the Reichstag.

Описание RU: Парламент больше не будет препятствовать императорским указам. Корона и Верховное командование получают всю полноту власти; баланс сил закрепляется, а демократические политические советники лишаются должностей и доступа к ним.

Описание EN: Parliament will no longer obstruct imperial commands. The crown and OHL take complete control, the balance of power is locked, and democratic political advisors lose their posts and eligibility.

Источник: `common/national_focus/GER_political.txt:152`. Стоимость: 10 (70 дней). Координаты: x=6, y=5. Иконка: `GFX_focus_GER_realpolitik`.

Предпосылки: (Потсдамский переворот [GER_the_potsdam_coup]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: GER_reign_in_mitteleuropa, GER_the_austrian_question.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- `set_country_flag`: ger_bop_frozen

Полное определение фокуса:

```pdx
focus = {
    id = GER_dissolve_the_reichstag
    icon = GFX_focus_GER_realpolitik
    cost = 10
    prerequisite = {
        focus = GER_the_potsdam_coup
    }
    available = {
        has_government = neutrality
    }
    completion_reward = {
        set_country_flag = ger_bop_frozen
        set_power_balance = {
            id = GER_kaiser_vs_reichstag
            set_value = -1
        }
        custom_effect_tooltip = GER_bop_frozen_tt
        remove_advisor_role = {
            character = GER_julius_leber
            slot = political_advisor
        }
        remove_advisor_role = {
            character = GER_kurt_schumacher
            slot = political_advisor
        }
        remove_advisor_role = {
            character = GER_theodor_heuss
            slot = political_advisor
        }
    }
    ai_will_do = {
        factor = 10
    }
    x = 6
    y = 5
}
```

### Обуздать Миттельевропу — `GER_reign_in_mitteleuropa`

EN: Rein in Mitteleuropa.

Описание RU: Потребуем полного подчинения Литвы-Беларуси и Польши. Наши зависимые страны станут интегрированными марионетками, если система автономии это допускает; независимые правительства могут принять статус марионетки или отказаться. Германия не сможет начать войну с ЛитБелом до 1939 года.\n\n$GER_eastern_1939_gate_tt$

Описание EN: Demand binding subordination from Lithuania-Belarus and Poland. Our existing subjects become integrated puppets where the autonomy system permits; independent governments may accept puppet status or refuse. No German war against Lithuania-Belarus may begin before 1939.\n\n$GER_eastern_1939_gate_tt$

Источник: `common/national_focus/GER_political.txt:188`. Стоимость: 10 (70 дней). Координаты: x=4, y=6. Иконка: `GFX_focus_GER_extend_mitteleuropa`.

Предпосылки: (Распустить рейхстаг [GER_dissolve_the_reichstag]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: GER_crush_eastern_syndicates.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- Награда вызывает вспомогательные эффекты: см. completion_reward и раздел определений.

Полное определение фокуса:

```pdx
focus = {
    id = GER_reign_in_mitteleuropa
    icon = GFX_focus_GER_extend_mitteleuropa
    cost = 10
    prerequisite = {
        focus = GER_dissolve_the_reichstag
    }
    available = {
        custom_trigger_tooltip = {
            tooltip = GER_nww_historical_pressure_ready
            GER_nww_historical_pressure_ready = yes
        }
        has_government = neutrality
        is_subject = no
        date > 1938.12.31
        custom_trigger_tooltip = {
            tooltip = GER_eastern_1939_gate_tt
            date > 1938.12.31
        }
        nww_GER_ai_can_prepare_campaign = yes
    }
    completion_reward = {
        custom_effect_tooltip = GER_eastern_1939_gate_tt
        custom_effect_tooltip = GER_mitteleuropa_demand_tt
        hidden_effect = {
            LTB = {
                nww_GER_mitteleuropa_demand = yes
            }
            POL = {
                nww_GER_mitteleuropa_demand = yes
            }
        }
    }
    ai_will_do = {
        factor = 10
    }
    x = 4
    y = 6
}
```

### Австрийский вопрос — `GER_the_austrian_question`

EN: The Austrian Question.

Описание RU: Вена должна признать верховенство Берлина и принять статус марионетки. Австрия может отказаться; в этом случае мы получим цель войны для её подчинения.

Описание EN: Vienna must acknowledge the supremacy of Berlin and accept puppet status. Austria may refuse; such a refusal gives us a war goal to enforce its submission.

Источник: `common/national_focus/GER_political.txt:227`. Стоимость: 10 (70 дней). Координаты: x=8, y=6. Иконка: `GFX_focus_GER_the_austrian_question`.

Предпосылки: (Распустить рейхстаг [GER_dissolve_the_reichstag]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: GER_gott_mit_uns.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- Награда вызывает вспомогательные эффекты: см. completion_reward и раздел определений.

Полное определение фокуса:

```pdx
focus = {
    id = GER_the_austrian_question
    icon = GFX_focus_GER_the_austrian_question
    cost = 10
    prerequisite = {
        focus = GER_dissolve_the_reichstag
    }
    bypass = {
        OR = {
            AUS = {
                exists = no
            }
            AUS = {
                is_subject_of = GER
            }
        }
    }
    available = {
        date > 1938.12.31
        custom_trigger_tooltip = {
            tooltip = GER_nww_austrian_1939_tt
            date > 1938.12.31
        }
        has_government = neutrality
        is_subject = no
        AUS = {
            exists = yes
            is_subject = no
        }
        NOT = {
            has_war_with = AUS
        }
        nww_GER_ai_can_target_AUS = yes
    }
    completion_reward = {
        GER_nww_dispatch_austrian_demand = yes
    }
    ai_will_do = {
        factor = 5
    }
    x = 8
    y = 6
}
```

### Разгромить восточные синдикаты — `GER_crush_eastern_syndicates`

EN: Crush the Eastern Syndicates.

Описание RU: Подготовим уничтожение независимых синдикалистских центров на территории махновцев и Украины. Цели войны выдаются только против существующих независимых стран вне нашего союза.\n\n$GER_eastern_1939_gate_tt$

Описание EN: Prepare the destruction of the independent syndicalist centres in the Makhnovist territory and Ukraine. War goals are granted only against existing independent countries outside our alliance.\n\n$GER_eastern_1939_gate_tt$

Источник: `common/national_focus/GER_political.txt:270`. Стоимость: 10 (70 дней). Координаты: x=4, y=7. Иконка: `GFX_focus_GER_end_european_communism`.

Предпосылки: (Обуздать Миттельевропу [GER_reign_in_mitteleuropa]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: GER_gott_mit_uns.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- Награда вызывает вспомогательные эффекты: см. completion_reward и раздел определений.

Полное определение фокуса:

```pdx
focus = {
    id = GER_crush_eastern_syndicates
    icon = GFX_focus_GER_end_european_communism
    cost = 10
    prerequisite = {
        focus = GER_reign_in_mitteleuropa
    }
    available = {
        custom_trigger_tooltip = {
            tooltip = GER_nww_historical_eastern_war_ready
            GER_nww_historical_eastern_war_ready = yes
        }
        has_government = neutrality
        is_subject = no
        date > 1938.12.31
        custom_trigger_tooltip = {
            tooltip = GER_eastern_1939_gate_tt
            date > 1938.12.31
        }
        nww_GER_ai_can_prepare_campaign = yes
    }
    completion_reward = {
        custom_effect_tooltip = GER_eastern_1939_gate_tt
        nww_GER_eastern_wargoals = yes
    }
    ai_will_do = {
        factor = 5
    }
    x = 4
    y = 7
}
```

### С нами Бог — `GER_gott_mit_uns`

EN: Gott mit uns.

Описание RU: Железная империя объединяет корону, армию и нацию общей имперской целью. Дивизии получают +15% к защите на национальной территории, +10% к атаке и +10% к прорыву. Завершить военную и административную реформу, удалив обе версии имперского перенапряжения.

Описание EN: The Iron Kaiserreich binds crown, army and nation to a single imperial purpose. Its divisions gain 15% core defence, 10% attack and 10% breakthrough. Complete military and administrative reform, removing both versions of Imperial Overstretch.

Источник: `common/national_focus/GER_political.txt:301`. Стоимость: 10 (70 дней). Координаты: x=6, y=8. Иконка: `GFX_focus_GER_army`.

Предпосылки: (Разгромить восточные синдикаты [GER_crush_eastern_syndicates]) И (Австрийский вопрос [GER_the_austrian_question]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: GER_schlieffen_reborn.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- `remove_ideas`: GER_imperial_overstretch
- `remove_ideas`: GER_imperial_overstretch_2
- `add_ideas`: GER_gott_mit_uns

Полное определение фокуса:

```pdx
focus = {
    id = GER_gott_mit_uns
    icon = GFX_focus_GER_army
    cost = 10
    prerequisite = {
        focus = GER_crush_eastern_syndicates
    }
    prerequisite = {
        focus = GER_the_austrian_question
    }
    available = {
        has_government = neutrality
    }
    completion_reward = {
        remove_ideas = GER_imperial_overstretch
        remove_ideas = GER_imperial_overstretch_2
        add_ideas = GER_gott_mit_uns
    }
    ai_will_do = {
        factor = 10
    }
    x = 6
    y = 8
}
```

### План Шлиффена 2.0 — `GER_schlieffen_reborn`

EN: Schlieffen Reborn.

Описание RU: Современная штабная работа заменит планы прошлого столетия. С 1941 года мы сможем добиваться подчинения Нидерландов и Бельгии. Исторический ИИ сначала должен завершить польскую и австрийскую кампании.

Описание EN: Modern staff work replaces a plan inherited from the last century. From 1941 we can demand the subordination of the Netherlands and Belgium. The historical AI must first settle its Polish and Austrian campaigns.

Источник: `common/national_focus/GER_political.txt:999`. Стоимость: 10 (70 дней). Координаты: x=6, y=9. Иконка: `GFX_focus_GER_army`.

Предпосылки: (С нами Бог [GER_gott_mit_uns]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: GER_strike_the_west.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- `create_wargoal`: type = puppet_wargoal_focus; target = HOL
- `create_wargoal`: type = puppet_wargoal_focus; target = BEL

Полное определение фокуса:

```pdx
focus = {
    id = GER_schlieffen_reborn
    icon = GFX_focus_GER_army
    x = 6
    y = 9
    cost = 10
    prerequisite = {
        focus = GER_gott_mit_uns
    }
    available_if_capitulated = no
    available = {
        has_government = neutrality
        is_subject = no
        date > 1940.12.31
        OR = {
            is_ai = no
            GER_nww_eastern_campaigns_settled = yes
        }
    }
    completion_reward = {
        if = {
            limit = {
                HOL = {
                    exists = yes
                    is_subject = no
                }
                NOT = {
                    is_ally_with = HOL
                }
                NOT = {
                    has_war_with = HOL
                }
                NOT = {
                    has_wargoal_against = HOL
                }
            }
            create_wargoal = {
                type = puppet_wargoal_focus
                target = HOL
            }
        }
        if = {
            limit = {
                BEL = {
                    exists = yes
                    is_subject = no
                }
                NOT = {
                    is_ally_with = BEL
                }
                NOT = {
                    has_war_with = BEL
                }
                NOT = {
                    has_wargoal_against = BEL
                }
            }
            create_wargoal = {
                type = puppet_wargoal_focus
                target = BEL
            }
        }
    }
    ai_will_do = {
        factor = 10
    }
}
```

### Удар на Запад — `GER_strike_the_west`

EN: Strike the West.

Описание RU: Реформированная императорская армия готовит поход против Франции. Цель войны на полное завоевание создаёт дипломатическую основу, но победу ещё предстоит одержать на поле боя.

Описание EN: The reformed imperial army prepares a campaign against France. A conquest war goal supplies the diplomatic instrument; victory still has to be won on the battlefield.

Источник: `common/national_focus/GER_political.txt:1035`. Стоимость: 10 (70 дней). Координаты: x=6, y=10. Иконка: `GFX_focus_GER_hegemony_over_europe`.

Предпосылки: (План Шлиффена 2.0 [GER_schlieffen_reborn]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: GER_the_second_naval_race.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- `create_wargoal`: type = annex_everything; target = FRA

Полное определение фокуса:

```pdx
focus = {
    id = GER_strike_the_west
    icon = GFX_focus_GER_hegemony_over_europe
    x = 6
    y = 10
    cost = 10
    prerequisite = {
        focus = GER_schlieffen_reborn
    }
    available_if_capitulated = no
    available = {
        has_government = neutrality
        is_subject = no
    }
    completion_reward = {
        if = {
            limit = {
                FRA = {
                    exists = yes
                    is_subject = no
                }
                NOT = {
                    is_ally_with = FRA
                }
                NOT = {
                    has_war_with = FRA
                }
                NOT = {
                    has_wargoal_against = FRA
                }
            }
            create_wargoal = {
                type = annex_everything
                target = FRA
            }
        }
    }
    ai_will_do = {
        factor = 10
    }
}
```

### Вторая морская гонка — `GER_the_second_naval_race`

EN: The Second Naval Race.

Описание RU: Прежнее соперничество за океаны возобновляется. Скорость строительства верфей возрастёт на 15%, их производительность — на 10%. Две технологии крупных кораблей или их модулей получат бонус к исследованиям 100%. Цель войны на завоевание Британии завершит нашу западную стратегию.

Описание EN: An earlier rivalry for the oceans resumes. Shipyard construction rises by 15%, dockyard output by 10%, and two capital-ship or related module technologies receive a 100% research bonus. A conquest war goal against Britain completes our western strategy.

Источник: `common/national_focus/GER_political.txt:1060`. Стоимость: 10 (70 дней). Координаты: x=6, y=11. Иконка: `GFX_focus_GER_our_place_in_the_sun`.

Предпосылки: (Удар на Запад [GER_strike_the_west]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: нет.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- `add_tech_bonus`: name = GER_capital_ship_research; bonus = 1.0; uses = 2; category = mio_cat_tech_all_capital_ship_and_modules
- `create_wargoal`: type = annex_everything; target = ENG

Полное определение фокуса:

```pdx
focus = {
    id = GER_the_second_naval_race
    icon = GFX_focus_GER_our_place_in_the_sun
    x = 6
    y = 11
    cost = 10
    prerequisite = {
        focus = GER_strike_the_west
    }
    available_if_capitulated = no
    available = {
        has_government = neutrality
        is_subject = no
    }
    completion_reward = {
        swap_ideas = {
            remove_idea = GER_gott_mit_uns
            add_idea = GER_gott_mit_uns_naval
        }
        add_tech_bonus = {
            name = GER_capital_ship_research
            bonus = 1.0
            uses = 2
            category = mio_cat_tech_all_capital_ship_and_modules
        }
        if = {
            limit = {
                ENG = {
                    exists = yes
                    is_subject = no
                }
                NOT = {
                    is_ally_with = ENG
                }
                NOT = {
                    has_war_with = ENG
                }
                NOT = {
                    has_wargoal_against = ENG
                }
            }
            create_wargoal = {
                type = annex_everything
                target = ENG
            }
        }
    }
    ai_will_do = {
        factor = 10
    }
}
```

## Демократический путь / Парламентская весна — 8

### Парламентская весна — `GER_parliamentary_spring`

EN: Parliamentary Spring.

Описание RU: При поддержке демократов не менее 40%, усиленном канцлере и балансе правее +0,10 парламент возьмёт престолонаследие под контроль. Ганс Фогель сформирует социал-демократическое правительство; баланс закрепится за рейхстагом.

Описание EN: With at least 40% democratic support, a strengthened chancellor and the balance to the right of +0.10, parliament can take charge of the succession. Hans Vogel forms a social democratic government; the balance is permanently fixed at full Reichstag control.

Источник: `common/national_focus/GER_political.txt:377`. Стоимость: 10 (70 дней). Координаты: x=14, y=4. Иконка: `GFX_focus_GER_defender_of_democracy`.

Предпосылки: (Конец эпохи [GER_end_of_an_era]).

Взаимоисключения: GER_the_potsdam_coup, GER_the_pan_germanic_triumph, GER_the_spartacist_uprising.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): GER_empower_the_chancellor.

Прямые продолжения: GER_true_constitutional_monarchy.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- `set_country_flag`: ger_parliamentary_spring
- `set_country_flag`: ger_bop_frozen
- `set_politics`: ruling_party = democratic; elections_allowed = yes; election_frequency = 48

Полное определение фокуса:

```pdx
focus = {
    id = GER_parliamentary_spring
    icon = GFX_focus_GER_defender_of_democracy
    x = 14
    y = 4
    cost = 10
    prerequisite = {
        focus = GER_end_of_an_era
    }
    available = {
        nww_GER_no_political_path = yes
        has_completed_focus = GER_empower_the_chancellor
        has_country_flag = ger_wilhelm_ii_dead
        NOT = {
            democratic < 0.40
        }
        NOT = {
            has_civil_war = yes
        }
        power_balance_value = {
            id = GER_kaiser_vs_reichstag
            value > 0.10
        }
    }
    completion_reward = {
        set_country_flag = ger_parliamentary_spring
        set_country_flag = ger_bop_frozen
        set_politics = {
            ruling_party = democratic
            elections_allowed = yes
            election_frequency = 48
        }
        if = {
            limit = {
                NOT = {
                    has_character = GER_hans_vogel
                }
            }
            recruit_character = GER_hans_vogel
        }
        GER_hans_vogel = {
            set_portraits = {
                civilian = {
                    large = GFX_NWW_GER_hans_vogel
                }
            }
            add_country_leader_role = {
                country_leader = {
                    ideology = GER_social_democracy
                    expire = 1965.1.1
                    traits = {

                    }
                }
                promote_leader = yes
            }
        }
        set_power_balance = {
            id = GER_kaiser_vs_reichstag
            set_value = 1
        }
        custom_effect_tooltip = GER_reichstag_locked_tt
    }
    ai_will_do = {
        factor = 5
        modifier = {
            factor = 0
            is_historical_focus_on = yes
        }
    }
    mutually_exclusive = {
        focus = GER_the_potsdam_coup
        focus = GER_the_pan_germanic_triumph
        focus = GER_the_spartacist_uprising
    }
}
```

### Подлинная конституционная монархия — `GER_true_constitutional_monarchy`

EN: A True Constitutional Monarchy.

Описание RU: Вильгельм III сохраняет корону как конституционный символ, а исполнительная власть переходит избранным министрам. Парламентские институты дают +15% стабильности и +0,20 политической власти в день. Гражданский контроль запускает ту же реформу штабов, что и финансирование армии, снимая штраф к организации.

Описание EN: Wilhelm III retains the crown as a constitutional symbol while elected ministers exercise executive power. Parliamentary institutions grant +15% stability and +0.20 daily political power. Civilian oversight begins the same staff reform as army funding, removing the organisation penalty.

Источник: `common/national_focus/GER_political.txt:453`. Стоимость: 10 (70 дней). Координаты: x=14, y=5. Иконка: `GFX_focus_GER_monarchy_compromise`.

Предпосылки: (Парламентская весна [GER_parliamentary_spring]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: GER_mitteleuropa_economic_community, GER_the_austrian_referendum.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- `set_country_flag`: ger_constitutional_crown
- `add_ideas`: GER_constitutional_monarchy

Полное определение фокуса:

```pdx
focus = {
    id = GER_true_constitutional_monarchy
    icon = GFX_focus_GER_monarchy_compromise
    x = 14
    y = 5
    cost = 10
    prerequisite = {
        focus = GER_parliamentary_spring
    }
    available = {
        has_government = democratic
    }
    completion_reward = {
        GER_nww_partial_army_reform = yes
        remove_country_leader_role = {
            character = GER_wilhelm_iii
            ideology = GER_imperial_autocracy
        }
        set_country_flag = ger_constitutional_crown
        add_ideas = GER_constitutional_monarchy
    }
}
```

### Экономическое сообщество Миттельевропы — `GER_mitteleuropa_economic_community`

EN: Mitteleuropa Economic Community.

Описание RU: Предоставим независимость Литве-Беларуси и Польше, если они зависят от нас, и пригласим их в добровольный союз Миттельевропы. Согласие каждого партнёра даёт одну внемаповую гражданскую фабрику, всего не более двух. Отказ не даёт цели войны.

Описание EN: Free Lithuania-Belarus and Poland if they are our subjects, and invite them to the voluntary Mitteleuropa alliance. Each partner that accepts contributes one off-map civilian factory to economic integration, up to two in total. Refusal brings no war goal.

Источник: `common/national_focus/GER_political.txt:475`. Стоимость: 10 (70 дней). Координаты: x=12, y=6. Иконка: `GFX_focus_GER_customs_union`.

Предпосылки: (Подлинная конституционная монархия [GER_true_constitutional_monarchy]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: GER_arsenal_of_democracy.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- Награда вызывает вспомогательные эффекты: см. completion_reward и раздел определений.

Полное определение фокуса:

```pdx
focus = {
    id = GER_mitteleuropa_economic_community
    icon = GFX_focus_GER_customs_union
    x = 12
    y = 6
    cost = 10
    prerequisite = {
        focus = GER_true_constitutional_monarchy
    }
    available = {
        has_government = democratic
        is_subject = no
        OR = {
            is_in_faction = no
            is_faction_leader = yes
        }
        has_war = no
    }
    completion_reward = {
        nww_GER_establish_mitteleuropa = yes
        LTB = {
            nww_GER_democratic_community_offer = yes
        }
        POL = {
            nww_GER_democratic_community_offer = yes
        }
        custom_effect_tooltip = GER_economic_community_tt
    }
}
```

### Австрийский референдум — `GER_the_austrian_referendum`

EN: The Austrian Referendum.

Описание RU: Предложим Вене мирное объединение при демократическом правительстве или союз суверенных государств. Австрия самостоятельно принимает решение и должна находиться в мире; отказ не имеет военных последствий.

Описание EN: Offer Vienna peaceful unification if its government is democratic, or an alliance between sovereign states. Austria decides freely and must be at peace; refusing either arrangement has no military consequences.

Источник: `common/national_focus/GER_political.txt:504`. Стоимость: 10 (70 дней). Координаты: x=16, y=6. Иконка: `GFX_focus_GER_european_confederation`.

Предпосылки: (Подлинная конституционная монархия [GER_true_constitutional_monarchy]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: GER_arsenal_of_democracy.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- `country_event`: id = ger_crisis.30; days = 1

Полное определение фокуса:

```pdx
focus = {
    id = GER_the_austrian_referendum
    icon = GFX_focus_GER_european_confederation
    x = 16
    y = 6
    cost = 10
    prerequisite = {
        focus = GER_true_constitutional_monarchy
    }
    bypass = {
        OR = {
            AUS = {
                exists = no
            }
            AUS = {
                is_subject_of = ROOT
            }
        }
    }
    available = {
        has_government = democratic
        is_subject = no
        has_war = no
        AUS = {
            exists = yes
            is_subject = no
            has_war = no
        }
    }
    completion_reward = {
        if = {
            limit = {
                has_government = democratic
                is_subject = no
                has_war = no
                AUS = {
                    exists = yes
                    is_subject = no
                    has_war = no
                }
            }
            AUS = {
                country_event = {
                    id = ger_crisis.30
                    days = 1
                }
            }
        }
    }
}
```

### Арсенал демократии — `GER_arsenal_of_democracy`

EN: Arsenal of Democracy.

Описание RU: Укрепим конституционные институты оборонной промышленной программой: +20% выпуска фабрик и +10% защиты дивизий с сохранением бонусов стабильности и политической власти. Гарантируем независимость суверенных Литвы-Беларуси и Польши от внешней агрессии. Завершить военную и административную реформу, удалив обе версии имперского перенапряжения.

Описание EN: Strengthen our constitutional institutions with a defensive industrial programme: +20% factory output and +10% division defence, retaining their stability and political-power bonuses. Guarantee independent Lithuania-Belarus and Poland against foreign aggression. Complete military and administrative reform, removing both versions of Imperial Overstretch.

Источник: `common/national_focus/GER_political.txt:554`. Стоимость: 10 (70 дней). Координаты: x=14, y=7. Иконка: `GFX_focus_GER_integrated_economies`.

Предпосылки: (Экономическое сообщество Миттельевропы [GER_mitteleuropa_economic_community]) И (Австрийский референдум [GER_the_austrian_referendum]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: GER_european_federation.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- `remove_ideas`: GER_imperial_overstretch
- `remove_ideas`: GER_imperial_overstretch_2

Полное определение фокуса:

```pdx
focus = {
    id = GER_arsenal_of_democracy
    icon = GFX_focus_GER_integrated_economies
    x = 14
    y = 7
    cost = 10
    prerequisite = {
        focus = GER_mitteleuropa_economic_community
    }
    prerequisite = {
        focus = GER_the_austrian_referendum
    }
    available = {
        has_government = democratic
        is_subject = no
    }
    completion_reward = {
        remove_ideas = GER_imperial_overstretch
        remove_ideas = GER_imperial_overstretch_2
        swap_ideas = {
            remove_idea = GER_constitutional_monarchy
            add_idea = GER_arsenal_of_democracy
        }
        if = {
            limit = {
                LTB = {
                    exists = yes
                    is_subject = no
                }
                NOT = {
                    has_war_with = LTB
                }
            }
            give_guarantee = LTB
        }
        if = {
            limit = {
                POL = {
                    exists = yes
                    is_subject = no
                }
                NOT = {
                    has_war_with = POL
                }
            }
            give_guarantee = POL
        }
    }
}
```

### Европейская федерация — `GER_european_federation`

EN: European Federation.

Описание RU: Преобразуем наш добровольный союз в Европейскую федерацию. Все участники получат +10% к скорости строительства гражданских фабрик и +5% к производительности военных заводов, пока демократическая Германия возглавляет федерацию. Программа распространяется на новых участников и прекращается при выходе.

Описание EN: Transform our voluntary alliance into the European Federation. Every member receives +10% civilian factory construction speed and +5% factory output while democratic Germany leads the federation. Future entrants share the programme; leaving ends its benefits.

Источник: `common/national_focus/GER_political.txt:1200`. Стоимость: 10 (70 дней). Координаты: x=14, y=8. Иконка: `GFX_focus_GER_european_confederation`.

Предпосылки: (Арсенал демократии [GER_arsenal_of_democracy]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: GER_anti_imperialist_crusade.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- Награда вызывает вспомогательные эффекты: см. completion_reward и раздел определений.

Полное определение фокуса:

```pdx
focus = {
    id = GER_european_federation
    icon = GFX_focus_GER_european_confederation
    x = 14
    y = 8
    cost = 10
    prerequisite = {
        focus = GER_arsenal_of_democracy
    }
    available_if_capitulated = no
    available = {
        has_government = democratic
        is_subject = no
        OR = {
            is_in_faction = no
            is_faction_leader = yes
        }
    }
    completion_reward = {
        if = {
            limit = {
                is_in_faction = no
            }
            nww_GER_establish_mitteleuropa = yes
        }
        set_faction_name = GER_european_federation_faction
        GER_nww_refresh_federal_investment = yes
        every_other_country = {
            limit = {
                is_in_faction_with = ROOT
            }
            GER_nww_refresh_federal_investment = yes
        }
    }
    ai_will_do = {
        factor = 10
    }
}
```

### Поход против империализма — `GER_anti_imperialist_crusade`

EN: Anti-Imperialist Crusade.

Описание RU: Подготовим цели войны на освобождение против Франции и Британии, если они независимы, недемократичны и не входят в наш союз. Освобождение предстоит обеспечить войной и мирным урегулированием.

Описание EN: Prepare liberation war goals against France and Britain if they are independent, non-democratic states outside our alliance. Liberation must be achieved through war and the peace settlement.

Источник: `common/national_focus/GER_political.txt:1224`. Стоимость: 10 (70 дней). Координаты: x=14, y=9. Иконка: `GFX_focus_GER_liberate_exploited_colonial_workers`.

Предпосылки: (Европейская федерация [GER_european_federation]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: GER_shield_against_the_reds.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- `create_wargoal`: type = liberate_wargoal; target = FRA
- `create_wargoal`: type = liberate_wargoal; target = ENG

Полное определение фокуса:

```pdx
focus = {
    id = GER_anti_imperialist_crusade
    icon = GFX_focus_GER_liberate_exploited_colonial_workers
    x = 14
    y = 9
    cost = 10
    prerequisite = {
        focus = GER_european_federation
    }
    available_if_capitulated = no
    available = {
        has_government = democratic
        is_subject = no
    }
    completion_reward = {
        if = {
            limit = {
                FRA = {
                    exists = yes
                    is_subject = no
                    NOT = {
                        has_government = democratic
                    }
                }
                NOT = {
                    is_ally_with = FRA
                }
                NOT = {
                    has_war_with = FRA
                }
                NOT = {
                    has_wargoal_against = FRA
                }
            }
            create_wargoal = {
                type = liberate_wargoal
                target = FRA
            }
        }
        if = {
            limit = {
                ENG = {
                    exists = yes
                    is_subject = no
                    NOT = {
                        has_government = democratic
                    }
                }
                NOT = {
                    is_ally_with = ENG
                }
                NOT = {
                    has_war_with = ENG
                }
                NOT = {
                    has_wargoal_against = ENG
                }
            }
            create_wargoal = {
                type = liberate_wargoal
                target = ENG
            }
        }
    }
    ai_will_do = {
        factor = 10
    }
}
```

### Щит против красных — `GER_shield_against_the_reds`

EN: Shield against the Reds.

Описание RU: Демократия должна уметь защищаться. Мы получим +15% к обороне на национальных территориях, ещё две добровольческие дивизии и снижение порога мировой напряжённости для добровольцев на 50 пунктов. Разрешим отправку добровольцев и поддержим независимые страны, сопротивляющиеся фашистской или коммунистической агрессии.

Описание EN: Democracy must be able to defend itself. Gain +15% defence on our core territory, two additional volunteer divisions and a 50-point reduction to the volunteer world-tension requirement. Authorise volunteers and support independent states resisting fascist or communist aggression.

Источник: `common/national_focus/GER_political.txt:1258`. Стоимость: 10 (70 дней). Координаты: x=14, y=10. Иконка: `GFX_focus_GER_defender_of_democracy`.

Предпосылки: (Поход против империализма [GER_anti_imperialist_crusade]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: нет.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- Награда вызывает вспомогательные эффекты: см. completion_reward и раздел определений.

Полное определение фокуса:

```pdx
focus = {
    id = GER_shield_against_the_reds
    icon = GFX_focus_GER_defender_of_democracy
    x = 14
    y = 10
    cost = 10
    prerequisite = {
        focus = GER_anti_imperialist_crusade
    }
    available_if_capitulated = no
    available = {
        has_government = democratic
        is_subject = no
    }
    completion_reward = {
        swap_ideas = {
            remove_idea = GER_arsenal_of_democracy
            add_idea = GER_arsenal_of_democracy_shield
        }
        set_rule = {
            can_send_volunteers = yes
        }
    }
    ai_will_do = {
        factor = 10
    }
}
```

## Пангерманский путь — 8

### Пангерманский триумф — `GER_the_pan_germanic_triumph`

EN: The Pan-Germanic Triumph.

Описание RU: При поддержке националистов не менее 40% и балансе в тупиковом диапазоне от −0,30 до +0,30 пангерманское движение захватит правительство. Вильгельм III останется номинальным главой до упразднения династии.

Описание EN: With at least 40% nationalist support and a deadlocked balance between -0.30 and +0.30, the Pan-German movement seizes government. Wilhelm III remains its nominal head until the dynasty is abolished.

Источник: `common/national_focus/GER_political.txt:603`. Стоимость: 10 (70 дней). Координаты: x=22, y=4. Иконка: `GFX_focus_GER_hegemony_over_europe`.

Предпосылки: (Конец эпохи [GER_end_of_an_era]).

Взаимоисключения: GER_the_potsdam_coup, GER_parliamentary_spring, GER_the_spartacist_uprising.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): GER_pan_german_leagues.

Прямые продолжения: GER_abolish_the_hohenzollerns.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- `set_country_flag`: ger_pan_germanic_path
- `set_country_flag`: ger_bop_frozen
- `set_politics`: ruling_party = fascism; elections_allowed = no; election_frequency = 48

Полное определение фокуса:

```pdx
focus = {
    id = GER_the_pan_germanic_triumph
    icon = GFX_focus_GER_hegemony_over_europe
    x = 22
    y = 4
    cost = 10
    prerequisite = {
        focus = GER_end_of_an_era
    }
    available = {
        nww_GER_no_political_path = yes
        has_completed_focus = GER_pan_german_leagues
        has_country_flag = ger_wilhelm_ii_dead
        NOT = {
            fascism < 0.40
        }
        NOT = {
            has_civil_war = yes
        }
        NOT = {
            power_balance_value = {
                id = GER_kaiser_vs_reichstag
                value < -0.30
            }
        }
        NOT = {
            power_balance_value = {
                id = GER_kaiser_vs_reichstag
                value > 0.30
            }
        }
    }
    completion_reward = {
        set_country_flag = ger_pan_germanic_path
        set_country_flag = ger_bop_frozen
        set_politics = {
            ruling_party = fascism
            elections_allowed = no
            election_frequency = 48
        }
        GER_wilhelm_iii = {
            add_country_leader_role = {
                country_leader = {
                    ideology = GER_pan_germanism
                    expire = 1965.1.1
                    traits = {

                    }
                }
                promote_leader = yes
            }
        }
    }
    ai_will_do = {
        factor = 5
        modifier = {
            factor = 0
            is_historical_focus_on = yes
        }
    }
    mutually_exclusive = {
        focus = GER_the_potsdam_coup
        focus = GER_parliamentary_spring
        focus = GER_the_spartacist_uprising
    }
}
```

### Упразднить власть Гогенцоллернов — `GER_abolish_the_hohenzollerns`

EN: Abolish the Hohenzollerns.

Описание RU: Устраним Вильгельма III и последние династические ограничения. Альфред Гугенберг возглавит радикальное националистическое правительство; баланс между короной и рейхстагом будет окончательно упразднён. Реорганизация штабов снимет штраф к организации от имперского перенапряжения.

Описание EN: Remove Wilhelm III and the last dynastic restraints. Alfred Hugenberg heads a radical nationalist government, and the crown-Reichstag balance of power is abolished permanently. Reorganise the staff to remove the organisation penalty from Imperial Overstretch.

Источник: `common/national_focus/GER_political.txt:669`. Стоимость: 10 (70 дней). Координаты: x=22, y=5. Иконка: `GFX_focus_GER_the_supreme_leader`.

Предпосылки: (Пангерманский триумф [GER_the_pan_germanic_triumph]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: GER_anschluss_by_force.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- `set_country_flag`: ger_bop_removed

Полное определение фокуса:

```pdx
focus = {
    id = GER_abolish_the_hohenzollerns
    icon = GFX_focus_GER_the_supreme_leader
    x = 22
    y = 5
    cost = 10
    prerequisite = {
        focus = GER_the_pan_germanic_triumph
    }
    available = {
        has_government = fascism
    }
    completion_reward = {
        GER_nww_partial_army_reform = yes
        retire_character = GER_wilhelm_iii
        GER_alfred_hugenberg = {
            add_country_leader_role = {
                country_leader = {
                    ideology = GER_pan_germanism
                    expire = 1965.1.1
                    traits = {

                    }
                }
                promote_leader = yes
            }
        }
        set_country_flag = ger_bop_removed
        if = {
            limit = {
                has_power_balance = {
                    id = GER_kaiser_vs_reichstag
                }
            }
            remove_power_balance = {
                id = GER_kaiser_vs_reichstag
            }
        }
    }
}
```

### Аншлюс силой — `GER_anschluss_by_force`

EN: Anschluss by Force.

Описание RU: Потребуем от Австрии согласиться на присоединение к новому германскому государству. Отказ даёт цель войны для аннексии. Требование направляется только независимой Австрии, находящейся в мире.

Описание EN: Demand Austria consent to annexation into the new German state. A refusal grants an annexation war goal. The demand is delivered only to an independent Austria at peace.

Источник: `common/national_focus/GER_political.txt:709`. Стоимость: 10 (70 дней). Координаты: x=22, y=6. Иконка: `GFX_focus_GER_anschluss`.

Предпосылки: (Упразднить власть Гогенцоллернов [GER_abolish_the_hohenzollerns]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: GER_lebensraum_in_the_east.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- `country_event`: id = ger_crisis.40; days = 1

Полное определение фокуса:

```pdx
focus = {
    id = GER_anschluss_by_force
    icon = GFX_focus_GER_anschluss
    x = 22
    y = 6
    cost = 10
    prerequisite = {
        focus = GER_abolish_the_hohenzollerns
    }
    bypass = {
        AUS = {
            exists = no
        }
    }
    available = {
        has_government = fascism
        is_subject = no
        AUS = {
            exists = yes
            is_subject = no
        }
        NOT = {
            has_war_with = AUS
        }
        has_war = no
        AUS = {
            has_war = no
        }
        nww_GER_ai_can_target_AUS = yes
    }
    completion_reward = {
        if = {
            limit = {
                has_government = fascism
                is_subject = no
                AUS = {
                    exists = yes
                    is_subject = no
                }
                NOT = {
                    has_war_with = AUS
                }
                has_war = no
                AUS = {
                    has_war = no
                }
            }
            AUS = {
                country_event = {
                    id = ger_crisis.40
                    days = 1
                }
            }
        }
    }
}
```

### Экспансия на Восток — `GER_lebensraum_in_the_east`

EN: Expansion in the East.

Описание RU: Пангерманское руководство объявляет восточные приграничные земли сферой своей экспансии. Подготовим цели войны для аннексии независимых несоюзных Литвы-Беларуси и Польши только после открытия восточного направления.\n\n$GER_eastern_1939_gate_tt$

Описание EN: The Pan-German leadership claims the eastern borderlands as its sphere of expansion. Prepare annexation war goals against independent, non-allied Lithuania-Belarus and Poland, only after the eastern gate opens.\n\n$GER_eastern_1939_gate_tt$

Источник: `common/national_focus/GER_political.txt:765`. Стоимость: 10 (70 дней). Координаты: x=22, y=7. Иконка: `GFX_focus_GER_the_eastern_border`.

Предпосылки: (Аншлюс силой [GER_anschluss_by_force]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: GER_the_new_reich.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- Награда вызывает вспомогательные эффекты: см. completion_reward и раздел определений.

Полное определение фокуса:

```pdx
focus = {
    id = GER_lebensraum_in_the_east
    icon = GFX_focus_GER_the_eastern_border
    x = 22
    y = 7
    cost = 10
    prerequisite = {
        focus = GER_anschluss_by_force
    }
    available = {
        has_government = fascism
        is_subject = no
        date > 1938.12.31
        custom_trigger_tooltip = {
            tooltip = GER_eastern_1939_gate_tt
            date > 1938.12.31
        }
        nww_GER_ai_can_prepare_campaign = yes
    }
    completion_reward = {
        nww_GER_pan_german_eastern_wargoals = yes
    }
}
```

### Новый рейх — `GER_the_new_reich`

EN: The New Reich.

Описание RU: Милитаризованное националистическое государство готовит дивизии к наступательной войне: +15% атаки, +20% прорыва и +10% скорости дивизий. Завершить военную и административную реформу, удалив обе версии имперского перенапряжения.

Описание EN: A militarised nationalist state mobilises its divisions for offensive war: +15% division attack, +20% breakthrough and +10% division speed. Complete military and administrative reform, removing both versions of Imperial Overstretch.

Источник: `common/national_focus/GER_political.txt:788`. Стоимость: 10 (70 дней). Координаты: x=22, y=8. Иконка: `GFX_focus_GER_german_army_invincible`.

Предпосылки: (Экспансия на Восток [GER_lebensraum_in_the_east]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: GER_drang_nach_osten_expanded.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- `remove_ideas`: GER_imperial_overstretch
- `remove_ideas`: GER_imperial_overstretch_2
- `add_ideas`: GER_the_new_reich

Полное определение фокуса:

```pdx
focus = {
    id = GER_the_new_reich
    icon = GFX_focus_GER_german_army_invincible
    x = 22
    y = 8
    cost = 10
    prerequisite = {
        focus = GER_lebensraum_in_the_east
    }
    available = {
        has_government = fascism
    }
    completion_reward = {
        remove_ideas = GER_imperial_overstretch
        remove_ideas = GER_imperial_overstretch_2
        add_ideas = GER_the_new_reich
    }
}
```

### Расширить натиск на Восток — `GER_drang_nach_osten_expanded`

EN: Expand the Eastern Offensive.

Описание RU: С 1941 года радикальное правительство готовит цели войны на завоевание Советской России и Махновщины, если они сохраняют независимость и не являются нашими союзниками.

Описание EN: From 1941 the radical government prepares conquest war goals against Soviet Russia and the Makhnovist state, provided they still exist as independent, non-allied states.

Источник: `common/national_focus/GER_political.txt:1087`. Стоимость: 10 (70 дней). Координаты: x=22, y=9. Иконка: `GFX_focus_GER_the_eastern_border`.

Предпосылки: (Новый рейх [GER_the_new_reich]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: GER_total_assimilation.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- `create_wargoal`: type = annex_everything; target = SOV
- `create_wargoal`: type = annex_everything; target = MKN

Полное определение фокуса:

```pdx
focus = {
    id = GER_drang_nach_osten_expanded
    icon = GFX_focus_GER_the_eastern_border
    x = 22
    y = 9
    cost = 10
    prerequisite = {
        focus = GER_the_new_reich
    }
    available_if_capitulated = no
    available = {
        has_government = fascism
        is_subject = no
        date > 1940.12.31
    }
    completion_reward = {
        if = {
            limit = {
                SOV = {
                    exists = yes
                    is_subject = no
                }
                NOT = {
                    is_ally_with = SOV
                }
                NOT = {
                    has_war_with = SOV
                }
                NOT = {
                    has_wargoal_against = SOV
                }
            }
            create_wargoal = {
                type = annex_everything
                target = SOV
            }
        }
        if = {
            limit = {
                MKN = {
                    exists = yes
                    is_subject = no
                }
                NOT = {
                    is_ally_with = MKN
                }
                NOT = {
                    has_war_with = MKN
                }
                NOT = {
                    has_wargoal_against = MKN
                }
            }
            create_wargoal = {
                type = annex_everything
                target = MKN
            }
        }
    }
    ai_will_do = {
        factor = 10
    }
}
```

### Тотальная ассимиляция — `GER_total_assimilation`

EN: Total Assimilation.

Описание RU: Принудительная администрация ускорит рост подчинения на оккупированных нами территориях на 10% и снизит целевое сопротивление на 10 процентных пунктов. Полицейский аппарат увеличит потребность в гарнизонах на 10%. Эти меры не дают новых национальных территорий.

Описание EN: A coercive occupation administration accelerates compliance growth in our occupied territories by 10% and lowers the resistance target by 10 percentage points. Its extensive policing increases required garrisons by 10%. These measures grant no new national cores.

Источник: `common/national_focus/GER_political.txt:1122`. Стоимость: 10 (70 дней). Координаты: x=22, y=10. Иконка: `GFX_focus_GER_realpolitik`.

Предпосылки: (Расширить натиск на Восток [GER_drang_nach_osten_expanded]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: GER_hegemony_over_europe_focus.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- Награда вызывает вспомогательные эффекты: см. completion_reward и раздел определений.

Полное определение фокуса:

```pdx
focus = {
    id = GER_total_assimilation
    icon = GFX_focus_GER_realpolitik
    x = 22
    y = 10
    cost = 10
    prerequisite = {
        focus = GER_drang_nach_osten_expanded
    }
    available_if_capitulated = no
    available = {
        has_government = fascism
        is_subject = no
    }
    completion_reward = {
        swap_ideas = {
            remove_idea = GER_the_new_reich
            add_idea = GER_the_new_reich_integrated
        }
    }
    ai_will_do = {
        factor = 10
    }
}
```

### Гегемония над Европой — `GER_hegemony_over_europe_focus`

EN: Hegemony over Europe.

Описание RU: Новый рейх получит цели войны на завоевание независимых Дании, Норвегии, Швеции, Финляндии и Швейцарии. Союзники и страны, с которыми мы уже воюем, исключаются.

Описание EN: The New Reich issues conquest war goals against independent Denmark, Norway, Sweden, Finland and Switzerland, excluding our allies and existing wars.

Источник: `common/national_focus/GER_political.txt:1139`. Стоимость: 10 (70 дней). Координаты: x=22, y=11. Иконка: `GFX_focus_GER_hegemony_over_europe`.

Предпосылки: (Тотальная ассимиляция [GER_total_assimilation]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: нет.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- `create_wargoal`: type = annex_everything; target = DEN
- `create_wargoal`: type = annex_everything; target = NOR
- `create_wargoal`: type = annex_everything; target = SWE
- `create_wargoal`: type = annex_everything; target = FIN
- `create_wargoal`: type = annex_everything; target = SWI

Полное определение фокуса:

```pdx
focus = {
    id = GER_hegemony_over_europe_focus
    icon = GFX_focus_GER_hegemony_over_europe
    x = 22
    y = 11
    cost = 10
    prerequisite = {
        focus = GER_total_assimilation
    }
    available_if_capitulated = no
    available = {
        has_government = fascism
        is_subject = no
    }
    completion_reward = {
        if = {
            limit = {
                DEN = {
                    exists = yes
                    is_subject = no
                }
                NOT = {
                    is_ally_with = DEN
                }
                NOT = {
                    has_war_with = DEN
                }
                NOT = {
                    has_wargoal_against = DEN
                }
            }
            create_wargoal = {
                type = annex_everything
                target = DEN
            }
        }
        if = {
            limit = {
                NOR = {
                    exists = yes
                    is_subject = no
                }
                NOT = {
                    is_ally_with = NOR
                }
                NOT = {
                    has_war_with = NOR
                }
                NOT = {
                    has_wargoal_against = NOR
                }
            }
            create_wargoal = {
                type = annex_everything
                target = NOR
            }
        }
        if = {
            limit = {
                SWE = {
                    exists = yes
                    is_subject = no
                }
                NOT = {
                    is_ally_with = SWE
                }
                NOT = {
                    has_war_with = SWE
                }
                NOT = {
                    has_wargoal_against = SWE
                }
            }
            create_wargoal = {
                type = annex_everything
                target = SWE
            }
        }
        if = {
            limit = {
                FIN = {
                    exists = yes
                    is_subject = no
                }
                NOT = {
                    is_ally_with = FIN
                }
                NOT = {
                    has_war_with = FIN
                }
                NOT = {
                    has_wargoal_against = FIN
                }
            }
            create_wargoal = {
                type = annex_everything
                target = FIN
            }
        }
        if = {
            limit = {
                SWI = {
                    exists = yes
                    is_subject = no
                }
                NOT = {
                    is_ally_with = SWI
                }
                NOT = {
                    has_war_with = SWI
                }
                NOT = {
                    has_wargoal_against = SWI
                }
            }
            create_wargoal = {
                type = annex_everything
                target = SWI
            }
        }
    }
    ai_will_do = {
        factor = 10
    }
}
```

## Спартакистский путь — 9

### Спартакистское восстание — `GER_the_spartacist_uprising`

EN: The Spartacist Uprising.

Описание RU: При организованных рабочих и поддержке коммунистов не менее 40% выступим против монархии. Начнётся настоящая гражданская война; игрок перейдёт к коммунистическим повстанцам с 40% исходной военной силы. Для провозглашения республики необходима победа.

Описание EN: With workers organised and at least 40% Communist support, rise against the monarchy. A real civil war begins; the player switches to the Communist insurgents with 40% of the initial military strength. Victory is required before proclaiming the republic.

Источник: `common/national_focus/GER_political.txt:806`. Стоимость: 10 (70 дней). Координаты: x=30, y=4. Иконка: `GFX_focus_GER_support_the_proletarian_uprising`.

Предпосылки: (Конец эпохи [GER_end_of_an_era]).

Взаимоисключения: GER_the_potsdam_coup, GER_parliamentary_spring, GER_the_pan_germanic_triumph.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): GER_organize_ruhr_workers.

Прямые продолжения: GER_german_soviet_republic.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- Награда вызывает вспомогательные эффекты: см. completion_reward и раздел определений.

Полное определение фокуса:

```pdx
focus = {
    id = GER_the_spartacist_uprising
    icon = GFX_focus_GER_support_the_proletarian_uprising
    x = 30
    y = 4
    cost = 10
    prerequisite = {
        focus = GER_end_of_an_era
    }
    bypass = {
        has_country_flag = ger_spartacist_side
    }
    available = {
        nww_GER_no_political_path = yes
        has_completed_focus = GER_organize_ruhr_workers
        has_country_flag = ger_wilhelm_ii_dead
        NOT = {
            communism < 0.40
        }
        NOT = {
            has_civil_war = yes
        }
        is_subject = no
    }
    completion_reward = {
        nww_GER_start_spartacist_civil_war = yes
    }
    ai_will_do = {
        factor = 5
        modifier = {
            factor = 0
            is_historical_focus_on = yes
        }
    }
    mutually_exclusive = {
        focus = GER_the_potsdam_coup
        focus = GER_parliamentary_spring
        focus = GER_the_pan_germanic_triumph
    }
}
```

### Германская советская республика — `GER_german_soviet_republic`

EN: The German Soviet Republic.

Описание RU: После победы спартакистов над имперскими лоялистами в гражданской войне учредим германскую республику советов во главе с Эрнстом Тельманом. Необходима победа восстания, а не просто прекращение боёв. Воссоздать штабы и заменить имперское перенапряжение облегчённой версией.

Описание EN: After the Spartacists defeat the imperial loyalists in the civil war, establish a German council republic under Ernst Thalmann. The uprising must have won; simply waiting for the fighting to end is insufficient. Reconstitute the staff and replace Imperial Overstretch with its reduced version.

Источник: `common/national_focus/GER_political.txt:846`. Стоимость: 10 (70 дней). Координаты: x=30, y=5. Иконка: `GFX_focus_GER_the_peoples_victory`.

Предпосылки: (Спартакистское восстание [GER_the_spartacist_uprising]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: GER_workers_militias.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- `set_politics`: ruling_party = communism; elections_allowed = no; election_frequency = 48

Полное определение фокуса:

```pdx
focus = {
    id = GER_german_soviet_republic
    icon = GFX_focus_GER_the_peoples_victory
    x = 30
    y = 5
    cost = 10
    prerequisite = {
        focus = GER_the_spartacist_uprising
    }
    available = {
        has_country_flag = ger_spartacist_side
        has_country_flag = ger_spartacist_victory
        has_government = communism
        NOT = {
            has_civil_war = yes
        }
    }
    completion_reward = {
        GER_nww_partial_army_reform = yes
        set_politics = {
            ruling_party = communism
            elections_allowed = no
            election_frequency = 48
        }
        GER_ernst_thalmann = {
            set_portraits = {
                civilian = {
                    large = GFX_NWW_GER_ernst_thalmann
                }
            }
            add_country_leader_role = {
                country_leader = {
                    ideology = GER_spartacism
                    expire = 1965.1.1
                    traits = {

                    }
                }
                promote_leader = yes
            }
        }
    }
}
```

### Рабочие ополчения — `GER_workers_militias`

EN: Workers Militias.

Описание RU: Создадим единую организацию ополчений на основе фабричных советов: +5 процентных пунктов военнообязанного населения и +10% восстановления организации. Завершить военную и административную реформу, удалив обе версии имперского перенапряжения.

Описание EN: Build a common militia organisation around the factory councils, granting +5 percentage points of recruitable population and +10% organisation recovery. Complete military and administrative reform, removing both versions of Imperial Overstretch.

Источник: `common/national_focus/GER_political.txt:889`. Стоимость: 10 (70 дней). Координаты: x=30, y=6. Иконка: `GFX_focus_GER_proletarian_solidarity`.

Предпосылки: (Германская советская республика [GER_german_soviet_republic]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: GER_dismantle_imperial_borders.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- `remove_ideas`: GER_imperial_overstretch
- `remove_ideas`: GER_imperial_overstretch_2
- `add_ideas`: GER_workers_militias

Полное определение фокуса:

```pdx
focus = {
    id = GER_workers_militias
    icon = GFX_focus_GER_proletarian_solidarity
    x = 30
    y = 6
    cost = 10
    prerequisite = {
        focus = GER_german_soviet_republic
    }
    available = {
        has_government = communism
    }
    completion_reward = {
        remove_ideas = GER_imperial_overstretch
        remove_ideas = GER_imperial_overstretch_2
        add_ideas = GER_workers_militias
    }
}
```

### Демонтировать имперские границы — `GER_dismantle_imperial_borders`

EN: Dismantle Imperial Borders.

Описание RU: Прекратим германское господство над Литвой-Беларусью и Польшей. Освобождаются только наши собственные зависимые страны; независимые государства и владения третьих держав не аннексируются и не передаются.

Описание EN: End German overlordship over Lithuania-Belarus and Poland. Only our own existing subjects are freed; independent countries and the possessions of third powers are not annexed or transferred.

Источник: `common/national_focus/GER_political.txt:907`. Стоимость: 10 (70 дней). Координаты: x=30, y=7. Иконка: `GFX_focus_GER_liberate_exploited_colonial_workers`.

Предпосылки: (Рабочие ополчения [GER_workers_militias]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: GER_berlin_moscow_axis.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- Награда вызывает вспомогательные эффекты: см. completion_reward и раздел определений.

Полное определение фокуса:

```pdx
focus = {
    id = GER_dismantle_imperial_borders
    icon = GFX_focus_GER_liberate_exploited_colonial_workers
    x = 30
    y = 7
    cost = 10
    prerequisite = {
        focus = GER_workers_militias
    }
    available = {
        has_government = communism
        is_subject = no
    }
    completion_reward = {
        nww_GER_free_eastern_subjects = yes
    }
}
```

### Ось Берлин — Москва — `GER_berlin_moscow_axis`

EN: The Berlin-Moscow Axis.

Описание RU: Предложим советскому правительству принять нашу республику в его союз или создать общий коммунистический альянс, если такого ещё нет. Необходимо согласие СССР; отказ не приводит к войне.

Описание EN: Ask the Soviet government to admit our republic into its alliance, or create a common Communist alliance if it has none. Soviet consent is required; a refusal does not start a war.

Источник: `common/national_focus/GER_political.txt:924`. Стоимость: 10 (70 дней). Координаты: x=30, y=8. Иконка: `GFX_focus_GER_SOV_treaty`.

Предпосылки: (Демонтировать имперские границы [GER_dismantle_imperial_borders]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: GER_world_revolution.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- `country_event`: id = ger_crisis.60; days = 1

Полное определение фокуса:

```pdx
focus = {
    id = GER_berlin_moscow_axis
    icon = GFX_focus_GER_SOV_treaty
    x = 30
    y = 8
    cost = 10
    prerequisite = {
        focus = GER_dismantle_imperial_borders
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
        OR = {
            is_in_faction = no
            is_in_faction_with = SOV
        }
        SOV = {
            OR = {
                is_faction_leader = yes
                is_in_faction = no
                is_in_faction_with = ROOT
            }
        }
    }
    completion_reward = {
        if = {
            limit = {
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
            SOV = {
                country_event = {
                    id = ger_crisis.60
                    days = 1
                }
            }
        }
    }
}
```

### Мировая революция — `GER_world_revolution`

EN: World Revolution.

Описание RU: Подготовим цели войны для аннексии независимых несоюзных Франции и Британии. Эти западные цели не отменяют ограничений Германии на восточном направлении.

Описание EN: Prepare annexation war goals against independent, non-allied France and Britain. These western objectives never waive Germany’s eastern restrictions.

Источник: `common/national_focus/GER_political.txt:979`. Стоимость: 10 (70 дней). Координаты: x=30, y=9. Иконка: `GFX_focus_GER_strengthen_the_proletarian_international`.

Предпосылки: (Ось Берлин — Москва [GER_berlin_moscow_axis]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: GER_red_rhine.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- Награда вызывает вспомогательные эффекты: см. completion_reward и раздел определений.

Полное определение фокуса:

```pdx
focus = {
    id = GER_world_revolution
    icon = GFX_focus_GER_strengthen_the_proletarian_international
    x = 30
    y = 9
    cost = 10
    prerequisite = {
        focus = GER_berlin_moscow_axis
    }
    available = {
        has_government = communism
        is_subject = no
        nww_GER_ai_can_prepare_campaign = yes
    }
    completion_reward = {
        nww_GER_western_revolution_wargoals = yes
    }
}
```

### Красный Рейн — `GER_red_rhine`

EN: The Red Rhine.

Описание RU: Поддержим коммунистические организации Франции, Нидерландов, Бельгии и Люксембурга. Каждая независимая страна сможет допустить агитацию или подавить её. Коммунистическое восстание возможно лишь при значительной местной поддержке и наличии более одной контролируемой области.

Описание EN: Support communist organisations in France, the Netherlands, Belgium and Luxembourg. Each independent recipient may tolerate agitation or suppress it. A communist uprising is possible only with a substantial local movement and more than one controlled state.

Источник: `common/national_focus/GER_political.txt:1276`. Стоимость: 10 (70 дней). Координаты: x=30, y=10. Иконка: `GFX_focus_GER_support_the_proletarian_uprising`.

Предпосылки: (Мировая революция [GER_world_revolution]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: GER_nva_mass_mobilization.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- `country_event`: id = ger_crisis.70; days = 1
- `country_event`: id = ger_crisis.70; days = 1
- `country_event`: id = ger_crisis.70; days = 1
- `country_event`: id = ger_crisis.70; days = 1

Полное определение фокуса:

```pdx
focus = {
    id = GER_red_rhine
    icon = GFX_focus_GER_support_the_proletarian_uprising
    x = 30
    y = 10
    cost = 10
    prerequisite = {
        focus = GER_world_revolution
    }
    available_if_capitulated = no
    available = {
        has_government = communism
        is_subject = no
    }
    completion_reward = {
        FRA = {
            if = {
                limit = {
                    exists = yes
                    is_subject = no
                    NOT = {
                        has_government = communism
                    }
                    has_civil_war = no
                }
                country_event = {
                    id = ger_crisis.70
                    days = 1
                }
            }
        }
        HOL = {
            if = {
                limit = {
                    exists = yes
                    is_subject = no
                    NOT = {
                        has_government = communism
                    }
                    has_civil_war = no
                }
                country_event = {
                    id = ger_crisis.70
                    days = 1
                }
            }
        }
        BEL = {
            if = {
                limit = {
                    exists = yes
                    is_subject = no
                    NOT = {
                        has_government = communism
                    }
                    has_civil_war = no
                }
                country_event = {
                    id = ger_crisis.70
                    days = 1
                }
            }
        }
        LUX = {
            if = {
                limit = {
                    exists = yes
                    is_subject = no
                    NOT = {
                        has_government = communism
                    }
                    has_civil_war = no
                }
                country_event = {
                    id = ger_crisis.70
                    days = 1
                }
            }
        }
    }
    ai_will_do = {
        factor = 10
    }
}
```

### Массовая мобилизация ННА — `GER_nva_mass_mobilization`

EN: National People’s Army.

Описание RU: Преобразуем рабочие ополчения в постоянную массовую армию. Увеличим долю военнообязанного населения ещё на 5 процентных пунктов, доведя общий бонус до 10. Сохраним +10% к восстановлению организации и сократим время подготовки армии на 10%. Приоритет пехоты оборачивается штрафом 20% к скорости исследований авиационной и морской техники.

Описание EN: Turn the workers’ militias into a permanent mass army. Raise recruitable population by another 5 percentage points, to 10 in total. Retain +10% organisation recovery and reduce army training time by 10%. Prioritising infantry imposes a 20% research-speed penalty on aircraft and naval equipment.

Источник: `common/national_focus/GER_political.txt:1296`. Стоимость: 10 (70 дней). Координаты: x=30, y=11. Иконка: `GFX_focus_GER_proletarian_solidarity`.

Предпосылки: (Красный Рейн [GER_red_rhine]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: GER_challenge_moscow.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- Награда вызывает вспомогательные эффекты: см. completion_reward и раздел определений.

Полное определение фокуса:

```pdx
focus = {
    id = GER_nva_mass_mobilization
    icon = GFX_focus_GER_proletarian_solidarity
    x = 30
    y = 11
    cost = 10
    prerequisite = {
        focus = GER_red_rhine
    }
    available_if_capitulated = no
    available = {
        has_government = communism
        is_subject = no
    }
    completion_reward = {
        swap_ideas = {
            remove_idea = GER_workers_militias
            add_idea = GER_nva_mass_army
        }
    }
    ai_will_do = {
        factor = 10
    }
}
```

### Бросить вызов Москве — `GER_challenge_moscow`

EN: Challenge Moscow.

Описание RU: С 1941 года, в мирное время, оспорим притязания Москвы на руководство революцией. Выйдем из советского союза либо исключим Советскую Россию, если возглавляем альянс, затем подготовим цель войны на завоевание независимого советского государства.

Описание EN: From 1941, at peace, dispute Moscow’s claim to lead the revolution. Leave the Soviet alliance, or expel the Soviet Union if we lead it, then prepare a conquest war goal against an independent Soviet state.

Источник: `common/national_focus/GER_political.txt:1313`. Стоимость: 10 (70 дней). Координаты: x=30, y=12. Иконка: `GFX_focus_GER_strengthen_the_proletarian_international`.

Предпосылки: (Массовая мобилизация ННА [GER_nva_mass_mobilization]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: нет.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- `create_wargoal`: type = annex_everything; target = SOV

Полное определение фокуса:

```pdx
focus = {
    id = GER_challenge_moscow
    icon = GFX_focus_GER_strengthen_the_proletarian_international
    x = 30
    y = 12
    cost = 10
    prerequisite = {
        focus = GER_nva_mass_mobilization
    }
    available_if_capitulated = no
    available = {
        has_government = communism
        is_subject = no
        date > 1940.12.31
        has_war = no
    }
    completion_reward = {
        if = {
            limit = {
                is_in_faction_with = SOV
            }
            if = {
                limit = {
                    is_faction_leader = yes
                }
                remove_from_faction = SOV
            }
            else = {
                leave_faction = yes
            }
        }
        if = {
            limit = {
                SOV = {
                    exists = yes
                    is_subject = no
                }
                NOT = {
                    is_ally_with = SOV
                }
                NOT = {
                    has_war_with = SOV
                }
                NOT = {
                    has_wargoal_against = SOV
                }
            }
            create_wargoal = {
                type = annex_everything
                target = SOV
            }
        }
    }
    ai_will_do = {
        factor = 10
    }
}
```

## Промышленность, наука, торговля и разведка — 31

### Имперский промышленный совет — `GER_krupp_and_thyssen`

EN: Imperial Industrial Council.

Описание RU: Крупп, Тиссен, электротехнические концерны и земли согласуют программу инвестиций. Это начало развития единого промышленного комплекса, а не схема долгов ради завоеваний.

Описание EN: Krupp, Thyssen, electrical firms and the states coordinate investment. Industrial research and construction improve through a lasting program financed without conquest debt.

Источник: `common/national_focus/GER_focuses.txt:38`. Стоимость: 10 (70 дней). Координаты: x=51, y=0. Иконка: `GFX_focus_generic_industrialists`.

Предпосылки: нет нарисованной предпосылки; см. available.

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: GER_mitteleuropa_trade, GER_1, GER_5.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- Параметр `GER_industry_construction`: 0.05
- `add_tech_bonus`: category = industry; uses = 1; bonus = 0.5

Полное определение фокуса:

```pdx
focus = {
    id = GER_krupp_and_thyssen
    x = 51
    y = 0
    cost = 10
    icon = GFX_focus_generic_industrialists
    available_if_capitulated = no
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    completion_reward = {
        add_to_variable = {
            GER_industry_construction = 0.05
            tooltip = GER_nww_industry_construction_tt
        }
        add_tech_bonus = {
            category = industry
            uses = 1
            bonus = 0.5
        }
        hidden_effect = {
            GER_nww_refresh_industry = yes
        }
    }
    ai_will_do = {
        factor = 1
    }
}
```

### Модернизировать Рурский бассейн — `GER_1`

EN: Modernize the Ruhr Basin.

Описание RU: Новые шахтные стволы и обогатительные установки увеличат добычу рурского угля. Рост промышленности должен опираться на реальную энергетическую базу.

Описание EN: Modern shafts and processing plants expand Ruhr coal extraction. The resource investment requires ownership and control of the Ruhr.

Источник: `common/national_focus/GER_focuses.txt:144`. Стоимость: 10 (70 дней). Координаты: x=49, y=1. Иконка: `GFX_focus_generic_coal_mining`.

Предпосылки: (Имперский промышленный совет [GER_krupp_and_thyssen]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: GER_nww_electrical_grid.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- `add_resource`: type = coal; amount = 8

Полное определение фокуса:

```pdx
focus = {
    id = GER_1
    x = 49
    y = 1
    cost = 10
    icon = GFX_focus_generic_coal_mining
    prerequisite = {
        focus = GER_krupp_and_thyssen
    }
    available_if_capitulated = no
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    completion_reward = {
        42 = {
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
        hidden_effect = {
            GER_nww_refresh_industry = yes
        }
    }
    ai_will_do = {
        factor = 1
    }
}
```

### Рейнские инвестиционные банки — `GER_5`

EN: Rhineland Investment Banks.

Описание RU: Привлечём долгосрочные вложения к рейнским и общегерманским предприятиям. Производственные мощности растут без МЕФО и завоевательной долговой экономики.

Описание EN: Long-term investment supports a new civilian enterprise on owned and controlled German core territory.

Источник: `common/national_focus/GER_focuses.txt:275`. Стоимость: 10 (70 дней). Координаты: x=53, y=1. Иконка: `GFX_focus_generic_industry_investment`.

Предпосылки: (Имперский промышленный совет [GER_krupp_and_thyssen]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: GER_6, GER_nww_worker_housing.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- Награда вызывает вспомогательные эффекты: см. completion_reward и раздел определений.

Полное определение фокуса:

```pdx
focus = {
    id = GER_5
    x = 53
    y = 1
    cost = 10
    icon = GFX_focus_generic_industry_investment
    prerequisite = {
        focus = GER_krupp_and_thyssen
    }
    available_if_capitulated = no
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    completion_reward = {
        GER_nww_build_civilian = yes
        hidden_effect = {
            GER_nww_refresh_industry = yes
        }
    }
    ai_will_do = {
        factor = 1
    }
}
```

### Торговые палаты Миттельевропы — `GER_mitteleuropa_trade`

EN: Mitteleuropa Chambers of Commerce.

Описание RU: Договоры поставок и торговые палаты расширят гражданское производство. Экономическое сотрудничество само по себе не подчиняет соседей.

Описание EN: Supply contracts and chambers of commerce expand civilian production. Economic cooperation does not itself subjugate neighboring states.

Источник: `common/national_focus/GER_focuses.txt:82`. Стоимость: 10 (70 дней). Координаты: x=57, y=1. Иконка: `GFX_goal_generic_trade`.

Предпосылки: (Имперский промышленный совет [GER_krupp_and_thyssen]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: GER_2.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- Награда вызывает вспомогательные эффекты: см. completion_reward и раздел определений.

Полное определение фокуса:

```pdx
focus = {
    id = GER_mitteleuropa_trade
    x = 57
    y = 1
    cost = 10
    icon = GFX_goal_generic_trade
    prerequisite = {
        focus = GER_krupp_and_thyssen
    }
    available_if_capitulated = no
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    completion_reward = {
        GER_nww_build_civilian = yes
        hidden_effect = {
            GER_nww_refresh_industry = yes
        }
    }
    ai_will_do = {
        factor = 1
    }
}
```

### Соединить региональные энергосистемы — `GER_nww_electrical_grid`

EN: Connect Regional Power Grids.

Описание RU: Объединим региональные электростанции и промышленные сети. Уголь и генерация останутся основой энергетики, а единая сеть уменьшит потери.

Описание EN: Link regional generating stations and industrial grids to improve energy supply. Coal extraction and efficient distribution must support new factories.

Источник: `common/national_focus/GER_focuses.txt:438`. Стоимость: 10 (70 дней). Координаты: x=49, y=2. Иконка: `GFX_focus_generic_electrification`.

Предпосылки: (Модернизировать Рурский бассейн [GER_1]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: GER_nww_silesian_steel, GER_nww_energy_keystones.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- Параметр `GER_industry_energy`: 0.1

Полное определение фокуса:

```pdx
focus = {
    id = GER_nww_electrical_grid
    x = 49
    y = 2
    cost = 10
    icon = GFX_focus_generic_electrification
    prerequisite = {
        focus = GER_1
    }
    available_if_capitulated = no
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    completion_reward = {
        add_to_variable = {
            GER_industry_energy = 0.1
            tooltip = GER_nww_industry_energy_tt
        }
        hidden_effect = {
            GER_nww_refresh_industry = yes
        }
    }
    ai_will_do = {
        factor = 1
    }
}
```

### Промышленные облигации земель — `GER_6`

EN: State Industrial Bonds.

Описание RU: Добровольные облигации земель направят сбережения в оборудование, коммуникации и новые корпуса. Неограниченных денежных или фабричных наград эта программа не даёт.

Описание EN: Voluntary state industrial bonds direct savings into equipment and construction, permanently improving the industrial program.

Источник: `common/national_focus/GER_focuses.txt:298`. Стоимость: 10 (70 дней). Координаты: x=53, y=2. Иконка: `GFX_focus_generic_stockpile_currency`.

Предпосылки: (Рейнские инвестиционные банки [GER_5]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: GER_7.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- Параметр `GER_industry_construction`: 0.05

Полное определение фокуса:

```pdx
focus = {
    id = GER_6
    x = 53
    y = 2
    cost = 10
    icon = GFX_focus_generic_stockpile_currency
    prerequisite = {
        focus = GER_5
    }
    available_if_capitulated = no
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    completion_reward = {
        add_to_variable = {
            GER_industry_construction = 0.05
            tooltip = GER_nww_industry_construction_tt
        }
        hidden_effect = {
            GER_nww_refresh_industry = yes
        }
    }
    ai_will_do = {
        factor = 1
    }
}
```

### Жильё для промышленных рабочих — `GER_nww_worker_housing`

EN: Industrial Workers Housing.

Описание RU: Жилищные программы снизят напряжённость в растущих промышленных городах. Развитие производственной базы должно сопровождаться улучшением быта.

Описание EN: Housing programs reduce tensions in growing industrial towns and improve national stability.

Источник: `common/national_focus/GER_focuses.txt:827`. Стоимость: 10 (70 дней). Координаты: x=55, y=2. Иконка: `GFX_focus_generic_low_cost_housing`.

Предпосылки: (Рейнские инвестиционные банки [GER_5]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: нет.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- `add_stability`: 0.05

Полное определение фокуса:

```pdx
focus = {
    id = GER_nww_worker_housing
    x = 55
    y = 2
    cost = 10
    icon = GFX_focus_generic_low_cost_housing
    prerequisite = {
        focus = GER_5
    }
    available_if_capitulated = no
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    completion_reward = {
        add_stability = 0.05
        hidden_effect = {
            GER_nww_refresh_industry = yes
        }
    }
    ai_will_do = {
        factor = 1
    }
}
```

### Концессии заморских предприятий — `GER_2`

EN: Overseas Enterprise Concessions.

Описание RU: Вложения в заморские предприятия увеличат добычу только в принадлежащих нам и контролируемых регионах. Коренное население сохраняет национальные территории; германские колониальные коры не добавляются.

Описание EN: Develop overseas rubber and chromium enterprises only in regions we actually own and control. Indigenous claims remain intact.

Источник: `common/national_focus/GER_focuses.txt:177`. Стоимость: 10 (70 дней). Координаты: x=57, y=2. Иконка: `GFX_focus_generic_resource_extraction`.

Предпосылки: (Торговые палаты Миттельевропы [GER_mitteleuropa_trade]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: GER_nww_freight_corridors.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- `add_resource`: type = rubber; amount = 8
- `add_resource`: type = chromium; amount = 6

Полное определение фокуса:

```pdx
focus = {
    id = GER_2
    x = 57
    y = 2
    cost = 10
    icon = GFX_focus_generic_resource_extraction
    prerequisite = {
        focus = GER_mitteleuropa_trade
    }
    available_if_capitulated = no
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    completion_reward = {
        546 = {
            if = {
                limit = {
                    is_owned_and_controlled_by = ROOT
                }
                add_resource = {
                    type = rubber
                    amount = 8
                }
            }
        }
        541 = {
            if = {
                limit = {
                    is_owned_and_controlled_by = ROOT
                }
                add_resource = {
                    type = chromium
                    amount = 6
                }
            }
        }
        hidden_effect = {
            GER_nww_refresh_industry = yes
        }
    }
    ai_will_do = {
        factor = 1
    }
}
```

### Связи с богемскими автономистами — `GER_nww_prague_network`

EN: Contacts with Bohemian Autonomists.

Описание RU: Разведка установит контакты с богемскими автономистами. При наличии La Résistance в агентстве откроется операция против Австрии: каждое завершение даёт +2 к напряжённости и учитывается как немецкий вклад.

Описание EN: Intelligence contacts with Bohemian autonomists unlock an agency operation against Austria with La Resistance. Each completion adds two tension and counts toward German influence.

Источник: `common/national_focus/GER_focuses.txt:904`. Стоимость: 5 (35 дней). Координаты: x=45, y=3. Иконка: `GFX_focus_generic_secret_agent_operative`.

Предпосылки: (GER_guardians_of_the_reich [GER_guardians_of_the_reich]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: нет.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- `add_political_power`: 50

Полное определение фокуса:

```pdx
focus = {
    id = GER_nww_prague_network
    x = 45
    y = 3
    cost = 5
    icon = GFX_focus_generic_secret_agent_operative
    prerequisite = {
        focus = GER_guardians_of_the_reich
    }
    available_if_capitulated = no
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    completion_reward = {
        add_political_power = 50
        custom_effect_tooltip = GER_nww_bohemian_operation_unlock_tt
        hidden_effect = {
            GER_nww_refresh_industry = yes
        }
    }
    ai_will_do = {
        factor = 1
    }
}
```

### Энергетическая инфраструктура Рура — `GER_nww_energy_keystones`

EN: Ruhr Energy Infrastructure.

Описание RU: Построим энергетическую инфраструктуру в собственном контролируемом регионе, где её ещё нет. Используется инфраструктурный объект установленной версии игры.

Описание EN: Build an energy-infrastructure installation, prioritizing the Ruhr when eligible. The project requires an owned and controlled core region with room for the building.

Источник: `common/national_focus/GER_focuses.txt:804`. Стоимость: 10 (70 дней). Координаты: x=47, y=3. Иконка: `GFX_focus_generic_energy`.

Предпосылки: (Соединить региональные энергосистемы [GER_nww_electrical_grid]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: нет.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- Награда вызывает вспомогательные эффекты: см. completion_reward и раздел определений.

Полное определение фокуса:

```pdx
focus = {
    id = GER_nww_energy_keystones
    x = 47
    y = 3
    cost = 10
    icon = GFX_focus_generic_energy
    prerequisite = {
        focus = GER_nww_electrical_grid
    }
    available_if_capitulated = no
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    completion_reward = {
        GER_nww_build_energy_infrastructure = yes
        hidden_effect = {
            GER_nww_refresh_industry = yes
        }
    }
    ai_will_do = {
        factor = 1
    }
}
```

### Силезская металлургия — `GER_nww_silesian_steel`

EN: Silesian Steelworks.

Описание RU: Модернизация силезских домен даст сталь для станков, рельсов и вооружения. Награда предоставляется только при нашем владении и контроле над Силезией.

Описание EN: Modernize Silesian furnaces to supply steel for machinery, railways and armaments. The steel is added only while we own and control the region.

Источник: `common/national_focus/GER_focuses.txt:464`. Стоимость: 10 (70 дней). Координаты: x=49, y=3. Иконка: `GFX_focus_generic_steel_mill`.

Предпосылки: (Соединить региональные энергосистемы [GER_nww_electrical_grid]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: GER_3.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- `add_resource`: type = steel; amount = 8

Полное определение фокуса:

```pdx
focus = {
    id = GER_nww_silesian_steel
    x = 49
    y = 3
    cost = 10
    icon = GFX_focus_generic_steel_mill
    prerequisite = {
        focus = GER_nww_electrical_grid
    }
    available_if_capitulated = no
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    completion_reward = {
        67 = {
            if = {
                limit = {
                    is_owned_and_controlled_by = ROOT
                }
                add_resource = {
                    type = steel
                    amount = 8
                }
            }
        }
        hidden_effect = {
            GER_nww_refresh_industry = yes
        }
    }
    ai_will_do = {
        factor = 1
    }
}
```

### Культура точного производства — `GER_7`

EN: Precision Manufacturing.

Описание RU: Обучение мастеров и контроль качества дадут устойчивый рост производственной эффективности. Программа развивает общий промышленный дух.

Описание EN: Train master craftsmen and strengthen quality control to raise the production efficiency cap.

Источник: `common/national_focus/GER_focuses.txt:324`. Стоимость: 10 (70 дней). Координаты: x=53, y=3. Иконка: `GFX_focus_generic_industrial_experts`.

Предпосылки: (Промышленные облигации земель [GER_6]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: GER_nww_machine_tools.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- Параметр `GER_industry_maximum`: 0.05

Полное определение фокуса:

```pdx
focus = {
    id = GER_7
    x = 53
    y = 3
    cost = 10
    icon = GFX_focus_generic_industrial_experts
    prerequisite = {
        focus = GER_6
    }
    available_if_capitulated = no
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    completion_reward = {
        add_to_variable = {
            GER_industry_maximum = 0.05
            tooltip = GER_nww_industry_maximum_tt
        }
        hidden_effect = {
            GER_nww_refresh_industry = yes
        }
    }
    ai_will_do = {
        factor = 1
    }
}
```

### Грузовые коридоры империи — `GER_nww_freight_corridors`

EN: Imperial Freight Corridors.

Описание RU: Улучшим инфраструктуру двух собственных германских промышленных регионов. Заводы должны получать уголь и комплектующие до начала новой гонки вооружений.

Описание EN: Improve infrastructure twice in eligible owned and controlled German core regions so industry can receive coal and components.

Источник: `common/national_focus/GER_focuses.txt:606`. Стоимость: 10 (70 дней). Координаты: x=57, y=3. Иконка: `GFX_focus_generic_railroad`.

Предпосылки: (Концессии заморских предприятий [GER_2]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: GER_nww_merchant_contracts.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- Награда вызывает вспомогательные эффекты: см. completion_reward и раздел определений.

Полное определение фокуса:

```pdx
focus = {
    id = GER_nww_freight_corridors
    x = 57
    y = 3
    cost = 10
    icon = GFX_focus_generic_railroad
    prerequisite = {
        focus = GER_2
    }
    available_if_capitulated = no
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    completion_reward = {
        GER_nww_improve_infrastructure = yes
        hidden_effect = {
            GER_nww_refresh_industry = yes
        }
    }
    ai_will_do = {
        factor = 1
    }
}
```

### Восточные промышленные заказы — `GER_3`

EN: Eastern Industrial Orders.

Описание RU: Государственные заказы поддержат оборонные предприятия германских земель. Заводы строятся на собственных контролируемых национальных территориях.

Описание EN: State orders support new military production on owned and controlled German core territory.

Источник: `common/national_focus/GER_focuses.txt:221`. Стоимость: 10 (70 дней). Координаты: x=49, y=4. Иконка: `GFX_focus_generic_military_industry`.

Предпосылки: (Силезская металлургия [GER_nww_silesian_steel]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: GER_nww_arsenal_contracts.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- Награда вызывает вспомогательные эффекты: см. completion_reward и раздел определений.

Полное определение фокуса:

```pdx
focus = {
    id = GER_3
    x = 49
    y = 4
    cost = 10
    icon = GFX_focus_generic_military_industry
    prerequisite = {
        focus = GER_nww_silesian_steel
    }
    available_if_capitulated = no
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    completion_reward = {
        GER_nww_build_military = yes
        hidden_effect = {
            GER_nww_refresh_industry = yes
        }
    }
    ai_will_do = {
        factor = 1
    }
}
```

### Станкостроительная кооперация — `GER_nww_machine_tools`

EN: Machine Tool Cooperation.

Описание RU: Машиностроительные фирмы согласуют выпуск станков, оснастки и запасных частей. Это ускорит развёртывание новых производственных линий.

Описание EN: Coordinate machine tools, fixtures and spare parts to speed the development of new production lines and industrial technology.

Источник: `common/national_focus/GER_focuses.txt:523`. Стоимость: 10 (70 дней). Координаты: x=53, y=4. Иконка: `GFX_focus_generic_mass_production`.

Предпосылки: (Культура точного производства [GER_7]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: GER_nww_industrial_standards, GER_nww_electromechanical_labs.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- `add_tech_bonus`: category = industry; uses = 1; bonus = 0.5
- Параметр `GER_industry_efficiency`: 0.05

Полное определение фокуса:

```pdx
focus = {
    id = GER_nww_machine_tools
    x = 53
    y = 4
    cost = 10
    icon = GFX_focus_generic_mass_production
    prerequisite = {
        focus = GER_7
    }
    available_if_capitulated = no
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    completion_reward = {
        add_tech_bonus = {
            category = industry
            uses = 1
            bonus = 0.5
        }
        add_to_variable = {
            GER_industry_efficiency = 0.05
            tooltip = GER_nww_industry_efficiency_tt
        }
        hidden_effect = {
            GER_nww_refresh_industry = yes
        }
    }
    ai_will_do = {
        factor = 1
    }
}
```

### Контракты торгового флота — `GER_nww_merchant_contracts`

EN: Merchant Shipping Contracts.

Описание RU: Долгосрочные контракты дадут торговому флоту транспорты для устойчивых поставок между метрополией и заморскими владениями.

Описание EN: Long-term shipping contracts supply twenty convoys for trade between the metropole and overseas possessions.

Источник: `common/national_focus/GER_focuses.txt:629`. Стоимость: 10 (70 дней). Координаты: x=57, y=4. Иконка: `GFX_focus_generic_merchant_fleet`.

Предпосылки: (Грузовые коридоры империи [GER_nww_freight_corridors]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: GER_nww_export_credit.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- Награда вызывает вспомогательные эффекты: см. completion_reward и раздел определений.

Полное определение фокуса:

```pdx
focus = {
    id = GER_nww_merchant_contracts
    x = 57
    y = 4
    cost = 10
    icon = GFX_focus_generic_merchant_fleet
    prerequisite = {
        focus = GER_nww_freight_corridors
    }
    available_if_capitulated = no
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    completion_reward = {
        add_equipment_to_stockpile = {
            type = convoy
            amount = 20
            producer = GER
        }
        hidden_effect = {
            GER_nww_refresh_industry = yes
        }
    }
    ai_will_do = {
        factor = 1
    }
}
```

### Долгосрочные контракты арсеналов — `GER_nww_arsenal_contracts`

EN: Long-Term Arsenal Contracts.

Описание RU: Вместо чрезвычайных займов арсеналы получат предсказуемые многолетние заказы. Это повышает выпуск уже существующих военных заводов.

Описание EN: Give arsenals predictable long-term contracts, improving the output of existing military factories.

Источник: `common/national_focus/GER_focuses.txt:497`. Стоимость: 10 (70 дней). Координаты: x=49, y=5. Иконка: `GFX_focus_generic_arms_trade`.

Предпосылки: (Восточные промышленные заказы [GER_3]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: GER_4.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- Параметр `GER_industry_output`: 0.05

Полное определение фокуса:

```pdx
focus = {
    id = GER_nww_arsenal_contracts
    x = 49
    y = 5
    cost = 10
    icon = GFX_focus_generic_arms_trade
    prerequisite = {
        focus = GER_3
    }
    available_if_capitulated = no
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    completion_reward = {
        add_to_variable = {
            GER_industry_output = 0.05
            tooltip = GER_nww_industry_output_tt
        }
        hidden_effect = {
            GER_nww_refresh_industry = yes
        }
    }
    ai_will_do = {
        factor = 1
    }
}
```

### Общегерманские технические нормы — `GER_nww_industrial_standards`

EN: National Technical Standards.

Описание RU: Унификация деталей и производственных норм позволит совместить разработки частных фирм с государственными заказами.

Описание EN: Common technical standards integrate private designs with public orders, raising the production efficiency cap.

Источник: `common/national_focus/GER_focuses.txt:554`. Стоимость: 10 (70 дней). Координаты: x=53, y=5. Иконка: `GFX_focus_generic_improve_the_administration_2`.

Предпосылки: (Станкостроительная кооперация [GER_nww_machine_tools]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: GER_nww_technical_colleges.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- Параметр `GER_industry_maximum`: 0.05

Полное определение фокуса:

```pdx
focus = {
    id = GER_nww_industrial_standards
    x = 53
    y = 5
    cost = 10
    icon = GFX_focus_generic_improve_the_administration_2
    prerequisite = {
        focus = GER_nww_machine_tools
    }
    available_if_capitulated = no
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    completion_reward = {
        add_to_variable = {
            GER_industry_maximum = 0.05
            tooltip = GER_nww_industry_maximum_tt
        }
        hidden_effect = {
            GER_nww_refresh_industry = yes
        }
    }
    ai_will_do = {
        factor = 1
    }
}
```

### Электромеханические лаборатории — `GER_nww_electromechanical_labs`

EN: Electromechanical Laboratories.

Описание RU: Электромеханика и связь дадут основу для следующего поколения промышленного оборудования. Гражданское применение технологий предшествует массовому перевооружению.

Описание EN: Electromechanical laboratories support electronics research and the development of industrial communications.

Источник: `common/national_focus/GER_focuses.txt:850`. Стоимость: 10 (70 дней). Координаты: x=55, y=5. Иконка: `GFX_goal_generic_radar`.

Предпосылки: (Станкостроительная кооперация [GER_nww_machine_tools]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: нет.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- `add_tech_bonus`: category = electronics; uses = 1; bonus = 0.5

Полное определение фокуса:

```pdx
focus = {
    id = GER_nww_electromechanical_labs
    x = 55
    y = 5
    cost = 10
    icon = GFX_goal_generic_radar
    prerequisite = {
        focus = GER_nww_machine_tools
    }
    available_if_capitulated = no
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    completion_reward = {
        add_tech_bonus = {
            category = electronics
            uses = 1
            bonus = 0.5
        }
        hidden_effect = {
            GER_nww_refresh_industry = yes
        }
    }
    ai_will_do = {
        factor = 1
    }
}
```

### Экспортное кредитование — `GER_nww_export_credit`

EN: Export Credit.

Описание RU: Государственные гарантии экспортных контрактов поддержат гражданские предприятия. Торговля станет подготовкой к переговорам, а не поводом для немедленной войны.

Описание EN: Export guarantees support another civilian enterprise. Trade prepares the ground for diplomacy rather than an immediate war.

Источник: `common/national_focus/GER_focuses.txt:656`. Стоимость: 10 (70 дней). Координаты: x=57, y=5. Иконка: `GFX_goal_generic_positive_trade_relations`.

Предпосылки: (Контракты торгового флота [GER_nww_merchant_contracts]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: GER_nww_investment_guarantees.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- Награда вызывает вспомогательные эффекты: см. completion_reward и раздел определений.

Полное определение фокуса:

```pdx
focus = {
    id = GER_nww_export_credit
    x = 57
    y = 5
    cost = 10
    icon = GFX_goal_generic_positive_trade_relations
    prerequisite = {
        focus = GER_nww_merchant_contracts
    }
    available_if_capitulated = no
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    completion_reward = {
        GER_nww_build_civilian = yes
        hidden_effect = {
            GER_nww_refresh_industry = yes
        }
    }
    ai_will_do = {
        factor = 1
    }
}
```

### Единые стандарты вооружения — `GER_4`

EN: Common Armament Standards.

Описание RU: Единые допуски и взаимозаменяемые детали ускорят освоение серийного оружия. Военные технологии опираются на развитие станочного производства.

Описание EN: Common tolerances and interchangeable parts improve production efficiency growth and support infantry weapon research.

Источник: `common/national_focus/GER_focuses.txt:244`. Стоимость: 10 (70 дней). Координаты: x=49, y=6. Иконка: `GFX_goal_generic_small_arms`.

Предпосылки: (Долгосрочные контракты арсеналов [GER_nww_arsenal_contracts]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: GER_8.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- `add_tech_bonus`: category = infantry_weapons; uses = 1; bonus = 0.5
- Параметр `GER_industry_efficiency`: 0.05

Полное определение фокуса:

```pdx
focus = {
    id = GER_4
    x = 49
    y = 6
    cost = 10
    icon = GFX_goal_generic_small_arms
    prerequisite = {
        focus = GER_nww_arsenal_contracts
    }
    available_if_capitulated = no
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    completion_reward = {
        add_tech_bonus = {
            category = infantry_weapons
            uses = 1
            bonus = 0.5
        }
        add_to_variable = {
            GER_industry_efficiency = 0.05
            tooltip = GER_nww_industry_efficiency_tt
        }
        hidden_effect = {
            GER_nww_refresh_industry = yes
        }
    }
    ai_will_do = {
        factor = 1
    }
}
```

### Технические училища земель — `GER_nww_technical_colleges`

EN: State Technical Colleges.

Описание RU: Инженерные школы подготовят специалистов для заводов и лабораторий. Их постоянный вклад выражается в общем промышленном духе.

Описание EN: Technical colleges train engineers and laboratory staff, providing a lasting research bonus.

Источник: `common/national_focus/GER_focuses.txt:580`. Стоимость: 10 (70 дней). Координаты: x=53, y=6. Иконка: `GFX_focus_generic_education`.

Предпосылки: (Общегерманские технические нормы [GER_nww_industrial_standards]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: GER_8.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- Параметр `GER_industry_research`: 0.05

Полное определение фокуса:

```pdx
focus = {
    id = GER_nww_technical_colleges
    x = 53
    y = 6
    cost = 10
    icon = GFX_focus_generic_education
    prerequisite = {
        focus = GER_nww_industrial_standards
    }
    available_if_capitulated = no
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    completion_reward = {
        add_to_variable = {
            GER_industry_research = 0.05
            tooltip = GER_nww_industry_research_tt
        }
        hidden_effect = {
            GER_nww_refresh_industry = yes
        }
    }
    ai_will_do = {
        factor = 1
    }
}
```

### Гарантии долгосрочных вложений — `GER_nww_investment_guarantees`

EN: Long-Term Investment Guarantees.

Описание RU: Прозрачные гарантии заказов завершают инвестиционную программу земель. Рост строительства не требует запуска ванильной экономики завоеваний.

Описание EN: Predictable procurement completes the states investment program and permanently improves construction speed.

Источник: `common/national_focus/GER_focuses.txt:679`. Стоимость: 10 (70 дней). Координаты: x=57, y=6. Иконка: `GFX_focus_generic_currency_reforms`.

Предпосылки: (Экспортное кредитование [GER_nww_export_credit]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: GER_nww_synthetic_fuels.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- Параметр `GER_industry_construction`: 0.05

Полное определение фокуса:

```pdx
focus = {
    id = GER_nww_investment_guarantees
    x = 57
    y = 6
    cost = 10
    icon = GFX_focus_generic_currency_reforms
    prerequisite = {
        focus = GER_nww_export_credit
    }
    available_if_capitulated = no
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    completion_reward = {
        add_to_variable = {
            GER_industry_construction = 0.05
            tooltip = GER_nww_industry_construction_tt
        }
        hidden_effect = {
            GER_nww_refresh_industry = yes
        }
    }
    ai_will_do = {
        factor = 1
    }
}
```

### Согласовать промышленную программу — `GER_8`

EN: Coordinate the Industrial Program.

Описание RU: Военная стандартизация и гражданские технические школы должны сойтись в общей исследовательской программе. Дополнительная ячейка предоставляется только до пяти исследовательских ячеек.

Описание EN: Bring military standardization and technical education together. An additional research slot is granted only below five slots.

Источник: `common/national_focus/GER_focuses.txt:350`. Стоимость: 10 (70 дней). Координаты: x=51, y=7. Иконка: `GFX_focus_research2`.

Предпосылки: (Единые стандарты вооружения [GER_4]) И (Технические училища земель [GER_nww_technical_colleges]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: GER_9, GER_10.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- `add_research_slot`: 1

Полное определение фокуса:

```pdx
focus = {
    id = GER_8
    x = 51
    y = 7
    cost = 10
    icon = GFX_focus_research2
    prerequisite = {
        focus = GER_4
    }
    prerequisite = {
        focus = GER_nww_technical_colleges
    }
    available_if_capitulated = no
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    completion_reward = {
        if = {
            limit = {
                amount_research_slots < 5
            }
            add_research_slot = 1
        }
        hidden_effect = {
            GER_nww_refresh_industry = yes
        }
    }
    ai_will_do = {
        factor = 1
    }
}
```

### Синтетическое топливо из угля — `GER_nww_synthetic_fuels`

EN: Coal-Based Synthetic Fuels.

Описание RU: Разовьём синтетическую переработку в собственном промышленном регионе. Топливная безопасность дополняет, но не заменяет энергетическую систему угля и сетей.

Описание EN: Build a synthetic refinery in an eligible domestic core region. Fuel security complements coal extraction and the electrical grid.

Источник: `common/national_focus/GER_focuses.txt:758`. Стоимость: 10 (70 дней). Координаты: x=57, y=7. Иконка: `GFX_goal_generic_oil_refinery`.

Предпосылки: (Гарантии долгосрочных вложений [GER_nww_investment_guarantees]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: GER_nww_colonial_ports.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- Награда вызывает вспомогательные эффекты: см. completion_reward и раздел определений.

Полное определение фокуса:

```pdx
focus = {
    id = GER_nww_synthetic_fuels
    x = 57
    y = 7
    cost = 10
    icon = GFX_goal_generic_oil_refinery
    prerequisite = {
        focus = GER_nww_investment_guarantees
    }
    available_if_capitulated = no
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    completion_reward = {
        GER_nww_build_refinery = yes
        hidden_effect = {
            GER_nww_refresh_industry = yes
        }
    }
    ai_will_do = {
        factor = 1
    }
}
```

### Арсеналы нового поколения — `GER_9`

EN: Next-Generation Arsenals.

Описание RU: Новые военные предприятия опираются на уже подготовленную производственную и инженерную базу. Это завершение подготовки, а не ранний скачок к массовой агрессии.

Описание EN: New military factories and improved output build on the completed industrial and engineering program.

Источник: `common/national_focus/GER_focuses.txt:381`. Стоимость: 10 (70 дней). Координаты: x=49, y=8. Иконка: `GFX_focus_generic_tank_production`.

Предпосылки: (Согласовать промышленную программу [GER_8]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: GER_nww_industrial_research.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- Параметр `GER_industry_output`: 0.05

Полное определение фокуса:

```pdx
focus = {
    id = GER_9
    x = 49
    y = 8
    cost = 10
    icon = GFX_focus_generic_tank_production
    prerequisite = {
        focus = GER_8
    }
    available_if_capitulated = no
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    completion_reward = {
        GER_nww_build_military = yes
        add_to_variable = {
            GER_industry_output = 0.05
            tooltip = GER_nww_industry_output_tt
        }
        hidden_effect = {
            GER_nww_refresh_industry = yes
        }
    }
    ai_will_do = {
        factor = 1
    }
}
```

### Автоматизация оружейных линий — `GER_10`

EN: Automated Armament Lines.

Описание RU: Внедрим автоматическую оснастку в оружейное производство. Бонус исследований не выдаёт технологии другой эпохи напрямую.

Описание EN: Automatic tooling supports infantry weapon research without directly granting technologies from a later era.

Источник: `common/national_focus/GER_focuses.txt:408`. Стоимость: 10 (70 дней). Координаты: x=53, y=8. Иконка: `GFX_goal_generic_production2`.

Предпосылки: (Согласовать промышленную программу [GER_8]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: GER_nww_industrial_research.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- `add_tech_bonus`: category = infantry_weapons; uses = 1; bonus = 0.5

Полное определение фокуса:

```pdx
focus = {
    id = GER_10
    x = 53
    y = 8
    cost = 10
    icon = GFX_goal_generic_production2
    prerequisite = {
        focus = GER_8
    }
    available_if_capitulated = no
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    completion_reward = {
        add_tech_bonus = {
            category = infantry_weapons
            uses = 1
            bonus = 0.5
        }
        hidden_effect = {
            GER_nww_refresh_industry = yes
        }
    }
    ai_will_do = {
        factor = 1
    }
}
```

### Складские узлы заморских портов — `GER_nww_colonial_ports`

EN: Overseas Port Warehouses.

Описание RU: Складские и перерабатывающие мощности поддержат заморские перевозки. Программа не передаёт чужие территории и не создаёт германские колониальные коры.

Описание EN: Expand civilian storage and processing capacity for overseas shipping without transferring territory or creating colonial cores.

Источник: `common/national_focus/GER_focuses.txt:781`. Стоимость: 10 (70 дней). Координаты: x=57, y=8. Иконка: `GFX_goal_generic_construction`.

Предпосылки: (Синтетическое топливо из угля [GER_nww_synthetic_fuels]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: GER_nww_supply_resilience.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- Награда вызывает вспомогательные эффекты: см. completion_reward и раздел определений.

Полное определение фокуса:

```pdx
focus = {
    id = GER_nww_colonial_ports
    x = 57
    y = 8
    cost = 10
    icon = GFX_goal_generic_construction
    prerequisite = {
        focus = GER_nww_synthetic_fuels
    }
    available_if_capitulated = no
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    completion_reward = {
        GER_nww_build_civilian = yes
        hidden_effect = {
            GER_nww_refresh_industry = yes
        }
    }
    ai_will_do = {
        factor = 1
    }
}
```

### Имперское исследовательское объединение — `GER_nww_industrial_research`

EN: Imperial Research Association.

Описание RU: Университеты, арсеналы и частные лаборатории объединят прикладные программы. Результат сохраняется в общем промышленном духе.

Описание EN: Unite universities, arsenals and private laboratories in applied research, improving the lasting industrial program.

Источник: `common/national_focus/GER_focuses.txt:705`. Стоимость: 10 (70 дней). Координаты: x=51, y=9. Иконка: `GFX_focus_generic_university_3`.

Предпосылки: (Арсеналы нового поколения [GER_9]) И (Автоматизация оружейных линий [GER_10]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: GER_nww_balanced_orders.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- Параметр `GER_industry_research`: 0.05

Полное определение фокуса:

```pdx
focus = {
    id = GER_nww_industrial_research
    x = 51
    y = 9
    cost = 10
    icon = GFX_focus_generic_university_3
    prerequisite = {
        focus = GER_9
    }
    prerequisite = {
        focus = GER_10
    }
    available_if_capitulated = no
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    completion_reward = {
        add_to_variable = {
            GER_industry_research = 0.05
            tooltip = GER_nww_industry_research_tt
        }
        hidden_effect = {
            GER_nww_refresh_industry = yes
        }
    }
    ai_will_do = {
        factor = 1
    }
}
```

### Устойчивые цепочки поставок — `GER_nww_supply_resilience`

EN: Resilient Supply Chains.

Описание RU: Резерв локомотивов и согласованные контракты укрепят снабжение. Программа создаёт реальный транспорт, не заменяя его абстрактной наградой людскими ресурсами.

Описание EN: Provide twenty locomotives to support resilient supply chains and reliable freight transport.

Источник: `common/national_focus/GER_focuses.txt:877`. Стоимость: 10 (70 дней). Координаты: x=55, y=9. Иконка: `GFX_focus_generic_supply_line`.

Предпосылки: (Складские узлы заморских портов [GER_nww_colonial_ports]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: нет.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- Награда вызывает вспомогательные эффекты: см. completion_reward и раздел определений.

Полное определение фокуса:

```pdx
focus = {
    id = GER_nww_supply_resilience
    x = 55
    y = 9
    cost = 10
    icon = GFX_focus_generic_supply_line
    prerequisite = {
        focus = GER_nww_colonial_ports
    }
    available_if_capitulated = no
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    completion_reward = {
        add_equipment_to_stockpile = {
            type = train_equipment_1
            amount = 20
            producer = GER
        }
        hidden_effect = {
            GER_nww_refresh_industry = yes
        }
    }
    ai_will_do = {
        factor = 1
    }
}
```

### Сбалансированная система заказов — `GER_nww_balanced_orders`

EN: Balanced Procurement.

Описание RU: Гражданские и военные предприятия получают сбалансированную программу заказов. Имперская промышленность должна выдержать длительное напряжение без долговых миссий.

Описание EN: Balance civilian and military orders by building one enterprise of each kind on owned and controlled German core territory.

Источник: `common/national_focus/GER_focuses.txt:734`. Стоимость: 10 (70 дней). Координаты: x=49, y=10. Иконка: `GFX_focus_generic_reorient_production`.

Предпосылки: (Имперское исследовательское объединение [GER_nww_industrial_research]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: нет.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- Награда вызывает вспомогательные эффекты: см. completion_reward и раздел определений.

Полное определение фокуса:

```pdx
focus = {
    id = GER_nww_balanced_orders
    x = 49
    y = 10
    cost = 10
    icon = GFX_focus_generic_reorient_production
    prerequisite = {
        focus = GER_nww_industrial_research
    }
    available_if_capitulated = no
    search_filters = {
        FOCUS_FILTER_INDUSTRY
    }
    completion_reward = {
        GER_nww_build_civilian = yes
        GER_nww_build_military = yes
        hidden_effect = {
            GER_nww_refresh_industry = yes
        }
    }
    ai_will_do = {
        factor = 1
    }
}
```

## Прочие военные и государственные фокусы — 5

### GER_the_kaiser_endures — `GER_the_kaiser_endures`

EN: The Kaiser Endures.

Описание RU: Укрепим государственные и производственные учреждения империи.

Описание EN: Strengthen the imperial institutions and production system.

Источник: `common/national_focus/GER_focuses.txt:13`. Стоимость: 5 (35 дней). Координаты: x=43, y=0. Иконка: `GFX_focus_generic_diplomatic_treaty`.

Предпосылки: нет нарисованной предпосылки; см. available.

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: GER_prussian_traditions, GER_guardians_of_the_reich.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- `add_political_power`: 120
- `add_stability`: 0.05

Полное определение фокуса:

```pdx
focus = {
    id = GER_the_kaiser_endures
    icon = GFX_focus_generic_diplomatic_treaty
    cost = 5
    completion_reward = {
        add_political_power = 120
        add_stability = 0.05
    }
    y = 0
    x = 43
}
```

### GER_the_fleet_question — `GER_the_fleet_question`

EN: The Fleet Question.

Описание RU: Укрепим государственные и производственные учреждения империи.

Описание EN: Strengthen the imperial institutions and production system.

Источник: `common/national_focus/GER_focuses.txt:66`. Стоимость: 5 (35 дней). Координаты: x=61, y=0. Иконка: `GFX_focus_generic_diplomatic_treaty`.

Предпосылки: нет нарисованной предпосылки; см. available.

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: нет.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- `navy_experience`: 15

Полное определение фокуса:

```pdx
focus = {
    id = GER_the_fleet_question
    icon = GFX_focus_generic_diplomatic_treaty
    cost = 5
    y = 0
    completion_reward = {
        add_doctrine_cost_reduction = {
            name = NWW_legacy_naval_doctrine_bonus
            category = naval_doctrine
            uses = 1
            cost_reduction = 0.5
        }
        navy_experience = 15
    }
    x = 61
}
```

### GER_prussian_traditions — `GER_prussian_traditions`

EN: Prussian Traditions.

Описание RU: Укрепим государственные и производственные учреждения империи.

Описание EN: Strengthen the imperial institutions and production system.

Источник: `common/national_focus/GER_focuses.txt:24`. Стоимость: 5 (35 дней). Координаты: x=41, y=1. Иконка: `GFX_focus_generic_army_attack`.

Предпосылки: (GER_the_kaiser_endures [GER_the_kaiser_endures]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: GER_the_eastern_question.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- `army_experience`: 25
- `add_war_support`: 0.05

Полное определение фокуса:

```pdx
focus = {
    id = GER_prussian_traditions
    icon = GFX_focus_generic_army_attack
    prerequisite = {
        focus = GER_the_kaiser_endures
    }
    cost = 5
    completion_reward = {
        army_experience = 25
        add_war_support = 0.05
    }
    y = 1
    x = 41
}
```

### GER_guardians_of_the_reich — `GER_guardians_of_the_reich`

EN: Guardians Of The Reich.

Описание RU: Укрепим государственные и производственные учреждения империи.

Описание EN: Strengthen the imperial institutions and production system.

Источник: `common/national_focus/GER_focuses.txt:124`. Стоимость: 5 (35 дней). Координаты: x=45, y=1. Иконка: `GFX_focus_generic_manpower`.

Предпосылки: (GER_the_kaiser_endures [GER_the_kaiser_endures]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): GER_mitteleuropa_trade, GER_the_eastern_question.

Прямые продолжения: GER_nww_prague_network.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- `add_manpower`: 100000
- `add_stability`: 0.05

Полное определение фокуса:

```pdx
focus = {
    id = GER_guardians_of_the_reich
    icon = GFX_focus_generic_manpower
    prerequisite = {
        focus = GER_the_kaiser_endures
    }
    available = {
        OR = {
            has_completed_focus = GER_mitteleuropa_trade
            has_completed_focus = GER_the_eastern_question
        }
    }
    cost = 5
    completion_reward = {
        add_manpower = 100000
        add_stability = 0.05
    }
    y = 1
    x = 45
}
```

### GER_the_eastern_question — `GER_the_eastern_question`

EN: The Eastern Question.

Описание RU: Укрепим государственные и производственные учреждения империи.

Описание EN: Strengthen the imperial institutions and production system.

Источник: `common/national_focus/GER_focuses.txt:105`. Стоимость: 10 (70 дней). Координаты: x=41, y=2. Иконка: `GFX_focus_generic_army_doctrines_2`.

Предпосылки: (GER_prussian_traditions [GER_prussian_traditions]).

Взаимоисключения: нет.

Дополнительные focus-gates в available (полная логика OR/NOT ниже): нет.

Прямые продолжения: нет.

Обзор возможной награды; условия и области действия сохранены в полном коде:

- `add_manpower`: 50000
- `add_war_support`: 0.1

Полное определение фокуса:

```pdx
focus = {
    id = GER_the_eastern_question
    icon = GFX_focus_generic_army_doctrines_2
    prerequisite = {
        focus = GER_prussian_traditions
    }
    cost = 10
    completion_reward = {
        add_manpower = 50000
        add_equipment_to_stockpile = {
            type = infantry_equipment_1
            amount = 2000
            producer = GER
        }
        add_war_support = 0.1
    }
    y = 2
    x = 41
}
```

## Настройка дерева и непрерывных фокусов

```pdx
focus_tree = {
    id = GER_focus
    country = {
        factor = 0
        modifier = {
            add = 100
            tag = GER
        }
    }
    default = no
    shared_focus = GER_the_gilded_colossus
    initial_show_position = {
        focus = GER_the_gilded_colossus
    }
    continuous_focus_position = {
        x = 100
        y = 3000
    }
}
```

## Связанные системы Германии

Стартовые и автоматические эффекты приведены как контекст; их нельзя считать наградой каждого фокуса.

### `common/bop/GER_bop.txt`

```pdx
GER_kaiser_vs_reichstag = {
    initial_value = 0
    left_side = GER_ohl_and_crown_side
    right_side = GER_reichstag_side
    decision_category = GER_bop_decisions_category
    range = {
        id = GER_bop_balanced
        min = -0.45
        max = 0.45
        modifier = {
            political_power_gain = 0.10
        }
    }
    side = {
        id = GER_ohl_and_crown_side
        icon = GFX_focus_GER_prussian_legacy
        range = {
            id = GER_bop_total_ohl
            min = -1
            max = -0.80
            modifier = {
                army_attack_factor = 0.15
                stability_factor = -0.20
                political_power_gain = -0.15
            }
        }
        range = {
            id = GER_bop_ohl_leaning
            min = -0.80
            max = -0.55
            modifier = {
                army_attack_factor = 0.05
                stability_factor = -0.10
            }
        }
        range = {
            id = GER_bop_ohl_influence
            min = -0.55
            max = -0.45
            modifier = {

            }
        }
    }
    side = {
        id = GER_reichstag_side
        icon = GFX_focus_GER_monarchy_compromise
        range = {
            id = GER_bop_reichstag_influence
            min = 0.45
            max = 0.55
            modifier = {

            }
        }
        range = {
            id = GER_bop_reichstag_leaning
            min = 0.55
            max = 0.80
            modifier = {
                stability_factor = 0.10
                industrial_capacity_factory = 0.05
            }
        }
        range = {
            id = GER_bop_total_reichstag
            min = 0.80
            max = 1
            modifier = {
                stability_factor = 0.20
                political_power_gain = 0.25
                army_org_factor = -0.10
                planning_speed = -0.15
            }
        }
    }
}
```

### `common/decisions/GER_bop_decisions.txt`

```pdx
GER_bop_decisions_category = {
    GER_consult_the_general_staff = {
        icon = GFX_focus_GER_prussian_legacy
        cost = 50
        days_re_enable = 30
        visible = {
            has_power_balance = {
                id = GER_kaiser_vs_reichstag
            }
            NOT = {
                has_country_flag = ger_bop_frozen
            }
        }
        available = {
            NOT = {
                has_country_flag = ger_bop_frozen
            }
            power_balance_value = {
                id = GER_kaiser_vs_reichstag
                value > -1
            }
        }
        complete_effect = {
            if = {
                limit = {
                    NOT = {
                        has_country_flag = ger_bop_frozen
                    }
                }
                add_power_balance_value = {
                    id = GER_kaiser_vs_reichstag
                    value = -0.10
                    tooltip_side = GER_ohl_and_crown_side
                }
                add_popularity = {
                    ideology = neutrality
                    popularity = 0.05
                }
            }
            else = {
                add_political_power = 50
            }
        }
        ai_will_do = {
            factor = 1
            modifier = {
                factor = 0
                power_balance_value = {
                    id = GER_kaiser_vs_reichstag
                    value < -0.20
                }
            }
        }
    }
    GER_concede_to_parliament = {
        icon = GFX_focus_GER_monarchy_compromise
        cost = 50
        days_re_enable = 30
        visible = {
            has_power_balance = {
                id = GER_kaiser_vs_reichstag
            }
            NOT = {
                has_country_flag = ger_bop_frozen
            }
        }
        available = {
            NOT = {
                has_country_flag = ger_bop_frozen
            }
            power_balance_value = {
                id = GER_kaiser_vs_reichstag
                value < 1
            }
        }
        complete_effect = {
            if = {
                limit = {
                    NOT = {
                        has_country_flag = ger_bop_frozen
                    }
                }
                add_power_balance_value = {
                    id = GER_kaiser_vs_reichstag
                    value = 0.10
                    tooltip_side = GER_reichstag_side
                }
                add_popularity = {
                    ideology = democratic
                    popularity = 0.05
                }
            }
            else = {
                add_political_power = 50
            }
        }
        ai_will_do = {
            factor = 0
        }
    }
    GER_rally_pan_german_leagues = {
        icon = GFX_focus_GER_brothers_in_arms
        cost = 50
        days_re_enable = 30
        visible = {
            has_completed_focus = GER_pan_german_leagues
            nww_GER_no_political_path = yes
        }
        available = {
            nww_GER_no_political_path = yes
            NOT = {
                fascism > 0.90
            }
        }
        complete_effect = {
            if = {
                limit = {
                    nww_GER_no_political_path = yes
                }
                add_popularity = {
                    ideology = fascism
                    popularity = 0.10
                }
            }
            else = {
                add_political_power = 50
            }
        }
        ai_will_do = {
            factor = 1
            modifier = {
                factor = 0
                is_historical_focus_on = yes
            }
        }
    }
    GER_organize_workers_councils = {
        icon = GFX_focus_GER_legacy_of_the_spartacus_league
        cost = 50
        days_re_enable = 30
        visible = {
            has_completed_focus = GER_organize_ruhr_workers
            nww_GER_no_political_path = yes
        }
        available = {
            nww_GER_no_political_path = yes
            NOT = {
                communism > 0.90
            }
        }
        complete_effect = {
            if = {
                limit = {
                    nww_GER_no_political_path = yes
                }
                add_popularity = {
                    ideology = communism
                    popularity = 0.10
                }
            }
            else = {
                add_political_power = 50
            }
        }
        ai_will_do = {
            factor = 1
            modifier = {
                factor = 0
                is_historical_focus_on = yes
            }
        }
    }
    GER_imperial_field_exercises = {
        icon = generic_army_support
        cost = 60
        days_re_enable = 180
        visible = {
            has_power_balance = {
                id = GER_kaiser_vs_reichstag
            }
            NOT = {
                has_country_flag = ger_bop_frozen
            }
        }
        available = {
            has_power_balance = {
                id = GER_kaiser_vs_reichstag
            }
            NOT = {
                has_country_flag = ger_bop_frozen
            }
            power_balance_value = {
                id = GER_kaiser_vs_reichstag
                value > -1
            }
            NOT = {
                has_idea = GER_staff_manoeuvres
            }
        }
        complete_effect = {
            if = {
                limit = {
                    has_power_balance = {
                        id = GER_kaiser_vs_reichstag
                    }
                    NOT = {
                        has_country_flag = ger_bop_frozen
                    }
                    power_balance_value = {
                        id = GER_kaiser_vs_reichstag
                        value > -1
                    }
                    NOT = {
                        has_idea = GER_staff_manoeuvres
                    }
                }
                add_power_balance_value = {
                    id = GER_kaiser_vs_reichstag
                    value = -0.10
                    tooltip_side = GER_ohl_and_crown_side
                }
                add_stability = -0.05
                add_war_support = 0.05
                add_timed_idea = {
                    idea = GER_staff_manoeuvres
                    days = 120
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
    GER_reichstag_social_compact = {
        icon = generic_political_discourse
        cost = 50
        days_re_enable = 180
        visible = {
            has_power_balance = {
                id = GER_kaiser_vs_reichstag
            }
            NOT = {
                has_country_flag = ger_bop_frozen
            }
        }
        available = {
            has_power_balance = {
                id = GER_kaiser_vs_reichstag
            }
            NOT = {
                has_country_flag = ger_bop_frozen
            }
            power_balance_value = {
                id = GER_kaiser_vs_reichstag
                value < 1
            }
            NOT = {
                has_idea = GER_social_budget
            }
        }
        complete_effect = {
            if = {
                limit = {
                    has_power_balance = {
                        id = GER_kaiser_vs_reichstag
                    }
                    NOT = {
                        has_country_flag = ger_bop_frozen
                    }
                    power_balance_value = {
                        id = GER_kaiser_vs_reichstag
                        value < 1
                    }
                    NOT = {
                        has_idea = GER_social_budget
                    }
                }
                add_power_balance_value = {
                    id = GER_kaiser_vs_reichstag
                    value = 0.10
                    tooltip_side = GER_reichstag_side
                }
                add_stability = 0.05
                add_war_support = -0.05
                add_timed_idea = {
                    idea = GER_social_budget
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
    GER_publish_military_audit = {
        icon = generic_political_discourse
        cost = 35
        days_re_enable = 150
        visible = {
            has_power_balance = {
                id = GER_kaiser_vs_reichstag
            }
            NOT = {
                has_country_flag = ger_bop_frozen
            }
        }
        available = {
            has_power_balance = {
                id = GER_kaiser_vs_reichstag
            }
            NOT = {
                has_country_flag = ger_bop_frozen
            }
            power_balance_value = {
                id = GER_kaiser_vs_reichstag
                value < 1
            }
            NOT = {
                has_idea = GER_military_accounts
            }
        }
        complete_effect = {
            if = {
                limit = {
                    has_power_balance = {
                        id = GER_kaiser_vs_reichstag
                    }
                    NOT = {
                        has_country_flag = ger_bop_frozen
                    }
                    power_balance_value = {
                        id = GER_kaiser_vs_reichstag
                        value < 1
                    }
                    NOT = {
                        has_idea = GER_military_accounts
                    }
                }
                add_power_balance_value = {
                    id = GER_kaiser_vs_reichstag
                    value = 0.05
                    tooltip_side = GER_reichstag_side
                }
                add_stability = 0.05
                add_timed_idea = {
                    idea = GER_military_accounts
                    days = 90
                }
            }
            else = {
                add_political_power = 35
            }
        }
        ai_will_do = {
            factor = 0.5
        }
    }
    GER_mediate_crown_and_chamber = {
        icon = generic_political_discourse
        cost = 75
        days_re_enable = 180
        visible = {
            has_power_balance = {
                id = GER_kaiser_vs_reichstag
            }
            NOT = {
                has_country_flag = ger_bop_frozen
            }
        }
        available = {
            has_power_balance = {
                id = GER_kaiser_vs_reichstag
            }
            NOT = {
                has_country_flag = ger_bop_frozen
            }
            OR = {
                power_balance_value = {
                    id = GER_kaiser_vs_reichstag
                    value < -0.10
                }
                power_balance_value = {
                    id = GER_kaiser_vs_reichstag
                    value > 0.10
                }
            }
            NOT = {
                has_idea = GER_constitutional_truce
            }
        }
        complete_effect = {
            if = {
                limit = {
                    has_power_balance = {
                        id = GER_kaiser_vs_reichstag
                    }
                    NOT = {
                        has_country_flag = ger_bop_frozen
                    }
                    OR = {
                        power_balance_value = {
                            id = GER_kaiser_vs_reichstag
                            value < -0.10
                        }
                        power_balance_value = {
                            id = GER_kaiser_vs_reichstag
                            value > 0.10
                        }
                    }
                    NOT = {
                        has_idea = GER_constitutional_truce
                    }
                }
                if = {
                    limit = {
                        power_balance_value = {
                            id = GER_kaiser_vs_reichstag
                            value < 0
                        }
                    }
                    add_power_balance_value = {
                        id = GER_kaiser_vs_reichstag
                        value = 0.10
                        tooltip_side = GER_reichstag_side
                    }
                }
                else = {
                    add_power_balance_value = {
                        id = GER_kaiser_vs_reichstag
                        value = -0.10
                        tooltip_side = GER_ohl_and_crown_side
                    }
                }
                add_stability = 0.05
                add_war_support = -0.05
                add_timed_idea = {
                    idea = GER_constitutional_truce
                    days = 90
                }
            }
            else = {
                add_political_power = 75
            }
        }
        ai_will_do = {
            factor = 0.5
        }
    }
}
```

### `common/decisions/categories/GER_categories.txt`

```pdx
GER_bop_decisions_category = {
    icon = GFX_focus_GER_our_place_in_the_sun
    allowed = {
        original_tag = GER
    }
    visible = {
        has_focus_tree = GER_focus
    }
}
```

### `common/ideas/GER_ideas.txt`

```pdx
ideas = {
    country = {
        GER_constitutional_monarchy = {
            picture = generic_flexible_foreign_policy
            allowed = {
                original_tag = GER
            }
            removal_cost = -1
            modifier = {
                stability_factor = 0.15
                political_power_gain = 0.20
            }
        }
        GER_arsenal_of_democracy = {
            picture = generic_army_war_college
            allowed = {
                original_tag = GER
            }
            removal_cost = -1
            modifier = {
                stability_factor = 0.15
                political_power_gain = 0.20
                industrial_capacity_factory = 0.20
                army_defence_factor = 0.10
            }
        }
        GER_the_new_reich = {
            picture = generic_artillery_regiments
            allowed = {
                original_tag = GER
            }
            removal_cost = -1
            modifier = {
                army_attack_factor = 0.15
                breakthrough_factor = 0.20
                army_speed_factor = 0.10
            }
        }
        GER_workers_militias = {
            picture = generic_reserve_divisions
            allowed = {
                original_tag = GER
            }
            removal_cost = -1
            modifier = {
                conscription = 0.05
                army_morale_factor = 0.10
            }
        }
        GER_imperial_overstretch = {
            picture = generic_oppression
            allowed = {
                original_tag = GER
            }
            removal_cost = -1
            modifier = {
                political_power_gain = -0.25
                consumer_goods_factor = 0.30
                war_support_factor = -0.30
                army_org_factor = -0.20
                training_time_army_factor = 0.40
                planning_speed = -0.30
            }
        }
        GER_master_of_mitteleuropa = {
            picture = generic_flexible_foreign_policy
            allowed = {
                original_tag = GER
            }
            removal_cost = -1
            modifier = {
                trade_laws_cost_factor = -0.20
                master_ideology_drift = 0.05
            }
        }
        GER_prussian_martial_spirit = {
            picture = generic_artillery_regiments
            allowed = {
                original_tag = GER
            }
            removal_cost = -1
            modifier = {
                army_org_factor = 0.10
                planning_speed = 0.15
            }
        }
        GER_gott_mit_uns = {
            picture = generic_army_war_college
            allowed = {
                original_tag = GER
            }
            removal_cost = -1
            modifier = {
                army_core_defence_factor = 0.15
                army_attack_factor = 0.10
                breakthrough_factor = 0.10
            }
        }
        NWW_GER_quality = {
            picture = generic_industrial_concern_1
            removal_cost = -1
            allowed = {
                always = yes
            }
            modifier = {
                production_factory_efficiency_gain_factor = 0.05
            }
        }
        GER_staff_manoeuvres = {
            picture = generic_army_war_college
            allowed = {
                original_tag = GER
            }
            removal_cost = -1
            modifier = {
                planning_speed = 0.15
                army_morale_factor = 0.05
            }
        }
        GER_social_budget = {
            picture = generic_industrial_concern_1
            allowed = {
                original_tag = GER
            }
            removal_cost = -1
            modifier = {
                production_speed_industrial_complex_factor = 0.10
            }
        }
        GER_military_accounts = {
            picture = generic_industrial_concern_1
            allowed = {
                original_tag = GER
            }
            removal_cost = -1
            modifier = {
                political_power_gain = 0.15
                army_attack_factor = -0.05
            }
        }
        GER_constitutional_truce = {
            picture = generic_industrial_concern_1
            allowed = {
                original_tag = GER
            }
            removal_cost = -1
            modifier = {
                consumer_goods_factor = -0.05
            }
        }
        GER_imperial_overstretch_2 = {
            picture = generic_oppression
            allowed = {
                always = yes
            }
            removal_cost = -1
            modifier = {
                political_power_gain = -0.25
                consumer_goods_factor = 0.15
                war_support_factor = -0.15
                training_time_army_factor = 0.20
                planning_speed = -0.15
            }
        }
        GER_gott_mit_uns_naval = {
            picture = generic_industrial_concern_1
            allowed = {
                always = yes
            }
            removal_cost = -1
            modifier = {
                army_core_defence_factor = 0.15
                army_attack_factor = 0.10
                breakthrough_factor = 0.10
                production_speed_dockyard_factor = 0.15
                industrial_capacity_dockyard = 0.10
            }
        }
        GER_the_new_reich_integrated = {
            picture = generic_oppression
            allowed = {
                always = yes
            }
            removal_cost = -1
            modifier = {
                army_attack_factor = 0.15
                breakthrough_factor = 0.20
                army_speed_factor = 0.10
                compliance_growth = 0.10
                resistance_target = -0.10
                required_garrison_factor = 0.10
            }
        }
        GER_federal_investment = {
            picture = generic_industrial_concern_1
            allowed = {
                always = yes
            }
            removal_cost = -1
            modifier = {
                production_speed_industrial_complex_factor = 0.10
                industrial_capacity_factory = 0.05
            }
        }
        GER_arsenal_of_democracy_shield = {
            picture = generic_army_war_college
            allowed = {
                always = yes
            }
            removal_cost = -1
            modifier = {
                army_core_defence_factor = 0.15
                stability_factor = 0.15
                political_power_gain = 0.20
                industrial_capacity_factory = 0.20
                army_defence_factor = 0.10
                send_volunteer_size = 2
                send_volunteers_tension = -0.50
            }
        }
        GER_nva_mass_army = {
            picture = generic_reserve_divisions
            allowed = {
                always = yes
            }
            removal_cost = -1
            modifier = {
                conscription = 0.10
                army_morale_factor = 0.10
                training_time_army_factor = -0.10
            }
            research_bonus = {
                air_equipment = -0.20
                naval_equipment = -0.20
            }
        }
    }
}
```

### `common/dynamic_modifiers/GER_industry_modifiers.txt`

```pdx
GER_nww_industrial_program = {
    enable = {
        always = yes
    }
    icon = GFX_idea_generic_industrial_concern_1
    production_speed_buildings_factor = GER_industry_construction
    industrial_capacity_factory = GER_industry_output
    production_factory_efficiency_gain_factor = GER_industry_efficiency
    production_factory_max_efficiency_factor = GER_industry_maximum
    research_speed_factor = GER_industry_research
    energy_gain_factor = GER_industry_energy
}
```

### `common/country_leader/GER_traits.txt`

```pdx
leader_traits = {
    ger_aging_monarch = {
        random = no
        stability_factor = -0.10
        political_advisor_cost_factor = 0.25
    }
}
```

### `common/on_actions/GER_campaign_safety_on_actions.txt`

```pdx
on_actions = {
    on_startup = {
        effect = {
            GER = {
                if = {
                    limit = {
                        exists = yes
                        has_focus_tree = GER_focus
                    }
                    nww_GER_ai_install_campaign_guard = yes
                    if = {
                        limit = {
                            is_ai = yes
                            has_war = no
                            NOT = {
                                has_country_flag = NWW_GER_campaign_safety_initialized
                            }
                        }
                        set_country_flag = {
                            flag = NWW_GER_campaign_recovery
                            days = 180
                        }
                    }
                    set_country_flag = NWW_GER_campaign_safety_initialized
                    nww_GER_ai_observe_campaign = yes
                }
            }
        }
    }
    on_daily_GER = {
        effect = {
            if = {
                limit = {
                    has_focus_tree = GER_focus
                }
                nww_GER_ai_observe_campaign = yes
            }
        }
    }
    on_war = {
        effect = {
            if = {
                limit = {
                    tag = GER
                    has_focus_tree = GER_focus
                }
                nww_GER_ai_observe_campaign = yes
            }
        }
    }
    on_war_relation_added = {
        effect = {
            if = {
                limit = {
                    tag = GER
                    has_focus_tree = GER_focus
                }
                nww_GER_ai_observe_campaign = yes
            }
            FROM = {
                if = {
                    limit = {
                        tag = GER
                        has_focus_tree = GER_focus
                    }
                    nww_GER_ai_observe_campaign = yes
                }
            }
        }
    }
    on_capitulation = {
        effect = {
            if = {
                limit = {
                    tag = GER
                    has_focus_tree = GER_focus
                }
                set_country_flag = NWW_GER_campaign_defeat_pending
            }
        }
    }
    on_peaceconference_ended = {
        effect = {
            if = {
                limit = {
                    tag = GER
                    has_focus_tree = GER_focus
                }
                set_country_flag = NWW_GER_campaign_was_at_war
                nww_GER_ai_observe_campaign = yes
            }
        }
    }
}
```

### `common/on_actions/GER_diplomacy_on_actions.txt`

```pdx
on_actions = {
    on_startup = {
        effect = {
            every_country = {
                limit = {
                    original_tag = GER
                    has_focus_tree = GER_focus
                }
                nww_GER_remove_starting_axis = yes
            }
        }
    }
    on_daily_GER = {
        effect = {
            nww_GER_remove_starting_axis = yes
        }
    }
}
```

### `common/on_actions/GER_industry_on_actions.txt`

```pdx
on_actions = {
    on_startup = {
        effect = {
            every_country = {
                limit = {
                    original_tag = GER
                    has_focus_tree = GER_focus
                }
                GER_nww_refresh_industry = yes
            }
        }
    }
    on_daily_GER = {
        effect = {
            if = {
                limit = {
                    has_focus_tree = GER_focus
                }
                GER_nww_refresh_industry = yes
            }
        }
    }
}
```

### `common/on_actions/GER_lategame_on_actions.txt`

```pdx
on_actions = {
    on_startup = {
        effect = {
            every_country = {
                limit = {
                    original_tag = GER
                    has_focus_tree = GER_focus
                }
                GER_nww_repair_army_reform = yes
                GER_nww_refresh_western_wargoals = yes
            }
        }
    }
    on_daily = {
        effect = {
            every_country = {
                limit = {
                    original_tag = GER
                    has_focus_tree = GER_focus
                }
                GER_nww_repair_army_reform = yes
                GER_nww_refresh_western_wargoals = yes
            }
            every_country = {
                limit = {
                    OR = {
                        is_in_faction = yes
                        has_idea = GER_federal_investment
                    }
                }
                GER_nww_refresh_federal_investment = yes
            }
        }
    }
}
```

### `common/on_actions/GER_on_actions.txt`

```pdx
on_actions = {
    on_startup = {
        effect = {
            every_country = {
                limit = {
                    original_tag = GER
                    has_focus_tree = GER_focus
                }
                nww_GER_disable_mefo = yes
                nww_GER_initialize_politics = yes
                nww_GER_spartacist_victory_repair = yes
            }
        }
    }
    on_daily_GER = {
        effect = {
            nww_GER_spartacist_victory_repair = yes
            if = {
                limit = {
                    has_focus_tree = GER_focus
                }
                nww_GER_initialize_politics = yes
                nww_GER_mitteleuropa_refusal_wargoals = yes
                if = {
                    limit = {
                        date > 1936.12.30
                        NOT = {
                            has_country_flag = ger_wilhelm_ii_dead
                        }
                    }
                    country_event = {
                        id = ger_crisis.1
                    }
                }
                if = {
                    limit = {
                        has_country_flag = ger_wilhelm_ii_dead
                        NOT = {
                            has_completed_focus = GER_end_of_an_era
                        }
                    }
                    complete_national_focus = GER_end_of_an_era
                }
            }
            if = {
                limit = {
                    has_focus_tree = GER_focus
                    OR = {
                        NOT = {
                            has_country_flag = NWW_GER_no_mefo
                        }
                        has_dynamic_modifier = {
                            modifier = GER_mefo_bills_modifier
                        }
                        has_dynamic_modifier = {
                            modifier = GER_economy_of_conquest_modifier
                        }
                        has_active_mission = GER_mefo_bills_mission
                    }
                }
                nww_GER_disable_mefo = yes
            }
        }
    }
    on_daily = {
        effect = {
            every_country = {
                limit = {
                    original_tag = GER
                    has_focus_tree = GER_focus
                    NOT = {
                        tag = GER
                    }
                }
                nww_GER_disable_mefo = yes
                nww_GER_initialize_politics = yes
                nww_GER_spartacist_victory_repair = yes
            }
        }
    }
    on_civil_war_end = {
        effect = {
            if = {
                limit = {
                    original_tag = GER
                    has_country_flag = ger_spartacist_side
                    has_government = communism
                    FROM = {
                        original_tag = GER
                        has_country_flag = ger_spartacist_loyalists
                    }
                }
                set_country_flag = ger_spartacist_victory
                load_focus_tree = {
                    tree = GER_focus
                    keep_completed = yes
                }
                nww_GER_disable_mefo = yes
                nww_GER_initialize_politics = yes
            }
        }
    }
}
```

### `common/on_actions/GER_pacing_on_actions.txt`

```pdx
on_actions = {
    on_startup = {
        effect = {
            GER = {
                if = {
                    limit = {
                        exists = yes
                        has_focus_tree = GER_focus
                    }
                    GER_nww_dispatch_austrian_demand = yes
                }
            }
        }
    }
    on_daily_GER = {
        effect = {
            if = {
                limit = {
                    has_focus_tree = GER_focus
                }
                GER_nww_dispatch_austrian_demand = yes
            }
        }
    }
}
```

### `common/scripted_effects/GER_bohemian_effects.txt`

```pdx
GER_nww_update_bohemian_influence = {
    if = {
        limit = {
            NOT = {
                has_variable = AUS_bohemian_german_pressure
            }
        }
        set_variable = {
            AUS_bohemian_german_pressure = 0
        }
    }
    clamp_variable = {
        var = AUS_bohemian_german_pressure
        min = 0
        max = 10
    }
    if = {
        limit = {
            check_variable = {
                var = AUS_bohemian_german_pressure
                value = AUS_bohemian_tension
                compare = greater_than
            }
        }
        set_variable = {
            AUS_bohemian_german_pressure = AUS_bohemian_tension
        }
    }
    set_variable = {
        AUS_bohemian_german_share = 0
    }
    if = {
        limit = {
            check_variable = {
                AUS_bohemian_tension > 0
            }
        }
        set_variable = {
            AUS_bohemian_german_share = AUS_bohemian_german_pressure
        }
        divide_variable = {
            AUS_bohemian_german_share = AUS_bohemian_tension
        }
        multiply_variable = {
            AUS_bohemian_german_share = 100
        }
    }
    set_variable = {
        AUS_bohemian_german_weight = AUS_bohemian_german_pressure
    }
    multiply_variable = {
        AUS_bohemian_german_weight = 5
    }
    set_variable = {
        AUS_bohemian_german_threshold = AUS_bohemian_tension
    }
    multiply_variable = {
        AUS_bohemian_german_threshold = 3
    }
}
GER_nww_support_bohemian_autonomists = {
    if = {
        limit = {
            GER_nww_bohemian_target_open = yes
        }
        set_variable = {
            AUS_bohemian_operation_gain = 10
        }
        subtract_from_variable = {
            AUS_bohemian_operation_gain = AUS_bohemian_tension
        }
        clamp_variable = {
            var = AUS_bohemian_operation_gain
            min = 0
            max = 2
        }
        add_to_variable = {
            AUS_bohemian_tension = AUS_bohemian_operation_gain
        }
        add_to_variable = {
            AUS_bohemian_german_pressure = AUS_bohemian_operation_gain
        }
        AUS_nww_update_bohemian_spirit = yes
        if = {
            limit = {
                check_variable = {
                    var = AUS_bohemian_tension
                    value = 10
                    compare = greater_than_or_equals
                }
            }
            country_event = {
                id = nww_aus_overhaul.1
            }
        }
    }
}
GER_nww_settle_bohemian_influence = {
    GER_nww_update_bohemian_influence = yes
    if = {
        limit = {
            has_country_flag = AUS_nww_fresh_bohemian_secession
            check_variable = {
                var = AUS_bohemian_german_weight
                value = AUS_bohemian_german_threshold
                compare = greater_than
            }
            CZE = {
                exists = yes
                is_subject = no
                is_in_faction = no
                owns_state = 9
                NOT = {
                    has_war_with = GER
                }
            }
            GER = {
                exists = yes
                is_subject = no
                NOT = {
                    has_war_with = AUS
                }
                NOT = {
                    has_war_with = CZE
                }
            }
        }
        GER = {
            set_autonomy = {
                target = CZE
                autonomy_state = autonomy_puppet
                end_wars = no
                end_civil_wars = no
            }
            country_event = {
                id = nww_ger_bohemia.1
            }
        }
        CZE = {
            set_country_flag = GER_nww_bohemian_client
        }
    }
    clr_country_flag = AUS_nww_fresh_bohemian_secession
}
```

### `common/scripted_effects/GER_campaign_safety_effects.txt`

```pdx
nww_GER_ai_install_campaign_guard = {
    remove_relation_rule_override = {
        trigger = nww_GER_ai_unsafe_declaration
        can_not_declare_war = yes
    }
    add_relation_rule_override = {
        trigger = nww_GER_ai_unsafe_declaration
        usage_desc = NWW_GER_campaign_safety_tt
        can_not_declare_war = yes
    }
    set_country_flag = NWW_GER_campaign_guard_installed
}
nww_GER_ai_observe_campaign = {
    if = {
        limit = {
            NOT = {
                has_country_flag = NWW_GER_campaign_guard_installed
            }
        }
        nww_GER_ai_install_campaign_guard = yes
    }
    if = {
        limit = {
            has_capitulated = yes
        }
        set_country_flag = NWW_GER_campaign_defeat_pending
    }
    if = {
        limit = {
            has_war = yes
        }
        set_country_flag = NWW_GER_campaign_was_at_war
    }
    if = {
        limit = {
            has_war = no
            OR = {
                has_country_flag = NWW_GER_campaign_was_at_war
                has_country_flag = NWW_GER_campaign_defeat_pending
            }
        }
        if = {
            limit = {
                has_country_flag = NWW_GER_campaign_defeat_pending
            }
            set_country_flag = {
                flag = NWW_GER_campaign_recovery
                days = 730
            }
        }
        else = {
            set_country_flag = {
                flag = NWW_GER_campaign_recovery
                days = 180
            }
        }
        clr_country_flag = NWW_GER_campaign_was_at_war
        clr_country_flag = NWW_GER_campaign_defeat_pending
    }
}
```

### `common/scripted_effects/GER_diplomacy_effects.txt`

```pdx
nww_GER_remove_starting_axis = {
    if = {
        limit = {
            has_faction_template = faction_template_axis
            NOT = {
                is_faction_leader = yes
                OR = {
                    has_completed_focus = GER_mitteleuropa_economic_community
                    AND = {
                        has_completed_focus = GER_the_austrian_referendum
                        AUS = {
                            is_in_faction_with = PREV
                        }
                    }
                }
            }
        }
        if = {
            limit = {
                is_faction_leader = yes
            }
            dismantle_faction = yes
        }
        else = {
            leave_faction = yes
        }
    }
}
```

### `common/scripted_effects/GER_effects.txt`

```pdx
nww_GER_disable_mefo = {
    if = {
        limit = {
            has_dynamic_modifier = {
                modifier = GER_mefo_bills_modifier
            }
        }
        remove_dynamic_modifier = {
            modifier = GER_mefo_bills_modifier
        }
    }
    if = {
        limit = {
            has_dynamic_modifier = {
                modifier = GER_economy_of_conquest_modifier
            }
        }
        remove_dynamic_modifier = {
            modifier = GER_economy_of_conquest_modifier
        }
    }
    if = {
        limit = {
            has_idea = GER_mefo_bills_1
        }
        remove_ideas = GER_mefo_bills_1
    }
    if = {
        limit = {
            has_idea = GER_mefo_bills_2
        }
        remove_ideas = GER_mefo_bills_2
    }
    if = {
        limit = {
            has_idea = GER_mefo_bills_3
        }
        remove_ideas = GER_mefo_bills_3
    }
    if = {
        limit = {
            has_idea = GER_mefo_bills_4
        }
        remove_ideas = GER_mefo_bills_4
    }
    if = {
        limit = {
            has_idea = GER_mefo_bills_5
        }
        remove_ideas = GER_mefo_bills_5
    }
    if = {
        limit = {
            has_idea = GER_mefo_bills_6
        }
        remove_ideas = GER_mefo_bills_6
    }
    if = {
        limit = {
            has_idea = GER_mefo_bills_7
        }
        remove_ideas = GER_mefo_bills_7
    }
    if = {
        limit = {
            has_idea = GER_mefo_bills_8
        }
        remove_ideas = GER_mefo_bills_8
    }
    if = {
        limit = {
            has_idea = GER_mefo_bills_9
        }
        remove_ideas = GER_mefo_bills_9
    }
    if = {
        limit = {
            has_idea = GER_mefo_bills_10
        }
        remove_ideas = GER_mefo_bills_10
    }
    if = {
        limit = {
            has_idea = GER_mefo_bills_11
        }
        remove_ideas = GER_mefo_bills_11
    }
    if = {
        limit = {
            has_idea = GER_mefo_bills_12
        }
        remove_ideas = GER_mefo_bills_12
    }
    if = {
        limit = {
            has_idea = GER_mefo_bills_13
        }
        remove_ideas = GER_mefo_bills_13
    }
    if = {
        limit = {
            has_idea = GER_mefo_bills_14
        }
        remove_ideas = GER_mefo_bills_14
    }
    if = {
        limit = {
            has_idea = GER_mefo_bills_15
        }
        remove_ideas = GER_mefo_bills_15
    }
    if = {
        limit = {
            has_idea = GER_mefo_bills_16
        }
        remove_ideas = GER_mefo_bills_16
    }
    if = {
        limit = {
            has_idea = GER_mefo_bills_17
        }
        remove_ideas = GER_mefo_bills_17
    }
    if = {
        limit = {
            has_idea = GER_mefo_bills_18
        }
        remove_ideas = GER_mefo_bills_18
    }
    if = {
        limit = {
            has_idea = GER_mefo_bills_ended
        }
        remove_ideas = GER_mefo_bills_ended
    }
    if = {
        limit = {
            has_idea = GER_mefo_bills_1936_fake_ns
        }
        remove_ideas = GER_mefo_bills_1936_fake_ns
    }
    if = {
        limit = {
            has_idea = GER_mefo_bills_1939_fake_ns
        }
        remove_ideas = GER_mefo_bills_1939_fake_ns
    }
    if = {
        limit = {
            has_active_mission = GER_mefo_bills_mission
        }
        remove_mission = GER_mefo_bills_mission
    }
    clr_country_flag = ger_has_cancelled_mefo
    clr_country_flag = paid_for_mefo
    clr_country_flag = GER_mefo_bills_penalty_flag
    set_variable = {
        GER_mefo_bill_counter = 0
    }
    set_variable = {
        GER_monthly_consumer_goods_increase = 0
    }
    set_variable = {
        GER_industrial_consumer_goods_factor = 0
    }
    set_country_flag = NWW_GER_no_mefo
}
nww_GER_initialize_politics = {
    if = {
        limit = {
            OR = {
                has_completed_focus = GER_abolish_the_hohenzollerns
                has_country_flag = ger_spartacist_side
                has_country_flag = ger_bop_removed
            }
        }
        set_country_flag = ger_bop_removed
        if = {
            limit = {
                has_power_balance = {
                    id = GER_kaiser_vs_reichstag
                }
            }
            remove_power_balance = {
                id = GER_kaiser_vs_reichstag
            }
        }
    }
    else = {
        if = {
            limit = {
                NOT = {
                    has_power_balance = {
                        id = GER_kaiser_vs_reichstag
                    }
                }
            }
            set_power_balance = {
                id = GER_kaiser_vs_reichstag
                set_default = yes
            }
        }
        if = {
            limit = {
                OR = {
                    has_completed_focus = GER_parliamentary_spring
                    has_country_flag = ger_parliamentary_spring
                }
            }
            set_country_flag = ger_bop_frozen
            if = {
                limit = {
                    NOT = {
                        power_balance_value = {
                            id = GER_kaiser_vs_reichstag
                            value = 1
                        }
                    }
                }
                set_power_balance = {
                    id = GER_kaiser_vs_reichstag
                    set_value = 1
                }
            }
        }
        else_if = {
            limit = {
                has_completed_focus = GER_dissolve_the_reichstag
            }
            set_country_flag = ger_bop_frozen
            if = {
                limit = {
                    NOT = {
                        power_balance_value = {
                            id = GER_kaiser_vs_reichstag
                            value = -1
                        }
                    }
                }
                set_power_balance = {
                    id = GER_kaiser_vs_reichstag
                    set_value = -1
                }
            }
        }
    }
    nww_GER_eastern_war_guard = yes
    nww_GER_set_party_labels = yes
}
GER_nww_dispatch_austrian_demand = {
    if = {
        limit = {
            date > 1938.12.31
            has_completed_focus = GER_the_austrian_question
            has_government = neutrality
            is_subject = no
            AUS = {
                exists = yes
                is_subject = no
            }
            NOT = {
                has_country_flag = GER_nww_austrian_demand_sent
            }
            NOT = {
                has_war_with = AUS
            }
            NOT = {
                is_ally_with = AUS
            }
            NOT = {
                has_wargoal_against = AUS
            }
            nww_GER_ai_can_target_AUS = yes
        }
        set_country_flag = GER_nww_austrian_demand_sent
        AUS = {
            country_event = {
                id = ger_crisis.10
                days = 1
            }
        }
    }
}
nww_GER_litbel_war_guard = {
    nww_GER_eastern_war_guard = yes
}
nww_GER_mitteleuropa_demand = {
    if = {
        limit = {
            exists = yes
            NOT = {
                has_war_with = GER
            }
            GER = {
                exists = yes
                is_subject = no
                has_government = neutrality
            }
            date > 1938.12.31
            nww_GER_ai_can_prepare_campaign = yes
        }
        if = {
            limit = {
                is_subject_of = GER
                NOT = {
                    has_autonomy_state = autonomy_integrated_puppet
                }
            }
            if = {
                limit = {
                    has_dlc = "Together for Victory"
                }
                GER = {
                    set_autonomy = {
                        target = PREV
                        autonomy_state = autonomy_integrated_puppet
                        end_wars = no
                        end_civil_wars = no
                    }
                }
            }
            else = {
                GER = {
                    set_autonomy = {
                        target = PREV
                        autonomy_state = autonomy_puppet
                        end_wars = no
                        end_civil_wars = no
                    }
                }
            }
        }
        else_if = {
            limit = {
                is_subject = no
            }
            country_event = {
                id = ger_crisis.20
                days = 1
            }
        }
    }
}
nww_GER_mitteleuropa_refusal_wargoals = {
    if = {
        limit = {
            has_completed_focus = GER_reign_in_mitteleuropa
            has_government = neutrality
            is_subject = no
            NOT = {
                date < 1939.1.1
            }
            LTB = {
                exists = yes
                is_subject = no
                has_country_flag = ger_mitteleuropa_refused
            }
            NOT = {
                has_war_with = LTB
            }
            NOT = {
                is_ally_with = LTB
            }
            NOT = {
                has_wargoal_against = LTB
            }
            date > 1938.12.31
        }
        if = {
            limit = {
                nww_GER_ai_can_target_LTB = yes
            }
            create_wargoal = {
                type = puppet_wargoal_focus
                target = LTB
            }
        }
        LTB = {
            clr_country_flag = ger_mitteleuropa_refused
        }
    }
    if = {
        limit = {
            has_completed_focus = GER_reign_in_mitteleuropa
            has_government = neutrality
            is_subject = no
            POL = {
                exists = yes
                is_subject = no
                has_country_flag = ger_mitteleuropa_refused
            }
            NOT = {
                has_war_with = POL
            }
            NOT = {
                is_ally_with = POL
            }
            NOT = {
                has_wargoal_against = POL
            }
            date > 1938.12.31
        }
        if = {
            limit = {
                nww_GER_ai_can_target_POL = yes
            }
            create_wargoal = {
                type = puppet_wargoal_focus
                target = POL
            }
        }
        POL = {
            clr_country_flag = ger_mitteleuropa_refused
        }
    }
}
nww_GER_eastern_wargoals = {
    if = {
        limit = {
            MKN = {
                exists = yes
                is_subject = no
            }
            NOT = {
                has_war_with = MKN
            }
            NOT = {
                is_ally_with = MKN
            }
            NOT = {
                has_wargoal_against = MKN
            }
            date > 1938.12.31
            has_government = neutrality
            is_subject = no
        }
        if = {
            limit = {
                nww_GER_ai_can_target_MKN = yes
            }
            create_wargoal = {
                type = annex_everything
                target = MKN
            }
        }
    }
    if = {
        limit = {
            UKR = {
                exists = yes
                is_subject = no
            }
            NOT = {
                has_war_with = UKR
            }
            NOT = {
                is_ally_with = UKR
            }
            NOT = {
                has_wargoal_against = UKR
            }
            date > 1938.12.31
            has_government = neutrality
            is_subject = no
        }
        if = {
            limit = {
                nww_GER_ai_can_target_UKR = yes
            }
            create_wargoal = {
                type = annex_everything
                target = UKR
            }
        }
    }
}
nww_GER_eastern_war_guard = {
    if = {
        limit = {
            date < 1939.1.1
            NOT = {
                has_country_flag = ger_eastern_war_guard
            }
        }
        add_relation_rule_override = {
            target = LTB
            usage_desc = GER_eastern_war_guard_tt
            can_not_declare_war = yes
        }
        add_relation_rule_override = {
            target = POL
            usage_desc = GER_eastern_war_guard_tt
            can_not_declare_war = yes
        }
        add_relation_rule_override = {
            target = UKR
            usage_desc = GER_eastern_war_guard_tt
            can_not_declare_war = yes
        }
        add_relation_rule_override = {
            target = MKN
            usage_desc = GER_eastern_war_guard_tt
            can_not_declare_war = yes
        }
        add_relation_rule_override = {
            target = SOV
            usage_desc = GER_eastern_war_guard_tt
            can_not_declare_war = yes
        }
        set_country_flag = ger_eastern_war_guard
    }
    else_if = {
        limit = {
            NOT = {
                date < 1939.1.1
            }
            has_country_flag = ger_eastern_war_guard
        }
        remove_relation_rule_override = {
            target = LTB
            can_not_declare_war = yes
        }
        remove_relation_rule_override = {
            target = POL
            can_not_declare_war = yes
        }
        remove_relation_rule_override = {
            target = UKR
            can_not_declare_war = yes
        }
        remove_relation_rule_override = {
            target = MKN
            can_not_declare_war = yes
        }
        remove_relation_rule_override = {
            target = SOV
            can_not_declare_war = yes
        }
        clr_country_flag = ger_eastern_war_guard
    }
    if = {
        limit = {
            NOT = {
                date < 1939.1.1
            }
            has_country_flag = ger_litbel_war_guard
        }
        remove_relation_rule_override = {
            target = LTB
            can_not_declare_war = yes
        }
        clr_country_flag = ger_litbel_war_guard
    }
}
nww_GER_set_party_labels = {
    if = {
        limit = {
            NOT = {
                has_country_flag = ger_party_labels_set
            }
        }
        set_party_name = {
            ideology = neutrality
            name = GER_neutrality_party
            long_name = GER_neutrality_party_long
        }
        set_party_name = {
            ideology = democratic
            name = GER_democratic_party
            long_name = GER_democratic_party_long
        }
        set_party_name = {
            ideology = fascism
            name = GER_fascism_party
            long_name = GER_fascism_party_long
        }
        set_party_name = {
            ideology = communism
            name = GER_communism_party
            long_name = GER_communism_party_long
        }
        set_country_flag = ger_party_labels_set
    }
}
nww_GER_establish_mitteleuropa = {
    if = {
        limit = {
            is_in_faction = no
        }
        create_faction_from_template = {
            template = faction_template_GER_mitteleuropa
            name = GER_mitteleuropa_faction
        }
    }
    else_if = {
        limit = {
            is_faction_leader = yes
        }
        set_faction_name = GER_mitteleuropa_faction
        set_faction_manifest = faction_manifest_defense_of_democracy_allies
        set_faction_rule = joining_rule_non_fascist
        set_faction_rule = joining_rule_has_no_offensive_war
        set_faction_rule = faction_peace_rule_liberation_focus
    }
}
nww_GER_free_eastern_subjects = {
    if = {
        limit = {
            LTB = {
                exists = yes
                is_subject_of = ROOT
            }
        }
        set_autonomy = {
            target = LTB
            autonomy_state = autonomy_free
            end_wars = no
            end_civil_wars = no
        }
    }
    if = {
        limit = {
            POL = {
                exists = yes
                is_subject_of = ROOT
            }
        }
        set_autonomy = {
            target = POL
            autonomy_state = autonomy_free
            end_wars = no
            end_civil_wars = no
        }
    }
}
nww_GER_democratic_community_offer = {
    if = {
        limit = {
            exists = yes
            NOT = {
                has_war_with = ROOT
            }
        }
        if = {
            limit = {
                is_subject_of = ROOT
            }
            ROOT = {
                set_autonomy = {
                    target = PREV
                    autonomy_state = autonomy_free
                    end_wars = no
                    end_civil_wars = no
                }
            }
        }
        if = {
            limit = {
                is_subject = no
                NOT = {
                    has_country_flag = ger_economic_community_accepted
                }
            }
            country_event = {
                id = ger_crisis.50
                days = 1
            }
        }
    }
}
nww_GER_start_spartacist_civil_war = {
    set_country_flag = ger_spartacist_civil_war_started
    set_country_flag = ger_spartacist_loyalists
    set_country_flag = ger_bop_frozen
    start_civil_war = {
        ideology = communism
        size = 0.40
        set_country_flag = ger_spartacist_civil_war_started
        set_country_flag = ger_spartacist_side
        set_cosmetic_tag = GER
        if = {
            limit = {
                is_in_faction = yes
            }
            leave_faction = yes
        }
        clr_country_flag = ger_spartacist_loyalists
        set_country_flag = ger_wilhelm_ii_dead
        set_country_flag = ger_bop_removed
        load_focus_tree = {
            tree = GER_focus
            keep_completed = yes
            copy_completed_from = ROOT
        }
        set_politics = {
            ruling_party = communism
            elections_allowed = no
            election_frequency = 48
        }
        GER_wilhelm_pieck = {
            add_country_leader_role = {
                country_leader = {
                    ideology = GER_spartacism
                    expire = 1965.1.1
                    traits = {

                    }
                }
                promote_leader = yes
            }
        }
        clr_country_flag = ger_eastern_war_guard
        nww_GER_disable_mefo = yes
        nww_GER_initialize_politics = yes
        change_tag_from = ROOT
        ROOT = {
            GER_ernst_thalmann = {
                set_nationality = PREV.PREV
            }
        }
    }
}
nww_GER_spartacist_victory_repair = {
    if = {
        limit = {
            has_country_flag = ger_spartacist_side
            has_completed_focus = GER_german_soviet_republic
            has_government = communism
        }
        set_country_flag = ger_spartacist_victory
    }
}
nww_GER_pan_german_eastern_wargoals = {
    if = {
        limit = {
            has_government = fascism
            is_subject = no
            date > 1938.12.31
            LTB = {
                exists = yes
                is_subject = no
            }
            NOT = {
                has_war_with = LTB
            }
            NOT = {
                is_ally_with = LTB
            }
            NOT = {
                has_wargoal_against = LTB
            }
        }
        if = {
            limit = {
                nww_GER_ai_can_target_LTB = yes
            }
            create_wargoal = {
                type = annex_everything
                target = LTB
            }
        }
    }
    if = {
        limit = {
            has_government = fascism
            is_subject = no
            date > 1938.12.31
            POL = {
                exists = yes
                is_subject = no
            }
            NOT = {
                has_war_with = POL
            }
            NOT = {
                is_ally_with = POL
            }
            NOT = {
                has_wargoal_against = POL
            }
        }
        if = {
            limit = {
                nww_GER_ai_can_target_POL = yes
            }
            create_wargoal = {
                type = annex_everything
                target = POL
            }
        }
    }
}
nww_GER_western_revolution_wargoals = {
    if = {
        limit = {
            has_government = communism
            is_subject = no
            FRA = {
                exists = yes
                is_subject = no
            }
            NOT = {
                has_war_with = FRA
            }
            NOT = {
                is_ally_with = FRA
            }
            NOT = {
                has_wargoal_against = FRA
            }
        }
        if = {
            limit = {
                nww_GER_ai_can_target_FRA = yes
            }
            create_wargoal = {
                type = annex_everything
                target = FRA
            }
        }
    }
    if = {
        limit = {
            has_government = communism
            is_subject = no
            ENG = {
                exists = yes
                is_subject = no
            }
            NOT = {
                has_war_with = ENG
            }
            NOT = {
                is_ally_with = ENG
            }
            NOT = {
                has_wargoal_against = ENG
            }
        }
        if = {
            limit = {
                nww_GER_ai_can_target_ENG = yes
            }
            create_wargoal = {
                type = annex_everything
                target = ENG
            }
        }
    }
}
```

### `common/scripted_effects/GER_industry_effects.txt`

```pdx
GER_nww_refresh_industry = {
    set_variable = {
        GER_industry_construction = 0
    }
    set_variable = {
        GER_industry_output = 0
    }
    set_variable = {
        GER_industry_efficiency = 0
    }
    set_variable = {
        GER_industry_maximum = 0
    }
    set_variable = {
        GER_industry_research = 0
    }
    set_variable = {
        GER_industry_energy = 0
    }
    if = {
        limit = {
            has_completed_focus = GER_krupp_and_thyssen
        }
        add_to_variable = {
            GER_industry_construction = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = GER_nww_electrical_grid
        }
        add_to_variable = {
            GER_industry_energy = 0.1
        }
    }
    if = {
        limit = {
            has_completed_focus = GER_nww_arsenal_contracts
        }
        add_to_variable = {
            GER_industry_output = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = GER_4
        }
        add_to_variable = {
            GER_industry_efficiency = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = GER_6
        }
        add_to_variable = {
            GER_industry_construction = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = GER_7
        }
        add_to_variable = {
            GER_industry_maximum = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = GER_nww_machine_tools
        }
        add_to_variable = {
            GER_industry_efficiency = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = GER_nww_industrial_standards
        }
        add_to_variable = {
            GER_industry_maximum = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = GER_nww_technical_colleges
        }
        add_to_variable = {
            GER_industry_research = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = GER_nww_investment_guarantees
        }
        add_to_variable = {
            GER_industry_construction = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = GER_9
        }
        add_to_variable = {
            GER_industry_output = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = GER_nww_industrial_research
        }
        add_to_variable = {
            GER_industry_research = 0.05
        }
    }
    if = {
        limit = {
            has_completed_focus = GER_7
            has_idea = NWW_GER_quality
        }
        remove_ideas = NWW_GER_quality
    }
    if = {
        limit = {
            has_completed_focus = GER_krupp_and_thyssen
            NOT = {
                has_dynamic_modifier = {
                    modifier = GER_nww_industrial_program
                }
            }
        }
        add_dynamic_modifier = {
            modifier = GER_nww_industrial_program
        }
    }
}
GER_nww_build_civilian = {
    random_owned_controlled_state = {
        limit = {
            is_core_of = PREV
        }
        add_extra_state_shared_building_slots = 1
        add_building_construction = {
            type = industrial_complex
            level = 1
            instant_build = yes
        }
    }
}
GER_nww_build_military = {
    random_owned_controlled_state = {
        limit = {
            is_core_of = PREV
        }
        add_extra_state_shared_building_slots = 1
        add_building_construction = {
            type = arms_factory
            level = 1
            instant_build = yes
        }
    }
}
GER_nww_build_refinery = {
    random_owned_controlled_state = {
        limit = {
            is_core_of = PREV
        }
        add_extra_state_shared_building_slots = 1
        add_building_construction = {
            type = synthetic_refinery
            level = 1
            instant_build = yes
        }
    }
}
GER_nww_improve_infrastructure = {
    random_owned_controlled_state = {
        limit = {
            is_core_of = PREV
            infrastructure < 5
        }
        add_building_construction = {
            type = infrastructure
            level = 1
            instant_build = yes
        }
    }
    random_owned_controlled_state = {
        limit = {
            is_core_of = PREV
            infrastructure < 5
        }
        add_building_construction = {
            type = infrastructure
            level = 1
            instant_build = yes
        }
    }
}
GER_nww_build_energy_infrastructure = {
    random_owned_controlled_state = {
        limit = {
            is_core_of = PREV
            energy_infrastructure < 1
            free_building_slots = {
                building = energy_infrastructure
                size > 0
                include_locked = yes
            }
        }
        prioritize = {
            42
        }
        add_extra_state_shared_building_slots = 1
        add_building_construction = {
            type = energy_infrastructure
            level = 1
            instant_build = yes
        }
    }
}
```

### `common/scripted_effects/GER_lategame_effects.txt`

```pdx
GER_nww_partial_army_reform = {
    if = {
        limit = {
            has_idea = GER_imperial_overstretch
        }
        swap_ideas = {
            remove_idea = GER_imperial_overstretch
            add_idea = GER_imperial_overstretch_2
        }
    }
}
GER_nww_refresh_western_wargoals = {
    if = {
        limit = {
            GER_nww_western_mandate = yes
        }
        if = {
            limit = {
                FRA = {
                    exists = yes
                    is_subject = no
                }
                NOT = {
                    is_ally_with = FRA
                }
                NOT = {
                    has_war_with = FRA
                }
                NOT = {
                    has_wargoal_against = FRA
                }
                nww_GER_ai_can_target_FRA = yes
            }
            create_wargoal = {
                type = annex_everything
                target = FRA
            }
        }
        if = {
            limit = {
                OR = {
                    has_completed_focus = GER_world_revolution
                    has_completed_focus = GER_the_second_naval_race
                }
                ENG = {
                    exists = yes
                    is_subject = no
                }
                NOT = {
                    is_ally_with = ENG
                }
                NOT = {
                    has_war_with = ENG
                }
                NOT = {
                    has_wargoal_against = ENG
                }
                nww_GER_ai_can_target_ENG = yes
            }
            create_wargoal = {
                type = annex_everything
                target = ENG
            }
        }
    }
}
GER_nww_repair_army_reform = {
    if = {
        limit = {
            OR = {
                has_idea = GER_imperial_overstretch
                has_idea = GER_imperial_overstretch_2
            }
            OR = {
                has_completed_focus = GER_gott_mit_uns
                has_completed_focus = GER_arsenal_of_democracy
                has_completed_focus = GER_the_new_reich
                has_completed_focus = GER_workers_militias
            }
        }
        remove_ideas = GER_imperial_overstretch
        remove_ideas = GER_imperial_overstretch_2
    }
    else_if = {
        limit = {
            has_idea = GER_imperial_overstretch
            OR = {
                has_completed_focus = GER_fund_the_reichswehr
                has_completed_focus = GER_true_constitutional_monarchy
                has_completed_focus = GER_abolish_the_hohenzollerns
                has_completed_focus = GER_german_soviet_republic
            }
        }
        GER_nww_partial_army_reform = yes
    }
}
GER_nww_austrian_guarantee = {
    if = {
        limit = {
            CZE = {
                exists = yes
                is_subject = no
                NOT = {
                    has_war_with = GER
                }
                NOT = {
                    has_war_with = AUS
                }
                NOT = {
                    is_ally_with = GER
                }
            }
        }
        CZE = {
            give_guarantee = AUS
        }
    }
    else_if = {
        limit = {
            FRA = {
                exists = yes
                is_subject = no
                NOT = {
                    has_war_with = GER
                }
                NOT = {
                    has_war_with = AUS
                }
                NOT = {
                    is_ally_with = GER
                }
            }
        }
        FRA = {
            give_guarantee = AUS
        }
    }
}
GER_nww_refresh_federal_investment = {
    if = {
        limit = {
            is_in_faction = yes
            OR = {
                AND = {
                    original_tag = GER
                    has_focus_tree = GER_focus
                    has_completed_focus = GER_european_federation
                    has_government = democratic
                    is_faction_leader = yes
                }
                any_other_country = {
                    original_tag = GER
                    has_focus_tree = GER_focus
                    has_completed_focus = GER_european_federation
                    has_government = democratic
                    is_faction_leader = yes
                    is_in_faction_with = PREV
                }
            }
        }
        if = {
            limit = {
                NOT = {
                    has_idea = GER_federal_investment
                }
            }
            add_ideas = GER_federal_investment
        }
    }
    else_if = {
        limit = {
            has_idea = GER_federal_investment
        }
        remove_ideas = GER_federal_investment
    }
}
```

### `common/scripted_triggers/GER_bohemian_triggers.txt`

```pdx
GER_nww_bohemian_target_open = {
    tag = AUS
    exists = yes
    is_subject = no
    has_focus_tree = AUS_focus
    9 = {
        is_owned_and_controlled_by = AUS
    }
    NOT = {
        has_country_flag = AUS_nww_bohemia_settled
    }
    NOT = {
        has_country_flag = AUS_nww_bohemia_seceded
    }
    NOT = {
        has_war_with = GER
    }
    CZE = {
        exists = no
    }
    GER = {
        exists = yes
        is_subject = no
        has_focus_tree = GER_focus
        has_completed_focus = GER_nww_prague_network
        NOT = {
            is_ally_with = AUS
        }
    }
    check_variable = {
        AUS_bohemian_tension < 10
    }
}
```

### `common/scripted_triggers/GER_campaign_safety_triggers.txt`

```pdx
nww_GER_ai_campaign_ready = {
    has_war = no
    has_capitulated = no
    has_civil_war = no
    is_subject = no
    surrender_progress < 0.05
    has_stability > 0.40
    has_war_support > 0.35
    NOT = {
        has_country_flag = NWW_GER_campaign_recovery
    }
    NOT = {
        has_country_flag = NWW_GER_campaign_defeat_pending
    }
    NOT = {
        has_country_flag = NWW_GER_campaign_was_at_war
    }
}
nww_GER_ai_target_safe = {
    OR = {
        GER_nww_lategame_western_target = yes
        AND = {
            exists = yes
            is_subject = no
            NOT = {
                is_ally_with = GER
            }
            NOT = {
                has_war_with_major = yes
            }
            strength_ratio = {
                tag = GER
                ratio < 0.80
            }
            NOT = {
                any_other_country = {
                    has_guaranteed = PREV
                    OR = {
                        is_major = yes
                        is_in_faction = yes
                        is_subject = yes
                    }
                    NOT = {
                        GER_nww_containable_austrian_guarantor = yes
                    }
                }
            }
            OR = {
                is_in_faction = no
                AND = {
                    OR = {
                        is_faction_leader = yes
                        is_major = no
                    }
                    NOT = {
                        any_other_country = {
                            is_major = yes
                            is_in_faction_with = PREV
                            NOT = {
                                is_faction_leader = yes
                            }
                        }
                    }
                    NOT = {
                        any_other_country = {
                            is_faction_leader = yes
                            is_in_faction_with = PREV
                            NOT = {
                                strength_ratio = {
                                    tag = GER
                                    ratio < 0.67
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
nww_GER_ai_unsafe_declaration = {
    GER = {
        is_ai = yes
        has_focus_tree = GER_focus
    }
    OR = {
        GER = {
            NOT = {
                nww_GER_ai_campaign_ready = yes
            }
        }
        FROM = {
            NOT = {
                nww_GER_ai_target_safe = yes
            }
        }
    }
}
nww_GER_ai_can_prepare_campaign = {
    custom_trigger_tooltip = {
        tooltip = nww_GER_ai_can_prepare_campaign
        OR = {
            is_ai = no
            nww_GER_ai_campaign_ready = yes
        }
    }
}
nww_GER_ai_can_target_AUS = {
    custom_trigger_tooltip = {
        tooltip = nww_GER_ai_can_target_AUS
        OR = {
            is_ai = no
            AND = {
                nww_GER_ai_campaign_ready = yes
                AUS = {
                    nww_GER_ai_target_safe = yes
                }
            }
        }
    }
}
nww_GER_ai_can_target_LTB = {
    custom_trigger_tooltip = {
        tooltip = nww_GER_ai_can_target_LTB
        OR = {
            is_ai = no
            AND = {
                nww_GER_ai_campaign_ready = yes
                LTB = {
                    nww_GER_ai_target_safe = yes
                }
            }
        }
    }
}
nww_GER_ai_can_target_POL = {
    custom_trigger_tooltip = {
        tooltip = nww_GER_ai_can_target_POL
        OR = {
            is_ai = no
            AND = {
                nww_GER_ai_campaign_ready = yes
                POL = {
                    nww_GER_ai_target_safe = yes
                }
            }
        }
    }
}
nww_GER_ai_can_target_MKN = {
    custom_trigger_tooltip = {
        tooltip = nww_GER_ai_can_target_MKN
        OR = {
            is_ai = no
            AND = {
                nww_GER_ai_campaign_ready = yes
                MKN = {
                    nww_GER_ai_target_safe = yes
                }
            }
        }
    }
}
nww_GER_ai_can_target_UKR = {
    custom_trigger_tooltip = {
        tooltip = nww_GER_ai_can_target_UKR
        OR = {
            is_ai = no
            AND = {
                nww_GER_ai_campaign_ready = yes
                UKR = {
                    nww_GER_ai_target_safe = yes
                }
            }
        }
    }
}
nww_GER_ai_can_target_FRA = {
    custom_trigger_tooltip = {
        tooltip = nww_GER_ai_can_target_FRA
        OR = {
            is_ai = no
            AND = {
                nww_GER_ai_campaign_ready = yes
                FRA = {
                    nww_GER_ai_target_safe = yes
                }
            }
        }
    }
}
nww_GER_ai_can_target_ENG = {
    custom_trigger_tooltip = {
        tooltip = nww_GER_ai_can_target_ENG
        OR = {
            is_ai = no
            AND = {
                nww_GER_ai_campaign_ready = yes
                ENG = {
                    nww_GER_ai_target_safe = yes
                }
            }
        }
    }
}
nww_GER_ai_can_target_SOV = {
    custom_trigger_tooltip = {
        tooltip = nww_GER_ai_can_target_SOV
        OR = {
            is_ai = no
            AND = {
                nww_GER_ai_campaign_ready = yes
                SOV = {
                    nww_GER_ai_target_safe = yes
                }
            }
        }
    }
}
```

### `common/scripted_triggers/GER_lategame_triggers.txt`

```pdx
GER_nww_containable_austrian_guarantor = {
    is_subject = no
    OR = {
        is_in_faction = no
        is_faction_leader = yes
    }
    OR = {
        tag = CZE
        tag = FRA
    }
    PREV = {
        tag = AUS
    }
    strength_ratio = {
        tag = GER
        ratio < 0.67
    }
    GER = {
        has_focus_tree = GER_focus
        date > 1940.12.31
        OR = {
            AND = {
                has_government = neutrality
                has_completed_focus = GER_gott_mit_uns
            }
            AND = {
                has_government = fascism
                has_completed_focus = GER_the_new_reich
            }
        }
    }
}
GER_nww_eastern_campaigns_settled = {
    OR = {
        AND = {
            POL = {
                exists = no
            }
            owns_state = 10
        }
        POL = {
            exists = yes
            is_subject_of = PREV
        }
        POL = {
            exists = yes
            has_capitulated = yes
            has_war_with = PREV
        }
    }
    OR = {
        AND = {
            AUS = {
                exists = no
            }
            owns_state = 4
        }
        AUS = {
            exists = yes
            is_subject_of = PREV
        }
        AUS = {
            exists = yes
            has_capitulated = yes
            has_war_with = PREV
        }
    }
}
GER_nww_western_mandate = {
    original_tag = GER
    has_focus_tree = GER_focus
    is_subject = no
    date > 1940.12.31
    GER_nww_eastern_campaigns_settled = yes
    OR = {
        AND = {
            has_government = neutrality
            has_completed_focus = GER_strike_the_west
        }
        AND = {
            has_government = communism
            has_completed_focus = GER_world_revolution
        }
    }
}
GER_nww_lategame_western_target = {
    OR = {
        tag = FRA
        tag = ENG
    }
    exists = yes
    is_subject = no
    NOT = {
        is_ally_with = GER
    }
    GER = {
        GER_nww_western_mandate = yes
    }
    strength_ratio = {
        tag = GER
        ratio < 1.25
    }
}
GER_nww_red_rhine_offer_valid = {
    exists = yes
    is_subject = no
    has_civil_war = no
    NOT = {
        has_government = communism
    }
    OR = {
        tag = FRA
        tag = HOL
        tag = BEL
        tag = LUX
    }
    FROM = {
        exists = yes
        original_tag = GER
        has_focus_tree = GER_focus
        has_government = communism
        is_subject = no
        has_completed_focus = GER_red_rhine
    }
}
GER_nww_red_rhine_revolt_ready = {
    check_variable = {
        num_owned_controlled_states > 1
    }
    OR = {
        communism > 0.29
        AND = {
            communism > 0.14
            has_stability < 0.40
        }
    }
}
```

### `common/scripted_triggers/GER_pacing_triggers.txt`

```pdx
GER_nww_historical_pressure_ready = {
    OR = {
        is_ai = no
        is_historical_focus_on = no
        date > 1939.12.31
    }
}
GER_nww_historical_eastern_war_ready = {
    OR = {
        is_ai = no
        is_historical_focus_on = no
        date > 1940.12.31
    }
}
```

### `common/scripted_triggers/GER_triggers.txt`

```pdx
nww_GER_no_political_path = {
    NOT = {
        has_country_flag = ger_iron_kaiserreich
    }
    NOT = {
        has_country_flag = ger_parliamentary_spring
    }
    NOT = {
        has_country_flag = ger_pan_germanic_path
    }
    NOT = {
        has_country_flag = ger_spartacist_civil_war_started
    }
}
```

### `common/operations/GER_bohemian_operations.txt`

```pdx
GER_nww_bohemian_autonomists = {
    icon = GFX_operations_boost_resistance
    map_icon = GFX_operations_boost_resistance_map
    name = GER_nww_bohemian_autonomists
    desc = GER_nww_bohemian_autonomists_desc
    priority = 12
    days = 45
    operatives = 1
    network_strength = 35
    allowed = {
        original_tag = GER
        has_dlc = "La Resistance"
    }
    operation_target = {
        targets = {
            AUS
        }
    }
    visible = {
        has_completed_focus = GER_nww_prague_network
        FROM = {
            GER_nww_bohemian_target_open = yes
        }
    }
    available = {
        FROM = {
            GER_nww_bohemian_target_open = yes
        }
    }
    requirements = {
        FROM = {
            GER_nww_bohemian_target_open = yes
        }
    }
    equipment = {
        civilian_factories = 2
        infantry_equipment = 100
        support_equipment = 25
    }
    risk_chance = 0.15
    experience = 1
    outcome_extra_chance = 0
    outcome_modifiers = {
        operation_outcome
    }
    cost_modifiers = {
        operation_cost
    }
    risk_modifiers = {
        operation_risk
    }
    outcome_potential = {
        custom_effect_tooltip = GER_nww_bohemian_operation_reward_tt
    }
    outcome_execute = {
        FROM = {
            GER_nww_support_bohemian_autonomists = yes
        }
    }
    outcome_extra_execute = {
        FROM = {
            GER_nww_support_bohemian_autonomists = yes
        }
    }
    phases = {
        infiltration_diplomatic = {
            base = 100
        }
    }
    phases = {
        infiltrate_military_bribe = {
            base = 100
        }
    }
    phases = {
        exfiltration_border = {
            base = 100
        }
    }
    ai_will_do = {
        factor = 20
    }
}
```

### `common/ai_strategy/GER_lategame_strategies.txt`

```pdx
GER_nww_lategame_france = {
    allowed = {
        original_tag = GER
    }
    enable = {
        GER_nww_western_mandate = yes
        FRA = {
            exists = yes
            is_subject = no
        }
        NOT = {
            is_ally_with = FRA
        }
    }
    abort_when_not_enabled = yes
    ai_strategy = {
        type = declare_war
        id = FRA
        value = 200
    }
    ai_strategy = {
        type = prepare_for_war
        id = FRA
        value = 200
    }
}
GER_nww_lategame_britain = {
    allowed = {
        original_tag = GER
    }
    enable = {
        GER_nww_western_mandate = yes
        ENG = {
            exists = yes
            is_subject = no
        }
        NOT = {
            is_ally_with = ENG
        }
    }
    abort_when_not_enabled = yes
    ai_strategy = {
        type = declare_war
        id = ENG
        value = 200
    }
    ai_strategy = {
        type = prepare_for_war
        id = ENG
        value = 200
    }
}
GER_nww_support_threatened_democracies = {
    reversed = yes
    allowed = {
        original_tag = GER
    }
    enable = {
        exists = yes
        is_subject = no
        NOT = {
            original_tag = GER
        }
        NOT = {
            has_government = fascism
        }
        NOT = {
            has_government = communism
        }
        has_war = yes
        any_enemy_country = {
            OR = {
                has_government = communism
                has_government = fascism
            }
        }
        NOT = {
            has_war_with = GER
        }
        GER = {
            has_focus_tree = GER_focus
            has_government = democratic
            is_subject = no
            has_completed_focus = GER_arsenal_of_democracy
        }
    }
    abort_when_not_enabled = yes
    ai_strategy = {
        type = send_volunteers_desire
        id = GER
        value = 200
    }
    ai_strategy = {
        type = protect
        id = GER
        value = 200
    }
    ai_strategy = {
        type = diplo_action_desire
        id = GER
        target = guarantee
        value = 200
    }
}
GER_nww_schlieffen_reborn_HOL = {
    allowed = {
        original_tag = GER
    }
    enable = {
        has_focus_tree = GER_focus
        has_government = neutrality
        has_completed_focus = GER_schlieffen_reborn
        is_subject = no
        HOL = {
            exists = yes
            is_subject = no
        }
        NOT = {
            is_ally_with = HOL
        }
    }
    abort_when_not_enabled = yes
    ai_strategy = {
        type = declare_war
        id = HOL
        value = 200
    }
    ai_strategy = {
        type = prepare_for_war
        id = HOL
        value = 200
    }
}
GER_nww_schlieffen_reborn_BEL = {
    allowed = {
        original_tag = GER
    }
    enable = {
        has_focus_tree = GER_focus
        has_government = neutrality
        has_completed_focus = GER_schlieffen_reborn
        is_subject = no
        BEL = {
            exists = yes
            is_subject = no
        }
        NOT = {
            is_ally_with = BEL
        }
    }
    abort_when_not_enabled = yes
    ai_strategy = {
        type = declare_war
        id = BEL
        value = 200
    }
    ai_strategy = {
        type = prepare_for_war
        id = BEL
        value = 200
    }
}
GER_nww_drang_nach_osten_expanded_SOV = {
    allowed = {
        original_tag = GER
    }
    enable = {
        has_focus_tree = GER_focus
        has_government = fascism
        has_completed_focus = GER_drang_nach_osten_expanded
        is_subject = no
        SOV = {
            exists = yes
            is_subject = no
        }
        NOT = {
            is_ally_with = SOV
        }
    }
    abort_when_not_enabled = yes
    ai_strategy = {
        type = declare_war
        id = SOV
        value = 200
    }
    ai_strategy = {
        type = prepare_for_war
        id = SOV
        value = 200
    }
}
GER_nww_drang_nach_osten_expanded_MKN = {
    allowed = {
        original_tag = GER
    }
    enable = {
        has_focus_tree = GER_focus
        has_government = fascism
        has_completed_focus = GER_drang_nach_osten_expanded
        is_subject = no
        MKN = {
            exists = yes
            is_subject = no
        }
        NOT = {
            is_ally_with = MKN
        }
    }
    abort_when_not_enabled = yes
    ai_strategy = {
        type = declare_war
        id = MKN
        value = 200
    }
    ai_strategy = {
        type = prepare_for_war
        id = MKN
        value = 200
    }
}
GER_nww_hegemony_over_europe_focus_DEN = {
    allowed = {
        original_tag = GER
    }
    enable = {
        has_focus_tree = GER_focus
        has_government = fascism
        has_completed_focus = GER_hegemony_over_europe_focus
        is_subject = no
        DEN = {
            exists = yes
            is_subject = no
        }
        NOT = {
            is_ally_with = DEN
        }
    }
    abort_when_not_enabled = yes
    ai_strategy = {
        type = declare_war
        id = DEN
        value = 200
    }
    ai_strategy = {
        type = prepare_for_war
        id = DEN
        value = 200
    }
}
GER_nww_hegemony_over_europe_focus_NOR = {
    allowed = {
        original_tag = GER
    }
    enable = {
        has_focus_tree = GER_focus
        has_government = fascism
        has_completed_focus = GER_hegemony_over_europe_focus
        is_subject = no
        NOR = {
            exists = yes
            is_subject = no
        }
        NOT = {
            is_ally_with = NOR
        }
    }
    abort_when_not_enabled = yes
    ai_strategy = {
        type = declare_war
        id = NOR
        value = 200
    }
    ai_strategy = {
        type = prepare_for_war
        id = NOR
        value = 200
    }
}
GER_nww_hegemony_over_europe_focus_SWE = {
    allowed = {
        original_tag = GER
    }
    enable = {
        has_focus_tree = GER_focus
        has_government = fascism
        has_completed_focus = GER_hegemony_over_europe_focus
        is_subject = no
        SWE = {
            exists = yes
            is_subject = no
        }
        NOT = {
            is_ally_with = SWE
        }
    }
    abort_when_not_enabled = yes
    ai_strategy = {
        type = declare_war
        id = SWE
        value = 200
    }
    ai_strategy = {
        type = prepare_for_war
        id = SWE
        value = 200
    }
}
GER_nww_hegemony_over_europe_focus_FIN = {
    allowed = {
        original_tag = GER
    }
    enable = {
        has_focus_tree = GER_focus
        has_government = fascism
        has_completed_focus = GER_hegemony_over_europe_focus
        is_subject = no
        FIN = {
            exists = yes
            is_subject = no
        }
        NOT = {
            is_ally_with = FIN
        }
    }
    abort_when_not_enabled = yes
    ai_strategy = {
        type = declare_war
        id = FIN
        value = 200
    }
    ai_strategy = {
        type = prepare_for_war
        id = FIN
        value = 200
    }
}
GER_nww_hegemony_over_europe_focus_SWI = {
    allowed = {
        original_tag = GER
    }
    enable = {
        has_focus_tree = GER_focus
        has_government = fascism
        has_completed_focus = GER_hegemony_over_europe_focus
        is_subject = no
        SWI = {
            exists = yes
            is_subject = no
        }
        NOT = {
            is_ally_with = SWI
        }
    }
    abort_when_not_enabled = yes
    ai_strategy = {
        type = declare_war
        id = SWI
        value = 200
    }
    ai_strategy = {
        type = prepare_for_war
        id = SWI
        value = 200
    }
}
GER_nww_challenge_moscow_SOV = {
    allowed = {
        original_tag = GER
    }
    enable = {
        has_focus_tree = GER_focus
        has_government = communism
        has_completed_focus = GER_challenge_moscow
        is_subject = no
        SOV = {
            exists = yes
            is_subject = no
        }
        NOT = {
            is_ally_with = SOV
        }
    }
    abort_when_not_enabled = yes
    ai_strategy = {
        type = declare_war
        id = SOV
        value = 200
    }
    ai_strategy = {
        type = prepare_for_war
        id = SOV
        value = 200
    }
}
GER_nww_anti_imperialist_crusade_FRA = {
    allowed = {
        original_tag = GER
    }
    enable = {
        has_focus_tree = GER_focus
        has_government = democratic
        has_completed_focus = GER_anti_imperialist_crusade
        is_subject = no
        FRA = {
            exists = yes
            is_subject = no
            NOT = {
                has_government = democratic
            }
        }
        NOT = {
            is_ally_with = FRA
        }
    }
    abort_when_not_enabled = yes
    ai_strategy = {
        type = declare_war
        id = FRA
        value = 200
    }
    ai_strategy = {
        type = prepare_for_war
        id = FRA
        value = 200
    }
}
GER_nww_anti_imperialist_crusade_ENG = {
    allowed = {
        original_tag = GER
    }
    enable = {
        has_focus_tree = GER_focus
        has_government = democratic
        has_completed_focus = GER_anti_imperialist_crusade
        is_subject = no
        ENG = {
            exists = yes
            is_subject = no
            NOT = {
                has_government = democratic
            }
        }
        NOT = {
            is_ally_with = ENG
        }
    }
    abort_when_not_enabled = yes
    ai_strategy = {
        type = declare_war
        id = ENG
        value = 200
    }
    ai_strategy = {
        type = prepare_for_war
        id = ENG
        value = 200
    }
}
```

### `common/ai_strategy/GER_pacing.txt`

```pdx
GER_nww_historical_restraint_AUS = {
    enable = {
        original_tag = GER
        has_focus_tree = GER_focus
        is_historical_focus_on = yes
        date < 1939.1.1
    }
    abort_when_not_enabled = yes
    ai_strategy = {
        type = declare_war
        id = AUS
        value = -1000
    }
    ai_strategy = {
        type = antagonize
        id = AUS
        value = -1000
    }
}
GER_nww_historical_restraint_CZE = {
    enable = {
        original_tag = GER
        has_focus_tree = GER_focus
        is_historical_focus_on = yes
        date < 1939.1.1
    }
    abort_when_not_enabled = yes
    ai_strategy = {
        type = declare_war
        id = CZE
        value = -1000
    }
    ai_strategy = {
        type = antagonize
        id = CZE
        value = -1000
    }
}
GER_nww_historical_restraint_LTB = {
    enable = {
        original_tag = GER
        has_focus_tree = GER_focus
        is_historical_focus_on = yes
        date < 1940.1.1
    }
    abort_when_not_enabled = yes
    ai_strategy = {
        type = declare_war
        id = LTB
        value = -1000
    }
    ai_strategy = {
        type = antagonize
        id = LTB
        value = -1000
    }
}
GER_nww_historical_restraint_POL = {
    enable = {
        original_tag = GER
        has_focus_tree = GER_focus
        is_historical_focus_on = yes
        date < 1940.1.1
    }
    abort_when_not_enabled = yes
    ai_strategy = {
        type = declare_war
        id = POL
        value = -1000
    }
    ai_strategy = {
        type = antagonize
        id = POL
        value = -1000
    }
}
GER_nww_historical_restraint_MKN = {
    enable = {
        original_tag = GER
        has_focus_tree = GER_focus
        is_historical_focus_on = yes
        date < 1941.1.1
    }
    abort_when_not_enabled = yes
    ai_strategy = {
        type = declare_war
        id = MKN
        value = -1000
    }
    ai_strategy = {
        type = antagonize
        id = MKN
        value = -1000
    }
}
GER_nww_historical_restraint_UKR = {
    enable = {
        original_tag = GER
        has_focus_tree = GER_focus
        is_historical_focus_on = yes
        date < 1941.1.1
    }
    abort_when_not_enabled = yes
    ai_strategy = {
        type = declare_war
        id = UKR
        value = -1000
    }
    ai_strategy = {
        type = antagonize
        id = UKR
        value = -1000
    }
}
GER_nww_historical_restraint_SOV = {
    enable = {
        original_tag = GER
        has_focus_tree = GER_focus
        is_historical_focus_on = yes
        date < 1941.1.1
    }
    abort_when_not_enabled = yes
    ai_strategy = {
        type = declare_war
        id = SOV
        value = -1000
    }
    ai_strategy = {
        type = antagonize
        id = SOV
        value = -1000
    }
}
```

### `common/ai_strategy/GER_politics.txt`

```pdx
NWW_GER_ltb_restraint = {
    enable = {
        original_tag = GER
        has_focus_tree = GER_focus
        date < 1939.1.1
    }
    abort_when_not_enabled = yes
    ai_strategy = {
        type = declare_war
        id = LTB
        value = -1000
    }
    ai_strategy = {
        type = antagonize
        id = LTB
        value = -1000
    }
}
NWW_GER_pol_restraint = {
    enable = {
        original_tag = GER
        has_focus_tree = GER_focus
        date < 1939.1.1
    }
    abort_when_not_enabled = yes
    ai_strategy = {
        type = declare_war
        id = POL
        value = -1000
    }
    ai_strategy = {
        type = antagonize
        id = POL
        value = -1000
    }
}
NWW_GER_ukr_restraint = {
    enable = {
        original_tag = GER
        has_focus_tree = GER_focus
        date < 1939.1.1
    }
    abort_when_not_enabled = yes
    ai_strategy = {
        type = declare_war
        id = UKR
        value = -1000
    }
    ai_strategy = {
        type = antagonize
        id = UKR
        value = -1000
    }
}
NWW_GER_mkn_restraint = {
    enable = {
        original_tag = GER
        has_focus_tree = GER_focus
        date < 1939.1.1
    }
    abort_when_not_enabled = yes
    ai_strategy = {
        type = declare_war
        id = MKN
        value = -1000
    }
    ai_strategy = {
        type = antagonize
        id = MKN
        value = -1000
    }
}
NWW_GER_sov_restraint = {
    enable = {
        original_tag = GER
        has_focus_tree = GER_focus
        date < 1939.1.1
    }
    abort_when_not_enabled = yes
    ai_strategy = {
        type = declare_war
        id = SOV
        value = -1000
    }
    ai_strategy = {
        type = antagonize
        id = SOV
        value = -1000
    }
}
```

### `common/ai_strategy_plans/GER_alternate_strategy_plan.txt`

```pdx

```

### `common/ai_strategy_plans/GER_historical.txt`

```pdx
NWW_GER_historical = {
    name = GER_nww_historical_plan
    desc = GER_nww_historical_plan_desc
    allowed = {
        original_tag = GER
    }
    enable = {
        is_historical_focus_on = yes
        has_focus_tree = GER_focus
    }
    abort = {
        is_subject = yes
    }
    ai_national_focuses = {
        GER_the_gilded_colossus
        GER_fund_the_reichswehr
        GER_krupp_and_thyssen
        GER_the_kaiser_endures
        GER_prussian_traditions
        GER_1
        GER_nww_electrical_grid
        GER_5
        GER_6
        GER_mitteleuropa_trade
        GER_guardians_of_the_reich
        GER_nww_prague_network
        GER_the_potsdam_coup
        GER_dissolve_the_reichstag
        GER_nww_silesian_steel
        GER_3
        GER_7
        GER_nww_machine_tools
        GER_nww_arsenal_contracts
        GER_nww_industrial_standards
        GER_the_austrian_question
        GER_nww_technical_colleges
        GER_4
        GER_8
        GER_reign_in_mitteleuropa
        GER_2
        GER_nww_freight_corridors
        GER_nww_merchant_contracts
        GER_nww_export_credit
        GER_nww_investment_guarantees
        GER_crush_eastern_syndicates
        GER_gott_mit_uns
        GER_9
        GER_10
        GER_nww_industrial_research
        GER_schlieffen_reborn
        GER_strike_the_west
        GER_the_second_naval_race
    }
    focus_factors = {
        GER_empower_the_chancellor = 0
    }
    weight = {
        factor = 100
    }
}
```

### `common/ai_strategy_plans/GER_historical_strategy_plan.txt`

```pdx

```

### `common/factions/templates/GER_templates.txt`

```pdx
faction_template_GER_mitteleuropa = {
    name = GER_mitteleuropa_faction
    manifest = faction_manifest_defense_of_democracy_allies
    icon = GFX_faction_icon_allies
    default_rules = {
        joining_rule_non_fascist
        joining_rule_has_no_offensive_war
        faction_peace_rule_liberation_focus
        change_leader_rule_industry
    }
}
```

### `events/GER_bohemian_events.txt`

```pdx
add_namespace = nww_ger_bohemia
country_event = {
    id = nww_ger_bohemia.1
    title = nww_ger_bohemia.1.t
    desc = nww_ger_bohemia.1.d
    picture = GFX_report_event_generic_conference
    is_triggered_only = yes
    option = {
        name = nww_ger_bohemia.1.a
    }
}
```

### `events/GER_events.txt`

```pdx
add_namespace = ger_crisis
add_namespace = ger_news
country_event = {
    id = ger_crisis.1
    title = ger_crisis.1.t
    desc = ger_crisis.1.d
    picture = GFX_report_event_generic_funeral
    fire_only_once = yes
    trigger = {
        tag = GER
        has_focus_tree = GER_focus
        date > 1936.8.1
        NOT = {
            has_country_flag = ger_wilhelm_ii_dead
        }
    }
    mean_time_to_happen = {
        days = 60
        modifier = {
            factor = 0
            date > 1936.12.30
        }
    }
    immediate = {
        set_country_flag = ger_wilhelm_ii_dead
        complete_national_focus = GER_end_of_an_era
        GER_wilhelm_ii = {
            remove_country_leader_trait = ger_aging_monarch
        }
        retire_character = GER_wilhelm_ii
        GER_wilhelm_iii = {
            add_country_leader_role = {
                country_leader = {
                    ideology = GER_imperial_autocracy
                    expire = 1965.1.1
                    traits = {

                    }
                }
                promote_leader = yes
            }
        }
        news_event = {
            id = ger_news.1
        }
    }
    option = {
        name = ger_crisis.1.a
    }
}
news_event = {
    id = ger_news.1
    title = ger_news.1.t
    desc = ger_news.1.d
    picture = GFX_report_event_generic_funeral
    major = yes
    is_triggered_only = yes
    option = {
        name = ger_news.1.a
    }
}
country_event = {
    id = ger_crisis.10
    title = ger_crisis.10.t
    desc = ger_crisis.10.d
    picture = GFX_report_event_generic_conference
    is_triggered_only = yes
    trigger = {
        date > 1938.12.31
        tag = AUS
        is_subject = no
        NOT = {
            has_war_with = GER
        }
        GER = {
            exists = yes
            is_subject = no
            has_focus_tree = GER_focus
            has_government = neutrality
            has_completed_focus = GER_the_austrian_question
        }
    }
    option = {
        name = ger_crisis.10.a
        ai_chance = {
            factor = 20
            modifier = {
                factor = 0
                is_historical_focus_on = yes
            }
        }
        if = {
            limit = {
                date > 1938.12.31
                is_subject = no
                NOT = {
                    has_war_with = GER
                }
                GER = {
                    exists = yes
                    is_subject = no
                    has_government = neutrality
                }
            }
            GER = {
                set_autonomy = {
                    target = AUS
                    autonomy_state = autonomy_puppet
                    end_wars = no
                    end_civil_wars = no
                }
            }
        }
    }
    option = {
        name = ger_crisis.10.b
        ai_chance = {
            factor = 80
        }
        if = {
            limit = {
                date > 1938.12.31
                is_subject = no
                NOT = {
                    has_war_with = GER
                }
                GER = {
                    exists = yes
                    is_subject = no
                    has_government = neutrality
                }
            }
            GER = {
                if = {
                    limit = {
                        NOT = {
                            has_wargoal_against = AUS
                        }
                    }
                    if = {
                        limit = {
                            nww_GER_ai_can_target_AUS = yes
                        }
                        create_wargoal = {
                            type = puppet_wargoal_focus
                            target = AUS
                        }
                    }
                }
            }
            GER_nww_austrian_guarantee = yes
        }
    }
}
country_event = {
    id = ger_crisis.20
    title = ger_crisis.20.t
    desc = ger_crisis.20.d
    picture = GFX_report_event_generic_conference
    is_triggered_only = yes
    trigger = {
        OR = {
            tag = LTB
            tag = POL
        }
        is_subject = no
        NOT = {
            has_war_with = GER
        }
        GER = {
            exists = yes
            is_subject = no
            has_focus_tree = GER_focus
            has_government = neutrality
            has_completed_focus = GER_reign_in_mitteleuropa
        }
        date > 1938.12.31
    }
    option = {
        name = ger_crisis.20.a
        ai_chance = {
            factor = 35
            modifier = {
                factor = 0
                tag = POL
                OR = {
                    has_completed_focus = POL_the_colonels_regime
                    has_completed_focus = POL_endecja_ascendant
                    AND = {
                        is_historical_focus_on = yes
                        NOT = {
                            has_completed_focus = POL_pragmatic_deal
                        }
                        NOT = {
                            has_country_flag = POL_ai_german
                        }
                    }
                }
            }
            modifier = {
                add = 65
                tag = POL
                has_completed_focus = POL_pragmatic_deal
            }
            modifier = {
                factor = 0
                is_historical_focus_on = yes
                tag = LTB
            }
        }
        if = {
            limit = {
                is_subject = no
                NOT = {
                    has_war_with = GER
                }
                GER = {
                    exists = yes
                    is_subject = no
                    has_government = neutrality
                }
                date > 1938.12.31
            }
            GER = {
                set_autonomy = {
                    target = ROOT
                    autonomy_state = autonomy_puppet
                    end_wars = no
                    end_civil_wars = no
                }
            }
        }
    }
    option = {
        name = ger_crisis.20.b
        ai_chance = {
            factor = 65
            modifier = {
                factor = 0
                tag = POL
                has_completed_focus = POL_pragmatic_deal
            }
        }
        if = {
            limit = {
                is_subject = no
                NOT = {
                    has_war_with = GER
                }
                GER = {
                    exists = yes
                    is_subject = no
                    has_government = neutrality
                }
                date > 1938.12.31
            }
            set_country_flag = ger_mitteleuropa_refused
            custom_effect_tooltip = GER_mitteleuropa_refusal_tt
            GER = {
                nww_GER_mitteleuropa_refusal_wargoals = yes
            }
        }
    }
}
country_event = {
    id = ger_crisis.30
    title = ger_crisis.30.t
    desc = ger_crisis.30.d
    picture = GFX_report_event_generic_conference
    is_triggered_only = yes
    trigger = {
        tag = AUS
        is_subject = no
        has_war = no
        FROM = {
            exists = yes
            original_tag = GER
            has_focus_tree = GER_focus
            has_government = democratic
            is_subject = no
            has_completed_focus = GER_the_austrian_referendum
        }
        NOT = {
            has_war_with = FROM
        }
        FROM = {
            has_war = no
        }
    }
    option = {
        name = ger_crisis.30.a
        ai_chance = {
            factor = 25
        }
        trigger = {
            has_government = democratic
        }
        if = {
            limit = {
                tag = AUS
                is_subject = no
                has_war = no
                FROM = {
                    exists = yes
                    original_tag = GER
                    has_focus_tree = GER_focus
                    has_government = democratic
                    is_subject = no
                    has_completed_focus = GER_the_austrian_referendum
                }
                NOT = {
                    has_war_with = FROM
                }
                FROM = {
                    has_war = no
                }
                has_government = democratic
            }
            FROM = {
                annex_country = {
                    target = ROOT
                    transfer_troops = yes
                }
            }
        }
    }
    option = {
        name = ger_crisis.30.b
        ai_chance = {
            factor = 50
        }
        trigger = {
            OR = {
                is_in_faction = no
                is_in_faction_with = FROM
            }
        }
        if = {
            limit = {
                tag = AUS
                is_subject = no
                has_war = no
                FROM = {
                    exists = yes
                    original_tag = GER
                    has_focus_tree = GER_focus
                    has_government = democratic
                    is_subject = no
                    has_completed_focus = GER_the_austrian_referendum
                }
                NOT = {
                    has_war_with = FROM
                }
                FROM = {
                    has_war = no
                }
                OR = {
                    is_in_faction = no
                    is_in_faction_with = FROM
                }
                FROM = {
                    OR = {
                        is_in_faction = no
                        is_faction_leader = yes
                    }
                }
            }
            FROM = {
                nww_GER_establish_mitteleuropa = yes
                add_to_faction = ROOT
            }
        }
    }
    option = {
        name = ger_crisis.30.c
        ai_chance = {
            factor = 25
        }
    }
}
country_event = {
    id = ger_crisis.40
    title = ger_crisis.40.t
    desc = ger_crisis.40.d
    picture = GFX_report_event_generic_conference
    is_triggered_only = yes
    trigger = {
        tag = AUS
        is_subject = no
        has_war = no
        FROM = {
            exists = yes
            original_tag = GER
            has_focus_tree = GER_focus
            has_government = fascism
            is_subject = no
            has_completed_focus = GER_anschluss_by_force
        }
        NOT = {
            has_war_with = FROM
        }
    }
    option = {
        name = ger_crisis.40.a
        ai_chance = {
            factor = 10
        }
        if = {
            limit = {
                tag = AUS
                is_subject = no
                has_war = no
                FROM = {
                    exists = yes
                    original_tag = GER
                    has_focus_tree = GER_focus
                    has_government = fascism
                    is_subject = no
                    has_completed_focus = GER_anschluss_by_force
                }
                NOT = {
                    has_war_with = FROM
                }
            }
            FROM = {
                annex_country = {
                    target = ROOT
                    transfer_troops = yes
                }
            }
        }
    }
    option = {
        name = ger_crisis.40.b
        ai_chance = {
            factor = 90
        }
        if = {
            limit = {
                tag = AUS
                is_subject = no
                has_war = no
                FROM = {
                    exists = yes
                    original_tag = GER
                    has_focus_tree = GER_focus
                    has_government = fascism
                    is_subject = no
                    has_completed_focus = GER_anschluss_by_force
                }
                NOT = {
                    has_war_with = FROM
                }
            }
            FROM = {
                if = {
                    limit = {
                        NOT = {
                            has_wargoal_against = AUS
                        }
                    }
                    if = {
                        limit = {
                            nww_GER_ai_can_target_AUS = yes
                        }
                        create_wargoal = {
                            type = annex_everything
                            target = AUS
                        }
                    }
                }
            }
            GER_nww_austrian_guarantee = yes
        }
    }
}
country_event = {
    id = ger_crisis.50
    title = ger_crisis.50.t
    desc = ger_crisis.50.d
    picture = GFX_report_event_generic_conference
    is_triggered_only = yes
    trigger = {
        OR = {
            tag = LTB
            tag = POL
        }
        is_subject = no
        has_war = no
        NOT = {
            has_country_flag = ger_economic_community_accepted
        }
        FROM = {
            exists = yes
            original_tag = GER
            has_focus_tree = GER_focus
            has_government = democratic
            is_subject = no
            has_completed_focus = GER_mitteleuropa_economic_community
        }
        NOT = {
            has_war_with = FROM
        }
        FROM = {
            has_war = no
            is_faction_leader = yes
        }
        OR = {
            is_in_faction = no
            is_in_faction_with = FROM
        }
    }
    option = {
        name = ger_crisis.50.a
        ai_chance = {
            factor = 75
        }
        if = {
            limit = {
                OR = {
                    tag = LTB
                    tag = POL
                }
                is_subject = no
                has_war = no
                NOT = {
                    has_country_flag = ger_economic_community_accepted
                }
                FROM = {
                    exists = yes
                    original_tag = GER
                    has_focus_tree = GER_focus
                    has_government = democratic
                    is_subject = no
                    has_completed_focus = GER_mitteleuropa_economic_community
                }
                NOT = {
                    has_war_with = FROM
                }
                FROM = {
                    has_war = no
                    is_faction_leader = yes
                }
                OR = {
                    is_in_faction = no
                    is_in_faction_with = FROM
                }
            }
            set_country_flag = ger_economic_community_accepted
            FROM = {
                add_to_faction = ROOT
                add_offsite_building = {
                    type = industrial_complex
                    level = 1
                }
            }
        }
    }
    option = {
        name = ger_crisis.50.b
        ai_chance = {
            factor = 25
        }
    }
}
country_event = {
    id = ger_crisis.60
    title = ger_crisis.60.t
    desc = ger_crisis.60.d
    picture = GFX_report_event_generic_conference
    is_triggered_only = yes
    trigger = {
        tag = SOV
        is_subject = no
        has_government = communism
        FROM = {
            exists = yes
            original_tag = GER
            has_focus_tree = GER_focus
            has_government = communism
            is_subject = no
            has_completed_focus = GER_berlin_moscow_axis
        }
        NOT = {
            has_war_with = FROM
        }
        OR = {
            is_faction_leader = yes
            is_in_faction = no
            is_in_faction_with = FROM
        }
        FROM = {
            OR = {
                is_in_faction = no
                is_in_faction_with = ROOT
            }
        }
    }
    option = {
        name = ger_crisis.60.a
        ai_chance = {
            factor = 80
        }
        if = {
            limit = {
                tag = SOV
                is_subject = no
                has_government = communism
                FROM = {
                    exists = yes
                    original_tag = GER
                    has_focus_tree = GER_focus
                    has_government = communism
                    is_subject = no
                    has_completed_focus = GER_berlin_moscow_axis
                }
                NOT = {
                    has_war_with = FROM
                }
                OR = {
                    is_faction_leader = yes
                    is_in_faction = no
                    is_in_faction_with = FROM
                }
                FROM = {
                    OR = {
                        is_in_faction = no
                        is_in_faction_with = ROOT
                    }
                }
            }
            if = {
                limit = {
                    NOT = {
                        is_in_faction_with = FROM
                    }
                }
                if = {
                    limit = {
                        is_in_faction = no
                    }
                    create_faction_from_template = {
                        template = faction_template_comintern
                        name = GER_berlin_moscow_faction
                    }
                }
                add_to_faction = FROM
            }
        }
    }
    option = {
        name = ger_crisis.60.b
        ai_chance = {
            factor = 20
        }
    }
}
country_event = {
    id = ger_crisis.70
    title = ger_crisis.70.t
    desc = ger_crisis.70.d
    picture = GFX_report_event_generic_conference
    is_triggered_only = yes
    fire_only_once = yes
    trigger = {
        GER_nww_red_rhine_offer_valid = yes
    }
    option = {
        name = ger_crisis.70.a
        trigger = {
            GER_nww_red_rhine_revolt_ready = yes
        }
        ai_chance = {
            factor = 40
            modifier = {
                factor = 3
                has_stability < 0.40
            }
        }
        if = {
            limit = {
                GER_nww_red_rhine_offer_valid = yes
                GER_nww_red_rhine_revolt_ready = yes
            }
            start_civil_war = {
                ideology = communism
                size = 0.30
            }
        }
    }
    option = {
        name = ger_crisis.70.b
        ai_chance = {
            factor = 30
        }
        if = {
            limit = {
                GER_nww_red_rhine_offer_valid = yes
            }
            add_popularity = {
                ideology = communism
                popularity = 0.15
            }
            add_stability = -0.05
        }
    }
    option = {
        name = ger_crisis.70.c
        ai_chance = {
            factor = 60
        }
        if = {
            limit = {
                GER_nww_red_rhine_offer_valid = yes
            }
            add_political_power = -50
            add_stability = -0.05
            add_popularity = {
                ideology = communism
                popularity = -0.05
            }
        }
    }
}
```

### `history/countries/GER - Germany.txt`

```pdx
capital = 64
if = {
    limit = {
        NOT = {
            has_dlc = "No Step Back"
        }
    }
    set_oob = GER_1936
}
if = {
    limit = {
        has_dlc = "No Step Back"
    }
    set_oob = GER_1936_nsb
}
add_breakthrough_progress = {
    specialization = specialization_land
    value = 1.0
}
add_breakthrough_progress = {
    specialization = specialization_naval
    value = 0.8
}
add_breakthrough_progress = {
    specialization = specialization_air
    value = 0.3
}
set_grand_doctrine = new_mobile_warfare
set_grand_doctrine = new_convoy_raiding
set_grand_doctrine = new_battlefield_support
if = {
    limit = {
        has_dlc = "By Blood Alone"
    }
    set_air_oob = GER_1936_air_bba
    set_technology = {
        aa_lmg = 1
        aa_cannon_1 = 1
        engines_1 = 1
        engines_2 = 1
        early_bombs = 1
        aircraft_construction = 1
        iw_small_airframe = 1
        basic_small_airframe = 1
        iw_medium_airframe = 1
        basic_medium_airframe = 1
        iw_large_airframe = 1
        air_torpedoe_1 = 1
        bba_early_transport_plane = 1
    }
    else = {
        set_air_oob = GER_1936_air_legacy
        set_technology = {
            early_fighter = 1
            fighter1 = 1
            early_bomber = 1
            tactical_bomber1 = 1
            strategic_bomber1 = 1
            CAS1 = 1
            naval_bomber1 = 1
            early_transport_plane = 1
        }
    }
}
if = {
    limit = {
        has_dlc = "La Resistance"
        has_dlc = "By Blood Alone"
    }
    set_technology = {
        photo_reconnaisance = 1
    }
}
starting_train_buffer = 2
set_fuel_ratio = 0.8
set_technology = {
    infantry_weapons = 1
    infantry_weapons1 = 1
    tech_recon = 1
    tech_support = 1
    tech_engineers = 1
    tech_mountaineers = 1
    tech_trucks = 1
    motorised_infantry = 1
    gw_artillery = 1
    interwar_antiair = 1
    basic_train = 1
    synth_oil_experiments = 1
    fuel_silos = 1
    fuel_refining = 1
}
if = {
    limit = {
        NOT = {
            has_dlc = "No Step Back"
        }
    }
    set_technology = {
        gwtank = 1
        basic_light_tank = 1
        improved_light_tank = 1
        basic_heavy_tank = 1
    }
}
if = {
    limit = {
        has_dlc = "No Step Back"
    }
    set_technology = {
        gwtank_chassis = 1
        basic_light_tank_chassis = 1
        improved_light_tank_chassis = 1
        basic_heavy_tank_chassis = 1
        engine_tech_1 = 1
    }
}
if = {
    limit = {
        not = {
            has_dlc = "Man the Guns"
        }
    }
    set_technology = {
        early_submarine = 1
        basic_submarine = 1
        early_destroyer = 1
        basic_destroyer = 1
        early_light_cruiser = 1
        basic_light_cruiser = 1
        early_heavy_cruiser = 1
        basic_heavy_cruiser = 1
        early_battleship = 1
        basic_battleship = 1
        early_battlecruiser = 1
        transport = 1
    }
    set_naval_oob = GER_1936_naval
}
if = {
    limit = {
        has_dlc = "Man the Guns"
    }
    set_technology = {
        basic_naval_mines = 1
        submarine_mine_laying = 1
        early_ship_hull_light = 1
        basic_ship_hull_light = 1
        early_ship_hull_cruiser = 1
        basic_ship_hull_cruiser = 1
        early_ship_hull_heavy = 1
        basic_ship_hull_heavy = 1
        panzerschiffe = 1
        pre_dreadnoughts = 1
        early_ship_hull_submarine = 1
        basic_ship_hull_submarine = 1
        mtg_transport = 1
        basic_torpedo = 1
        improved_ship_torpedo_launcher = 1
        basic_battery = 1
        basic_light_battery = 1
        basic_heavy_battery = 1
        basic_depth_charges = 1
        sonar = 1
        basic_cruiser_armor_scheme = 1
    }
    set_naval_oob = GER_1936_naval_mtg
}
if = {
    limit = {
        has_dlc = "La Resistance"
    }
    set_technology = {
        armored_car1 = 1
    }
}
set_variable = {
    GER_monthly_consumer_goods_start = 0.03
}
set_variable = {
    GER_change_monthly_CG_vichy_france = 0.005
}
set_variable = {
    GER_change_monthly_CG_price_controls = 0.005
}
set_variable = {
    GER_change_monthly_CG_occupied_states = 0.005
}
set_variable = {
    GER_expected_consumer_goods_penalty = 0.1
}
set_variable = {
    GER_factory_output_penalty = 0.2
}
set_variable = {
    GER_dockyard_output_penalty = 0.2
}
set_variable = {
    GER_reduce_russian_CG_bonus = 0
}
set_variable = {
    GER_monthly_consumer_goods_increase = GER_monthly_consumer_goods_start
}
set_variable = {
    GER_industrial_consumer_goods_factor = 0.1
}
set_variable = {
    GER_industrial_civilian_intel_to_others = -25
}
set_variable = {
    GER_industrial_army_intel_to_others = -25
}
set_variable = {
    GER_industrial_navy_intel_to_others = -25
}
set_variable = {
    GER_industrial_airforce_intel_to_others = -25
}
set_variable = {
    GER_industrial_production_speed_arms_factory_factor = 0.1
}
set_variable = {
    GER_industrial_production_speed_dockyard_factor = 0.1
}
set_variable = {
    GER_industrial_industrial_capacity_factory = 0
}
set_variable = {
    GER_industrial_industrial_capacity_dockyard = 0
}
set_variable = {
    GER_industrial_production_lack_of_resource_penalty_factor = 0
}
set_variable = {
    GER_industrial_conversion_cost_civ_to_mil_factor = 0
}
set_variable = {
    GER_industrial_industry_air_damage_factor = 0
}
set_variable = {
    GER_industrial_resource_trade_cost_bonus_per_factory = 0
}
set_variable = {
    GER_industrial_production_speed_buildings_factor = 0
}
set_variable = {
    GER_industrial_research_speed_factor = 0
}
set_variable = {
    GER_industrial_economy_cost_factor = 0
}
set_variable = {
    GER_industrial_trade_laws_cost_factor = 0
}
set_variable = {
    GER_recovering_economy_modifier_local_resources_factor = 0
}
set_variable = {
    GER_industrial_production_factory_max_efficiency_factor = 0
}
set_variable = {
    GER_industrial_production_factory_efficiency_gain_factor = 0
}
set_variable = {
    GER_industrial_production_factory_start_efficiency_factor = 0
}
set_variable = {
    GER_industrial_line_change_production_efficiency_factor = 0
}
set_variable = {
    GER_industrial_equipment_conversion_speed = 0
}
set_variable = {
    GER_industrial_consumer_goods_expected_value = 0
}
set_variable = {
    GER_economic_crash_consumer_goods = 0.75
}
set_variable = {
    GER_wunderwaffen_special_project_speed_factor = 0
}
set_variable = {
    GER_wunderwaffen_sp_tag_tank_speed_factor = 0
}
set_variable = {
    GER_wunderwaffen_sp_air_helicopter_speed_factor = 0
}
set_variable = {
    GER_wunderwaffen_sp_tag_jet_speed_factor = 0
}
set_variable = {
    GER_wunderwaffen_sp_tag_rocket_speed_factor = 0
}
set_variable = {
    GER_wunderwaffen_sp_commercial_nuclear_reactor_speed_factor = 0
}
set_variable = {
    GER_wunderwaffen_sp_nuclear_bomb_speed_factor = 0
}
set_variable = {
    GER_wunderwaffen_sp_nuclear_reactor_speed_factor = 0
}
set_variable = {
    GER_wunderwaffen_sp_nuclear_warheads_speed_factor = 0
}
set_variable = {
    GER_wunderwaffen_sp_tag_artillery_speed_factor = 0
}
set_variable = {
    GER_wunderwaffen_sp_naval_modern_battleship_speed_factor = 0
}
set_variable = {
    GER_wunderwaffen_sp_naval_modern_carrier_speed_factor = 0
}
set_variable = {
    GER_wunderwaffen_production_speed_nuclear_reactor_factor = 0
}
set_variable = {
    GER_wunderwaffen_production_speed_nuclear_facility_factor = 0
}
set_variable = {
    GER_wunderwaffen_production_speed_facility_factor = 0
}
set_variable = {
    GER_wunderwaffen_sp_tag_submarine_speed_factor = 0
}
set_variable = {
    GER_wunderwaffen_sp_air_intercontinental_bomber_speed_factor = 0
}
set_variable = {
    GER_wunderwaffen_sp_air_mothership_aircraft_speed_factor = 0
}
set_variable = {
    GER_wehrwirtschaft_local_resources_factor = 0
}
set_variable = {
    GER_wehrwirtschaft_production_speed_buildings_factor = 0
}
set_variable = {
    GER_wehrwirtschaft_production_oil_factor = 0
}
set_variable = {
    GER_wehrwirtschaft_production_speed_synthetic_refinery_factor = 0
}
set_variable = {
    GER_wehrwirtschaft_production_speed_fuel_silo_factor = 0
}
set_variable = {
    GER_military_army_armor_attack_factor = 0
}
set_variable = {
    GER_military_army_armor_speed_factor = 0
}
set_variable = {
    GER_military_org_loss_when_moving = 0
}
set_variable = {
    GER_military_motorized_attack_factor = 0
}
set_variable = {
    GER_military_mechanized_attack_factor = 0
}
set_variable = {
    GER_military_army_infantry_attack_factor = 0
}
set_variable = {
    GER_military_army_artillery_attack_factor = 0
}
set_variable = {
    GER_military_army_org_factor = 0.05
}
set_variable = {
    GER_military_planning_speed = 0.25
}
set_variable = {
    GER_military_supply_consumption_factor = 0.15
}
set_variable = {
    GER_military_equipment_capture = 0
}
set_variable = {
    GER_military_initiative_factor = 0
}
set_variable = {
    GER_military_army_fuel_consumption_factor = 0
}
set_variable = {
    GER_military_coordination_bonus = 0
}
set_variable = {
    GER_military_air_superiority_bonus_in_combat = 0
}
set_variable = {
    GER_military_max_dig_in_factor = 0
}
set_variable = {
    GER_military_army_artillery_defence_factor = 0
}
set_variable = {
    GER_military_special_forces_cap = 0
}
set_variable = {
    GER_military_acclimatization_hot_climate_gain_factor = 0
}
set_variable = {
    GER_military_acclimatization_cold_climate_gain_factor = 0
}
set_variable = {
    GER_military_land_doctrine_cost_factor = 0
}
set_variable = {
    GER_military_modifier_army_sub_unit_militia_attack_factor = 0
}
set_variable = {
    GER_military_modifier_army_sub_unit_militia_defence_factor = 0
}
set_variable = {
    GER_military_modifier_army_sub_unit_militia_max_org_factor = 0
}
set_variable = {
    GER_military_experience_gain_army_factor = 0
}
set_variable = {
    GER_military_army_morale_factor = 0
}
set_variable = {
    GER_military_mobilization_speed = 0
}
set_variable = {
    GER_military_minimum_training_level = 0
}
set_variable = {
    GER_military_unit_leader_as_advisor_cp_cost_factor = 0
}
set_variable = {
    GER_military_command_power_gain_mult = 0
}
add_dynamic_modifier = {
    modifier = GER_army_modifier
}
set_variable = {
    GER_military_naval_heavy_gun_hit_chance_factor = 0
}
set_variable = {
    GER_military_screening_efficiency = 0
}
set_variable = {
    GER_military_screening_without_screens = 0.1
}
set_variable = {
    GER_military_navy_max_range_factor = 0
}
set_variable = {
    GER_military_convoy_raiding_efficiency_factor = 0
}
set_variable = {
    GER_military_naval_light_gun_hit_chance_factor = 0
}
set_variable = {
    GER_military_naval_hit_chance = 0
}
set_variable = {
    GER_military_naval_defense_factor = -0.1
}
add_dynamic_modifier = {
    modifier = GER_navy_fascist_modifier
}
set_variable = {
    GER_military_air_accidents_factor = 0.10
}
set_variable = {
    GER_military_air_manpower_requirement_factor = 0.10
}
set_variable = {
    GER_military_air_agility_factor = 0
}
set_variable = {
    GER_military_air_ace_generation_chance_factor = 0
}
set_variable = {
    GER_military_air_nav_efficiency = 0
}
set_variable = {
    GER_military_air_cas_efficiency = 0
}
set_variable = {
    GER_military_air_strategic_bomber_bombing_factor = 0
}
set_variable = {
    GER_military_air_range_factor = 0
}
set_variable = {
    GER_military_air_fuel_consumption_factor = 0
}
add_dynamic_modifier = {
    modifier = GER_airforce_modifier
}
set_variable = {
    number_of_states_getting_dockyards = 0
}
set_variable = {
    crossing_the_atlantic_max_states_for_dockyards = 10
}
set_variable = {
    GER_fort_construction_cp_cost = 25
}
set_variable = {
    GER_fort_construction_pp_cost = 15
}
set_variable = {
    GER_fort_construction_cp_payment = -25
}
set_variable = {
    GER_fort_construction_pp_payment = -15
}
set_variable = {
    var = ger_gateway_to_europe_influence
    value = 0
}
set_variable = {
    var = wehrmacht_anger
    value = 0
}
set_variable = {
    var = ss_anger
    value = 0
}
set_variable = {
    GER_narvik_shipments = 0
}
set_variable = {
    GER_narvik_civs = 0
}
set_variable = {
    GER_communist_intel_drift_defence_factor = 0.2
}
set_variable = {
    GER_communist_intel_communism_drift = 0.05
}
set_variable = {
    GER_communist_intel_operative_slot = 0
}
set_variable = {
    GER_communist_intel_stability_factor = 0
}
set_variable = {
    GER_communist_intel_operation_cost = 0
}
set_variable = {
    GER_communist_intel_subversive_activities_upkeep = 0
}
set_variable = {
    GER_communist_intel_intel_network_gain = 0
}
set_variable = {
    GER_communist_intel_decryption_factor = 0
}
set_variable = {
    GER_communist_intel_encryption_factor = 0
}
set_variable = {
    GER_politburo_defensive_war_stability_factor = 0
}
set_variable = {
    GER_politburo_offensive_war_stability_factor = 0
}
set_variable = {
    GER_politburo_party_popularity_stability_factor = 0
}
set_variable = {
    GER_politburo_weekly_manpower = 0
}
set_variable = {
    GER_politburo_stability_factor = 0
}
set_variable = {
    GER_politburo_conscription = 0
}
set_variable = {
    GER_politburo_democratic_drift = 0
}
set_variable = {
    GER_politburo_political_power_factor = 0
}
set_variable = {
    GER_politburo_resistance_growth = 0
}
set_variable = {
    GER_politburo_compliance_growth = 0
}
set_variable = {
    GER_politburo_subjects_autonomy_gain = 0
}
set_variable = {
    GER_politburo_conscription_factor = 0
}
set_variable = {
    GER_alfred_rosenberg_modifier_subjects_autonomy_gain = -0.2
}
set_variable = {
    GER_alfred_rosenberg_modifier_consumer_goods_factor = 0
}
set_variable = {
    GER_alfred_rosenberg_modifier_production_speed_arms_factory_factor = 0
}
set_variable = {
    GER_alfred_rosenberg_modifier_industrial_capacity_factory = 0
}
set_variable = {
    GER_max_alfred_rosenberg_upgrades = 10
}
set_variable = {
    GER_count_down_alfred_rosenberg_upgrades = GER_max_alfred_rosenberg_upgrades
}
set_variable = {
    GER_total_reichskommissariats = 0
}
set_variable = {
    GER_rnd_programs_modifier_research_speed_factor = 0.01
}
set_variable = {
    GER_rnd_programs_modifier_allies_count = 1
}
set_variable = {
    GER_industrial_relocation_resources_country_resource_oil = 0
}
set_variable = {
    GER_industrial_relocation_resources_country_resource_tungsten = 0
}
set_variable = {
    GER_industrial_relocation_resources_country_resource_chromium = 0
}
set_variable = {
    GER_puppet_economies_integration_cap = 3
}
set_variable = {
    GER_puppet_economies_integration_days = 365
}
set_variable = {
    GER_military_intelligence_service_operative_slot = 0
}
set_variable = {
    GER_military_intelligence_service_intelligence_agency_defense = 0
}
set_variable = {
    GER_military_intelligence_service_agency_upgrade_time = 0
}
set_variable = {
    GER_military_intelligence_service_boost_ideology_mission_factor = 0
}
set_variable = {
    GER_military_intelligence_service_master_ideology_drift = 0
}
set_variable = {
    GER_military_intelligence_service_encryption_factor = 0
}
set_variable = {
    GER_military_intelligence_service_decryption_factor = 0
}
set_variable = {
    GER_military_intelligence_service_subversive_activites_upkeep = 0
}
set_variable = {
    GER_military_intelligence_service_consumer_goods_factor = 0
}
set_variable = {
    GER_military_intelligence_service_decryption_power = 0
}
set_variable = {
    GER_military_intelligence_service_intel_network_gain_factor = 0
}
set_variable = {
    GER_military_intelligence_root_out_resistance_effectiveness_factor = 0
}
set_variable = {
    GER_occupied_states_europe = 0
}
set_variable = {
    GER_capitulated_major_countries = 0
}
set_variable = {
    GER_num_of_occupied_states = 0
}
set_variable = {
    GER_wunderwaffe_research_speed_bonus = 0.1
}
set_variable = {
    GER_hitlers_blunders_variable = 0
}
set_variable = {
    GER_inner_circle_days_to_start_focus = 75
}
set_variable = {
    GER_inner_circle_random_days = 45
}
set_variable = {
    GER_ascended_advisor_1 = 0
}
set_variable = {
    GER_ascended_advisor_2 = 0
}
set_variable = {
    GER_ascended_advisor_3 = 0
}
set_variable = {
    GER_wonder_weapons_focus_advisor = 0
}
set_variable = {
    GER_optimize_reich_service_focus_advisor = 0
}
set_variable = {
    GER_total_control_over_domestic_affairs_focus_advisor = 0
}
set_variable = {
    GER_industrialist_prevailed = 0
}
set_research_slots = 4
set_convoys = 200
IF = {
    limit = {
        has_dlc = Gotterdammerung
    }
    set_stability = 0.7
    ELSE = {
        set_stability = 0.75
    }
}
set_war_support = 0.3
1939.1.1 = {
    add_named_threat = {
        threat = 40
        name = 1939_bookmark_threat
    }
    set_war_support = 0.7
    add_political_power = 1000
    add_command_power = 80
    set_research_slots = 5
    add_ideas = {
        henschel
        ig_faben
        walther_funk
        GER_reinhard_heydrich
        GER_franz_seldte
        ludwig_beck
        gerd_von_rundstedt
        goering
        war_economy
        extensive_conscription
    }
    set_autonomy = {
        target = SLO
        autonomous_state = autonomy_puppet
    }
    give_military_access = SLO
    create_wargoal = {
        type = take_state_focus
        target = POL
        generator = {
            72
            88
            90
            87
            86
            762
            807
            85
        }
    }
    create_import = {
        resource = oil
        factories = 2
        exporter = SOV
    }
    set_country_flag = GER_constructed_the_westwall
    if = {
        limit = {
            has_dlc = "La Resistance"
        }
        create_intelligence_agency = yes
    }
    unlock_national_focus = GER_molotov_ribbentrop_pact
    every_other_country = {
        limit = {
            has_government = fascism
        }
        add_opinion_modifier = {
            target = GER
            modifier = MR_pact_fascists
        }
    }
    diplomatic_relation = {
        country = SOV
        relation = non_aggression_pact
    }
    add_opinion_modifier = {
        target = SOV
        modifier = MR_pact
    }
    complete_national_focus = GER_construct_the_reichsautobahn
    complete_national_focus = GER_institute_price_controls
    complete_national_focus = GER_fuhrerprinzip
    complete_national_focus = GER_party_chancellor_bormann
    complete_national_focus = GER_accelerate_the_rearmament_program
    complete_national_focus = GER_kdf_wagen_factories
    complete_national_focus = GER_develop_modern_maneuver_warfare
    complete_national_focus = GER_adopt_new_panzer_doctrine
    complete_national_focus = GER_coal_liquefaction
    complete_national_focus = GER_ascension_of_speer
    complete_national_focus = GER_establish_buna_werke
    complete_national_focus = GER_expanding_the_luftwaffe
    complete_national_focus = GER_aeronautical_research_institute
    complete_national_focus = GER_concentrated_armament_program
    complete_national_focus = GER_panzer_troops_school
    complete_national_focus = GER_ascension_of_goebbels
    complete_national_focus = GER_reorganize_the_wehrmacht
    complete_national_focus = GER_advanced_panzer_research
    complete_national_focus = GER_bribe_senior_officers
    complete_national_focus = GER_befriend_japan
    unlock_national_focus = GER_remilitarize_the_rhineland
    unlock_national_focus = GER_anti_comintern_pact
    unlock_national_focus = GER_fortify_the_vaterland
    unlock_national_focus = GER_anschluss
    unlock_national_focus = GER_demand_sudetenland
    unlock_national_focus = GER_first_vienna_award
    unlock_national_focus = GER_fate_of_czechoslovakia
    unlock_national_focus = GER_reassert_eastern_claims
    unlock_national_focus = GER_danzig_or_war
    unlock_national_focus = GER_the_four_year_plan
    unlock_national_focus = GER_develop_heraeus_facilities
    unlock_national_focus = GER_legion_condor
    unlock_national_focus = GER_autarky_efforts
    add_ideas = autarkic_economy
    add_dynamic_modifier = {
        modifier = GER_wehrwirtschaft_modifier
    }
    every_other_country = {
        limit = {
            is_in_faction_with = PREV
        }
        add_opinion_modifier = {
            target = GER
            modifier = GER_autarky_trade_opinion
        }
        GER = {
            add_opinion_modifier = {
                target = PREV
                modifier = GER_german_trade_opinion
            }
        }
    }
    unlock_national_focus = GER_establish_the_reichswerke
    set_variable = {
        GER_industrial_consumer_goods_factor = 0.71
    }
    set_country_flag = GER_inactivate_price_control_measures_flag
    add_to_variable = {
        GER_wehrwirtschaft_local_resources_factor = 0.05
        tooltip = local_resources_factor_tt
    }
    set_global_flag = end_of_czechoslovakia
    set_global_flag = olympics_1936
    set_variable = {
        var = GER_mefo_bill_counter
        value = 90
    }
    set_country_flag = GER_todt_was_ascended_flag
    complete_national_focus = GER_form_organization_todt
    clr_country_flag = GER_speer_was_ascended_flag
    set_country_flag = {
        flag = GER_speer_was_ascended_flag
        days = 1095
        value = 1
    }
    complete_national_focus = GER_employ_philipp_holzmann
    clr_country_flag = GER_goebbels_was_ascended_flag
    set_country_flag = {
        flag = GER_goebbels_was_ascended_flag
        days = 900
        value = 1
    }
    complete_national_focus = GER_ministry_of_public_enlightenment
    complete_national_focus = GER_fund_the_film_department
    complete_national_focus = GER_propaganda_master
    add_stability = -0.05
    add_war_support = -0.05
    complete_national_focus = GER_optimize_reich_labour_service
    complete_national_focus = GER_glorify_party_rallies
    complete_national_focus = GER_total_control_over_domestic_affairs
    add_political_power = -150
    activate_decision = GER_reichsprotektorat_bohemia_moravia
    set_nationality = {
        target_country = RKH
        character = GER_konstantin_von_neurath
    }
    RKH = {
        GER_konstantin_von_neurath = {
            add_country_leader_role = {
                promote_leader = yes
                country_leader = {
                    ideology = nazism
                    expire = 1960.1.1
                    traits = {
                        GER_reichsprotektor_trait
                    }
                }
            }
        }
        set_research_slots = 3
    }
    if = {
        limit = {
            has_dlc = "Peace For Our Time"
        }
        unlock_national_focus = GER_integrate_czech_manufacturers
        RKH = {
            add_ideas = {
                CZE_form_the_government_army_idea
            }
        }
    }
    clr_country_flag = GER_inner_circle_cd_flag
    complete_special_project = {
        project = sp:sp_naval_midget_submarine
        scientist = GER_hellmuth_walter
        state = 56
    }
    IF = {
        limit = {
            has_dlc = "No Step Back"
        }
        complete_special_project = {
            project = sp:sp_land_flamethrower_tank
            scientist = GER_eduard_grote
            state = 64
        }
    }
    set_technology = {
        interwar_artillery = 1
        interwar_antitank = 1
        infantry_weapons2 = 1
        improved_infantry_weapons = 1
        support_weapons = 1
        support_weapons2 = 1
        paratroopers = 1
        electronic_mechanical_engineering = 1
        radio = 1
        cavity_magnatron = 1
        mechanical_computing = 1
        computing_machine = 1
        basic_encryption = 1
        basic_decryption = 1
        basic_machine_tools = 1
        improved_machine_tools = 1
        advanced_machine_tools = 1
        oil_processing = 1
        fuel_refining2 = 1
        construction1 = 1
        construction2 = 1
        construction3 = 1
        construction4 = 1
        dispersed_industry = 1
        dispersed_industry2 = 1
        dispersed_industry3 = 1
        dispersed_industry4 = 1
        basic_fortification_tech = 1
    }
    set_grand_doctrine = new_mobile_warfare
    set_grand_doctrine = new_convoy_raiding
    set_grand_doctrine = new_battlefield_support
    set_sub_doctrine = mobile_infantry
    add_mastery = {
        amount = 200
        sub_doctrine = mobile_infantry
    }
    set_sub_doctrine = mission_type_tactics
    add_mastery = {
        amount = 100
        sub_doctrine = mission_type_tactics
    }
    set_sub_doctrine = mobile_recon_and_assault
    add_mastery = {
        amount = 150
        sub_doctrine = mobile_recon_and_assault
    }
    set_sub_doctrine = air_subdoctrine_tactical_flexibility
    add_mastery = {
        amount = 100
        sub_doctrine = air_subdoctrine_tactical_flexibility
    }
    set_sub_doctrine = air_subdoctrine_dive_bombers
    add_mastery = {
        amount = 50
        sub_doctrine = air_subdoctrine_dive_bombers
    }
    complete_special_project = {
        project = sp:sp_air_radar
        scientist = GER_konrad_zuse
        state = 62
    }
    if = {
        limit = {
            NOT = {
                has_dlc = "No Step Back"
            }
        }
        set_technology = {
            basic_medium_tank = 1
        }
        set_oob = GER_1939
    }
    if = {
        limit = {
            has_dlc = "No Step Back"
        }
        set_technology = {
            basic_medium_tank_chassis = 1
        }
        set_oob = GER_1939_nsb
    }
    if = {
        limit = {
            not = {
                has_dlc = "Man the Guns"
            }
        }
        set_technology = {
            basic_heavy_cruiser = 1
            improved_heavy_cruiser = 1
            improved_battleship = 1
            early_carrier = 1
            basic_carrier = 1
            improved_carrier = 1
        }
        set_naval_oob = GER_1939_naval_legacy
    }
    if = {
        limit = {
            has_dlc = "Man the Guns"
        }
        set_technology = {
            improved_ship_hull_cruiser = 1
            basic_ship_hull_heavy = 1
            early_ship_hull_carrier = 1
            basic_ship_hull_carrier = 1
            improved_heavy_battery = 1
            basic_heavy_armor_scheme = 1
        }
        set_naval_oob = GER_1939_naval_mtg
    }
    if = {
        limit = {
            has_dlc = "By Blood Alone"
        }
        set_air_oob = GER_1939_air_bba
        else = {
            set_air_oob = GER_1939_air_legacy
            set_technology = {
                CAS2 = 1
                heavy_fighter1 = 1
            }
        }
    }
}
set_politics = {
    ruling_party = neutrality
    last_election = 1933.3.5
    election_frequency = 48
    elections_allowed = no
}
set_popularities = {
    democratic = 20
    fascism = 10
    communism = 5
    neutrality = 65
}
add_ideas = {
    limited_exports
    limited_conscription
    partial_economic_mobilisation
    GER_imperial_overstretch
    GER_master_of_mitteleuropa
    GER_prussian_martial_spirit
}
recruit_character = GER_wilhelm_pieck
recruit_character = GER_konrad_adenauer
recruit_character = GER_adolf_hitler
recruit_character = GER_albert_kesselring
recruit_character = GER_alfred_jodl
recruit_character = GER_alfred_saalwachter
recruit_character = GER_erhard_milch
recruit_character = GER_erich_bey
recruit_character = GER_erich_raeder
recruit_character = GER_erich_von_manstein
recruit_character = GER_ernst_udet
recruit_character = GER_ernsteberhard_hell
recruit_character = GER_erwin_rommel
recruit_character = GER_erwin_von_witzleben
recruit_character = GER_ewald_von_kleist
recruit_character = GER_fedor_von_bock
recruit_character = GER_felix_steiner
recruit_character = GER_ferdinand_schorner
recruit_character = GER_franz_halder
recruit_character = GER_friedrich_paulus
recruit_character = GER_friedrich_schulz
recruit_character = GER_georg_von_kuchler
recruit_character = GER_georghans_reinhardt
recruit_character = GER_gerd_von_rundstedt
recruit_character = GER_hermann_goring
recruit_character = GER_gotthard_heinrici
recruit_character = GER_gunther_lutjens
recruit_character = GER_gunther_von_kluge
recruit_character = GER_hasso_von_manteuffel
recruit_character = GER_heinz_guderian
recruit_character = GER_heisenberg
recruit_character = GER_hermann_boehm
recruit_character = GER_hermann_hoth
recruit_character = GER_hugo_sperrle
recruit_character = GER_johannes_blaskowitz
recruit_character = GER_karl_donitz
recruit_character = GER_kurt_student
recruit_character = GER_ludwig_beck
recruit_character = GER_maximilian_von_weichs
recruit_character = GER_otto_ciliax
recruit_character = GER_paul_hausser
recruit_character = GER_ritter_von_greim
recruit_character = GER_sepp_dietrich
recruit_character = GER_viktor_schutze
recruit_character = GER_von_braun
recruit_character = GER_walter_kruger
recruit_character = GER_walter_model
recruit_character = GER_walther_von_brauchitsch
recruit_character = GER_walther_wever
recruit_character = GER_werner_von_fritsch
recruit_character = GER_wilhelm_keitel
recruit_character = GER_wilhelm_list
recruit_character = GER_wilhelm_marschall
recruit_character = GER_wilhelm_ritter_von_leeb
recruit_character = GER_wolfram_von_richthofen
recruit_character = GER_heinrich_himmler
recruit_character = GER_walther_funk
recruit_character = GER_hjalmar_schacht
recruit_character = GER_julius_leber
recruit_character = GER_albert_speer
recruit_character = GER_hans_oster
recruit_character = GER_theodor_heuss
recruit_character = GER_fritz_todt
recruit_character = GER_joachim_von_ribbentrop
recruit_character = GER_ernst_thalmann
recruit_character = GER_rudolf_hess
recruit_character = GER_martin_bormann
recruit_character = GER_wilhelm_canaris
recruit_character = GER_joseph_goebbels
recruit_character = GER_konstantin_von_neurath
recruit_character = GER_alfred_hugenberg
recruit_character = GER_kurt_schumacher
recruit_character = GER_wilhelm_ii
recruit_character = GER_wilhelm_iii
recruit_character = GER_victoria
recruit_character = GER_august_von_mackensen
recruit_character = GER_alexander_von_falkenhausen
recruit_character = GER_werner_von_blomberg
recruit_character = GER_oswald_lutz
recruit_character = GER_walther_nehring
recruit_character = GER_hans_krebs
recruit_character = GER_rolf_carls
recruit_character = GER_helmuth_wilberg
recruit_character = GER_josef_kammhuber
recruit_character = GER_robert_knauss
recruit_character = GER_alfred_becker
recruit_character = GER_walter_dornberger
recruit_character = GER_alfred_rosenberg
recruit_character = GER_reinhard_heydrich
recruit_character = GER_leni_riefenstahl
recruit_character = GER_franz_seldte
recruit_character = GER_hanns_kerrl
recruit_character = GER_ludwig_erhard
recruit_character = GER_paul_von_lettow_vorbeck
recruit_character = GER_carl_friedrich_goerdeler
recruit_character = GER_wilhelm_iv
recruit_character = GER_eva_braun
recruit_character = GER_peter_adolf_thiessen
recruit_character = GER_gustav_ludwig_hertz
recruit_character = GER_eduard_grote
recruit_character = GER_ferdinand_porsche
recruit_character = GER_erwin_aders
recruit_character = GER_hermann_burkhardt
recruit_character = GER_ulrich_gabler
recruit_character = GER_hans_von_ohain
recruit_character = GER_max_kramer
recruit_character = GER_kurt_tank
recruit_character = GER_hellmuth_walter
recruit_character = GER_manfred_von_ardenne
recruit_character = GER_konrad_zuse
if = {
    limit = {
        has_dlc = Gotterdammerung
    }
    recruit_character = GER_jurgen_von_blumenthal
    recruit_character = GER_hans_vogel
    recruit_character = GER_adolf_friedrich_von_mecklenburg
    recruit_character = GER_wilhelm_von_gayl
    recruit_character = GER_andreas_hermes
    recruit_character = GER_hans_luther
    recruit_character = GER_hermann_erhardt
    recruit_character = GER_dietrich_bonhoeffer
    recruit_character = GER_oberste_heeresleitung_character
    recruit_character = GER_franz_ritter_von_epp
    recruit_character = GER_walter_ulbricht
    if = {
        limit = {
            has_dlc = "La Resistance"
        }
        recruit_character = GER_wilhelm_zaisser
    }
    recruit_character = GER_otto_ruhle
    recruit_character = GER_hermann_duncker
    recruit_character = GER_august_thalheimer
    recruit_character = GER_heinrich_brandler
    recruit_character = GER_bernhard_bastlein
    recruit_character = GER_vincenz_muller
    recruit_character = GER_hans_kahle
    recruit_character = GER_hans_marchwitza
    recruit_character = GER_arno_von_lenski
    recruit_character = GER_otto_strasser
    recruit_character = GER_otto_grotewohl
    recruit_character = GER_henrich_focke
}
if = {
    limit = {
        OR = {
            has_dlc = Gotterdammerung
            has_dlc = "No Step Back"
        }
    }
    recruit_character = GER_karl_heinrich_emil_becker
}
if = {
    limit = {
        has_dlc = "La Resistance"
    }
    GER_create_operative_nikolaus_ritter = yes
    GER_create_operative_erich_gimpel = yes
    GER_create_operative_fritz_duquesne = yes
}
if = {
    limit = {
        NOT = {
            has_dlc = "Man the Guns"
        }
    }
    create_equipment_variant = {
        name = Königsberg
        type = light_cruiser_1
        parent_version = 0
        upgrades = {
            ship_reliability_upgrade = 2
            ship_engine_upgrade = 2
            ship_gun_upgrade = 2
            ship_anti_air_upgrade = 2
        }
        obsolete = yes
    }
    create_equipment_variant = {
        name = Deutschland
        type = heavy_cruiser_1
        parent_version = 0
        upgrades = {
            ship_reliability_upgrade = 1
            ship_engine_upgrade = 1
            ship_armor_upgrade = 1
            ship_gun_upgrade = 2
        }
    }
}
if = {
    limit = {
        has_dlc = "No Step Back"
    }
    create_equipment_variant = {
        name = Leichttraktor
        type = light_tank_chassis_0
        parent_version = 0
        modules = {
            main_armament_slot = tank_small_cannon
            turret_type_slot = tank_light_two_man_tank_turret
            suspension_type_slot = tank_christie_suspension
            armor_type_slot = tank_riveted_armor
            engine_type_slot = tank_gasoline_engine
            special_type_slot_1 = tank_radio_1
        }
        upgrades = {
            tank_nsb_engine_upgrade = 2
            tank_nsb_armor_upgrade = 2
        }
        obsolete = yes
        icon = GFX_GER_gwtank_medium
    }
    create_equipment_variant = {
        name = "Panzer I Ausf. A"
        type = light_tank_chassis_1
        parent_version = 0
        modules = {
            main_armament_slot = tank_heavy_machine_gun
            turret_type_slot = tank_light_one_man_tank_turret
            suspension_type_slot = tank_christie_suspension
            armor_type_slot = tank_riveted_armor
            engine_type_slot = tank_gasoline_engine
            special_type_slot_1 = tank_radio_1
        }
        upgrades = {
            tank_nsb_engine_upgrade = 5
            tank_nsb_armor_upgrade = 1
        }
        icon = GFX_GER_basic_light_tank_medium
        obsolete = yes
    }
    create_equipment_variant = {
        name = Neubaufahrzeug
        type = heavy_tank_chassis_1
        parent_version = 0
        modules = {
            main_armament_slot = tank_close_support_gun
            turret_type_slot = tank_heavy_three_man_tank_turret
            suspension_type_slot = tank_bogie_suspension
            armor_type_slot = tank_riveted_armor
            engine_type_slot = tank_gasoline_engine
            special_type_slot_1 = tank_radio_1
            special_type_slot_2 = secondary_turret_hmg
            special_type_slot_3 = secondary_turret_hmg
            special_type_slot_4 = secondary_turret_hmg
        }
        upgrades = {
            tank_nsb_engine_upgrade = 6
            tank_nsb_armor_upgrade = 2
        }
        icon = GFX_GER_basic_heavy_tank_medium
    }
    create_equipment_variant = {
        name = "Panzer II Ausf. A"
        type = light_tank_chassis_2
        design_team = mio:GER_daimler_benz_organization
        parent_version = 0
        obsolete = yes
        modules = {
            main_armament_slot = tank_auto_cannon
            turret_type_slot = tank_light_two_man_tank_turret
            suspension_type_slot = tank_christie_suspension
            armor_type_slot = tank_riveted_armor
            engine_type_slot = tank_gasoline_engine
            special_type_slot_1 = tank_radio_1
        }
        upgrades = {
            tank_nsb_engine_upgrade = 3
            tank_nsb_armor_upgrade = 2
        }
        icon = GFX_GER_improved_light_tank_medium
    }
    create_equipment_variant = {
        name = "Panzer II"
        type = light_tank_chassis_2
        design_team = mio:GER_daimler_benz_organization
        parent_version = 1
        modules = {
            main_armament_slot = tank_auto_cannon
            turret_type_slot = tank_light_two_man_tank_turret
            suspension_type_slot = tank_christie_suspension
            armor_type_slot = tank_riveted_armor
            engine_type_slot = tank_gasoline_engine
            special_type_slot_1 = tank_radio_1
        }
        upgrades = {
            tank_nsb_engine_upgrade = 3
            tank_nsb_armor_upgrade = 3
        }
        icon = GFX_GER_improved_light_tank_medium
    }
    create_equipment_variant = {
        name = "StuG III"
        type = medium_tank_destroyer_chassis_1
        design_team = mio:GER_alkett_organization
        parent_version = 0
        modules = {
            main_armament_slot = tank_medium_cannon
            turret_type_slot = tank_medium_fixed_superstructure_turret
            suspension_type_slot = tank_bogie_suspension
            armor_type_slot = tank_welded_armor
            engine_type_slot = tank_gasoline_engine
            special_type_slot_1 = tank_radio_1
        }
        upgrades = {
            tank_nsb_engine_upgrade = 4
            tank_nsb_armor_upgrade = 3
        }
    }
}
if = {
    limit = {
        has_dlc = "Man the Guns"
    }
    create_equipment_variant = {
        name = Deutschland
        type = ship_hull_cruiser_panzerschiff
        name_group = GER_PZ_HISTORICAL
        parent_version = 0
        modules = {
            fixed_ship_anti_air_slot = ship_anti_air_1
            fixed_ship_battery_slot = ship_heavy_battery_2
            fixed_ship_secondaries_slot = ship_secondaries_1
            fixed_ship_armor_slot = ship_armor_cruiser_1
            fixed_ship_fire_control_system_slot = ship_fire_control_system_0
            fixed_ship_engine_slot = cruiser_ship_engine_2
            rear_1_custom_slot = ship_torpedo_1
            mid_1_custom_slot = ship_airplane_launcher_1
        }
    }
    create_equipment_variant = {
        name = "Type 24"
        type = ship_hull_light_1
        name_group = GER_TB_HISTORICAL
        parent_version = 0
        modules = {
            fixed_ship_battery_slot = ship_light_battery_1
            fixed_ship_anti_air_slot = empty
            fixed_ship_fire_control_system_slot = ship_fire_control_system_0
            fixed_ship_radar_slot = empty
            fixed_ship_engine_slot = light_ship_engine_1
            fixed_ship_torpedo_slot = ship_torpedo_1
            rear_1_custom_slot = ship_mine_layer_1
        }
        obsolete = yes
    }
    create_equipment_variant = {
        name = "Zerstörer 1934"
        type = ship_hull_light_2
        name_group = GER_DD_HISTORICAL
        parent_version = 0
        modules = {
            fixed_ship_battery_slot = ship_light_battery_2
            fixed_ship_anti_air_slot = ship_anti_air_1
            fixed_ship_fire_control_system_slot = ship_fire_control_system_0
            fixed_ship_radar_slot = empty
            fixed_ship_engine_slot = light_ship_engine_2
            fixed_ship_torpedo_slot = ship_torpedo_1
            mid_1_custom_slot = ship_torpedo_1
            rear_1_custom_slot = ship_mine_layer_1
        }
        obsolete = yes
    }
    create_equipment_variant = {
        name = "Zerstörer 1934A"
        type = ship_hull_light_2
        name_group = GER_DD_HISTORICAL
        parent_version = 0
        modules = {
            fixed_ship_battery_slot = ship_light_battery_2
            fixed_ship_anti_air_slot = ship_anti_air_1
            fixed_ship_fire_control_system_slot = ship_fire_control_system_0
            fixed_ship_radar_slot = empty
            fixed_ship_engine_slot = light_ship_engine_2
            fixed_ship_torpedo_slot = ship_torpedo_1
            mid_1_custom_slot = ship_torpedo_1
            rear_1_custom_slot = ship_depth_charge_1
        }
    }
    create_equipment_variant = {
        name = "Type II"
        type = ship_hull_submarine_1
        name_group = GER_SS_HISTORICAL
        parent_version = 0
        modules = {
            fixed_ship_torpedo_slot = ship_torpedo_sub_1
            fixed_ship_engine_slot = sub_ship_engine_1
            rear_1_custom_slot = empty
        }
        obsolete = yes
    }
    create_equipment_variant = {
        name = "Type VII"
        type = ship_hull_submarine_2
        name_group = GER_SS_HISTORICAL
        parent_version = 0
        modules = {
            fixed_ship_torpedo_slot = ship_torpedo_sub_2
            fixed_ship_engine_slot = sub_ship_engine_1
            rear_1_custom_slot = empty
        }
    }
    create_equipment_variant = {
        name = Königsberg
        type = ship_hull_cruiser_1
        name_group = GER_CL_HISTORICAL
        parent_version = 0
        modules = {
            fixed_ship_battery_slot = ship_light_medium_battery_1
            fixed_ship_anti_air_slot = ship_anti_air_1
            fixed_ship_fire_control_system_slot = ship_fire_control_system_0
            fixed_ship_radar_slot = empty
            fixed_ship_engine_slot = cruiser_ship_engine_2
            fixed_ship_armor_slot = ship_armor_cruiser_1
            mid_1_custom_slot = ship_torpedo_1
            mid_2_custom_slot = ship_light_medium_battery_1
            rear_1_custom_slot = ship_mine_layer_1
        }
        obsolete = yes
    }
    create_equipment_variant = {
        name = Emden
        type = ship_hull_cruiser_1
        name_group = GER_CL_HISTORICAL
        parent_version = 0
        modules = {
            fixed_ship_battery_slot = ship_light_medium_battery_1
            fixed_ship_anti_air_slot = empty
            fixed_ship_fire_control_system_slot = ship_fire_control_system_0
            fixed_ship_radar_slot = empty
            fixed_ship_engine_slot = cruiser_ship_engine_1
            fixed_ship_armor_slot = ship_armor_cruiser_1
            mid_1_custom_slot = ship_light_medium_battery_1
            mid_2_custom_slot = ship_torpedo_1
            rear_1_custom_slot = empty
        }
        obsolete = yes
    }
    create_equipment_variant = {
        name = Bremse
        type = ship_hull_cruiser_1
        name_group = GER_CL_HISTORICAL
        parent_version = 0
        modules = {
            fixed_ship_battery_slot = ship_light_battery_1
            fixed_ship_anti_air_slot = ship_anti_air_1
            fixed_ship_fire_control_system_slot = ship_fire_control_system_0
            fixed_ship_radar_slot = empty
            fixed_ship_engine_slot = cruiser_ship_engine_1
            mid_1_custom_slot = ship_anti_air_1
            mid_2_custom_slot = ship_mine_layer_1
            rear_1_custom_slot = ship_mine_layer_1
        }
        obsolete = yes
    }
    create_equipment_variant = {
        name = Leipzig
        type = ship_hull_cruiser_2
        name_group = GER_CL_HISTORICAL
        parent_version = 0
        modules = {
            fixed_ship_battery_slot = ship_light_medium_battery_1
            fixed_ship_anti_air_slot = ship_anti_air_1
            fixed_ship_fire_control_system_slot = ship_fire_control_system_0
            fixed_ship_radar_slot = empty
            fixed_ship_engine_slot = cruiser_ship_engine_1
            fixed_ship_armor_slot = ship_armor_cruiser_1
            front_1_custom_slot = ship_anti_air_1
            mid_1_custom_slot = ship_torpedo_1
            mid_2_custom_slot = ship_light_medium_battery_1
            rear_1_custom_slot = ship_airplane_launcher_1
        }
    }
    create_equipment_variant = {
        name = "Admiral Hipper"
        type = ship_hull_cruiser_2
        name_group = GER_CA_HISTORICAL
        parent_version = 0
        modules = {
            fixed_ship_battery_slot = ship_medium_battery_2
            fixed_ship_anti_air_slot = ship_anti_air_1
            fixed_ship_fire_control_system_slot = ship_fire_control_system_0
            fixed_ship_radar_slot = empty
            fixed_ship_engine_slot = cruiser_ship_engine_2
            fixed_ship_armor_slot = ship_armor_cruiser_2
            front_1_custom_slot = ship_anti_air_1
            mid_1_custom_slot = ship_torpedo_1
            mid_2_custom_slot = ship_airplane_launcher_1
            rear_1_custom_slot = ship_medium_battery_2
        }
    }
    create_equipment_variant = {
        name = Scharnhorst
        type = ship_hull_heavy_2
        name_group = GER_BB_HISTORICAL
        parent_version = 0
        modules = {
            fixed_ship_battery_slot = ship_heavy_battery_2
            fixed_ship_anti_air_slot = ship_anti_air_1
            fixed_ship_fire_control_system_slot = ship_fire_control_system_0
            fixed_ship_radar_slot = empty
            fixed_ship_engine_slot = heavy_ship_engine_2
            fixed_ship_secondaries_slot = ship_secondaries_1
            fixed_ship_armor_slot = ship_armor_bc_1
            front_1_custom_slot = ship_anti_air_1
            mid_1_custom_slot = empty
            mid_2_custom_slot = ship_secondaries_1
            rear_1_custom_slot = ship_heavy_battery_2
        }
    }
    create_equipment_variant = {
        name = Deutschland
        type = ship_hull_pre_dreadnought
        name_group = GER_PZ_HISTORICAL
        parent_version = 0
        modules = {
            fixed_ship_battery_slot = ship_heavy_battery_1
            fixed_ship_anti_air_slot = ship_anti_air_1
            fixed_ship_fire_control_system_slot = ship_fire_control_system_0
            fixed_ship_radar_slot = empty
            fixed_ship_engine_slot = heavy_ship_engine_2
            fixed_ship_secondaries_slot = ship_secondaries_1
            fixed_ship_armor_slot = ship_armor_bb_1
            front_1_custom_slot = ship_anti_air_1
            mid_1_custom_slot = empty
            rear_1_custom_slot = empty
        }
        obsolete = yes
    }
}
if = {
    limit = {
        NOT = {
            has_dlc = "By Blood Alone"
        }
    }
    create_equipment_variant = {
        name = "Ju 86"
        type = tac_bomber_equipment_0
        design_team = mio:GER_junkers_organization
        upgrades = {
            plane_tac_bomb_upgrade = 5
            plane_range_upgrade = 5
            plane_engine_upgrade = 5
            plane_reliability_upgrade = 5
        }
        obsolete = yes
        icon = GFX_GER_early_bomber_medium
    }
    create_equipment_variant = {
        name = "Do 17"
        type = tac_bomber_equipment_0
        design_team = mio:GER_dornier_organization
        upgrades = {
            plane_tac_bomb_upgrade = 5
            plane_range_upgrade = 1
            plane_engine_upgrade = 1
            plane_reliability_upgrade = 5
        }
        obsolete = yes
    }
}
if = {
    limit = {
        has_dlc = "By Blood Alone"
    }
    create_equipment_variant = {
        name = "Do 23"
        type = medium_plane_airframe_0
        design_team = mio:GER_dornier_organization
        modules = {
            fixed_main_weapon_slot = medium_bomb_bay
            fixed_auxiliary_weapon_slot_1 = empty
            fixed_auxiliary_weapon_slot_2 = empty
            fixed_auxiliary_weapon_slot_3 = empty
            engine_type_slot = engine_1_2x
            special_type_slot_1 = empty
            special_type_slot_2 = empty
            special_type_slot_3 = empty
            special_type_slot_4 = empty
        }
        obsolete = yes
        icon = GFX_GER_early_bomber_medium
    }
    create_equipment_variant = {
        name = "Ju 86"
        type = medium_plane_airframe_0
        design_team = mio:GER_junkers_organization
        modules = {
            fixed_main_weapon_slot = medium_bomb_bay
            fixed_auxiliary_weapon_slot_1 = empty
            fixed_auxiliary_weapon_slot_2 = empty
            fixed_auxiliary_weapon_slot_3 = empty
            engine_type_slot = engine_2_2x
            special_type_slot_1 = lmg_defense_turret_2x
            special_type_slot_2 = fuel_tanks_medium
            special_type_slot_3 = empty
            special_type_slot_4 = empty
        }
        obsolete = yes
        icon = GFX_GER_early_bomber_medium
    }
    create_equipment_variant = {
        name = "He 111"
        type = medium_plane_airframe_1
        modules = {
            fixed_main_weapon_slot = medium_bomb_bay
            fixed_auxiliary_weapon_slot_1 = medium_bomb_bay
            fixed_auxiliary_weapon_slot_2 = empty
            fixed_auxiliary_weapon_slot_3 = empty
            engine_type_slot = engine_2_2x
            special_type_slot_1 = lmg_defense_turret_2x
            special_type_slot_2 = lmg_defense_turret_2x
            special_type_slot_3 = empty
            special_type_slot_4 = empty
        }
        icon = GFX_GER_tactical_bomber1_medium
    }
    create_equipment_variant = {
        name = "Do 17"
        type = medium_plane_airframe_1
        design_team = mio:GER_dornier_organization
        modules = {
            fixed_main_weapon_slot = medium_bomb_bay
            engine_type_slot = engine_1_2x
            special_type_slot_1 = lmg_defense_turret_2x
        }
        icon = GFX_GER_medium_plane_1_medium
    }
    create_equipment_variant = {
        name = "He 51"
        type = small_plane_airframe_0
        modules = {
            fixed_main_weapon_slot = light_mg_2x
            engine_type_slot = engine_1_1x
            special_type_slot_1 = empty
        }
        obsolete = yes
    }
    create_equipment_variant = {
        name = "Hs 123"
        type = small_plane_cas_airframe_0
        modules = {
            fixed_main_weapon_slot = bomb_locks
            engine_type_slot = engine_1_1x
            special_type_slot_1 = empty
        }
        obsolete = yes
        icon = GFX_GER_cv_fighter1_medium
    }
    create_equipment_variant = {
        name = "Bf 109 D"
        type = small_plane_airframe_1
        design_team = mio:GER_messerschmitt_organization
        modules = {
            fixed_main_weapon_slot = light_mg_4x
            engine_type_slot = engine_2_1x
            special_type_slot_1 = empty
        }
        icon = GFX_GER_fighter1_medium
    }
    create_equipment_variant = {
        name = "Ju 87"
        type = small_plane_cas_airframe_1
        design_team = mio:GER_junkers_organization
        modules = {
            fixed_main_weapon_slot = bomb_locks
            engine_type_slot = engine_2_1x
            special_type_slot_1 = lmg_defense_turret
            special_type_slot_2 = dive_brakes_small
        }
        icon = GFX_GER_CAS1_medium
    }
    create_equipment_variant = {
        name = "Do 22"
        type = small_plane_naval_bomber_airframe_1
        modules = {
            fixed_main_weapon_slot = torpedo_mounting
            engine_type_slot = engine_2_1x
            special_type_slot_1 = lmg_defense_turret
            special_type_slot_2 = floats
        }
        icon = GFX_GER_naval_bomber1_medium
    }
}
1939.1.1 = {
    if = {
        limit = {
            NOT = {
                has_dlc = "Man the Guns"
            }
        }
        create_equipment_variant = {
            name = "Type VIIA"
            type = submarine_2
            parent_version = 0
            upgrades = {
                ship_reliability_upgrade = 1
                sub_engine_upgrade = 1
                sub_stealth_upgrade = 1
                sub_torpedo_upgrade = 1
            }
        }
        create_equipment_variant = {
            name = "Zerstörer 1936"
            type = destroyer_2
            parent_version = 0
            upgrades = {
                ship_torpedo_upgrade = 2
                destroyer_engine_upgrade = 2
                ship_ASW_upgrade = 2
                ship_anti_air_upgrade = 2
            }
        }
    }
    if = {
        limit = {
            has_dlc = "Man the Guns"
        }
        create_equipment_variant = {
            name = "Zerstörer 1936"
            type = ship_hull_light_2
            name_group = GER_DD_HISTORICAL
            parent_version = 0
            modules = {
                fixed_ship_battery_slot = ship_light_battery_2
                fixed_ship_anti_air_slot = ship_anti_air_1
                fixed_ship_fire_control_system_slot = ship_fire_control_system_0
                fixed_ship_radar_slot = empty
                fixed_ship_engine_slot = light_ship_engine_2
                fixed_ship_torpedo_slot = ship_torpedo_1
                rear_1_custom_slot = ship_depth_charge_1
            }
        }
        create_equipment_variant = {
            name = Bismarck
            type = ship_hull_heavy_2
            name_group = GER_BB_HISTORICAL
            parent_version = 0
            modules = {
                fixed_ship_battery_slot = ship_heavy_battery_2
                fixed_ship_anti_air_slot = ship_anti_air_1
                fixed_ship_fire_control_system_slot = ship_fire_control_system_0
                fixed_ship_radar_slot = empty
                fixed_ship_engine_slot = heavy_ship_engine_2
                fixed_ship_secondaries_slot = ship_secondaries_1
                fixed_ship_armor_slot = ship_armor_bc_1
                front_1_custom_slot = ship_anti_air_1
                mid_1_custom_slot = empty
                mid_2_custom_slot = ship_secondaries_1
                rear_1_custom_slot = ship_heavy_battery_2
            }
            obsolete = yes
        }
        create_equipment_variant = {
            name = "Ranger Class"
            type = ship_hull_carrier_1
            parent_version = 0
            modules = {
                fixed_ship_deck_slot_1 = ship_deck_space
                fixed_ship_deck_slot_2 = ship_deck_space
                fixed_ship_anti_air_slot = ship_anti_air_1
                fixed_ship_radar_slot = empty
                fixed_ship_engine_slot = carrier_ship_engine_1
                fixed_ship_secondaries_slot = empty
                front_1_custom_slot = ship_deck_space
            }
            obsolete = yes
        }
        create_equipment_variant = {
            name = NWW_Umbau
            type = ship_hull_carrier_conversion_bb
            parent_version = 0
            modules = {
                fixed_ship_deck_slot_1 = ship_deck_space
                fixed_ship_deck_slot_2 = ship_deck_space
                fixed_ship_anti_air_slot = ship_anti_air_1
                fixed_ship_radar_slot = empty
                fixed_ship_engine_slot = heavy_ship_engine_2
                fixed_ship_secondaries_slot = ship_secondaries_1
                mid_1_custom_slot = ship_deck_space
            }
            obsolete = yes
        }
        create_equipment_variant = {
            name = NWW_Trager
            type = ship_hull_carrier_1
            parent_version = 0
            modules = {
                fixed_ship_deck_slot_1 = ship_deck_space
                fixed_ship_deck_slot_2 = ship_deck_space
                fixed_ship_anti_air_slot = ship_anti_air_1
                fixed_ship_radar_slot = empty
                fixed_ship_engine_slot = carrier_ship_engine_1
                fixed_ship_secondaries_slot = empty
                front_1_custom_slot = ship_deck_space
            }
            obsolete = yes
        }
        create_equipment_variant = {
            name = "Graf Zeppelin"
            type = ship_hull_carrier_1
            name_group = GER_CV_HISTORICAL
            parent_version = 0
            modules = {
                fixed_ship_deck_slot_1 = ship_deck_space
                fixed_ship_deck_slot_2 = ship_deck_space
                fixed_ship_anti_air_slot = ship_anti_air_1
                fixed_ship_radar_slot = empty
                fixed_ship_engine_slot = carrier_ship_engine_1
                fixed_ship_secondaries_slot = empty
                front_1_custom_slot = ship_deck_space
            }
            obsolete = yes
        }
    }
    if = {
        limit = {
            has_dlc = "No Step Back"
        }
        create_equipment_variant = {
            name = "Panzer III Ausf. F"
            type = medium_tank_chassis_1
            parent_version = 0
            modules = {
                main_armament_slot = tank_small_cannon_2
                turret_type_slot = tank_medium_three_man_tank_turret
                suspension_type_slot = tank_torsion_bar_suspension
                armor_type_slot = tank_welded_armor
                engine_type_slot = tank_gasoline_engine
                special_type_slot_1 = tank_radio_1
                special_type_slot_2 = smoke_launchers
                special_type_slot_3 = empty
                special_type_slot_4 = empty
            }
            upgrades = {
                tank_nsb_engine_upgrade = 6
                tank_nsb_armor_upgrade = 3
            }
            icon = GFX_GER_basic_medium_tank_medium
        }
        create_equipment_variant = {
            name = "Panzer IV Ausf. C"
            type = medium_tank_chassis_1
            parent_version = 1
            modules = {
                main_armament_slot = tank_close_support_gun
                turret_type_slot = tank_medium_three_man_tank_turret
                suspension_type_slot = tank_bogie_suspension
                armor_type_slot = tank_welded_armor
                engine_type_slot = tank_gasoline_engine
                special_type_slot_1 = tank_radio_1
                special_type_slot_2 = smoke_launchers
                special_type_slot_3 = empty
                special_type_slot_4 = empty
            }
            upgrades = {
                tank_nsb_engine_upgrade = 6
                tank_nsb_armor_upgrade = 3
            }
            icon = GFX_GER_improved_medium_tank_medium
        }
        create_equipment_variant = {
            name = "Panzer 35(t)"
            type = light_tank_chassis_1
            parent_version = 1
            modules = {
                main_armament_slot = tank_high_velocity_cannon
                turret_type_slot = tank_light_two_man_tank_turret
                suspension_type_slot = tank_bogie_suspension
                armor_type_slot = tank_riveted_armor
                engine_type_slot = tank_gasoline_engine
                special_type_slot_1 = tank_radio_1
                special_type_slot_2 = empty
                special_type_slot_3 = empty
                special_type_slot_4 = empty
            }
            upgrades = {
                tank_nsb_engine_upgrade = 3
                tank_nsb_armor_upgrade = 2
            }
            obsolete = yes
            icon = GFX_CZE_basic_light_tank_medium
        }
        create_equipment_variant = {
            name = "Panzer 38(t)"
            type = light_tank_chassis_2
            parent_version = 1
            modules = {
                main_armament_slot = tank_high_velocity_cannon
                turret_type_slot = tank_light_two_man_tank_turret
                suspension_type_slot = tank_bogie_suspension
                armor_type_slot = tank_riveted_armor
                engine_type_slot = tank_gasoline_engine
                special_type_slot_1 = tank_radio_1
                special_type_slot_2 = smoke_launchers
                special_type_slot_3 = empty
                special_type_slot_4 = empty
            }
            upgrades = {
                tank_nsb_engine_upgrade = 3
                tank_nsb_armor_upgrade = 3
            }
            icon = GFX_CZE_improved_light_tank_medium
        }
    }
    if = {
        limit = {
            NOT = {
                has_dlc = "By Blood Alone"
            }
        }
        create_equipment_variant = {
            name = "He 112"
            type = fighter_equipment_1
            upgrades = {
                plane_gun_upgrade = 1
                plane_range_upgrade = 1
                plane_engine_upgrade = 0
                plane_reliability_upgrade = 2
            }
        }
        create_equipment_variant = {
            name = "Bf 109 E"
            type = fighter_equipment_1
            upgrades = {
                plane_gun_upgrade = 2
                plane_range_upgrade = 1
                plane_engine_upgrade = 2
                plane_reliability_upgrade = 4
            }
        }
    }
    if = {
        limit = {
            has_dlc = "By Blood Alone"
        }
        create_equipment_variant = {
            name = "Bf 109 E"
            type = small_plane_airframe_1
            design_team = mio:GER_messerschmitt_organization
            modules = {
                fixed_main_weapon_slot = light_mg_2x
                fixed_auxiliary_weapon_slot_1 = aircraft_cannon_1_2x
                engine_type_slot = engine_2_1x
                special_type_slot_1 = empty
            }
            icon = GFX_GER_fighter1_medium
        }
        create_equipment_variant = {
            name = "Bf 110 C"
            type = small_plane_airframe_1
            design_team = mio:GER_messerschmitt_organization
            modules = {
                fixed_main_weapon_slot = light_mg_4x
                fixed_auxiliary_weapon_slot_1 = aircraft_cannon_1_2x
                engine_type_slot = engine_2_2x
                special_type_slot_1 = empty
            }
            icon = GFX_GER_heavy_fighter1_medium
        }
        create_equipment_variant = {
            name = "He 112"
            type = small_plane_airframe_1
            modules = {
                fixed_main_weapon_slot = light_mg_2x
                fixed_auxiliary_weapon_slot_1 = aircraft_cannon_1_2x
                engine_type_slot = engine_2_1x
                special_type_slot_1 = empty
            }
            icon = GFX_GER_light_plane_1_medium
        }
    }
}
GER_wilhelm_ii = {
    add_country_leader_role = {
        country_leader = {
            ideology = GER_imperial_autocracy
            expire = 1965.1.1
            traits = {
                ger_aging_monarch
            }
        }
        promote_leader = yes
    }
}
if = {
    limit = {
        has_dlc = "Man the Guns"
    }
    create_equipment_variant = {
        name = Bismarck
        type = ship_hull_heavy_2
        name_group = GER_BB_HISTORICAL
        parent_version = 0
        modules = {
            fixed_ship_battery_slot = ship_heavy_battery_2
            fixed_ship_anti_air_slot = ship_anti_air_1
            fixed_ship_fire_control_system_slot = ship_fire_control_system_0
            fixed_ship_radar_slot = empty
            fixed_ship_engine_slot = heavy_ship_engine_2
            fixed_ship_secondaries_slot = ship_secondaries_1
            fixed_ship_armor_slot = ship_armor_bc_1
            front_1_custom_slot = ship_anti_air_1
            mid_1_custom_slot = empty
            mid_2_custom_slot = ship_secondaries_1
            rear_1_custom_slot = ship_heavy_battery_2
        }
        obsolete = yes
    }
}
nww_GER_disable_mefo = yes
nww_GER_initialize_politics = yes
add_ideas = MTG_naval_treaty_adherent
```

## Вызываемые внешние эффекты, события и духи

### `AUS_nww_update_bohemian_spirit` — `common/scripted_effects/AUS_overhaul_effects.txt`

```pdx
AUS_nww_update_bohemian_spirit = {
    GER_nww_update_bohemian_influence = yes
    set_variable = {
        AUS_bohemian_stability = AUS_bohemian_tension
    }
    multiply_variable = {
        AUS_bohemian_stability = -0.01
    }
    set_variable = {
        AUS_bohemian_output = AUS_bohemian_tension
    }
    multiply_variable = {
        AUS_bohemian_output = -0.01
    }
}
```

### `MTG_naval_treaty_adherent` — `common/ideas/zzz_generic.txt`

```pdx
MTG_naval_treaty_adherent = {
    allowed = {
        always = no
    }
    allowed_civil_war = {
        always = no
    }
    removal_cost = -1
    picture = MTG_naval_treaty_adherent
    modifier = {
        production_cost_max_ship_hull_cruiser = 5300
        production_cost_max_ship_hull_heavy = 10000
        production_cost_max_ship_hull_carrier = 9500
    }
}
```

### `nww_aus_overhaul.1` — `events/AUS_overhaul_events.txt`

```pdx
country_event = {
    id = nww_aus_overhaul.1
    title = nww_aus_overhaul.1.t
    desc = nww_aus_overhaul.1.d
    picture = GFX_report_event_election_vote
    is_triggered_only = yes
    trigger = {
        tag = AUS
        NOT = {
            has_country_flag = AUS_nww_bohemia_settled
        }
        NOT = {
            has_country_flag = AUS_nww_bohemia_seceded
        }
        check_variable = {
            var = AUS_bohemian_tension
            value = 10
            compare = greater_than_or_equals
        }
        9 = {
            is_owned_and_controlled_by = AUS
        }
    }
    immediate = {
        AUS_nww_release_bohemia = yes
    }
    option = {
        name = nww_aus_overhaul.1.a
        add_political_power = -50
    }
    option = {
        name = nww_aus_overhaul.1.b
        create_wargoal = {
            type = annex_everything
            target = CZE
        }
        add_war_support = 0.05
    }
}
```

### `AUS_nww_release_bohemia` — `common/scripted_effects/AUS_overhaul_effects.txt`

```pdx
AUS_nww_release_bohemia = {
    if = {
        limit = {
            CZE = {
                exists = no
            }
        }
        set_country_flag = AUS_nww_fresh_bohemian_secession
    }
    set_country_flag = AUS_nww_bohemia_seceded
    remove_mission = AUS_nww_bohemian_drift
    remove_dynamic_modifier = {
        modifier = AUS_nww_bohemian_question
    }
    if = {
        limit = {
            9 = {
                is_owned_and_controlled_by = AUS
            }
        }
        9 = {
            add_core_of = CZE
            transfer_state_to = CZE
        }
    }
    if = {
        limit = {
            69 = {
                is_owned_and_controlled_by = AUS
            }
        }
        69 = {
            add_core_of = CZE
            transfer_state_to = CZE
        }
    }
    if = {
        limit = {
            72 = {
                is_owned_and_controlled_by = AUS
            }
        }
        72 = {
            add_core_of = CZE
            transfer_state_to = CZE
        }
    }
    if = {
        limit = {
            74 = {
                is_owned_and_controlled_by = AUS
            }
        }
        74 = {
            add_core_of = CZE
            transfer_state_to = CZE
        }
    }
    if = {
        limit = {
            75 = {
                is_owned_and_controlled_by = AUS
            }
        }
        75 = {
            add_core_of = CZE
            transfer_state_to = CZE
        }
    }
    CZE = {
        set_cosmetic_tag = AUS_nww_bohemia
        set_politics = {
            ruling_party = democratic
            elections_allowed = yes
            election_frequency = 48
        }
        set_stability = 0.60
    }
    GER_nww_settle_bohemian_influence = yes
    add_stability = -0.10
}
```

## Регионы, используемые наградами, и заморский старт

История региона содержит начальные и датированные записи. Условная награда в регионе не означает, что Германия владеет им в начале игры.

### `history/states/42-Rhineland.txt`

```pdx
state = {
    id = 42
    name = STATE_42
    manpower = 3027739
    resources = {
        steel = 50
        aluminium = 14
        coal = 14
    }
    state_category = metropolis
    history = {
        owner = GER
        add_core_of = GER
        add_core_of = RHI
        add_core_of = PRE
        victory_points = {
            11435
            1
        }
        victory_points = {
            9575
            3
        }
        victory_points = {
            11531
            5
        }
        buildings = {
            infrastructure = 4
            industrial_complex = 3
        }
        1936.3.7 = {
            set_demilitarized_zone = no
        }
        1939.1.1 = {
            buildings = {
                radar_station = 1
                synthetic_refinery = 3
                11470 = {
                    bunker = 2
                }
                11435 = {
                    bunker = 2
                }
                9575 = {
                    bunker = 2
                }
                11531 = {
                    bunker = 2
                }
                563 = {
                    bunker = 2
                }
                3558 = {
                    bunker = 2
                }
            }
        }
    }
    provinces = {
        563
        3423
        3558
        9575
        11435
        11470
        11494
        11531
        11547
    }
    local_supplies = 0.0
}
```

### `history/states/541-South West Africa.txt`

```pdx
state = {
    id = 541
    name = STATE_541
    manpower = 254100
    state_category = pastoral
    history = {
        owner = GER
        buildings = {
            infrastructure = 2
        }
        victory_points = {
            4879
            1
        }
        add_core_of = NMB
    }
    provinces = {
        2207
        4879
        7770
    }
    buildings_max_level_factor = 1.000
    local_supplies = 0.000
}
```

### `history/states/546-Tanganyika.txt`

```pdx
state = {
    id = 546
    name = STATE_546
    state_category = rural
    resources = {
        rubber = 2
    }
    history = {
        owner = GER
        victory_points = {
            2196
            1
        }
        buildings = {
            infrastructure = 2
            2196 = {
                naval_base = 2
            }
        }
        add_core_of = TZN
    }
    provinces = {
        2176
        2196
        2206
        2281
        2308
        4171
        5180
        5224
        8144
        8182
        8183
        8201
        8205
        10845
        10932
        10988
        11017
        12911
        12944
        12967
    }
    manpower = 5299000
    buildings_max_level_factor = 1.000
    local_supplies = 0.0
}
```

### `history/states/67-Oberschlesien.txt`

```pdx
state = {
    id = 67
    name = STATE_67
    manpower = 1402591
    resources = {
        steel = 8
        aluminium = 6
        coal = 25
    }
    state_category = city
    history = {
        owner = GER
        add_core_of = GER
        add_core_of = SIL
        add_core_of = PRE
        victory_points = {
            11467
            5
        }
        victory_points = {
            9511
            3
        }
        buildings = {
            infrastructure = 3
        }
    }
    provinces = {
        479
        6512
        9457
        9511
        11467
    }
    local_supplies = 4.0
}
```

### `history/states/69-Sudatenland.txt`

```pdx
state = {
    id = 69
    name = STATE_69
    manpower = 2476250
    state_category = town
    resources = {
        steel = 4
    }
    history = {
        victory_points = {
            3585
            3
        }
        victory_points = {
            11432
            1
        }
        victory_points = {
            6470
            1
        }
        victory_points = {
            11401
            3
        }
        owner = AUS
        add_core_of = AUS
        add_core_of = CZE
        buildings = {
            infrastructure = 4
            industrial_complex = 2
            arms_factory = 1
            anti_air_building = 1
            424 = {
                bunker = 1
            }
            469 = {
                bunker = 1
            }
            3585 = {
                bunker = 1
            }
            6470 = {
                bunker = 1
            }
            9555 = {
                bunker = 1
            }
            11432 = {
                bunker = 1
            }
        }
        1938.9.30 = {
            owner = AUS
            add_core_of = AUS
            controller = AUS
            add_core_of = GER
        }
    }
    provinces = {
        424
        469
        3418
        3585
        6470
        9555
        11401
        11414
        11432
    }
    local_supplies = 0.0
}
```

### `history/states/72-Zaolzie.txt`

```pdx
state = {
    id = 72
    name = STATE_72
    manpower = 152000
    resources = {
        coal = 7
    }
    state_category = rural
    history = {
        owner = AUS
        add_core_of = AUS
        buildings = {
            infrastructure = 3
            industrial_complex = 1
        }
        add_core_of = CZE
        add_claim_by = SIL
        1939.3.14 = {
            owner = AUS
            add_core_of = AUS
            controller = AUS
        }
    }
    provinces = {
        9551
        9567
    }
    local_supplies = 1.0
}
```

### `history/states/74-East Sudatenland.txt`

```pdx
state = {
    id = 74
    name = STATE_74
    manpower = 820000
    resources = {
        coal = 12
    }
    state_category = rural
    history = {
        owner = AUS
        add_core_of = AUS
        add_core_of = CZE
        add_claim_by = SIL
        buildings = {
            infrastructure = 4
            arms_factory = 1
        }
        victory_points = {
            3583
            5
        }
        victory_points = {
            3414
            2
        }
        1938.9.30 = {
            owner = AUS
            add_core_of = AUS
            controller = AUS
            add_core_of = GER
        }
    }
    provinces = {
        421
        3414
        3583
        6485
    }
    local_supplies = 2.0
}
```

### `history/states/75-Moravia.txt`

```pdx
state = {
    id = 75
    name = STATE_75
    manpower = 2598400
    resources = {
        steel = 4
        oil = 2
    }
    state_category = city
    history = {
        owner = AUS
        add_core_of = AUS
        victory_points = {
            3569
            20
        }
        victory_points = {
            6562
            5
        }
        buildings = {
            infrastructure = 4
            industrial_complex = 4
            air_base = 5
        }
        add_core_of = CZE
        1939.3.14 = {
            owner = AUS
            add_core_of = AUS
            controller = CHI
        }
    }
    provinces = {
        569
        3553
        3569
        6562
        6576
        6590
        11511
    }
    local_supplies = 3.0
}
```

### `history/states/9-Czechoslovakia.txt`

```pdx
state = {
    id = 9
    name = STATE_9
    manpower = 4492600
    resources = {
        steel = 5
        coal = 6
    }
    state_category = large_city
    history = {
        owner = AUS
        add_core_of = AUS
        victory_points = {
            11542
            30
        }
        victory_points = {
            6418
            5
        }
        victory_points = {
            9569
            5
        }
        buildings = {
            infrastructure = 4
            arms_factory = 5
            industrial_complex = 1
            anti_air_building = 5
            air_base = 5
            11542 = {
                landmark_prague_castle = {
                    level = 1
                    allowed = {
                        has_dlc = "Peace For Our Time"
                    }
                }
            }
        }
        add_core_of = CZE
        1939.3.14 = {
            owner = AUS
            add_core_of = AUS
            controller = CHI
        }
    }
    provinces = {
        445
        494
        583
        3462
        6418
        6440
        6592
        9414
        9421
        9429
        9541
        9569
        11542
        11556
    }
    local_supplies = 0.0
}
```

### `docs/GER_overseas_setup.json`

```json
{
  "territories": [
    {
      "state": 541,
      "region": "German South-West Africa",
      "file": "history/states/541-South West Africa.txt",
      "previous_owner": "GER"
    },
    {
      "state": 893,
      "region": "German South-West Africa",
      "file": "history/states/893-Karas.txt",
      "previous_owner": "GER"
    },
    {
      "state": 894,
      "region": "German South-West Africa",
      "file": "history/states/894-Kuneme.txt",
      "previous_owner": "GER"
    },
    {
      "state": 895,
      "region": "German South-West Africa",
      "file": "history/states/895-Kavango.txt",
      "previous_owner": "GER"
    },
    {
      "state": 546,
      "region": "German East Africa",
      "file": "history/states/546-Tanganyika.txt",
      "previous_owner": "GER"
    },
    {
      "state": 768,
      "region": "German East Africa",
      "file": "history/states/768-Rwanda.txt",
      "previous_owner": "GER"
    },
    {
      "state": 769,
      "region": "German East Africa",
      "file": "history/states/769-Burundi.txt",
      "previous_owner": "GER"
    },
    {
      "state": 773,
      "region": "Cameroon",
      "file": "history/states/773-Cameroon.txt",
      "previous_owner": "GER"
    },
    {
      "state": 777,
      "region": "Togoland",
      "file": "history/states/777-Togo.txt",
      "previous_owner": "GER"
    },
    {
      "state": 979,
      "region": "German New Guinea and Bismarck Archipelago",
      "file": "history/states/979 - Kaiser Wilhelms Land.txt",
      "previous_owner": "GER"
    },
    {
      "state": 737,
      "region": "German New Guinea and Bismarck Archipelago",
      "file": "history/states/737-New Britain.txt",
      "previous_owner": "GER"
    },
    {
      "state": 1070,
      "region": "German New Guinea and Bismarck Archipelago",
      "file": "history/states/1070 - Bougainville.txt",
      "previous_owner": "GER"
    },
    {
      "state": 633,
      "region": "Pacific islands",
      "file": "history/states/633-Marshall Islands.txt",
      "previous_owner": "GER"
    },
    {
      "state": 646,
      "region": "Pacific islands",
      "file": "history/states/646-Saipan.txt",
      "previous_owner": "GER"
    },
    {
      "state": 647,
      "region": "Pacific islands",
      "file": "history/states/647-Palau.txt",
      "previous_owner": "GER"
    },
    {
      "state": 684,
      "region": "Pacific islands",
      "file": "history/states/684-Caroline Islands.txt",
      "previous_owner": "GER"
    },
    {
      "state": 725,
      "region": "Pacific islands",
      "file": "history/states/725-Nauru.txt",
      "previous_owner": "GER"
    },
    {
      "state": 726,
      "region": "German Samoa",
      "file": "history/states/726-Samoa.txt",
      "previous_owner": "GER"
    },
    {
      "state": 743,
      "region": "Kiautschou lease",
      "file": "history/states/743-Qingdao.txt",
      "previous_owner": "GER"
    }
  ],
  "total_states": 19,
  "no_ger_colonial_cores": true,
  "mefo_ideas": [
    "GER_mefo_bills_1",
    "GER_mefo_bills_2",
    "GER_mefo_bills_3",
    "GER_mefo_bills_4",
    "GER_mefo_bills_5",
    "GER_mefo_bills_6",
    "GER_mefo_bills_7",
    "GER_mefo_bills_8",
    "GER_mefo_bills_9",
    "GER_mefo_bills_10",
    "GER_mefo_bills_11",
    "GER_mefo_bills_12",
    "GER_mefo_bills_13",
    "GER_mefo_bills_14",
    "GER_mefo_bills_15",
    "GER_mefo_bills_16",
    "GER_mefo_bills_17",
    "GER_mefo_bills_18",
    "GER_mefo_bills_ended",
    "GER_mefo_bills_1936_fake_ns",
    "GER_mefo_bills_1939_fake_ns"
  ],
  "historical_sources": [
    "https://www.dhm.de/lemo/kapitel/kaiserreich/aussenpolitik/statistische-angaben-zu-den-deutschen-kolonien",
    "https://www.dhm.de/lemo/kapitel/kaiserreich/aussenpolitik/kolonialpolitik",
    "https://www.bundesarchiv.de/themen-entdecken/online-entdecken/geschichtsgalerien/die-entstehung-der-musterkolonie-kiautschou/"
  ]
}
```

### `docs/GER_industry_rework.json`

```json
{
  "focuses": [
    "GER_krupp_and_thyssen",
    "GER_1",
    "GER_nww_electrical_grid",
    "GER_nww_silesian_steel",
    "GER_3",
    "GER_nww_arsenal_contracts",
    "GER_4",
    "GER_5",
    "GER_6",
    "GER_7",
    "GER_nww_machine_tools",
    "GER_nww_industrial_standards",
    "GER_nww_technical_colleges",
    "GER_mitteleuropa_trade",
    "GER_2",
    "GER_nww_freight_corridors",
    "GER_nww_merchant_contracts",
    "GER_nww_export_credit",
    "GER_nww_investment_guarantees",
    "GER_8",
    "GER_9",
    "GER_10",
    "GER_nww_industrial_research",
    "GER_nww_balanced_orders",
    "GER_nww_synthetic_fuels",
    "GER_nww_colonial_ports",
    "GER_nww_energy_keystones",
    "GER_nww_worker_housing",
    "GER_nww_electromechanical_labs",
    "GER_nww_supply_resilience",
    "GER_nww_prague_network"
  ],
  "persistent_bonuses": {
    "GER_krupp_and_thyssen": {
      "construction": 0.05
    },
    "GER_nww_electrical_grid": {
      "energy": 0.1
    },
    "GER_nww_arsenal_contracts": {
      "output": 0.05
    },
    "GER_4": {
      "efficiency": 0.05
    },
    "GER_6": {
      "construction": 0.05
    },
    "GER_7": {
      "maximum": 0.05
    },
    "GER_nww_machine_tools": {
      "efficiency": 0.05
    },
    "GER_nww_industrial_standards": {
      "maximum": 0.05
    },
    "GER_nww_technical_colleges": {
      "research": 0.05
    },
    "GER_nww_investment_guarantees": {
      "construction": 0.05
    },
    "GER_9": {
      "output": 0.05
    },
    "GER_nww_industrial_research": {
      "research": 0.05
    }
  },
  "modifiers": {
    "construction": "production_speed_buildings_factor",
    "output": "industrial_capacity_factory",
    "efficiency": "production_factory_efficiency_gain_factor",
    "maximum": "production_factory_max_efficiency_factor",
    "research": "research_speed_factor",
    "energy": "energy_gain_factor"
  }
}
```

## Неигровая совместимость с ванильными ID

В `GER_native_compatibility.txt` определено 436 неимпортированных shared_focus. Это заглушки для внешних ссылок, не дополнительные ветки. В дереве GER_focus их нет.

```text
GER_a_new_and_better_germany
GER_a_strong_successor
GER_abolish_price_controls
GER_absorb_the_abwehr
GER_accelerate_the_rearmament_program
GER_accept_british_naval_dominance
GER_accept_british_naval_dominance_ww
GER_adopt_new_panzer_doctrine
GER_advanced_panzer_research
GER_aerodynamic_research_institute
GER_aeronautical_research_institute
GER_african_allies
GER_agricultural_reforms
GER_align_czechoslovakia
GER_align_italy
GER_align_south_america
GER_all_for_the_front
GER_all_terrain_military_motorcycle
GER_alliance_with_portugal
GER_alliance_with_spain
GER_alliance_with_the_ussr
GER_ally_chiang_kai_shek
GER_ally_the_shade
GER_ally_white_russian_forces
GER_amerikabomber
GER_an_invincible_army
GER_anglo_germanic_cooperation_program
GER_anglo_germanic_defense_pact
GER_anschluss
GER_anti_comintern_pact
GER_anti_comintern_pact_unaligned
GER_anti_soviet_pact
GER_anti_soviet_pact_unaligned
GER_armament_rationalization
GER_army_indoctrination
GER_around_maginot
GER_artillery_bombardment
GER_ascension_of_goebbels
GER_ascension_of_goring
GER_ascension_of_himmler
GER_ascension_of_speer
GER_ascension_of_todt
GER_asian_allies
GER_assassinate_mussolini
GER_assassinate_mussolini_ww
GER_assemble_red_orchestra
GER_assist_our_eastern_comrades
GER_atlantic_naval_bases
GER_atlantic_naval_dominance
GER_autarky_achieved
GER_autarky_efforts
GER_autonomous_organization_todt
GER_autonomy_in_the_kriegsschulen
GER_backdoor_negotiations
GER_baltic_membership
GER_ban_political_uniforms
GER_befriend_china
GER_befriend_czechoslovakia
GER_befriend_japan
GER_befriend_poland
GER_befriend_turkey
GER_blitzkrieg_across_the_pacific
GER_break_anglo_french_colonial_hegemony_ww
GER_break_the_anglo_french_colonial_hegemony
GER_bribe_senior_officers
GER_bring_turkey_into_the_fold
GER_brothers_in_arms
GER_build_defense_industry
GER_build_the_eastern_bulwark
GER_build_the_rur_dam
GER_bulwark_against_bolshevism
GER_bypass_maginot_in_the_south
GER_bypass_maginot_in_the_south_ww
GER_carte_blanche_for_alsace_and_french_colonies
GER_carte_blanche_for_alsace_and_french_colonies_ww
GER_carve_up_congo
GER_carve_up_czechoslovakia
GER_central_european_alliance
GER_central_planning
GER_challenge_the_monroe_doctrine
GER_civil_liberties
GER_claim_old_colonies_in_the_east
GER_closer_sino_germanic_relations
GER_coal_liquefaction
GER_combined_arms
GER_concentrated_armament_program
GER_conquer_italy
GER_construct_aircraft_carriers
GER_construct_the_kammhuber_line
GER_construct_the_reichsautobahn
GER_create_asian_reichskommissariat
GER_create_rustungsstab
GER_crossing_the_atlantic
GER_cruiser_warfare
GER_currency_reforms
GER_czechoslovakia
GER_danubian_expansion
GER_danubian_membership
GER_danzig_for_guarantees
GER_danzig_for_guarantees_ww
GER_danzig_for_slovakia
GER_danzig_or_war
GER_defend_the_vaterland
GER_defense_of_the_reich
GER_defense_treaty_with_the_soviet
GER_demand_further_polish_concessions
GER_demand_lithuanian_integration
GER_demand_slovenia
GER_demand_sudetenland
GER_demand_the_return_of_southern_jutland
GER_demands_to_sweden
GER_democratic_shield
GER_demonstration_of_military_achievements
GER_denazification_campaigns
GER_develop_heraeus_facilities
GER_develop_modern_maneuver_warfare
GER_develop_the_knickebein
GER_dive_bombers
GER_divide_and_conquer
GER_effective_operations
GER_effectivize_the_volkswerke
GER_embrace_democratic_institutions
GER_embrace_liberal_leanings
GER_employ_philipp_holzmann
GER_end_european_communism
GER_establish_a_customs_union
GER_establish_buna_werke
GER_establish_carrier_groups
GER_establish_eastern_grand_duchies
GER_establish_night_fighter_squadrons
GER_establish_production_targets
GER_establish_protectorates_in_america
GER_establish_the_afrikakorps
GER_establish_the_reichswerke
GER_establish_the_skijager
GER_establish_volkskommissariats
GER_establish_western_grand_duchies
GER_european_confederation
GER_expand_african_reach
GER_expand_claims_in_baltic
GER_expand_gestapo
GER_expand_kriegsmarinewerft
GER_expand_kummersdorfs_capacity
GER_expand_pacific_holdings
GER_expand_social_welfare
GER_expand_ss_recruitment
GER_expand_ss_security_duties
GER_expand_the_reichsautobahn_east
GER_expand_the_reichsautobahn_south
GER_expand_the_truppenschulen
GER_expanding_the_luftwaffe
GER_expatriate_the_communists
GER_expatriate_the_communists_ww
GER_experimental_rotorcrafts
GER_extend_mitteleuropas_bounderies
GER_factories_for_resources
GER_fallschirmjager
GER_fan_prussian_militarism
GER_fan_the_prussian_militarism
GER_fate_of_czechoslovakia
GER_fate_of_greece
GER_fate_of_yugoslavia
GER_finnish_membership
GER_first_ljubljana_award
GER_first_vienna_award
GER_focus_on_the_true_enemy
GER_form_agricultural_cooperatives
GER_form_organization_todt
GER_form_rome_berlin_axis
GER_form_the_jagdwaffe
GER_form_the_stasi
GER_formalize_the_intelligence_wing
GER_fortify_the_vaterland
GER_franco_germanic_pact
GER_fuhrerprinzip
GER_fund_the_film_department
GER_german_hegemony_in_the_middle_east
GER_glorify_party_rallies
GER_glorious_mechanical_machinations
GER_glory_to_the_imperial_army
GER_grosskampfschiff_construction
GER_heed_von_neuraths_concerns
GER_hegemony_of_the_ss
GER_hegemony_over_europe
GER_high_seas_fleet
GER_hold_joint_military_drills
GER_housing_developments
GER_hungary
GER_improve_motorized_troops
GER_improve_the_logistics_system
GER_incorporate_the_polish_rump_state
GER_increased_trade
GER_industrial_cooperation
GER_industrial_expansion
GER_industrial_investments
GER_industrialize_volkskommissariats
GER_influence_the_baltics
GER_influence_the_benelux
GER_influence_the_middle_east
GER_innovative_warfare
GER_instigate_middle_eastern_revolutions
GER_instill_auftragstaktik
GER_instill_german_discipline
GER_institute_price_controls
GER_integrate_czech_manufacturers
GER_integrate_czechoslovakia
GER_integrate_subjects_economies
GER_integrate_volkskommissariats
GER_integrate_western_german_speakers
GER_integrated_economies
GER_integration_of_puppet_economies
GER_intervene_in_spain
GER_invade_italy
GER_invest_in_vereinigte_stahlwerke
GER_invite_scientists_back
GER_japanese_naval_cooperation
GER_kdf_wagen_factories
GER_kriegslokomotiven
GER_labor_rights_and_union_stuff
GER_launch_sino_germanic_joint_research_program
GER_legacy_of_the_spartacus_league
GER_legion_condor
GER_lessons_of_the_great_war
GER_liberate_austria
GER_liberate_italy
GER_liberate_oppressed_people
GER_low_countries_membership
GER_lower_taxes
GER_loyalty_to_the_fuhrer
GER_marinestosstrupp
GER_mass_production
GER_memel_ultimatum
GER_military_dictatorship
GER_ministry_of_public_enlightenment
GER_mittelafrika
GER_mitteleuropa
GER_mitteleuropa_cooperation_sphere
GER_molotov_ribbentrop_pact
GER_monarchist_sentiment
GER_nationalize_ford_factories
GER_nationalize_industries
GER_negotiate_old_colonies_in_the_east
GER_no_balkan_communism
GER_no_reds_in_western_europe
GER_offer_military_production_support
GER_offer_trade_proposal
GER_operation_felix
GER_operation_green
GER_operation_isabella
GER_operation_sea_lion
GER_operation_tannenbaum
GER_operation_weserubung
GER_oppose_hitler
GER_oppose_hitler_ww
GER_optimize_reich_labour_service
GER_our_place_in_the_sun
GER_our_place_in_the_sun_ww
GER_panzer_troops_school
GER_panzergrenadier
GER_panzerschiff_raiders
GER_party_chancellor_bormann
GER_party_chancellor_hess
GER_petition_for_the_return_of_old_colonies
GER_plan_z
GER_plenipotentiary_of_armaments
GER_plenipotentiary_of_the_four_year_plan
GER_poland
GER_polish_membership
GER_political_commissars
GER_pool_technical_know_how
GER_pool_technical_know_how_ww
GER_prepare_for_the_next_blockade
GER_prepare_for_the_next_blockade_ww
GER_prepare_for_the_next_naval_blockade
GER_prepare_italian_coup
GER_prepare_italian_coup_ww
GER_pride_of_the_modern_germany
GER_prioritize_economic_growth
GER_prioritize_the_four_year_plan
GER_proletarian_dictatorship
GER_proletarian_solidarity
GER_propaganda_master
GER_protect_the_revolution
GER_prussian_artillery
GER_puppet_finland
GER_puppet_turkey
GER_rally_the_industrialists
GER_rally_the_nation
GER_rapid_army_expansion
GER_re_establish_free_elections_ww
GER_re_establish_german_control_over_qingdao
GER_re_establish_the_landwehr
GER_re_establish_the_seekriegsleitung
GER_re_form_the_freikorps
GER_re_ratify_the_locarno_treaty
GER_reach_out_to_scandinavia
GER_realize_mittelafrika
GER_realpolitik
GER_reassert_eastern_claims
GER_rebuild_the_high_seas_fleet
GER_rebuild_the_high_seas_fleet_ww
GER_rebuild_the_nation
GER_rebuild_the_nation_ww
GER_reclaim_former_african_colonies
GER_red_europe
GER_reestablish_free_elections
GER_reinstate_imperial_possessions
GER_reinstate_imperial_possessions_ww
GER_reintegrate_luxemburg_and_alsace_lorraine
GER_reject_the_locarno_treaty
GER_rekindle_imperial_sentiment
GER_rekindle_imperial_sentiment_ww
GER_remilitarize_the_rhineland
GER_reorganize_nationale_volksarmee
GER_reorganize_secret_services
GER_reorganize_the_luftwaffe
GER_reorganize_the_wehrmacht
GER_request_the_return_of_french_held_colonies
GER_request_the_return_of_qingdao
GER_resource_trade
GER_ressurect_the_red_front_fighters_league
GER_restore_eastern_imperial_possessions
GER_restore_the_brest_litovsk_borders
GER_restore_the_holy_roman_empire
GER_return_of_the_kaiser
GER_return_of_the_kaiser_ww
GER_reverse_the_brain_drain
GER_reverse_the_brain_drain_ww
GER_revitalize_the_nation
GER_revive_the_kaiserreich
GER_revive_the_kaiserreich_ww
GER_rocketry_innovations
GER_root_out_imperialism
GER_safeguard_poland
GER_safeguard_the_baltic
GER_safeguard_the_baltic_ww
GER_salvage_captured_equipment
GER_scandinavian_membership
GER_schlieffen_once_more
GER_schlieffen_once_more_ww
GER_second_ljubljana_award
GER_secure_finland
GER_secure_the_new_state
GER_see_to_the_eastern_front
GER_see_to_the_eastern_front_ww
GER_seeherrschaft
GER_seize_foreign_industries
GER_send_military_aid
GER_send_volunteers
GER_sentinels_of_the_pacific
GER_shared_rd_programs
GER_shared_rd_programs_ww
GER_shatter_usas_hegemony
GER_sign_the_second_treaty_of_berlin
GER_social_ownership
GER_solve_the_logistical_bottlenecks
GER_south_east_asian_natural_wealth
GER_spark_the_flame_of_revolution
GER_spheres_of_influence
GER_start_the_proletarian_revolution
GER_state_controlled_economy
GER_stormtroopers
GER_strafbataillon
GER_strengthen_the_kriegsmarine
GER_strengthen_the_proletarian_international
GER_strengthen_the_waffen_ss
GER_strengthen_the_welfare_state
GER_strike_at_the_rising_sun
GER_strike_at_the_source
GER_strike_eastward
GER_strive_for_conservative_values
GER_subduing_the_baltic_states
GER_subjugate_romanian_economy
GER_subsidize_hoesch_benzin
GER_subversive_infiltrators
GER_support_a_coup_in_liechtenstein
GER_support_finland
GER_support_the_finns
GER_support_the_finns_ww
GER_support_the_proletarian_uprising
GER_sway_the_balkans
GER_tackle_the_communist_threat
GER_tactical_bombers
GER_tech_sharing
GER_tend_to_the_future_of_germany
GER_the_central_powers
GER_the_end_to_fascist_europe
GER_the_final_blow_to_communism
GER_the_first_berlin_award
GER_the_four_year_plan
GER_the_german_stakhanovite_movement
GER_the_great_red_menace
GER_the_iberian_problem
GER_the_mannheim_project
GER_the_mannheim_project_ww
GER_the_monarchy_compromise
GER_the_monarchy_compromise_ww
GER_the_northern_shield
GER_the_peoples_victory
GER_the_proletarian_legion
GER_the_proud_eagle_and_the_resurgent_dragon
GER_the_prussian_legacy
GER_the_second_berlin_award
GER_the_sino_germanic_pact
GER_the_supreme_leader
GER_the_swiss_gold
GER_the_triumphant_will
GER_torpedobomber
GER_total_control_over_domestic_affairs
GER_totaler_krieg
GER_trade_agreements
GER_trade_deal_with_sweden
GER_trade_interdiction
GER_treaty_with_the_ussr
GER_tributes_for_guarantees
GER_u_boat_efforts
GER_unify_west_africa
GER_unrestricted_convoy_raiding
GER_uplift_the_rosenberg_office
GER_uralbomber_program
GER_uranverein
GER_urbanization
GER_utilize_the_nordliche_gesellschaft
GER_wage_war_on_capitalism
GER_war_preparations
GER_war_production
GER_war_with_france
GER_war_with_greece
GER_war_with_the_ussr
GER_weltpolitik
GER_wirtschaftswunder
GER_wolfpack_tactics
GER_womens_rights_and_equality
GER_workers_rights
GER_wunderwaffe
GER_zentrale_planung
```

## Локализация духов, диапазонов BoP, решений, событий и ответов

```json
{
  "AUS_nww_bohemia": {
    "ru": "Богемия",
    "en": "Bohemia"
  },
  "AUS_nww_bohemian_drift": {
    "ru": "Богемия желает отделиться: [?AUS_bohemian_tension|0]/10",
    "en": "Bohemian Separatism: [?AUS_bohemian_tension|0]/10"
  },
  "AUS_nww_bohemian_drift_desc": {
    "ru": "Каждые 60 дней напряжённость растёт на 1. При 10 Богемия отделяется. Переговоры снижают её на 2 после 20 дней; инвестиции создают фабрику и снижают напряжённость на 2 после 35 дней.",
    "en": "Every sixty days tension rises by one. At ten Bohemia secedes. Negotiations reduce it by two after twenty days; investment builds a factory and reduces it by two after thirty-five days."
  },
  "AUS_nww_bohemian_question": {
    "ru": "Богемия желает отделиться",
    "en": "Bohemia Demands Independence"
  },
  "AUS_nww_bohemian_question_desc": {
    "ru": "С ростом напряжённости падают стабильность и выпуск заводов. На уровне 10 Богемия выходит из состава государства.",
    "en": "Rising tension reduces stability and factory output. At level 10 Bohemia secedes."
  },
  "GER_10_desc": {
    "ru": "Внедрим автоматическую оснастку в оружейное производство. Бонус исследований не выдаёт технологии другой эпохи напрямую.",
    "en": "Automatic tooling supports infantry weapon research without directly granting technologies from a later era."
  },
  "GER_1_desc": {
    "ru": "Новые шахтные стволы и обогатительные установки увеличат добычу рурского угля. Рост промышленности должен опираться на реальную энергетическую базу.",
    "en": "Modern shafts and processing plants expand Ruhr coal extraction. The resource investment requires ownership and control of the Ruhr."
  },
  "GER_2_desc": {
    "ru": "Вложения в заморские предприятия увеличат добычу только в принадлежащих нам и контролируемых регионах. Коренное население сохраняет национальные территории; германские колониальные коры не добавляются.",
    "en": "Develop overseas rubber and chromium enterprises only in regions we actually own and control. Indigenous claims remain intact."
  },
  "GER_3_desc": {
    "ru": "Государственные заказы поддержат оборонные предприятия германских земель. Заводы строятся на собственных контролируемых национальных территориях.",
    "en": "State orders support new military production on owned and controlled German core territory."
  },
  "GER_4_desc": {
    "ru": "Единые допуски и взаимозаменяемые детали ускорят освоение серийного оружия. Военные технологии опираются на развитие станочного производства.",
    "en": "Common tolerances and interchangeable parts improve production efficiency growth and support infantry weapon research."
  },
  "GER_5_desc": {
    "ru": "Привлечём долгосрочные вложения к рейнским и общегерманским предприятиям. Производственные мощности растут без МЕФО и завоевательной долговой экономики.",
    "en": "Long-term investment supports a new civilian enterprise on owned and controlled German core territory."
  },
  "GER_6_desc": {
    "ru": "Добровольные облигации земель направят сбережения в оборудование, коммуникации и новые корпуса. Неограниченных денежных или фабричных наград эта программа не даёт.",
    "en": "Voluntary state industrial bonds direct savings into equipment and construction, permanently improving the industrial program."
  },
  "GER_7_desc": {
    "ru": "Обучение мастеров и контроль качества дадут устойчивый рост производственной эффективности. Программа развивает общий промышленный дух.",
    "en": "Train master craftsmen and strengthen quality control to raise the production efficiency cap."
  },
  "GER_8_desc": {
    "ru": "Военная стандартизация и гражданские технические школы должны сойтись в общей исследовательской программе. Дополнительная ячейка предоставляется только до пяти исследовательских ячеек.",
    "en": "Bring military standardization and technical education together. An additional research slot is granted only below five slots."
  },
  "GER_9_desc": {
    "ru": "Новые военные предприятия опираются на уже подготовленную производственную и инженерную базу. Это завершение подготовки, а не ранний скачок к массовой агрессии.",
    "en": "New military factories and improved output build on the completed industrial and engineering program."
  },
  "GER_abolish_the_hohenzollerns_desc": {
    "ru": "Устраним Вильгельма III и последние династические ограничения. Альфред Гугенберг возглавит радикальное националистическое правительство; баланс между короной и рейхстагом будет окончательно упразднён. Реорганизация штабов снимет штраф к организации от имперского перенапряжения.",
    "en": "Remove Wilhelm III and the last dynastic restraints. Alfred Hugenberg heads a radical nationalist government, and the crown-Reichstag balance of power is abolished permanently. Reorganise the staff to remove the organisation penalty from Imperial Overstretch."
  },
  "GER_anschluss_by_force_desc": {
    "ru": "Потребуем от Австрии согласиться на присоединение к новому германскому государству. Отказ даёт цель войны для аннексии. Требование направляется только независимой Австрии, находящейся в мире.",
    "en": "Demand Austria consent to annexation into the new German state. A refusal grants an annexation war goal. The demand is delivered only to an independent Austria at peace."
  },
  "GER_anti_imperialist_crusade_desc": {
    "ru": "Подготовим цели войны на освобождение против Франции и Британии, если они независимы, недемократичны и не входят в наш союз. Освобождение предстоит обеспечить войной и мирным урегулированием.",
    "en": "Prepare liberation war goals against France and Britain if they are independent, non-democratic states outside our alliance. Liberation must be achieved through war and the peace settlement."
  },
  "GER_arsenal_of_democracy_desc": {
    "ru": "Укрепим конституционные институты оборонной промышленной программой: +20% выпуска фабрик и +10% защиты дивизий с сохранением бонусов стабильности и политической власти. Гарантируем независимость суверенных Литвы-Беларуси и Польши от внешней агрессии. Завершить военную и административную реформу, удалив обе версии имперского перенапряжения.",
    "en": "Strengthen our constitutional institutions with a defensive industrial programme: +20% factory output and +10% division defence, retaining their stability and political-power bonuses. Guarantee independent Lithuania-Belarus and Poland against foreign aggression. Complete military and administrative reform, removing both versions of Imperial Overstretch."
  },
  "GER_arsenal_of_democracy_shield": {
    "ru": "Демократический щит",
    "en": "Democratic Shield"
  },
  "GER_arsenal_of_democracy_shield_desc": {
    "ru": "Сохраним институциональные и промышленные преимущества арсенала демократии, укрепим оборону родины и организуем расширенный добровольческий контингент для поддержки независимых государств под угрозой.",
    "en": "Retain the Arsenal of Democracy’s institutional and industrial benefits, strengthen homeland defence and organise a larger volunteer contingent to support threatened independent states."
  },
  "GER_berlin_moscow_axis_desc": {
    "ru": "Предложим советскому правительству принять нашу республику в его союз или создать общий коммунистический альянс, если такого ещё нет. Необходимо согласие СССР; отказ не приводит к войне.",
    "en": "Ask the Soviet government to admit our republic into its alliance, or create a common Communist alliance if it has none. Soviet consent is required; a refusal does not start a war."
  },
  "GER_berlin_moscow_faction": {
    "ru": "Рабочий союз Берлина и Москвы",
    "en": "Berlin-Moscow Workers Alliance"
  },
  "GER_bop_balanced": {
    "ru": "Равновесие учреждений",
    "en": "Institutional Balance"
  },
  "GER_bop_decisions_category": {
    "ru": "Корона, командование и парламент",
    "en": "Crown, Command and Parliament"
  },
  "GER_bop_decisions_category_desc": {
    "ru": "Империя балансирует между властью короны и Генерального штаба и требованиями рейхстага. Военное командование находится слева, парламент — справа.",
    "en": "The empire balances the authority of the crown and General Staff against the demands of the Reichstag. Military command lies to the left; parliament lies to the right."
  },
  "GER_bop_frozen_tt": {
    "ru": "Баланс сил навсегда закрепляется за Верховным командованием и короной. Оба решения по изменению влияния становятся недоступны.",
    "en": "The balance of power is permanently fixed at complete OHL and Crown control. Both influence decisions are disabled."
  },
  "GER_bop_ohl_influence": {
    "ru": "Растущее влияние военных",
    "en": "Growing Military Influence"
  },
  "GER_bop_ohl_leaning": {
    "ru": "Преобладание Верховного командования",
    "en": "OHL Ascendant"
  },
  "GER_bop_reichstag_influence": {
    "ru": "Растущее влияние парламента",
    "en": "Growing Parliamentary Influence"
  },
  "GER_bop_reichstag_leaning": {
    "ru": "Преобладание рейхстага",
    "en": "Reichstag Ascendant"
  },
  "GER_bop_total_ohl": {
    "ru": "Полная власть Верховного командования",
    "en": "Total OHL Control"
  },
  "GER_bop_total_reichstag": {
    "ru": "Верховенство парламента",
    "en": "Parliamentary Supremacy"
  },
  "GER_capital_ship_research": {
    "ru": "Программа крупных кораблей",
    "en": "Capital Ship Programme"
  },
  "GER_challenge_moscow_desc": {
    "ru": "С 1941 года, в мирное время, оспорим притязания Москвы на руководство революцией. Выйдем из советского союза либо исключим Советскую Россию, если возглавляем альянс, затем подготовим цель войны на завоевание независимого советского государства.",
    "en": "From 1941, at peace, dispute Moscow’s claim to lead the revolution. Leave the Soviet alliance, or expel the Soviet Union if we lead it, then prepare a conquest war goal against an independent Soviet state."
  },
  "GER_communism_party": {
    "ru": "Спартакизм",
    "en": "Spartacism"
  },
  "GER_communism_party_long": {
    "ru": "Спартакизм",
    "en": "Spartacism"
  },
  "GER_concede_to_parliament": {
    "ru": "Уступить парламенту",
    "en": "Concede to Parliament"
  },
  "GER_concede_to_parliament_desc": {
    "ru": "Признаем рейхстаг партнёром в управлении. Сдвигает баланс на 10% вправо и повышает поддержку демократов на 5 процентных пунктов. Доступно повторно через 30 дней до роспуска рейхстага.",
    "en": "Recognise the Reichstag as a partner in government. Moves the balance 10% right and increases democratic support by 5 percentage points. Repeatable every 30 days until the Reichstag is dissolved."
  },
  "GER_constitutional_monarchy": {
    "ru": "Конституционные институты",
    "en": "Constitutional Institutions"
  },
  "GER_constitutional_monarchy_desc": {
    "ru": "Подотчётный парламенту кабинет управляет от имени символической короны. Эти институты развиваются в Арсенал демократии.",
    "en": "An accountable cabinet governs in the name of a ceremonial crown. These institutions grow into the Arsenal of Democracy."
  },
  "GER_constitutional_truce": {
    "ru": "Конституционное перемирие",
    "en": "Constitutional Truce"
  },
  "GER_constitutional_truce_desc": {
    "ru": "Временное соглашение высвобождает ресурсы, прежде уходившие на политические уступки.",
    "en": "A temporary settlement releases resources previously absorbed by political concessions."
  },
  "GER_consult_the_general_staff": {
    "ru": "Советоваться с Генеральным штабом",
    "en": "Consult the General Staff"
  },
  "GER_consult_the_general_staff_desc": {
    "ru": "Пригласим генералов определять имперскую политику. Сдвигает баланс на 10% влево и повышает поддержку монархистов на 5 процентных пунктов. Доступно повторно через 30 дней до роспуска рейхстага.",
    "en": "Invite the generals to shape imperial policy. Moves the balance 10% left and increases monarchist support by 5 percentage points. Repeatable every 30 days until the Reichstag is dissolved."
  },
  "GER_crush_eastern_syndicates_desc": {
    "ru": "Подготовим уничтожение независимых синдикалистских центров на территории махновцев и Украины. Цели войны выдаются только против существующих независимых стран вне нашего союза.\\n\\n$GER_eastern_1939_gate_tt$",
    "en": "Prepare the destruction of the independent syndicalist centres in the Makhnovist territory and Ukraine. War goals are granted only against existing independent countries outside our alliance.\\n\\n$GER_eastern_1939_gate_tt$"
  },
  "GER_democratic_party": {
    "ru": "Социал-демократия",
    "en": "Social Democracy"
  },
  "GER_democratic_party_long": {
    "ru": "Социал-демократия",
    "en": "Social Democracy"
  },
  "GER_dismantle_imperial_borders_desc": {
    "ru": "Прекратим германское господство над Литвой-Беларусью и Польшей. Освобождаются только наши собственные зависимые страны; независимые государства и владения третьих держав не аннексируются и не передаются.",
    "en": "End German overlordship over Lithuania-Belarus and Poland. Only our own existing subjects are freed; independent countries and the possessions of third powers are not annexed or transferred."
  },
  "GER_dissolve_the_reichstag_desc": {
    "ru": "Парламент больше не будет препятствовать императорским указам. Корона и Верховное командование получают всю полноту власти; баланс сил закрепляется, а демократические политические советники лишаются должностей и доступа к ним.",
    "en": "Parliament will no longer obstruct imperial commands. The crown and OHL take complete control, the balance of power is locked, and democratic political advisors lose their posts and eligibility."
  },
  "GER_drang_nach_osten_expanded_desc": {
    "ru": "С 1941 года радикальное правительство готовит цели войны на завоевание Советской России и Махновщины, если они сохраняют независимость и не являются нашими союзниками.",
    "en": "From 1941 the radical government prepares conquest war goals against Soviet Russia and the Makhnovist state, provided they still exist as independent, non-allied states."
  },
  "GER_eastern_1939_gate_tt": {
    "ru": "§YМы не готовы к масштабной войне на Востоке. Этот фокус будет доступен только с 1 января 1939 года.§!",
    "en": "§YWe are not ready for a major war in the East. This focus will be available only from 1 January 1939.§!"
  },
  "GER_eastern_war_guard_tt": {
    "ru": "Германия не может объявлять войну Литве-Беларуси, Польше, Украине, махновцам или СССР до 1 января 1939 года.",
    "en": "Germany cannot declare war on Lithuania-Belarus, Poland, Ukraine, the Makhnovists or the Soviet Union before 1 January 1939."
  },
  "GER_economic_community_tt": {
    "ru": "Освобождаем зависимые от нас Литву-Беларусь и Польшу и приглашаем их в Миттельевропу. Согласие каждого партнёра один раз даёт одну внемаповую гражданскую фабрику.",
    "en": "Free our existing Lithuanian-Belarusian and Polish subjects and invite them into Mitteleuropa. Each consenting partner grants one off-map civilian factory, once only."
  },
  "GER_empower_the_chancellor_desc": {
    "ru": "Канцлер должен согласовывать бюджет с рейхстагом, а не подчиняться двору и Генеральному штабу. Гражданские учреждения получат более весомый голос.",
    "en": "The chancellor must negotiate budgets through the Reichstag rather than defer to the court and General Staff. Civilian institutions gain a stronger voice."
  },
  "GER_end_of_an_era_desc": {
    "ru": "Вильгельм II олицетворял империю, не знавшую мировой войны. Его смерть положит конец долгому политическому застою и откроет борьбу за наследство. Фокус завершается только событием престолонаследия между августом и концом 1936 года.",
    "en": "Wilhelm II personified an empire that never faced a world war. His death will end its long political suspension and open the struggle over the succession. This focus is completed only by the succession event, between August and the end of 1936."
  },
  "GER_european_federation_desc": {
    "ru": "Преобразуем наш добровольный союз в Европейскую федерацию. Все участники получат +10% к скорости строительства гражданских фабрик и +5% к производительности военных заводов, пока демократическая Германия возглавляет федерацию. Программа распространяется на новых участников и прекращается при выходе.",
    "en": "Transform our voluntary alliance into the European Federation. Every member receives +10% civilian factory construction speed and +5% factory output while democratic Germany leads the federation. Future entrants share the programme; leaving ends its benefits."
  },
  "GER_european_federation_faction": {
    "ru": "Европейская федерация",
    "en": "European Federation"
  },
  "GER_fascism_party": {
    "ru": "Пангерманизм",
    "en": "Pan-Germanism"
  },
  "GER_fascism_party_long": {
    "ru": "Пангерманизм",
    "en": "Pan-Germanism"
  },
  "GER_federal_investment": {
    "ru": "Федеральная инвестиционная программа",
    "en": "Federal Investment Programme"
  },
  "GER_federal_investment_desc": {
    "ru": "Общие промышленные стандарты и добровольные инвестиционные соглашения ускоряют гражданское строительство и выпуск военных заводов. Преимущества прекращаются при выходе страны или утрате демократического германского руководства федерацией.",
    "en": "Common industrial standards and voluntary investment agreements improve civilian construction and military factory output. Membership benefits end when the federation loses its democratic German leadership or this country leaves it."
  },
  "GER_focus": {
    "ru": "Германская империя",
    "en": "German Empire"
  },
  "GER_focus_desc": {
    "ru": "Дерево фокусов кайзеровской Германии.",
    "en": "The national focus tree of the Kaiserreich."
  },
  "GER_fund_the_reichswehr_desc": {
    "ru": "Предоставим имперской армии требуемые средства и доступ к власти. Генеральный штаб усилит влияние за счёт парламентского контроля. Начать реформу штабов и заменить имперское перенапряжение облегчённой версией без штрафа к организации.",
    "en": "Give the imperial army the funds and access it demands. The General Staff gains influence at the expense of parliamentary oversight. Begin staff reform and replace Imperial Overstretch with its reduced version, removing the organisation penalty."
  },
  "GER_german_soviet_republic_desc": {
    "ru": "После победы спартакистов над имперскими лоялистами в гражданской войне учредим германскую республику советов во главе с Эрнстом Тельманом. Необходима победа восстания, а не просто прекращение боёв. Воссоздать штабы и заменить имперское перенапряжение облегчённой версией.",
    "en": "After the Spartacists defeat the imperial loyalists in the civil war, establish a German council republic under Ernst Thalmann. The uprising must have won; simply waiting for the fighting to end is insufficient. Reconstitute the staff and replace Imperial Overstretch with its reduced version."
  },
  "GER_gott_mit_uns_desc": {
    "ru": "Железная империя объединяет корону, армию и нацию общей имперской целью. Дивизии получают +15% к защите на национальной территории, +10% к атаке и +10% к прорыву. Завершить военную и административную реформу, удалив обе версии имперского перенапряжения.",
    "en": "The Iron Kaiserreich binds crown, army and nation to a single imperial purpose. Its divisions gain 15% core defence, 10% attack and 10% breakthrough. Complete military and administrative reform, removing both versions of Imperial Overstretch."
  },
  "GER_gott_mit_uns_naval": {
    "ru": "С нами Бог: океанская империя",
    "en": "Gott mit uns: Oceanic Empire"
  },
  "GER_gott_mit_uns_naval_desc": {
    "ru": "Имперское военное устройство сохраняет армейские преимущества, а долгосрочные контракты ускоряют строительство верфей и выпуск кораблей океанского флота.",
    "en": "The imperial military settlement retains its army bonuses while long-term contracts expand dockyard construction and naval output for an ocean-going fleet."
  },
  "GER_guardians_of_the_reich_desc": {
    "ru": "Укрепим государственные и производственные учреждения империи.",
    "en": "Strengthen the imperial institutions and production system."
  },
  "GER_hegemony_over_europe_focus_desc": {
    "ru": "Новый рейх получит цели войны на завоевание независимых Дании, Норвегии, Швеции, Финляндии и Швейцарии. Союзники и страны, с которыми мы уже воюем, исключаются.",
    "en": "The New Reich issues conquest war goals against independent Denmark, Norway, Sweden, Finland and Switzerland, excluding our allies and existing wars."
  },
  "GER_imperial_autocracy": {
    "ru": "Имперская автократия",
    "en": "Imperial Autocracy"
  },
  "GER_imperial_autocracy_desc": {
    "ru": "Имперская власть принадлежит короне и её военным учреждениям.",
    "en": "Imperial authority rests in the crown and its military institutions."
  },
  "GER_imperial_field_exercises": {
    "ru": "Провести имперские манёвры",
    "en": "Hold Imperial Field Exercises"
  },
  "GER_imperial_field_exercises_desc": {
    "ru": "Генеральный штаб демонстрирует готовность ценой общественного спокойствия. Усиливает Корону и временно улучшает планирование и восстановление организации.",
    "en": "The General Staff demonstrates its readiness at the cost of public confidence. Strengthen the Crown and temporarily improve planning and recovery."
  },
  "GER_imperial_overstretch": {
    "ru": "Имперское перенапряжение",
    "en": "Imperial Overstretch"
  },
  "GER_imperial_overstretch_2": {
    "ru": "Имперское перенапряжение: реформа штабов",
    "en": "Imperial Overstretch: Reformed Staff"
  },
  "GER_imperial_overstretch_2_desc": {
    "ru": "Реформа штабов снимает штраф к организации, но бюрократия и устаревшие институты продолжают обременять потребительское производство, поддержку войны, планирование и подготовку. Лишь завершение военной программы избранного политического пути позволит устранить эти обязательства.",
    "en": "Staff reform removes the organisation penalty, but bureaucracy and obsolete institutions still burden consumer production, war support, planning and training. Only the political programme’s final military settlement can end these obligations."
  },
  "GER_imperial_overstretch_desc": {
    "ru": "Колониальные гарнизоны, континентальные гарантии и негибкий двор истощают империю, уже не способную нести все обязательства. Неиспытанный в современной войне аристократический штаб держится за доктрины XIX века: организация падает, обучение новобранцев затягивается, оперативные планы буксуют.",
    "en": "Colonial garrisons, continental guarantees and an inflexible court drain an empire that can no longer afford every obligation. An untested, aristocratic staff clings to nineteenth-century doctrine: organisation falls, recruits train slowly and operational plans stagnate."
  },
  "GER_kaiser_vs_reichstag": {
    "ru": "Кайзер и рейхстаг",
    "en": "Kaiser and Reichstag"
  },
  "GER_krupp_and_thyssen_desc": {
    "ru": "Крупп, Тиссен, электротехнические концерны и земли согласуют программу инвестиций. Это начало развития единого промышленного комплекса, а не схема долгов ради завоеваний.",
    "en": "Krupp, Thyssen, electrical firms and the states coordinate investment. Industrial research and construction improve through a lasting program financed without conquest debt."
  },
  "GER_lebensraum_in_the_east_desc": {
    "ru": "Пангерманское руководство объявляет восточные приграничные земли сферой своей экспансии. Подготовим цели войны для аннексии независимых несоюзных Литвы-Беларуси и Польши только после открытия восточного направления.\\n\\n$GER_eastern_1939_gate_tt$",
    "en": "The Pan-German leadership claims the eastern borderlands as its sphere of expansion. Prepare annexation war goals against independent, non-allied Lithuania-Belarus and Poland, only after the eastern gate opens.\\n\\n$GER_eastern_1939_gate_tt$"
  },
  "GER_master_of_mitteleuropa": {
    "ru": "Хозяин Миттельевропы",
    "en": "Master of Mitteleuropa"
  },
  "GER_master_of_mitteleuropa_desc": {
    "ru": "Берлин определяет торговые правила Центральной Европы и распространяет имперское политическое влияние среди зависимых стран.",
    "en": "Berlin shapes the commercial rules of Central Europe and promotes imperial political influence among its dependants."
  },
  "GER_mediate_crown_and_chamber": {
    "ru": "Примирить Корону и палату",
    "en": "Mediate between Crown and Chamber"
  },
  "GER_mediate_crown_and_chamber_desc": {
    "ru": "Дорогостоящее конституционное перемирие приближает баланс к центру. Обязательства по потребительским товарам снижаются вместе с военным энтузиазмом.",
    "en": "Move the balance toward the center through a costly constitutional truce. Consumer obligations ease, while enthusiasm for war falls."
  },
  "GER_military_accounts": {
    "ru": "Открытые военные счета",
    "en": "Published Military Accounts"
  },
  "GER_military_accounts_desc": {
    "ru": "Прозрачность счетов облегчает политическую работу, но недовольство военных ослабляет наступательные действия.",
    "en": "Transparent accounts ease political work, but military opposition weakens offensive action."
  },
  "GER_mitteleuropa_demand_tt": {
    "ru": "Литва-Беларусь и Польша: автономия уже зависимых от Германии стран снижается; независимые правительства получают требование стать марионеткой и могут отказаться. Для интегрированной марионетки требуется Together for Victory; иначе используется обычный статус марионетки.",
    "en": "Lithuania-Belarus and Poland: existing German subjects have their autonomy reduced; independent governments receive a demand for puppet status and may refuse. Integrated puppet status requires Together for Victory; otherwise puppet status is used."
  },
  "GER_mitteleuropa_economic_community_desc": {
    "ru": "Предоставим независимость Литве-Беларуси и Польше, если они зависят от нас, и пригласим их в добровольный союз Миттельевропы. Согласие каждого партнёра даёт одну внемаповую гражданскую фабрику, всего не более двух. Отказ не даёт цели войны.",
    "en": "Free Lithuania-Belarus and Poland if they are our subjects, and invite them to the voluntary Mitteleuropa alliance. Each partner that accepts contributes one off-map civilian factory to economic integration, up to two in total. Refusal brings no war goal."
  },
  "GER_mitteleuropa_faction": {
    "ru": "Миттельевропа",
    "en": "Mitteleuropa"
  },
  "GER_mitteleuropa_refusal_tt": {
    "ru": "Отказ может дать Германии цель войны для подчинения страны. Для Литвы-Беларуси это возможно только с 1 января 1939 года, пока она независима и не входит в союз с Германией.",
    "en": "Refusal may grant Germany a puppet war goal. For Lithuania-Belarus this can happen only from 1 January 1939, while it remains independent and outside the German alliance."
  },
  "GER_mitteleuropa_trade_desc": {
    "ru": "Договоры поставок и торговые палаты расширят гражданское производство. Экономическое сотрудничество само по себе не подчиняет соседей.",
    "en": "Supply contracts and chambers of commerce expand civilian production. Economic cooperation does not itself subjugate neighboring states."
  },
  "GER_neutrality_party": {
    "ru": "Имперская автократия",
    "en": "Imperial Autocracy"
  },
  "GER_neutrality_party_long": {
    "ru": "Имперская автократия",
    "en": "Imperial Autocracy"
  },
  "GER_nva_mass_army": {
    "ru": "Национальная народная армия",
    "en": "National People’s Army"
  },
  "GER_nva_mass_army_desc": {
    "ru": "Постоянная преемница рабочих ополчений добавляет ещё 5 процентных пунктов военнообязанного населения, сохраняет восстановление организации и ускоряет обучение пехоты, но сокращает приоритет авиационных и морских исследований.",
    "en": "A permanent successor to the workers’ militias adds another 5 percentage points of recruitable population, retains their recovery benefits and trains infantry faster, while air and naval research loses priority."
  },
  "GER_nva_mass_mobilization_desc": {
    "ru": "Преобразуем рабочие ополчения в постоянную массовую армию. Увеличим долю военнообязанного населения ещё на 5 процентных пунктов, доведя общий бонус до 10. Сохраним +10% к восстановлению организации и сократим время подготовки армии на 10%. Приоритет пехоты оборачивается штрафом 20% к скорости исследований авиационной и морской техники.",
    "en": "Turn the workers’ militias into a permanent mass army. Raise recruitable population by another 5 percentage points, to 10 in total. Retain +10% organisation recovery and reduce army training time by 10%. Prioritising infantry imposes a 20% research-speed penalty on aircraft and naval equipment."
  },
  "GER_nww_arsenal_contracts_desc": {
    "ru": "Вместо чрезвычайных займов арсеналы получат предсказуемые многолетние заказы. Это повышает выпуск уже существующих военных заводов.",
    "en": "Give arsenals predictable long-term contracts, improving the output of existing military factories."
  },
  "GER_nww_austrian_1939_tt": {
    "ru": "Ультиматум Австрии доступен §Yне ранее 1 января 1939 года§!.",
    "en": "The Austrian ultimatum is available §Yno earlier than 1 January 1939§!."
  },
  "GER_nww_balanced_orders_desc": {
    "ru": "Гражданские и военные предприятия получают сбалансированную программу заказов. Имперская промышленность должна выдержать длительное напряжение без долговых миссий.",
    "en": "Balance civilian and military orders by building one enterprise of each kind on owned and controlled German core territory."
  },
  "GER_nww_bohemian_autonomists": {
    "ru": "Поддержать богемских автономистов",
    "en": "Support Bohemian Autonomists"
  },
  "GER_nww_bohemian_autonomists_desc": {
    "ru": "Финансирование местных организаций, подпольная печать и посредники усилят требования суверенитета.\\n\\nНапряжённость: §Y[?AUS.AUS_bohemian_tension|0]/10§!. Немецкий вклад: §Y[?AUS.AUS_bohemian_german_share|1]%§!.\\n\\nКаждое завершение добавляет §R+2§! напряжённости (до предела 10). При отделении Богемия становится нашим вассалом, если текущий немецкий вклад §Yстрого больше 60%§!. Австрийские уступки пропорционально уменьшают наш вклад. После урегулирования или отделения операция недоступна.",
    "en": "Funding local organizations, clandestine presses and intermediaries strengthens demands for sovereignty.\\n\\nTension: §Y[?AUS.AUS_bohemian_tension|0]/10§!. German contribution: §Y[?AUS.AUS_bohemian_german_share|1]%§!.\\n\\nEach completion adds §R+2§! tension, capped at 10. Upon secession, Bohemia becomes our puppet if the current German share is §Ystrictly greater than 60%§!. Austrian concessions proportionally reduce our contribution. The operation ends with settlement or secession."
  },
  "GER_nww_bohemian_operation_reward_tt": {
    "ru": "§R+2§! к богемской напряжённости, но не выше 10. Фактически добавленное давление учитывается как вклад Германии. Если это вызывает отделение при немецкой доле §Yболее 60%§!, новая Богемия становится германским вассалом. Ровно 60% недостаточно.",
    "en": "§R+2§! Bohemian tension, capped at 10. Only the pressure actually added counts as Germany's contribution. If this causes secession with a German share §Yabove 60%§!, the new Bohemia becomes Germany's puppet. Exactly 60% is insufficient."
  },
  "GER_nww_bohemian_operation_unlock_tt": {
    "ru": "Открывает операцию §Y«Поддержать богемских автономистов»§! в разведывательном агентстве против §YАвстрии§! (требуется La Résistance). Операция длится §Y45 дней§!, требует одного агента, сеть §Y35§!, две гражданские фабрики, 100 единиц пехотного и 25 единиц дополнительного оснащения.",
    "en": "Unlocks §YSupport Bohemian Autonomists§! in the intelligence agency against §YAustria§! (La Résistance required). The operation takes §Y45 days§!, one operative, a §Y35§! network, two civilian factories, 100 infantry equipment and 25 support equipment."
  },
  "GER_nww_colonial_ports_desc": {
    "ru": "Складские и перерабатывающие мощности поддержат заморские перевозки. Программа не передаёт чужие территории и не создаёт германские колониальные коры.",
    "en": "Expand civilian storage and processing capacity for overseas shipping without transferring territory or creating colonial cores."
  },
  "GER_nww_electrical_grid_desc": {
    "ru": "Объединим региональные электростанции и промышленные сети. Уголь и генерация останутся основой энергетики, а единая сеть уменьшит потери.",
    "en": "Link regional generating stations and industrial grids to improve energy supply. Coal extraction and efficient distribution must support new factories."
  },
  "GER_nww_electromechanical_labs_desc": {
    "ru": "Электромеханика и связь дадут основу для следующего поколения промышленного оборудования. Гражданское применение технологий предшествует массовому перевооружению.",
    "en": "Electromechanical laboratories support electronics research and the development of industrial communications."
  },
  "GER_nww_energy_keystones_desc": {
    "ru": "Построим энергетическую инфраструктуру в собственном контролируемом регионе, где её ещё нет. Используется инфраструктурный объект установленной версии игры.",
    "en": "Build an energy-infrastructure installation, prioritizing the Ruhr when eligible. The project requires an owned and controlled core region with room for the building."
  },
  "GER_nww_export_credit_desc": {
    "ru": "Государственные гарантии экспортных контрактов поддержат гражданские предприятия. Торговля станет подготовкой к переговорам, а не поводом для немедленной войны.",
    "en": "Export guarantees support another civilian enterprise. Trade prepares the ground for diplomacy rather than an immediate war."
  },
  "GER_nww_freight_corridors_desc": {
    "ru": "Улучшим инфраструктуру двух собственных германских промышленных регионов. Заводы должны получать уголь и комплектующие до начала новой гонки вооружений.",
    "en": "Improve infrastructure twice in eligible owned and controlled German core regions so industry can receive coal and components."
  },
  "GER_nww_historical_eastern_war_ready": {
    "ru": "Исторический ИИ переходит к восточным военным целям с §Y1941 года§!.",
    "en": "Historical AI pursues eastern war goals in §Y1941§!."
  },
  "GER_nww_historical_plan": {
    "ru": "Железная империя",
    "en": "The Iron Kaiserreich"
  },
  "GER_nww_historical_plan_desc": {
    "ru": "Престолонаследие, усиление военной власти и давление на германскую сферу влияния.",
    "en": "An imperial succession followed by military consolidation and pressure on the German sphere."
  },
  "GER_nww_historical_pressure_ready": {
    "ru": "Исторический ИИ начинает давление на Миттельевропу с §Y1940 года§!.",
    "en": "Historical AI begins coercive pressure in Mitteleuropa in §Y1940§!."
  },
  "GER_nww_industrial_program": {
    "ru": "Имперская промышленная программа",
    "en": "Imperial Industrial Program"
  },
  "GER_nww_industrial_program_desc": {
    "ru": "Согласованные вложения земель, предприятий и технических школ соединяют энергетику, станкостроение и долгосрочные государственные заказы. Промышленные реформы последовательно развивают эту программу.",
    "en": "Coordinated investment by the states, enterprises and technical colleges links energy supply, machine tools and long-term public procurement. Industrial reforms progressively develop this program."
  },
  "GER_nww_industrial_research_desc": {
    "ru": "Университеты, арсеналы и частные лаборатории объединят прикладные программы. Результат сохраняется в общем промышленном духе.",
    "en": "Unite universities, arsenals and private laboratories in applied research, improving the lasting industrial program."
  },
  "GER_nww_industrial_standards_desc": {
    "ru": "Унификация деталей и производственных норм позволит совместить разработки частных фирм с государственными заказами.",
    "en": "Common technical standards integrate private designs with public orders, raising the production efficiency cap."
  },
  "GER_nww_industry_construction_tt": {
    "ru": "Имперская промышленная программа: скорость строительства §G+5%§!.",
    "en": "Imperial Industrial Program: construction speed §G+5%§!."
  },
  "GER_nww_industry_efficiency_tt": {
    "ru": "Имперская промышленная программа: прирост эффективности производства §G+5%§!.",
    "en": "Imperial Industrial Program: production efficiency growth §G+5%§!."
  },
  "GER_nww_industry_energy_tt": {
    "ru": "Имперская промышленная программа: прирост энергии §G+10%§!.",
    "en": "Imperial Industrial Program: energy gain §G+10%§!."
  },
  "GER_nww_industry_maximum_tt": {
    "ru": "Имперская промышленная программа: предел эффективности производства §G+5%§!.",
    "en": "Imperial Industrial Program: production efficiency cap §G+5%§!."
  },
  "GER_nww_industry_output_tt": {
    "ru": "Имперская промышленная программа: выпуск военных заводов §G+5%§!.",
    "en": "Imperial Industrial Program: military factory output §G+5%§!."
  },
  "GER_nww_industry_research_tt": {
    "ru": "Имперская промышленная программа: скорость исследований §G+5%§!.",
    "en": "Imperial Industrial Program: research speed §G+5%§!."
  },
  "GER_nww_investment_guarantees_desc": {
    "ru": "Прозрачные гарантии заказов завершают инвестиционную программу земель. Рост строительства не требует запуска ванильной экономики завоеваний.",
    "en": "Predictable procurement completes the states investment program and permanently improves construction speed."
  },
  "GER_nww_machine_tools_desc": {
    "ru": "Машиностроительные фирмы согласуют выпуск станков, оснастки и запасных частей. Это ускорит развёртывание новых производственных линий.",
    "en": "Coordinate machine tools, fixtures and spare parts to speed the development of new production lines and industrial technology."
  },
  "GER_nww_merchant_contracts_desc": {
    "ru": "Долгосрочные контракты дадут торговому флоту транспорты для устойчивых поставок между метрополией и заморскими владениями.",
    "en": "Long-term shipping contracts supply twenty convoys for trade between the metropole and overseas possessions."
  },
  "GER_nww_prague_network_desc": {
    "ru": "Разведка установит контакты с богемскими автономистами. При наличии La Résistance в агентстве откроется операция против Австрии: каждое завершение даёт +2 к напряжённости и учитывается как немецкий вклад.",
    "en": "Intelligence contacts with Bohemian autonomists unlock an agency operation against Austria with La Resistance. Each completion adds two tension and counts toward German influence."
  },
  "GER_nww_silesian_steel_desc": {
    "ru": "Модернизация силезских домен даст сталь для станков, рельсов и вооружения. Награда предоставляется только при нашем владении и контроле над Силезией.",
    "en": "Modernize Silesian furnaces to supply steel for machinery, railways and armaments. The steel is added only while we own and control the region."
  },
  "GER_nww_supply_resilience_desc": {
    "ru": "Резерв локомотивов и согласованные контракты укрепят снабжение. Программа создаёт реальный транспорт, не заменяя его абстрактной наградой людскими ресурсами.",
    "en": "Provide twenty locomotives to support resilient supply chains and reliable freight transport."
  },
  "GER_nww_synthetic_fuels_desc": {
    "ru": "Разовьём синтетическую переработку в собственном промышленном регионе. Топливная безопасность дополняет, но не заменяет энергетическую систему угля и сетей.",
    "en": "Build a synthetic refinery in an eligible domestic core region. Fuel security complements coal extraction and the electrical grid."
  },
  "GER_nww_technical_colleges_desc": {
    "ru": "Инженерные школы подготовят специалистов для заводов и лабораторий. Их постоянный вклад выражается в общем промышленном духе.",
    "en": "Technical colleges train engineers and laboratory staff, providing a lasting research bonus."
  },
  "GER_nww_worker_housing_desc": {
    "ru": "Жилищные программы снизят напряжённость в растущих промышленных городах. Развитие производственной базы должно сопровождаться улучшением быта.",
    "en": "Housing programs reduce tensions in growing industrial towns and improve national stability."
  },
  "GER_ohl_and_crown_side": {
    "ru": "Верховное командование и корона",
    "en": "OHL and the Crown"
  },
  "GER_organize_ruhr_workers_desc": {
    "ru": "Восстановим рабочие советы и подготовим спартакистский вызов имперскому порядку. Через советы можно нарастить поддержку будущего восстания.",
    "en": "Rebuild the workers councils and prepare a Spartacist challenge to the imperial order. Councils can raise support for the coming uprising."
  },
  "GER_organize_workers_councils": {
    "ru": "Организовать рабочие советы",
    "en": "Organise Workers Councils"
  },
  "GER_organize_workers_councils_desc": {
    "ru": "Потратить 50 политической власти, чтобы получить 10 процентных пунктов поддержки спартакистов. Повторяется через 30 дней до выбора политического пути; баланс сил не меняется.",
    "en": "Spend 50 political power to gain 10 percentage points of Spartacist support. Repeatable every 30 days before committing to a political path; the balance does not move."
  },
  "GER_pan_german_leagues_desc": {
    "ru": "Объединим националистические общества в организованное движение. Их митинги позволят собрать необходимые 40% поддержки для выхода из парламентского тупика.",
    "en": "Organise nationalist associations into a coherent political movement. Their rallies can build the 40% mandate needed to break a parliamentary deadlock."
  },
  "GER_pan_germanism": {
    "ru": "Пангерманизм",
    "en": "Pan-Germanism"
  },
  "GER_pan_germanism_desc": {
    "ru": "Радикальное националистическое движение за расширенное германское государство.",
    "en": "A radical nationalist movement seeking a greater German state."
  },
  "GER_parliamentary_spring_desc": {
    "ru": "При поддержке демократов не менее 40%, усиленном канцлере и балансе правее +0,10 парламент возьмёт престолонаследие под контроль. Ганс Фогель сформирует социал-демократическое правительство; баланс закрепится за рейхстагом.",
    "en": "With at least 40% democratic support, a strengthened chancellor and the balance to the right of +0.10, parliament can take charge of the succession. Hans Vogel forms a social democratic government; the balance is permanently fixed at full Reichstag control."
  },
  "GER_prussian_martial_spirit": {
    "ru": "Прусский воинский дух",
    "en": "Prussian Martial Spirit"
  },
  "GER_prussian_martial_spirit_desc": {
    "ru": "Поколения профессиональных военных сохраняют дисциплину и традиции планирования имперской армии.",
    "en": "Generations of professional service preserve the discipline and planning traditions of the imperial army."
  },
  "GER_prussian_traditions_desc": {
    "ru": "Укрепим государственные и производственные учреждения империи.",
    "en": "Strengthen the imperial institutions and production system."
  },
  "GER_publish_military_audit": {
    "ru": "Опубликовать военные счета",
    "en": "Publish the Military Accounts"
  },
  "GER_publish_military_audit_desc": {
    "ru": "Открытая ревизия укрепляет доверие и влияние парламента. Офицеры недовольны проверкой и временно противятся наступательным инициативам.",
    "en": "An open audit restores confidence and parliamentary influence. Officers resent the scrutiny and temporarily resist offensive initiatives."
  },
  "GER_rally_pan_german_leagues": {
    "ru": "Собрать пангерманские союзы",
    "en": "Rally the Pan-German Leagues"
  },
  "GER_rally_pan_german_leagues_desc": {
    "ru": "Потратить 50 политической власти, чтобы получить 10 процентных пунктов поддержки пангерманистов. Повторяется через 30 дней до выбора политического пути; баланс сил не меняется.",
    "en": "Spend 50 political power to gain 10 percentage points of Pan-German support. Repeatable every 30 days before committing to a political path; the balance does not move."
  },
  "GER_red_rhine_desc": {
    "ru": "Поддержим коммунистические организации Франции, Нидерландов, Бельгии и Люксембурга. Каждая независимая страна сможет допустить агитацию или подавить её. Коммунистическое восстание возможно лишь при значительной местной поддержке и наличии более одной контролируемой области.",
    "en": "Support communist organisations in France, the Netherlands, Belgium and Luxembourg. Each independent recipient may tolerate agitation or suppress it. A communist uprising is possible only with a substantial local movement and more than one controlled state."
  },
  "GER_reichstag_locked_tt": {
    "ru": "Баланс сил навсегда закрепляется за рейхстагом. Решения об усилении военных становятся недоступны.",
    "en": "The balance of power is permanently fixed at full Reichstag control. Military influence decisions are disabled."
  },
  "GER_reichstag_side": {
    "ru": "Рейхстаг",
    "en": "The Reichstag"
  },
  "GER_reichstag_social_compact": {
    "ru": "Согласовать социальный бюджет Рейхстага",
    "en": "Negotiate the Reichstag Social Budget"
  },
  "GER_reichstag_social_compact_desc": {
    "ru": "Парламент финансирует гражданское строительство и общественное согласие ценой снижения воинственных настроений.",
    "en": "Parliament funds civilian construction and social peace, accepting a less martial public mood."
  },
  "GER_reign_in_mitteleuropa_desc": {
    "ru": "Потребуем полного подчинения Литвы-Беларуси и Польши. Наши зависимые страны станут интегрированными марионетками, если система автономии это допускает; независимые правительства могут принять статус марионетки или отказаться. Германия не сможет начать войну с ЛитБелом до 1939 года.\\n\\n$GER_eastern_1939_gate_tt$",
    "en": "Demand binding subordination from Lithuania-Belarus and Poland. Our existing subjects become integrated puppets where the autonomy system permits; independent governments may accept puppet status or refuse. No German war against Lithuania-Belarus may begin before 1939.\\n\\n$GER_eastern_1939_gate_tt$"
  },
  "GER_schlieffen_reborn_desc": {
    "ru": "Современная штабная работа заменит планы прошлого столетия. С 1941 года мы сможем добиваться подчинения Нидерландов и Бельгии. Исторический ИИ сначала должен завершить польскую и австрийскую кампании.",
    "en": "Modern staff work replaces a plan inherited from the last century. From 1941 we can demand the subordination of the Netherlands and Belgium. The historical AI must first settle its Polish and Austrian campaigns."
  },
  "GER_shield_against_the_reds_desc": {
    "ru": "Демократия должна уметь защищаться. Мы получим +15% к обороне на национальных территориях, ещё две добровольческие дивизии и снижение порога мировой напряжённости для добровольцев на 50 пунктов. Разрешим отправку добровольцев и поддержим независимые страны, сопротивляющиеся фашистской или коммунистической агрессии.",
    "en": "Democracy must be able to defend itself. Gain +15% defence on our core territory, two additional volunteer divisions and a 50-point reduction to the volunteer world-tension requirement. Authorise volunteers and support independent states resisting fascist or communist aggression."
  },
  "GER_social_budget": {
    "ru": "Социальный бюджет парламента",
    "en": "Parliamentary Social Budget"
  },
  "GER_social_budget_desc": {
    "ru": "Заказы на гражданское строительство поддерживают компромисс с Рейхстагом.",
    "en": "Civil construction contracts underpin the compromise with the Reichstag."
  },
  "GER_social_democracy": {
    "ru": "Социал-демократия",
    "en": "Social Democracy"
  },
  "GER_social_democracy_desc": {
    "ru": "Парламентское правление, социальные реформы и добровольное международное сотрудничество.",
    "en": "Parliamentary government, social reform and voluntary international cooperation."
  },
  "GER_spartacism": {
    "ru": "Спартакизм",
    "en": "Spartacism"
  },
  "GER_spartacism_desc": {
    "ru": "Революционное германское движение рабочих советов.",
    "en": "A revolutionary German workers council movement."
  },
  "GER_staff_manoeuvres": {
    "ru": "Манёвры Генерального штаба",
    "en": "General Staff Manoeuvres"
  },
  "GER_staff_manoeuvres_desc": {
    "ru": "Совместные учения улучшают планирование и восстановление частей.",
    "en": "Coordinated exercises strengthen planning and the recovery of formations."
  },
  "GER_strike_the_west_desc": {
    "ru": "Реформированная императорская армия готовит поход против Франции. Цель войны на полное завоевание создаёт дипломатическую основу, но победу ещё предстоит одержать на поле боя.",
    "en": "The reformed imperial army prepares a campaign against France. A conquest war goal supplies the diplomatic instrument; victory still has to be won on the battlefield."
  },
  "GER_the_austrian_question_desc": {
    "ru": "Вена должна признать верховенство Берлина и принять статус марионетки. Австрия может отказаться; в этом случае мы получим цель войны для её подчинения.",
    "en": "Vienna must acknowledge the supremacy of Berlin and accept puppet status. Austria may refuse; such a refusal gives us a war goal to enforce its submission."
  },
  "GER_the_austrian_referendum_desc": {
    "ru": "Предложим Вене мирное объединение при демократическом правительстве или союз суверенных государств. Австрия самостоятельно принимает решение и должна находиться в мире; отказ не имеет военных последствий.",
    "en": "Offer Vienna peaceful unification if its government is democratic, or an alliance between sovereign states. Austria decides freely and must be at peace; refusing either arrangement has no military consequences."
  },
  "GER_the_eastern_question_desc": {
    "ru": "Укрепим государственные и производственные учреждения империи.",
    "en": "Strengthen the imperial institutions and production system."
  },
  "GER_the_fleet_question_desc": {
    "ru": "Укрепим государственные и производственные учреждения империи.",
    "en": "Strengthen the imperial institutions and production system."
  },
  "GER_the_gilded_colossus_desc": {
    "ru": "Империя распоряжается рынками и колониями по всему миру, но её учреждения закоснели, а обязательства превышают возможности. Короне предстоит решить, как управлять этой неповоротливой гегемонией.",
    "en": "The empire commands markets and colonies across the world, yet its institutions have grown rigid and its commitments exceed its means. The crown must decide how this unwieldy hegemony will be governed."
  },
  "GER_the_kaiser_endures_desc": {
    "ru": "Укрепим государственные и производственные учреждения империи.",
    "en": "Strengthen the imperial institutions and production system."
  },
  "GER_the_new_reich_desc": {
    "ru": "Милитаризованное националистическое государство готовит дивизии к наступательной войне: +15% атаки, +20% прорыва и +10% скорости дивизий. Завершить военную и административную реформу, удалив обе версии имперского перенапряжения.",
    "en": "A militarised nationalist state mobilises its divisions for offensive war: +15% division attack, +20% breakthrough and +10% division speed. Complete military and administrative reform, removing both versions of Imperial Overstretch."
  },
  "GER_the_new_reich_integrated": {
    "ru": "Новый рейх: оккупационная администрация",
    "en": "The New Reich: Occupation Administration"
  },
  "GER_the_new_reich_integrated_desc": {
    "ru": "Новый рейх сохраняет армейские преимущества и расширяет аппарат принуждения для управления оккупированными территориями ценой увеличения гарнизонов.",
    "en": "The New Reich retains its army bonuses and expands its coercive bureaucracy to manage occupied territories, at the cost of larger garrisons."
  },
  "GER_the_pan_germanic_triumph_desc": {
    "ru": "При поддержке националистов не менее 40% и балансе в тупиковом диапазоне от −0,30 до +0,30 пангерманское движение захватит правительство. Вильгельм III останется номинальным главой до упразднения династии.",
    "en": "With at least 40% nationalist support and a deadlocked balance between -0.30 and +0.30, the Pan-German movement seizes government. Wilhelm III remains its nominal head until the dynasty is abolished."
  },
  "GER_the_potsdam_coup_desc": {
    "ru": "Опираясь на Генеральный штаб, Вильгельм III сосредоточит в своих руках власть, ослабевшую при его отце. Необходимы предварительная поддержка армии, смещение баланса более чем на 10% влево от центра и не менее 40% поддержки монархистов.",
    "en": "With the General Staff behind him, Wilhelm III will seize the powers his father allowed to decay. The army must already have received our backing; military influence must exceed 10% to the left of centre, and the monarchists need at least 40% support."
  },
  "GER_the_second_naval_race_desc": {
    "ru": "Прежнее соперничество за океаны возобновляется. Скорость строительства верфей возрастёт на 15%, их производительность — на 10%. Две технологии крупных кораблей или их модулей получат бонус к исследованиям 100%. Цель войны на завоевание Британии завершит нашу западную стратегию.",
    "en": "An earlier rivalry for the oceans resumes. Shipyard construction rises by 15%, dockyard output by 10%, and two capital-ship or related module technologies receive a 100% research bonus. A conquest war goal against Britain completes our western strategy."
  },
  "GER_the_spartacist_uprising_desc": {
    "ru": "При организованных рабочих и поддержке коммунистов не менее 40% выступим против монархии. Начнётся настоящая гражданская война; игрок перейдёт к коммунистическим повстанцам с 40% исходной военной силы. Для провозглашения республики необходима победа.",
    "en": "With workers organised and at least 40% Communist support, rise against the monarchy. A real civil war begins; the player switches to the Communist insurgents with 40% of the initial military strength. Victory is required before proclaiming the republic."
  },
  "GER_total_assimilation_desc": {
    "ru": "Принудительная администрация ускорит рост подчинения на оккупированных нами территориях на 10% и снизит целевое сопротивление на 10 процентных пунктов. Полицейский аппарат увеличит потребность в гарнизонах на 10%. Эти меры не дают новых национальных территорий.",
    "en": "A coercive occupation administration accelerates compliance growth in our occupied territories by 10% and lowers the resistance target by 10 percentage points. Its extensive policing increases required garrisons by 10%. These measures grant no new national cores."
  },
  "GER_true_constitutional_monarchy_desc": {
    "ru": "Вильгельм III сохраняет корону как конституционный символ, а исполнительная власть переходит избранным министрам. Парламентские институты дают +15% стабильности и +0,20 политической власти в день. Гражданский контроль запускает ту же реформу штабов, что и финансирование армии, снимая штраф к организации.",
    "en": "Wilhelm III retains the crown as a constitutional symbol while elected ministers exercise executive power. Parliamentary institutions grant +15% stability and +0.20 daily political power. Civilian oversight begins the same staff reform as army funding, removing the organisation penalty."
  },
  "GER_workers_militias_desc": {
    "ru": "Создадим единую организацию ополчений на основе фабричных советов: +5 процентных пунктов военнообязанного населения и +10% восстановления организации. Завершить военную и административную реформу, удалив обе версии имперского перенапряжения.",
    "en": "Build a common militia organisation around the factory councils, granting +5 percentage points of recruitable population and +10% organisation recovery. Complete military and administrative reform, removing both versions of Imperial Overstretch."
  },
  "GER_world_revolution_desc": {
    "ru": "Подготовим цели войны для аннексии независимых несоюзных Франции и Британии. Эти западные цели не отменяют ограничений Германии на восточном направлении.",
    "en": "Prepare annexation war goals against independent, non-allied France and Britain. These western objectives never waive Germany’s eastern restrictions."
  },
  "LTB": {
    "ru": "Литва-Беларусь",
    "en": "Lithuania-Belarus"
  },
  "MKN": {
    "ru": "Махновцы",
    "en": "Makhnovists"
  },
  "MTG_naval_treaty_adherent": {
    "ru": "Лондонское морское соглашение",
    "en": "London Naval Agreement"
  },
  "MTG_naval_treaty_adherent_desc": {
    "ru": "Лондонский компромисс Британии, Италии, Германии, Франции, Японии, Китая и США сдерживает стоимость новых морских вооружений. Пределы стоимости проектов (крейсер / тяжёлый корабль / авианосец): 5300 / 10000 / 9500. Существующий флот не подлежит автоматическому списанию.",
    "en": "The London compromise between Britain, Italy, Germany, France, Japan, China and the United States limits the cost of new naval armaments. Design cost limits (cruiser / heavy ship / carrier): 5300 / 10000 / 9500. Existing fleets are not automatically scrapped."
  },
  "NWW_GER_campaign_safety_tt": {
    "ru": "Германия восстанавливает силы или цель втянет её в неподготовленную войну. ИИ ведёт одну наступательную кампанию за раз; после мира требуется 180 дней восстановления, после капитуляции — два года.",
    "en": "Germany is recovering or the target would draw it into an unprepared war. AI conducts one offensive campaign at a time, with 180 days of recovery after peace and two years after capitulation."
  },
  "NWW_GER_quality": {
    "ru": "Промышленная стандартизация",
    "en": "Industrial standardisation"
  },
  "NWW_GER_quality_desc": {
    "ru": "Правительство финансирует эту программу и поддерживает её действие через государственные учреждения.",
    "en": "The government funds this programme and sustains it through public institutions."
  },
  "NWW_legacy_naval_doctrine_bonus": {
    "ru": "Программа изучения доктрины",
    "en": "Doctrine study programme"
  },
  "POL_endecja_ascendant": {
    "ru": "Триумф Эндеции",
    "en": "Endecja Ascendant"
  },
  "POL_endecja_ascendant_desc": {
    "ru": "Национал-демократы сменят режим при поддержке не менее 40% и подготовленном политическом движении.",
    "en": "The National Democrats replace the regime with at least 40% support and a prepared political movement."
  },
  "POL_pragmatic_deal": {
    "ru": "Прагматическая сделка",
    "en": "A Pragmatic Deal"
  },
  "POL_pragmatic_deal_desc": {
    "ru": "Выберем переговоры с Берлином; политический союз всё ещё потребует согласия Германии.",
    "en": "Choose negotiations with Berlin; a political alliance still requires German consent."
  },
  "POL_the_colonels_regime": {
    "ru": "Режим полковников",
    "en": "The Colonels’ Regime"
  },
  "POL_the_colonels_regime_desc": {
    "ru": "Сохраним независимость и власть Санации при мандате не менее 40%.",
    "en": "Preserve independence and Sanation rule with at least 40% support."
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
  "ger_aging_monarch": {
    "ru": "Стареющий монарх",
    "en": "Aging Monarch"
  },
  "ger_aging_monarch_desc": {
    "ru": "Стареющий кайзер держится за привычных придворных, ослабляя стабильность и повышая стоимость назначения политических советников.",
    "en": "The aging Kaiser clings to familiar courtiers, weakening stability and making political appointments more expensive."
  },
  "ger_crisis.1.a": {
    "ru": "Кайзер умер. Да здравствует кайзер!",
    "en": "The Kaiser is dead. Long live the Kaiser!"
  },
  "ger_crisis.1.d": {
    "ru": "Кайзер Вильгельм II скончался. Десятилетиями он возвышался над процветающей, но всё более неподвижной имперской системой: колониальные и континентальные обязательства росли, а политические реформы стояли на месте. Его сын восходит на престол как Вильгельм III. За всеобщим трауром Генеральный штаб и рейхстаг оценивают соотношение сил. Новому правлению предстоит ответить на вопросы, оставленные прежним.",
    "en": "Kaiser Wilhelm II has died. For decades he stood above a prosperous yet increasingly immobile imperial system, its colonial and continental obligations multiplying while political reform stalled. His son now ascends the throne as Wilhelm III. Behind the public mourning, the General Staff and Reichstag measure their strength. The new reign must settle questions that the old one left unanswered."
  },
  "ger_crisis.1.t": {
    "ru": "Смерть кайзера Вильгельма II",
    "en": "The Death of Kaiser Wilhelm II"
  },
  "ger_crisis.10.a": {
    "ru": "Принять германское покровительство.",
    "en": "Accept German protection."
  },
  "ger_crisis.10.b": {
    "ru": "Австрия останется суверенной.",
    "en": "Austria will remain sovereign."
  },
  "ger_crisis.10.d": {
    "ru": "Вильгельм III требует от Австрии признать германское верховенство и принять статус марионетки. Согласие сохранит наше правительство под германским надзором. Отказ даст Берлину повод добиться подчинения силой.",
    "en": "Wilhelm III demands that Austria recognise German supremacy and accept the status of a puppet state. Acceptance preserves our government under German oversight. Refusal will give Berlin a pretext to enforce submission by war."
  },
  "ger_crisis.10.t": {
    "ru": "Берлин требует подчинения Австрии",
    "en": "Berlin Demands Austrian Submission"
  },
  "ger_crisis.20.a": {
    "ru": "Принять имперские условия.",
    "en": "Accept the imperial settlement."
  },
  "ger_crisis.20.b": {
    "ru": "Наш суверенитет не обсуждается.",
    "en": "Our sovereignty is not negotiable."
  },
  "ger_crisis.20.d": {
    "ru": "Имперское правительство в Берлине требует, чтобы государство [ROOT.GetNameDef] официально подчинилось Германии в качестве марионетки. Наши учреждения сохранятся, но внешняя политика и стратегические решения будут зависеть от кайзера. Мы можем отвергнуть требование. Германия обязана не начинать войну с Литвой-Беларусью до 1939 года, хотя отказ оставит затяжной спор.",
    "en": "The imperial government in Berlin demands that [ROOT.GetNameDef] accept formal subordination as a German puppet. Our institutions would survive, but foreign policy and strategic decisions would answer to the Kaiser. We can reject this demand. Germany is bound not to begin war against Lithuania-Belarus before 1939, though refusal will leave a lasting dispute."
  },
  "ger_crisis.20.t": {
    "ru": "Ультиматум Миттельевропы",
    "en": "The Mitteleuropa Ultimatum"
  },
  "ger_crisis.30.a": {
    "ru": "Выбрать демократическое объединение.",
    "en": "Vote for democratic unification."
  },
  "ger_crisis.30.b": {
    "ru": "Вступить в Миттельевропу как суверенный партнёр.",
    "en": "Join Mitteleuropa as a sovereign partner."
  },
  "ger_crisis.30.c": {
    "ru": "Сохранить самостоятельный курс.",
    "en": "Retain our independent course."
  },
  "ger_crisis.30.d": {
    "ru": "Парламентское правительство государства [FROM.GetNameDef] предлагает мирное урегулирование. Демократическая Австрия может добровольно выбрать объединение; альтернативой служит союз суверенных государств. Вена также вправе отказаться без угрозы войны.",
    "en": "The parliamentary government of [FROM.GetNameDef] proposes a peaceful settlement. A democratic Austria may freely choose unification, while a sovereign alliance offers an alternative. Vienna can also decline without inviting war."
  },
  "ger_crisis.30.t": {
    "ru": "Австрийский референдум",
    "en": "An Austrian Referendum"
  },
  "ger_crisis.40.a": {
    "ru": "Согласиться на включение в Германию.",
    "en": "Accept incorporation into Germany."
  },
  "ger_crisis.40.b": {
    "ru": "Австрия будет сопротивляться.",
    "en": "Austria will resist."
  },
  "ger_crisis.40.d": {
    "ru": "Радикальное националистическое правительство в Берлине требует немедленного включения Австрии в своё государство. Согласие означает аннексию; отказ даст Германии цель войны. Решение принимает Австрия, передача территории не происходит автоматически.",
    "en": "The radical nationalist government in Berlin demands that Austria join its state immediately. Acceptance means annexation; refusal will give Germany a war goal. This is an Austrian decision, not an automatic transfer of territory."
  },
  "ger_crisis.40.t": {
    "ru": "Пангерманское требование аннексии",
    "en": "The Pan-German Annexation Demand"
  },
  "ger_crisis.50.a": {
    "ru": "Присоединиться к сообществу.",
    "en": "Join the community."
  },
  "ger_crisis.50.b": {
    "ru": "Предпочесть самостоятельные экономические отношения.",
    "en": "Prefer independent economic relations."
  },
  "ger_crisis.50.d": {
    "ru": "Социал-демократическое правительство государства [FROM.GetNameDef] предлагает вступить в добровольное экономическое и оборонное сообщество. Наш суверенитет признаётся независимо от ответа. Согласие создаст общие экономические институты; отказ не повлечёт ультиматума.",
    "en": "The social democratic government of [FROM.GetNameDef] offers membership in a voluntary economic and defensive community. Our sovereignty is recognised independently of our answer. Acceptance establishes joint economic institutions; refusal brings no ultimatum."
  },
  "ger_crisis.50.t": {
    "ru": "Приглашение в Миттельевропу",
    "en": "An Invitation to Mitteleuropa"
  },
  "ger_crisis.60.a": {
    "ru": "Принять германских товарищей.",
    "en": "Accept our German comrades."
  },
  "ger_crisis.60.b": {
    "ru": "Следовать собственной стратегии.",
    "en": "Pursue our own strategy."
  },
  "ger_crisis.60.d": {
    "ru": "Победившие германские спартакисты предлагают союз с СССР. Если мы возглавляем существующий альянс, они вступят в него; иначе можно создать общий рабочий союз. Решение остаётся за нашим правительством.",
    "en": "The victorious German Spartacists propose an alliance with the Soviet Union. If we lead an existing alliance they will join it; otherwise a common workers alliance can be established. The decision remains with our government."
  },
  "ger_crisis.60.t": {
    "ru": "Предложение Берлина Москве",
    "en": "The Berlin-Moscow Proposal"
  },
  "ger_crisis.70.a": {
    "ru": "Здесь начинается революция!",
    "en": "The revolution begins here!"
  },
  "ger_crisis.70.b": {
    "ru": "Допустить мирную рабочую агитацию.",
    "en": "Allow peaceful workers’ agitation."
  },
  "ger_crisis.70.c": {
    "ru": "Пресечь деятельность организаций с иностранным финансированием.",
    "en": "Disrupt the foreign-funded organisations."
  },
  "ger_crisis.70.d": {
    "ru": "Германские спартакисты связались с местными коммунистическими группами. Их деньги и пропаганда могут усилить движение, но правительство ещё способно его подавить. Там, где коммунисты уже располагают значительной поддержкой, радикалы требуют немедленного вооружённого восстания.",
    "en": "German Spartacist organisers have contacted local communist groups. Their funds and propaganda may strengthen the movement, but the government can still suppress it. Where communist support is already substantial, radicals demand an immediate armed uprising."
  },
  "ger_crisis.70.t": {
    "ru": "Революционная агитация из Германии",
    "en": "Revolutionary Agitation from Germany"
  },
  "ger_news.1.a": {
    "ru": "Европа следит за Берлином.",
    "en": "Europe watches Berlin."
  },
  "ger_news.1.d": {
    "ru": "Берлин объявил о смерти кайзера Вильгельма II и восшествии на престол Вильгельма III. Покойный монарх стоял во главе долгой германской гегемонии, определившей облик Европы без мировой войны. Теперь правительства от Вены до восточной границы задаются вопросом: сохранит ли наследник прежние договорённости или направит военную мощь рейха на установление нового имперского порядка?",
    "en": "Berlin has announced the death of Kaiser Wilhelm II and the accession of Wilhelm III. The late monarch presided over the long German hegemony that shaped Europe without a world war. Now governments from Vienna to the eastern frontier are asking whether his successor will preserve the old arrangements or turn the military weight of the Reich toward a new imperial settlement."
  },
  "ger_news.1.t": {
    "ru": "Уход последнего истинного императора",
    "en": "The Passing of the Last True Emperor"
  },
  "neutrality": {
    "ru": "Нейтралитет",
    "en": "Non-Aligned"
  },
  "neutrality_desc": {
    "ru": "Авторитарный режим",
    "en": "Authoritarian Regime"
  },
  "nww_GER_ai_can_prepare_campaign": {
    "ru": "ИИ должен завершить текущую войну и восстановить армию и внутреннюю устойчивость.",
    "en": "AI must finish its current war and restore its army and domestic stability."
  },
  "nww_GER_ai_can_target_AUS": {
    "ru": "ИИ должен завершить восстановление и оценить силы Австрии, её союзников и гарантов.",
    "en": "AI must finish recovery and assess Austria, its allies and guarantors."
  },
  "nww_GER_ai_can_target_ENG": {
    "ru": "ИИ: мир, восстановление и оценка сил Британии и её союзников.",
    "en": "AI: peace, recovery and assessment of Britain and its allies."
  },
  "nww_GER_ai_can_target_FRA": {
    "ru": "ИИ: мир, восстановление и оценка сил Франции и её союзников.",
    "en": "AI: peace, recovery and assessment of France and its allies."
  },
  "nww_GER_ai_can_target_LTB": {
    "ru": "ИИ: мир, восстановление и оценка риска кампании против Литовско-Белорусского союза.",
    "en": "AI: peace, recovery and assessment of the Lithuanian-Belarusian campaign."
  },
  "nww_GER_ai_can_target_MKN": {
    "ru": "ИИ: мир, восстановление и оценка риска кампании против Вольной территории.",
    "en": "AI: peace, recovery and assessment of the Free Territory campaign."
  },
  "nww_GER_ai_can_target_POL": {
    "ru": "ИИ: мир, восстановление и оценка риска польской кампании.",
    "en": "AI: peace, recovery and assessment of the Polish campaign."
  },
  "nww_GER_ai_can_target_SOV": {
    "ru": "ИИ: мир, восстановление и оценка сил Советской России и её союзников.",
    "en": "AI: peace, recovery and assessment of Soviet Russia and its allies."
  },
  "nww_GER_ai_can_target_UKR": {
    "ru": "ИИ: мир, восстановление и оценка риска украинской кампании.",
    "en": "AI: peace, recovery and assessment of the Ukrainian campaign."
  },
  "nww_aus_overhaul.1.a": {
    "ru": "Признать свершившийся факт",
    "en": "Accept the Separation"
  },
  "nww_aus_overhaul.1.b": {
    "ru": "Подготовить возвращение коронных земель",
    "en": "Prepare to Recover the Crown Lands"
  },
  "nww_aus_overhaul.1.d": {
    "ru": "Переговоры сорваны. Пражский сейм отверг власть Вены и провозгласил независимое государство коронных земель.",
    "en": "Negotiations have collapsed. The Prague Diet rejects Viennas authority and proclaims an independent crown-land state."
  },
  "nww_aus_overhaul.1.t": {
    "ru": "Богемия объявляет независимость",
    "en": "Bohemia Declares Independence"
  },
  "nww_ger_bohemia.1.a": {
    "ru": "Прага входит в нашу сферу влияния.",
    "en": "Prague enters our sphere."
  },
  "nww_ger_bohemia.1.d": {
    "ru": "Наша разведывательная работа обеспечила решающую долю давления, приведшего к разрыву между Прагой и Веной. Новое богемское правительство зависит от германской поддержки и принимает положение вассала империи.",
    "en": "Our intelligence work supplied the decisive share of pressure behind the break between Prague and Vienna. Dependent on German support, the new Bohemian government accepts its place as a puppet of the empire."
  },
  "nww_ger_bohemia.1.t": {
    "ru": "Богемия принимает германское покровительство",
    "en": "Bohemia Accepts German Protection"
  }
}
```

## Воспроизводимость

Повторный экспорт: `python tools/export_ger_focuses.py --snapshot-date YYYY-MM-DD`. В каталоге фокусов только прямые definitions и shared_focus, действительно импортированные в GER_focus. SHA-256 источников:

```text
8dc22c30b80bd2423d01389fe6becd58070582eafbe1fc9756356f11f031e854  common/ai_strategy/GER_lategame_strategies.txt
4b6d65bbbf81c4635e958b49087921d0fe7e4687d2ae1b9c6b5a33ad5d053928  common/ai_strategy/GER_pacing.txt
0699d57eaaa35a3620b17f0a2302c3a7f2c47549ec6a33a7d708d416132daacf  common/ai_strategy/GER_politics.txt
43e6d2e1e53da0f48f6be2e9182ab46f24c57afac9779d0df630ef950e057eda  common/ai_strategy_plans/GER_alternate_strategy_plan.txt
8a673de5c60ce79f95d1b93dfb0ae03a918712ae4b02549aa8e30e345b1d3023  common/ai_strategy_plans/GER_historical.txt
280c7a25da36b07e475987735bbec6373bb652ea7892b6aba19dcc78b045b698  common/ai_strategy_plans/GER_historical_strategy_plan.txt
6a57fad20988de4bc4756a103274278709d0ae01a02a9a18535e1f7e38906d45  common/bop/GER_bop.txt
cbd921fe03ed1ddf89d82cf829f00d0308b4f204829a288c35b814710ad5037a  common/country_leader/GER_traits.txt
2f3b58c76aa8ad10a4a6f52a337497b993d944409dcdcebee0513041eb675e17  common/decisions/GER_bop_decisions.txt
c77a52c8234db9609f9b07889061e93e07d17f81fa2963862099575a403e23c4  common/decisions/categories/GER_categories.txt
398bcbf55a32226b819f24d23f8afe20b7c89fd623110ab1471da9ee43f0f7d5  common/dynamic_modifiers/GER_industry_modifiers.txt
8e4cc97b767f392d4b1c1bb3d02a4bc6f123406a413889bc9a5d75150e47648a  common/factions/templates/GER_templates.txt
cd73161d2064ebbfc9c8426927cd556cfa7963d6cb4789e5837be0738776c74f  common/ideas/GER_ideas.txt
793a1aae0e549854e696edfc78d94a67a6c3ddb6eb263a08e44460d0c2c96dda  common/ideas/zzz_generic.txt
770033acf846e5bf7bf1514484c075d1b1497820e67032b58e51c686f375a2bc  common/national_focus/GER_focuses.txt
23722e3f91518daf83a3d85ba105a7558b30ae18f78700f02c8221dd509f0fec  common/national_focus/GER_native_compatibility.txt
deeeafa22258ee1a845995b0c110e7e79b878e4abb11219a876144cfa3aed592  common/national_focus/GER_political.txt
1d650d24534b7568e1ce936db87e1287fbbd3ce6f0899f4b41aefc90a060456d  common/on_actions/GER_campaign_safety_on_actions.txt
fbb8e625b727452470b0f4a516c18d582da19d4c9f83424ba0b94ac22b3f8ced  common/on_actions/GER_diplomacy_on_actions.txt
2f390aef428593b31cfa9a417b0b8a44682caed292c2a5d56769cc6cfbadbfd7  common/on_actions/GER_industry_on_actions.txt
df883c3a94e0037df5639534c96a3510350b2bfbc6425156aeabd6e61469acb1  common/on_actions/GER_lategame_on_actions.txt
65c35216335290bfab21df581b66636108ce2f13103049658c25fe238f738b3a  common/on_actions/GER_on_actions.txt
fd6ddea6913bf0cb3af7be5dc926577be61890645e875c8ccd789aed82736d87  common/on_actions/GER_pacing_on_actions.txt
504c38f190784c24dde335fc9117a8f86dad64f782c45f76bbeb2774fda70262  common/operations/GER_bohemian_operations.txt
e46b3bd3f0eae111f8c8bb48e03b07bcfcab5fd16d6ff7d610686e90b935be17  common/scripted_effects/AUS_overhaul_effects.txt
bfe2c32a037407f8d74fe369e44868ae51d73d8cebd7743f8a69c982e196071b  common/scripted_effects/GER_bohemian_effects.txt
20592257c16f8ab730c670c706807aec38eb3f0454690ed3d0f1a92482d33e3d  common/scripted_effects/GER_campaign_safety_effects.txt
cd1e7caaa2decbce7eccd31836b60b50fc2bbee2b0ff06384c4d0bf124298007  common/scripted_effects/GER_diplomacy_effects.txt
c741479db9559ef7031b0365cb9f759cf89d84481e5a2dc1e8dc21de0e0e1dd2  common/scripted_effects/GER_effects.txt
917fbba8e0f29394c8f94644fc295fd04b0b63c11c700da5a9cb38bfcb39979a  common/scripted_effects/GER_industry_effects.txt
9a6e116974a251efd39c047255cc8722214c281fcace84403a02105d52ec8248  common/scripted_effects/GER_lategame_effects.txt
2f85642f7c03a6aba64a18615d78373b3b0de03fb64ddec14403b4c40b725773  common/scripted_triggers/GER_bohemian_triggers.txt
48e7e6d96526ba3f767330f9cee2b5db1edb827162aa465cb818b550881bf6ac  common/scripted_triggers/GER_campaign_safety_triggers.txt
c1f51c6f30fccbc3799a94445195f91fdefeb352f947d9c06b909cfe30663854  common/scripted_triggers/GER_lategame_triggers.txt
1a33babdc53c31201d795756641203061ba376909c4a2d81a163ce68f493a357  common/scripted_triggers/GER_pacing_triggers.txt
2b143ba94e7ce12c8ee4af0753a8017af7d57794328237e7aad5e0b5787f0d79  common/scripted_triggers/GER_triggers.txt
06b9bf16c8e6bc1a7b17176e1269f87d5d9270ab877457a69275e132a13c94a1  docs/GER_industry_rework.json
6f19d21f1981c3786bceec9a51e1039d348060dc013256cab9410bb6cdc478cb  docs/GER_overseas_setup.json
b3e48ec6d79e0bdc6d691941ad02cf51bb18cd91d0406b28599592655136217b  events/AUS_overhaul_events.txt
70670a1568e4bfd0a36afffa8bf6f4a107b6f9324b2caa2d3f6a178ae559ed8e  events/GER_bohemian_events.txt
78392fcab30b96cc8ba1f99bd15119a01f49460b3551464a99d4ec69c35b3243  events/GER_events.txt
2715c039727a63e99adae2cf2e5374c2117c9e4b666e77791327b7ae86e4e104  history/countries/GER - Germany.txt
a0d2a12c7c249eed4058ebc462088870f344fb17f9b175e043a35b7c5fb372fc  history/states/42-Rhineland.txt
60bffb081c095ff95005d261cffb298603e4d6c8e76cd934865c71de70b78cf8  history/states/541-South West Africa.txt
dc1dacbd2ce3290c31ab68cf9aa2d8cff541031d0fb752b98367ec6a1d1a6711  history/states/546-Tanganyika.txt
5aee7bbc87dfd9a54aa4a9ee367f1a23149bcb435663b7602093f34ff6056f23  history/states/67-Oberschlesien.txt
2baefcfd7f19d9f206a870dd12fbf2d698e0565a3d9c9228fd4f1e8b7f5ccd27  history/states/69-Sudatenland.txt
7ffa4d5995b74fda5baf1f24dda8670f7f5f643f19a20818daff2f1f965aaf2a  history/states/72-Zaolzie.txt
b5d3e4e53a12b1a914ed0d7eb36e73b185949de595bb6f826dcaa7a1511e0a7d  history/states/74-East Sudatenland.txt
7820b754a01bd47e476e11d0baa1409816bf2d7ec338ffc62fb7ee08c3817b88  history/states/75-Moravia.txt
6db87b5fe32cf7d38f51f7071dce07812460c4299be74358a8d73c648ac7b48e  history/states/9-Czechoslovakia.txt
d6b4f93e50987ec5922a5c6ca8fc5e1fcca7c02fb549dbfe24f457108c41d340  localisation/english/GER_l_english.yml
a0df213a05f9f83101c6786d7c1005830bd41323bc0412fb2b3175cbefa66c30  localisation/english/GER_parties_l_english.yml
b69d77b78f33ac5ff628e2b0ab8010a7bcf7a3731b22bb81aed11c83e2e43bf5  localisation/mod_countries_l_english.yml
a028273b52862db67f5a9cae5d4612c333a97c2dded85e7dc350c6bb5fd38160  localisation/mod_countries_l_russian.yml
836619e11268066723b123ca7d75a78edb836c0404e1da156079cb566160374b  localisation/mod_focus_l_english.yml
c900e99e0e5aa12a2a26affe735af52610677f543cfee120ec10a89629fa242f  localisation/mod_focus_l_russian.yml
0f246f17e5646fe8b0be1aedc7f874883bd75ffacf7ed1b2a5054d722accf4d1  localisation/replace/GER_campaign_safety_l_english.yml
55c29fc2158c518c560ec63c0a26a538165eed2074f0a111c0950135bc4278fc  localisation/replace/GER_campaign_safety_l_russian.yml
8954e3307aaffe44be2a208ff20b255c0be96bdbefef207931174669cb4cea9a  localisation/replace/GER_l_english.yml
b0cfdb851a7b966e4d739fb6a525f2be29b1062d3f47d9b419c097dd9d633cea  localisation/replace/GER_l_russian.yml
96914d9dc42a9c3fbd267a53da170e9f290ae668e4f1616f415f9385ec1207ec  localisation/replace/GER_rework_l_english.yml
afabf24164e129361835650ccf95642568035341de7c6043281e3c94edc104e9  localisation/replace/GER_rework_l_russian.yml
279640ec32fcf9029646eb240c65335225ec2209b29dfbfb9ffd815f67820a6e  localisation/russian/GER_l_russian.yml
907646c625b180f234ae8d16cc1da1be8c06d16ad21fb23d1154c20cb230a8c2  localisation/russian/GER_parties_l_russian.yml
56acf194afc2d26190c06b3ed74fb17913f519568f9cd7caf5cac6187bfcb007  tools/export_ger_focuses.py
6a1698fca9a56fd34464a36b4a309ed1595e09290dfe0638623a7bb592b4f3aa  tools/export_mkn_industrial_focuses.py
05a0b3facf4d97366afef978722e4e2e1dbb6b7d39bbdbc3c3458d1bd47ecc61  tools/hoi4_script.py
```
