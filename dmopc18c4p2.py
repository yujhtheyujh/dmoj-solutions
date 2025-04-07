N=int(input())
l=1<<N*350
for i in map(int,input().split()):l=l<<i|l>>i
i=0
for _ in bin(l)[-N*350-1::-1]:
    if'1'==_:print(i);break
    i+=1