#==============
# Decoradores:
#    - Funciones que a su vez añaden funcionalidades a otras funciones.
#     - Por eso se las denomina "decoradores", porque "decoran" a otras funciones.
#       Les añaden funcionalidades.
# Estructura de un Decorador:
#   - 3 funciones ( A, B y C) donde A recibe como parámetro a B para devolver C.
#   - Un decorador devulve una función

# funcion_decorador --> Función A
# funcion ---> Fución B
# funcion_interna --> Función C
''' 
def funcion_decorador(funcion):   
    def funcion_interna():
        # código de la función interna
        return funcion_interna
'''
def funcion_decoradora(funcion_parametro):
    def funcion_interior():
        # Acciones adicionales que decoran 
        print(" Se realizara un cálculo: ")
        funcion_parametro()
        # Acciones adicionales que decoran
        print("Se ha terminado el cálculo")

    return funcion_interior

# Para decorar se escribe el nombre de la funcion decoradora precedida de @ antes
# de la función a decorar
@funcion_decoradora
def suma():
    print(15+20)

@funcion_decoradora
def resta():
    print(30-10)

suma()
resta()



