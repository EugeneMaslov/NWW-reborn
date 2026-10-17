"""Small Clausewitz reader for content checks (preserves duplicate keys)."""
import re
from pathlib import Path

TOKEN = re.compile(r'\s+|#[^\n]*|"(?:\\.|[^"\\])*"|[{}]|[=<>!]=?|[^\s{}=<>!#"]+')


def scalar(token):
    """Remove the outer quote pair only; preserve escaped interior quotes."""
    return token[1:-1] if token.startswith('"') and token.endswith('"') else token


def quoted(value):
    """Quote a raw script string without escaping existing escapes a second time."""
    value = re.sub(r'(\\*)"', lambda m: m[1] + ('\\' if len(m[1]) % 2 == 0 else '') + '"', value)
    trailing = len(value) - len(value.rstrip('\\'))
    if trailing % 2:
        value += '\\'
    return '"' + value + '"'


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
                result.append((scalar(key), value if isinstance(value, list) else scalar(value), op))
            else:
                result.append((None, scalar(key), None))
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


def variable_check(node):
    """Read the engine's named or single-operator check_variable syntax."""
    comparisons = {
        'equals': '=', 'not_equals': '!=', 'less_than': '<',
        'less_than_or_equals': '<=', 'greater_than': '>',
        'greater_than_or_equals': '>=',
    }
    if one(node, 'var') is not None:
        var, value = one(node, 'var'), one(node, 'value')
        compare = one(node, 'compare', 'equals')
        if value is None or compare not in comparisons:
            raise ValueError('Invalid named check_variable comparison')
        return var, value, comparisons[compare]
    operands = [entry for entry in node if entry[0] != 'tooltip']
    if len(operands) != 1 or operands[0][2] not in ('=', '<', '>'):
        raise ValueError('check_variable shorthand requires =, < or >; use named compare for inclusive comparisons')
    return operands[0]


def engine_script_errors(node, parents=()):
    """Catch native loader errors a permissive Clausewitz reader can miss."""
    for key, value, op in node:
        context = '/'.join((*parents, str(key)))
        if op not in (None, '=', '<', '>'):
            yield f'{context}: unsupported raw operator {op}; use a named variable comparison'
        if key == 'exists' and value not in ('yes', 'no'):
            yield f'{context}: exists requires yes/no in country scope'
        if key == 'num_owned_states' and (not parents or parents[-1] != 'check_variable'):
            yield f'{context}: num_owned_states is a dynamic variable, not a native trigger'
        if key == 'political_power' and (not parents or parents[-1] not in ('check_variable', 'set_variable', 'set_temp_variable')):
            yield f'{context}: political_power is not a trigger; use has_political_power'
        if key == 'modifier_army_sub_unit_motorized_attack_factor':
            yield f'{context}: unregistered motorized modifier; use motorized_attack_factor'
        if key in ('add_relation_rule_override','remove_relation_rule_override') and isinstance(value,list) and one(value,'can_not_declare_war') is not None:
            yield f'{context}: HOI4 1.19.3 rejects declaration bans as relation overrides; use country rules and AI strategies'
        if key == 'equipment' and isinstance(value,list) and isinstance(one(value,'civilian_factories'),str):
            yield f'{context}: operation civilian_factories needs an amount/days block'
        if key == 'check_variable' and isinstance(value, list):
            try:
                variable_check(value)
            except ValueError as exc:
                yield f'{context}: {exc}'
        if key == 'strength_ratio' and isinstance(value, list):
            target = one(value, 'tag', '')
            if isinstance(target, str) and target.startswith('PREV.'):
                yield f'{context}: avoid chained country targets in army comparisons; enter an existing country and use a single PREV'
        if key == 'target_trigger' and isinstance(value, list):
            state_only = {'is_owned_by', 'is_controlled_by', 'is_owned_and_controlled_by', 'any_neighbor_state'}
            for name, operand, operator in value:
                if name in state_only:
                    yield f'{context}/{name}: target_trigger is country scope; enter the target state through FROM'
        if isinstance(value, list):
            yield from engine_script_errors(value, (*parents, str(key)))


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
            if isinstance(value, list):
                lines.append(prefix + '{')
                lines.append(dump(value, depth + 1))
                lines.append(prefix + '}')
            else:
                if not value or any(c.isspace() for c in value) or any(c in value for c in '/"\\'):
                    value = quoted(value)
                lines.append(prefix + value)
        elif isinstance(value, list):
            lines.append(f'{prefix}{key} {op} {{')
            lines.append(dump(value, depth + 1))
            lines.append(prefix + '}')
        else:
            if re.fullmatch(r'-?\.\d+', value):
                value = '-0' + value[1:] if value.startswith('-') else '0' + value
            if not value or any(c.isspace() for c in value) or any(c in value for c in '/"\\'):
                value = quoted(value)
            lines.append(f'{prefix}{key} {op} {value}')
    return '\n'.join(lines)
