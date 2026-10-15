# Полный статический аудит NWW Reborn

Дата и время (Europe/Minsk): 2026-10-15T17:59:21+03:00. Установленная HOI4: 1.19.3.0.

## Краткие результаты

- Инвентаризация рабочего каталога: **1960 файлов**, без Git и служебных кешей.
- Проверено содержимое **1699 файлов**: игровые скрипты, локализация, изображения и арт-манифесты.
- Исходный замер: **103 ошибок**, **35 предупреждений**.
- Устранено диагностик исходного замера: **103 ошибок**, **32 предупреждений**.
- Финальный замер: **0 ошибок**, **3 предупреждений**.

Каталог игры: `/home/dima00138/.local/share/Steam/steamapps/common/Hearts of Iron IV`. Windows-путь из AGENTS.md заменён фактическим Linux-путём.

## Методика и границы

**`old-mod/` исключён из аудита по указанию пользователя. Изменений в архиве нет.**

Аудитор читает реальные файлы игры, распакованные DLC и ZIP, затем применяет файловые переопределения мода. Реестры включают только определения соответствующего типа; вложенные event/province ID не становятся ID фокусов. Скобки и кавычки проверяются лексером с полным потреблением текста; комментарии, строки и экранирование учитываются. Локализация учитывает корневые файлы и replace, а также обе языковые папки и наследуемые строки игры. Отсутствие копии ванильного ресурса в моде не считается ошибкой.

Статический анализ не доказывает отсутствие всех логических ошибок в произвольных скриптах. Проверка конфликтов условий ограничена доказуемыми противоречиями AND/NOT; OR и зависимые от мира условия требуют сценариев. Переменные представлены отдельным реестром и дополнительно проверены сценарными валидаторами. Некратные степени двойки размеры интерфейса допустимы: портреты 65×67, фокусы 96×96 и иллюстрации нельзя автоматически растягивать до POT. Статус запуска пользователя и исправлений по его журналу указан отдельно ниже. Успешный статический прогон не подтверждает результат повторного запуска игры после этих исправлений.

## Подтверждённые исправления и ссылки на образцы

### Дополнение по запуску игры 15 октября 2026 года

Пользователь запустил игру после первоначального аудита. Изучен новый
`error.log` с сообщениями 15:18–15:22 по Минску: **165 строк**. Его неизменённый
снимок — `docs/audit/runtime_2026-10-15_error.txt`; пути, время изменения
и SHA-256 журналов записаны в `docs/audit/runtime_2026-10-15.json`.
Ниже указаны исправления после этого запуска. **Повторный запуск игры после
них ещё не проверен; результаты валидаторов ниже относятся к статике
и сценарным моделям.**

| Наблюдение в игре или журнале | Причина | Изменение |
|---|---|---|
| Пропали изображения духов, советников, законов; `Unexpected token: ﻿spriteTypes` | BOM в начале `interface/ideas.gfx` входит в первый токен загрузчика. Из-за отказа всего реестра последовали 67 сообщений о `GFX_idea_traits_strip`, 6 о `GFX_idea_porsche` и 28 сообщений `_small`. | BOM удалён. В сборщике `tools/build_mkn_overhaul_assets.py` исправлена кодировка записи на UTF-8 без BOM. Повторная сборка теперь сохраняет исправления штатных путей вместо восстановления повреждённого реестра из шаблона. |
| В подписях идеологий видны `[GetNwwMkn…]` | Существование зарегистрированного scripted-localisation селектора не означает его вычисление в статическом поле политического интерфейса. | В `localisation/replace/{russian,english}/MKN_ideologies_l_*.yml` возвращены обычные штатные подписи четырёх идеологических групп. Махновские названия партий сохранены отдельно; внутренние группы и правила не менялись. |
| У стартовых шаблонов MKN отсутствуют нормальные названия | В OOB используются `MKN_Povstancheskaya` и `MKN_Konny`, но переводов этих ключей не было. | В обоих `MKN_l_*.yml` добавлены «Повстанческая пехота» / «Insurgent Infantry» и «Конный отряд» / «Cavalry Detachment». Имена-ключи шаблонов и ссылки на них сохранены. |
| `Invalid scope type for effect add_ideas/remove_ideas`, `nww_MKN.txt:388/391` | Обработчики найма/увольнения советника начинают работу в области персонажа. | Для Романа Даниленко перед изменением национального духа добавлена явная область `MKN`, по образцу советников SWE. |
| `Unknown modifier: modifier_army_sub_unit_motorized_attack_factor` | Модификатор был ошибочно составлен из имени батальона; загрузчик не регистрирует его под этим именем. | В `MKN_overhaul_traits.txt` используется документированный `motorized_attack_factor = 0.10`. Бонус и кавалерийская специализация сохранены. Валидатор больше не считает любой синтезированный `modifier_army_sub_unit_*` допустимым. |
| `political_power` — неизвестный trigger в событии Евгена | Для проверки наличия политической власти нужен `has_political_power`. | Условие заменено на `NOT = { has_political_power < 50 }`. Цена −50 ПВ сохранена; сценарии проверяют значения 0, 49.9, 50 и 200. |
| `has_focus_tree` не разрешён в `allowed` советского плана ИИ | `allowed` этого типа определяется статически. | Из `allowed` условие удалено; `original_tag = SOV` сохранён, а проверка `SOV_focus` остаётся в `enable`. |
| Не найдены `soviet_focus` и категория `SOV_paranoia_system` | Отделённые ванильные скрипты всё ещё компилируют литеральные ссылки, даже если их игровое выполнение заблокировано NWW. | В файлах владельца SOV зарегистрированы пустой невыбираемый ID дерева с нулевым весом и полностью скрытая категория без решений. Игровым деревом остаётся `SOV_focus`. Защита на запуске/ежедневной проверке возвращает `SOV_focus`, если ванильный callback загрузил пустой старый ID; завершённые фокусы сохраняются, награды не выполняются. |
| Два предупреждения о `recruit_character` внутри `MKN_repair_personnel` | Новая кампания получала персонажа через вложенный helper вместо прямой записи в истории. | Добавлен прямой `recruit_character = NWW_MKN_eugen` в историю MKN. Защищённый fallback для старых сохранений сохранён. Исчезновение предупреждения в новой кампании требует повторного запуска; поддержка старых сохранений не удалялась ради чистого лога. |

Первоначальный аудит пропустил эти случаи. В частности, чтение через
`utf-8-sig` скрывало BOM от проверки, проверка существования селекторов
не проверяла отрисовку политического интерфейса, а искусственное построение
имён модификаторов ошибочно разрешало моторизованный вариант. Проверки
исправлены; набор регрессионных тестов расширен с 15 до **21**.
Советский валидатор дополнен проверкой невыбираемости совместимого дерева
и тремя сценариями повторяемого восстановления дерева без наград.
Исправлены и соответствующие записи в `tools/patch_mkn_overhaul.py` и
`tools/finalize_mkn_overhaul.py`, чтобы эти генераторы не возвращали
неверный модификатор и эффекты советника без области страны.

Для проверки визуального результата требуется **полностью перезапустить
HOI4**: текущий процесс уже загрузил отвергнутый реестр. Сам факт исправления
файла не доказывает восстановление изображений в уже открытой игре.
Ошибки звука, контрольной суммы DLC, описателей сторонних модов и штатных
3D-моделей не исправлялись в установленной игре.

### Что означал раздел «Переменные решений»

«Нет clamp» означало только отсутствие найденного эффекта `clamp_variable`.
Это не было заключением о баге и не означало, что переменная исправлена.
В первом аудите **ни одна из этих шести переменных не изменялась**. Прежняя
фраза «проверять назначение/сценарии» была незавершённым объяснением;
таблица ниже теперь содержит назначение, реальные ограничения и отдельную
колонку «Что изменено».

- `MKN_raids_done` — накопительный счётчик. При значении 2 до очередного
  увеличения включается флаг гнева Украины: это реакция на третий рейд,
  а не запрет четвёртого и последующих. Добавлять предел 2 или 3 без
  изменения дизайна механики было бы неправильно.
- `mkn_consecutive_border_wars` — счётчик с порогом реакции и сбросом;
  наличие порога не объявляется жёсткой верхней границей.
- `mkn_ukr_attacking_state` и `mkn_ukr_defending_state` хранят ID штатов.
  Ограничение числа могло бы направить конфликт в другой штат.
