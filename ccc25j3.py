for _ in[0]*int(input()):
    s=input().rstrip();a=[i for i in s if i in map(chr,range(65,91))]
    for i in map(chr,range(65,123)):s=s.replace(i,'+')
    print(''.join(a)+str(eval(s+'+0')))