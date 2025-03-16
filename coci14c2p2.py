d = {}
a = int(input())
a *= 2
a -= 1
i = 0
while i < a:
    n = input()
    try:
        d[n] ^= 1
    except:
        d[n] = 1
    i += 1
for i in d:
    if d[i] == 1:
        print(i)
        break