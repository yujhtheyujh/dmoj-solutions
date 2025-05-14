from bisect import*
input()
l=[9e9]
for i in map(int,input().split()):
    if i>l[-1]:l.append(i)
    else:a=bisect(l,i-1);l[a]=min(l[a],i)
print(len(l))