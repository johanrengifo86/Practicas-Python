# Método burbuja
from tkinter.tix import ListNoteBook


lista = [2, 26, 4, 3, 1]

for i in range(1, len(lista)): # Bucle que hace len(lista)-1 pasadas
    print('Pasada', i)
    for j in range(0, len(lista)-i):
        print('  Comparación de lista [{}] y lista [{}]'.format(j, j+1))
        if lista[j] > lista[j+1]:
            elemento = lista[j]
            lista[j] = lista[j+1]
            lista[j+1] = elemento
            print('  Se intercambian')
        print('  Estado actual de la lista', lista)
        
print(lista)