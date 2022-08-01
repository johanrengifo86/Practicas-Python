#==================================
# PASO 1: Abrir fichero.
#=================================
fichero = open("C:/Users/Stark/Documents/PracticasPython/Ficheros/ejemplo.txt", "r")

#==================================
# PASO 2: Leer los datos del fichero.
#====================================
for linea in fichero:
    print(linea)

#==================================
# PASO 3: Cerrar fichero.
#====================================
fichero.close()
