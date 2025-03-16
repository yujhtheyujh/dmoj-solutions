import sys
def f(n):
    a = []
    while n:
        a.append(str(n % 3))
        n //= 3
    return a[::-1]
def g(n):
    a = f(n)
    b = False
    for i in range(len(a)):
        if b:
            a[i] = "1"
        elif a[i] == "2":
            b = True
            a[i] = "1"
    return int("".join(a), 2)

for i in range(int(input())):
    a, b = map(int, sys.stdin.readline().split())
    print(g(b) - g(a - 1))