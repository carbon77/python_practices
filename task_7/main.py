def main(s):
    x = int(s, 16)
    result = []
    sizes = (6, 6, 9, 4, 4, 9)

    for size in sizes[:-1]:
        result.append(str(x & (2 ** size - 1)))
        x >>= size

    result.append(str(x))
    return tuple(result)


print(main('0x6e36824707'))
print(main('0x4181996ba5'))
print(main('0x5ebc936022'))
print(main('0x3ea1981477'))
