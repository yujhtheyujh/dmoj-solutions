def log2(n):
    return len(bin(n)) - 3

N, T = map(int, input().split())
s = [*map(int, [*input()])]

while T:
    e = 1 << log2(T)
    T -= e
    stemp = s[:]
    for i in range(N):
        stemp[i] = s[(i + e) % N] ^ s[(i - e) % N]
    s = stemp[:]

print("".join(map(str, s)))