import math
N, M, c, d = map(int, input().split())
c -= 1
sum = 0
if N <= 2:
    p = 2
    cc = c // p + 1
    dd = d // p
    sum += (dd + cc) * (dd - cc + 1)
    sum %= 2016420
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
l = sieve(math.isqrt(M) + 3)
if N % 2 == 0:
    N += 1
en = M - N + 1
li = [1] * en
for i in l:
    if i < N:
        for j in range((-N) % i, en, i):
            li[j] = 0
    else:
        for j in range((-N) % i + i, en, i):
            li[j] = 0
for i in range(0, en, 2):
    if li[i]:
        p = i + N
        cc = c // p + 1
        dd = d // p
        sum += (dd + cc) * (dd - cc + 1) // 2 * p
        sum %= 2016420
print(sum % 2016420)