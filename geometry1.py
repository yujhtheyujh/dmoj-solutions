def main():
    for _ in range(int(input())):
        a, b, c, d, e, f = map(int, input().split())
        A = ((a - c) ** 2 + (b - d) ** 2) ** 0.5
        B = ((c - e) ** 2 + (d - f) ** 2) ** 0.5
        C = ((e - a) ** 2 + (b - f) ** 2) ** 0.5
        P = A + B + C
        S = P / 2
        X = (S * (S - A) * (S - B) * (S - C)) ** 0.5
        print(X, P)
main()