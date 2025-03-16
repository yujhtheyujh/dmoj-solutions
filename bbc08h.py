n = int(input())
MOD = 1000000007
t = 1
for i in range(2, n + 1):
    t *= i
    t %= MOD
t1 = t
t *= n + 1
t %= MOD
t2 = t
for i in range(n + 2, 2 * n + 2):
    t *= i
    t %= MOD
t3 = t
t3 *= 2
t3 *= pow(t1, MOD - 2, MOD)
t3 *= pow(t2, MOD - 2, MOD)
t3 -= 1
print(t3 % MOD)