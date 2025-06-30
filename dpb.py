N,K=map(int,input().split())
l=[*map(int,input().split())]

ll=[0]
for i in range(1,N):
    m=abs(l[i]-l[i-1])+ll[i-1]
    for j in range(2,K+1):
        if i<j:break
        m=min(m,abs(l[i]-l[i-j])+ll[i-j])
    ll.append(m)
print(ll[-1])