- `mkn_ukr_escalation_level` уже имела ограничение 1–5; оно проверено,
  но не добавлялось в первом аудите.
- `num_owned_states` вычисляется движком и не требует инициализации.

### Скрипты и инструменты

- В `events/NSB_Soviet.txt` исправлены 12 строк `create_unit`: двойные обратные слеши перед внутренними кавычками заменены правильным экранированием. Обычное равенство числа скобок не обнаруживало эту ошибку: имена дивизий становились свободными токенами внутри блока.
- Исправлен источник повторной порчи: `tools/hoi4_script.py` теперь снимает только внешнюю пару кавычек и не экранирует существующие escape-последовательности повторно. Проверены пять последовательных циклов чтения/записи, в том числе строка с кавычкой в конце.
- Добавлены `tools/full_project_audit.py` и 21 регрессионный тест в `tools/test_full_project_audit.py`. Помимо первоначальных проверок теперь проверяются интерфейсный BOM, статические подписи идеологий, локализация шаблонов MKN, области callbacks советников, различие `allowed`/`enable` ИИ и два фактически отвергнутых движком токена.

### Спрайты и текстуры

- В `interface/ideas.gfx` устранены пять повторных регистраций: `GFX_idea_CZE_army_bop_minus_1`, `GFX_idea_marcel_bucard`, `GFX_idea_CZE_zlin_aircraft`, `GFX_idea_SOV_restoration_and_development_idea_ccp_sov_compatibility`, `GFX_idea_USA_jonathan_wainwright`. Сохранены последние определения, включая более новый портрет Бюкара.
- Исправлены четыре отсутствующих текстуры: производитель вертолётов использует существующую общую авиационную иконку; обе регистрации Персиваля используют `idea_ENG_arthur_percival.dds`; малый портрет Пхахона использует `idea_SIA_phraya_phahon.dds`.
- Регистр `idea_GER_mefo_bills.dds` исправлен на фактический `idea_ger_mefo_bills.dds`. Это только путь иконки; экономика MEFO не включается.
- Нормализованы 32 пути с двойными `/`. Это устранение неоднозначной записи путей, а не 32 отсутствовавшие текстуры: после нормализации соответствующие файлы находились и до исправления.
- В `interface/MKN_decision_categories.gfx` зарегистрирован отсутствовавший `GFX_decision_category_generic_guerilla_base`, используемый двумя категориями MKN. Общий владелец регистрации указан в комментарии; используется штатная текстура игры.
- В советском событии ссылка на протесты исправлена на существующий `GFX_report_event_worker_protests`. В британской истории опечатка `GFX_ENG_nav_bomber1_medium` исправлена на `GFX_ENG_naval_bomber1_medium`.
- `validate_mkn_art.py` продолжает требовать сохранения каждой исходной эффективной регистрации и её параметров. Вместо побайтного совпадения всего списка он допускает только перечисленные выше исправления путей и удаление повторов. Произвольная подмена спрайтов по-прежнему вызывает ошибку.

### Локализация

- Удалены 12 конфликтующих строк — по шесть описаний украинских фокусов из `mod_focus_l_russian.yml` и `mod_focus_l_english.yml`. Единственным владельцем этих описаний стали существующие файлы `nww_UKR_expansion_l_*`, содержащие конкретные описания нынешних механик.
- Добавлен 31 отсутствовавший ключ на каждом языке: **62 строки**. Файлы находятся в `localisation/russian/` и `localisation/english/`: `SOV_audit_l_*`, `TUR_audit_l_*`, `NWW_native_audit_l_*`.
- Имена советников Деникина, Хрущёва и Чакмака используют ссылки на штатные локализованные имена. Для скрытых советских сообщений, скрытых модификаторов и недоступного штатного морского духа добавлены содержательные резервные названия и тексты. Эти строки не включают отключённые подсистемы и не изменяют ID событий или идей.
- Заголовки, BOM, UTF-8, отступы, повторы ключей, цветовые теги, парность `$` и скобок форматтера проверены. Унаследованные ванильные строки с внутренними буквальными кавычками читаются по первой/последней кавычке строки; они не объявляются отсутствующими из-за более строгой проверки файлов самого мода.

### Портреты и воспроизводимость

- Исходный `validate_country_content.py` аварийно завершался из-за отсутствовавших JPG. По той же причине не завершались зависимые проверки; исходные выводы сохранены в `docs/audit/baseline_verification.json`.
- Три PNG в `docs/art/recovered_personnel/` извлечены без потери пикселей из сохранившихся утверждённых DDS. Это доступные источники для повторного экспорта, **не восстановленные оригинальные фотографии высокого разрешения**. Прежние пути и SHA-256 сохранены в отдельных полях манифеста, происхождение описано в README.
- Сборщик умеет использовать эти PNG при отсутствии JPG и сохраняет сведения о происхождении. Валидатор сообщает об отсутствующем источнике или экспорте как об ошибке проверки, без аварии `FileNotFoundError`.
- Повторная сборка выполнена: **все четыре DDS побайтно совпали с исходными**. У карточки Евгена сохранены размер 65×67 и занятая alpha-область `(4, 2, 61, 60)`; нижние семь строк прозрачны. Большие портреты остались отдельными.

### Карта, фокусы, персонажи и решения

- Проверены все 1082 эффективных штата, 13413 провинций и 304 стратегических региона. Каждый сухопутный ID имеет единственный штат; каждый ID провинции — единственный стратегический регион. Проверены типы и уровни зданий по `common/buildings/00_buildings.txt`, принадлежность провинциальных зданий и очков победы штату, береговые ограничения, теги владельцев/контроллеров/национальных территорий, население и категории штатов.
- **Штат 1082**: провинции 429 и 9571, MKN владелец и национальная территория, очко победы внутри штата. **Штат 200**: семь провинций, MKN владелец и национальная территория, очки победы внутри штата. Обязательные позиции аэродромов/ракетных объектов проверены по пикселям `provinces.bmp`; снабжение и железные дороги также прошли проверку. Изменения карты не потребовались.
- Озёрные провинции законно включены в штатные определения игры: 118 таких назначений не ошибочно классифицируются как морские провинции.
- Дубли определений фокусов, отсутствующие родители, циклы и односторонние исключения не обнаружены. Активные фокусы имеют положительную стоимость и целые координаты. У 311 скрытых совместимых определений SOV отсутствуют 622 координатных поля; это не активные элементы раскладки, ID сохранены без добавления искусственных узлов.
- Проверены все 1108 вызовов `recruit_character` в переопределённой истории стран. Слоты советников сверены с установленными ванильными определениями, черты — с реестрами политических, военных и научных черт. Портреты проходят общую проверку ресурсов.
- Категории решений определены; у всех 33 миссий имеются блоки `timeout_effect` и положительные числовые сроки. Пустые блоки отключённых совместимых миссий допустимы. Доказуемых конфликтов AND/NOT между `visible` и `available` не обнаружено.
- `mkn_ukr_escalation_level` явно инициализируется значением 1 и ограничивается `clamp_variable` диапазоном 1–5. Идентификаторы штатов берутся из выбранного текущего состояния и проверяются перед применением; они не требуют числового clamp. Счётчики рейдов и боёв имеют инициализацию и проверки порогов/сброса; `num_owned_states` — вычисляемая переменная движка, ей не требуется `set_variable`. Полный реестр с местами присваиваний и ограничений приведён ниже.
- Проектные сценарные проверки подтверждают сохранение компромисса LTB, 40% политических мандатов, процедур распада и восстановления сохранений, полного завоевания Австрии и Османов, запрета MEFO и советской дипломатии с согласием получателя. Аудит не менял их баланс или сюжетные ограничения.

### Проверенные образцы установленной игры и DLC

Все пути ниже относительны к указанному в отчёте каталогу HOI4:

