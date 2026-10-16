"""Export complete agrarian definitions as reviewable Markdown file blocks."""
from pathlib import Path
from hoi4_script import read, one, values
from export_mkn_industrial_focuses import script
from validate_mkn_agrarians import FOCUSES


ROOT = Path(__file__).resolve().parents[1]
focuses = {one(f,'id'):f for f in values(one(read(ROOT/'common/national_focus/MKN.txt'),'focus_tree'),'focus')}
out = ['# MKN: готовые блоки файлов аграрной ветки', '',
       'Код уже внесён в рабочий проект. Повторно вставлять определения не нужно. '
       'При конфликте чисел использованы значения из описаний фокусов. '
       'Механики, исходные образцы DLC и ограничения: [MKN_agrarians.md](MKN_agrarians.md).', '',
       '## common/national_focus/MKN.txt', '',
       'Внутрь существующего `focus_tree`:', '', '```pdx',
       script([('focus',focuses[fid],'=') for fid in FOCUSES]), '```', '']
files = ['common/ideas/MKN_agrarian_ideas.txt',
         'common/dynamic_modifiers/MKN_agrarian_modifiers.txt',
         'common/technologies/MKN_agrarian_technologies.txt',
         'common/opinion_modifiers/MKN_agrarian_opinions.txt',
         'common/scripted_effects/MKN_agrarian_effects.txt',
         'common/on_actions/MKN_agrarian_on_actions.txt']
for file in files:
    out += ['## '+file, '', 'Новый файл целиком.', '', '```pdx',
            (ROOT/file).read_text(encoding='utf-8-sig').rstrip(), '```', '']
category = one(read(ROOT/'common/decisions/MKN_decisions.txt'),'MKN_steppe_operations_category')
out += ['## common/decisions/MKN_decisions.txt', '',
        'Добавить внутрь существующей категории `MKN_steppe_operations_category`:', '', '```pdx',
        script([('MKN_barter_grain_surplus',one(category,'MKN_barter_grain_surplus'),'=')]), '```', '']
category = one(read(ROOT/'common/decisions/categories/MKN_bop_categories.txt'),'MKN_steppe_operations_category')
out += ['## common/decisions/categories/MKN_bop_categories.txt', '',
        'Заменить определение прежней категории целиком, сохранив остальные категории файла:', '', '```pdx',
        script([('MKN_steppe_operations_category',category,'=')]), '```', '']
for lang in ('russian','english'):
    file=f'localisation/{lang}/MKN_agrarian_l_{lang}.yml'
    out += ['## '+file, '', 'Новый файл целиком, UTF-8 с BOM.', '', '```yaml',
            (ROOT/file).read_text(encoding='utf-8-sig').rstrip(), '```', '']
file='interface/MKN_political_expansions.gfx'
out += ['## '+file, '',
        'Новый файл целиком. Содержит обычные и светящиеся спрайты всех 36 новых политических фокусов. '
        'Текстуры, исходники и точные промпты перечислены в '
        '[манифесте](art/mkn_political_expansions/assets.json).', '', '```pdx',
        (ROOT/file).read_text().rstrip(), '```', '',
        'Предпросмотр: [96×96](mkn_political_expansions_preview_1x.png), '
        '[увеличение ×2](mkn_political_expansions_preview_2x.png).', '']
(ROOT/'docs/MKN_AGRARIANS_CODE.md').write_text('\n'.join(out),encoding='utf-8')
print('Written docs/MKN_AGRARIANS_CODE.md')
