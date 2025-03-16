def main():
    m, n = map(int, input().split())
    if m > n:
        m, n = n, m
    l = [i for i in range(m + 1)]
    for i in range(2, len(l)):
        if l[i] == i:
            for j in range(i, len(l), i):
                l[j] //= i
                l[j] *= i - 1
    s = 0
    for i in range(2, m + 1):
        s += (m // i) * (n // i) * l[i]
    s *= 2
    s += m * n
    print(s)
main()