- `documentation/effects_documentation.md`, раздел `create_unit`: синтаксис вложенной строки дивизии; `events/NSB_Soviet.txt`: реальные вызовы из No Step Back с `\"`.
- `common/characters/SWE.txt`: роли и слоты советников Arms Against Tyranny; `common/scientist_traits/00_traits.txt`: отдельный реестр научных черт.
- `common/national_focus/sweden.txt`: структура дерева Arms Against Tyranny, стоимость и координаты.
- `common/decisions/TUR.txt`: миссии Battle for the Bosporus с `days_mission_timeout` и `timeout_effect`.
- `events/BFTB_Turkey.txt`, блок около строки 774: полный `set_politics` с правящей партией, выборами и периодичностью. Аудит не выносил поля политики из таких блоков.
- `interface/ideas.gfx`, `interface/eventpictures.gfx`, `interface/Technologies.gfx`, `interface/decisions.gfx`: существующие имена и ресурсы спрайтов.
- `common/buildings/00_buildings.txt`, `documentation/dynamic_variables_documentation.md`: актуальные ограничения зданий и вычисляемая `num_owned_states`.
- `localisation/{russian,english}/parties_l_*.yml`: штатные статические подписи идеологических групп; `history/units/SWE_1936.txt`: определения шаблонов дивизий.
- `documentation/triggers_documentation.md`, раздел `has_political_power`, и `documentation/modifiers_documentation.md`, раздел `motorized_attack_factor`: точные имена из текущей игры.
- `common/ai_strategy_plans/SOV_historical_strategy_plan.txt`: `original_tag` в статическом `allowed`, условия состояния игры в `enable`.
- `common/on_actions/03_wtt_on_actions.txt:465`, `common/scripted_effects/SOV_scripted_effects.txt:8012` и `events/NSB_Soviet.txt`: источники компилируемых старых ID советского дерева и категории.

### Журнал, прочитанный до первоначального аудита

Прочитан уже имевшийся `error.log` из пользовательского каталога HOI4; сводка сохранена в `docs/audit/existing_game_log.json`. В нём 211 строк, включая сообщения других модов/движка и 39 повторов прежнего `MKN_effects.txt:50–52: create_unit -- invalid scope state`. У текущего файла эти позиции уже относятся к другому коду, а три вызова `create_unit` находятся в области страны. Этот журнал предшествует аудиту и **не является проверкой внесённых исправлений**. Ошибки ИИ вторжений, звука, корабельного MIO Италии и сторонних описателей не приписываются текущему моду без воспроизведения.

Три оставшихся статических предупреждения относятся к синтаксису установленных файлов игры, перечисленных ниже. Для чтения реестров аудитор восстанавливает только внешние скобки в памяти. Файлы игры не изменяются. Новый пользовательский запуск разобран в начале отчёта; повторная кампания и новый журнал после исправлений его ошибок пока не проверены.

## Подробные результаты по категориям

### Синтаксис и разбор

Устранено: 12. Осталось: 0.

| Файл и строка исходного замера | Проверка | Исходная проблема | Применённое исправление |
|---|---|---|---|
| `events/NSB_Soviet.txt:8465` | `record_scalar` | create_unit: свободные токены внутри блока с именованными параметрами; проверить экранирование строк | Исправлено экранирование create_unit; устранена повторная порча в hoi4_script.py |
| `events/NSB_Soviet.txt:8551` | `record_scalar` | create_unit: свободные токены внутри блока с именованными параметрами; проверить экранирование строк | Исправлено экранирование create_unit; устранена повторная порча в hoi4_script.py |
| `events/NSB_Soviet.txt:8611` | `record_scalar` | create_unit: свободные токены внутри блока с именованными параметрами; проверить экранирование строк | Исправлено экранирование create_unit; устранена повторная порча в hoi4_script.py |
| `events/NSB_Soviet.txt:9572` | `record_scalar` | create_unit: свободные токены внутри блока с именованными параметрами; проверить экранирование строк | Исправлено экранирование create_unit; устранена повторная порча в hoi4_script.py |
| `events/NSB_Soviet.txt:9581` | `record_scalar` | create_unit: свободные токены внутри блока с именованными параметрами; проверить экранирование строк | Исправлено экранирование create_unit; устранена повторная порча в hoi4_script.py |
| `events/NSB_Soviet.txt:12291` | `record_scalar` | create_unit: свободные токены внутри блока с именованными параметрами; проверить экранирование строк | Исправлено экранирование create_unit; устранена повторная порча в hoi4_script.py |
| `events/NSB_Soviet.txt:13250` | `record_scalar` | create_unit: свободные токены внутри блока с именованными параметрами; проверить экранирование строк | Исправлено экранирование create_unit; устранена повторная порча в hoi4_script.py |
| `events/NSB_Soviet.txt:13815` | `record_scalar` | create_unit: свободные токены внутри блока с именованными параметрами; проверить экранирование строк | Исправлено экранирование create_unit; устранена повторная порча в hoi4_script.py |
| `events/NSB_Soviet.txt:13826` | `record_scalar` | create_unit: свободные токены внутри блока с именованными параметрами; проверить экранирование строк | Исправлено экранирование create_unit; устранена повторная порча в hoi4_script.py |
| `events/NSB_Soviet.txt:15192` | `record_scalar` | create_unit: свободные токены внутри блока с именованными параметрами; проверить экранирование строк | Исправлено экранирование create_unit; устранена повторная порча в hoi4_script.py |
| `events/NSB_Soviet.txt:15196` | `record_scalar` | create_unit: свободные токены внутри блока с именованными параметрами; проверить экранирование строк | Исправлено экранирование create_unit; устранена повторная порча в hoi4_script.py |
| `events/NSB_Soviet.txt:15200` | `record_scalar` | create_unit: свободные токены внутри блока с именованными параметрами; проверить экранирование строк | Исправлено экранирование create_unit; устранена повторная порча в hoi4_script.py |

### Графика и ресурсы

Устранено: 46. Осталось: 0.

