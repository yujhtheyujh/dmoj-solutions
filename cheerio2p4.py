A, B, C, D = map(int, input().split())
e = C - D
l = []
from math import isqrt
for i in range(1, isqrt(e) + 1):
    if e % i == 0:
        if C % i == D and A % i == B:
            l.append(i)
        if i * i != e:
            j = e // i
            if C % j == D and A % j == B:
                l.append(j)
l.sort()
for i in l:
    print(i)