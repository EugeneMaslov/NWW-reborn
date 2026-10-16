# Полный статический аудит NWW Reborn

Дата и время (Europe/Minsk): 2026-10-16T22:57:07+03:00. Установленная HOI4: 1.19.3.0.

## Краткие результаты

- Инвентаризация рабочего каталога: **2943 файлов**, без Git и служебных кешей.
- Проверено содержимое **2060 файлов**: игровые скрипты, локализация, изображения и арт-манифесты.
- Исходный замер: **0 ошибок**, **0 предупреждений**.
- Устранено диагностик исходного замера: **0 ошибок**, **0 предупреждений**.
- Финальный замер: **23 ошибок**, **5 предупреждений**.

Каталог игры: `D:\Steam\steamapps\common\Hearts of Iron IV`. Windows-путь из AGENTS.md заменён фактическим Linux-путём.

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


## MKN: укрупнение хозяйства и проекты на карте — 2026-10-16

- Две хозяйственные ветки сокращены с 24 до 10 фокусов каждая; 35/70 дней, 525/490 дней на весь путь вместо 840. Взаимные исключения сохранены. Награды объединены с сохранением близких итогов общего духа и прежних сумм фабрик, включая перенесённые решения/проекты.
- Добавлены пять инициатив хозяйственного конгресса и девять региональных проектов по 60 дней с оплатой PP либо занятием двух гражданских фабрик. Проверены отложенная награда, отмена/возврат PP, повторный запуск после отмены и защита от повторного получения.
- Обновлены пересборка `MKN_unified_*`, флаг версии v3, AAT MIO и обычные предприятия, локализация RU/EN, JSON, SVG и экспорт полного кода. Сохранены события mkn.30/mkn.31 и прочие политические/военные ID. Хартия даёт защиту промышленности и ремонт через тот же постоянный дух.
- Уточнения карты/движка: штат 226 внутренний, порт речного проекта расположен в принадлежащем MKN прибрежном 196 (провинция 721); бонус терминалов использует действительный `convoy_retreat_speed`, энергетика — `energy_gain_factor`, ресурс — `coal`.
- Изучены установленные `common/national_focus/sweden.txt`, `common/decisions/SWE.txt` (urbanization/repair_the_mines), `common/decisions/FIN.txt` (weapon caches/motti), `common/decisions/SIA.txt` (develop_phibunsongkhram), `common/military_industrial_organization/organizations/00_generic_organization.txt`, `common/resources/00_resources.txt`, `common/buildings/00_buildings.txt`, `map/definition.csv` и `documentation/{effects,triggers,modifiers}_documentation.md`. Каталог игры и разбор образцов: [MKN_economy_refactor.md](../MKN_economy_refactor.md).
- Проверки: общий валидатор стран, 984 проверки MKN overhaul, новая проверка экономических жизненных циклов и `git diff --check`. Обязательный Windows-путь отсутствует; использован установленный Linux-каталог игры. Новая кампания, старое сохранение и свежий игровой журнал после изменений ещё не проверены.


## MKN: Украина, союзники и портреты — 2026-10-16