| Файл и строка исходного замера | Проверка | Исходная проблема | Применённое исправление |
|---|---|---|---|
| `interface/ideas.gfx:2638` | `sprite_duplicate` | GFX_idea_CZE_army_bop_minus_1: повтор из interface/ideas.gfx | Удалён повтор; сохранена последняя регистрация |
| `interface/ideas.gfx:4241` | `sprite_duplicate` | GFX_idea_marcel_bucard: повтор из interface/ideas.gfx | Удалён повтор; сохранена последняя регистрация |
| `interface/ideas.gfx:8215` | `sprite_duplicate` | GFX_idea_CZE_zlin_aircraft: повтор из interface/ideas.gfx | Удалён повтор; сохранена последняя регистрация |
| `interface/ideas.gfx:9073` | `sprite_duplicate` | GFX_idea_SOV_restoration_and_development_idea_ccp_sov_compatibility: повтор из interface/ideas.gfx | Удалён повтор; сохранена последняя регистрация |
| `interface/ideas.gfx:11697` | `sprite_duplicate` | GFX_idea_USA_jonathan_wainwright: повтор из interface/ideas.gfx | Удалён повтор; сохранена последняя регистрация |
| `interface/ideas.gfx:1136` | `texture_missing` | gfx/interface/ideas/idea_generic_helicopter_manufacturer_1.dds | Указан существующий штатный ресурс; см. точные замены выше |
| `interface/ideas.gfx:1997` | `texture_missing` | gfx/interface/ideas/portrait_Britain_arthur_percival.dds | Указан существующий штатный ресурс; см. точные замены выше |
| `interface/ideas.gfx:5990` | `texture_noncanonical` | gfx//interface//ideas//POL_Ideology_Drift_Defence.dds → gfx/interface/ideas/POL_Ideology_Drift_Defence.dds | Двойные / заменены одинарными |
| `interface/ideas.gfx:8006` | `texture_noncanonical` | gfx//interface//ideas//idea_FB.dds → gfx/interface/ideas/idea_FB.dds | Двойные / заменены одинарными |
| `interface/ideas.gfx:8010` | `texture_noncanonical` | gfx//interface//ideas//idea_LRL.dds → gfx/interface/ideas/idea_LRL.dds | Двойные / заменены одинарными |
| `interface/ideas.gfx:8014` | `texture_noncanonical` | gfx//interface//ideas//idea_PWS.dds → gfx/interface/ideas/idea_PWS.dds | Двойные / заменены одинарными |
| `interface/ideas.gfx:8018` | `texture_noncanonical` | gfx//interface//ideas//idea_PZinz.dds → gfx/interface/ideas/idea_PZinz.dds | Двойные / заменены одинарными |
| `interface/ideas.gfx:8022` | `texture_noncanonical` | gfx//interface//ideas//idea_PZL.dds → gfx/interface/ideas/idea_PZL.dds | Двойные / заменены одинарными |
| `interface/ideas.gfx:8026` | `texture_noncanonical` | gfx//interface//ideas//idea_SMPA.dds → gfx/interface/ideas/idea_SMPA.dds | Двойные / заменены одинарными |
| `interface/ideas.gfx:8030` | `texture_noncanonical` | gfx//interface//ideas//idea_Stocznia_Gydia.dds → gfx/interface/ideas/idea_Stocznia_Gydia.dds | Двойные / заменены одинарными |
| `interface/ideas.gfx:8037` | `texture_noncanonical` | gfx//interface//ideas//idea_lithgow_saf.dds → gfx/interface/ideas/idea_lithgow_saf.dds | Двойные / заменены одинарными |
| `interface/ideas.gfx:8041` | `texture_noncanonical` | gfx//interface//ideas//idea_evans_deakin_co.dds → gfx/interface/ideas/idea_evans_deakin_co.dds | Двойные / заменены одинарными |
| `interface/ideas.gfx:8045` | `texture_noncanonical` | gfx//interface//ideas//idea_Cockatoo_doe.dds → gfx/interface/ideas/idea_Cockatoo_doe.dds | Двойные / заменены одинарными |
| `interface/ideas.gfx:8049` | `texture_noncanonical` | gfx//interface//ideas//idea_com_aircraft_corporation.dds → gfx/interface/ideas/idea_com_aircraft_corporation.dds | Двойные / заменены одинарными |
| `interface/ideas.gfx:8053` | `texture_noncanonical` | gfx//interface//ideas//idea_new_south_wales_rc.dds → gfx/interface/ideas/idea_new_south_wales_rc.dds | Двойные / заменены одинарными |
| `interface/ideas.gfx:8057` | `texture_noncanonical` | gfx//interface//ideas//idea_lysaghts_works.dds → gfx/interface/ideas/idea_lysaghts_works.dds | Двойные / заменены одинарными |
| `interface/ideas.gfx:8063` | `texture_noncanonical` | gfx//interface//ideas//idea_mazagon_dock_limited.dds → gfx/interface/ideas/idea_mazagon_dock_limited.dds | Двойные / заменены одинарными |
| `interface/ideas.gfx:8067` | `texture_noncanonical` | gfx//interface//ideas//idea_ishapore_rifle_factory.dds → gfx/interface/ideas/idea_ishapore_rifle_factory.dds | Двойные / заменены одинарными |
| `interface/ideas.gfx:8071` | `texture_noncanonical` | gfx//interface//ideas//idea_ordnance_factories_board.dds → gfx/interface/ideas/idea_ordnance_factories_board.dds | Двойные / заменены одинарными |
| `interface/ideas.gfx:8075` | `texture_noncanonical` | gfx//interface//ideas//idea_hindustan_aircraft.dds → gfx/interface/ideas/idea_hindustan_aircraft.dds | Двойные / заменены одинарными |
| `interface/ideas.gfx:8079` | `texture_noncanonical` | gfx//interface//ideas//idea_garden_reach_shipbuilders.dds → gfx/interface/ideas/idea_garden_reach_shipbuilders.dds | Двойные / заменены одинарными |
| `interface/ideas.gfx:8083` | `texture_noncanonical` | gfx//interface//ideas//idea_scindia_shipyard.dds → gfx/interface/ideas/idea_scindia_shipyard.dds | Двойные / заменены одинарными |
| `interface/ideas.gfx:8089` | `texture_noncanonical` | gfx//interface//ideas//idea_canadian_car_foundry.dds → gfx/interface/ideas/idea_canadian_car_foundry.dds | Двойные / заменены одинарными |
| `interface/ideas.gfx:8093` | `texture_noncanonical` | gfx//interface//ideas//idea_halifax_shipyard.dds → gfx/interface/ideas/idea_halifax_shipyard.dds | Двойные / заменены одинарными |
| `interface/ideas.gfx:8097` | `texture_noncanonical` | gfx//interface//ideas//idea_kingston_shipbuilding.dds → gfx/interface/ideas/idea_kingston_shipbuilding.dds | Двойные / заменены одинарными |
| `interface/ideas.gfx:8101` | `texture_noncanonical` | gfx//interface//ideas//idea_vickers_armstrong_canada.dds → gfx/interface/ideas/idea_vickers_armstrong_canada.dds | Двойные / заменены одинарными |
| `interface/ideas.gfx:8105` | `texture_noncanonical` | gfx//interface//ideas//idea_small_arms_limited.dds → gfx/interface/ideas/idea_small_arms_limited.dds | Двойные / заменены одинарными |
| `interface/ideas.gfx:8109` | `texture_noncanonical` | gfx//interface//ideas//idea_inglis_company.dds → gfx/interface/ideas/idea_inglis_company.dds | Двойные / заменены одинарными |
| `interface/ideas.gfx:8119` | `texture_noncanonical` | gfx//interface//ideas//idea_charlton_mw.dds → gfx/interface/ideas/idea_charlton_mw.dds | Двойные / заменены одинарными |
| `interface/ideas.gfx:8123` | `texture_noncanonical` | gfx//interface//ideas//idea_christchurch_workshops.dds → gfx/interface/ideas/idea_christchurch_workshops.dds | Двойные / заменены одинарными |
| `interface/ideas.gfx:8127` | `texture_noncanonical` | gfx//interface//ideas//idea_nz_railways.dds → gfx/interface/ideas/idea_nz_railways.dds | Двойные / заменены одинарными |
| `interface/ideas.gfx:8131` | `texture_noncanonical` | gfx//interface//ideas//idea_port_chalmers_shipbuilding.dds → gfx/interface/ideas/idea_port_chalmers_shipbuilding.dds | Двойные / заменены одинарными |
| `interface/ideas.gfx:8135` | `texture_noncanonical` | gfx//interface//ideas//idea_st_mary_bay_ship.dds → gfx/interface/ideas/idea_st_mary_bay_ship.dds | Двойные / заменены одинарными |
| `interface/ideas.gfx:8141` | `texture_noncanonical` | gfx//interface//ideas//idea_iscor.dds → gfx/interface/ideas/idea_iscor.dds | Двойные / заменены одинарными |
| `interface/ideas.gfx:9921` | `texture_case` | gfx/interface/ideas/idea_GER_mefo_bills.dds → gfx/interface/ideas/idea_ger_mefo_bills.dds | Указан существующий штатный ресурс; см. точные замены выше |
| `interface/ideas.gfx:11695` | `texture_missing` | gfx/interface/ideas/idea_Britain_arthur_percival_small.dds | Указан существующий штатный ресурс; см. точные замены выше |
| `interface/ideas.gfx:12183` | `texture_missing` | gfx/interface/ideas/portrait_SIA_phraya_phahon_small.dds | Указан существующий штатный ресурс; см. точные замены выше |
| `events/NSB_Soviet.txt:14322` | `sprite_missing` | GFX_report_event_generic_worker_protests | Исправлено имя на зарегистрированный спрайт |
| `history/countries/ENG - Britain.txt:2015` | `sprite_missing` | GFX_ENG_nav_bomber1_medium | Исправлено имя на зарегистрированный спрайт |
| `common/decisions/categories/MKN_bop_categories.txt:13` | `sprite_missing` | GFX_decision_category_generic_guerilla_base | Регистрация MKN_decision_categories.gfx |
| `common/decisions/categories/nww_mkn_categories.txt:1` | `sprite_missing` | GFX_decision_category_generic_guerilla_base | Регистрация MKN_decision_categories.gfx |

### Локализация и кодировка

Устранено: 74. Осталось: 0.

