#---------------------------------------
# Módulo: gravedad
#
# Propósito: Proporciona algunas constantes y funciones sobre física gravitatoria.
#
#
# Autor/es: Johan Rengifo
#---------------------------------------
# Constantes exportadas:
# G: Constante de gravitación universal.
# MTierra: Masa de la Tierra (en kilos).
# RTierra: Radio de la Tierra (en metros)
# MLuna: Masa de la Luna (en kilos).
# RLuna: Radio de la Luna (en metros)
#
# Funciones exportadas:
# fuerzaGravitatoria: calcula la fuerza gravitatotia existente entre dos cuerpos.
# entradas:
# M: masa de un cuerpo (en kg).
# m: masa del otro cuerpos (en kg).
# r: distancia entre ellos (en metros).
# salida:
# fuerza en (Newtons)
#
# distancia: calcula La distancia que separa dos cuerpos atraidos por una fuerza
# graVitatoria determinada.
# entradas:
# M: masa de un cuerpo (en kg).
# m: masa del otro cuerpo (en kg). 
# F: fuerza graVitatoria experimentada (en m).
# salida:
# distancia (en metros). 
# 
# velocidadEscape: calcula La velocidad necesaria para escapar de La atracción
# gravitatoria de un cuerpo esférico.
# entradas:
# M: masa dei cuerpo (en kg).
# R: radio dei cuerpo (en metros).
# saiida:
# velocidad (en metros por segundo).
#---------------------------------------------
# Historia:
# * Creado el 7/04/2022 por Johan 
# * Modificado el 8/04/2022 por Johan
# - se incluyen las constantes MLuna y RLuna
# - se añade la función velocidadEscape

from math import sqrt

G = 6.67e-11
MTierra = 5.97e24
RTierra = 6.37e6
MLuna = 7.35e22
RLuna = 1.74e6

def fuerzaGravitatoria(M, m, r):
    return G * M * m / r ** 2

def distancia(M, m, F):
    return sqrt(G * M * m / F)
    
def VelocidadEscape(M, R):
    return sqrt(2 *G *M / R)

veTierra = VelocidadEscape(MTierra, RTierra)
veLuna = VelocidadEscape(MLuna, RLuna)

