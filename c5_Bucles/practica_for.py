'''
for i in ['primavera','verano','otoño', 'invierno']:
    print('Hola',  i, end='- ')
'''
''' 
contador = 0
email = False
miEmail = input('Introduce tu direccion de email: ')

for i in miEmail:
    if (i == '@' or i =='.'):
        contador += 1
        email = True
if email: # equivalente --> if email == True:
    print('Email es correcto.')
else:
    print('El email no es correcto.')
'''
## <range>
''' 
for i in range(5):
    print('Hola')
    print(i)
'''
# Notación para unir textos con variables
''' 
for i in range(4):
    print(f'Valor de la variable {i}')
'''
# range desde un numero inicial hasta uno final y el conteo
'''
for i in range(5, 19, 3):
    print(f'El valor de la variable {i}')
'''
# función len --> longitud del argumento
# validacion de email  con '@'
valido = False
email = input('Introduce emil: ')
for i in range(len(email)):
    if email[i] == '@':
        valido = True
if valido:
    print('Email correcto')
else:
    print('Email incorrecto.')