| Файл и строка исходного замера | Проверка | Исходная проблема | Применённое исправление |
|---|---|---|---|
| `localisation/nww_UKR_expansion_l_english.yml:194` | `duplicate` | UKR_rebuild_kiev_desc: повтор ключа из localisation/mod_focus_l_english.yml:28 с другим текстом | Описание сохранено в nww_UKR_expansion_l_*, прежняя копия удалена |
| `localisation/nww_UKR_expansion_l_english.yml:195` | `duplicate` | UKR_dnieper_industry_desc: повтор ключа из localisation/mod_focus_l_english.yml:32 с другим текстом | Описание сохранено в nww_UKR_expansion_l_*, прежняя копия удалена |
| `localisation/nww_UKR_expansion_l_english.yml:198` | `duplicate` | UKR_collectivization_completed_desc: повтор ключа из localisation/mod_focus_l_english.yml:30 с другим текстом | Описание сохранено в nww_UKR_expansion_l_*, прежняя копия удалена |
| `localisation/nww_UKR_expansion_l_english.yml:199` | `duplicate` | UKR_guardians_of_the_steppe_desc: повтор ключа из localisation/mod_focus_l_english.yml:34 с другим текстом | Описание сохранено в nww_UKR_expansion_l_*, прежняя копия удалена |
| `localisation/nww_UKR_expansion_l_english.yml:206` | `duplicate` | UKR_friends_in_moscow_desc: повтор ключа из localisation/mod_focus_l_english.yml:36 с другим текстом | Описание сохранено в nww_UKR_expansion_l_*, прежняя копия удалена |
| `localisation/nww_UKR_expansion_l_english.yml:207` | `duplicate` | UKR_the_makhno_question_desc: повтор ключа из localisation/mod_focus_l_english.yml:38 с другим текстом | Описание сохранено в nww_UKR_expansion_l_*, прежняя копия удалена |
| `localisation/nww_UKR_expansion_l_russian.yml:194` | `duplicate` | UKR_rebuild_kiev_desc: повтор ключа из localisation/mod_focus_l_russian.yml:28 с другим текстом | Описание сохранено в nww_UKR_expansion_l_*, прежняя копия удалена |
| `localisation/nww_UKR_expansion_l_russian.yml:195` | `duplicate` | UKR_dnieper_industry_desc: повтор ключа из localisation/mod_focus_l_russian.yml:32 с другим текстом | Описание сохранено в nww_UKR_expansion_l_*, прежняя копия удалена |
| `localisation/nww_UKR_expansion_l_russian.yml:198` | `duplicate` | UKR_collectivization_completed_desc: повтор ключа из localisation/mod_focus_l_russian.yml:30 с другим текстом | Описание сохранено в nww_UKR_expansion_l_*, прежняя копия удалена |
| `localisation/nww_UKR_expansion_l_russian.yml:199` | `duplicate` | UKR_guardians_of_the_steppe_desc: повтор ключа из localisation/mod_focus_l_russian.yml:34 с другим текстом | Описание сохранено в nww_UKR_expansion_l_*, прежняя копия удалена |
| `localisation/nww_UKR_expansion_l_russian.yml:206` | `duplicate` | UKR_friends_in_moscow_desc: повтор ключа из localisation/mod_focus_l_russian.yml:36 с другим текстом | Описание сохранено в nww_UKR_expansion_l_*, прежняя копия удалена |
| `localisation/nww_UKR_expansion_l_russian.yml:207` | `duplicate` | UKR_the_makhno_question_desc: повтор ключа из localisation/mod_focus_l_russian.yml:38 с другим текстом | Описание сохранено в nww_UKR_expansion_l_*, прежняя копия удалена |
| `common/ideas/zzz_generic.txt:241` | `missing` | russian: MTG_TEST_NAVAL_IDEA | Добавлена строка в localisation/russian/NWW_native_audit_l_russian.yml |
| `common/ideas/zzz_generic.txt:241` | `missing` | english: MTG_TEST_NAVAL_IDEA | Добавлена строка в localisation/english/NWW_native_audit_l_english.yml |
| `events/NSB_Soviet.txt:10032` | `missing` | russian: NSB_Soviet_fascist_civil_war.004.a | Добавлена строка в localisation/russian/SOV_audit_l_russian.yml |
| `events/NSB_Soviet.txt:10032` | `missing` | english: NSB_Soviet_fascist_civil_war.004.a | Добавлена строка в localisation/english/SOV_audit_l_english.yml |
| `events/NSB_Soviet.txt:10025` | `missing` | russian: NSB_Soviet_fascist_civil_war.004.desc | Добавлена строка в localisation/russian/SOV_audit_l_russian.yml |
| `events/NSB_Soviet.txt:10025` | `missing` | english: NSB_Soviet_fascist_civil_war.004.desc | Добавлена строка в localisation/english/SOV_audit_l_english.yml |
| `events/NSB_Soviet.txt:10024` | `missing` | russian: NSB_Soviet_fascist_civil_war.004.t | Добавлена строка в localisation/russian/SOV_audit_l_russian.yml |
| `events/NSB_Soviet.txt:10024` | `missing` | english: NSB_Soviet_fascist_civil_war.004.t | Добавлена строка в localisation/english/SOV_audit_l_english.yml |
| `events/NSB_Soviet.txt:10398` | `missing` | russian: NSB_soviet_civil_war_common.004.a | Добавлена строка в localisation/russian/SOV_audit_l_russian.yml |
| `events/NSB_Soviet.txt:10398` | `missing` | english: NSB_soviet_civil_war_common.004.a | Добавлена строка в localisation/english/SOV_audit_l_english.yml |
| `events/NSB_Soviet.txt:10386` | `missing` | russian: NSB_soviet_civil_war_common.004.desc | Добавлена строка в localisation/russian/SOV_audit_l_russian.yml |
| `events/NSB_Soviet.txt:10386` | `missing` | english: NSB_soviet_civil_war_common.004.desc | Добавлена строка в localisation/english/SOV_audit_l_english.yml |
| `events/NSB_Soviet.txt:10385` | `missing` | russian: NSB_soviet_civil_war_common.004.t | Добавлена строка в localisation/russian/SOV_audit_l_russian.yml |
| `events/NSB_Soviet.txt:10385` | `missing` | english: NSB_soviet_civil_war_common.004.t | Добавлена строка в localisation/english/SOV_audit_l_english.yml |
| `events/NSB_Soviet.txt:10458` | `missing` | russian: NSB_soviet_civil_war_common.005.desc | Добавлена строка в localisation/russian/SOV_audit_l_russian.yml |
| `events/NSB_Soviet.txt:10458` | `missing` | english: NSB_soviet_civil_war_common.005.desc | Добавлена строка в localisation/english/SOV_audit_l_english.yml |
| `events/NSB_Soviet.txt:10457` | `missing` | russian: NSB_soviet_civil_war_common.005.t | Добавлена строка в localisation/russian/SOV_audit_l_russian.yml |
| `events/NSB_Soviet.txt:10457` | `missing` | english: NSB_soviet_civil_war_common.005.t | Добавлена строка в localisation/english/SOV_audit_l_english.yml |
| `events/NSB_Soviet.txt:9717` | `missing` | russian: NSB_soviet_communist_civil_war.007.a | Добавлена строка в localisation/russian/SOV_audit_l_russian.yml |
| `events/NSB_Soviet.txt:9717` | `missing` | english: NSB_soviet_communist_civil_war.007.a | Добавлена строка в localisation/english/SOV_audit_l_english.yml |
| `events/NSB_Soviet.txt:9714` | `missing` | russian: NSB_soviet_communist_civil_war.007.desc | Добавлена строка в localisation/russian/SOV_audit_l_russian.yml |
| `events/NSB_Soviet.txt:9714` | `missing` | english: NSB_soviet_communist_civil_war.007.desc | Добавлена строка в localisation/english/SOV_audit_l_english.yml |
| `events/NSB_Soviet.txt:9713` | `missing` | russian: NSB_soviet_communist_civil_war.007.t | Добавлена строка в localisation/russian/SOV_audit_l_russian.yml |
| `events/NSB_Soviet.txt:9713` | `missing` | english: NSB_soviet_communist_civil_war.007.t | Добавлена строка в localisation/english/SOV_audit_l_english.yml |
| `events/NSB_Soviet.txt:13073` | `missing` | russian: NSB_soviet_nationalist.000.a | Добавлена строка в localisation/russian/SOV_audit_l_russian.yml |
| `events/NSB_Soviet.txt:13073` | `missing` | english: NSB_soviet_nationalist.000.a | Добавлена строка в localisation/english/SOV_audit_l_english.yml |
| `events/NSB_Soviet.txt:13069` | `missing` | russian: NSB_soviet_nationalist.000.desc | Добавлена строка в localisation/russian/SOV_audit_l_russian.yml |
| `events/NSB_Soviet.txt:13069` | `missing` | english: NSB_soviet_nationalist.000.desc | Добавлена строка в localisation/english/SOV_audit_l_english.yml |
| `events/NSB_Soviet.txt:13068` | `missing` | russian: NSB_soviet_nationalist.000.t | Добавлена строка в localisation/russian/SOV_audit_l_russian.yml |
| `events/NSB_Soviet.txt:13068` | `missing` | english: NSB_soviet_nationalist.000.t | Добавлена строка в localisation/english/SOV_audit_l_english.yml |
| `events/NSB_Soviet.txt:1759` | `missing` | russian: NSB_soviet_propaganda_capmaign_events.101.desc | Добавлена строка в localisation/russian/SOV_audit_l_russian.yml |
| `events/NSB_Soviet.txt:1759` | `missing` | english: NSB_soviet_propaganda_capmaign_events.101.desc | Добавлена строка в localisation/english/SOV_audit_l_english.yml |
| `events/NSB_Soviet.txt:1758` | `missing` | russian: NSB_soviet_propaganda_capmaign_events.101.t | Добавлена строка в localisation/russian/SOV_audit_l_russian.yml |
| `events/NSB_Soviet.txt:1758` | `missing` | english: NSB_soviet_propaganda_capmaign_events.101.t | Добавлена строка в localisation/english/SOV_audit_l_english.yml |
| `events/NSB_Soviet.txt:1780` | `missing` | russian: NSB_soviet_propaganda_capmaign_events.102.desc | Добавлена строка в localisation/russian/SOV_audit_l_russian.yml |
| `events/NSB_Soviet.txt:1780` | `missing` | english: NSB_soviet_propaganda_capmaign_events.102.desc | Добавлена строка в localisation/english/SOV_audit_l_english.yml |
| `events/NSB_Soviet.txt:1779` | `missing` | russian: NSB_soviet_propaganda_capmaign_events.102.t | Добавлена строка в localisation/russian/SOV_audit_l_russian.yml |
| `events/NSB_Soviet.txt:1779` | `missing` | english: NSB_soviet_propaganda_capmaign_events.102.t | Добавлена строка в localisation/english/SOV_audit_l_english.yml |
| `events/NSB_Soviet.txt:1801` | `missing` | russian: NSB_soviet_propaganda_capmaign_events.103.desc | Добавлена строка в localisation/russian/SOV_audit_l_russian.yml |
| `events/NSB_Soviet.txt:1801` | `missing` | english: NSB_soviet_propaganda_capmaign_events.103.desc | Добавлена строка в localisation/english/SOV_audit_l_english.yml |
| `events/NSB_Soviet.txt:1800` | `missing` | russian: NSB_soviet_propaganda_capmaign_events.103.t | Добавлена строка в localisation/russian/SOV_audit_l_russian.yml |
| `events/NSB_Soviet.txt:1800` | `missing` | english: NSB_soviet_propaganda_capmaign_events.103.t | Добавлена строка в localisation/english/SOV_audit_l_english.yml |
| `common/ideas/SOV.txt:2985` | `missing` | russian: SOV_non_communism_aversion_ns | Добавлена строка в localisation/russian/SOV_audit_l_russian.yml |
| `common/ideas/SOV.txt:2985` | `missing` | english: SOV_non_communism_aversion_ns | Добавлена строка в localisation/english/SOV_audit_l_english.yml |
| `common/ideas/SOV.txt:3080` | `missing` | russian: SOV_targeted_bonus_against_ENG | Добавлена строка в localisation/russian/SOV_audit_l_russian.yml |
| `common/ideas/SOV.txt:3080` | `missing` | english: SOV_targeted_bonus_against_ENG | Добавлена строка в localisation/english/SOV_audit_l_english.yml |
| `common/ideas/SOV.txt:3094` | `missing` | russian: SOV_targeted_bonus_against_FRA | Добавлена строка в localisation/russian/SOV_audit_l_russian.yml |
| `common/ideas/SOV.txt:3094` | `missing` | english: SOV_targeted_bonus_against_FRA | Добавлена строка в localisation/english/SOV_audit_l_english.yml |
| `common/ideas/SOV.txt:3108` | `missing` | russian: SOV_targeted_bonus_against_GER | Добавлена строка в localisation/russian/SOV_audit_l_russian.yml |
| `common/ideas/SOV.txt:3108` | `missing` | english: SOV_targeted_bonus_against_GER | Добавлена строка в localisation/english/SOV_audit_l_english.yml |
| `common/ideas/SOV.txt:3122` | `missing` | russian: SOV_targeted_bonus_against_ITA | Добавлена строка в localisation/russian/SOV_audit_l_russian.yml |
| `common/ideas/SOV.txt:3122` | `missing` | english: SOV_targeted_bonus_against_ITA | Добавлена строка в localisation/english/SOV_audit_l_english.yml |
| `common/ideas/SOV.txt:3150` | `missing` | russian: SOV_targeted_bonus_against_JAP | Добавлена строка в localisation/russian/SOV_audit_l_russian.yml |
| `common/ideas/SOV.txt:3150` | `missing` | english: SOV_targeted_bonus_against_JAP | Добавлена строка в localisation/english/SOV_audit_l_english.yml |
| `common/ideas/SOV.txt:3136` | `missing` | russian: SOV_targeted_bonus_against_USA | Добавлена строка в localisation/russian/SOV_audit_l_russian.yml |
| `common/ideas/SOV.txt:3136` | `missing` | english: SOV_targeted_bonus_against_USA | Добавлена строка в localisation/english/SOV_audit_l_english.yml |
| `common/characters/TUR.txt:610` | `missing` | russian: TUR_fevzi_cakmak_prime_minister | Добавлена строка в localisation/russian/TUR_audit_l_russian.yml |
| `common/characters/TUR.txt:610` | `missing` | english: TUR_fevzi_cakmak_prime_minister | Добавлена строка в localisation/english/TUR_audit_l_english.yml |
| `common/characters/SOV.txt:2313` | `missing` | russian: anton_denikin | Добавлена строка в localisation/russian/SOV_audit_l_russian.yml |
| `common/characters/SOV.txt:2313` | `missing` | english: anton_denikin | Добавлена строка в localisation/english/SOV_audit_l_english.yml |
| `common/characters/SOV.txt:2559` | `missing` | russian: nikita_khrushchyov | Добавлена строка в localisation/russian/SOV_audit_l_russian.yml |
| `common/characters/SOV.txt:2559` | `missing` | english: nikita_khrushchyov | Добавлена строка в localisation/english/SOV_audit_l_english.yml |

