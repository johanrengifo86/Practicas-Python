from turtle import Screen, Turtle
from math import sin, pi
import turtle

pantalla = Screen()
pantalla.setup(825, 425)
pantalla.screensize(800, 400)
pantalla.setworldcoordinates(-2*pi, -1, 2*pi, 1)

tortuga = Turtle()

x = -2 * pi
dx = 4*pi /800
tortuga.penup()
tortuga.goto(x, sin(x))
tortuga.pendown()
while x <= 2*pi:
    tortuga.goto(x,sin(x))
    x += dx

pantalla.exitonclick()


