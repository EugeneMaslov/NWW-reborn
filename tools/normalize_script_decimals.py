"""Normalize bare .5/- .5 style numbers to engine-compatible 0.5/-0.5, preserving comments/text."""
from pathlib import Path
import re
from hoi4_script import TOKEN
ROOT=Path(__file__).resolve().parents[1]
total=0
for folder in ('common','events','history','interface'):
    for p in (ROOT/folder).rglob('*.txt'):
        original=p.read_text(encoding='utf-8-sig')
        spans=[m for m in TOKEN.finditer(original) if re.fullmatch(r'-?\.\d+',m.group())]
        if not spans:continue
        updated=original
        for m in reversed(spans):
            value=m.group();number='-0'+value[1:] if value.startswith('-') else '0'+value
            updated=updated[:m.start()]+number+updated[m.end():]
        if p.read_text(encoding='utf-8-sig')!=original:raise RuntimeError(f'{p}: changed during decimal normalization')
        p.write_text(updated,encoding='utf-8');total+=len(spans)
        print(p.relative_to(ROOT),len(spans))
print('Normalized',total,'bare decimal numbers; no numerical values changed.')
