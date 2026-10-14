"""Repair concrete startup errors observed in the 2026-10-14 NWW game log."""
import copy
from pathlib import Path
from hoi4_script import read,one,values,walk,parse,dump
ROOT=Path(__file__).resolve().parents[1]
GAME=Path('D:/Steam/steamapps/common/Hearts of Iron IV')
def save(p,doc):
    p=ROOT/p;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(dump(doc)+'\n',encoding='utf-8')
def setv(doc,k,v):
    doc[:]=[(key,value,o) for key,value,o in doc if key!=k];doc.append((k,v,'='))

# Croatia owns its core in Zadar: initializing occupation resistance is invalid.
p='history/states/163-Dalmatia.txt';doc=read(ROOT/p);state=one(doc,'state');history=one(state,'history')
history[:]=[(k,v,o) for k,v,o in history if k not in ('start_resistance','set_compliance')];save(p,doc)

# A legacy auto-generated leader competed with the recruited modern Lastouski character.
p='history/countries/BYE - Belarus.txt';doc=read(ROOT/p)
doc[:]=[(k,v,o) for k,v,o in doc if k!='create_country_leader'];save(p,doc)
p='common/characters/nww_BYE.txt';doc=read(ROOT/p)
node=one(one(doc,'characters'),'NWW_BYE_vaclaus_lastouski')
if not values(node,'country_leader'):node.extend(parse('country_leader = { ideology = oligarchism expire = "1965.1.1" }'))
save(p,doc)

# Imperial Germany cannot use Nazi-only division naming groups.
names=read(GAME/'common/units/names_divisions/GER_names_divisions.txt');result=[]
for new,old in [('GER_NWW_Arm_01','GER_Arm_01_ANTIFASCIST'),('GER_NWW_MOT_01','GER_MOT_02')]:
    node=copy.deepcopy(one(names,old));setv(node,'can_use',parse('always = yes'));result.append((new,node,'='))
save('common/units/names_divisions/GER_nww_names.txt',result)
p='history/units/GER_1936_nsb.txt';doc=read(ROOT/p)
for node in values(doc,'division_template'):
    group=one(node,'division_names_group')
    if group in ('GER_Arm_01','GER_MOT_02'):setv(node,'division_names_group',{'GER_Arm_01':'GER_NWW_Arm_01','GER_MOT_02':'GER_NWW_MOT_01'}[group])
# Medium armour was not unlocked in 1936 and had no variant; retain the existing light-tank lines.
def remove_medium(doc):
    result=[]
    for k,v,o in doc:
        if k=='add_equipment_production' and one(one(v,'equipment',[]),'type')=='medium_tank_chassis_1':continue
        if isinstance(v,list):v=remove_medium(v)
        result.append((k,v,o))
    return result
save(p,remove_medium(doc))

# NWW's additional starting battleships referred to a variant defined only in the 1939 block.
p='history/countries/GER - Germany.txt';doc=read(ROOT/p)
early={one(v,'name') for k,v,o in walk([(k,v,o) for k,v,o in doc if not (k and k[0].isdigit())]) if k=='create_equipment_variant'}
if 'Bismarck' not in early:
    variant=next(copy.deepcopy(v) for k,v,o in walk(doc) if k=='create_equipment_variant' and one(v,'name')=='Bismarck')
    doc.extend([('if',parse('limit = { has_dlc = "Man the Guns" }')+[('create_equipment_variant',variant,'=')],'=')]);save(p,doc)
print('Repaired core resistance, Belarusian leader duplication, imperial division names and German startup equipment references.')
