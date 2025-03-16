import sys
print = lambda n: sys.stdout.write(n + "\n")
l = [2 ** i for i in range(64)]
for _ in range(int(input())):print(str(int(input())in l)[0])