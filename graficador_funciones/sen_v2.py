from turtle import Screen, Turtle
from math import sin, cos, pi

x1 = float(input('Ingresa el límite Inferior del Intervalo: '))
x2 = float(input('Ingresa el límite Superior del Intervalo: '))
puntos = int(input('Cuantos puntos desea Mostrar: '))

pantalla = Screen()
pantalla.setup(825, 425)
pantalla.screensize(800,400)
pantalla.setworldcoordinates(x1, -1, x2, 1)



tortuga_sin = Turtle()
tortuga_cos = Turtle()

x = x1
dx = (x2 - x1)/ puntos
tortuga_sin.penup()
tortuga_sin.goto(x, sin(x))
tortuga_sin.pendown()
tortuga_cos.penup()
tortuga_cos.goto(x, cos(x))
tortuga_cos.pendown()
while x <= x2:
    tortuga_sin.pencolor('blue')
    tortuga_sin.goto(x, sin(x))
    tortuga_cos.pencolor('red')
    tortuga_cos.goto(x, cos(x))
    
    x += dx
    
    

pantalla.exitonclick()

