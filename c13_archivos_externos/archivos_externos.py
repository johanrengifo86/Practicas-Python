#============================
# Manejo de Archivos Externos
# =============================
# Fases necesarias para guardar información en archivos externos.
#  - Creación
#  - Apertura
#  - Manipulación
#  - Cierre 
#===================================
from io import open
''' 
archivo_texto = open('archivo.txt', 'w')
frase = 'Estupendo día para estudiar Python \n el Jueves'
archivo_texto.write(frase)
archivo_texto.close()
'''
archivo_texto = open('archivo.txt', 'r')
texto = archivo_texto.read()
archivo_texto.close()
print(texto)
