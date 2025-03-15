import sys
n=int(input())
a=''.join(i.rstrip()for i in sys.stdin.readlines())
if 'P'in a:
    a='P'+a+'P'
    p=r=m=s=0
    while 1:
        if s==1:m=max(m,p-r)
        if s<2:
            if p==n:break
            p+=1
            if a[p]<'S': s+=1
        else:
            r+=1
            if a[r]<'S': s-=1
    print(m)
else:print(n-1)