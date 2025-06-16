import math
N,M=map(int,input().split())
s=input()
t=input()
g=math.gcd(len(s),len(t))
S=0
for i in range(g):
    l=[0]*26
    L=[0]*26
    for j in s[i::g]:
        l[ord(j)-97]+=1
    for j in t[i::g]:
        L[ord(j)-97]+=1
    for j in range(26):
        S+=l[j]*L[j]
print(S*len(s)*N//math.lcm(len(s),len(t)))