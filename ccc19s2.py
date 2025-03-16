def smallp(n):
    for i in [2, 3, 5, 7, 11, 13]:
        if i == n:
            return True
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
    for a in [2, 3, 5]:
        if a >= n:
            return True
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

for i in range(int(input())):
    n = int(input()) * 2
    k = 3
    while 1:
        if smallp(k):
            if smallp(n - k):
                if miller(k):
                    if miller(n - k):
                        print(k, n - k)
                        break
        k += 1