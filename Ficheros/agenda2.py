#===========================================
# Clase Ingreso
#===========================================
class Ingreso:
    def __init__(self, nombre, apellido, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono

#=============================================
# Clase Agenda
#=============================================
class Agenda:
    def __init__(self):
        self.lista = []

    def buscar_telefono(self,nombre, apellido):
        for ingreso in self.lista:
            if ingreso.nombre == nombre and ingreso.apellido == apellido:
                return ingreso.telefono
        return None
    
    def añadir_ingreso(self, ingreso):
        self.lista.append(ingreso)
    
    def borrar_ingreso(self, nombre, apellido):
        for i in range(len(self.lista)):
            if self.lista[i].nombre == nombre and self.lista[i].apellido == apellido:
                del self.lista[i]
                return
#===============================================
# Funciones
#===============================================
def lee_ingreso():
    nombre = input('Nombre: ')
    apellido = input('Apellido: ')
    telefono = input('Teléfono: ')
    return Ingreso(nombre, apellido, telefono)

def cargar_agenda():
    agenda = Agenda()
    fichero = open('C:/Users/Stark/Documents/PracticasPython/Ficheros/agenda.txt', 'r')
    linea1 = fichero.readline()
    while linea1 != '':
        linea2 = fichero.readline()
        linea3= fichero.readline()
        ingreso = Ingreso(linea1[:-1], linea2[:-1], linea3[:-1])
        agenda.añadir_ingreso(ingreso)
        linea1 = fichero.readline()
    fichero.close()
    return agenda

def guardar_agenda(agenda):
    fichero = open('C:/Users/Stark/Documents/PracticasPython/Ficheros/agenda.txt', 'w')
    for ingreso in agenda.lista:
        fichero.write(ingreso.nombre + '\n')
        fichero.write(ingreso.apellido + '\n')
        fichero.write(ingreso.telefono + '\n')
    fichero.close()

#=======================================================
# Menú de Usuario
#=======================================================
def menu():
    print('**** AGENDA ****')
    print('1) Añadir Contacto ')
    print('2) Buscar Contacto.')
    print('3) Borrar Contacto')
    print('4) Salir.')
    opcion = int(input('Elige Una Opción: '))
    while opcion < 1 or opcion > 4:
        opcion = int(input('Elige una Opción: '))
    return opcion

#======================================================
# Programa Principal
#======================================================
agenda = cargar_agenda()

opcion = menu()
while opcion != 4:
    if opcion == 1:
        print('Añadir Contacto.')
        ingreso = lee_ingreso()
        agenda.añadir_ingreso(ingreso)
    elif opcion == 2:
        print('Buscar Contacto.')
        nombre = input('Nombre: ')
        apellido = input('Apellido: ')
        telefono = agenda.buscar_telefono(nombre, apellido)
        if telefono == None:
            print('EL contacto No esta en la Agenda.')
        else:
            print('Teléfono: ', telefono)
    elif opcion == 3:
        nombre = input('Nombre: ')
        apellido = input('Apellido: ')
        agenda.borrar_ingreso(nombre, apellido)
    opcion = menu()

guardar_agenda(agenda)

