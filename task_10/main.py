class MealyError(Exception):
    def __init__(self, method_name):
        self.method_name = method_name


class MealyJump:
    def __init__(self, function: str, return_value: int, next_state):
        self.function = function
        self.return_value = return_value
        self.next_state = next_state


class MealyState:
    def __init__(self, value: str, jumps: list[MealyJump] = None):
        self.value = value
        self.jumps = jumps if jumps else []


class Mealy:
    states = {
        'A': MealyState('A'),
        'B': MealyState('B'),
        'C': MealyState('C'),
        'D': MealyState('D'),
        'E': MealyState('E'),
        'F': MealyState('F'),
        'G': MealyState('G'),
    }

    def __init__(self):
        self.state = self.states['A']

        self.states['A'].jumps = [
            MealyJump('pan', 0, self.states['B']),
            MealyJump('base', 1, self.states['G']),
        ]

        self.states['B'].jumps = [
            MealyJump('pan', 3, self.states['B']),
            MealyJump('base', 2, self.states['C']),
        ]

        self.states['C'].jumps = [
            MealyJump('pan', 4, self.states['D']),
        ]

        self.states['D'].jumps = [
            MealyJump('get', 6, self.states['A']),
            MealyJump('base', 5, self.states['E']),
        ]

        self.states['E'].jumps = [
            MealyJump('get', 7, self.states['F']),
        ]

        self.states['F'].jumps = [
            MealyJump('pan', 9, self.states['D']),
            MealyJump('get', 8, self.states['G']),
        ]

    def template_method(self, method_name):
        for jump in self.state.jumps:
            if jump.function == method_name:
                self.state = jump.next_state
                return jump.return_value

        raise MealyError(method_name)

    def pan(self):
        return self.template_method('pan')

    def get(self):
        return self.template_method('get')

    def base(self):
        return self.template_method('base')


class MealyTest:
    def test_1(self):
        """Test 1"""
        o = main()
        self.assert_equal(o.pan(), 0)
        self.assert_equal(o.pan(), 3)
        self.assert_equal(o.base(), 2)
        self.assert_equal(o.pan(), 4)
        self.assert_equal(o.get(), 6)
        self.assert_equal(o.base(), 1)
        try:
            o.base()
        except MealyError as e:
            self.assert_equal(e.method_name, 'base')

        try:
            o.pan()
        except MealyError as e:
            self.assert_equal(e.method_name, 'pan')

        try:
            o.get()
        except MealyError as e:
            self.assert_equal(e.method_name, 'get')

    def test_2(self):
        """Test 2"""
        o = main()
        self.assert_equal(o.pan(), 0)
        self.assert_equal(o.base(), 2)
        self.assert_equal(o.pan(), 4)
        self.assert_equal(o.base(), 5)
        self.assert_equal(o.get(), 7)
        self.assert_equal(o.pan(), 9)
        o.base()
        o.get()
        self.assert_equal(o.get(), 8)
        self.assert_equal(o.state.value, 'G')

    @staticmethod
    def assert_equal(arg1, arg2):
        assert arg1 == arg2


def main():
    return Mealy()


def test():
    mealy_test = MealyTest()
    mealy_test.test_1()
    mealy_test.test_2()


if __name__ == '__main__':
    test()
