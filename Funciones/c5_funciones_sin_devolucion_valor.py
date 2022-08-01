# Una función que no devuelve valor se denomina procedimiento
# sirven para
# - mostrar mensajes o resultados por pantalla.
''' 
def es_perfecto(n): # Averigua si el número <n> es o no es perfecto.
    sumatorio = 0
    for i in range(1, n):
        if n % i == 0:
            sumatorio += i
    return sumatorio == n

def tabla_perfectos(m): # Muestra todos los números perfectos entre 1 y m
    for i in range(1, m+1):
        if es_perfecto(i):
            print(i, 'es un número perfecto')

#numero = int(input('Ingresa un número: '))
#tabla_perfectos(numero)

resultado = tabla_perfectos(100)
print(resultado)
'''
# Procedimiento que recibe como datos dos listas y una cadena con el nombre del estudiante
# si el estudiante pertenece a la clase, el procedimiento imprimirá su nombre y nota en pantalla.
# Si no es un alumno incluido en la lista, se imprimirá un mensaje que lo advierta.
#alumnos = ['Ana Pi', 'Pau López', 'Luis Sol', 'Mar_Vega', 'Paz Mir']
#notas = [10, 5.5, 2.0, 8.5, 7.0]
# Versión 1
''' 
def muestra_nota_de_alumno(alumnos, notas, alumno_buscado):
    encontrado = False
    for i in range(len(alumnos)):
        if alumnos[i] == alumno_buscado:
            print(alumno_buscado, notas[i])
            encontrado = True
        if not encontrado:
            print('El alumno {} no pertenece al grupo'.format(alumno_buscado))
'''
# version 2
''' 
def muestra_nota_de_alumno(alumnos, notas, alumno_buscado):
    encontrado = False
    for i in range(len(alumnos)):
        if alumnos[i] == alumno_buscado:
            print(alumno_buscado, notas[i])
            encontrado = True
            break
        if not encontrado:
            print('El alumno {} no pertenece al grupo'.format(alumno_buscado))
'''
# Version 3
alumnos = ['Ana Pi', 'Pau López', 'Luis Sol', 'MarVega', 'Paz Mir']
notas = [10, 5.5, 2.0, 8.5, 7.0]

def muestra_nota_de_alumno(alumnos, notas, alumno_buscado):
    for i in range(len(alumnos)):
        if alumnos[i] == alumno_buscado:
            print(alumno_buscado, notas[i])
            return
        
    print('El alumno {} no pertenece al grupo'.format(alumno_buscado))
# 295 En el problema de los alumnos y notas se pide:

# 1. Diseñar un procedimiento que reciba las dos listas y muestre por pantalla el nombre de 
# todos los estudiantes que aprobaron el examen
def nombre_aprobados(alumnos, notas):
    #for i in range(len(alumnos)):
        for j in range(len(notas)):
            if notas[j] >= 7:
                print(alumnos[j])
nombre_aprobados(alumnos, notas)

# 2. Diseñar una función que reciba la lista de notas y devuelva el número de aprobados.
def numero_aprobados(notas):
    aprobados = 0
    for i in range(len(notas)):
        if notas[i] >= 7:
           aprobados += 1
    #print(aprobados)
    return aprobados
numero_aprobados(notas)

c = numero_aprobados(notas)
print (c)

# 3. Diseñar un procedimiento que reciba las dos listas y muestre por pantalla el nombre de todos
# los estudiantes que obtuvieron la maxima nota

# 4. Diseñar un procedimiento que reciba las dos listas y muestre por pantalla el nombre de tosos los 
# estudiantes cuya calificación es igual o superior a la calificación media.

# 5. Diseñar una función que reciba las dos listas y un nombre (una cadena); si el nombre
# está en la lista de estudiantes, devolverá su nota, si no, devolverá None.






