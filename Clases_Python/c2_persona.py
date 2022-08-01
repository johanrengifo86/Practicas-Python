from errno import EADDRNOTAVAIL
from importlib.metadata import SelectableGroups


class Persona:
    def __init__(self, nombre, dni, edad):
        self.nombre = nombre
        self.dni = dni
        self.edad = edad

    def copia(self):
        nuevo = Persona(self.nombre[:], self.dni[:], self.edad)
        return nuevo
''' 
    def iniciales(self):
        cadena = ''
        for caracter in self.nombre:
            if caracter >= 'A' and caracter <= 'Z':
                cadena = cadena + caracter + '. '
        return cadena

    def __str__(self):
        cadena = 'Nombre: {}\n'.format(self.nombre)
        cadena = cadena + 'DNI: {}\n'.format(self.dni)
        cadena = cadena + 'Edad: {}\n'.format(self.edad)
        return cadena


toni = Persona('Antonio Pérez', '987654', 20)
juan = Persona('Juan Pérez', '123456', 19)
pedro = Persona('Pedro López', '234678', 18)

print(juan)
print(juan.iniciales())
'''
#----------------------------
def nada_util(persona1, persona2):
    persona1.edad += 1
    persona3 = persona2
    persona4 = persona2.copia()
    persona3.edad -= 1
    persona4.edad -= 2
    return persona4

juan = Persona('Juan Pérez', '123456', 19)
pedro = Persona('Pedro López', '234678', 18)
otro = nada_util(juan, pedro)
print(juan)
print(pedro)
print(otro)



   