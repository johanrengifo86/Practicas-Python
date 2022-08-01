# Funcion decoradora con Parametros 

def funcion_decoradora(funcion_parametro):
    def funcion_interior(*args, **kwargs): # *args --> le dice a una funcion en python que puede recibir un numero indetrminado de parametros 
                                           # **kwargs--> recibe parametros con clave valor
        # Acciones adicionales que decoran 
        print(" Se realizara un cálculo: ")
        funcion_parametro(*args, **kwargs) # tambien se le indica a la funcion interior
        # Acciones adicionales que decoran
        print(" Se ha terminado el cálculo")

    return funcion_interior


@funcion_decoradora
def suma(num1, num2, num3):
    print(num1+num2+num3)

@funcion_decoradora
def resta(num1, num2):
    print(num1-num2)
@funcion_decoradora
def potencia(base, exponente):
    print(pow(base, exponente))

suma(7, 5, 8)
resta(12, 10)
potencia(base=5,exponente=3)