#===========
# Yiel from
#===========
# Utilidad: Simplicar el código de los generadores en el caso de utilizar bucles anidados
def devuelve_ciudades(*ciudades): # el '*' le indica a python que recibira un número indeterminado de elementos
    for elemento in ciudades:
        #for subElemento in elemento:
            yield from elemento  
ciudades_devueltas = devuelve_ciudades('Madrid', 'Barcelona', 'Bilbao', 'Valencia')
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))