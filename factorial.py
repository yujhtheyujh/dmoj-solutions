import math
a = int(input())
for i in range (a):
    n = int(input())
    if n == 0: print(1)
    elif n < 3: print(n)
    elif n > 33: print(0)
    else: print(math.factorial(n) % 4294967296)