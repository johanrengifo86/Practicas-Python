# función que devuelve el mínimo y máximo de 3 números
def minmax(a, b ,c) :
    # Calcular el mínimo
    if a < b:
        if a < c:
            min = a 
        else:
            min = c
    else:
        if b < c:
            min = b
        else:
            min = c

    # Calcular el máximo
    if a > b:
        if a > c:
            max = a 
        else:
            max = c
    else:
        if b > c:
            max = b
        else:
            max = c

    return[min, max]

# opción 2
a = minmax(2,1,6)
print('El mínimo es: ', a[0])
print('El máximo es: ', a[1])

# opción 3
[minimo, maximo] = minmax(10,2,5)
print('El mínimo es: ', minimo)
print('El máximo es: ', maximo)

a = 1
b = 2
[a,b] = [b,a]
print(a,b)
