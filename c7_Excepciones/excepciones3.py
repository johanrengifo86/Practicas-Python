'''
def evaluarEdad(edad):
    if edad < 0:
        raise TypeError('No se permiten edades negativas')
    if edad < 20:
        return 'Eres muy Joven'
    elif edad < 40:
        return'Eres Joven'
    elif edad < 60:
        return 'Eres Mayor'
    elif edad < 100:
        return ' Cuidate..'
print(evaluarEdad(-39)) 
 '''
import math

def calculaRaiz(num):
    if num < 0:
        raise ValueError('El número no puede ser negativo')
    else:
        return math.sqrt(num)

opc1 = int(input('Introduce un número: '))
try:
    print(calculaRaiz(opc1))
except ValueError as ErrorDeNumeroNegativo:
    print(ErrorDeNumeroNegativo)
print('Programa terminado')
