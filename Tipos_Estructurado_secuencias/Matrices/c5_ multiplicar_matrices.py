# Se pide la dimensión de la primera matriz y el numero de columnas de la segunda
p = int(input('Ingresa el número de filas de A: '))
q = int(input('Ingresa el número de columnas de A (y Filas de B): '))
r = int(input('Ingresa el número de columnas de B: '))

# Se crean las matrices nulas
A = []
for i in range(p):
    A.append( [0] * q)

B = []
for i in range(q):
    B.append( [0] * r)

# Se leen su contenidos por teclado
print('Lectura de la matriz A')
for i in range(p):
    for j in range(q):
        A[i][j] = float(input('Componente ({}, {}): '.format(i,j)))

print('Lectura de la matriz B')
for i in range(q):
    for j in range(r):
        B[i][j] = float(input('Componente ({}, {}): '.format(i,j)))

# Se crea la matriz nula para el resultado
C = []
for i in range(p):
    C.append( [0] * r)

# Se efectua el cálculo del producto
for i in range(p):
    for j in range(r):
        for k in range(q):
            C[i][j] += A[i][k] * B[k][j]

# Muestra del resultado por pantalla
print('Multiplicación')
for i in range(p):
    for j in range(r):
        print(C[i][j], end=' ')
    print()