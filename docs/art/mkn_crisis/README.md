# Изображения политического кризиса MKN

Исходные `docs/black-horde.jpg`, `docs/iron-fist-train.jpg` и `docs/mahno-death.jpg` предоставлены пользователем. Их исходные промпты неизвестны; оригиналы сохраняются без изменений.

Подготовленные варианты и недостающие изображения созданы встроенным **imagegen**. Для каждого варианта рядом с PNG сохранён точный промпт. CLI/API не использовался. DDS получены только техническим масштабированием и кадрированием PNG; прозрачность сохранена.

Портрет из `mahno-death.jpg` служит референсом памятного фокуса и похоронной сцены. Игровой портрет Махно остаётся прежним.

| Изображение | Сохранённый PNG | Точный промпт | Источник |
| --- | --- | --- | --- |
| Чёрная орда | [black_horde.png](black_horde.png) | [Промпт](black_horde.prompt.txt) | Эмблема пользователя, удалён внешний пергамент |
| Железный кулак на рельсах | [iron_fist_trains.png](iron_fist_trains.png) | [Промпт](iron_fist_trains.prompt.txt) | Поезд пользователя, подготовлен прозрачный вариант |
| Неприступная житница | [impregnable_granary.png](impregnable_granary.png) | [Промпт](impregnable_granary.prompt.txt) | Новое изображение |
| Маяк безгосударственности | [beacon_of_statelessness.png](beacon_of_statelessness.png) | [Промпт](beacon_of_statelessness.prompt.txt) | Новое изображение |
| Уход Батько | [departure_of_batko.png](departure_of_batko.png) | [Промпт](departure_of_batko.prompt.txt) | Памятный медальон по портрету пользователя |
| Похороны Махно | [makhno_funeral.png](makhno_funeral.png) | [Промпт](makhno_funeral.prompt.txt) | Новая широкая сцена по портрету пользователя |

Игровые иконки находятся в `gfx/interface/goals/MKN/focus_*.dds`: холст 96×96, рисунок помещён в 84×84, по краям остаётся не менее шести прозрачных пикселей. Для всех пяти иконок определены обычный спрайт и `_shine` с двумя штатными анимациями подсветки.

Текстуры событий находятся в `gfx/event_pictures/MKN/`: обычное событие — 210×176, новость — 397×153. Размеры проверены по установленным `report_event_generic_funeral.dds` и `news_event_generic_funeral.dds`. Обычный кадр смещён к голове Махно; широкий сохраняет всю центральную сцену.

[Контактный лист в игровом размере](../../mkn_crisis_art_preview.png). [Политическая ветка с новыми иконками](../../mkn_crisis_focus_preview.png).

Пересборка: `python tools/build_mkn_crisis_assets.py`. [assets.json](assets.json) хранит соответствия focus/GFX/PNG/DDS, точные размеры, границы альфа-канала и SHA-256 всех оригиналов. Сохранённые JPG в `references/` побайтно совпадают с файлами пользователя.

Прочитанные игровые референсы: `interface/goals_shine.gfx` — шейдер `gfx/FX/buttonstate.lua`, две анимации `shine_overlay.dds` и маски; `interface/eventpictures.gfx` — спрайты похорон. Существующий `interface/MKN_focus_shine.gfx` использован как рабочий шаблон. Механики, персонажи и тексты событий не изменены.
