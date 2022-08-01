# El operador <is> devuelve <True> si dos objetos
# residen en la misma zona de memoria en caso contrario devuelve <false>
'''
a = [1,2,3]
b = [1,2,3]
c = a 
print(a is b)
print(a is c)

print(a is a)
print(a + [] is a)
print(a + [] == a)

print( (a[0] is b[0])  and (a[1] is b[1])  and (a[2] is b[2]))
'''
# 213 pag 189 QUe ocurrira al ejecutar estas ordenes Python
'''
print( [1,2] == [1,2])
print( [1,2] is [1,2])
a = [1,2,3]
b = [a[0], a[1], a[2]]
print(a == b)
print(a is b )
print(a[0] == b[1])
print(b is [b[0], b[1], b[2]])
'''
# 214 Que se muestra por pantalla como respuesta a cada una de las sentencias Python
a = [1,2,3,4,5]
b = a[1:3]
print('b = ',b)
c = a 
print('c = ',c)
d = a[:]
print('d = ',d)
print(a == c)
print(c == d)
print(a == b)
print(a is c)
print(a is d)
print(c is d)
print(a is b)
