from math import isqrt
for _ in range(int(input())):
    a, b = map(int, input().split())
    a, b = min(a, b), max(a, b)
    c = isqrt(a)
    s = c * (c + 1) * (2 * c + 1) // 6 + c + 1
    d = isqrt(b)
    s += (a + 1) * (d - c)
    e = isqrt(a + b)
    s += (e - d) * (a + b + 1)
    s -= e * (e + 1) * (2 * e + 1) // 6 - d * (d + 1) * (2 * d + 1) // 6
    print(s % 998244353)