lista = [2, 4]
try:
    print(lista[1])
except IndexError:
    print('Error: error en el indice')
else:
    print('No hay Error')
finally:
    print('Se ejecutó')