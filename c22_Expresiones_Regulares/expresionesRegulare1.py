#===============================
# Expresiones Regulares
#===========================0
'''
* Que son ?
        Son una secuencia dde caracteres que forman un patrón de busqueda
* Para qué sirven?
        Para el trabajo y procesamiento de texto.
* Ejemplos:
        - Buscar un texto que se ajusta a un formato determinado(correo electrónico)
        - Buscar si existe o no una cadena de caracteres dentro de un texto
        - Contar el número de coincidencias dentro de un texto
'''
import re

cadena = " Vamos a aprender expresiones regulares en Python. Python es un lenguaje de sintaxis sencilla "

#print(re.search("aprender", cadena))
#print(re.search("aprenderee", cadena))

textoBuscar = "Python"
#=============
''' 
if re.search(textoBuscar, cadena) is not None:
    print("Se ha encontrado del texto")

else:
    print("No se ha encontrado el texto")
'''
#===============
textoEncontrado = re.search(textoBuscar, cadena)
print(textoEncontrado.start())
print(textoEncontrado.end())
print(textoEncontrado.span())
print(re.findall(textoBuscar, cadena))
print(len(re.findall(textoBuscar, cadena)))