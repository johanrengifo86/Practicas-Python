'''
def area_triangulo(base, altura):
    return(base * altura)/2

triangulo1 =  area_triangulo(5,7)
triangulo2 = area_triangulo(9, 6)

print(triangulo1, triangulo2)
'''

area_triangulo = lambda base, altura:(base*altura)/2

triangulo1 = area_triangulo(7,5)
trinagulo2 = area_triangulo(9,6)

print(triangulo1, trinagulo2)


al_cubo = lambda numero: pow(numero, 3)

destaca_valor = lambda comision:"¡{}! $".format(comision)

comision_Ana = 15584

print(destaca_valor(comision_Ana))