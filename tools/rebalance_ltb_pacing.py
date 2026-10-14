"""Set half the LTB tree to 70 days and report the minimum full recovery route."""
import json
from datetime import date, timedelta
from pathlib import Path
from hoi4_script import read, one, values, dump

ROOT = Path(__file__).resolve().parents[1]
LONG = '''
LTB_rebuild_the_bridge LTB_union_general_staff LTB_agricultural_mechanization
LTB_cooperative_farms LTB_rural_electrification LTB_depression_recovery
LTB_factory_reconstruction LTB_union_industrial_plan LTB_union_mining_program
LTB_the_minsk_school LTB_timoshenkos_doctrine LTB_officers_of_two_nations
LTB_fortress_vitebsk LTB_cavalry_inspectorate LTB_border_guard_corps
LTB_motorized_reserves LTB_mogilev_artillery_school LTB_joint_maneuvers
LTB_professional_contract_army LTB_national_resilience
LTB_minsk_arsenal_works LTB_armaments_plant LTB_military_contracts
LTB_minsk_machine_works LTB_precision_engineering LTB_belmash_tank_program
LTB_timoshenko_industrial_board LTB_french_machine_tools
LTB_vilnius_university LTB_union_research_council LTB_minsk_university
LTB_rocket_research LTB_peaceful_atom
LTB_minsk_aircraft_works LTB_fighter_command LTB_army_air_support
LTB_multinational_air_program
LTB_memel_shipyards LTB_baltic_escort_program LTB_coastal_defense_network
'''.split()
path = ROOT / 'common/national_focus/ltb_focus.txt'
doc = read(path)
tree = one(doc, 'focus_tree')
focuses = {one(f, 'id'): f for f in values(tree, 'focus')}
for fid in LONG:
    f = focuses[fid]
    f[:] = [(k, '10' if k == 'cost' else v, o) for k, v, o in f]
long_count = sum(one(f, 'cost') == '10' for f in focuses.values())
assert long_count == 48 and len(focuses) == 96, (long_count, len(focuses))
path.write_text(dump(doc) + '\n', encoding='utf-8', newline='\n')
# These recovery paths contain only single-parent or AND prerequisites.
required = set()
def visit(fid):
    if fid in required:
        return
    required.add(fid)
    for group in values(focuses[fid], 'prerequisite'):
        parents = values(group, 'focus')
        assert len(parents) == 1, (fid, parents)
        visit(parents[0])
for fid in ['LTB_the_vilnius_compromise', 'LTB_union_general_staff',
            'LTB_factory_reconstruction', 'LTB_union_industrial_plan']:
    visit(fid)
duration = sum(int(one(focuses[f], 'cost')) * 7 for f in required)
report = {
    'total_focuses': len(focuses), 'seventy_day_focuses': long_count,
    'seventy_day_ids': sorted(fid for fid, f in focuses.items() if one(f, 'cost') == '10'),
    'full_starting_debuff_recovery_ids': sorted(required),
    'minimum_focus_days': duration,
    'earliest_uninterrupted_date': str(date(1936, 1, 1) + timedelta(days=duration)),
    'assumptions': 'One active focus; no console/autocomplete; starting map and spirits; no focus pauses or unrelated development. Crisis focus bypasses after compromise.'
}
(ROOT / 'docs/LTB_pacing.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
print(f'LTB: {long_count}/96 focuses take70days; full recovery {duration}focusdays, earliest {report["earliest_uninterrupted_date"]}.')
