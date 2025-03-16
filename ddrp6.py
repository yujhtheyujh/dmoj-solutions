MOD = 10 ** 9 + 7
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
nn = int(input())
if nn <= 3:
    print([0, 4, 16, 64][nn])
else:
    nn -= 3
    a = matexp([[3, 1, 0], [3, 0, 1], [2, 0, 0]], nn)
    print((64 * a[0][0] + 16 * a[1][0] + 4 * a[2][0]) % MOD)