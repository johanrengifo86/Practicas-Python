'''cadena = input('Escribe una frase: ')
while cadena != '':
    blancos = 0
    for caracter in cadena:
        if caracter == ' ':
            blancos += 1
    palabras = blancos + 1 # Hay una palabra más que blancos
    print('Palabras: ', palabras)

    cadena = input ('Escribe Una frase: ')
 '''
'''
cadena = input('Escribe una frase: ')
while cadena != '':
    cambios = 0
    anterior = ''
    for caracter in cadena:
        if caracter == ' ' and anterior != ' ':
            cambios += 1
        anterior = caracter
    palabras = cambios + 1 # Hay una palabra más que cambios de no blanco a blanco
    print('Palabras: ', palabras)

    cadena = input ('Escribe Una frase: ')
 '''
cadena = input('Escribe una frase: ')
while cadena != '':
    cambios = 0
    anterior = ' ' # Evita que cuente un espacio en blanco al inicio de la frase
    for caracter in cadena:
        if caracter == ' ' and anterior != ' ':
            cambios += 1
        anterior = caracter

    if cadena[-1] == ' ':
        cambios -= 1

    palabras = cambios + 1 # Hay una palabra más que cambios de no blanco a blanco
    print('Palabras: ', palabras)

    cadena = input ('Escribe Una frase: ')