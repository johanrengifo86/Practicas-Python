#===============
#Continue
#===============
# Salta a la siguiente iteración de bucle.
import email

from matplotlib.pyplot import bar_label


for letra in 'python':

    if letra =='h':
        continue
    print('viendo la letra: ' + letra )
    
# Contador de letras ignorando el espacio en blanco
nombre = 'un canchito feliz'
contador = 0

for i in nombre:
    if i == ' ':
        continue
    contador += 1

print(contador)

#===========================
# Pass
#===========================
''' 
while True:
    pass 

class MiClase:
    pass
'''
#==========================
# Else
#=========================
email = input('Introduce tu email, por favor: ')
for i in email:
    if i == '@':
        arroba = True
        break
else:
    arroba = False
print(arroba) 