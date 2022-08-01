from traceback import print_tb
from pyparsing import col


class Cola:
    def __init__(self): # Se guarda la lista en el atributo cola y se inicializa con una lista vacia 
        self.cola = []

    def añade(self, elemento): # Añade un nuevo elemento al final
        self.cola.append(elemento)

    def primero(self): # dice quién ocupa la primera posición en la cola
        if len(self.cola) == 0:
            return None
        else:
            return self.cola[0]
    
    def sacaPrimero(self): # Borra el primer elemento de la lista
        if len(self.cola) > 0:
            del self.cola[0]

    def __str__(self):
        cadena = ''
        for elemento in self.cola:
            cadena = cadena + str(elemento) + ' '
        return cadena

    def tamaño(self):
        return len(self.cola)

    def esVacia(self):
        return len(self.cola) == 0
    
cola = Cola()
cola.añade(5)
cola.añade(8)
cola.añade(4)
print(cola)
print(cola.primero())
cola.sacaPrimero()
print(cola)
cola.añade(9)
print(cola)
print(cola.tamaño())
print(cola.esVacia())
cola.sacaPrimero()
cola.sacaPrimero()
cola.sacaPrimero()
print(cola)
print(cola.esVacia())
print(cola.primero())