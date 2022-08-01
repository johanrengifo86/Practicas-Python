# Lee Positivos 

# Forma Ineficiente
'''
a = int(input('Ingresa un número Positivo: '))
while a < 0:
    print('Error: EL número debe ser positivo.')
    a = int(input('Ingresa un número positivo: '))

b = int(input('Ingresa un número Positivo: '))
while b < 0:
    print('Error: EL número debe ser positivo.')
    b = int(input('Ingresa un número positivo: '))

c = int(input('Ingresa un número Positivo: '))
while c < 0:
    print('Error: EL número debe ser positivo.')
    c = int(input('Ingresa un número positivo: '))
'''
# Ahorro de Tecleo mismo programa

def lee_entero_positivo(texto):
    numero = int(input(texto))
    while numero < 0:
        print('Error: El número ingresado debe ser Positivo.')
        numero = int(input(texto))
    return numero

a = lee_entero_positivo('Ingresa un número Positivo: ')
b = lee_entero_positivo('Ingresa otro número Positivo: ')
c = lee_entero_positivo('Ingresa otro número Positivo: ')
