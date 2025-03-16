N, K = map(int, input().split())
l = bytearray(N + 1)
for i in range(2, N + 1):
    l[i] = 1
for i in range(2, N + 1):
    if l[i]:
        for j in range(i * i, N + 1, i):
            l[j] = 0
if K == 1:
    print(sum(l))
elif K == 2:
    s = 0
    for i in range(4, N + 1):
        if i % 2 == 0:
            s += 1
        else:
            if l[i] == 0 and l[i - 2] == 1:
                s += 1
    print(s)
elif K == 3:
    s = 0
    for i in range(9, N + 1, 2):
        if l[i] == 0 and l[i - 2] == 0:
            s += 1
    print(s)
else:
    print(0)