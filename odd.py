def main():
    import sys
    m = 0
    sys.stdin.readline()
    for i in sys.stdin:
        m ^= int(i)
    print(m)
main()