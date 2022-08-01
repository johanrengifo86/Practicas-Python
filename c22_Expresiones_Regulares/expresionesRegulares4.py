#==============================
# Funciones del módulo re
#   * Match y Search
#=============================
import re

nombre1 = "Jara López"
nombre2 = "Antonio Gómez"
nombre3 = "Lara López"

if re.match("Sandra", nombre3, re.IGNORECASE):
#if re.match(".ara", nombre3, re.IGNORECASE):
    print("Se encontro el nombre")
else:
    print("No se ha encontrado el nombre")

cadena1 = "Jara López"
cadena2 = "55554545454"
cadena3 = "a8958547844"

if re.match("\d", cadena3): #busca al principio de una cadena de texto 
     print("Se encontro el número")
else:
    print("No se ha encontrado el número")

if re.search("López", nombre3): #busca en toda la cadena de texto
    print("Hemos encontrado el apellido")
else:
    print("No se ha encontrado")


codigo1 = "sdfkfldkfdfdfdfdf70dfdfdfdfdfdfdfd"
codigo2 = "fsdfsdfsdfsdf70dfsdfsdfsdf"
codigo3 = "fdfd fdfd fdfd dfdre sdsd "

if re.search("70", codigo2):
    print("Codigo encontrado")
else:
    print("Codigo no encontrado")