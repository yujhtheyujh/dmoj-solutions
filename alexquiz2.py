import sys
input = sys.stdin.readline
list = [0, 0] + [1] * 99999
for i in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313]:
    for j in range (i * i, 100001, i):
        list[j] = 0
for i in range (2, 100001):
    if list[i]:
        list[i] = i + list[i - 1]
    else:
        list[i] = list[i - 1]
for _ in range(int(input())):
    a = input().split()
    b, c = int(a[0]), int(a[1])
    sys.stdout.write(str(list[c] - list[b - 1]) + "\n")