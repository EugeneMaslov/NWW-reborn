# Изображения MKN и сохранённые промпты

Все 14 оригиналов созданы встроенным **imagegen**. PNG и точные промпты сохранены в проекте; CLI/API не использовались. Python/Pillow применяется только для разрешённого технического кадрирования, изменения размера и экспорта DDS. Изображение монархического Махно сохранено без перерисовки.

## Эмблемы предприятий

| Предприятие | Оригинал | Промпт |
| --- | --- | --- |
| «Коммунар» | [PNG](mkn_companies/kommunar.png) | [Промпт](mkn_companies/kommunar.prompt.txt) |
| Гуляйпольские оружейные артели | [PNG](mkn_companies/rifle_artels.png) | [Промпт](mkn_companies/rifle_artels.prompt.txt) |
| Никопольские орудийные мастерские | [PNG](mkn_companies/artillery_works.png) | [Промпт](mkn_companies/artillery_works.prompt.txt) |
| «Степной сокол» | [PNG](mkn_companies/air_artels.png) | [Промпт](mkn_companies/air_artels.prompt.txt) |
| «Днепровское крыло» | [PNG](mkn_companies/attack_air_artels.png) | [Промпт](mkn_companies/attack_air_artels.prompt.txt) |
| Херсонские судостроители | [PNG](mkn_companies/kherson_works.png) | [Промпт](mkn_companies/kherson_works.prompt.txt) |
| Лиманские подводные мастерские | [PNG](mkn_companies/submarine_works.png) | [Промпт](mkn_companies/submarine_works.prompt.txt) |

Игровые файлы — `gfx/interface/ideas/MKN/company_*.dds` (64×64). Иконки отдельных фокусов — `focus_*.dds` (96×96). [Контактный лист](../mkn_company_icons_preview.png).

## Новые командиры

Вымышленные персонажи альтернативного лора, с отдельными лицами и одеждой.

| Персонаж | Оригинал | Промпт |
| --- | --- | --- |
| Олександр Гордиенко | [PNG](mkn_commanders/oleksandr_hordiienko.png) | [Промпт](mkn_commanders/oleksandr_hordiienko.prompt.txt) |
| Андрий Дорош | [PNG](mkn_commanders/andrii_dorosh.png) | [Промпт](mkn_commanders/andrii_dorosh.prompt.txt) |
| Микола Коваленко | [PNG](mkn_commanders/mykola_kovalenko.png) | [Промпт](mkn_commanders/mykola_kovalenko.prompt.txt) |
| Роман Даниленко | [PNG](mkn_commanders/roman_danylenko.png) | [Промпт](mkn_commanders/roman_danylenko.prompt.txt) |
| Олена Гриценко | [PNG](mkn_commanders/olena_hrytsenko.png) | [Промпт](mkn_commanders/olena_hrytsenko.prompt.txt) |
| Дмитро Савченко | [PNG](mkn_commanders/dmytro_savchenko.png) | [Промпт](mkn_commanders/dmytro_savchenko.prompt.txt) |
| Яков Левченко | [PNG](mkn_commanders/yakiv_levchenko.png) | [Промпт](mkn_commanders/yakiv_levchenko.prompt.txt) |

Большие портреты — `gfx/leaders/MKN/*.dds` (156×210). Карточки советников — `gfx/interface/ideas/nww_portraits/MKN_*.dds` (65×67), с прозрачными последними шестью строками. [Контактный лист](../mkn_commander_portraits_preview.png). Пересборка — `python tools/build_mkn_assets.py`.
