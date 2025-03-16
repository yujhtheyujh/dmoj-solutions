def f(n):
    if n == 1: return 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i - 1 + f(n - n // i)
    return n - 1 + f(n - 1)
print(f(int(input())))