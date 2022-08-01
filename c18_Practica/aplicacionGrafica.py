from tkinter import *
from tkinter import messagebox
import sqlite3


#-----------------------funciones-----------------------

def conexionBBDD():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()

    try:
        miCursor.execute('''
            CREATE TABLE DATOSUSUARIOS(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE_USUARIO VARCHAR(50),
            APELLIDO VARCHAR(10),
            PASSWORD VARCHAR(50),
            DIRECCION VARCHAR(50),
            COMENTARIOS VARCHAR(100))    
        ''')
        messagebox.showinfo("BBDD", "BBDD creado con éxito.")
    except:
        messagebox.showwarning("¡Atención!", "La BBDD ya existe")

def salirAplicacion():
    valor = messagebox.askquestion("Salir", "¿Desea salir de la aplicación?")
    if valor =="yes":
        root.destroy()

def limpiarCampos():
    stringId.set("")
    stringNombre.set("")
    stringApellido.set("")
    stringPass.set("")
    stringDireccion.set("")
    textoComentario.delete(1.0, END)

def crear():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()
    ''' 
    miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL, '" + stringNombre.get() +
        "','" + stringApellido.get() +
        "','" + stringPass.get() +
        "','" + stringDireccion.get() +
        "','" + textoComentario.get("1.0", END) + "')")
    '''
    # Consulta parametrizada
    datos = stringNombre.get(), stringApellido.get(), stringPass.get(), stringDireccion.get(), textoComentario.get("1.0", END)
    miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,?,?,?,?,?)", (datos))


    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro Inserado con éxito")

def leer():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()
    miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID=" + stringId.get())
    elUsuario = miCursor.fetchall() # fetcharl devuelve un array
    for usuario in elUsuario:
        stringId.set(usuario[0])
        stringNombre.set(usuario[1])
        stringApellido.set(usuario[2])
        stringPass.set(usuario[3])
        stringDireccion.set(usuario[4])
        textoComentario.insert(1.0, usuario[5] )

    miConexion.commit()

def actualizar():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()
    ''' 
    miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO='" + stringNombre.get() +
                    "', APELLIDO='" + stringApellido.get() +
                    "', PASSWORD='" + stringPass.get() +
                    "', DIRECCION='" + stringDireccion.get() +
                    "',  COMENTARIOS='" + textoComentario.get("1.0", END) +
                    "' WHERE ID=" + stringId.get() )
    '''
    # Consulta parametrizada
    datos = stringNombre.get(), stringApellido.get(), stringPass.get(), stringDireccion.get(), textoComentario.get("1.0", END)
    miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO=?, APELLIDO=?, PASSWORD=?, DIRECCION=?, COMENTARIOS=?" + 
                     "WHERE ID=" + stringId.get(), (datos))

    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro Actualizado con éxito.")
    
def eliminar():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()

    miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID=" + stringId.get())
    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro borradp con éxito")


root = Tk()

#=================================
# Creación barra menú superior
#=================================
barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=300)
#================================================
# opciones de la barra superior con sus elementos
#================================================
# 1. opción menú
bbddMenu = Menu(barraMenu, tearoff=0)
# elementos de la opción Menú
bbddMenu.add_command(label='Conectar', command=conexionBBDD)
bbddMenu.add_command(label='Salir', command=salirAplicacion)
# 2. opción borrar
borrarMenu = Menu(barraMenu, tearoff=0)
# elementos de la opción Borrar
borrarMenu.add_command(label='Borrar Campos', command=limpiarCampos)
# 3. opción CRUD
crudMenu = Menu(barraMenu, tearoff=0)
# elementos de la opción CRUD
crudMenu.add_command(label='Crear', command=crear)
crudMenu.add_command(label='Leer', command=leer)
crudMenu.add_command(label='Actualizar', command=actualizar)
crudMenu.add_command(label='Borrar', command=eliminar)
# 4. opción AYuda
ayudaMenu = Menu(barraMenu, tearoff=0)
# elementos de la opción ayuda
ayudaMenu.add_command(label='Licencia')
ayudaMenu.add_command(label='Acerca de ...')

#=================================================
# incorporación de las opciones de la barra superior a la barra menú
barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

# -----------------------Inicio de Campos------------------------------- 
# Frame de la parte superior
#-----------------------------------------
miFrame = Frame(root)
miFrame.pack()

# Indica que en cada uno de los Entry va a haber una cadena de caracteres 
stringId = StringVar()
stringNombre = StringVar()
stringApellido = StringVar()
stringPass = StringVar()
stringDireccion = StringVar()

# Cuadros de texto
cuadroID = Entry(miFrame, textvariable=stringId)
cuadroID.grid(row=0, column=1, padx=10, pady=10)

cuadroNombre = Entry(miFrame, textvariable=stringNombre)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="right")

cuadroApellido = Entry(miFrame, textvariable=stringApellido)
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)

cuadroPass = Entry(miFrame, textvariable=stringPass)
cuadroPass.grid(row=3, column=1, padx=10, pady=10)
cuadroPass.config(show="*")

cuadroDireccion = Entry(miFrame, textvariable=stringDireccion)
cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)

textoComentario = Text(miFrame, width=16, height=5)
textoComentario.grid(row=5, column=1, padx=10, pady=10)
# barras de deplazamiento
scrollVert = Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")
# incorporación de la barra de desplazamiento al textoComentario
textoComentario.config(yscrollcommand=scrollVert.set)

#-------------------Creación de Label-------------------
idLabel = Label(miFrame, text="Id:")
idLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

nombreLabel = Label(miFrame, text="Nombre:")
nombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

apellidoLabel = Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

passLabel = Label(miFrame, text="Password:")
passLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

direccionLabel = Label(miFrame, text="Dirección:")
direccionLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

comentariosLabel = Label(miFrame, text="Comentarios:")
comentariosLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)

#--------------------Botones--------------------
inferiorFrame = Frame(root)
inferiorFrame.pack()

botonCrear = Button(inferiorFrame, text="Crear", command=crear)
botonCrear.grid(row=1, column=0, sticky="e", padx=10, pady=10)

botonLeer = Button(inferiorFrame, text="Leer", command=leer)
botonLeer.grid(row=1, column=1, sticky="e", padx=10, pady=10)

botonCargar = Button(inferiorFrame, text="Cargar", command=actualizar)
botonCargar.grid(row=1, column=2, sticky="e", padx=10, pady=10)

botonEliminar = Button(inferiorFrame, text="Eliminar", command=eliminar)
botonEliminar.grid(row=1, column=3, sticky="e", padx=10, pady=10)

root.mainloop()