# Matrices--> Son disposiciones bidimencionales de valore.
# e disponen en <filas> y <columnas>

M = [[1, 2, 3], [2, 12, 6], [1, 0, -3], [0, -1, 0]]
print(M[0][1]) # elemento que ocupa la celda de la fila 1 columna 2 

# Se utiliza una doble indexación para acceder a elementos de la matriz
# EL primer índice aplicado sobre M devuelve un componete de M, que es una lista
print(M[0])

# El segundo índice accede a un elemento de esa lista. que es un entero:
print(M[0][0])

# 235 Construye una matriz nula de 5 filas y 5 columnas
a = [0] * 5
a = [a] * 5
print(a)

# 236 construye una matriz identidad de 4 filas y 4 columnas

# 237 ¿Qué resulta de ejecutar este programa?

M = [ [1, 0, 0], [0, 1, 0], [0, 0, 1] ]
print(M[-1][0])
print(M[-1][-1])
print('-')
for i in range(0, 3):
    print(M[i])
print('-')
'''
for i in range(0, 3):
    for j in range(0, 3):
        print(M[i][j])
'''


# 238 ¿Qué resulta de este programa?
'''
N = [ [1, 0, 0], [0, 1, 0], [0, 0, 1]]
s = 0.0
for i in range(0, 3):
    for i in range(0, 3):
        s += N[i][j]
print(s / 9)
'''