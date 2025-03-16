for i in range(int(input())):
    n = int(input())
    c = 1
    j = 2
    while j * j <= n:
        k = 1
        while n % j == 0:
            n //= j
            k += 1
        c *= (2 * k - 1)
        j += 1
    if n - 1:
        c *= 3
    print(c)