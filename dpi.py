N=int(input())
l=[1]
for i in map(float,input().split()):
    q=l*1
    for j in range(len(l)):
        l[j]*=i
        q[j]*=1-i
    for j in range(1,len(l)):
        l[j]+=q[j-1]
    l.append(q[-1])
print(sum(l[:N//2+1]))
