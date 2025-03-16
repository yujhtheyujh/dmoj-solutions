A = int(input())
B = int(input())
l = [0] * (B + 1)
for i in range(2, B + 1):
    if l[i] == 0:
        for j in range(i, B + 1, i):
            l[j] += 1
for i in range(A, B + 1):
    print(l[i])