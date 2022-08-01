from tkinter import *

root = Tk()

miFrame = Frame(root, width=1200, height=600)
miFrame.pack()
#Entry 
cuadroNombre = Entry(miFrame)
cuadroNombre.grid(row=0, column=1)
cuadroNombre.config(fg='red', justify='center')

cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=1, column=1)

cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row=2, column=1)

cuadroPass = Entry(miFrame)
cuadroPass.grid(row=3, column=1)
cuadroPass.config(show='*')

# Label
nombreLabel = Label(miFrame, text='Nombre:')
nombreLabel.grid(row=0, column=0, sticky='w', padx=10, pady=10)

apellidoLabel = Label(miFrame, text='Apellido:' )
apellidoLabel.grid(row=1, column=0, sticky ='w', padx=10, pady=10)

direccionLabel = Label(miFrame, text='Dirección de casa:')
direccionLabel.grid(row=2, column=0, sticky = 'w', padx=10, pady=10)

passLabel = Label(miFrame, text='Password:')
passLabel.grid(row=3, column=0, sticky='w', padx=10, pady=10 )



root.mainloop()