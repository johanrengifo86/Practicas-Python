# Variable de instancia
# Es cuando una variable se relaciona unicamente con la instancia de una clase

class Persona():
    edad = 18                                   # variable de clase
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre                    # variable de instancia
        self.nacionalidad = nacionalidad        # variable de instacia 

# Metódos de Instancia
    def nadar(self):  # se debe colocar el self
        print("Estoy nandando")

persona1 = Persona("Johan","Colombiano")

persona1.nadar()