def f():
    a,n,p=map(int,input().split())
    a%=p
    n%=p
    if a==n==0:
        print(0)
        return
    if a==0 or n==0:
        print("DNE")
        return
    b=int(p**.5+1)
    d={}
    j=1
    for i in range(b):
        if j in d:break
        d[j]=i
        j=j*a%p
    q=pow(a,-b,p)
    for i in range(p//b+1):
        if n in d:
            print(d[n]+b*i)
            return
        n=n*q%p
    print("DNE")
f()