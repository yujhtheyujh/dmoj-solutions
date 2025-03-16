N, D, K, X = map(int, input().split())
l = []
for _ in [0] * N:
    l.append(int(input()))
P = int(input())
for i in range(N):
    while l[i] >= P:
        l[i] *= 100 - X
        l[i] //= 100
        K -= 1
    if K < 0:
        print("NO")
        import sys
        sys.exit()
print("YES")