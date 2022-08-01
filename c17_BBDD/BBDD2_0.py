# Claves Principales en BBDD

import sqlite3

miConexion = sqlite3.connect('GestionProductos')
miCursor = miConexion.cursor()

# Creacion de tabla

miCursor.execute('''
    CREATE TABLE PRODUCTOS(
    CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY,
    NOMBRE_ARTICULO VARCHAR(50),
    PRECIO INTEGER,
    SECCION VARCHAR(20))
''')
# Listado de Productos a insertar 
productos = [

    ('AR01', 'Pelota', 20, 'Juegueteria'),
    ('AR02', 'Pantalón', 15, 'Confección'),
    ('AR03', 'Destornillador', 25, 'Ferretería'),
    ('AR04', 'Jarrón', 45, 'Cerámica')
]



miCursor.executemany('INSERT INTO PRODUCTOS VALUES (?,?,?,?)', productos)


miConexion.commit()
miConexion.close()
