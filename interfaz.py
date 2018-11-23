from tkinter import *
from logica import *

def dulce():
    global inputL
    inputL = 0
    return inputL

def agridulce():
    global inputL
    inputL = 25
    return inputL

def picante():
    global inputL
    inputL = 55
    return inputL

def salado():
    global inputL
    inputL = 90
    return inputL

def chico():
    global inputP
    inputP = 0
    return inputP

def mediano():
    global inputP
    inputP = 40
    return inputP

def grande():
    global inputP
    inputP = 87
    return inputP

master = Tk()
master.title("ChiliWiz")

label1 = Label(master, text="Elige un Sabor", font=("Times", 20, ))
label1.pack()

f1 = Frame(master)
botonDulce = Button(f1, text="Dulce",  command= dulce)
botonDulce.pack(side = LEFT)
botonAgridulce = Button(f1, text="Agridulce", command= agridulce)
botonAgridulce.pack(side=LEFT)
botonSalado = Button(f1, text="Salado", command= salado)
botonSalado.pack(side=RIGHT)
botonPicante = Button(f1, text="Picante", command= picante)
botonPicante.pack(side=RIGHT)
f1.pack()

label2 = Label(master, text="Elige una porcion", font=("Times", 20, ))
label2.pack()

f2 = Frame(master)
botonChico = Button(f2, text="Chico", command=chico)
botonChico.pack(side=LEFT)
botonGrande = Button(f2, text="Grande", command=grande)
botonGrande.pack(side=RIGHT)
botonMediano= Button(f2, text="Mediano", command=mediano)
botonMediano.pack(side=RIGHT)
f2.pack()

space = Label(master, text="\n")
space.pack()

def resultadoPY():
    resultado = logica(inputL, inputP)
    labelResultado = Label(master, text=resultado, font=("Times", 12, ))
    labelResultado.pack()

botonResultado = Button(master, text = "Calcular Resultado", command = resultadoPY)
botonResultado.pack()

master.mainloop()
