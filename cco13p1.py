import math

def ispalim(aa, bb):
    ll = []
    while aa:
        ll.append(aa % bb)
        aa //= bb
    for i in range(len(ll)):
        if ll[i] != ll[-i - 1]:
            return False
    return True

n = int(input())
b = []

i = 1
while 1:
    a = (n - i) // i
    if a <= i:
        break
    if a * i + i == n:
        b.append(a)
    i += 1

i = math.isqrt(n)
while i > 1:
    if ispalim(n, i):
        b.append(i)
    i -= 1
b = b[::-1]
for i in b:
    print(i)