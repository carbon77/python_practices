from pract4.expressions.literal import Add, Num, Mul
from pract4.expressions.visitor import PrintVisitor, CalcVisitor, StackVisitor


if __name__ == '__main__':
    ast = Add(Num(7), Mul(Num(3), Num(2)))
    pv = PrintVisitor()
    print(pv.visit(ast))

    cv = CalcVisitor()
    print(cv.visit(ast))

    sv = StackVisitor()
    print(sv.visit(ast))

