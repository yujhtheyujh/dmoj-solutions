N=int(input())
A=B=C=0
for i in' '*N:
    a,b,c=map(int,input().split())
    A,B,C=max(B,C)+a,max(A,C)+b,max(A,B)+c
print(max(A,B,C))
