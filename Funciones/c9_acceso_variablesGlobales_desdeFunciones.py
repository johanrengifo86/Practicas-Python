# # Programa que gestiona una de las funciones de un cajero automátio
# que puede entregar cantidades que son múltiplos de 10
# En cada momento, el cajero tiene un número determinado de billetes de 50, 20 y 10 €
#  Utilizaremos una variable para cada tipo de billete y
#  en ella indicaremos cuántos billetes de ese tipo nos quedan en el cajero 
# Cuando un cliente pida sacar una cantidad determinada de dinero,
#  mostraremos por pantalla cuántos billetes de cada tipo le damos
#  lntentaremos darle siempre la menor cantidad de billetes posible 
# Si no es posible darle el dinero (porque no tenemos suﬁciente dinero en el cajero o porque la cantidad solicitada no puede darse con una combinación va’lida de los billetes disponibles) 
# informaremos al usuario lnicialmente 
# supondremos que el cajero esta’ cargado con 100 billetes de cada tipo:
# Programa Cajero
carga50 = 100
carga20 = 100
carga10 = 100

def retirar_dinero(cantidad):
    global carga50, carga20, carga10
    if cantidad <= 50 * carga50 + 20 *carga20 + 10 * carga10:
        de50 = cantidad // 50
        cantidad = cantidad % 50
        if de50 >= carga50: # Si no hay suficientes billetes de 50
            cantidad = cantidad + (de50 - carga50) * 50
            de50 = carga50
        de20 = cantidad // 20
        cantidad = cantidad % 20
        if de20 >= carga20: # Si no hay suficientes billetes de 20
            cantidad = cantidad + (de20 - carga20) * 20
            de20 = carga20
        de10 = cantidad // 10
        cantidad = cantidad % 10
        if de10 >= carga10: # y no hay suficientes billetes de 10
            cantidad = cantidad + (de10 - carga10) * 10
            de10 = carga10
        # Si todo ha ido bn, la cantidad que resta por entregar es nula:
        if cantidad == 0:
            # se hace efectiva la extraccion
            carga50 = carga50 - de50
            carga20 = carga20 - de20
            carga10 = carga10 - de10
            return [de50, de20, de10]
        else:
            return[0, 0, 0]
    else:
        return[0, 0, 0]

# Programa Principal
while 50*carga50 + 20*carga20 + 10*carga10 > 0:
    peticion = int(input('Cantidad que desea Retirar: '))
    [de50, de20, de10] = retirar_dinero(peticion)
    if[de50, de20, de10] != [0, 0, 0]:
        if de50 > 0:
            print('Billetes de 50 euros: ', de50)
        if de20 > 0:
            print('Billetes de 20 euros: ', de20)
        if de10 > 0:
            print('Billetes de 10 euros: ', de10)
        print('Gracias por usar el cajero. \n')
    else:
        print('Lamentamos no poder atender su petición.\n')
print('Cajero sin dinero. Avise a mantenimiento.')
