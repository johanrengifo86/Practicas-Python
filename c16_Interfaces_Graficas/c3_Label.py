#===========================================================
# Label --> Wigets utilizados para mostrar texto o imagenes.
#          - Tienen como única finalidad mostrar texto
#            no se puede interactuar con él.
#==========================================================
# Sintaxis
# variableLabel = Label(contenedor, opciones)
#==========================================================
from tkinter import * 

root = Tk()

miFrame = Frame(root, width=1200, height=1200)
miFrame.pack()

#  Cargar Imagen
miImagen = PhotoImage(file='I:/Johan/Naruto/kakashi.png')
Label(miFrame, image= miImagen).place(x=10, y =40)
# Texto
''' 
Label(miFrame, text='Hola Mundo', fg='blue', font= ('consola',18)).place(x=100, y =100) # Permite ubicar el texto en cualquier lugar dado por las coordenadas (x, y)
'''
root.mainloop()