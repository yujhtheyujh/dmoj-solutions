N,W=map(int,input().split())
l=[0]+[W+1]*N*1000
for i in range(N):
    w,v=map(int,input().split())
    L=l*1
    for j in range(len(l)-v):
        L[j+v]=min(l[j+v],l[j]+w)
    l=L*1
m=0
for i in range(len(l)):
    if l[i]<=W:
        m=i
print(m)
