x, y, z = map(int, input().split())
num = int(input())
mi = 1434143414341434
for i in range(num):
    x1, y1, z1 = map(int, input().split())
    a = 0
    x1 -= x
    y1 -= y
    z1 -= z
    if z1 <= 0:
        a += abs(z1)
        a += (x1 ** 2 + y1 ** 2) ** 0.5 / 2
    else:
        d = (x1 ** 2 + y1 ** 2) ** 0.5
        t = z1 / 4
        if t * 3 > d:
            a = t
        else:
            a = t + (d - t * 3) / 2
    mi = min(mi, a)
print(mi)