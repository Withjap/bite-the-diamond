# -*- coding: utf-8 -*-

dicc = "abcdefghijklmnopqrstuvwxyz"
ex = ",.-¿?¡! "


def codificador(palabra, cant):
	
	lista = []

	for letra in palabra.lower():
		if letra not in ex:
			lista.append(dicc[(dicc.index(letra)+cant)%-26])
		else:
			lista.append(letra)

	return "".join(lista).capitalize()

def decodificador(palabra, cant):
	
	lista2 = []

	for letra in palabra.lower():
		if letra not in ex:
			lista2.append(dicc[(dicc.index(letra)-cant)%-26])
		else:
			lista2.append(letra)

	return "".join(lista2).capitalize()
