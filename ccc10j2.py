a, b, c, d, s = (int(input()) for _ in range (5))
ap, bp = 0, 0
for i in range(s):
    if i % (a + b) < a:
        ap += 1
    else: ap -= 1
    if i % (c + d) < c:
        bp += 1
    else:
        bp -= 1
if ap > bp:
    print("Nikky")
elif bp > ap:
    print("Byron")
else:
    print("Tied")