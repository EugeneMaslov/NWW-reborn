"""Export full Revkom file blocks and precise insertions into shared files."""
from pathlib import Path
from hoi4_script import read, one, values
from export_mkn_industrial_focuses import script
from validate_mkn_communists import FOCUSES


ROOT=Path(__file__).resolve().parents[1]
fs={one(f,'id'):f for f in values(one(read(ROOT/'common/national_focus/MKN.txt'),'focus_tree'),'focus')}
out=['# MKN: готовые блоки файлов Ревкома', '',
     'Код уже внесён в проект. Все новые бонусы и штрафы ×2; фактор ТНП ×3 от исходного задания '
     '(+5% → +15%). По уточнению пользователя организация снижается у всех вражеских войск на нашей земле. '
     'Механики, баланс, аудит остальных территориальных штрафов и образцы DLC: '
     '[MKN_communists.md](MKN_communists.md).', '',
     '## common/national_focus/MKN.txt', '',
     'Добавить внутрь существующего `focus_tree`. Прежние определения сохраняются. У комиссаров и танковых '
     'корпусов второй межветочный допуск размещён в `available`, чтобы не проводить лишние линии.', '',
     '```pdx',script([('focus',fs[fid],'=') for fid in FOCUSES]),'```','']
files=['common/ideas/MKN_communist_ideas.txt',
       'common/scripted_triggers/MKN_communist_triggers.txt',
       'common/dynamic_modifiers/MKN_communist_modifiers.txt',
       'common/scripted_effects/MKN_communist_effects.txt',
       'common/on_actions/MKN_communist_on_actions.txt']
for file in files:
    out+=['## '+file,'','Новый файл целиком.','','```pdx',(ROOT/file).read_text().rstrip(),'```','']
out+=['## common/scripted_effects/nww_mkn_progression.txt — экономика','','В конце существующего '
      '`nww_mkn_rebuild_industry` оставить прежние пересчёты и добавить вызов Ревкома. Конец блока:', '',
      '```pdx','MKN_rebuild_militarist_industry_stats = yes','MKN_rebuild_soviet_industry_stats = yes',
      'MKN_rebuild_communist_industry_stats = yes','set_country_flag = MKN_industry_integration_v4','```','',
      '## common/scripted_effects/nww_mkn_progression.txt — армия','','В начале существующего '
      '`nww_mkn_rebuild_services`, после миграции штаба, добавить обнуление новой переменной:', '',
      '```pdx','set_variable = { MKN_army_army_armor_speed_factor = 0 }','```','',
      'В конце этого же эффекта оставить прежние пересчёты и добавить новый:', '',
      '```pdx','MKN_rebuild_horizons_service_stats = yes','MKN_rebuild_militarist_army_stats = yes',
      'MKN_rebuild_soviet_army_stats = yes','MKN_rebuild_communist_army_stats = yes','```','',
      'Остальные условия, сбросы и награды существующих эффектов сохранить; это вставки, '
      'а не дополнительные одноимённые определения.', '',
      '## common/dynamic_modifiers/nww_dynamic_modifiers.txt', '',
      'Внутри прежнего `MKN_army_development`, рядом с танковой атакой, добавить:', '',
      '```pdx','army_armor_speed_factor = MKN_army_army_armor_speed_factor','```','']
for lang in ('russian','english'):
    file=f'localisation/{lang}/MKN_communist_l_{lang}.yml'
    out+=['## '+file,'','Новый файл целиком, UTF-8 с BOM.','','```yaml',
          (ROOT/file).read_text(encoding='utf-8-sig').rstrip(),'```','']
file='interface/MKN_communist_focus_icons.gfx'
out+=['## '+file,'','Новый файл целиком. Текстуры, источники и точные промпты находятся в '
      '[манифесте](art/mkn_communist_expansion/assets.json).','','```pdx',
      (ROOT/file).read_text().rstrip(),'```','',
      '[Предпросмотр 12 иконок](mkn_communist_expansion_preview_2x.png).','',
      '## Проверка','','```sh',
      "python tools/validate_country_content.py --game '/home/dima00138/.local/share/Steam/steamapps/common/Hearts of Iron IV'",
      'git diff --check','```','',
      'Новая кампания и runtime-проверка боёв/подсказок не проводились.','']
(ROOT/'docs/MKN_COMMUNISTS_CODE.md').write_text('\n'.join(out),encoding='utf-8')
print('Written docs/MKN_COMMUNISTS_CODE.md')
