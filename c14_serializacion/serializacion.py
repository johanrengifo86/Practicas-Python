#==========================================
# Serialización
#=======================================
# Bibliotecas necesarias
# * Pickle
#   - Método <dump()>: volcado de datos al fichero binario externo
#   - Método <load()>: carga de los datos del fichero binario externo
#===============================================================
import pickle
''' 
# Lista que se guardara en un fichero binario
lista_nombres = ['Pedro', 'Ana', 'María', 'Isabel']
fichero_binario = open('lista_nombres', 'wb')

# EL método dump() requiere dos argumentos < 1. Informacion que se quieres volcar, 2. fichero al que se quiere volcar
pickle.dump(lista_nombres, fichero_binario)
fichero_binario.close()
del(fichero_binario)
'''
# Recuperación del fichero previamente guardado 
# se crea un fichero en memoria y se abre en lectura binaria <rb>
fichero = open('lista_nombres', 'rb')

# La información del fichero a cargar se guarda en una variable
lista = pickle.load(fichero)

print(lista)
