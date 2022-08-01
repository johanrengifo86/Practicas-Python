from tkinter import *

from numpy import var

root = Tk()
root.title('Ejemplo')
#=================================================
# Funcionalidad de los CheckButtoon

# Variables para evaluar los check
playa = IntVar()
montaña = IntVar()
turismoRural = IntVar()

def opcionesViaje():

    opcionEscogida=''
    if playa.get() == 1:
        opcionEscogida += '-Playa-'
    if montaña.get() == 1:
        opcionEscogida += '-Montaña-'
    if turismoRural.get() == 1:
        opcionEscogida += '-Turismo Rural-'

    textoDeSeleccion.config(text=opcionEscogida)

#==================================================
# Agregar Imagen a la interfaz 
foto = PhotoImage(file='C:/Users/Stark/Documents/PracticasPython/c16_Interfaces_Graficas/avion.png')
Label(root, image=foto).pack() # incorporación y empaquetado de la imagen en un label

# Cración de un frame para manejo independiente de los checkbutton
frame = Frame(root)
frame.pack() # empaquetado del frame 

Label(frame, text='Elige Destinos', width=50).pack()

# Construcción y empaquetado de  Checkbutton
Checkbutton(frame, text='Playa', variable=playa, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text='Montaña', variable=montaña, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text='Turismo Rural', variable=turismoRural, onvalue=1, offvalue=0, command=opcionesViaje).pack()

# variable que muestra los valores escogidos en los checkbutton
textoDeSeleccion = Label(frame)
textoDeSeleccion.pack()

root.mainloop()