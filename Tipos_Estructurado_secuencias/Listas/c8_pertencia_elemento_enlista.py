# Programa que, dados un elemento y una lista dice si 
# el elemento pertenece o no a la listra mostrando el 
# mensaje <<Pertenece>> o <<No Pertene>> en función del resultado

elemento = 5 
lista = [1, 4, 5, 1, 3, 8]

pertence = False
for i in lista:
    if elemento == i:
        pertence = True
        break

if pertence:
    print('Pertence')
else:
    print('No Pertenece')

# Ejemplo conjunto.py
conjunto = [1,2,3]
elemento = int(input('Ingresa un número: '))
if not elemento in conjunto:
    conjunto.append(elemento)
print(conjunto)

# Ejemplo equivalente conjunto.py
conjunto_a = [1,2,3]
elemento_a = int(input('Ingresa un número: '))
if elemento_a not in conjunto_a:
    conjunto_a.append(elemento_a)
print(conjunto_a)