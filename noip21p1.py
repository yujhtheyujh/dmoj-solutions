import sys
input = sys.stdin.readline
print = sys.stdout.write
l = [0] + [1] * (10 ** 7 + 1)
for i in range(7, 10 ** 7 + 2):
    if '7' in str(i):
        for j in range(i, 10 ** 7 + 2, i):
            l[j] = 0
l2 = l[:]
for i in range(10 ** 7, 0, -1):
    if l[i] == 1:
        l2[i - 1] = i
    else:
        l2[i - 1] = l2[i]
for i in range(int(input())):
    n = int(input())
    if l[n] == 0:
        print("-1\n")
    else:
        print(str(l2[n])+"\n")