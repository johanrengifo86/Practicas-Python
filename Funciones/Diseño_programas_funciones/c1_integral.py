a = float(input('Inicio del Intervalo: '))
b = float(input('Final del Intervalo: '))
n = int(input(' Número de Rectángulos: '))

if n == 0:
    sumatorio = 0.0
else:
    deltax = (b - a) / n
    sumatorio = 0.0
    for i in range(n):
        sumatorio += deltax * (a + i * deltax) ** 2

print('La Integral de x**2 entre ', end='')
print('{} y {} es (aprox) {}'.format(a, b, sumatorio))
