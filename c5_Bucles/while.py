'''
i = 1
while i<= 10:
    print('Ejecución' + str(i))
    i= i+1
print('Fin de la ejecución.')
'''

edad = int(input('Introduce tu edad por favor: '))

while edad < 5 or edad > 100:
    print('Has introducido una edad incorrecta. Vuelve a itentarlo')
    edad = int(input('Introduce tu edad por favor: '))
    
print('Gracias por su colaboración. Puedes pasar')
print('Edad del Aspirante: ', edad)

