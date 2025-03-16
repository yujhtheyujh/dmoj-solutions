for _ in [0] * int(input()):
    n = int(input())
    l = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            l.append(i)
            n //= i
        i += 1
    if n > 1:
        l.append(n)
    print(*l)