- Событие ukr.50 передаёт Одессу (192), а не Черкассы (203), с повторной проверкой владельца/контроллера. Исторический MKN принимает предложение примерно в 1% случаев; текст описывает реальную уступку.
- Общий блок MKN/UKR/SOV закрывает фронтир и отложенное объявление войны. Добавлены нативные отрицательные правила отношений; принятые равная автономия и советское урегулирование защищены от последующего нападения. Исторический пленум принимает автономию, включая явное историческое правило MKN. Прямая неисторическая первая советская развилка остаётся выбором получателя.
- Настройка кампании MKN и четыре AI-последовательности: исторический синдикализм либо один случайный курс (по 25%) с платной подготовкой 40% мандата. Старый фактический выбор и явные настройки имеют приоритет; повторной жеребьёвки нет.
- Восемь скрытых интеграционных фокусов (455 дней) открываются только после прекращения войны, исчезновения UKR и владения/контроля всех 11 её стартовых областей. Национализация перенесена из мгновенной капитуляции в региональные хартии; бонусы развивают один хозяйственный дух и восстанавливаются по версии v4 без повторных наград.
- Подтверждён чёрный RGB-заполнитель 156×210. Встроенный imagegen создал отдельного Цебрия и коллективный совет; сохранены оригиналы/промпты/манифест. Цебрий — художественная интерпретация без подтверждённого фото-референса. Карточка советника 65×67 имеет alpha bounds (4, 2, 61, 60); монарх Махно сохранён.
- Прочитаны установленные FIN historical/alternate AI plans, common/game_rules/00_game_rules.txt (FIN), common/national_focus/finland.txt (AAT allow_branch), events/AAT_Finland.txt:5409, events/BBA_ItaloEthiopianWar.txt:549, documentation/effects_documentation.md (relation rules, layout refresh, portrait update) и triggers_documentation.md. Конкретные изменения, файлы и проверочные команды: [MKN_ukraine_followup.md](../MKN_ukraine_followup.md).
- Проверены модели жизненных циклов и общей страны, портреты и совместимость советского урегулирования. Наблюдательская кампания и свежий игровой журнал после этих изменений ещё не проверены; исправление игрового случая без воспроизведения не заявляется.


## MKN: перенос столицы в Киев — 2026-10-16

- Добавлено одноразовое решение «Перенести столицу в Киев» за 50 PP в отдельной категории украинского самоуправления. Требуются исчезновение UKR и владение/полный контроль штата 202; вся ветка интеграции не обязательна. Проверка повторяется в эффекте; прежняя столица не запоминается для автоматического возврата.
- Прочитаны установленные common/decisions/INS.txt (INS_move_capital_to_amsterdam, INS_move_capital_to_batavia), documentation/effects_documentation.md (set_capital), triggers_documentation.md (has_full_control_of_state), история UKR и штат 202 с Киевом в провинции 525. Подробности: [MKN_ukraine_followup.md](../MKN_ukraine_followup.md).
- Русская/английская локализация и общий валидатор дополнены; проверка кампании и свежего игрового журнала остаётся ручной.

## Подробные результаты по категориям

### Синтаксис и разбор

Устранено: 0. Осталось: 0.

### Графика и ресурсы

Устранено: 0. Осталось: 19.

| Уровень | Файл и строка | Проверка | Результат |
|---|---|---|---|
| error | `common/decisions/MKN_economic_decisions.txt:4` | `sprite_missing` | GFX_decision_decision_generic_construction |
| error | `common/decisions/MKN_economic_decisions.txt:74` | `sprite_missing` | GFX_decision_decision_generic_construction |
| error | `common/decisions/MKN_economic_decisions.txt:108` | `sprite_missing` | GFX_decision_decision_generic_construction |
| error | `common/decisions/MKN_economic_decisions.txt:179` | `sprite_missing` | GFX_decision_decision_generic_construction |
| error | `common/decisions/MKN_economic_decisions.txt:205` | `sprite_missing` | GFX_decision_decision_generic_construction |
| error | `common/decisions/MKN_economic_decisions.txt:234` | `sprite_missing` | GFX_decision_decision_generic_construction |
| error | `common/decisions/MKN_economic_decisions.txt:343` | `sprite_missing` | GFX_decision_decision_generic_construction |
| error | `common/decisions/MKN_economic_decisions.txt:458` | `sprite_missing` | GFX_decision_decision_generic_construction |
| error | `common/decisions/MKN_economic_decisions.txt:556` | `sprite_missing` | GFX_decision_decision_generic_construction |
| error | `common/decisions/MKN_economic_decisions.txt:644` | `sprite_missing` | GFX_decision_decision_generic_construction |
| error | `common/decisions/MKN_economic_decisions.txt:733` | `sprite_missing` | GFX_decision_decision_generic_construction |
| error | `common/decisions/MKN_economic_decisions.txt:815` | `sprite_missing` | GFX_decision_decision_generic_construction |
| error | `common/decisions/MKN_economic_decisions.txt:895` | `sprite_missing` | GFX_decision_decision_generic_construction |
| error | `common/decisions/MKN_economic_decisions.txt:986` | `sprite_missing` | GFX_decision_decision_generic_construction |
| error | `common/decisions/MKN_horizons_decisions.txt:3` | `sprite_missing` | GFX_decision_generic_political_actions |
| error | `common/decisions/MKN_horizons_decisions.txt:36` | `sprite_missing` | GFX_decision_generic_political_actions |
| error | `common/decisions/MKN_horizons_decisions.txt:108` | `sprite_missing` | GFX_decision_generic_political_actions |
| error | `common/decisions/MKN_horizons_decisions.txt:121` | `sprite_missing` | GFX_decision_generic_political_actions |
| error | `common/decisions/MKN_horizons_decisions.txt:149` | `sprite_missing` | GFX_decision_decision_generic_construction |

