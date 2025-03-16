# cursed no sieve solution
import sys
input = sys.stdin.readline
print = sys.stdout.write

def e(n):
    global l
    k = n - 1
    if l[k]:
        print(str(l[k])+"\n")
        return
    i, c, q = 2, 0, 1
    while True:
        if i * i > n:
            q *= n ** 2 + 1 if n - 1 else 1
            print(str(q)+"\n")
            l[k] = q
            return
        while n % i == 0:
            c += 2
            n //= i
        if c:
            q *= i ** (c + 2) // (i ** 2 - 1)
            c = 0
        i += 1
def main():
    for i in range(int(input())):
        e(int(input()))
l = [0] * 100000
main()