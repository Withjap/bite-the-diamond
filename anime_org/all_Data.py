import shelve, os
import main as mn

def mostrar():
	os.chdir('data_folder')
	data = shelve.open('data_anime', 'r')
	fl = open('file_list.txt','w')

	for key in data:
		print('-'*30, end= '\n', file =fl)
		print(key, end='\n', file =fl)
		print('*'*30, end= '\n', file =fl)
		for elemento in data[str(key)]:
			print(elemento.upper(), end='\n', file =fl)
	else:
		fl.close()
	print('LISTO')
	os.startfile('file_list.txt')
	data.close()
	os.chdir('..')
	mn.main()
	

	data.close()