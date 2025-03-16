def main():
    from math import factorial as f
    a, b, c, d = map(int, input().split())
    print(f(a) // f(b) // f(c) // f(d) % (10 ** 9 + 7))
main()