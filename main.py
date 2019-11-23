import tkinter as tk
from tkinter import ttk 
from cifCes import *
#from cifBin import *
from tkinter import scrolledtext


win = tk.Tk()
win.title("Codificacion")
win.resizable(0, 0)

secc01 = ttk.LabelFrame(win, text="Cifrado Cesar")
secc01.grid(column=0, row=0)

"""
tabControl = ttk.Notebook(win)

tabCesar = ttk.Frame(tabControl)
tabControl.add(tabCesar, text='Cesar')

tabBinario = ttk.Frame(tabControl)
tabControl.add(tabBinario, text='Binario')
tabControl.pack(expand=1, fill="both")

secc02 = ttk.LabelFrame(tabBinario, text="Conversor Binario")
secc02.grid(column=0, row=0)
"""
#####################################################################################

def main():
	valor=chCod.get()
	if valor == 0:
		labelResult.config(text=codificador((ingresoCesar.get()).lower(), 
												int(spinCesar.get())))
	if valor == 1:
		labelResult.config(text=decodificador((ingresoCesar.get()).lower(), 
												int(spinCesar.get())))

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
"""
def binario():
	labelBin.config(text=codBinario(converBinario.get()))

label02 = ttk.Label(secc02, text="Ingrese texto: ")
label02.grid(column=0, row=0, sticky=tk.W)

scrolW = 30
scrolH = 3

aConvBin = tk.StringVar()
converBinario = scrolledtext.ScrolledText(secc02, width=scrolW, height=scrolH, wrap=tk.WORD)
converBinario.grid(column=0, sticky=tk.EW, columnspan=3)

labelBin = ttk.Label(secc02, text="")
labelBin.grid(column=0, row=2)

buttonBin = ttk.Button(secc02, text="Convertir", command=binario)
buttonBin.grid(column=3,row=2,sticky=tk.W)
"""

#####################################################################################

win.mainloop()