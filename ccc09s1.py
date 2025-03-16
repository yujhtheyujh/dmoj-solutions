a = int(input())
b = int(input())
i = 0
s = 0
while 1:
    if a <= i ** 6 <= b:
        s += 1
    elif i ** 6 > b:
        break
    i += 1
print(s)