import sys

N, T = map(int, input().split())
s = [int(sys.stdin.readline()) for i in range(N)]

while T:
    e = 1 << len(bin(T)) - 3
    T -= e
    s = [s[(i + e) % N] ^ s[i] for i in range(N)]

for i in s:
    sys.stdout.write(str(i) + "\n")