contador = {}
print('Ve introduciendo líneas (línea vacía para acabar)')
linea = input('Línea: ')
while linea != '':
    palabras = linea.split()
    for palabra in palabras:
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1
    linea = input('Línea: ') 

# Obtenemos la lista de palabras diferentes 
palabras = list(contador.keys())
# Ordenamos la lista de palabras
palabras.sort()
# Recorremos la lista ordenada para mostrar cada contador
print('Se han encontrado las siguiente palabras: ')
for palabra in palabras:
    print('{} ({})'.format(palabra, contador[palabra]))