class Vehiculos():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enmarcha = True

    def acelerar(self):
        self.acelera = True
    
    def frenar(self):
        self.frena = True

    def estado(self):
        print('Marca: ',self.marca, '\nModelo: ',self.modelo, '\nEn Marcha: ', self.enmarcha, 
              '\nAcelerando: ', self.acelera, '\nFrenando: ', self.frena)

class Furgoneta(Vehiculos):
    def carga(self, cargar):
        self.cargado = cargar
        if self.cargado:
            return 'La Furgoneta esta cargada'
        else:
            return 'La Furgoneta no esta cargada'


# La clase moto hereda de la clase Vehículos
class Moto(Vehiculos):
    hcaballito =''
    def caballito(self):
        self.hcaballito = 'Voy haciendo el caballito'
    
    def estado(self):
        print('Marca: ',self.marca, '\nModelo: ',self.modelo, '\nEn Marcha: ', self.enmarcha, 
              '\nAcelerando: ', self.acelera, '\nFrenando: ', self.frena, '\n', self.hcaballito)

class VElectricos():
    def __init__(self):
        self.autonomia = 100

    def cargarEnergia(self):
        self.cargando = True


miMoto = Moto('Honda', 'CBR')
miMoto.caballito()
miMoto.estado()

miFurgoneta = Furgoneta('Renault', 'Kangoo')
miFurgoneta.estado()
print(miFurgoneta.carga(True))
#print(miFurgoneta.carga(False))

# Herencia múltiple
class BicicletaElectrica(VElectricos, Vehiculos):
    pass

miBici = BicicletaElectrica()
