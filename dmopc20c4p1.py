for _ in range(int(input())):
    N, S = map(int, input().split())
    X = N * (N + 1) // 2 - S
    ma = min(N, X - 1)
    mi = max(1, X - N)
    print(ma - mi + 1>> 1)