### Локализация и кодировка

Устранено: 0. Осталось: 4.

| Уровень | Файл и строка | Проверка | Результат |
|---|---|---|---|
| error | `common/ideas/turkey.txt:2581` | `missing` | russian: TUR_debt_repayments |
| error | `common/ideas/turkey.txt:2581` | `missing` | english: TUR_debt_repayments |
| error | `common/scripted_triggers/TUR_campaign_safety_triggers.txt:31` | `missing` | russian: nww_TUR_ai_can_prepare_campaign |
| error | `common/scripted_triggers/TUR_campaign_safety_triggers.txt:31` | `missing` | english: nww_TUR_ai_can_prepare_campaign |

### Карта и регионы

Устранено: 0. Осталось: 0.

### Персонажи и советники

Устранено: 0. Осталось: 0.

### Национальные фокусы

Устранено: 0. Осталось: 0.

### Решения, миссии и переменные

Устранено: 0. Осталось: 2.

| Уровень | Файл и строка | Проверка | Результат |
|---|---|---|---|
| warning | `common/decisions/nww_mkn_decisions.txt:1034` | `variable_init` | MKN_raids_done: явная инициализация в моде не найдена; проверить наследуемые/временные переменные |
| warning | `common/decisions/MKN_military_decisions.txt:1054` | `variable_init` | damaged_building_level@infrastructure: явная инициализация в моде не найдена; проверить наследуемые/временные переменные |

### Инструменты и воспроизводимость

Устранено: 0. Осталось: 3.

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
| `custom_characters` | 341 |
| `custom_focuses` | 3008 |
| `custom_sprites` | 3293 |
| `dds_files` | 326 |
| `dds_non_pot_ui` | 215 |
| `decision_variables` | 65 |
| `decision_variables_without_clamp` | 55 |
| `decisions` | 494 |
| `disabled_compatibility_decisions` | 314 |
| `effective_characters` | 5485 |
| `effective_focuses` | 11742 |
| `effective_provinces` | 13413 |
| `effective_states` | 1082 |
| `hidden_compatibility_focuses` | 2078 |
| `hidden_focus_default_coordinates` | 1812 |
| `image_files` | 466 |
| `localisation_entries` | 9783 |
| `localisation_files` | 94 |
| `missions` | 42 |
| `native_reference_wrappers_restored` | 3 |
| `recruit_references` | 1027 |
| `required_localisation_keys` | 5375 |
| `script_files` | 1459 |
| `sprite_references` | 8828 |
| `state_1082_provinces` | 2 |
| `state_1082_vp` | 1 |
| `state_200_provinces` | 7 |
| `state_200_vp` | 1 |
| `state_lake_provinces` | 118 |
| `strategic_regions` | 304 |
| `texture_references` | 16066 |
| `total_files_scanned` | 2060 |
| `victory_point_entries` | 1501 |
| `workspace_inventory_files` | 2943 |

## Переменные решений

`clamp_variable` принудительно удерживает число в диапазоне min…max. Его отсутствие само по себе не означает ошибку: счётчик может расти, а ID штата нельзя обрезать как шкалу. Этот раздел — реестр и разбор, а не список исправленных багов. **В первом аудите значения, пороги и ограничения перечисленных переменных не менялись.**

