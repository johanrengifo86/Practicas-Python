from tkinter import *


root = Tk()

# Variable donde se almacenara el menu
barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=300)

#-------------------------------
# elementos en el menu
# - archivoMenu
# - archivoEdicion
# - archivoHerramientas
# - archivoAyuda
#-------------------------------
archivoMenu = Menu(barraMenu, tearoff=0) # tearoff=0 borra barra horizontal por defecto
# submenu para archivoMenu
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label='Guardar')
archivoMenu.add_command(label='Guardar Como')
archivoMenu.add_separator() # Separa elementos del submenu
archivoMenu.add_command(label='Cerrar')
archivoMenu.add_command(label='Salir')

archivoEdicion = Menu(barraMenu, tearoff=0)
# Submenu para archivoEdicion
archivoEdicion.add_command(label='Copiar')
archivoEdicion.add_command(label='Cortar')
archivoEdicion.add_command(label='Pegar')

archivoHerramientas = Menu(barraMenu, tearoff=0)

archivoAyuda = Menu(barraMenu, tearoff=0)
# Submenu archivoAyuda
archivoAyuda.add_command(label='Licencia')
archivoAyuda.add_command(label='Acerca de...')
#-------------------------------

# Parte grafica del menu
barraMenu.add_cascade(label='Archivo', menu=archivoMenu)
barraMenu.add_cascade(label='Edición', menu=archivoEdicion)
barraMenu.add_cascade(label='Herramientas', menu=archivoHerramientas)
barraMenu.add_cascade(label='Ayuda', menu=archivoAyuda)




root.mainloop()