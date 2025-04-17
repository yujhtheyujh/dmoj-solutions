def main():
    import sys
    input=sys.stdin.readline
    print=lambda n:sys.stdout.write(str(n)+"\n")
    def f(n):
        if n==0:return 99
        s=0
        while~n%2:n>>=1;s+=1
        return s
    N,Q=map(int,input().split())
    l=[[*map(int,input().split())]+[0]*(2**len(bin(N)[2:])-N)]
    while~-len(l[-1]):l.append([*map(sum,zip(l[-1][::2],l[-1][1::2]))])
    for i in[0]*Q:
        a,b,c=input().split()
        b,c=int(b)-1,int(c)
        if'U'>a:
            s=0
            while b-c:
                d=min(f(b),(c-b).bit_length()-1)
                s+=l[d][b>>d]
                b+=1<<d
            print(s)
        else:
            c-=l[d:=0][b]
            while d<len(l):l[d][b]+=c;d+=1;b>>=1
main()