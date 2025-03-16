import sys
def smallp(n):
    if n <= 50:
        for i in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]:
            if i == n:
                return True
        return False
    for i in [2, 3, 5, 7, 11, 13, 17, 19, 23]:
        if n % i == 0:
            return False
    return True

def miller(n):
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True
    d = n - 1
    while d % 2 == 0:
        d //= 2
    for a in [2, 13, 17, 23]:
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        while d != n - 1:
            x = (x * x) % n
            d *= 2
            if x == 1:
                return False
            if x == n - 1:
                break
        else:
            return False
    return True

n = int(input())
if n == 1:
    print(2)
    sys.exit()
while 1:
    if smallp(n):
        if miller(n):
            print(n)
            break
    n += 1