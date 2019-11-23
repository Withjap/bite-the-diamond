f1 = open('Tablas.txt','w')

for n in range(1,11):
	print('Tabla del {}'.format(n), end='\n', file=f1)
	for e in range(1,11):
		result = n*e
		print('{} * {} = {}'.format(n, e, result), end='\n', file=f1)

f1.close()