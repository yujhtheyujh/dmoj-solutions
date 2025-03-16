import sys
input = sys.stdin.buffer.readline
def main():
    l = [0] * 76
    for i in range(int(input())):
        l[int(input())] += 1
    a = 3
    for i in range(75, -1, -1):
        if l[i]:
            a -= 1
        if not a:
            print(i, l[i])
            break
main()