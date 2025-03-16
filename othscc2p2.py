a = int(input())
b = int(input())
c = 1
for i in range(b):
    if a <= int(input()):
        print("fight")
        c = 0
        break
if c:
    print("run away")