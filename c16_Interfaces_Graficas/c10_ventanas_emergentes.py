from tkinter import *
from tkinter import messagebox # libreria para generar las ventanas emergentes


root = Tk()

# función que construye la ventana emergente
def infoAdicional():
    messagebox.showinfo('Procesador Stark', 'Procesador de texto version 2022')

def avisoLicencia():
    messagebox.showwarning('Licencia', 'Producto bajo licencia GNU')

def salirAplicacion():
    #valor = messagebox.askquestion('Salir', '¿Deseas salir de la aplicación?')
    valor = messagebox.askokcancel('Salir', '¿Deseas salir de la aplicación?')
    #if valor == 'yes':
    if valor == True:
        root.destroy()

def cerrarDoumento():
    valor = messagebox.askretrycancel('Reintentar', 'No es posible cerrar. Documento bloqueado')
    if valor == False:
        root.destroy()



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
archivoMenu.add_command(label='Cerrar', command=cerrarDoumento)
archivoMenu.add_command(label='Salir', command=salirAplicacion)

archivoEdicion = Menu(barraMenu, tearoff=0)
# Submenu para archivoEdicion
archivoEdicion.add_command(label='Copiar')
archivoEdicion.add_command(label='Cortar')
archivoEdicion.add_command(label='Pegar')

archivoHerramientas = Menu(barraMenu, tearoff=0)

archivoAyuda = Menu(barraMenu, tearoff=0)
# Submenu archivoAyuda
archivoAyuda.add_command(label='Licencia', command=avisoLicencia)
archivoAyuda.add_command(label='Acerca de...', command=infoAdicional) # con el comando command asignamos la ventana emergente
#-------------------------------

# Parte grafica del menu
barraMenu.add_cascade(label='Archivo', menu=archivoMenu)
barraMenu.add_cascade(label='Edición', menu=archivoEdicion)
barraMenu.add_cascade(label='Herramientas', menu=archivoHerramientas)
barraMenu.add_cascade(label='Ayuda', menu=archivoAyuda)




root.mainloop()