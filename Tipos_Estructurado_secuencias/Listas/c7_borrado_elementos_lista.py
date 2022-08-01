# Para borrar elementos de utiliza la expersion <del>
'''
a = [1, 2, 3]
del a [1]
print(a)
'''
# Programa que borra números negativos de una lista 
''' 
a = [1, 2, -1, -4, 5, -2]

i = 0
while i < len(a):
    if a[i] < 0:
        del a[i]
    else:
        i +=1

print(a)
'''
#a = list(range(0, 5))
#del a[1]
#del a[1]
#print(a)

# 224 --> Programa que elimina de una lista todos los elementdo de índice par
# y muestra por pantalla el resultado


# 225 --> Programa que elimina de una lista todos los elementos de valor par 
# y muestra por pantalla el resultado
lista = [1, 2, 1, 4, 0, 3]

i = 0
while i < len(lista):
    if lista[i] % 2 == 0:
       print(i,":",lista[i])
       del lista[i]
    else:
        i += 1

print(lista)

