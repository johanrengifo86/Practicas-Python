from decimal import DivisionByZero


def divide():
    try:

        opc1 = float(input('Introduce el Primer Número: '))
        opc2 = float(input('Intrododuce el Segundo Número: '))

        print('La división es: '+ str(opc1 / opc2))
    except ValueError:
        print('El valor Introducido es erróneo')
    except DivisionByZero:
        print('No se puede dividir entre cero.')

    finally:
        print('Calculo FInalizado.')

divide()
