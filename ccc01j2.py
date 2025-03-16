import math
a = int(input())
b = int(input())
if a == 1: print(1)
elif a + 1 == b: print(a)
elif math.gcd(a, b) != 1: print("No such integer exists.")
else:
    for i in range(1, b):
        if i * a % b == 1:
            print(i)
            break