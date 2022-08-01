# Utilizar la documentación para realizar pruebas
# Módulo doctest

def areaTriangulo(base, altura):
    """ 
    Calcula el área de un triangulo dado
    >>> areaTriangulo(3,6)
    'El área del triángulo es: 9.0'

    >>> areaTriangulo(4,5)
    'El área del triángulo es: 10.0'

    >>> areaTriangulo(9,3)
    'El área del triángulo es: 13.5'
    """
    return "El área del triángulo es: "+ str((base * altura)/2)

import doctest
doctest.testmod()