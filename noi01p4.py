def main():
    a = int(input())
    c = a ** 2 + 1
    from math import isqrt
    b = isqrt(c)
    while c % b:
        b -= 1
    print(b + c // b + 2 * a)
main()