| Переменная и назначение | Присваивание / очистка | Защита и диапазон | Что изменено |
|---|---|---|---|
| `AUS_bohemian_investments` — Назначение требует разбора | `common/scripted_effects/AUS_overhaul_effects.txt:627` | Явный clamp не найден | Автоматически не изменялась |
| `AUS_bohemian_tension` — Назначение требует разбора | `common/scripted_effects/AUS_overhaul_effects.txt:644` | Есть явный clamp Места clamp: 0…10 (`common/decisions/AUS_decisions.txt:40`); 0…10 (`common/scripted_effects/AUS_overhaul_effects.txt:597`) | Автоматически не изменялась |
| `FRA_algeria_pressure` — Назначение требует разбора | `common/scripted_effects/FRA_effects.txt:966`, `common/scripted_effects/FRA_effects.txt:1426`, `common/scripted_effects/FRA_effects.txt:1454`, `common/scripted_effects/FRA_effects.txt:1497` | Есть явный clamp Места clamp: 0…100 (`common/scripted_effects/FRA_effects.txt:642`) | Автоматически не изменялась |
| `FRA_equatorial_pressure` — Назначение требует разбора | `common/scripted_effects/FRA_effects.txt:975`, `common/scripted_effects/FRA_effects.txt:2423`, `common/scripted_effects/FRA_effects.txt:2517`, `common/scripted_effects/FRA_effects.txt:2671` | Есть явный clamp Места clamp: 0…100 (`common/scripted_effects/FRA_effects.txt:657`) | Автоматически не изменялась |
| `FRA_indochina_pressure` — Назначение требует разбора | `common/scripted_effects/FRA_effects.txt:978`, `common/scripted_effects/FRA_effects.txt:2740`, `common/scripted_effects/FRA_effects.txt:2812`, `common/scripted_effects/FRA_effects.txt:2929` | Есть явный clamp Места clamp: 0…100 (`common/scripted_effects/FRA_effects.txt:662`) | Автоматически не изменялась |
| `FRA_islands_pressure` — Назначение требует разбора | `common/scripted_effects/FRA_effects.txt:981`, `common/scripted_effects/FRA_effects.txt:2998`, `common/scripted_effects/FRA_effects.txt:3070`, `common/scripted_effects/FRA_effects.txt:3187` | Есть явный clamp Места clamp: 0…100 (`common/scripted_effects/FRA_effects.txt:667`) | Автоматически не изменялась |
| `FRA_maghreb_pressure` — Назначение требует разбора | `common/scripted_effects/FRA_effects.txt:969`, `common/scripted_effects/FRA_effects.txt:1545`, `common/scripted_effects/FRA_effects.txt:1595`, `common/scripted_effects/FRA_effects.txt:1675` | Есть явный clamp Места clamp: 0…100 (`common/scripted_effects/FRA_effects.txt:647`) | Автоматически не изменялась |
| `FRA_mandate` — Назначение требует разбора | `common/scripted_effects/FRA_effects.txt:960`, `events/FRA_events.txt:25`, `events/FRA_events.txt:41` | Есть явный clamp Места clamp: 0…100 (`common/scripted_effects/FRA_effects.txt:632`) | Автоматически не изменялась |
| `FRA_tension` — Назначение требует разбора | `common/scripted_effects/FRA_effects.txt:963` | Есть явный clamp Места clamp: 0…100 (`common/scripted_effects/FRA_effects.txt:637`) | Автоматически не изменялась |
| `FRA_west_africa_pressure` — Назначение требует разбора | `common/scripted_effects/FRA_effects.txt:972`, `common/scripted_effects/FRA_effects.txt:1849`, `common/scripted_effects/FRA_effects.txt:2031`, `common/scripted_effects/FRA_effects.txt:2333` | Есть явный clamp Места clamp: 0…100 (`common/scripted_effects/FRA_effects.txt:652`) | Автоматически не изменялась |
| `MKN_air_air_accidents_factor` — Назначение требует разбора | `common/scripted_effects/nww_mkn_progression.txt:681` | Явный clamp не найден | Автоматически не изменялась |
| `MKN_air_air_ace_generation_chance_factor` — Назначение требует разбора | `common/scripted_effects/nww_mkn_progression.txt:684` | Явный clamp не найден | Автоматически не изменялась |
| `MKN_air_air_agility_factor` — Назначение требует разбора | `common/scripted_effects/nww_mkn_progression.txt:687` | Явный clamp не найден | Автоматически не изменялась |
| `MKN_air_air_attack_factor` — Назначение требует разбора | `common/scripted_effects/nww_mkn_progression.txt:690` | Явный clamp не найден | Автоматически не изменялась |
| `MKN_air_air_cas_efficiency` — Назначение требует разбора | `common/scripted_effects/nww_mkn_progression.txt:693` | Явный clamp не найден | Автоматически не изменялась |
| `MKN_air_air_fuel_consumption_factor` — Назначение требует разбора | `common/scripted_effects/nww_mkn_progression.txt:696` | Явный clamp не найден | Автоматически не изменялась |
| `MKN_air_air_home_defence_factor` — Назначение требует разбора | `common/scripted_effects/nww_mkn_progression.txt:699` | Явный clamp не найден | Автоматически не изменялась |
| `MKN_air_air_intercept_efficiency` — Назначение требует разбора | `common/scripted_effects/nww_mkn_progression.txt:702` | Явный clamp не найден | Автоматически не изменялась |
| `MKN_air_air_interception_detect_factor` — Назначение требует разбора | `common/scripted_effects/nww_mkn_progression.txt:705` | Явный clamp не найден | Автоматически не изменялась |
| `MKN_air_air_mission_efficiency` — Назначение требует разбора | `common/scripted_effects/nww_mkn_progression.txt:708` | Явный clamp не найден | Автоматически не изменялась |
| `MKN_air_air_range_factor` — Назначение требует разбора | `common/scripted_effects/nww_mkn_progression.txt:711` | Явный clamp не найден | Автоматически не изменялась |
| `MKN_air_naval_strike_attack_factor` — Назначение требует разбора | `common/scripted_effects/nww_mkn_progression.txt:714` | Явный clamp не найден | Автоматически не изменялась |
| `MKN_air_recon_factor` — Назначение требует разбора | `common/scripted_effects/nww_mkn_progression.txt:717` | Явный clamp не найден | Автоматически не изменялась |
| `MKN_air_supply_consumption_factor` — Назначение требует разбора | `common/scripted_effects/nww_mkn_progression.txt:720` | Явный clamp не найден | Автоматически не изменялась |
| `MKN_army_army_armor_attack_factor` — Назначение требует разбора | `common/scripted_effects/nww_mkn_progression.txt:609` | Явный clamp не найден | Автоматически не изменялась |
| `MKN_army_army_fuel_consumption_factor` — Назначение требует разбора | `common/scripted_effects/nww_mkn_progression.txt:612` | Явный clamp не найден | Автоматически не изменялась |
| `MKN_army_army_org_factor` — Назначение требует разбора | `common/scripted_effects/nww_mkn_progression.txt:615` | Явный clamp не найден | Автоматически не изменялась |
| `MKN_army_army_speed_factor` — Назначение требует разбора | `common/scripted_effects/nww_mkn_progression.txt:618` | Явный clamp не найден | Автоматически не изменялась |
| `MKN_army_casualty_trickleback` — Назначение требует разбора | `common/scripted_effects/nww_mkn_progression.txt:624` | Явный clamp не найден | Автоматически не изменялась |
| `MKN_army_conscription` — Назначение требует разбора | `common/scripted_effects/nww_mkn_progression.txt:672` | Явный clamp не найден | Автоматически не изменялась |
| `MKN_army_dig_in_speed_factor` — Назначение требует разбора | `common/scripted_effects/nww_mkn_progression.txt:627` | Явный clamp не найден | Автоматически не изменялась |
| `MKN_army_land_reinforce_rate` — Назначение требует разбора | `common/scripted_effects/nww_mkn_progression.txt:633` | Явный clamp не найден | Автоматически не изменялась |
| `MKN_army_max_dig_in` — Назначение требует разбора | `common/scripted_effects/nww_mkn_progression.txt:636` | Явный clamp не найден | Автоматически не изменялась |
| `MKN_army_modifier_army_sub_unit_cavalry_defence_factor` — Назначение требует разбора | `common/scripted_effects/nww_mkn_progression.txt:648` | Явный clamp не найден | Автоматически не изменялась |
| `MKN_army_modifier_army_sub_unit_infantry_defence_factor` — Назначение требует разбора | `common/scripted_effects/nww_mkn_progression.txt:657` | Явный clamp не найден | Автоматически не изменялась |
| `MKN_army_modifier_army_sub_unit_infantry_speed_factor` — Назначение требует разбора | `common/scripted_effects/nww_mkn_progression.txt:660` | Явный clamp не найден | Автоматически не изменялась |
| `MKN_army_org_loss_when_moving` — Назначение требует разбора | `common/scripted_effects/nww_mkn_progression.txt:663` | Явный clamp не найден | Автоматически не изменялась |
| `MKN_army_planning_speed` — Назначение требует разбора | `common/scripted_effects/nww_mkn_progression.txt:666` | Явный clamp не найден | Автоматически не изменялась |
| `MKN_army_supply_consumption_factor` — Назначение требует разбора | `common/scripted_effects/nww_mkn_progression.txt:678` | Явный clamp не найден | Автоматически не изменялась |
| `MKN_navy_convoy_escort_efficiency` — Назначение требует разбора | `common/scripted_effects/nww_mkn_progression.txt:723` | Явный clamp не найден | Автоматически не изменялась |
| `MKN_navy_convoy_raiding_efficiency_factor` — Назначение требует разбора | `common/scripted_effects/nww_mkn_progression.txt:726` | Явный clamp не найден | Автоматически не изменялась |
| `MKN_navy_mines_sweeping_by_fleets_factor` — Назначение требует разбора | `common/scripted_effects/nww_mkn_progression.txt:732` | Явный clamp не найден | Автоматически не изменялась |
| `MKN_navy_naval_coordination` — Назначение требует разбора | `common/scripted_effects/nww_mkn_progression.txt:735` | Явный clamp не найден | Автоматически не изменялась |
| `MKN_navy_naval_defense_factor` — Назначение требует разбора | `common/scripted_effects/nww_mkn_progression.txt:738` | Явный clamp не найден | Автоматически не изменялась |
| `MKN_navy_naval_detection` — Назначение требует разбора | `common/scripted_effects/nww_mkn_progression.txt:741` | Явный clamp не найден | Автоматически не изменялась |
| `MKN_navy_naval_retreat_speed` — Назначение требует разбора | `common/scripted_effects/nww_mkn_progression.txt:744` | Явный clamp не найден | Автоматически не изменялась |
| `MKN_navy_naval_ship_recovery_chance_factor` — Назначение требует разбора | `common/scripted_effects/nww_mkn_progression.txt:747` | Явный clamp не найден | Автоматически не изменялась |
| `MKN_navy_naval_speed_factor` — Назначение требует разбора | `common/scripted_effects/nww_mkn_progression.txt:750` | Явный clamp не найден | Автоматически не изменялась |
| `MKN_navy_naval_torpedo_hit_chance_factor` — Назначение требует разбора | `common/scripted_effects/nww_mkn_progression.txt:753` | Явный clamp не найден | Автоматически не изменялась |
| `MKN_navy_naval_torpedo_reveal_chance_factor` — Назначение требует разбора | `common/scripted_effects/nww_mkn_progression.txt:756` | Явный clamp не найден | Автоматически не изменялась |
| `MKN_navy_navy_casualty_on_sink` — Назначение требует разбора | `common/scripted_effects/nww_mkn_progression.txt:777` | Явный clamp не найден | Автоматически не изменялась |
| `MKN_navy_navy_fuel_consumption_factor` — Назначение требует разбора | `common/scripted_effects/nww_mkn_progression.txt:759` | Явный clamp не найден | Автоматически не изменялась |
| `MKN_navy_navy_submarine_attack_factor` — Назначение требует разбора | `common/scripted_effects/nww_mkn_progression.txt:762` | Явный clamp не найден | Автоматически не изменялась |
| `MKN_navy_navy_submarine_defence_factor` — Назначение требует разбора | `common/scripted_effects/nww_mkn_progression.txt:765` | Явный clamp не найден | Автоматически не изменялась |
| `MKN_navy_navy_submarine_detection_factor` — Назначение требует разбора | `common/scripted_effects/nww_mkn_progression.txt:768` | Явный clamp не найден | Автоматически не изменялась |
| `MKN_navy_repair_speed_factor` — Назначение требует разбора | `common/scripted_effects/nww_mkn_progression.txt:771` | Явный clamp не найден | Автоматически не изменялась |
| `MKN_navy_screening_efficiency` — Назначение требует разбора | `common/scripted_effects/nww_mkn_progression.txt:774` | Явный clamp не найден | Автоматически не изменялась |
| `MKN_raids_done` — Счётчик успешных рейдов | Явная не найдена; см. предупреждения | Стартует с 0; растёт на 1. Перед третьим рейдом значение 2 включает постоянный MKN_ukr_angered. Верхнего предела нет; это счётчик, а не шкала или индекс. | Без изменений; искусственный clamp не добавлялся. |
| `MKN_unified_convoy_retreat_speed` — Назначение требует разбора | `common/scripted_effects/nww_mkn_progression.txt:2` | Явный clamp не найден | Автоматически не изменялась |
| `MKN_unified_energy_gain_factor` — Назначение требует разбора | `common/scripted_effects/nww_mkn_progression.txt:5` | Явный clamp не найден | Автоматически не изменялась |
| `damaged_building_level@infrastructure` — Назначение требует разбора | Явная не найдена; см. предупреждения | Явный clamp не найден | Автоматически не изменялась |
| `mkn_ukr_attacking_state` — ID штата атакующей стороны | `common/decisions/MKN_ukr_border_decisions.txt:247`, `common/scripted_effects/MKN_ukr_border_effects.txt:610` | Присваивается из выбранной области штата; перед отменой боя проверяется has_variable. Числовой clamp мог бы подменить ID другим штатом. | Без изменений; clamp для ID не нужен. |
| `mkn_ukr_defending_state` — ID штата обороняющейся стороны | `common/decisions/MKN_ukr_border_decisions.txt:250`, `common/scripted_effects/MKN_ukr_border_effects.txt:623` | Присваивается из целевого штата; перед отменой боя проверяется has_variable. Это ссылка на штат, а не уровень механики. | Без изменений; clamp для ID не нужен. |
| `mkn_ukr_escalation_level` — Уровень эскалации | `common/scripted_effects/MKN_ukr_border_effects.txt:45`, `common/scripted_effects/MKN_ukr_border_effects.txt:94`, `common/scripted_effects/MKN_ukr_border_effects.txt:124`, `common/scripted_effects/MKN_ukr_border_effects.txt:329`, `common/scripted_effects/MKN_ukr_border_effects.txt:415`, `common/scripted_effects/MKN_ukr_border_effects.txt:465`, `events/MKN_ukr_border_events.txt:207` | Начальное значение 1. Уже существующий clamp поддерживает диапазон 1–5; прямые присваивания используют значения этого диапазона. Места clamp: 1…5 (`common/decisions/MKN_ukr_border_decisions.txt:17`); 1…5 (`common/decisions/MKN_ukr_border_decisions.txt:87`); 1…5 (`common/decisions/MKN_ukr_border_decisions.txt:166`); 1…5 (`common/decisions/MKN_ukr_border_decisions.txt:402`); 1…5 (`common/scripted_effects/MKN_ukr_border_effects.txt:68`) | Без изменений; существующее ограничение проверено. |
| `num_owned_states` — Число принадлежащих стране штатов | `Динамическая переменная движка: documentation/dynamic_variables_documentation.md` | Вычисляемая переменная движка. Её нельзя и не требуется инициализировать или ограничивать через set_variable/clamp_variable. | Без изменений; проверена штатная переменная. |

## Статус верификации

| Проверка | Код возврата | Статус |
|---|---|---|
| Дополнительные валидаторы | — | Не запущены: требуется --verify |

## Повторный запуск

```bash
python tools/full_project_audit.py --game "/home/dima00138/.local/share/Steam/steamapps/common/Hearts of Iron IV" --baseline docs/audit/baseline.json --verify
```

Полные машинные результаты: `docs/audit/latest.json`; исходный замер: `docs/audit/baseline.json`. Аудитор не исправляет контент эвристически при каждом запуске: внесённые исправления находятся в Git и перечислены выше.
