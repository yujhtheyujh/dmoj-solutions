import sys
input=sys.stdin.readline
N,M=map(int,input().split())
d={}
for i in range(N):
    v,m=map(int,input().split())
    if m in d:d[m].append(-v)
    else:d[m]=[-v]
l=[]
for i in d:
    l.append(i)
l.sort()
s=0
for i in range(len(l)):
    d[l[i]].sort()
    if i==len(l)-1:
        s+=sum(d[l[i]][:M//l[i]])
        continue
    M-=M%l[i]
    a=M%l[i+1]
    a//=l[i]
    s+=sum(d[l[i]][:a])
    d[l[i]]=d[l[i]][a:]
    b=l[i+1]//l[i]
    e=0
    for e in range(len(d[l[i]])//b+1):
        d[l[i+1]].append(sum(d[l[i]][e*b:e*b+b]))
print(-s)