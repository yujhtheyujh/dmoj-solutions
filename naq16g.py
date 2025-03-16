from math import log
import sys
sys.set_int_max_str_digits(0)
n = int(input())
if n == 2: print(2)
elif n == 6: print(3)
else:
    n = log(n)
    s = 0
    i = 1
    while 1:
        s += log(i)
        if -0.5 <= s - n <= 0.5:
            print(i)
            break
        i += 1