from fractions import *
import sys
sys.set_int_max_str_digits(0)

def powf(b, a, m = 1000000007):
    if a == 1:
        return b
    c = powf(b, a // 2, m)
    if a % 2 == 0:
        return [(c[0] ** 2 + 5 * c[1] ** 2) % m, (2 * c[0] * c[1]) % m]
    d = [(c[0] ** 2 + 5 * c[1] ** 2) % m, (2 * c[0] * c[1]) % m]
    return [(d[0] * b[0] + 5 * d[1] * b[1]) % m, (d[0] * b[1] + d[1] * b[0]) % m]
if (n := (int(input()) % 2000000016))  == 0:
    print(0)
else:
    print(powf([Fraction(1, 2), Fraction(1, 2)], n)[1] * 2 % 1000000007)