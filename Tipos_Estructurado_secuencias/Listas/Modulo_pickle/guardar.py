import pickle

# Creamos una lista
lista = [1, 2, 3, 4]
#guardamos en un fichero llamado mifichero.mio
pickle.dump(lista, open('mifichero.mio','wb'))
