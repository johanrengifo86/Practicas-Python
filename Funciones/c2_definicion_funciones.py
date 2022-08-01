# Se podria leer el programa como << define cuadrado de x como el valor que
# resulta de elevar x al cuadrado>>
def cuadrado(x):
    return x **2 
print(cuadrado(2))

a = 1 + cuadrado(3)
print (a)
print(cuadrado(a*3))

# 252 Definir una función que se llame raíz_cúbica

def raiz_cubica(valor):
    return(valor**(1/3))

print(raiz_cubica(27))

# 253 Define una función llamada área_círculo, a partir del radio de un circulo
from math import pi

def area_circulo(radio):
    return (pi * (radio**2) )

print(area_circulo(20))

# 254 Define una función que convierte grados Farenheit en grados centígrados

def gradosFarenheit_a_centigrados(grados):
    return (grados - 32) * (5/9)

print(gradosFarenheit_a_centigrados(39))

# Mayoria Edad
def es_mayor_edad(edad):
    if edad >= 18:
        return True
    else:
        return False

# Número perfecto
def es_perfecto(numero):
    suma_numero = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma_numero += i
    return suma_numero == numero

print(es_perfecto(28))

# Función que recibe una lista de números y devuelve el mayor elemento.
def maximo(lista):
    if len(lista) > 0:
        candidato = lista[0]
        for elemento in lista:
            if elemento > candidato:
                candidato = elemento
    else:
        candidato = None
    return candidato
    

