from operator import le
from time import sleep


class Fecha:
    def __init__(self, dia, mes, año):
        self.dia = dia
        self.mes = mes
        self.año = año

    def __str__(self):
        return '{} / {} / {}'.format(self.dia, self.mes, self.año)

    def formatoLargo(self):
        meses = { 1:'Enero', 2:'Febrero', 3:'Marzo', 4:'Abril', 5:'Mayo', 6:'Junio', 7:'Julio', 8:'Agosto', 9:'Septiembre', 10:'Octubre', 11:'Noviembre', 12:'Diciembre'}
        mes = meses.get(self.mes)
        print('{} de {} de {}'.format(self.dia, mes, self.año))

    def en_año_bisiesto(self):
        return self.año % 4 == 0 and (self.año % 100 != 0 or self.año % 400 == 0)

def lee_fecha():
    dia = 0
    while dia < 1 or dia > 31:
        dia = int(input('Día: '))
    mes = 0
    while mes < 1 or mes > 12:
        mes = int(input('Mes: '))
    año = int(input('Año: '))
    return Fecha(dia, mes, año)

# Comparar Fechas 
def fecha_es_menor(fecha1, fecha2):
    if fecha1.año < fecha2.año:
        return True
    elif fecha1.año > fecha2.año:
        return False
    if fecha1.mes < fecha2.mes:
        return True
    elif fecha1.mes > fecha2.mes:
        return False
    return fecha1.dia < fecha2.dia

# Si en un programa se desea comparar dos fechas, f1 y f2 se hace asi:
# if fecha_es_menor(f1,f2):
f = Fecha(13, 4, 2022)
f.formatoLargo()
lee_fecha()


