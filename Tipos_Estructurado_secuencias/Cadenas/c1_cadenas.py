'''print('\\n')
print('\157\143\164\141\154')
print('\t\tuna\bo')
'''

# Programa que lee por teclado un numero de DNI y muestra en pantalla
# la letra que le corresponde 
dni = int(input("Ingrese el valor del DNI: "))
cad = "REWAGMYFPDXBNJZSQVHLCKE"
print('La letra del DNI es: ', cad[dni %23])




