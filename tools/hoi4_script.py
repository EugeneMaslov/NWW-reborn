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


def focus_registry(directory):
    """Collect only direct focus/shared_focus definitions, never nested IDs."""
    registry = {}
    for path in Path(directory).glob('*.txt'):
        doc = read(path)
        nodes = values(doc, 'shared_focus')
        nodes += [f for tree in values(doc, 'focus_tree') for f in values(tree, 'focus')]
        for node in nodes:
            registry[one(node, 'id')] = node
    return registry


def tree_focuses(tree, directory):
    """Expand imported shared roots and their shared-focus descendants."""
    direct = list(values(tree, 'focus'))
    registry = {}
    for path in Path(directory).glob('*.txt'):
        for node in values(read(path), 'shared_focus'):
            registry[one(node, 'id')] = node
    imported = set(values(tree, 'shared_focus'))
    missing = imported - registry.keys()
    if missing:
        raise ValueError('Undefined shared focus imports: ' + ', '.join(sorted(missing)))
    while True:
        children = {fid for fid, node in registry.items() if fid not in imported
                    and any(set(values(group, 'focus')) & imported for group in values(node, 'prerequisite'))}
        if not children:
            break
        imported |= children
    present = {one(node, 'id') for node in direct}
    return direct + [node for fid, node in registry.items() if fid in imported and fid not in present]


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
