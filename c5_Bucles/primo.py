
limite = int(input('Ingresa un número'))

for numero in range(2, limite+1):
    creo_quees_primo = True
    for divisor in range(2, numero):
        if numero % divisor == 0:
            creo_quees_primo = False
            break
    if creo_quees_primo:
        print(numero, end=' ')
print()