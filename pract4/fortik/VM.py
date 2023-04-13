from pract4.fortik.kernel import LIB, OP_NAMES


class VM:
    def __init__(self, code):
        self.stack = []
        self.code = []
        self.scope = {
            '__parent__': None
        }
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
                    '__parent__': self.scope
                }

            elif op == 'call':
                env = self.scope
                called = env.get(arg)

                while called is None and env['__parent__'] is not None:
                    env = env.get('__parent__')
                    called = env.get(arg)

                if called is None:
                    raise ValueError("Name does not exist")

                if type(called) is dict:
                    self.scope = called
                    self.run(arg)
                else:
                    self.stack.append(called)

            elif op == 'to':
                value = self.stack.pop()
                self.scope[arg] = value

            elif op == 'exit':
                if self.scope['__parent__'] is not None:
                    self.scope = self.scope.get('__parent__')
                break

            pc += 1