### Карта и регионы

Устранено: 0. Осталось: 0.

### Персонажи и советники

Устранено: 0. Осталось: 0.

### Национальные фокусы

Устранено: 0. Осталось: 0.

### Решения, миссии и переменные

Устранено: 0. Осталось: 0.

### Инструменты и воспроизводимость

Устранено: 3. Осталось: 3.

| Файл и строка исходного замера | Проверка | Исходная проблема | Применённое исправление |
|---|---|---|---|
| `docs/art/MKN_personnel_assets.json:1` | `source_missing` | docs/for-gen/photo-eugen-general.jpg | PNG извлечён из DDS; обновлён манифест, прежнее происхождение сохранено |
| `docs/art/MKN_personnel_assets.json:1` | `source_missing` | docs/for-gen/dmitruk-tratishov-2.jpg | PNG извлечён из DDS; обновлён манифест, прежнее происхождение сохранено |
| `docs/art/MKN_personnel_assets.json:1` | `source_missing` | docs/for-gen/man.jpg | PNG извлечён из DDS; обновлён манифест, прежнее происхождение сохранено |

| Уровень | Файл и строка | Проверка | Результат |
|---|---|---|---|
| warning | `interface/aap_technologies.gfx:238` | `native_parse` | Установленная игра: Незакрытый блок; внешняя скобка восстановлена в памяти для чтения реестра, файл игры не изменён |
| warning | `interface/powerbalanceview.gfx:540` | `native_parse` | Установленная игра: Незакрытый блок; внешняя скобка восстановлена в памяти для чтения реестра, файл игры не изменён |
| warning | `common/national_focus/TSR_lingguang_incident_joint_branch.txt:420` | `native_parse` | Установленная игра: Лишняя закрывающая скобка; внешняя скобка восстановлена в памяти для чтения реестра, файл игры не изменён |

## Объём автоматических проверок

