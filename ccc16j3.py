n = input()
m = 1
for i in range(len(n)):
    a = 1
    for j in range(1, i + 1):
        if i - j < 0 or i + j > len(n) - 1:
            break
        if n[i + j] != n[i - j]:
            break
        a += 2
    if a > m:
        m = a
    a = 0
    for j in range(i + 1):
        if i - j < 0 or i + j > len(n) - 2:
            break
        if n[i + j + 1] != n[i - j]:
            break
        a += 2
    if a > m:
        m = a
print(m)