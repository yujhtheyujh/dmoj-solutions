from functools import cache
from math import isqrt
@cache
def f(n):
    if n == 1:
        return 0
    ma = 1
    bes = 1
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            a = min(f(i), f(n // i))
            if a > ma:
                ma = a
                bes = i
    return ma + 1
while 1:
    n = int(input())
    if n == 1:
        break
    ma = 1
    bes = 1
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            a = min(f(i), f(n // i))
            if a > ma:
                ma = a
                bes = i
    print(bes, n // bes)