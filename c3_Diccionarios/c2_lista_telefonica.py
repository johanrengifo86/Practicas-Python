class Lista:
    def __init__(self):
        self.lista = {}
    
    def añadir(self, nombre, telefono):
        if nombre in self.lista:
            if not telefono in self.lista[nombre]:
                self.lista[nombre].append(telefono)
        else:
            self.lista[nombre] = [telefono]

    def consultar(self, nombre):
        if nombre in self.lista:
            return self.lista[nombre]
        else:
            return []

    def eliminar(self, nombre):
        if nombre in self.lista:
            del self.lista[nombre]
# Fin del la Clase

def menu():
    opcion = 0
    while opcion < 1 or opcion > 4:
        print('1) Añadir Teléfonos')
        print('2) Consultar Lista.')
        print('3) Elimiar Persona de la Lista.')
        print('4) Salir')
        opcion = int(input('Escoge una opción: '))
    return opcion

# Programa Principal
lista = Lista()

opcion = 0
while opcion != 4:
    opcion = menu()
    if opcion == 1:
        nombre = input('Nombre: ')
        telefono = input('Teléfono: ')
        lista.añadir( nombre, telefono)
        mas = input(' ¿ Desea añadir otro teléfono a {} (s/n)?: '\
                    .format(nombre))
        while mas == 's':
            telefono = input('Teléfono: ')
            lista.añadir( nombre, telefono)
            mas = input(' ¿ Desea añadir otro teléfono a {} (s/n)?: '\
                        .format(nombre))
    elif opcion == 2:
        nombre = input('Nombre: ')
        telefonos = lista.consultar( nombre)
        for telefono in telefonos:
            print(telefono)
    elif opcion == 3:
        nombre = input('Nombre: ')
        lista.eliminar(nombre)

    