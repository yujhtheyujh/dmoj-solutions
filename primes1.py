l = [1] * 20001
n = int(input())
for i in range(2, 20001):
    if l[i]:
        print(i)
        n -= 1
        if n == 0:
            break
        for j in range(i * i, 20001, i):
            l[j] = 0