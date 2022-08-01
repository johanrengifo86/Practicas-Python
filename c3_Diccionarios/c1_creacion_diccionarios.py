#=================================================
#  Diccionarios 
# - Estructura de datos que permite almacenar valores de 
#   diferente tipo e incluso listas y otros diccionarios.
# - Los datos se almacenan asociados a una clave de tal forma
#   que se crea una asociación de tiopo <clave:valor> para cada elemento
# - Los elementos almacenados no están ordenados. EL orden es 
#   indiferente a la hora de almacenar informació en un diccionario
#=================================================
#
# Los diccionarios se denotan con un par de llaves 
d = {} # Diccionario vacío
diccionario = {'Alemania':'Berlín', 'Francia':'París','Inglaterra':'Londres', 'Colombia':'Bogota'}
midiccionario = {'Alemania':'Berlín', 23:'Jordan', 'Mosqueteros':3}
print(diccionario)
print(midiccionario)

# Acceder a la clave de un elemento del diccionario
print(diccionario['Francia'])

# Agregar un elemento al diccionario:
diccionario['Italia'] = 'Lisboa'
print(diccionario)
diccionario['Italia'] = 'Roma' # Cambiar clave  a un diccionario
print(diccionario)

# Utilizar una tupla para asignar claves
tupla = ('España', 'Francia', 'Reino Unido', 'Alemania')
diccionario1 = {tupla[0]:'Madrid', tupla[1]:'París', tupla[2]:'Londres', tupla[3]:'Berlín'}
print(diccionario1)
print(diccionario1['Francia'])

# Almacenamiento de un tupla en un diccionario
midicc = {23:'Jordan', 'Nombre':'Michael', 'Equipo':'Chicago Bulls', 'Anillos':(1991, 1992, 1993, 1996, 1997, 1998)}
print(midicc)
print(midicc['Equipo'])
print(midicc['Anillos'])

# Guardar un Diccionario dentro de otro diccionario
midicc1 = midicc = {23:'Jordan', 'Nombre':'Michael', 'Equipo':'Chicago Bulls', 'Anillos':{'temporadas':(1991, 1992, 1993, 1996, 1997, 1998)}}
print(midicc1)
print(midicc1['Anillos'])

# Construcción de lista telefónica:
d['Juan']  = '123 12 34 56'
d['Luis']  = '456 12 34 56'
d['Ana']   = '789 12 34 56'
d['María'] = '987 12 34 56'

#================================================
# Consulta en Diccionarios 
#================================================
# Si se desea consultar un telefóno, solo se tiene que 
# indexar el nombre
''' 
print(d['Juan'])
print(d['Ana'])
'''
# el operado <in> permite preguntar si una clave determinada aparece en un
# diccionario
'''
print('Juan' in d)
print('Pedro' in d)
'''
#==================================================
# Recorrido de Diccionarios
#==================================================
'''
for elemento in d:
    print(elemento)

for clave in d:
    print(clave, '-->', d[clave])
'''
#----------------------------
# En los  diccionarios se dispone de una método llamado <keys> proporciona
# Un generador de claves de un diccionario
# el recorrido anterios se pudo haber escrito asi:
''' 
for clave in d.keys():
    print(clave, '-->', d[clave])
'''
#----------------------------------------------
# A partir del generador de claves se puede obtener una lista
# con todas las claves del diccionario utilizando la función <list>
''' 
print(list(d.keys()))
'''
#=======================================================
# Borrado de Elementos
#=======================================================
''' 
del d['María']
for clave in d.keys():
    print( clave, '-->', d[clave])
'''   