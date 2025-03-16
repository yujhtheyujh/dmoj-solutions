def f(n,b):
    if b==1:return len(n)
    s=0
    for i in[*n]:s=s*b+int(i)
    return s
l=input().split()[:1]+input().split()
b=10
for i in l[::-1]:b=f(i,b)
print(b)