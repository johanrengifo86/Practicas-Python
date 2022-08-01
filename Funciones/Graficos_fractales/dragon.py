from turtle import Screen, Turtle
from math import sqrt

def dragon(tortuga, longitud, nivel):
    if nivel == 0:
        tortuga.forward(longitud)
    else:
        tortuga.right(45)
        dragon(tortuga, longitud, nivel-1)
        tortuga.left(90)
        nogard(tortuga, longitud/sqrt(2), nivel-1)
        tortuga.right(45)

def nogard(tortuga, longitud, nivel):
    if nivel == 0:
        tortuga.forward(longitud)
    else:
        tortuga.left(45)
        dragon(tortuga, longitud/sqrt(2), nivel-1)
        tortuga.right(90)
        nogard(tortuga, longitud/sqrt(2), nivel-1)
        tortuga.left(45)

pantalla = Screen()
pantalla.setup(500,500)
pantalla.screensize(500, 500)
pantalla.setworldcoordinates(0, -250, 500, 250)
tortuga = Turtle()
tortuga.speed(9)
dragon(tortuga, 20, 11)
pantalla.exitonclick()

