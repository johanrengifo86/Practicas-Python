# Ejemplos de Listas 
'''
a = [1, 2, 3]
nombres = [' Johan', 'Camilo', 'Adrian', 'Olga', 'Alberto','Dayana', 'Christopher']
b = [1, 1+1, 6//2]
print(b, "\n",nombres[6])
'''
 # Operador de corte aplicado a las listas
'''
print(a[1:-1]) 
print(a[1:])
'''
# Asignación a <y> una copia de <x>
'''
x = [1, 2, 3] 
y = x[:]
print(y)
y = x +[]
print(y)
'''
# Recorrido de una lista con ciclco <for>
'''
for i in [1,2,3]:
    print(i)
for i in range(1,4):
    print(i)
'''
# Combinación de las funciones <list> y <range> para construir una lista de valores
a = list(range(1,4))
print(a)

print('Principio')
for i in []:
    print('paso', i)
print('y fin')

for i in [1] * 10:
    print(i)