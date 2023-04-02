from pract4.expressions.interface import IPrintable, ICalculable, IStackable


class Literal(IPrintable, ICalculable, IStackable):
    pass


class BiOperation(Literal):
    def __init__(self, a, b):
        self.a = a
        self.b = b


class Add(BiOperation):
    def print(self):
        return '(' + self.a.print() + ' + ' + self.b.print() + ')'

    def calculate(self):
        return self.a.calculate() + self.b.calculate()

    def stack(self):
        a_stack = self.a.stack()
        b_stack = self.b.stack()

        return a_stack + '\n' + b_stack + '\n' + 'ADD'


class Mul(BiOperation):
    def print(self):
        return '(' + self.a.print() + ' * ' + self.b.print() + ')'

    def calculate(self):
        return self.a.calculate() * self.b.calculate()

    def stack(self):
        a_stack = self.a.stack()
        b_stack = self.b.stack()

        return a_stack + '\n' + b_stack + '\n' + 'MUL'


class Num(Literal):
    def __init__(self, value):
        self.value = value

    def print(self):
        return str(self.value)

    def calculate(self):
        return self.value

    def stack(self):
        return 'PUSH ' + str(self.value)
