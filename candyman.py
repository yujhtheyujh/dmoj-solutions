from math import gcd
import sys
def f(n, b):
    m = 0
    n = str(n)
    for i in n:
        m *= b
        m += int(i)
        if int(i) >= b:
            return 0
    return m

def g(l, ll = [], lll = []):
    lenn = len(ll)
    if lenn == len(l):
        for i in lll:
            print(i)
        sys.exit()
    for i in range(2, 11):
        t = f(l[lenn], i)
        if t != 0:
            cc = True
            for j in ll:
                if gcd(t, j) != 1:
                    cc = False
                    break
            if cc:
                g(l, ll + [t], lll + [i])
    return

input()
g(l = [*map(int, input().split())])