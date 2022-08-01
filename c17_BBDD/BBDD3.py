import sqlite3

miConexion = sqlite3.connect('GestionProductos')
miCursor = miConexion.cursor()

# Instrucciones CRUD
# Leer

miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION = 'Confección' ")

#productos = miCursor.fetchall()
#print(prodcutos)

 #Actualizar
 #miCursor.execute("UPDATE PRODUCTOS SET PRECIO=35 WHERE NOMBRE_ARTICULO='Pelota'")


# Borrar
miCursor.execute("DELETE FROM PRODUCTOS WHERE  ID=5")

miConexion.commit()
miConexion.close()
