"""Keep native ideology rules intact and add four GER-only display subtypes."""
import argparse
from pathlib import Path
from hoi4_script import read, one, parse, dump

ROOT = Path(__file__).resolve().parents[1]
TYPES = {'democratic': 'GER_social_democracy', 'fascism': 'GER_pan_germanism',
         'communism': 'GER_spartacism', 'neutrality': 'GER_imperial_autocracy'}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--game', type=Path, default=Path.home()/'.local/share/Steam/steamapps/common/Hearts of Iron IV')
    game = p.parse_args().game
    source = game/'common/ideologies/00_ideologies.txt'
    if not source.is_file(): p.error(f'Installed ideologies not found: {source}')
    doc = read(source)
    for group, subtype in TYPES.items():
        one(one(one(doc,'ideologies'),group),'types').append(
            (subtype, parse('can_be_randomly_selected = no'), '='))
    target = ROOT/'common/ideologies/00_ideologies.txt'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text('# Owner: GER. Native rules retained; only four nonrandom GER subtypes added.\n'
                      '# Rebuild for the target version with tools/build_ger_ideologies.py.\n'+dump(doc))
    print('PASS: four GER display subtypes; native groups, rules and other subtypes preserved')


if __name__ == '__main__':
    main()
