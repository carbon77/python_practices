def main(n):
    if n == 0:
        return -0.5
    return (main(n - 1) ** 2 - 9 * main(n - 1) - 1) ** 2 / 49


print(main(8))
print(main(4))
print(main(6))
print(main(3))
print(main(2))
