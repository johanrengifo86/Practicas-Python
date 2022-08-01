# parametros
def incrementa(p):
    p = p + 1
    return p

a = 1
a = incrementa(2+2)
print('a: ', a)

# paso de listas
def modifica(a, b):
    a.append(4)
    b = b +[4]
    return b 

lista1 = [1, 2, 3]
lista2 = [1, 2, 3]

lista3 = modifica(lista1, lista2)

print(lista1)
print(lista2)
print(lista3)

# ejercicio parametros 
def modifica_parametros(x, y):
	x = 1 
	print(y)
	y.append(3)
	print(y)
	y = y +[4]
	print(y)
	y[0] = 10
	print(y)

a = 0
b = [0, 1, 2]
modifica_parametros(a, b)
print(a)
print(b)

#inversion 
def invierte(lista):
	for i in range(len(lista)//2):
		c = lista[i]
		#lista[i] = lista[len(lista)-1-i]
		#lista[len(lista)-1-i] = c 
		lista[i] = lista[-i-1]
		lista[-i-1] = c

a = [1, 2, 3, 4, 5, 6]
invierte(a)
print(a)

#abslista
def abs_lista(lista):
	for i in range(len(lista)):
		lista[i] = abs(lista[i])

milista = [1, -1, 2, -3, -2, 0]
abs_lista(milista)
print(milista)

# INtercambio
def intento_intercambio(a, b):
	aux = a 
	a = b 
	b = aux
	return (a, b)

lista1 = [1, 2]
lista2 = [3, 4]

intento_intercambio(lista1, lista2)
print(intento_intercambio(lista1, lista2))
print(lista1)
print(lista2)
