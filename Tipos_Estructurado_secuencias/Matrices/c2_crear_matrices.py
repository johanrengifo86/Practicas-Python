# Creación de una matriz 3 x 6
M = []
for i in range(3):
    M.append([0] * 6)
M[0][0] = 1
print(M)

# 239 Crea una Matriz identidad 4 x 4
Matriz = []
for fila in range (4):
    Matriz.append([0]*4)
Matriz[0][0] = 1
Matriz[1][1] = 1
Matriz[2][2] = 1
Matriz[3][3] = 1
print('-')
for i in range(0, 4):
    print(Matriz[i])

print(Matriz) 