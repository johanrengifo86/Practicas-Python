
from tkinter import N


def numeros ():
    n = 1
    while True:
        yield n # detiene la ejecucion de la funcion
        n = n+1

i = numeros
print(i)
print(i.__next__())
print(i.__next__())