import math
for i in range(int(input())):
    a = input().split()
    if a[2] == "0":
        print((a := math.isqrt(int(a[0]))), a)
    else:
        p = math.gcd(int(a[0]), (int(a[2]) + int(a[3])))
        q = int(a[0]) // p
        if p >= q:
            print(q, p)
        else:
            print(p, q)