from tkinter import *

root = Tk()

miFrame = Frame(root, width=1200, height=600)
miFrame.pack()

minombre = StringVar()

#Entry
cuadroNombre = Entry(miFrame, textvariable=minombre)
cuadroNombre.grid(row=0, column=1)
cuadroNombre.config(fg='red', justify='center')

cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=1, column=1)

cuadroPass = Entry(miFrame)
cuadroPass.grid(row=2, column=1)
cuadroPass.config(show='*')

cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row=3, column=1)

#Text
textoComentario = Text(miFrame, width=16, height=5)
textoComentario.grid(row=4, column=1, padx=10, pady=10)
#scrollbar para el texto
scrollVert = Scrollbar(miFrame, command=textoComentario.yview)
#colocar scrollbar
scrollVert.grid(row=4, column=2, sticky='nsew')
textoComentario.config(yscrollcommand=scrollVert.set)


# Label
nombreLabel = Label(miFrame, text='Nombre:')
nombreLabel.grid(row=0, column=0, sticky='w', padx=10, pady=10)

apellidoLabel = Label(miFrame, text='Apellido:' )
apellidoLabel.grid(row=1, column=0, sticky ='w', padx=10, pady=10)

passLabel = Label(miFrame, text='Password:')
passLabel.grid(row=2, column=0, sticky='w', padx=10, pady=10 )

direccionLabel = Label(miFrame, text='Dirección:')
direccionLabel.grid(row=3, column=0, sticky = 'w', padx=10, pady=10)

comentariosLabel = Label(miFrame, text='Comentarios:')
comentariosLabel.grid(row=4, column=0, sticky='w', padx=10, pady=10)

def codigoBoton():
    minombre.set('Johan')
# Button
botonEnvio = Button(root,text='Enviar',command=codigoBoton)
botonEnvio.pack()





root.mainloop()