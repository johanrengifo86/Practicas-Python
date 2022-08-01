# Los programas que se diseñen tendrán <<tres tipos de linea>>
# 1. Importación de módulos (o funciones y variables de módulos)
# 2. Definición de fuciones
# 3. Sentencias del programa principal

from math import sqrt


def cuadrado(x):
    return x **2

def suma_cuadrados(vector):
    suma = 0
    for elemento in vector:
        suma += cuadrado(elemento)
    return suma

# Programa Principal
mivector = []
for i in range(3):
    mivector.append(float(input('Ingresa un numero: ')))
s = suma_cuadrados(mivector)
print('Distanci al origen: ', sqrt(s))

#rectangulo
def area_rectangulo(altura, ancho):
    return altura * ancho

print(area_rectangulo(3, 4))