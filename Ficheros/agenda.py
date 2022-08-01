def buscar_entrada(nombre, apellido):
    fichero = open('C:/Users/Stark/Documents/PracticasPython/Ficheros/agenda.txt', 'r')
    linea1 = fichero.readline()
    while linea1 != '':
        linea2 = fichero.readline()
        linea3 = fichero.readline()
        if nombre == linea1[:-1] and apellido == linea2[:-1]:
            fichero.close()
            return linea3[:-1]
        linea1 = fichero.readline()
    fichero.close()
    return None

def añadir_entrada(nombre, apellido, telefono):
    fichero = open('C:/Users/Stark/Documents/PracticasPython/Ficheros/agenda.txt', 'a')
    fichero.write(nombre + '\n')
    fichero.write(apellido + '\n')
    fichero.write(telefono + '\n')
    fichero.close()

def borrar_entrada(nombre, apellido):
    fichero = open('C:/Users/Stark/Documents/PracticasPython/Ficheros/agenda.txt', 'r')
    fcopia = open('C:/Users/Stark/Documents/PracticasPython/Ficheros/agenda.txt.copia', 'w')
    linea1 = fichero.readline()
    while linea1 != '':
        linea2 = fichero.readline()
        linea3 = fichero.readline()
        if nombre != linea1[:-1] or apellido != linea2[:-1]:
            fcopia.write(linea1)
            fcopia.write(linea2)
            fcopia.write(linea3)
        linea1 = fichero.readline()
    fichero.close()
    fcopia.close()
    
    fcopia = open('C:/Users/Stark/Documents/PracticasPython/Ficheros/agenda.txt', 'r')
    fichero = open('C:/Users/Stark/Documents/PracticasPython/Ficheros/agenda.txt', 'w')
    for linea in fcopia:
        fichero.write(linea)
    fcopia.close()
    fichero.close()

def menu():
    print('**** AGENDA ****')
    print('1) Buscar Contacto.')
    print('2) Añadir Contacto')
    print('3) Borrar Contacto')
    print('4) Salir.')
    opcion = int(input('Elige Una Opción: '))
    while opcion < 1 or opcion > 4:
        opcion = int(input('Elige una Opción: '))
    return opcion


opcion = menu()
while opcion != 4:
    
    if opcion == 1:
        print('Buscar Contacto.')
        buscar = buscar_entrada()

    if opcion == 2:
        print('Añadir Contacto.')
        añadir = añadir_entrada()
    
    if opcion == 3:
        print('Borrar Contacto.')
        borrar = borrar_entrada()

    opcion = menu()