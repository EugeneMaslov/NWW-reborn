# MKN: программно созданные иконки и обработка портретов

> Плоские иконки из этой записи заменены новой рисованной графикой imagegen. Актуальные исходники, промпты и правила сборки: [MKN_art_redesign.md](../MKN_art_redesign.md), [реестр](MKN_hoi4_art.json).

Иконки сделаны через Pillow по прямому требованию пользователя. Генерация новых растров через imagegen не использовалась. Существующие иллюстрированные финальные фокусы и их исходники сохранены.

Задание: «Generate unique focus and idea icons via Python Pillow (PIL) in gfx/interface/goals: GFX_focus_MKN_revkom; GFX_idea_MKN_free_workshops; distinct, visually diverse focus icons for the 4 political branches so they do not look identical». Для портретов: «process all portraits in gfx/leaders/MKN/ and composite any transparent images over a solid neutral dark-gray vignette background (#35383d)».

Мотивы: скрещённое оружие милитаристов, книга Набата, колосья аграриев, постановление и печать ревкома, силуэт вольных мастерских. Знаки щита, колонн, скрещённых инструментов, механизма, вагонетки и направляющей метки различают институты внутри программ. Палитры также различаются. Все фокусные DDS имеют 96×96 пикселей и прозрачные поля.

Сборка: `python tools/build_mkn_overhaul_assets.py --game "/home/dima00138/.local/share/Steam/steamapps/common/Hearts of Iron IV"`.

Исходные PNG: `gfx/generated_sources/MKN_overhaul/`. DDS: `gfx/interface/goals/MKN_*.dds`. Полные PNG прозрачных исходников портретов: `gfx/generated_sources/MKN_overhaul/portraits/`. Уже непрозрачные портреты повторно не перекрашиваются; маленькие портреты советников в других каталогах не обрабатываются.

Спрайты: `interface/MKN_overhaul_icons.gfx`, `interface/MKN_overhaul_shine.gfx`; идеи: MKN-добавления в конце `interface/ideas.gfx`, после сохранённых определений установленной игры. [Превью фактических DDS](../mkn_overhaul_icons_preview.png).
