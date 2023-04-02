from math import sin


def main(y, z, x):
    return x ** 2 - z ** 3 - y - sin(z ** 2 - (x / 47) - 82 * y ** 3) ** 5


print(main(0.23, -0.97, -0.52))
print(main(-0.82, -0.56, 0.37))
print(main(0.96, -0.89, -0.95))
print(main(0.72, -0.29, -0.73))
print(main(0.51, -0.43, -0.89))
