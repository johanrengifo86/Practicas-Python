class Socio:
    def __init__(self, dni, nombre, telefono, direccion):
        self.dni = dni
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion

    def __str__(self):
        return 'DNI: {}\nNombre: {}\nTeléfono: {}\nDirección: {}\n'.format(self.dni, self.nombre, self.telefono,self.direccion)

class Pelicula:
    def __init__(self, titulo, genero):
        self.titulo = titulo
        self.genero = genero
        self.alquilada = None

    def __str__(self):
        cadena = 'Título: {}\nGénero: {}\n'.format(self.titulo, self.genero)
        if self.alquilada == None:
            cadena = cadena + 'Disponible\n'
        else:
            cadena = cadena + 'Alquilada a: {}\n'.format(self.alquilada)
        return cadena

class Videoclub:
    def __init__(self):
        self.socios = []
        self.peliculas = []

    def contiene_socio(self, dni):
        for socio in self.socios:
         if socio.dni == dni:
            return True
        return False

    def registrar_socio(self, socio):
        self.socios.append(socio)

    def eliminar_socio(self,dni):
        for i in range(len(self.socios)):
            if self.socios[i].dni == dni:
                del self.socios[i]
                break

    def contiene_pelicula(self, titulo):
        for pelicula in self.peliculas:
         if pelicula.titulo == titulo:
            return True
        return False

    def registrar_pelicula(self, pelicula):
        self.peliculas.append(pelicula)

    def eliminar_pelicula(self,titulo):
        for i in range(len(self.peliculas)):
            if self.peliculas[i].titulo == titulo:
                del self.peliculas[i]
                break
    
    def alquilar_pelicula(self, dni, titulo):
        for pelicula in self.peliculas:
            if pelicula.titulo == titulo: 
                if pelicula.alquilada == None:
                    pelicula.alquilada = dni
                    return True
                else:
                    return False
    
    def listado_por_genero(self, genero):
        for pelicula in self.peliculas:
            if pelicula.genero == genero and pelicula.alquilada == None:
                print(titulo)



    
def nuevo_socio():
    dni = input('DNI: ')
    nombre = input('Nombre: ')
    telefono = input('Teléfono: ')
    direccion = input('Dirección: ')
    return Socio(dni, nombre, telefono, direccion)

def nueva_pelicula():
    titulo = input('Título: ')
    genero = input('Género: ')
    return Pelicula(titulo, genero)


def menu():
    print('*** VIDEOCLUB ***')
    print('1) Registrar un nuevo Socio')
    print('2) Eliminar Socio')
    print('3) Registrar un nueva Película')
    print('4) Eliminar una película')
    print('5) Alquilar una Película')
    print('6) Salir')
    opcion = int(input('Elige una opción: '))
    while opcion < 1 or opcion > 5:
        opcion = int(input('Elige una opción: '))
    return opcion





videoclub = Videoclub()

opcion = menu()
while opcion != 6:

    if opcion == 1:
        print('Registro de Socio')
        socio = nuevo_socio()
        if videoclub.contiene_socio(socio.dni):
            print('Ya existe un socio registrado con ese DNI', dni)
        else:
            videoclub.registrar_socio(socio)
    
    if opcion == 2:
        print('Eliminar Socio')
        dni = input('DNI: ')
        if videoclub.contiene_socio(dni):
            videoclub.eliminar_socio(dni)
            print('Socio con DNI', dni, 'Ha sido eliminado')
        else:
            print('No existe ningún socio registrado con el DNI', dni)

    elif opcion == 3:
        print('Registrar Película')
        pelicula = nueva_pelicula()
        if videoclub.contiene_pelicula(pelicula, titulo):
            print('Ya existe un pelícual registrada con el título', pelicula.titulo)
        else:
            videoclub.registrar_pelicula(pelicula)

    elif opcion == 4:
        print('Eliminar Película')
        titulo = input('Título: ')
        if videoclub.contiene_pelicula(titulo):
            videoclub.eliminar_pelicula(titulo)
        else:
            print('No existe ninguna película con el título: ', titulo)
    
    elif opcion == 5:
        print('Alquiler de película')
        titulo = input('Título de la Película: ')
        dni = input('DNI del socio: ')
        hay_pelicula = videoclub.contiene_pelicula(titulo)
        hay_socio = videoclub.contiene_socio(dni)
        if hay_pelicula and hay_socio:
            if videoclub.alquilar_pelicula(titulo, dni):
                print('Alquiler Realizado.')
            else:
                print('La película no se encuentra disponible.')
        else: 
            if not hay_pelicula:
                print('No hay película con el título: ', titulo)
            if not hay_socio:
                print('No hay socio con el DNI: ', dni)






