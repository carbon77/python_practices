from math import cos


def main(b, a):
    result = 0
    for k in range(1, a + 1):
        for j in range(1, b + 1):
            result += (cos(28 * j ** 3 - 11)) / 64 + \
                      55 * (50 * k ** 3 - 29) ** 4
    return result


print(main(3, 4))
print(main(7, 4))
print(main(2, 6))
print(main(2, 3))
print(main(7, 2))
