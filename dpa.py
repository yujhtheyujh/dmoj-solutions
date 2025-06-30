N=int(input())
l=[*map(int,input().split())]
ll=[0,abs(l[1]-l[0])]
for i in range(2,N):ll+=[min(abs(l[i]-l[i-1])+ll[i-1],abs(l[i]-l[i-2])+ll[i-2])]
print(ll[-1])
