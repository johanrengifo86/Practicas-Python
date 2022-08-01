class Persona():
    def __init__(self):
        pass

    def saltar(self):
        print('Salto')

    @classmethod
    def correr(cls):
        print('Corro')

    @staticmethod # --> no necesita ningun argumento como referencia ni a la instancia ni a la clase
    def nadar():
        print('Nado')

jose = Persona()
jose.nadar()