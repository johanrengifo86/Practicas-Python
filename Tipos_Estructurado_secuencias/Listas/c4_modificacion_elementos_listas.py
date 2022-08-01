# Se pueden asignar valores a elementos particulares gracias al 
# operador de indexacion
'''
a = [1,2,3]
a[1] = 10
print(a)
'''
# 215 Programa que almacena en una variable 'a' la lista obtenida
# mediante <list(range(1,4))> y a continuacion la modifique
#para que cada componente sea igual al cuadrado del original
# el programa mostrara el resultado por pantalla
''' 
a = list(range(1,4))
print('Lista Nomal: ',a)
for i in range(0,len(a)):
   a[i] = a[i]**2    
print('Lista Elevada al Cuadrado: ',a)
'''
#216 Programa que almacene en a una lista obtenida con <list(range(1,n))>, donde
# n es un entero que se pide al usuario, y modifique dicha lista para que cada
# componente sea igual al cuadrado del componente original.
# El programa mostrará la lista resultante por pantalla.
''' 
n = int(input('Ingrese el valor de n: ')) 
a = list(range(1,n))
print('Lista Normal: ',a)
for i in range(0, len(a)):
   a[i] = a[i]**2
print('Lista Elevada al Cuadrado', a)
'''
# 217 Programa que dada una lista 'a' cualquiera, sustituya cualquier elemento por cero
''' 
a = [-2, 3, 4, 10, -15]
for num in range(0, len(a)):
   print(a[num])
   if a[num] < 0:
      a[num] = 0
print('Lista: ',a)
'''
# 218 ¿Qué mostrará el siguiente programa ?
a = list(range(0, 5))
b = list(range(0, 5))
c = a
d = b[:]
e = a + b
f = b[:1]
g = b[0]
c[0] = 100
d[0] = 200
e[0] = 300
print('a = ', a,'\nb = ', b,'\nc = ', c,'\nd = ', d,'\ne = ', e,'\nf = ', f,'\ng = ', g)



