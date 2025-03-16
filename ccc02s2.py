import sys
a = int(input())
b = int(input())
if a == 0:
    print(0)
    sys.exit()
from math import gcd
g = gcd(a, b)
a //= g
b //= g
c = a // b
d = a % b
if c == 0:
    print(str(d) + "/" + str(b))
    sys.exit()
if d == 0:
    print(c)
    sys.exit()
print(str(c) + " " + str(d) + "/" + str(b))