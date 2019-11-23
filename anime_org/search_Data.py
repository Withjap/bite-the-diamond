import main as mn
import shelve, os

def search():
	
	def por_disco():

		data_file = shelve.open('data_anime','r')

		while True:
			try:
				search = int(input('Ingrese numero de disco: '))
				break
			except Exception:
				print('Ingrese entrada valida.')
		discos = []
		for d in data_file:
			discos.append(int(d))
		while True:
			if search in discos:
				print('El disco numero {} contiene los siguientes elementos:'.format(search))
				print('*'*30)
				for disco in data_file[str(search)]:
					print('>', disco.upper())
					data_file.close()
				print('*'*30)				
				break
			else:
				print('*'*30)
				print('AÚN NO SE HA ALMACENADO ESE DISCO')
				print('*'*30)				
				break

	def por_elemento():

		data_elemento = shelve.open('data_anime','r')
		contenedor = []
		while True:
			item_search = input('Ingrese un nombre a buscar: ')
			
			if len(item_search) >= 4:
				for key in data_elemento:
					for elemento in data_elemento[str(key)]:
						if item_search.upper() in elemento:
							contenedor.append(int(key))
				else:
					break
			else:
				print('INGRESE UN MÍNIMO DE 4(CUATRO) CARÁCTERES')

		contenedor = list(set(contenedor))
		contenedor.sort()
		if contenedor == []:
			print('NO SE HA ENCONTRADO.')
		else:
			for n in contenedor:
				print('EL ELEMENTO SE ENCUENTRA EN EL DISCO {}'.format(n))
		print('-'*30)

	os.chdir('data_folder')

	while True:

		print('Cómo desea buscar?: ')
		print('''
			1- Por disco.
			2- Por contenido.
			3- Salir
			''')	
		try:
			seleccion = int(input('> '))
			if seleccion == 1:
				por_disco()
				
			elif seleccion == 2:
				por_elemento()
				
			elif seleccion == 3:
				os.chdir('..')
				mn.main()
				break
			else:
				print('INGRESE UNA ENTRADA VÁLIDA')
		except ValueError:
			print('INGRESE UNA ENTRADA VÁLIDA')