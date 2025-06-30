M=10**9+7
def matmul(u,v):
    l=[[0]*len(v[0])for _ in range(len(u))]
    for i in range(len(u)):
        for j in range(len(v[0])):
            for k in range(len(v)):
                l[i][j]+=u[i][k]*v[k][j]%M
            l[i][j]%=M
    return l
def matexp(l, n):
    a=len(l)
    L=[[0]*a for _ in range(a)]
    for i in range(a):L[i][i]=1
    for i in bin(n)[2:]:
        L=matmul(L,L)
        if i=='1':L=matmul(L,l)
    return L
N,K=map(int,input().split())
m=[[*map(int,input().split())]for i in range(N)]
print(sum(sum(i)for i in matexp(m,K))%M)
