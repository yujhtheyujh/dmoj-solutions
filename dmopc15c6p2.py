from decimal import *
s = 0
for _ in [0] * int(input()):
    s += Decimal(input())
    s %= 360
print(s)