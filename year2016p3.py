n = int(input())
l = list(map(int, input().split()))
l.sort()
d = {}
m = 0
for i in l:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
for i in range(1, n - 1):
    for j in range(i):
        if l[i] == l[j]:
            if d[l[i]] >= 3:
                m = l[i]
            break
        if 2 * l[i] - l[j] in d:
            m = l[i]
            break
print(m * 3)