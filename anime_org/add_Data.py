import os, shelve
from main import *
from dbm import ndbm
def add_data(item):

	data_folder = 'data_folder'

	if os.access(data_folder, os.F_OK):
		pass
	else:
		os.mkdir(data_folder)
		
	os.chdir(data_folder)
	if os.access('data_anime.dat',os.F_OK):
		data_file = shelve.open('data_anime','w')

		nuevos = []
		for definiciones in data_file:
			nuevos.append(int(definiciones))

		key = max(nuevos) + 1
		data_file[str(key)] = item
		data_file.close()
		os.chdir('..')

	else:
		data_file = shelve.open('data_anime','c')
		data_file['1'] = item
		data_file.close()
		os.chdir('..')

def add():
	def add_more():
		print('Desea agregar más?(S/N)')
		while True:
			agregar_mas = str(input('> '))
			if agregar_mas.upper() == 'S':
				add()
				break
			elif agregar_mas.upper() == 'N':
				main()	
				break
			else:
				print('INGRESE UNA ENTRADA VÁLIDA')

	items = []
	val = True

	while True:
		print('Cuántos desea ingresar?: ')
		while True:
			try:
				cant_items = int(input('> '))
				break
			except Exception:
				print('INGRESE UNA ENTRADA VÁLIDA')
						
		for item in range(cant_items):
			new_entry = str(input('Ingrese item: '))
			items.append(new_entry.upper())
		print('-' * 30)
		print('Estos serán agregados.')
		print('_' * 30)
		for elemento in items:
			print(elemento.upper())
		print('_' * 30)
		print('Es correcto?(S/N)')
		
		while True:
			validez = str(input('> '))
			if validez.upper() == 'S':
				add_data(items)
				items.clear()
				break

			elif validez.upper() == 'N':	
				while True:
					for n in items:
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
								ubic_item = items.index(n)
								items.insert(ubic_item, item_nuevo)
								items.remove(n)
								break
							else:
								print('INGRESE UNA ENTRADA VÁLIDA')
						
					print('Los nuevos items serán estos:')
					print('_'*30)
					for item in items:
						print(item.upper())
					print('_'*30)
					print('Desea hacer algún cambio?(S/N)')

					while True:	
						cambio = str(input('>'))
						if cambio.upper() == 'S': ###################
							break
						elif cambio.upper() == 'N':
							add_data(items)
							items.clear()
							add_more()
							return
						else:
							print('INGRESE UNA ENTRADA VÁLIDA')

			else:
				print('INGRESE UNA ENTRADA VÁLIDA')
		
		add_more()
		break