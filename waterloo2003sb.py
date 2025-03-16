while 1:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        print(10)
    elif n == 1:
        print(11)
    else:
        s = ""
        for i in range(9, 1, -1):
            while n % i == 0:
                s += str(i)
                n //= i
        if n == 1:
            if len(s) == 1:
                print('1' + s)
            else:
                print(s[::-1])
        else:
            print("There is no such number.")