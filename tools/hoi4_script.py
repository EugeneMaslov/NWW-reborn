"""Small Clausewitz reader for content checks (preserves duplicate keys)."""
import re
from pathlib import Path

TOKEN = re.compile(r'\s+|#[^\n]*|"(?:\\.|[^"\\])*"|[{}]|[=<>!]=?|[^\s{}=<>!#"]+')


def parse(text):
    tokens = [m.group() for m in TOKEN.finditer(text.lstrip('\ufeff'))
              if not m.group().isspace() and not m.group().startswith('#')]
    pos = 0

    def block(nested=False):
        nonlocal pos
        result = []
        while pos < len(tokens):
            key = tokens[pos]
            pos += 1
            if key == '}':
                if not nested:
                    raise ValueError('Unexpected closing brace')
                return result
            if key == '{':
                result.append((None, block(True), None))
                continue
            if key in ('{', '=', '<', '>'):
                raise ValueError(f'Unexpected token {key}')
            if pos < len(tokens) and tokens[pos] in ('=', '<', '>', '<=', '>=', '!=', '=='):
                op = tokens[pos]
                pos += 1
                if pos >= len(tokens):
                    raise ValueError(f'Missing value for {key}')
                value = tokens[pos]
                pos += 1
                if value == '{':
                    value = block(True)
                result.append((key.strip('"'), value if isinstance(value, list) else value.strip('"'), op))
            else:
                result.append((None, key.strip('"'), None))
        if nested:
            raise ValueError('Unclosed block')
        return result

    return block()


def read(path):
    return parse(Path(path).read_text(encoding='utf-8-sig'))


def values(node, key):
    return [value for name, value, op in node if name == key]


def one(node, key, default=None):
    return next(iter(values(node, key)), default)


def walk(node):
    for key, value, op in node:
        yield key, value, op
        if isinstance(value, list):
            yield from walk(value)


def dump(node, depth=0):
    lines = []
    for key, value, op in node:
        prefix = '\t' * depth
        if key is None:
            if not value or any(c.isspace() for c in value) or '/' in value:
                value = '"' + value.replace('"', '\\"') + '"'
            lines.append(prefix + value)
        elif isinstance(value, list):
            lines.append(f'{prefix}{key} {op} {{')
            lines.append(dump(value, depth + 1))
            lines.append(prefix + '}')
        else:
            if re.fullmatch(r'-?\.\d+', value):
                value = '-0' + value[1:] if value.startswith('-') else '0' + value
            if not value or any(c.isspace() for c in value) or '/' in value:
                value = '"' + value.replace('"', '\\"') + '"'
            lines.append(f'{prefix}{key} {op} {value}')
    return '\n'.join(lines)
