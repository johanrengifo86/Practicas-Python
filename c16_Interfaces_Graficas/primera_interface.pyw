from tkinter import *

# Constucción de la raíz
raiz = Tk()
# Título para la ventana creada
raiz.title('Ventana de prueba')
# Método para controlar la dimensión de la ventana 
raiz.resizable(1,1)
# Método para cambiar icono de la ventana
raiz.iconbitmap('goku.ico')
# Cambio del tamaño por defecto
raiz.geometry('650x350')

# Metodo config

raiz.config(bg='blue')




# Método que se encarga de que la ventana se encuentre en ejecución
raiz.mainloop()