#======================
# Generadores
#======================
# - Estructuras que extraen valores de una función y se almacenan
#   en objetos iterables(que se puedeen recorrer)
# - Estos valores se almacenan de uno en uno
# - Cada vez que un generador almacena un valor, este permanece en 
#   un estado pausado hasta que se solicita el siguiente. Esta caracaterística
#   es conocida como 'Suspención de estado'
#====================================================
# Utilidades 
# - Son más eficientes que las funciones tradicionales
# - Muy útiles con listas de valores infinitos
# - Bajo determinados escenarios, será muy útil que un generador
#   devuelva los valores de uno en uno.
#===============================================
# Función Tradicional
''' 
def generaPares(limite):
    numero = 1
    lista = []
    while numero < limite:
        lista.append(numero*2)
        numero += 1
    return lista

print(generaPares(10))
'''
# Función con Generador
def generaPares(limite):
    numero = 1
   
    while numero < limite:
        yield numero *2
        numero += 1
devuelvePares = generaPares(10)

#for par in devuelvePares:
 #   print(par)

print(next(devuelvePares))
print('Aquí podría ir más codigo....')
print(next(devuelvePares))
print('Aquí podría ir más codigo....')
print(next(devuelvePares))
