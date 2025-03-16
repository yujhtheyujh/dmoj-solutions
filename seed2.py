l = 1
r = 2 * 10 ** 9
while 1:
    m = l + r >> 1
    print(m)
    a = input()
    if a == "OK":
        break
    if a == "SINKS":
        l = m + 1
    if a == "FLOATS":
        r = m - 1