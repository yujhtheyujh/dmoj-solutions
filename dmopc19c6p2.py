def fac(n):
    d = {}
    i = 2
    while i * i <= n:
        if n % i == 0:
            n //= i
            d[i] = 1
            while n % i == 0:
                n //= i
                d[i] += 1
        i += 1
    if n > 1:
        d[n] = 1
    return d
def f(n, p):
    m = 0
    while n:
        n //= p
        m += n
    return m

a, b = map(int, input().split())
m = b
dd = fac(a)
for i in dd:
    t = f(b, i) // dd[i]
    if t <= m:
        m = t
print(m)