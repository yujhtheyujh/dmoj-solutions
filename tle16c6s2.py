from fractions import Fraction
import sys
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

y = lambda x: -Fraction(y1, x1) * x + 2 * y1
if y(x2) >= y2:
    print(2 * x1 * y1)
    sys.exit()

y = lambda x: -Fraction(y2, x2) * x + 2 * y2
if y(x1) >= y1:
    print(2 * x2 * y2)
    sys.exit()

print(float((Fraction(x1, x2 - x1) * (y1 - y2) + y1) * (Fraction(y2, y1 - y2) * (x2 - x1) + x2) / 2))