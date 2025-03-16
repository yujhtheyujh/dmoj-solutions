for i in[0]*int(input()):
	try:eval('+1+'.join([*input()]).replace('+)',')'));print('YES')
	except:print('NO')