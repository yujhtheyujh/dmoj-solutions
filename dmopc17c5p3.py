input()
n = __import__("functools").reduce(__import__("math").gcd, map(int, input().split()))
if n == 1:
    print("DNE")
else:
    i = 2
    m = 0
    while i * i <= n:
        if n % i == 0:
            while n % i == 0:
                n //= i
        m = i
        i += 1
    if n > 1:
        print(n)
    else:
        print(m)