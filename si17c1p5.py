import sys
sys.setrecursionlimit(1000000)
MOD = 10 ** 9
def matmul(l1, l2):
    l = [[0 for i in range(len(l2[0]))] for j in range(len(l1))]
    for i in range(len(l1)):
        for j in range(len(l2[0])):
            for k in range(len(l2)):
                l[i][j] += l1[i][k] * l2[k][j]
                l[i][j] %= MOD
    return l
def matexp(l, n):
    if n == 1:
        return l
    if n % 2 == 0:
        return matexp(matmul(l, l), n//2)
    return matmul(matexp(matmul(l, l), n//2), l)
a, b, nn = map(int, input().split())
if nn == 0:
	print(a)
elif nn == 1:
    print(b)
else:
    nn -= 1
    mat = matexp([[1, 1], [1, 0]], nn)
    print((b * mat[0][0] + a * mat[1][0]) % MOD)