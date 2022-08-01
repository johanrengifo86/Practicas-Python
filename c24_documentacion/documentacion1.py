#========================
# Documentar un programa
#=========================
# ¿Qué es?
#  - Incluir comentario en clase, métodos, módulos etc
# ¿Para qué?
#  - Para ayudar en el trabajo en equipo. Especialmente útil en aplicaciones complejas
from c10_Modulos import funciones_matematicas


def areaCuadrado(lado):
    """ Calcula el área de un cuadrado
    elevando al cuadrado el lado pasado por parámetro"""

    return "El área del cuadrado es: " + str(lado*lado)

def areaTriangulo(base, altura):
    """ Calcula el área de un triángulo utilizando los par{ametros base y altura """
    return"El area del triángulo es: " + str((base * altura)/2)

print(areaCuadrado(3))
print(areaCuadrado.__doc__) # Imprime la documentación asociada a la función áreaCuadrado
help(areaCuadrado)
print(areaTriangulo(2,7))
help(areaTriangulo)


print("***************************************************************")


#===================================Documentacion clases===============
class Areas:
    """ Esta clase calcula las áreas de diferentes figuras geométricas"""
    def areaCuadrado(lado):
        """ Calcula el área de un cuadrado
        elevando al cuadrado el lado pasado por parámetro"""

        return "El área del cuadrado es: " + str(lado*lado)

    def areaTriangulo(base, altura):
        """ Calcula el área de un triángulo utilizando los par{ametros base y altura """
        return"El area del triángulo es: " + str((base * altura)/2)

help(Areas.areaTriangulo)
help(Areas)
help(funciones_matematicas)