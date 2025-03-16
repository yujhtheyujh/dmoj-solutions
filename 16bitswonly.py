for _ in [0] * int(input()):
    a, b, c = map(int, input().split())
    print(["16 BIT S/W ONLY", "POSSIBLE DOUBLE SIGMA"][a * b == c])