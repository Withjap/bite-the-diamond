"""
Programa de cifrado César simple
Python ver. 2.x y 3.x 
"""

import tkinter as tk
from tkinter import ttk 
from cifCes import *
#from cifBin import *
from tkinter import scrolledtext


win = tk.Tk()
win.title("Cifrado")
win.resizable(0, 0)

secc01 = ttk.LabelFrame(win, text="Cesar")
secc01.grid(column=0, row=0)

#####################################################################################

def main():
	valor=chCod.get()
	if valor == 0:
		labelResult.config(text=codificador((ingresoCesar.get()).lower(), int(spinCesar.get())))
	if valor == 1:
		labelResult.config(text=decodificador((ingresoCesar.get()).lower(), int(spinCesar.get())))

label = ttk.Label(secc01, text="Ingrese texto: ")
label.grid(column=1, row=0)

labelResult = ttk.Label(secc01, text="")
labelResult.grid(column=1, row=2)

aCifrar = tk.StringVar()
ingresoCesar = ttk.Entry(secc01, width=12, textvariable=aCifrar)
ingresoCesar.grid(column=1, row=1)
ingresoCesar.focus()

cifrar = ttk.Button(secc01, text="Cifrar", command=main)
cifrar.grid(column=2,row=1)

spinCesar = tk.Spinbox(secc01, from_=1, to=10, width=3)
spinCesar.grid(column=3, row=1)
spinCesar_valor = int(spinCesar.get())

codDec = ["Derecha", "Izquierda"]

chCod = tk.IntVar()

checkCodi = tk.Radiobutton(secc01, text=codDec[0], variable=chCod, value=0)
checkCodi.grid(column=4,row=0, sticky=tk.W)

checkDeco = tk.Radiobutton(secc01, text=codDec[1], variable=chCod, value=1)
checkDeco.grid(column=4,row=1, sticky=tk.W)

#####################################################################################
win.mainloop()
