'''def lower(elementos):
    return elementos.lower()

lista =["JOHAN","RENgifo","No"]

print(list(map(lower, lista)))

print([cad.lower() for cad in lista])'''

'''# Funciones de orden superior
def saludo(idioma):
    def saludo_es():
        print('Hola')
    def saludo_en():
        print('Hi')
    
    idioma_func = {"es":saludo_es,
                   "en":saludo_en
                   }
    return idioma_func[idioma]

saludar = saludo("en")
saludar()'''

from functools import reduce

numeros = (1,2,3,4,5)

def suma(x,y):
    return x+y

sumar = reduce(suma,numeros)
print(sumar)


