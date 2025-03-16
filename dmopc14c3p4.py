import sys
input = sys.stdin.readline
print = lambda n: sys.stdout.write(str(n) + "\n")
ll = [[0 for _ in range(100001)] for __ in range(129)]
l = [1] * 100001
t = [1] * 100001
for i in range(2, 100001):
    if l[i] == 1:
        for j in range(i, 100001, i):
            t[j] = 1
        j = 1
        while i ** j <= 100000:
            for k in range(i ** j, 100001, i ** j):
                t[k] += 1
            j += 1
        for j in range(i, 100001, i):
            l[j] *= t[j]
l[0] = 0
for i in range(0,100001):
    ll[l[i]][i] = 1
for i in range(129):
    for j in range(1, 100001):
        ll[i][j] += ll[i][j - 1]
for _ in range(int(input())):
    K, A, B = map(int, input().split())
    if K >= 129:
        print(0)
        continue
    print(ll[K][B] - ll[K][A - 1])