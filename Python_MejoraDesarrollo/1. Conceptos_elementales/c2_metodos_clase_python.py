from pydoc import classname


class Persona():
    def __init__(self):
        pass
    
    def despedir(self):
        print('Adios')

# Método de clase: --> No necesita crear un objeto
    @classmethod  #Decorador <classmethod> permite crear un método de clase
    def saludar(cls,nombre): #Cuando se utiliza un método de una clase se necesita
                             # agrega la referencia <cls> 
        print("Estoy saludando a: "+nombre)

# Para utilizar el método <saludar>
# se escribe el nombre de la clase + un punto + nombre del metodo+("nombre")
Persona.saludar("Juan")
