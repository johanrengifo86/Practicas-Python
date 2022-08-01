from traceback import print_tb


lista=['María', 'Pepep', 'Marta','Antonio']
# Imprimir Lista COmpleta
print(lista)

# Imprimir un elemento
print(lista[2])

# Porcion de Lista
print(lista[0:3]) # --> incluye los indices desde 0 hasta el indice de la posición 2 
print(lista[2:]) # --> Accede a los elemento de la poscion 2 en adelante

# Agregar elementos a las lista 
lista.append('Sandra')
print(lista)

# Agregar un elemento en un indice determinado 
lista.insert(2,'Pedro') 
print(lista)

# Agregar varios elementos a una lista
lista.extend(['Sandra', 'Ana', 'Lucia'])
print(lista)

# Devolver el indice donde se encunetra un elemento 
print(lista.index('Antonio'))

# Comprobar si un elemento se encuentra en la lista 
print('Pepe' in lista)

# Eliminar elementos 
lista.remove('Ana')
print(lista)

# Eliminar el último elemento de una lista 
lista.pop()
print(lista)
