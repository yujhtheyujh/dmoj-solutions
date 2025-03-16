def main():
	k = list(map(int, input().split()))
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))
	o = []
	o0 = 0
	e = []
	e0 = 0
	so = 0
	se = 0
	for i in range(k[0]):
		if not i % 2:
			if a[i] != 0 or b[i] != 0:
				if a[i] != 0 and b[i] != 0:
					if so == 0:
						so = a[i] + b[i]
					else:
						if a[i] + b[i] != so: print(0); return
				else:
					o.append(a[i] if a[i] else b[i])
			else: o0 += 1
		else:
			if a[i] != 0 or b[i] != 0:
				if a[i] != 0 and b[i] != 0:
					if se == 0:
						se = a[i] + b[i]
					else:
						if a[i] + b[i] != se: print(0); return
				else:
					e.append(a[i] if a[i] else b[i])
			else: e0 += 1
	c = 0
	if so:
		if so <= k[1]:
			c += pow(so - 1, o0, 1000000007)
		else:
			c += pow(2 * k[1] - so + 1, o0, 1000000007)
		if len(o) >= 1:
			if max(o) + 1 > so: print(0); return
			if min(o) + k[1] < so: print(0); return
	if not so:
		if len(o) >= 1: d = max(o); f = min(o)
		else: d = 1; f = k[1]
		if d > k[1]: print(0); return
		for i in range(d + 1, f + k[1] + 1):
			if i - 1 <= k[1]:
				c += pow(i - 1, o0, 1000000007)
			else:
				c += pow(2 * k[1] - i + 1, o0, 1000000007)
	ppp = 0
	if se:
		if se <= k[1]:
			ppp += pow(se - 1, e0, 1000000007)
		else:
			ppp += pow(2 * k[1] - se + 1, e0, 1000000007)
		if len(e) >= 1:
			if max(e) + 1 > se: print(0); return
			if min(e) + k[1] < se: print(0); return
	if not se:
		if len(e) >= 1: d = max(e); f = min(e)
		else: d = 1; f = k[1]
		if d > k[1]: print(0); return
		for i in range(d + 1, f + k[1] + 1):
			if i - 1 <= k[1]:
				ppp += pow(i - 1, e0, 1000000007)
			else:
				ppp += pow(2 * k[1] - i + 1, e0, 1000000007)
	print((c * ppp) % 1000000007)
	return
	
main()