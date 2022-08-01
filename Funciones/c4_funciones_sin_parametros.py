# leer entero
def lee_entero():
    return int(input())

a = lee_entero()

# función que dice si el número es par
def es_par(n):
    return n % 2 == 0

# función que lee un número por teclado y se asegura que es positivo
def lee_entero_positivo():
    numero = int(input())
    while numero < 0 :
        print('Error: El número debe ser positivo.')
        numero = int(input())
    return numero

b = lee_entero_positivo() 

# función menú 
def menu():
    opcion = ''
    while not (opcion >= 'a' and opcion <= 'c'):
        print('Cajero Automático.')
        print('a) Ingresar Dinero.')
        print('b) Retirar Dinero.')
        print('c) Consultar Saldo.')
        opcion = input('Escoja un Opción: ')
        if not (opcion >= 'a' and opcion <= 'c'):
            print('Solo puede escoger entre las opciones a, b, c. Inténto de nuevo.')
    return opcion