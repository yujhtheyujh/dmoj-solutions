n = int(input())
c = 0
if n <= 5:
    print([0, 1, 3, 5, 8, 10][n])
else:
    t = n
    l, r = 1, n
    for i in range(1, int(n ** (1 / 2)) - 1):
        a = n // i
        c += a
        l += 1
        t, a = a, t - a
        r -= a
        c += a * (i - 1)
    for i in range(l, r + 1):
        c += n // i
    print(c)