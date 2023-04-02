from math import cos, atan, log


def main(y):
    if y < 42:
        return (cos(28 - 11 * y ** 3) ** 7) / 64
    elif y < 104:
        return y ** 7
    elif y < 195:
        return 31 * y - 88 * y ** 4
    elif y < 226:
        return log(y) ** 6 - y ** 7
    return log(y) ** 4 + (atan(1 + y ** 3 + 48 * y)) / 92 + y ** 3


print(main(295))
print(main(24))
print(main(116))
print(main(258))
print(main(243))
