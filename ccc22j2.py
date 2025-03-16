k = 0
n = int(input())
for i in range(n):
    if int(input()) * 5 -int(input()) * 3 > 40:
        k += 1
if k >= n:
    print(str(k) + "+")
else:
    print(k)