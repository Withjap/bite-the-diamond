import shelve, os
from all_Data import *
import main as mn
def edit_data():
	os.chdir('data_folder')
	edit_data = shelve.open('data_anime')

	keys = []
	for n in edit_data:
		keys.append(int(n))

	print('¿Qué disco desea editar?')
	while True:
		try:
			edicion = int(input('> '))
			if edicion in keys:
				break
			else:
				print('NO SE HA REGISTRADO ESE DISCO. INGRESE NUEVAMENTE.')
		except ValueError:
			print('INGRESE UNA ENTRADA VÁLIDA')

	elementos = []

	print('El disco {} contiene lo siguientes elementos: '.format(edicion))
	for item in edit_data[str(edicion)]:
		elementos.append(item)
		print(item.upper())
	print('*'*30)

	while True:
		for n in elementos:
			while True:
				print('-'*30)
				print(n.upper())
				print('-'*30)
				print('ESTE ES CORRECTO?(S/N)')
				validez_dos = input('> ')

				if validez_dos.upper() == 'S':
					print('Muy bien.')
					print('_' * 30)
					break
				elif validez_dos.upper() == 'N':								
					print('Ingrese nuevamente el item:')
					item_nuevo = input('> ')
					print('_'*30)
					#Toma la ubicacion del item incorrecto en la lista,
					#ingresa al nuevo en esa ubicacion y elimina el incorrecto
					ubic_item = elementos.index(n)
					elementos.insert(ubic_item, item_nuevo)
					elementos.remove(n)
					break
				else:
					print('INGRESE UNA ENTRADA VÁLIDA')
						
		print('Los nuevos items serán estos:')
		print('*'*30)
		for item in elementos:
			print(item.upper())
		print('*'*30)
		print('Desea hacer algún cambio?(S/N)')

		while True:	
			cambio = str(input('>'))
			if cambio.upper() == 'S':
				break
			elif cambio.upper() == 'N':
				edit_data[str(edicion)] = elementos
				elementos.clear()
				edit_data.close()
				os.chdir('..')
				mn.main()
				return
			else:
				print('INGRESE UNA ENTRADA VÁLIDA')
