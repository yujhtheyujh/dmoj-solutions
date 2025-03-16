from math import isqrt
while 1:
    n = int(input())
    if n == 0:
        break
    i = isqrt(n)
    while 1:
        if n % i == 0:
            break
        i -= 1
    print(f"Minimum perimeter is {i + n // i << 1} with dimensions {i} x {n // i}")