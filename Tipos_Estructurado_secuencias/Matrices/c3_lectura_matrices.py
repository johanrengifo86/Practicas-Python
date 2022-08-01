# Pedimos dimension de la matriz
m = int(input('Ingrese el número de filas: '))
n = int(input('Ingrese el número de columnas: '))

# Se crea la matriz nula
M = []
for i in range(m):
    M.append([0] * n)

# Se lee su contenido por teclado
for i in range(m):
    for j in range(n):
        M[i][j] = float(input('Ingresa el componente {}, {}: '.format(i, j)))

print(M)
# Dimension de la matriz 

a = [[1, 2], [0, 1], [0, 0]]
print(len(a)) # número de filas
print(len(a[0])) # número de columnas
