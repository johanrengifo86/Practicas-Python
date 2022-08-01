from math import sqrt

a = float(input('Valor de a:'))
b = float(input('Valor de b:'))
c = float(input('Valor de c:'))

try:
    x1= (-b + sqrt(b**2 - 4*a*c)) / (2 * a)
    x2= (-b - sqrt(b**2 - 4*a*c)) / (2 * a)
    if x1 == x2:
        print('Solución: x={0: .3f}'.format(x1))
    else:
        print('Soluciones: x1={0:.3f} y x2={1:.3f}'.format(x1, x2))
except:
    # No sabemos si llegamos aquí por una división por cero o si llegaos
    # por intentar calcular la raíz cuadrada de un discriminante negativo
    print(' O no hay soluciones reales o es una ecuación de primer grado')