from tkinter import * 
from tkinter import filedialog

from setuptools import Command

root = Tk()

def abreFichero():
    fichero = filedialog.askopenfile(title='Abrir', initialdir="C:", filetypes=(('Ficheros de Excel', '*.xlsx'),('Ficheros de Texto', '*.txt')
    ,('Todos los Ficheros', '*.*')))
    print(fichero)

Button(root, text='Abrir fichero', command=abreFichero).pack()

root.mainloop()