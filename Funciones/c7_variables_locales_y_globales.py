''' 
from math import sqrt

def area_triangulo(a, b, c):
    s = (a + b + c) / 2
    return sqrt ( s * (s-a) * (s-b) * (s-c))

print(area_triangulo(6, 30, 25))
'''
from math import sqrt, asin, pi

def area_triangulo(a, b, c):
    s = (a + b + c)/2
    return sqrt( s * (s-a) * (s-b) * (s-c))

def angulo_alfa(a, b, c):
    s = area_triangulo(a, b ,c)
    return 180 / pi * asin(2 * s/ (b*c)) 

def menu():
    opcion = 0
    while opcion != 1 and opcion != 2:
        print('1) Calcular área del triángulo')
        print('2) Calcular ángulo opuesto al primer lado')
        opcion = int(input('Escoge opción: '))
    return opcion

lado1 = float(input('Ingresa lado a: '))
lado2 = float(input('Ingresa lado b: '))
lado3 = float(input('Ingresa lado c: '))

s = menu()

if s == 1:
    resultado = area_triangulo(lado1, lado2, lado3)
else:
    resultado = angulo_alfa(lado1, lado2, lado3)

print('Escogio la opción: ', s)
print('El resultado es: ', resultado)
