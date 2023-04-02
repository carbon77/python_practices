from pract4.fortik.kernel import LIB, OP_NAMES


class VM:
    def __init__(self, code):
        self.stack = []
        self.code = []
        self.scope = {
            'main': {
                'type': 'func',
                'called_by': None,
                'scope': {}
            }
        }
        self.current_call = 'main'
        self.entry = code[0]

        for byte in code[1:]:
            op = OP_NAMES[byte % 8]
            arg = byte >> 3
            self.code.append((op, arg))

    def run(self, pc=-1):
        if pc == -1:
            pc = self.entry

        while True:
            op, arg = self.code[pc]

            if op == 'push':
                self.stack.append(arg)

            elif op == 'op':
                lib_op = list(LIB.keys())[arg]

                if lib_op in ['+', '-', '/', '*', '%', '&', '|']:
                    arg1 = self.stack.pop()
                    arg2 = self.stack.pop()
                    self.stack.append(LIB[lib_op](arg1, arg2))
                elif lib_op == '.' or lib_op == 'emit':
                    LIB[lib_op](self.stack.pop())
                elif lib_op == 'if':
                    call = LIB[lib_op](arg)

            elif op == 'is':
                self.scope[arg] = {
                    'type': 'func',
                    'called_by': None,
                    'scope': {}
                }

            elif op == 'call':
                scope = self.scope[arg]

                if scope['type'] == 'func':
                    value = arg
                    scope['called_by'] = self.current_call
                    self.current_call = value
                    self.run(value)

                elif scope['type'] == 'var':
                    value = scope['value']
                    func = scope['func']
                    call = self.current_call

                    while call is not None and func != call:
                        call = self.scope[call]['called_by']

                    if call is None:
                        raise ValueError('This variable doesn\'t exist in this scope')

                    self.stack.append(value)

            elif op == 'to':
                value = self.stack.pop()
                self.scope[self.current_call]['scope'] = {
                    'type': 'var',
                    'value': value
                }

            elif op == 'exit':
                self.current_call = self.scope[self.current_call]['called_by']
                break

            pc += 1
