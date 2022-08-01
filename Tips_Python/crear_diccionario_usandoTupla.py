# crear un diccionario usando desde una tupla 
# usando la clase 'counter' del módulo de colecciones.
from collections import Counter

a = Counter(angry=False, happy=True, disapointed=True)
print(dict((a)))
