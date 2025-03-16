ll = [int(input()) for _ in range(int(input()))]
l = [ll[i] - ll[i + 1] for i in range(len(ll) - 1)]
import math, functools
lll = []
lll.append(n := abs(functools.reduce(math.gcd, l)))
for i in range(2, math.isqrt(n - 1) + 1):
    if n % i == 0:
        lll.append(i)
        lll.append(n // i)
if math.isqrt(n) ** 2 == n:
    lll.append(math.isqrt(n))
print(' '.join(map(str, lll)))