| Метрика | Значение |
|---|---|
| `art_manifests` | 3 |
| `building_entries` | 3095 |
| `custom_characters` | 258 |
| `custom_focuses` | 1983 |
| `custom_sprites` | 2982 |
| `dds_files` | 141 |
| `dds_non_pot_ui` | 95 |
| `decision_variables` | 6 |
| `decision_variables_without_clamp` | 5 |
| `decisions` | 307 |
| `disabled_compatibility_decisions` | 254 |
| `effective_characters` | 5472 |
| `effective_focuses` | 11387 |
| `effective_provinces` | 13413 |
| `effective_states` | 1082 |
| `hidden_compatibility_focuses` | 1251 |
| `hidden_focus_default_coordinates` | 622 |
| `image_files` | 270 |
| `localisation_entries` | 6197 |
| `localisation_files` | 66 |
| `missions` | 33 |
| `native_reference_wrappers_restored` | 3 |
| `recruit_references` | 1109 |
| `required_localisation_keys` | 3936 |
| `script_files` | 1322 |
| `sprite_references` | 7086 |
| `state_1082_provinces` | 2 |
| `state_1082_vp` | 1 |
| `state_200_provinces` | 7 |
| `state_200_vp` | 1 |
| `state_lake_provinces` | 118 |
| `strategic_regions` | 304 |
| `texture_references` | 13270 |
| `total_files_scanned` | 1699 |
| `victory_point_entries` | 1501 |
| `workspace_inventory_files` | 1960 |

## Переменные решений

`clamp_variable` принудительно удерживает число в диапазоне min…max. Его отсутствие само по себе не означает ошибку: счётчик может расти, а ID штата нельзя обрезать как шкалу. Этот раздел — реестр и разбор, а не список исправленных багов. **В первом аудите значения, пороги и ограничения перечисленных переменных не менялись.**

| Переменная и назначение | Присваивание / очистка | Защита и диапазон | Что изменено |
|---|---|---|---|
| `MKN_raids_done` — Счётчик успешных рейдов | `common/national_focus/MKN.txt:1037` | Стартует с 0; растёт на 1. Перед третьим рейдом значение 2 включает постоянный MKN_ukr_angered. Верхнего предела нет; это счётчик, а не шкала или индекс. | Без изменений; искусственный clamp не добавлялся. |
| `mkn_consecutive_border_wars` — Счётчик недавних пограничных боёв | `common/scripted_effects/MKN_ukr_border_effects.txt:48`, `common/scripted_effects/MKN_ukr_border_effects.txt:113`, `common/scripted_effects/MKN_ukr_border_effects.txt:404`, `common/scripted_effects/MKN_ukr_border_effects.txt:486` | Инициализация и сброс в 0; флаг недавнего боя действует 180 дней. При значении >= 3 эскалация становится 5. Это порог реакции, а не жёсткий предел счётчика. | Без изменений; используются порог и сброс. |
| `mkn_ukr_attacking_state` — ID штата атакующей стороны | `common/decisions/MKN_ukr_border_decisions.txt:229`, `common/scripted_effects/MKN_ukr_border_effects.txt:596` | Присваивается из выбранной области штата; перед отменой боя проверяется has_variable. Числовой clamp мог бы подменить ID другим штатом. | Без изменений; clamp для ID не нужен. |
| `mkn_ukr_defending_state` — ID штата обороняющейся стороны | `common/decisions/MKN_ukr_border_decisions.txt:232`, `common/scripted_effects/MKN_ukr_border_effects.txt:609` | Присваивается из целевого штата; перед отменой боя проверяется has_variable. Это ссылка на штат, а не уровень механики. | Без изменений; clamp для ID не нужен. |
| `mkn_ukr_escalation_level` — Уровень эскалации | `common/scripted_effects/MKN_ukr_border_effects.txt:45`, `common/scripted_effects/MKN_ukr_border_effects.txt:94`, `common/scripted_effects/MKN_ukr_border_effects.txt:124`, `common/scripted_effects/MKN_ukr_border_effects.txt:322`, `common/scripted_effects/MKN_ukr_border_effects.txt:401`, `common/scripted_effects/MKN_ukr_border_effects.txt:451`, `events/MKN_ukr_border_events.txt:201` | Начальное значение 1. Уже существующий clamp поддерживает диапазон 1–5; прямые присваивания используют значения этого диапазона. Места clamp: 1…5 (`common/decisions/MKN_ukr_border_decisions.txt:16`); 1…5 (`common/decisions/MKN_ukr_border_decisions.txt:72`); 1…5 (`common/decisions/MKN_ukr_border_decisions.txt:151`); 1…5 (`common/decisions/MKN_ukr_border_decisions.txt:374`); 1…5 (`common/scripted_effects/MKN_ukr_border_effects.txt:68`) | Без изменений; существующее ограничение проверено. |
| `num_owned_states` — Число принадлежащих стране штатов | `Динамическая переменная движка: documentation/dynamic_variables_documentation.md` | Вычисляемая переменная движка. Её нельзя и не требуется инициализировать или ограничивать через set_variable/clamp_variable. | Без изменений; проверена штатная переменная. |

## Статус верификации

| Проверка | Код возврата | Статус |
|---|---|---|
| `validate_country_content.py` | 0 | PASS |
| `validate_runtime_setup.py` | 0 | PASS |
| `validate_soviet_content.py` | 0 | PASS |
| `validate_turkey_balkans.py` | 0 | PASS |
| `validate_austria_campaigns.py` | 0 | PASS |
| `validate_mkn_overhaul.py` | 0 | PASS |
| `validate_mkn_art.py` | 0 | PASS |
| `validate_repository_layout.py` | 0 | PASS |
| `test_full_project_audit.py` | 0 | PASS |
| `git diff --check` | 0 | PASS |

### Вывод `validate_country_content.py`

```text
PASS: MKN_dneprostroi: 24 focuses, one permanent industry spirit, all initial penalties resolved
PASS: MKN_free_cooperatives: 24 focuses, one permanent industry spirit, all initial penalties resolved
PASS: MKN_steel_horses: ten core and ten optional focuses, varied icons/rewards, exclusive program, one service spirit
PASS: MKN_batko_cavalry: ten core and ten optional focuses, varied icons/rewards, exclusive program, one service spirit
PASS: MKN_black_swarm: ten core and ten optional focuses, varied icons/rewards, exclusive program, one service spirit
PASS: MKN_close_support_program: ten core and ten optional focuses, varied icons/rewards, exclusive program, one service spirit
PASS: MKN_coastal_defense_steppe: ten core and ten optional focuses, varied icons/rewards, exclusive program, one service spirit
PASS: MKN_black_sea_smugglers: ten core and ten optional focuses, varied icons/rewards, exclusive program, one service spirit
PASS: seven specialized MIOs, exclusive traits, installed equipment stats, generic templates preserved
PASS: Ukraine 80 focuses, genuine political mandates and foreign acceptance/refusal
PASS: 37 advisors, 10 commanders, seven generated portraits; monarch Makhno preserved
PASS: UKR: 129 migration scenarios, exact parameter replay, no repeated one-off rewards
PASS: MKN: 161 migration scenarios, exact parameter replay, no repeated one-off rewards
PASS: 48 Ukraine political/program combinations, independent diplomacy, equipment and doctrine mastery references
PASS: MKN native BoP ranges, decisions, four political paths, consent-based diplomacy and 22 idempotent repair scenarios
PASS: MKN funeral/mission lifecycle, 32 political focuses, Soviet consent, native modifiers, map conservation and 131 real-script collapse scenarios
PASS: MKN 100-day intervention, sole-survivor races, faction splits, once-only dispatch and 24 real-script scenarios
PASS: MKN/UKR native frontier callbacks, exact-state cores, localization and 43 source-script lifecycle scenarios
PASS: MKN personnel, 32 service combinations, interruption/date/affordability gates, source hashes and native textures
PASS: map initialization: unique states/strategic regions, mandatory air/rocket sites, 1082/200 placement, supply and railway province references
PASS: repository layout: 1306 game files; no tools, previews, caches or case collisions in game data
PASS: LTB_focus: 96 focuses, MKN_focus: 262 focuses, UKR_focus: 80 focuses
PASS: prerequisites/exclusive paths, spacing and panel clearance, localization and unique sprites, portrait bounds, traits and recruitment, concern tier visibility, MIO upgrades, technology sharing, construction, selection menu, startup mission, army crisis gate, old-save settlement scenarios and daily repair, 40% political mandates, timed campaigns and diplomatic acceptance/refusal gates
```

### Вывод `validate_runtime_setup.py`

```text
PASS: 19 German colonies, excluded foreign territories, MEFO removal without repayment, old-save hooks, six transparent LTB icons/highlights, operation IDs, scoped purge suspension and decimal syntax
```

### Вывод `validate_soviet_content.py`

