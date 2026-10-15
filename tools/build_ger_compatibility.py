"""Register detached native German focus IDs without importing native mechanics."""
import argparse
from pathlib import Path

from hoi4_script import read, one, values, focus_registry

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--game', type=Path, default=Path.home()/'.local/share/Steam/steamapps/common/Hearts of Iron IV')
    game = parser.parse_args().game
    source = game/'common/national_focus/germany.txt'
    if not source.is_file(): parser.error(f'Installed German tree does not exist: {source}')
    native = read(source)
    # Only direct definitions: event IDs and state/province IDs are never collected.
    nodes = values(native, 'shared_focus') + [f for tree in values(native,'focus_tree') for f in values(tree,'focus')]
    active = focus_registry(ROOT/'common/national_focus')
    for path in (ROOT/'common/national_focus').glob('GER_native_compatibility.txt'):
        for f in values(read(path),'shared_focus'):
            active.pop(one(f,'id'),None)
    ids = sorted({one(node,'id') for node in nodes} - active.keys())
    lines = ['# Owner: GER. Generated from direct definitions in installed common/national_focus/germany.txt.',
             '# tools/build_ger_compatibility.py; these unimported IDs never grant native rewards.']
    for fid in ids:
        lines += ['shared_focus = {', f'\tid = {fid}', '\tcost = 10',
                  '\tallow_branch = { always = no }', '\tavailable = { always = no }',
                  '\tcompletion_reward = {}', '}']
    for tree in values(native,'focus_tree'):
        lines += ['focus_tree = {', f'\tid = {one(tree,"id")}',
                  '\tcountry = { factor = 0 }', '\tdefault = no', '}']
    (ROOT/'common/national_focus/GER_native_compatibility.txt').write_text('\n'.join(lines)+'\n')
    (ROOT/'common/national_focus/germany.txt').write_text(
        '# Owner: GER. Playable tree: GER_focuses.txt and GER_political.txt.\n'
        '# Native IDs: GER_native_compatibility.txt; native politics and economy stay detached.\n')
    print(f'PASS: {len(ids)} direct native GER focus IDs retained as hidden compatibility definitions')


if __name__ == '__main__':
    main()
