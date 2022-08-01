class ColaPrioridad:
    def __init__(self):
        self.cola = []

    def inserta(self, elemento):
        self.cola.append(elemento)

    def primero(self, elemento):
        if len(self.cola) == 0:
            return None
        maximo = self.cola[0]
        for valor in self.cola:
            if valor > maximo:
                maximo = valor
        return maximo

    def extraer(self, elemento):
        if len(self.cola) == 0:
            return None
        indice = 0
        for i in range(len(self.cola)):
            if self.cola[i] > self.cola[indice]:
                indice = i
        aux = self.cola[indice]
        del self.cola[indice]
        return aux

    def tamaño(self):
        return len(self.cola)

    def es_vacia(self):
        return len(self.cola) == 0



