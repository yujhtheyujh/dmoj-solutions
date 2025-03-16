import sys
input = sys.stdin.readline
print = sys.stdout.write
def main():
    n = int(input())
    l1 = [*map(int, input().split())]
    l2 = [*map(int, input().split())]
    star = [set() for _ in range(n + 1)]
    dest = [set() for _ in range(n + 1)]
    for i in range(n):
        if l1[i] != l2[i]:
            star[l1[i]].add(i)
            dest[l2[i]].add(i)
    coun = 0
    ous = ""
    for i in range(n + 1):
        for _ in range(len(star[i])):
            a = star[i].pop()
            b = dest[i].pop()
            # print(i, a, b)
            ous += str(a + 1) + " " + str(b + 1) + "\n"
            coun += 1
            destnum = l1[b]
            if l2[a] == destnum:
                star[destnum].remove(b)
                dest[destnum].remove(a)
            else:
                star[destnum].remove(b)
                star[destnum].add(a)
            l1[a], l1[b] = destnum, l1[a]
    print(str(coun) + "\n")
    print(ous)
main()