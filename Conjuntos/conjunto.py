class Conjunto():
    def __init__(self):
        self.elementos = []

    def inserta (self, elemento):
        if not (elemento in self.elementos):
            self.elementos.append(elemento)
    
    def elimina(self, elemento):
        if elemento in self.elementos:
            del self.elementos[elemento]

    def __str__(self):
        cadena = '{'
        if len(self.elementos) > 0:
            for elemento in self.elementos[:-1]:
                cadena = cadena + str(elemento) + ', '
            cadena = cadena + str(self.elementos[-1])
        return cadena + '}'

    def talla(self):
        return len(self.elementos)

    def pertenece(self, elemento):
        return elemento in self.elementos

    def union(self, otro):
        C = Conjunto()
        C.elementos = self.elementos[:]
        for elemento in otro.elementos:
            C.inserta(elemento)
        return C

    def incluye(self, otro):
        for elemento in otro.elementos:
            if not (elemento in self.elementos):
                return False
        return True


conjunto = Conjunto()
conjunto.inserta(1)
conjunto.inserta(2)
conjunto.inserta(3)
print(conjunto)
conjunto.elimina(1)
print(conjunto)
a = Conjunto()
a.inserta(3)
a.inserta(5)
a.inserta(3)
print(a)
