import os
import add_Data as aD
import search_Data as sD
import all_Data as alD
from edit_data import *

data_folder = 'data_folder'
files_in_data_folder = 'data_anime.dat', 'data_anime.bak', 'data_anime.dir'

def main():

	if os.path.isdir(data_folder):
		os.chdir(data_folder)
		if os.access('data_anime.dat',os.F_OK):
			os.chdir('..')
			print('Ingrese opción de menú: ')
			print("""
				1.- Agregar nuevos
				2.- Buscar
				3.- Mostrar todos
				4.- Editar lista
				5.- Salir
						""")
			
			while True:
				try:
					eleccion_menu = int(input("> "))
					if eleccion_menu == 1:
						aD.add()
						break
					elif eleccion_menu == 2:
						sD.search()
						break
					elif eleccion_menu == 3:
						alD.mostrar()
						break
					elif eleccion_menu == 4:
						edit_data()
						break	
					elif eleccion_menu == 5:
						break

					elif eleccion_menu == 1707:

						seguro = str(input('ESTÁ SEGURO?(S/N): '))

						if seguro.upper() == 'S':

							seguro_dos = str(input('ESTÁ SEGURO DE ELIMINAR LA CARPETA DE DATOS?(S/N): '))

							if seguro_dos.upper() == 'S':
								os.chdir(data_folder)
								for file in files_in_data_folder:
									os.remove(file)
								if os.access('file_list.txt',os.F_OK):
									os.remove('file_list.txt')
								os.chdir('..')
								os.rmdir(data_folder)
								print('CARPETA ELIMINADA')
								main()
								break
							else:
								print('ERROR')
								main()
						
						else:
							main()		

					else:
						print('INGRESE UNA ENTRADA VÁLIDA')
				except ValueError:
					print('INGRESE UNA ENTRADA VÁLIDA')
		else:
			os.chdir('..')
			os.rmdir(data_folder)
			main()

	else:
		print('Ingrese opción de menú: ')
		print("""
				1.- Agregar nuevos
				2.- Salir
						""")

		while True:
			try:
				op_dos = int(input('> '))

				if op_dos == 1:
					aD.add()
					break
				elif op_dos == 2:
					break
				else:
					print('INGRESE UNA ENTRADA VÁLIDA')
			except ValueError:
				print('INGRESE UNA ENTRADA VÁLIDA')
	
if __name__ == '__main__':main()