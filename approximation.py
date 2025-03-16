from math import isqrt, pi
for _ in [0] * int(input()):
    n = int(input())
    if n <= 200:
        s = 0
        for i in range(1, n):
            s += isqrt(n ** 2 - i ** 2)
        print(s)
    else:
        print(pi / 4 * n ** 2 - n)