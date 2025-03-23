c=[0]*3
(n,m),a,b=[[*map(int,input().split())]for _ in c]
l=[c*m for _ in n*c]
for _ in range(m*n):i=_//m;j=_%m;l[i+1][j+1]=max(l[i][j+1],l[i+1][j],l[i][j]+(a[i]==b[j]))
print(l[n][m])