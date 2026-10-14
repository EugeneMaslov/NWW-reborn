"""Adapt two native runtime systems which spammed the 1.19.3 NWW error log."""
import copy,re
from pathlib import Path
from hoi4_script import read,one,walk,parse,dump
ROOT=Path(__file__).resolve().parents[1]
GAME=Path('D:/Steam/steamapps/common/Hearts of Iron IV')
source=read(GAME/'common/scripted_effects/operation_strat_effects.txt')
operations=sorted({v.removeprefix('token:') for k,v,o in walk(source) if k=='operation_types' and isinstance(v,str) and v.startswith('token:')})
registered={k for p in (GAME/'common/operations').glob('*.txt') for k,v,o in read(p) if isinstance(v,list)}
assert set(operations)<=registered
def operation_checks(doc):
    result=[]
    for k,v,o in doc:
        if k in ('is_preparing_operation','num_finished_operations') and isinstance(v,list) and one(v,'operation','').startswith('var:'):
            variable=one(v,'operation').removeprefix('var:')
            choices=[]
            for operation in operations:
                literal=copy.deepcopy(v)
                literal[:]=[(key,operation if key=='operation' else value,op) for key,value,op in literal]
                choices.append(('AND',parse(f'check_variable = {{ var = {variable} value = token:{operation} }}')+[(k,literal,o)],'='))
            result.append(('OR',choices,'='))
        else:
            if isinstance(v,list):v=operation_checks(v)
            result.append((k,v,o))
    return result
adapted=operation_checks(source)
# Reuse vanilla selection/scoring and current operation tokens. Only dynamic operation checks change.
path=ROOT/'common/scripted_effects/operation_strat_effects.txt'
path.write_text('# NWW 1.19.3 compatibility: compare selected tokens, then check literal registered operation IDs.\n'+dump(adapted)+'\n',encoding='utf-8')

# The NWW Soviet tree has no NSB purge path. Prevent its detached native purge system
# from selecting unregistered advisor ideas or purging characters without a playable resolution.
effects_path=ROOT/'common/scripted_effects/SOV_effects.txt'
effects=read(effects_path) if effects_path.exists() else []
effects[:]=[(k,v,o) for k,v,o in effects if k!='nww_SOV_suspend_detached_purges']
effects.extend(parse('''nww_SOV_suspend_detached_purges = {
clr_country_flag = SOV_paranoia_system_active_flag
clr_country_flag = SOV_paranoia_modifier_active_flag
set_variable = { SOV_paranoia = 0 }
set_variable = { SOV_paranoia_weekly_bucket = 0 }
set_variable = { SOV_paranoia_modifier_increase = 0 }
}'''))
effects_path.write_text(dump(effects)+'\n',encoding='utf-8')
doc=parse('''on_actions = {
on_startup = { effect = { SOV = { if = { limit = { has_focus_tree = SOV_focus } nww_SOV_suspend_detached_purges = yes } } } }
on_daily_SOV = { effect = { if = { limit = { has_focus_tree = SOV_focus OR = { has_country_flag = SOV_paranoia_system_active_flag has_country_flag = SOV_paranoia_modifier_active_flag } } nww_SOV_suspend_detached_purges = yes } } }
}''')
(ROOT/'common/on_actions/SOV_on_actions.txt').write_text(dump(doc)+'\n',encoding='utf-8')
print('Native espionage checks use literal operation IDs; native NSB purges run only outside the custom NWW Soviet tree.')
