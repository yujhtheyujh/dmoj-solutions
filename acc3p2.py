def f(m1, m2, l1, l2):
    s = 0
    for i in range(len(l1)):
        s += max(abs(l1[i] - m1), abs(l2[i] - m2))
    return s
n = int(input())
l1 = []
l2 = []
l3 = []
l4 = []
for i in range(n):
    a, b = map(int, input().split())
    l1.append(a)
    l2.append(b)
    l3.append(a + b)
    l4.append(a - b)
l3.sort()
l4.sort()
m1 = l3[n - 1 >> 1]
m2 = l4[n - 1 >> 1]
a, b = m1, m2
if (m1 + m2) % 2 == 0:
    print(f(m1 + m2 >> 1, m1 - m2 >> 1, l1, l2))
else:
    print(min(
        f(m1 + m2 >> 1, m1 - m2 >> 1, l1, l2),
        f(m1 + m2 + 1>> 1, m1 - m2 >> 1, l1, l2),
        f(m1 + m2 >> 1, m1 - m2 + 1>> 1, l1, l2),
        f(m1 + m2 + 1>> 1, m1 - m2 + 1>> 1, l1, l2)
    ))