R,C,M=[int(input())for _ in '000']
o=[0]*C
s=0
for _ in range(R):
    l = [s % M + 1 + min(o[0], o[1])]
    l+=[(i + s) % M + 1 + min(o[i - 1], o[i], o[i + 1])for i in range(1, C - 1)]
    l.append((C - 1 + s) % M + 1 + min(o[-1], o[-2]))
    s=(C - 1 + s) % M + 1
    o=l
print(min(o))