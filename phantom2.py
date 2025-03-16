import math
l = bytearray(1000001)
for i in range(2, 1000001):
    l[i] = 1
for i in range(2, 1000001):
    if l[i]:
        for j in range(i * i, 1000001, i):
            l[j] = 0
for _ in [0] * int(input()):
    a, b = map(int, input().split())
    print(sum(l[a:b]))