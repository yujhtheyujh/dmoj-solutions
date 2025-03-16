a, b = map(int, input().split())
l = []
for i in range(a):
    l.append((int(input()) * 244002641) % 2 ** 32)
l.sort()
print(sum(l[-b:]))