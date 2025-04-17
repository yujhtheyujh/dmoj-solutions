I=lambda:[*map(int,input().split())]
def f():
    l=[0]+[I()for _ in[0]*I()[0]]
    def g(i):return"("+"".join(sorted(j<0and str(j)or g(j)for j in l[i]))+")"
    return g(1)
print("Fred and Mary",["have different mobiles.","might have the same mobile."][f()==f()])