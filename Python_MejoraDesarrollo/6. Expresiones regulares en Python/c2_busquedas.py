import re
'''
print(re.search(r"\d\d\d","kilo912metro")) # busqueda de 3 numero que esten juntos del 0-9
'''
'''
patron = re.compile("\d\d\d")
print(patron.search("kilo912metro").group()) # .group devuelve la subcadena de lo q se encuentra 
'''
if(re.search("\Aa[0-9].*[end-fin]", "a4 es una marca de fin")):
    print("Se encontro el patrón")

