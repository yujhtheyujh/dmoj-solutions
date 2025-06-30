N,W=map(int,input().split())
l=[0]+[-1]*W
for i in range(N):
    w,v=map(int,input().split())
    L=l*1
    for j in range(len(l)-w):
        if l[j]>=0:
            L[j+w]=max(l[j+w],l[j]+v)
    l=L*1
print(max(l))
