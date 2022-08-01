class MP3:
    def __init__(self, titulo, interprete, duracion, genero):
        self.titulo = titulo
        self.interprete = interprete
        self.duracion = duracion
        self.genero = genero

    def resumen(titulo, interprete):
        return titulo,"-",interprete

    def __str__(self):
        cadena = 'Título de la Canción: {}\n'.format(self.titulo)
        cadena = cadena + 'Interprete: {}\n'.format(self.interprete)
        cadena = cadena + 'Duración: {}\n'.format(self.duracion)
        cadena = cadena + 'Género: {}\n'.format(self.genero)

      
listaCanciones = []

def ingresarCancion():
    tituloCancion = input('Ingrese Título de Canción: ')
    interprete = input('Ingrese Interprete de la canción: ')
    duracion = input('Ingrese duración de la canción: ')
    genero = input('Ingrese género de la canción: ')
    return MP3(tituloCancion, interprete, duracion, genero)

def añadirCancion(lista):
        cancion = ingresarCancion()
        lista.append(cancion) 

listaCanciones = añadirCancion(listaCanciones)

print (listaCanciones)