def primerD(funcion):
    def funcionDecorada(*args, **kkwars): # Para poder recibir parametros (*args) argumentos(kkwars)
        print('Primer decorador')
    return funcionDecorada



@primerD
def funcion():
    print('Mi primer decorador')

funcion()