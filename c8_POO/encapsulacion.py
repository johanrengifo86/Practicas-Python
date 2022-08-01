#==============================
# Encapsulación de método
#==============================
class Coche():
    # Propiedades de la clase Coche
    def __init__(self):
               
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4 # Encapsulación de propiedad (variable)no es accesible desde fuera de la clase 
        self.__enmarcha = False

    # Métodos de la clase Coche
    def arrancar(self,arrancamos):
        self.__enmarcha = arrancamos

        if self.__enmarcha:
            chequeo = self.__chequeo_interno()
        if(self.__enmarcha and chequeo):
            return 'El coche está en marcha'
        elif self.__enmarcha and chequeo == False:
            return 'Algo ha ido mal en el chequeo. no se puede arrancar'
        else:
            return 'El coche está quieto'

    def estado(self):
        print('El coche tiene: ',self.__ruedas, 'ruedas.', 'Un ancho de: ', self.__anchoChasis,
               'y un largo de: ', self.__largoChasis)
    # Método encapsulado
    def __chequeo_interno(self):
        print('Realizando Cheque Interno.')

        self.gasolina = 'ok'
        self.aceite = 'ok'
        self.puertas = 'cerradas'

        if (self.gasolina == 'ok' and self.aceite == 'ok' and self.puertas == 'cerradas'):
            return True
        else:
            return False
                    

# instacia de la clase Coche
miCoche = Coche()

print(miCoche.arrancar(True))
miCoche.estado()


print("------------A continuación creamos el segundo objeto---------------")

miCoche2 = Coche()

print(miCoche2.arrancar(False))
miCoche2.estado()

