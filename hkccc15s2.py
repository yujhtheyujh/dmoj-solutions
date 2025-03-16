import math
n, m = map(int, input().split())
s = input()
t = input()
g = math.gcd(len(s), len(t))
list1 = [[0] * g for _ in range(26)]
list2 = [[0] * g for _ in range(26)]
for i in range(len(s)):
    list1[ord(s[i]) - 97][i % g] += 1
for i in range(len(t)):
    list2[ord(t[i]) - 97][i % g] += 1
su = 0
for i in range(g):
    for j in range(26):
        su += list1[j][i] * list2[j][i]
print(su * n * len(s) // math.lcm(len(s), len(t)))