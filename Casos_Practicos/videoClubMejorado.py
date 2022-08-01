#==============================================
# VideoCLub
#==============================================
# Programa para la gestión de videoclubs
#==============================================

from unittest import result
from fecha import Fecha, lee_fecha

#----------------------------------------------------------
# Socio
#----------------------------------------------------------
# Clase para almacenar los datos relativos a un socio
#----------------------------------------------------------
class Socio:
    def __init__(self, dni, nombre, telefono, direccion):
        self.dni = dni
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion

    def __str__(self):
        return 'DNI: {}\nNombre: {}\nTeléfono: {}\nDirección: {}\n' \
            .format(self.dni, self.nombre, self.telefono,self.direccion)

#----------------------------------------------------------------
# Pelicula
#----------------------------------------------------------------
# Clase para almacenar los datos relativos a un ejemplar de una
# película
#----------------------------------------------------------------
class Pelicula:
    def __init__(self, titulo, genero, dias_permitidos):
        self.titulo = titulo
        self.genero = genero
        self.alquilada = None
        self.fecha_alquiler = None
        self.dias_permitidos = dias_permitidos

    def __str__(self):
        cadena = 'Título: {}\nGénero: {}\n'.format(self.titulo, self.genero)
        if self.alquilada == None:
            cadena = cadena + 'Disponible\n'
        else:
            cadena = cadena + 'Alquilada a: {}\n'.format(self.alquilada)
        return cadena

#----------------------------------------------------------------------
# Videoclub
#----------------------------------------------------------------------
# Almacena dos listas: una de socios y otra de películas. Los
# elementos de la primera lista don de la clase Socio, y los de la 
# segunda, de la clase Película.
#----------------------------------------------------------------------
class Videoclub:
    def __init__(self):
        self.socios = []
        self.peliculas = []

    def contiene_socio(self, dni):
        # Devuelve True si existe algún socio con DNI ingresado
        # y False en caso contrario
        for socio in self.socios:
         if socio.dni == dni:
            return True
        return False

    def registrar_socio(self, socio):
        # Añade un soscio a la lista de socios
        # Requisito: no debe exixtir ningún socio con el mismo DNI
        self.socios.append(socio)

    def eliminar_socio(self,dni):
        # Elimina al socio cuyo DNI es igual a dni.
        # Requisito: debe existir in socio con ese DNI.
        for i in range(len(self.socios)):
            if self.socios[i].dni == dni:
                del self.socios[i]
                break

    def contiene_pelicula(self, titulo):
        for pelicula in self.peliculas:
         if pelicula.titulo == titulo:
            return True
        return False

    def registrar_pelicula(self, pelicula, ejemplares):
        # Registra un número dado de ejemplares de una película.
        for i in range(ejemplares):
            nuevo_ejemplar = Pelicula(pelicula.titulo, pelicula.genero, \
                                      pelicula.dias_permitidos)
            self.peliculas.append(nuevo_ejemplar)

    def eliminar_pelicula(self,titulo, ejemplares):
        # Elimina una número de ejemplares de la película cuyo título nos
        # es suministrado como argumento. Devuelve el número de ejemplares que 
        # se elimino efectivamente
        eliminaciones_efectivas = 0
        i = 0
        while i < len(self.peliculas):
            if self.peliculas[i].titulo == titulo and self.peliculas[i].alquilada == None:
                del self.peliculas[i]
                eliminaciones_efectivas += 1
            else:
                i += 1
        return eliminaciones_efectivas
    
    def alquilar_pelicula(self, dni, titulo):
        # Alquila un ejemplar de la película cuyo título es indicado, al socio
        # con DNI dni. Si no consigue efectuar el alquiler, devuelve False, y True
        # si lo consigue. La fecha del alquiler se fija automáticamente al día actual
        # Requisito: debe existir un socio con DNI suministrado.
        for pelicula in self.peliculas:
            if pelicula.titulo == titulo: 
                if pelicula.alquilada == None:
                    pelicula.alquilada = dni
                    pelicula.fecha_alquiler = hoy
                    return True       
        return False

    def devolver_pelicula(self, titulo, dni):
        # Devuelve un ejemplar de la película cuyo título nos indica que 
        # estaba alquilada al socio con DNI dni. Devuelve el número de días
        # de retraso o -1 si ningún ejemplar de la película está alquilado
        # al socio.
        # Requisito: debe existir un socio con el DNI suministrado.
        for pelicula in self.peliculas:
            if pelicula.titulo == titulo and pelicula.alquilada == dni:
                pelicula.alquilada = None
                dias_retraso = pelicula.fecha_alquiler.dias_transcurridos(hoy)
                return dias_retraso
        return -1
    
    def listado_por_genero(self, genero):
        # Muestra un listado de las películas cuyo género es el indicado.
        # Cada título aparece solo una vez. Al lado del título aparece 
        # una indicación sobre si hay o no hay ejemplares disponibles para 
        # alquiler.
        disponibles = []
        alquiladas = []
        for pelicula in self.peliculas:
            if pelicula.genero == genero: 
                if pelicula.alquilada == None and not (pelicula.titulo in disponibles):
                    disponibles.append(pelicula.titulo)
            if pelicula.alquilada != None and not(pelicula.titulo in alquiladas):
                alquiladas.append(pelicula.titulo)
        for titulo in disponibles:
            print(titulo, 'DISPONIBLE')
        for titulo in alquiladas:
            if not (titulo in disponibles):
                print(titulo, 'NO DISPONIBLE')

