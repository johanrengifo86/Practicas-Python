cadena = input('Ingrese una cadena: ')
i = int(input('Ingrese un Número: '))
j = int(input('Ingrese otro Número: '))

subcadena = ''
for k in range(i, j):
    subcadena += cadena[k]

print('La subcadena entre {} y {} es {}.'.format(i, j, subcadena))
