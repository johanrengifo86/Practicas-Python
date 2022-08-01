filas = 10
columnas = 10

tablero = []
for i in range(filas):
    tablero.append([False] * columnas)

tablero[4][5] = True
tablero[5][5] = True
tablero[6][5] = True

# Representar el tablero
print('Estado Inicial')
for y in range(filas):
    for x in range(columnas):
        if tablero[y][x]:
            print('*', end='')
        else:
            print('.', end='')
    print()

pulsos = 6
for t in range(pulsos):
    # Preparar un nuevo tablero.
    nuevo = []
    for i in range(filas):
        nuevo.append([False]*columnas)
            
    # Atualizar el tablero
    for y in range(filas):
        for x in range(columnas):
            # Calcular el número de vecinos de la celda que se esta visitando
            n = 0
            if y > 0 and x > 0 and tablero[y-1][x-1]:
                 n += 1
            if x > 0 and tablero[ y ][x-1]:
                n += 1
            if y < filas-1 and x > 0 and tablero[y+1][x-1]:
                n += 1
            if y > 0 and tablero[y-1][ x ]:
                 n += 1
            if y < filas-1 and tablero[y+1][ x ]:
                 n += 1
            if y > 0 and x < columnas-1 and  tablero[y-1][x+1]:
                n += 1
            if x < columnas-1 and tablero[ y ][x+1]:
                 n += 1
            if y < filas-1 and x < columnas-1 and tablero[y+1][x+1]:
                n += 1
            # Aplicar las reglas.
            if tablero[y][x] and (n == 2 or n == 3): # Suppervivencia
                nuevo[y][x] = True
            elif not tablero[y][x] and n == 3: #Nacimiento
                nuevo[y][x] = True
            else: # Superopoblación y aislamiento
                nuevo[y][x] = False

    # Actualizar tablero.
    tablero = nuevo
    # Representar el tablero
    print('Pulso', t+1)
    for y in range(filas):
        for x in range(columnas):
            if tablero[y][x]:
                print('*', end='')
            else:
                print('.', end='')
        print()
