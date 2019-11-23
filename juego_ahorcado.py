import random

listaPalabras = ['gato',    'madera',   'automovil', 	 'cerveza', 'bicicleta',
				'perro', 'colectivo', 	   'camion', 	  'python', 'zapatilla',
			 'camiseta', 	  'capa', 	     'cafe', 'chocolatada',     'plato',
			'impresora',   'monitor',      'mueble',    'empanada',   'teclado',
			 'lenguaje',    'pierna', 'computadora',       'pulpo',   'japones']
palabraLista = []
palabraSeleccionada = []
listaEspacios = []

for n in random.choice(listaPalabras):
	palabraSeleccionada.append(n)
	palabraLista.append(n)

for item in palabraSeleccionada:
	listaEspacios.append('_')

partesMuñeco = ['O', '/','|','\ ','/','\ ']
partesAhorcado = ['', '', '', '', '', '']

partes = len(partesAhorcado) 
cont = 0

while True:
	alfabeto = ['A','B','C','D','E','F','G',
				'H','I','J','K','L','M','N',
				'O','P','Q','R','S','T','U',
				'V','W','X','Y','Z']

	ahorcado = 	("""			
	 ____
	|    | 	   	
	|    %s	   			
	|   %s%s%s    
	|__ %s %s    """% tuple(partesAhorcado))

	print(ahorcado, ' '.join(listaEspacios))
	
	if partes > 0:
		if '_' in listaEspacios:

			letraUser = str(input('Ingrese una letra: '))
	
			if letraUser in palabraSeleccionada:
				for letra in palabraSeleccionada:
					if letra == letraUser:
						coincidenciaIndex = palabraSeleccionada.index(letraUser)

						del listaEspacios[coincidenciaIndex]
						listaEspacios.insert(coincidenciaIndex, letraUser)
						del palabraSeleccionada[coincidenciaIndex]
						palabraSeleccionada.insert(coincidenciaIndex, '*')

			elif letraUser not in palabraSeleccionada:
				partesAhorcado[cont] = partesMuñeco[cont]
				cont += 1
				partes -= 1	
		else:
			print('Ganaste')
			break
	else:
		print('Perdiste')
		print('La palabra era {}'.format((''.join(palabraLista).upper())))		
		break