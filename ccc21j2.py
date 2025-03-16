w = ""
m = 0
for i in range(int(input())):
    a = input()
    b = int(input())
    if b > m:
        m = b
        w = a
print(w)