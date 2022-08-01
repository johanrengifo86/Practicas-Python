from turtle import Screen, Turtle

def koch(tortuga, longitud, nivel):
    if nivel == 0:
        tortuga.forward(longitud)
    else:
        koch(tortuga, longitud/3, nivel-1)
        tortuga.left(60)
        koch(tortuga, longitud/3, nivel-1)
        tortuga.right(120)
        koch(tortuga, longitud/3, nivel-1)
        tortuga.left(60)
        koch(tortuga, longitud/3, nivel-1)

# El copo de koch se obtiene uniendo tres curvas de koch
# cada una girada 120 grados a la derecha de la anterior
def copo(tortuga, longitud, nivel):
    koch(tortuga, longitud, nivel)
    tortuga.right(120)
    koch(tortuga, longitud, nivel)
    tortuga.right(120)
    koch(tortuga, longitud, nivel)
   
pantalla = Screen()
pantalla.setup(500,500)
pantalla.screensize(500, 500)
pantalla.setworldcoordinates(0, -250, 500, 250)
tortuga = Turtle()
tortuga.speed(9)
#koch(tortuga, 400, 5)
copo(tortuga, 400, 3)
pantalla.exitonclick()

