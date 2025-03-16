import sys
sys.set_int_max_str_digits(0)
MOD = 10 ** 9 + 7
def matmul(l1, l2):
    l = [[0 for i in range(len(l2[0]))] for j in range(len(l1))]
    for i in range(len(l1)):
        for j in range(len(l2[0])):
            for k in range(len(l2)):
                l[i][j] += l1[i][k] * l2[k][j] % MOD
                l[i][j] %= MOD
    return l
def matexp(l, n):
    if n == 1:
        return l
    ll = [[0 for __ in range(4)] for _ in range(4)]
    for i in range(len(ll)):
        ll[i][i] = 1
    while n > 1:
        if n % 2 == 1:
            ll = matmul(ll, l)
        l = matmul(l, l)
        n //= 2
    return matmul(l, ll)

def main():
    po = int(input())
    if po <= 2:
        print([0, 1, 2][po])
    else:
        po -= 2
        mat = [
        [1, 1, 0, 0],
        [0, 0, 1, 0],
        [1, 0, 0, 0],
        [1, 0, 0, 1]
        ]
        # Is doing the constant term like this clown idk
        fin = matmul([[2, 1, 0, 1]], matexp(mat, po))
        print(fin[0][0] % MOD)
main()