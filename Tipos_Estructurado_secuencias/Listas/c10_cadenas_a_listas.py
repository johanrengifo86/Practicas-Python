a = 'uno dos tres'.split()
print(a)

# Módulo <split()>
# conteo de palabras de una frase
b = len('   uno  dos tres  '.split())
print(b)

# El método <split> acepta un argumento opcional <:> el carácter <<divisor>>
# que por defecto es el espacio en blanco:

c = 'uno:dos tres:cuatro'.split(':') 
print(c)

# 231 En una cadena llamada <texto> disponemos de un texto formado por varias frase
# ¿Con qué orden simple se puede contar el número de frases ?

texto = len('una frase. dos frase. tres frases'.split('.'))
print(texto)

# Método que une las cadenas de una lista en una sola cadena <join>
unir = ' '.join(['uno', 'dos', 'tres'])
unir_1 = ':'.join(['uno', 'dos', 'tres'])
unir_2 = '--'.join(['uno', 'dos', 'tres'])
print(unir)
print(unir_1)
print(unir_2)

#233 ¿Qué resulta de ejecutar esta sentencia?
print(''.join(['uno', 'dos', 'tres']))

# FUnción Predefinida que convierte una cadena en una lista. La función <list>
print(list('cadena'))

