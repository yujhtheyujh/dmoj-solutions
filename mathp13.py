M,N,K=map(int,input().split())
O=M-N
k=K
l=[]
i=2
while i*i<=k:
    if k%i==0:
        j=0
        while k%i==0:
            j+=1
            k//=i
        l.append((i,j))
    i+=1
if k>1:
    l.append((k,1))
def v(n,p):
    s=0
    while n:
        n//=p
        s+=n
    return s
def f(n,p,e):
    d=p**e
    l=[1]
    for i in range(1,p):
        l.append(l[-1]*i%d)
    s=1
    while n:
        a=n//p
        s*=pow(l[-1],a,d)
        b=n%p
        s*=l[b]
        s%=d
        n=a
    return s

L=[]
for i in l:
    P,E=i
    V=v(M,P)-v(N,P)-v(O,P)
    if V>=E:
        L.append((P**E,0))
        continue
    E-=V
    m,n,o=f(M,P,E),f(N,P,E),f(O,P,E)
    n*=o
    m=m*pow(n,-1,P**E)%P**E
    m*=P**V
    L.append((P**(V+E),m))

for i in range(K):
    if all(i%e==f for e,f in L):
        print(i)
        break
