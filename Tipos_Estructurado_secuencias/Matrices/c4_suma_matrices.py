# Se pide la dimensión de las matrices
from random import randrange


m = int(input('Ingresa el número de filas: '))
n = int(input('Ingrese el número de columnas: '))

# Se crean las matrices nulas
A = []
for i in range(m):
    A.append([0] * n)

B = []
for j in range(n):
    B.append([0] * m)

# lectrua por teclado de los elementos de la matriz
print('Lectura de la Matriz A')
for i in range(m):
    for j in range(n):
        A[i][j] = float(input('Componente ( {}, {}): '.format(i, j)))

print('Lectura de la Matriz B')
for i in range(m):
    for j in range(n):
        B[i][j] = float(input('Componente ( {}, {}): '.format(i, j)))

# Se construye otra matriz para guardar el resultado
C = [] 
for i in range(m):
    C.append( [0] * n)

# Cálculo de la suma.
for i in range(m):
    for j in range(n):
        C[i][j] = A[i][j] + B[i][j]

# Muestra del resultado por pantalla
print('Suma')
for i in range(m):
    for j in range(n):
        print(C[i][j], end=' ')
    print()