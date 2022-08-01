from random import randrange
from turtle import Screen, Turtle
from time import sleep

from matplotlib.pyplot import table

CeldaCerrada = 0
CeldaAbierta = 1
CeldaTemporalmenteAbierta = 2

def crea_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        matriz.append([None] * columnas)
    return matriz

# Tercera Versión
def rellena_simbolos(simbolo):
    numsimbolo = 0
    for i in range(len(simbolo)):
        for j in range(len(simbolo[0])):
            simbolo[i][j] = chr(ord('a') + numsimbolo // 2)
            numsimbolo += 1

    for i in range (1000):
        [f1, c1] = [randrange(len(simbolo)), randrange(len(simbolo[0]))]
        [f2, c2] = [randrange(len(simbolo)), randrange(len(simbolo[0]))]
        tmp = simbolo[f1][c1]
        simbolo[f1][c1] = simbolo[f2][c2]
        simbolo[f2][c2] = tmp

def inicializa_tablero(tablero):
    for i in range(len(tablero)):
        for j in range(len(tablero[0])):
            tablero[i][j] = CeldaCerrada

def dibuja_tablero(tablero, simbolo):
    for i in range(len(simbolo)):
        for j in range(len(simbolo[0])):
            dibuja_celda(tablero, simbolo, i, j)

def dibuja_celda(baldosa, simbolo, i , j):
    global tortuga
    tortuga.penup()
    tortuga.goto(j+5, i)
    tortuga.begin_fill()  # Inicia un polígono relleno
    if baldosa[i][j] == CeldaCerrada:
        tortuga.fillcolor('blue') # Hace que le color de relleno sea el especificado 
        tortuga.circle(5)
    elif baldosa[i][j] == CeldaAbierta:
        tortuga.fillcolor('white')
        tortuga.circle(5)
        tortuga.goto(j+5, i+25)
        tortuga.write(simbolo[i][j])
    else:
        tortuga.fillcolor('yellow')
        tortuga.circle(5)
        tortuga.goto(j+5, i+25)
        tortuga.write(simbolo[i][j])
    tortuga.end_fill() # Rellena el polígono iniciado con tortuga.begin_fill()
    tortuga.pendown

def clic(x, y):
    global pantalla, tablero, simbolo, temporal1, temporal2
    pantalla.onclick(None)
    [j, i] = [int(x), int(y)]
    #print('Clic en fila {} y columna {}'.format(i, j))
    if 0 <= i < len(tablero) and 0 <=j < len(tablero[0]):
        if tablero[i][j] == CeldaCerrada:
            if temporal1 == None:
                temporal1 = [i, j]
                tablero[i][j] = CeldaTemporalmenteAbierta
            else:
                temporal2 = [i,j]
                tablero[i][j] = CeldaTemporalmenteAbierta
            dibuja_celda(tablero, simbolo, i, j)
            if temporal2 != None:
                if simbolo[temporal1[0]][temporal1[1]] \
                    == simbolo[temporal2[0]][temporal2[1]]:
                    tablero[temporal1[0]][temporal1[1]] = CeldaAbierta
                    tablero[temporal2[0]][temporal2[1]] = CeldaAbierta
                else:
                    sleep(0.5)
                    tablero[temporal1[0]][temporal1[1]] = CeldaCerrada
                    tablero[temporal2[0]][temporal2[1]] = CeldaCerrada
                dibuja_celda(tablero, simbolo, temporal1[0], temporal1[1])
                dibuja_celda(tablero, simbolo, temporal2[0], temporal2[1])
                temporal1 = None
                temporal2 = None
        dibuja_celda(tablero, simbolo, i, j)

    if todas_abiertas(tablero):
        pantalla.bye()
    else:
        pantalla.onclick(clic)

def todas_abiertas(tablero):
    for i in range(len(tablero)):
        for j in range(len(tablero[0])):
            if tablero[i][j] == CeldaCerrada:
                return False
    return True

# Programa Principal
filas = 4 
columnas = 6

pantalla = Screen()
pantalla.setup(columnas*50, filas*50)
pantalla.screensize(columnas*50, filas*50)
pantalla.setworldcoordinates(-5, -5, columnas+5, filas+5)
pantalla.delay(0)
tortuga = Turtle()
tortuga.hideturtle()
simbolo = crea_matriz(filas, columnas)
tablero = crea_matriz(filas, columnas)

temporal1 = None
temporal2 = None
inicializa_tablero(tablero)
rellena_simbolos(simbolo)
dibuja_tablero(tablero, simbolo)

pantalla.onclick(clic)

pantalla.mainloop()






 # Primera versión
'''
def rellena_simbolos(simbolo): 
    for caracter in 'abcdefghijkl':
        for ejemplar in range(2):
            ocupado = True 
            while ocupado:
                [i, j] = [randrange(len(simbolo)), randrange(len(simbolo[0]))]
                if simbolo [i, j] == None:
                    ocupado = False
            simbolo[i][j] = caracter
'''
# Segunda versión
'''
def rellena_simbolos(simbolo):
    lista = []
    for i in range(len(simbolo)):
        for j in range(len(simbolo[0])):
            lista.append( [i, j])

    for i in range(1000):
        [i, j] = [randrange(len(simbolo)), randrange(len(simbolo[0]))]
        aux = lista[i]
        lista[i] = lista[j]
        lista[j] = aux

        i = 0
        for coords in lista:
            simbolo[coords[0]][coords[1]] = 'abcdefghijkl'[i//2]
        i += 1
'''

