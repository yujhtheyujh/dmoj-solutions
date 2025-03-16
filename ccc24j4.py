def main():
    a, b = input(), input()
    if len(a) == len(b):
        for i in "abcdefghijklmnopqrstuvwxyz":
            if i in a and i not in b:
                print(i, b[a.index(i)])
                print("-")
                return
        print("-")
        print("-")
        return
    k = []
    for i in "abcdefghijklmnopqrstuvwxyz":
        if i in a and i not in b:
            k.append(i)
    if len(k) == 1:
        print("-")
        print(k[0])
        return
    for j in "abcdefghijklmnopqrstuvwxyz":
        c = "".join(i if i not in k else (
            "" if i == k[0] else j) for i in list(a))
        if c == b:
            print(k[1], j)
            print(k[0])
            return
    for j in "abcdefghijklmnopqrstuvwxyz":
        c = "".join(i if i not in k else (
            "" if i == k[1] else j) for i in list(a))
        if c == b:
            print(k[0], j)
            print(k[1])
            return
main()