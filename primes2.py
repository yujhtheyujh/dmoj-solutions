import math
N, M = map(int, input().split())
if N <= 2:
    print(2)
    N = 3
def sieve(n):
    l = [False, False, True] + [True, False] * (n - 1 >> 1)
    r = []
    for i in range(3, n + 1, 2):
        if l[i]:
            r.append(i)
            for j in range(i * i, n + 1, 2 * i):
                l[j] = False
    return r
l = sieve(math.isqrt(M))
if N % 2 == 0:
    N += 1
en = M - N + 1
li = bytearray(en)
for i in range(en):
    li[i] = 1
for i in l:
    if i < N:
        for j in range((-N) % i, en, i):
            li[j] = 0
    else:
        for j in range((-N) % i + i, en, i):
            li[j] = 0
for i in range(0, en, 2):
    if li[i]:
        print(i + N)