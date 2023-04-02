from pract4.expressions.interface import IPrintable, ICalculable, IStackable


class PrintVisitor:
    def visit(self, ast: IPrintable) -> str:
        return ast.print()


class CalcVisitor:
    def visit(self, ast: ICalculable) -> int:
        return ast.calculate()


class StackVisitor:
    def visit(self, ast: IStackable) -> str:
        return ast.stack()
