#=========================
# Función Filter
#======================
'''
* Verifica que los elementos de una secuencia cumplen una condición, devolviendo un iterador
  con los elementos que cumplen dicha condición.
'''
''' 
def numero_par(num):
    if num % 2 ==0:
        return True
'''
numeros = [17, 24, 7 , 39, 8, 51, 92]

#print(list(filter(numero_par, numeros)))

print(list(filter(lambda numero_par: numero_par%2==0, numeros)))
