#======================================
# Pasos a seguir para conectar una BBDD
#======================================
# 1. Abrir - Crear conexion
# 2. Crear Puntero o Cursor
# 3. Ejecutar query(Consulta)SQL
# 4. Manejar los resultados de la query(consulta)
# 4.1 Insertar, Leer, Actualizar, Borrar( Create, Read, Update, Delete)
# 5. Cerrar puntero
# 6. Cerrar conexion
#=============================================================================
import sqlite3
# 1
miConexion = sqlite3.connect('PrimeraBBDD')

# 2
miCursor = miConexion.cursor()

# 3
#miCursor.execute("CREATE TABLE PRODUCTOS( NOMBRE_ARTICULOS VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")
# 4
#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALÓN', 15, 'DEPORTES')")
# 4.1
# Insertar un Lote de registros 
''' 
variosProductos=[

    ("Camiseta", 10, "Deportes"),
    ("Jarrón", 90, "Cerámica"),
    ("Camión", 20, "Juguetería")

]
miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?, ?, ?)", variosProductos)
'''
# Consultar

miCursor.execute("SELECT * FROM PRODUCTOS")
variosProductos = miCursor.fetchall() # fetchall devuleve una lista con todos los registros 
for producto in variosProductos:
    print('Nombre Articulo: ',producto[0], '\nSección: ', producto[2], '\nPrecio: $', producto[1])

miConexion.commit() # Confirmacion de cambios 



# 6
miConexion.close()

