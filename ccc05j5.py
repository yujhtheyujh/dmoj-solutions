while(a:=input())!='X':
    try:eval(a.replace('B','(+').replace('S',')').replace('A','(0)').replace('N','*'));print('YES')
    except:print('NO')