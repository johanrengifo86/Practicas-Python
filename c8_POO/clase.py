class Coche():
    # Propiedades de la clase Coche
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enmarcha = False

    # Métodos de la clase Coche
    def arrancar(self):
        self.enmarcha = True

    def estado(self):
        if(self.enmarcha):
            return 'El coche está en marcha'
        else:
            return 'El coche está quieto'

# instacia de la clase Coche
miCoche = Coche()

print('El largo del coche es: ',miCoche.largoChasis)
print('El coche tiene: ', miCoche.ruedas)
miCoche.arrancar()
print(miCoche.estado())

print("------------A continuación creamos el segundo objeto---------------")

miCoche2 = Coche()
print('El largo del coche es: ',miCoche2.largoChasis)
print('El coche tiene: ', miCoche2.ruedas)
print(miCoche2.estado())

