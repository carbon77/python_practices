def main(z, x):
    n = len(z)
    s = 0

    for i in range(1, n + 1):
        s += (47 + 94 * z[n - i] + x[n - i] ** 2) ** 3 / 17

    return 46 * s


print(main([0.78, 0.29], [0.56, -0.35]))
print(main([-0.11, -0.27], [-0.19, -0.25]))
print(main([-0.42, -0.12], [0.5, -0.43]))
print(main([-0.15, 0.88], [-0.56, 0.1]))
print(main([0.41, -0.86], [0.93, 0.73]))
