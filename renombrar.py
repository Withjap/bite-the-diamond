"""
Renombrar archivos a partir de etiqueta en direccion web
"""

import os
import requests
from bs4 import BeautifulSoup

os.chdir('')

palabra = []
for n in os.listdir():
	for letra in n:
		palabra.append(letra)
	if ' ' in palabra:
		palabra.remove(' ')
		nueva_palabra = ''.join(palabra)
		os.rename(n, nueva_palabra)

	palabra.clear()

for item in os.listdir():
	os.path.splitext(item)
	name_changed = os.path.splitext(item)[0]
	print(name_changed)

	if name_changed.isdigit():
		req = requests.get('/{}/'.format(name_changed))
		soup = BeautifulSoup(req.text, "lxml")

		new_name = soup.h1.string + '.rar'
	
		palabra_dos = []
		not_allowed = ['*', '"', '/', '\ ', '<', '>', ':', '|', '?']

		for letra in new_name:
			palabra_dos.append(letra)
		for character in no_allowed:
			for n in palabra_dos:
				if character == n:
					palabra_dos.remove(character)
		new_name = ''.join(palabra_dos)
		print(new_name)
		os.rename(item, new_name)
		palabra_dos.clear()
		

	