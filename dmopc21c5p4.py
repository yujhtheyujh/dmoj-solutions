def main():
    lp = [False, False] + [True] * 10 ** 6
    for i in range (2, len(lp)):
        if lp[i]:
            for j in range(i * i, len(lp), i):
                lp[j] = False
    lp[2] = False
    ps = [i for i in range(len(lp))if lp[i]]
    def f(p, n, q = 2):
        if p < q:
            p, q = q, p
        l = []
        t = 1
        s = [1]
        for i in range(p + q - 1):
            if t + q <= p + q:
                t += q
            else:
                t -= p
            s.append(t)
        for i in range(n):
            l += [j + i * (p + 2) for j in s]
        return l
    for _ in range(int(input())):
        t = False
        n = int(input())
        if n == 1:
            print(1)
            continue
        if n <= 3:
            print(-1)
            continue
        for i in range(4, n + 3):
            if n % i == 0 and lp[i - 2]:
                print(*f(i - 2, n // i))
                t = True
                break
            if (n + 1) % i == 0 and lp[i - 2]:
                print(*[j - 1 for j in f(i - 2, (n + 1) // i)[1:]])
                t = True
                break
            if (n - 1) % i == 0 and lp[i - 2]:
                print(*f(i - 2, (n - 1) // i), n)
                t = True
                break
        if t: continue
        for p in ps:
            if lp[n - p]:
                print(*f(n - p, 1, p))
                break
            if lp[n - p + 1]:
                print(*[j - 1 for j in f(n - p + 1, 1, p)[1:]])
                break
main()