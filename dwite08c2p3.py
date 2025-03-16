def sa(a, b, c):
    return a * b + b * c + c * a << 1
def main():
    for _ in[0]*5:
        n = int(input())
        m = sa(n, 1, 1)
        i = 2
        while i * i <= n:
            if n % i == 0:
                t = n // i
                j = 1
                while j * j <= t:
                    if t % j == 0:
                        m = min(sa(i, j, t // j), m)
                    j += 1
                j = 1
                while j * j <= i:
                    if i % j == 0:
                        m = min(sa(t, j, i // j), m)
                    j += 1
            i += 1
        print(m)
main()