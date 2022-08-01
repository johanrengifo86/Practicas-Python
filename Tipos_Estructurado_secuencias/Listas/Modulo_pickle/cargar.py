import pickle

# Leemos la lista cargandola del fichero mifichero.mio
lista = pickle.load(open('mifichero.mio', 'rb'))
# y se muestra por pantalla
print(lista)