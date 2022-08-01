#===============
# Metacaracteres(caracteres comodín)
# * Anclas y clases de caracteres
#=====================
# Anclas
import re
'''
lista_nombres = [ 'Ana Gomez', 
                  'María Martín',
                  'Sandra López',
                  'Santiago Martín',
                  'Sandra Fernandéz'            
                ]
for elemento in lista_nombres:
#   if re.findall('^Sandra', elemento):  #  para la busqueda inician por: '^' antes de elemento de busqueda
    if re.findall('Martín$', elemento):  # para la busqueda que terminan por :'$'
        print(elemento)
'''
lista_dominio=['http://pildorasinformaticas.es',
               'ftp://pildorasinformaticas.es',
               'http://pildorasinfromaticas.com',
               'ftp://pildorasinformaticas.com'
              ]

for elemento in lista_dominio:
    if re.findall('es$', elemento):
        print(elemento)


# Clases de caracteres 
lista = ['hombres', 'mujeres', 'niños','niñas', 'mascotas']
for elemento in lista:
    if re.findall('niñ[oa]s', elemento):
        print(elemento)