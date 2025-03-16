i = 1
n = int(input())
while 1:
    if i * (i + 1) // 2 >= n >= i * (i - 1) // 2 + 1:
        print((i * (i + 1) // 2 + i * (i - 1) // 2 + 1) * (i * (i + 1) // 2 - i * (i - 1) // 2) // 2)
        break
    i += 1