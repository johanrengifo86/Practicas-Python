# Clase Persona

class Persona:   # Palabra reservada <class> --> indica la definición de un nuevo tipo de dato, una nueva clase.
    def __init__(self, nombre, dni, edad):
        self.nombre = nombre
        self.dni = dni
        self.edad = edad 

toni = Persona('Antonio Pérez', '987654', 20)
juan = Persona('Juan Pérez', '123456', 19)
pedro = Persona('Pedro López', '234678', 18)

alumnos = [toni, juan, pedro]

print(toni.edad)
print(alumnos[2].edad)

for alumno in alumnos:
    print(alumno.dni)

for i in range(len(alumnos)):
    print(alumnos[i].dni)


    