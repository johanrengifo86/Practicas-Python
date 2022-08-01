#================================
# Métodos Strings
#=================================
# upper() ---------> Convierte en mayusculas todas las letras de un string
# lower() ---------> Convierte en minsculas un string
# capitalize()-----> Poner la primera letra de un string en mayúscula
# count()----------> Cuenta cuantas veces aparece una letra o una cadena de caracteres 
# find() ----------> representa el indice o la posicion en la cual aparece un caracter
# isdigit() -------> dice si el valor introducido es un digito
# isalum() --------> comprueba si el valor introducido es alfanumerico
# isalpha() -------> comprueba si el valor introducido son solo letras
# split() ---------> separa por palabras utilizando espacios
# strip() ---------> borra espacios sobrantes al principio y al final 
# replace() -------> cambia una palabra o una letra por otra 
# rfind() ---------> representa el indice de un caracter contrando desde atras 
#=====================
'''
nombreUsuario = input('Introduce nombre de Usuario:')
print('EL nombre es: ', nombreUsuario.upper())
'''
edad = input('Introduce la edad: ')
while edad.isdigit() == False:
    print('Por favor, introduce un valor numerico.')
    edad = input('Introduce la edad: ')

if int(edad)< 18: 
    print('No puede pasar.')
else:
    print('Puedes pasar.')