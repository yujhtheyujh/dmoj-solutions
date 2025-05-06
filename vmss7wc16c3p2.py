[I:=lambda:[*map(int,input().split())],f:=lambda a,b:e.__setitem__(a,{*e[a],b}if a in e else{b}),A:=I(),t:={A[2]},v:=t,e:={A[2]:t},[[l:=I(),f(*l),f(*l[::-1])]for _ in' '*A[1]]]
while(n:=t):[t:=set(),[[[t.add(j)for j in e[i]if(j in v)+(j in n)<1],v.add(i)]for i in n]]
print(["N","G"][A[3]in v]+"O SHAHIR!")