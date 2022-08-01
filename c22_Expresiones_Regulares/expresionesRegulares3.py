# Rangos
import re
''' 
lista_nombres = ['Ana', 'Pedro', 'María', 'Rosa', 'Sandra', 'Celia']

for elemento in lista_nombres:
    if re.findall('^[O-T]', elemento):
        print(elemento)
'''
codigos = [ 'Ma1',
            'Se1',
            'Ma2',
            'Ba1',
            'Ma3',
            'Va1',
            'Va2',
            'Ma4',
            'MaA',
            'Ma5',
            'MaB',
            'MaC'     
          ]
# Busqueda de los codigos comprendidos en el rango[0-3]
for elemento in codigos:
    if re.findall('Ma[0-3]', elemento):
        print(elemento)
print('********************************')
# Busqueda de los codigos diferentes al rango[0-3]
for elemento in codigos:
    if re.findall('Ma[^0-3]', elemento):
         print(elemento)
print('**********************')
# multiple busqueda de rangos
for elemento in codigos:
    if re.findall('Ma[0-3A-B]',elemento):
        print(elemento)
