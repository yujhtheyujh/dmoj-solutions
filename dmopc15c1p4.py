N, X = map(int, input().split())
l = [1] * (N + 1)
p = []
s = 0
for i in range(2, N + 1):
    if l[i]:
        s += (N - i) // X + 1
        if N - i - 1 >= 0:
            s += (N - i - 1) // X + 1
        for j in range(i * i, N + 1, i):
            l[j] = 0
print(s)