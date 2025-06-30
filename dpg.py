__import__("sys").setrecursionlimit(2000000)
V,E=map(int,input().split())
l=[[]for i in range(V)]
for i in range(E):
    a,b=map(int,input().split())
    a-=1
    b-=1
    l[b].append(a)
d={}
def f(n):
    if n in d:return d[n]
    m=0
    for i in l[n]:m=max(m,f(i)+1)
    d[n]=m
    return m
print(max(f(i)for i in range(V)))
