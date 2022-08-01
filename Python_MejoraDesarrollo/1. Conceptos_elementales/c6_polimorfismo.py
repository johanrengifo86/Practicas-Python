from cgi import print_arguments


class Perro ():
    def avanzar(self):
        print('4 Patas')

class Pajaro():
    def avanzar(self):
        print('Volar')

def mover(animal):
    animal.avanzar()

perro = Perro()
pajaro = Pajaro()

perro.avanzar()
pajaro.avanzar()

mover(perro)
mover(pajaro)
