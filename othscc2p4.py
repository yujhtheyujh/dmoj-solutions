a = input().split(" ")
n = int(a[0])
m = int(a[1])
q = int(a[2])
e = []
f = []
for i in range(n):
	t = input().split(" ")
	for j in range(m):
		e.append(int(t[j]))
		f.append(i * 10000000000 + j)

d = {e[i]: f[i] for i in range(m * n)}
for i in range(q):
	k = input().split(" ")
	num = int(k[0])
	if num not in d:
		print("no")
	else:
		o = d[num] // 10000000000
		p = d[num] % 10000000000
		if (int(k[1]) <= o + 1 <= int(k[3])) and (int(k[2]) <= p + 1 <= int(k[4])):
			print("yes")
		else:
			print("no")