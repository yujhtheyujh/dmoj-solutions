f=lambda a,m,n,b,M,N:([[a[y//N][x//M]*b[y%N][x%M]for x in range(M*m)]for y in range(N*n)],M*m,N*n)
l=[[1]],1,1
for i in[0]*int(input()):c,d=map(int,input().split());l=f(*l,[[*map(int,input().split())]for _ in[0]*c],d,c)
a=l[0]
g=lambda l:[max(l),min(l)]
*map(print,[max([max(i)for i in a]),min([min(i)for i in a])]+g([sum(i)for i in a])+g([sum([a[j][i]for j in range(l[2])])for i in range(l[1])])),