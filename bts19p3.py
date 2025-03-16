n = int(input())
k = int(input())
i = 0
while 1:
    if (2 ** i) ** k >= n:
        print(i)
        break
    i += 1