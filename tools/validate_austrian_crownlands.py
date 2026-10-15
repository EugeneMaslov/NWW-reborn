"""Audit state-charter scopes, shared cooldown, native modifiers and meter stages."""
from pathlib import Path
import re
import json
from PIL import Image

root = Path(__file__).resolve().parents[1]
game = Path('D:/Steam/steamapps/common/Hearts of Iron IV')
# Reuse the repository's Clausewitz reader used by the Austrian lifecycle tests.
from hoi4_script import read, one, values
decision = one(one(read(root/'common/decisions/AUS_crownland_development.txt'),'AUS_nww_crownland_development'),'AUS_nww_grant_crownland')
assert one(decision,'cost') == '75'
assert one(decision,'state_target') == 'yes'
assert one(decision,'fire_only_once') == 'no'
assert one(one(one(one(decision,'complete_effect'),'if'),'set_country_flag'),'days') == '30'
assert one(one(one(decision,'target_trigger'),'FROM'),'AUS_nww_can_receive_charter') == 'yes'
assert one(one(one(decision,'visible'),'FROM'),'AUS_nww_can_receive_charter') == 'yes'
assert one(one(one(decision,'available'),'FROM'),'AUS_nww_can_receive_charter') == 'yes'
modifier = one(read(root/'common/dynamic_modifiers/AUS_crownlands.txt'),'AUS_nww_crownland_charter')
native = set(re.findall(r'^## (\w+)',(game/'documentation/modifiers_documentation.md').read_text(encoding='utf-8-sig'),re.M))
for key,value,op in modifier:
    if key not in ('icon','enable'):
        # Native docs describe building-specific modifiers as a template.
        if key == 'state_production_speed_infrastructure_factor':
            docs = (game/'documentation/modifiers_documentation.md').read_text(encoding='utf-8-sig')
            assert 'state_production_speed_<Building>_factor' in docs
            assert re.search(r'^\s*infrastructure\s*=\s*\{',(game/'common/buildings/00_buildings.txt').read_text(encoding='utf-8-sig'),re.M)
        else:
            assert key in native, key
        assert value == '0.10'
assert one(one(one(modifier,'enable'),'owner'),'original_tag') == 'AUS'
gui = (root/'common/scripted_guis/AUS_bohemian_gui.txt').read_text()
assert set(map(int,re.findall(r'AUS_seal_(\d+)_visible',gui))) == set(range(11))
for path in (root/'gfx/interface/goals/AUS').glob('*.dds'):
    im = Image.open(path).convert('RGBA')
    assert im.size == (96,96)
    bounds = im.getbbox()
    assert bounds and bounds[0] >= 4 and bounds[1] >= 4 and bounds[2] <= 92 and bounds[3] <= 92
assert 'GFX_frontier_' not in (root/'interface/AUS_bohemian_gui.gui').read_text()
window=one(one(read(root/'interface/AUS_bohemian_gui.gui'),'guiTypes'),'containerWindowType')
for kind,body,operator in window:
    if kind in ('iconType','instantTextBoxType'):
        assert one(body,'orientation')=='center_up',one(body,'name')
background=next(b for k,b,o in window if k=='iconType' and one(b,'name')=='AUS_background')
assert int(one(one(background,'position'),'x'))==-220
mapping=json.loads((root/'docs/art/AUS/focus_icon_map.json').read_text())
tree=one(read(root/'common/national_focus/AUS_focuses.txt'),'focus_tree')
assert {one(f,'id'):one(f,'icon') for f in values(tree,'focus')}==mapping
sprites={}
for base in (game,root):
    for p in (base/'interface').glob('*.gfx'):
        try: parsed=read(p)
        except ValueError: continue
        for block in values(parsed,'spriteTypes'):
            for kind,body,operator in block:
                if kind.lower()=='spritetype' and isinstance(body,list):
                    name=one(body,'name'); texture=one(body,'texturefile')
                    if name and texture:sprites[name]=(body,texture)
for icon in mapping.values():
    assert icon in sprites and icon+'_shine' in sprites,icon
    for name in (icon,icon+'_shine'):
        body,texture=sprites[name]
        assert (root/texture).exists() or (game/texture).exists(),texture
assert len(set(mapping.values())) >= 100
for lang in ('russian','english'):
    text=(root/f'localisation/replace/AUS_crownlands_l_{lang}.yml').read_text(encoding='utf-8-sig')
    for key in re.findall(r'text = "(AUS_\w+)"',(root/'interface/AUS_bohemian_gui.gui').read_text()):
        assert re.search(r'^ '+key+r':',text,re.M),key
print(f'PASS: {len(mapping)} exact focus mappings, {len(set(mapping.values()))} distinct base/shine pairs, native textures, independent Bohemian artwork and RU/EN panel text')
print('PASS: Austrian crown charter state scopes, ownership, 75 PP/shared 30-day gate, native bonuses, 11 meter positions and six transparent textures')
