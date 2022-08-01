class Estudiante:
    def __init__(self, nombre, grupo, nota, practica):
        self.nombre = nombre
        self.grupo = grupo
        self.nota = nota
        self.practica = practica

    # Método para Imprimir infomación de un estudiante   
    def __str__(self):     
        cadena = 'Nombre: {}\n'.format(self.nombre)
        cadena = cadena + 'Grupo: {}\n'.format(self.grupo)
        cadena = cadena + 'Nota Examen: {0:3.1f}\n'.format(self.nota)
        if self.practica:
            cadena = cadena + 'Práctica entregada.'
        else:
            cadena = cadena + 'Prática no entregada.'
        return cadena

    # Método para conocer la calificaión de un estudiante
    def calificacion(self):
        if not self.practica:
            return 'Suspenso'
        else:
            if self.nota < 5:
                return 'Suspenso'
            elif self.nota < 7:
                return 'Aprobado'
            elif self.nota < 8.5:
                return 'Notable'
            elif self.nota < 10:
                return 'Sobresaliente'
            else:
                return 'Matricula de Honor'

# Función que lee por teclado el valor de cada campo y construye un nuevo Estudiante    
def lee_estudiante():
    nombre = input('Nombre: ')
    grupo = input('Grupo (A, B o C): ')
    nota = float(input('Nota de Examen: '))
    entregada = input('Prática Entregada (s/n): ')
    practica = entregada == 'a'
    return Estudiante(nombre, grupo, nota, practica)

# Función que dada una lista de estudiantes, pide los datos de un estudiante y añade
# el nuevo estudiante a la lista 
def lee_y_añade_estudiante(lista):
    estudiante = lee_estudiante()
    lista.append(estudiante)

# Función que muestra el nombre y la calificación de todos los estudiantes
def acta(lista):
    for estudiante in lista:
        print(estudiante.nombre, estudiante.calificacion())

# Función Nota Media
def nota_media(lista):
    suma = 0 
    cantidad = 0
    for estudiante in lista:
        if estudiante.practica:
            suma += estudiante.nota
            cantidad += 1
    if cantidad != 0:
        return suma / cantidad
    else:
        return 0.0

# Función que muestra el porcentaje de practicas entregadas
def poncentaje_praticas_entregadas(lista):
    if len(lista) != 0:
        cantidad = 0
        for estudiante in lista:
            if estudiante.practica:
                cantidad += 1
        return cantidad / len(lista) * 100
    else:
        return 0.0 

# Lista con los estudiantes de las notas más altas
def mejores_estudiantes(lista):
    nota_mas_alta = 0
    mejores = []
    for estudiante in lista:
        if estudiante.practica:
            if estudiante.nota > nota_mas_alta:
                mejores = [estudiante]
                nota_mas_alta = estudiante.nota
            elif estudiante.nota == nota_mas_alta:
                mejores.append(estudiante)
    return mejores

# Imprimir en pantalla los mejores estudiantes
    los_mejores = mejores_estudiantes(lista)
    for estudiante in los_mejores:
         print(estudiante.nombre)

#lee_estudiante()

