class Intro():
    def __init__(self,valor):
        self.valor = valor
    def segundo(self):
        print('Segundo')
    def tercero(self):
        print('Tercero')

dato = Intro("Valor")
dir(dato)
print(dir(dato))

print(isinstance (dato,Intro ))

print(hasattr(dato, 'Introver'))