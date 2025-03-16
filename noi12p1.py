def f(b, p, m):
    if p == 1:
        return 1
    if p % 2 == 0:
        return (f(b, p // 2, m) * (pow(b, p // 2, m) + 1)) % m
    return (f(b, p - 1, m) * b + 1) % m
m, a, c, x0, n, g = map(int, input().split())
s = pow(a, n, m) * x0
s += f(a, n, m) * c
s %= m
print(s % g)