```text
PASS: MKN_dneprostroi: 24 focuses, one permanent industry spirit, all initial penalties resolved
PASS: MKN_free_cooperatives: 24 focuses, one permanent industry spirit, all initial penalties resolved
PASS: MKN_steel_horses: ten core and ten optional focuses, varied icons/rewards, exclusive program, one service spirit
PASS: MKN_batko_cavalry: ten core and ten optional focuses, varied icons/rewards, exclusive program, one service spirit
PASS: MKN_black_swarm: ten core and ten optional focuses, varied icons/rewards, exclusive program, one service spirit
PASS: MKN_close_support_program: ten core and ten optional focuses, varied icons/rewards, exclusive program, one service spirit
PASS: MKN_coastal_defense_steppe: ten core and ten optional focuses, varied icons/rewards, exclusive program, one service spirit
PASS: MKN_black_sea_smugglers: ten core and ten optional focuses, varied icons/rewards, exclusive program, one service spirit
PASS: seven specialized MIOs, exclusive traits, installed equipment stats, generic templates preserved
PASS: Ukraine 80 focuses, genuine political mandates and foreign acceptance/refusal
PASS: 37 advisors, 10 commanders, seven generated portraits; monarch Makhno preserved
PASS: UKR: 129 migration scenarios, exact parameter replay, no repeated one-off rewards
PASS: MKN: 161 migration scenarios, exact parameter replay, no repeated one-off rewards
PASS: 48 Ukraine political/program combinations, independent diplomacy, equipment and doctrine mastery references
PASS: MKN native BoP ranges, decisions, four political paths, consent-based diplomacy and 22 idempotent repair scenarios
PASS: MKN funeral/mission lifecycle, 32 political focuses, Soviet consent, native modifiers, map conservation and 131 real-script collapse scenarios
PASS: MKN 100-day intervention, sole-survivor races, faction splits, once-only dispatch and 24 real-script scenarios
PASS: MKN/UKR native frontier callbacks, exact-state cores, localization and 43 source-script lifecycle scenarios
PASS: MKN personnel, 32 service combinations, interruption/date/affordability gates, source hashes and native textures
PASS: map initialization: unique states/strategic regions, mandatory air/rocket sites, 1082/200 placement, supply and railway province references
PASS: repository layout: 1306 game files; no tools, previews, caches or case collisions in game data
PASS: LTB_focus: 96 focuses, MKN_focus: 262 focuses, UKR_focus: 80 focuses
PASS: prerequisites/exclusive paths, spacing and panel clearance, localization and unique sprites, portrait bounds, traits and recruitment, concern tier visibility, MIO upgrades, technology sharing, construction, selection menu, startup mission, army crisis gate, old-save settlement scenarios and daily repair, 40% political mandates, timed campaigns and diplomatic acceptance/refusal gates
PASS: 2566 Soviet checks; 53 focuses, 14 preserved IDs, staged recovery, repeat-safe save repair, native purge isolation, consent/refusal, protected MKN autonomy and 1939–1940 campaign timing
```

### Вывод `validate_turkey_balkans.py`

```text
PASS: 1634 Ottoman campaign/council scenarios; historical reachability, sequential controlled conquest, true-victor annexation, permanent goals and renewals, six declaration strategies, council cancellation and Kuwait setup
```

### Вывод `validate_austria_campaigns.py`

```text
PASS: 138 conquest/formation scenarios, real-victor scopes, no peacetime annexation, full-country peace priorities, permanent goals, old-save renewal and controlled ownership of all 20 crown-land states
```

### Вывод `validate_mkn_overhaul.py`

```text
PASS: MKN overhaul: 994 checks; pacing, economy, 24 advisors, leaders, real-script 20/30-day actions, terminal cleanup and Soviet target callbacks
```

### Вывод `validate_mkn_art.py`

```text
PASS: 29 distinct painted focus/idea exports, 5 flag masters, 48 flag-lifecycle scenarios, all native sizes/alpha and original idea sprites
```

### Вывод `validate_repository_layout.py`

```text
PASS: 1306 game files; SHA-256 adde425d00b54888a3d333e86b16cefce58e216ae54b34b66c6acbf4f36d8b82
```

### Вывод `test_full_project_audit.py`

```text
test_comments_strings_and_escaped_quotes_do_not_change_brackets (test_full_project_audit.ScriptTests.test_comments_strings_and_escaped_quotes_do_not_change_brackets) ... ok
test_division_string_survives_repeated_serialization (test_full_project_audit.ScriptTests.test_division_string_survives_repeated_serialization) ... ok
test_missing_value_and_extra_brace_are_rejected (test_full_project_audit.ScriptTests.test_missing_value_and_extra_brace_are_rejected) ... ok
test_new_interior_quotes_are_escaped_once (test_full_project_audit.ScriptTests.test_new_interior_quotes_are_escaped_once) ... ok
test_real_engine_rejections_are_not_accepted_as_valid_tokens (test_full_project_audit.ScriptTests.test_real_engine_rejections_are_not_accepted_as_valid_tokens) ... ok
test_trailing_top_level_token_is_rejected (test_full_project_audit.ScriptTests.test_trailing_top_level_token_is_rejected) ... ok
test_unclosed_quote_is_not_silently_discarded (test_full_project_audit.ScriptTests.test_unclosed_quote_is_not_silently_discarded) ... ok
test_advisor_effects_need_a_country_scope (test_full_project_audit.WorkspaceTests.test_advisor_effects_need_a_country_scope) ... ok
test_ai_static_allowed_and_runtime_enable_are_different (test_full_project_audit.WorkspaceTests.test_ai_static_allowed_and_runtime_enable_are_different) ... ok
test_broken_division_escaping_is_detected_even_with_balanced_braces (test_full_project_audit.WorkspaceTests.test_broken_division_escaping_is_detected_even_with_balanced_braces) ... ok
test_cycles_and_asymmetric_exclusions_are_detected (test_full_project_audit.WorkspaceTests.test_cycles_and_asymmetric_exclusions_are_detected) ... ok
test_dlc_zip_textures_and_case_sensitive_paths_are_resolved (test_full_project_audit.WorkspaceTests.test_dlc_zip_textures_and_case_sensitive_paths_are_resolved) ... ok
test_duplicate_focus_ids_do_not_collect_nested_event_ids (test_full_project_audit.WorkspaceTests.test_duplicate_focus_ids_do_not_collect_nested_event_ids) ... ok
test_interface_bom_is_rejected_despite_a_balanced_ast (test_full_project_audit.WorkspaceTests.test_interface_bom_is_rejected_despite_a_balanced_ast) ... ok
test_localisation_bom_duplicate_and_colour_errors_are_detected (test_full_project_audit.WorkspaceTests.test_localisation_bom_duplicate_and_colour_errors_are_detected) ... ok
test_missing_mkn_template_labels_are_checked_in_both_languages (test_full_project_audit.WorkspaceTests.test_missing_mkn_template_labels_are_checked_in_both_languages) ... ok
test_missing_parent_in_selected_tree_is_detected (test_full_project_audit.WorkspaceTests.test_missing_parent_in_selected_tree_is_detected) ... ok
test_mod_filename_override_replaces_native_definition (test_full_project_audit.WorkspaceTests.test_mod_filename_override_replaces_native_definition) ... ok
test_or_branches_are_not_reported_as_contradictory_conjunctions (test_full_project_audit.WorkspaceTests.test_or_branches_are_not_reported_as_contradictory_conjunctions) ... ok
test_replace_path_removes_inherited_files (test_full_project_audit.WorkspaceTests.test_replace_path_removes_inherited_files) ... ok
test_static_ideology_ui_does_not_accept_scripted_callbacks (test_full_project_audit.WorkspaceTests.test_static_ideology_ui_does_not_accept_scripted_callbacks) ... ok

----------------------------------------------------------------------
Ran 21 tests in 0.009s

OK
```

### Вывод `git diff --check`

```text
(пустой вывод)
```

## Повторный запуск

```bash
python tools/full_project_audit.py --game "/home/dima00138/.local/share/Steam/steamapps/common/Hearts of Iron IV" --baseline docs/audit/baseline.json --verify
```

Полные машинные результаты: `docs/audit/latest.json`; исходный замер: `docs/audit/baseline.json`. Аудитор не исправляет контент эвристически при каждом запуске: внесённые исправления находятся в Git и перечислены выше.
