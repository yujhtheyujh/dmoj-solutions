for _ in [0] * int(input()):
    n = str(bin(int(input())))[2:]
    while len(n) % 4:
        n = '0' + n
    print(" ".join(n[i << 2:i + 1 << 2] for i in range(len(n) // 4)))