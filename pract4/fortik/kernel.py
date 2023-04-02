import operator as op

OP_NAMES = {0: 'push', 1: 'op', 2: 'call', 3: 'is', 4: 'to', 5: 'exit'}


def not_implemented(vm):
    raise RuntimeError('Not implemented!')


LIB = {
    '+': op.add,
    '-': op.sub,
    '*': op.mul,
    '/': op.truediv,
    '%': op.mod,
    '&': op.and_,
    '|': op.or_,
    '^': op.not_,
    '<': lambda a, b: a < b,
    '>': lambda a, b: a > b,
    '=': op.eq,
    '<<': op.lshift,
    '>>': op.rshift,
    'if': lambda val, yes, no: yes if val else no,
    'for': not_implemented,
    '.': print,
    'emit': lambda x: print(chr(x), end=''),
    '?': not_implemented,
    'array': not_implemented,
    '@': not_implemented,
    '!': not_implemented
}
