def main():
    from math import isqrt
    for _ in range(int(input())):
        n = int(input())
        nu = 2
        up = 2
        do = 1
        l = {(n, 1), (n, n - 1)}
        if n >= 6:
            a = isqrt(2 * n) + 1
            if a * (a - 1) // 2 == n:
                l.add((a, 2))
                l.add((a, a - 2))
        while 1:
            if nu > n:
                break
            up += 1
            nu *= up
            up += 1
            nu *= up
            do += 1
            nu //= do ** 2
        nu *= do ** 2
        do -= 1
        nu //= up
        up -= 1
        nu //= up
        up -= 1
        while 1:
            if do <= 2:
                break
            if nu < n:
                up += 1
                nu *= up
                nu //= up - do
                continue
            if nu > n:
                nu *= do
                do -= 1
                nu //= up - do
                continue
            if nu == n:
                l.add((up, do))
                l.add((up, up - do))
                nu *= do
                do -= 1
                nu //= up - do
        l = list(l)
        l.sort()
        for i in range(len(l)):
            l[i] = f"({l[i][0]},{l[i][1]})"
        print(len(l))
        print(" ".join(l))
main()