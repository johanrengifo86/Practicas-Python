cadena = input('Ingrese una cadena: ')
i = int(input('Ingrese un Número: '))
j = int(input('Ingrese otro Número: '))

if j > len(cadena):
    final = len(cadena)
else:
    final = j

subcadena = ''
for k in range(i, final):
    subcadena += cadena[k]

print('La subcadena entre {} y {} es {}.'.format(i, j, subcadena))