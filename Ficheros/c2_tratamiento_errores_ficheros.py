import os

if os.path.exists('ejemplo.txt'):
    fichero = open('ejemplo.txt', 'r')
    for linea in fichero:
        print(linea)
    fichero.close()
else:
    print('El fichero no existe.')

#===============================
# Otra forma seria capturar la excepción que genera el intento de apertura
'''
try:
    fichero = open('ejemplo.txt', 'r')
    for linea in fichero:
        print(linea)
    fichero.close()
   except iOError:
       print('El fichero no existe.') 
'''