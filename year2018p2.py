from math import isqrt
input()
s = 0
for i in map(int, input().split()):
    temp = 1
    if i == 1:
        continue
    for j in range(2, isqrt(i) + 1):
        if i % j == 0:
            temp = 0
    s += temp
print(s)