#--------------------------------------------------------
# Funciones
#--------------------------------------------------------               

def menu():
    # Muestra el menú por pantalla y lee un opción de teclado, que es el 
    # resultado devuelto.
    # La función se asegura de que la opción leida esté entre 0 y 8.
    print('*** VIDEOCLUB ***')
    print('1) Registrar un nuevo Socio')
    print('2) Eliminar Socio')
    print('3) Registrar un nueva Película')
    print('4) Eliminar una película')
    print('5) Alquilar una Película')
    print('6) Devolver Película')
    print('7) Listado por Género')
    print('8) Salir')
    opcion = int(input('Elige una opción: '))
    while opcion < 1 or opcion > 8:
        opcion = int(input('Elige una opción (0 y 8): '))
    return opcion

def nuevo_socio():
    # Pide por teclado los datos de un nuevo socio y devuelve un objeto 
    # de la clase Socio.
    dni = input('DNI: ')
    nombre = input('Nombre: ')
    telefono = input('Teléfono: ')
    direccion = input('Dirección: ')
    return Socio(dni, nombre, telefono, direccion)

def nueva_pelicula():
    # Pide por teclado los datos de una nueva película y devuelve un objeto 
    # de la clase Pelicula.
    titulo = input('Título: ')
    genero = input('Género: ')
    dias_permitidos = input('Días Permitidos: ')
    return Pelicula(titulo, genero, dias_permitidos)

#-------------------------------------------------------------------------
# Programa principal
#-------------------------------------------------------------------------

# Fijar Fecha actual
hoy = lee_fecha()

videoclub = Videoclub()

opcion = menu()
while opcion != 8:

    if opcion == 0:
        print('Cambiar fecha actual')
        hoy = lee_fecha()

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
        ejemplares = int(input('Ejemplares: '))
        videoclub.registrar_pelicula(pelicula, ejemplares)

    elif opcion == 4:
        print('Eliminar Película')
        titulo = input('Título: ')
        ejemplares = int(input('Ejemplares: '))
        eliminados = videoclub.eliminar_pelicula(titulo, ejemplares)
        if eliminados < ejemplares:
            print('Solo puede eliminar ', eliminados, 'ejemplares' )
        else:
            print('Operación realizada ')
    
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
    
    elif opcion == 6:
        print('Devolver película')
        titulo = input('Título de la Película: ')
        dni = input('DNI del socio: ')
        hay_pelicula = videoclub.contiene_pelicula(titulo)
        hay_socio = videoclub.contiene_socio(dni)
        if hay_pelicula and hay_socio:
            resultado = videoclub.devolver_pelicula(titulo, dni)
            if resultado == 0:
                print('Operacion realizada')
            elif resultado > 0:
                print('Película entregada con un retraso de ', resultado, 'días')
            else:
                print('La pleícula ', titulo, 'no está alquilada al socio ', dni)
        else:
            if not hay_pelicula:
                print('No hay película con el titulo ', titulo)
            if not hay_socio:
                print('No hay socio con DNI ', dni)
    
    elif opcion == 7:
        print('Listado por Género')
        genero = input('Género: ')
        videoclub.listado_por_genero(genero)

    opcion = menu()