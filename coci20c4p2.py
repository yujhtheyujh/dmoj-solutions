l = [1] * 10 ** 7
PRIMES = []
for i in range(2, 10 ** 7):
    if l[i]:
        PRIMES.append(i)
        for j in range(i * i, 10 ** 7, i):
            l[j] = 0
def f(n, p):
    s = 0
    while n:
        n //= p
        s += n
    return s

for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    a -= 1
    c -= 1
    div = True
    for p in PRIMES:
        if p > max(b, d):
            break
        if f(d, p) - f(c, p) < f(b, p) - f(a, p):
            div = False
            break
    if div:
        print("DA")
    else:
        print("NE")