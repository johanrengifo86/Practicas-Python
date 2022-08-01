#==============
# Tuplas
#==============
# Son listas inmutables
# - No permiten añadir, eliminar, mover elementos etc(No append,extend, remove)
# - Permite extraer porciones, pero el resultado es un tupla nueva
# - Permite búsquedas
# - Permite comprobar si un elemento se encuentra en una tupla
# Ventajas : 
#   - Más Rápidas
#   - Menos espacio( mayor optimización)
#   - Formatean Strings
#   - Pueden utilizarse como claves en un diccionario
#=======================================================
tupla = ( 'Juan', 13, 5, 1995, 13)

# Acceder a un elemento de una tupla
print(tupla[2])

# Método para convertir tuplas en listas
lista = list(tupla)
print (lista)
print(tupla)

# Método para convertir lista en tupla
convtupla = tuple(lista)
print(convtupla)

# Consultar si un elemento se encuntra dentro de una tupla
print('Juan' in tupla)

# Método para contar cuantas veces se encunetra el elemento en una tupla
print(tupla.count(13))

# Método para averiguar la longitud de una tupla
print(len(tupla))

# Tupla unitaria
mitupla = ('Juan', )

# Desempaquetado de tuplas
mitupla1 = ('Juan', 13, 1, 1995)
name, day, month, year = mitupla1
print(name)
print(day)
print(year)
print(month)
