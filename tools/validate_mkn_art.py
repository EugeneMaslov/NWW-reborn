"""Check MKN painted sources, native exports and the historical flag lifecycle."""
import argparse
import hashlib
import json
from pathlib import Path

from PIL import Image
from hoi4_script import one, read, values, walk, engine_script_errors, focus_registry

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--game', type=Path, required=True)
    args = parser.parse_args()
    spec = json.loads((ROOT / 'docs/art/MKN_hoi4_art.json').read_text())
    assert len(spec['assets']) == 29 and len(spec['flags']) == 5
    exported_hashes = set()
    focuses = focus_registry(ROOT / 'common/national_focus')
    sprites = {}
    for filename in ('interface/MKN_overhaul_icons.gfx', 'interface/MKN_overhaul_shine.gfx', 'interface/ideas.gfx'):
        for key, node, _ in walk(read(ROOT / filename)):
            if key and key.lower() == 'spritetype':
                sprites[one(node, 'name')] = node
    for asset in spec['assets']:
        assert one(focuses[asset['focus']], 'icon') == asset['sprite'], asset['focus']
        source, texture = ROOT / asset['source'], ROOT / asset['texture']
        assert source.is_file() and (ROOT / asset['prompt']).is_file(), asset['key']
        assert hashlib.sha256(source.read_bytes()).hexdigest() == asset['source_sha256'], asset['key']
        with Image.open(source) as image:
            assert min(image.size) >= 512 and image.convert('RGBA').getchannel('A').getextrema()[0] == 0
        with Image.open(texture) as image:
            assert image.size == (96, 96) and image.format == 'DDS'
            bounds = image.convert('RGBA').getchannel('A').getbbox()
            assert bounds and min(bounds[:2]) >= 6 and max(bounds[2:]) <= 90, (asset['key'], bounds)
        digest = hashlib.sha256(texture.read_bytes()).hexdigest()
        assert digest not in exported_hashes, 'Duplicate painted texture: ' + asset['key']
        exported_hashes.add(digest)
        for suffix in ('', '_shine'):
            assert one(sprites[asset['sprite'] + suffix], 'texturefile') == asset['texture']
    for asset in spec['flags']:
        assert (ROOT / asset['source']).is_file() and (ROOT / asset['prompt']).is_file()
    for directory, size in (('', (82, 52)), ('medium', (41, 26)), ('small', (10, 7))):
        root = ROOT / 'gfx/flags' / directory
        historical = Image.open(root / 'MKN_batko.tga').convert('RGB')
        hashes = set()
        for party in ('fascism', 'democratic', 'neutrality', 'communism'):
            with Image.open(root / ('MKN_' + party + '.tga')) as image:
                assert image.size == size and image.mode == 'RGBA'
                assert image.getchannel('A').getextrema() == (255, 255)
                assert image.convert('RGB').getextrema() != ((0, 0),) * 3, party
                hashes.add(hashlib.sha256(image.tobytes()).hexdigest())
            with Image.open(root / ('MKN_batko_' + party + '.tga')) as image:
                assert image.size == size and image.convert('RGB').tobytes() == historical.tobytes()
        assert len(hashes) == 4, 'Successor flags are not distinct'

    effect = one(read(ROOT / 'common/scripted_effects/MKN_flag_effects.txt'), 'MKN_update_national_flag')
    def test(nodes, state):
        result = []
        for k, v, _ in nodes:
            if k == 'NOT': answer = not test(v, state)
            elif k == 'OR': answer = any(test([x], state) for x in v)
            elif k == 'original_tag': answer = state['origin'] == v
            elif k == 'has_country_flag': answer = v in state['flags']
            elif k == 'has_cosmetic_tag': answer = state['cosmetic'] == v
            else: raise AssertionError(k)
            result.append(answer)
        return all(result)
    def apply(state):
        for key, node, _ in effect:
            if test(one(node, 'limit'), state):
                for k, v, _ in node:
                    if k == 'set_cosmetic_tag': state['cosmetic'] = v
                    elif k == 'drop_cosmetic_tag': state['cosmetic'] = None
                break
    for origin in ('MKN', 'UKR'):
        for departed in (False, True):
            for rebel in (False, True):
                for cosmetic in (None, 'MKN_batko', 'MKN_cw_neutrality'):
                    flags = ({'mkn_batko_departed'} if departed else set()) | ({'MKN_duel_participant'} if rebel else set())
                    state = dict(origin=origin, flags=flags, cosmetic=cosmetic)
                    apply(state)
                    expected = (cosmetic if origin != 'MKN' else ('MKN_batko' if not departed and not rebel else (None if cosmetic == 'MKN_batko' else cosmetic)))
                    assert state['cosmetic'] == expected, state
                    again = dict(state)
                    apply(state)
                    assert state == again, 'Daily flag maintenance is not idempotent'
    history = read(ROOT / 'history/countries/MKN - Makhnovists.txt')
    assert one(history, 'set_cosmetic_tag') == 'MKN_batko'
    funeral = next(e for e in values(read(ROOT / 'events/MKN_events.txt'), 'country_event') if one(e, 'id') == 'mkn_crisis.1')
    assert one(one(funeral, 'immediate'), 'MKN_update_national_flag') == 'yes'
    for filename in ('common/scripted_effects/MKN_flag_effects.txt', 'common/on_actions/MKN_flag_on_actions.txt'):
        assert not list(engine_script_errors(read(ROOT / filename)))
    # The requested filename override retains every native idea sprite.
    original = read(args.game / 'interface/ideas.gfx')
    assert read(ROOT / 'interface/ideas.gfx')[:len(original)] == original
    print('PASS: 29 distinct painted focus/idea exports, 5 flag masters, 48 flag-lifecycle scenarios, all native sizes/alpha and original idea sprites')


if __name__ == '__main__':
    main()
