a = float(input('Ingrese valor de a: '))
b = float(input('Ingrese valor de b: '))

try:
    x = -b/a
    print('Solución: ', x)
except:
    if b != 0:
        print('La ecuación no tiene solución')
    else:
        print('La ecuación tiene infinitas soluciones.')

