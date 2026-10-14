"""Audit game directories and compare byte-identical multiplayer mod inputs.

This SHA-256 manifest is a diagnostic, not the four-character HOI4 checksum.
Usage: python tools/validate_repository_layout.py --manifest /tmp/nww-client.json
       python tools/validate_repository_layout.py --compare /tmp/other-client.json
"""
import argparse
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
GAME_DIRECTORIES = ('common', 'events', 'history', 'map')


def audit(root):
    errors = []
    files = {}
    folded = {}
    for directory in GAME_DIRECTORIES:
        for path in sorted((root / directory).rglob('*')):
            if not path.is_file():
                continue
            relative = path.relative_to(root).as_posix()
            if path.suffix.lower() in ('.py', '.pyc', '.pyo', '.svg', '.tmp', '.bak', '.log') or path.name.lower() in ('.ds_store', 'thumbs.db', 'desktop.ini') or '__pycache__' in path.parts:
                errors.append(f'{relative}: tool, cache or temporary file in game data')
            if directory in ('common', 'events', 'history') and path.suffix.lower() == '.png':
                errors.append(f'{relative}: preview image in a script directory')
            collision = folded.get(relative.casefold())
            if collision and collision != relative:
                errors.append(f'Case-sensitive filename collision: {collision}, {relative}')
            folded[relative.casefold()] = relative
            files[relative] = hashlib.sha256(path.read_bytes()).hexdigest()
    canonical = json.dumps(files, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode('utf-8')
    return errors, {'schema': 1, 'directories': list(GAME_DIRECTORIES),
                    'sha256': hashlib.sha256(canonical).hexdigest(), 'files': files}


def validate_layout(root, check):
    errors, manifest = audit(root)
    for error in errors:
        check(False, error)
    if not errors:
        print(f'PASS: repository layout: {len(manifest["files"])} game files; no tools, previews, caches or case collisions in game data')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest', type=Path, help='Write hashes to this file outside game data')
    parser.add_argument('--compare', type=Path, help='Compare against a manifest from the other client')
    args = parser.parse_args()
    errors, manifest = audit(ROOT)
    if args.manifest:
        destination = args.manifest.resolve()
        if any(destination.is_relative_to(ROOT / folder) for folder in GAME_DIRECTORIES):
            parser.error('Write the manifest in tools/, docs/ or outside the mod, not in a game directory')
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    if args.compare:
        other = json.loads(args.compare.read_text(encoding='utf-8'))
        if other.get('schema') != 1 or other.get('directories') != list(GAME_DIRECTORIES):
            parser.error('Incompatible manifest schema or directory selection')
        other_files = other['files']
        for path in sorted(manifest['files'].keys() | other_files.keys()):
            if path not in manifest['files']:
                errors.append(f'{path}: present only on the other client')
            elif path not in other_files:
                errors.append(f'{path}: present only on this client')
            elif manifest['files'][path] != other_files[path]:
                errors.append(f'{path}: content differs between clients')
    for error in errors:
        print('ERROR:', error)
    if errors:
        return 1
    print(f'PASS: {len(manifest["files"])} game files; SHA-256 {manifest["sha256"]}')
    if args.compare:
        print('PASS: all compared mod game files are byte-identical')
    return 0


if __name__ == '__main__':
    sys.exit(main())
