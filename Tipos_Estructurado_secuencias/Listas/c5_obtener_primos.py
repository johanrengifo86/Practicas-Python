n = int(input('Introduce el valor máximo: '))

primos = []
for numero in range(2, n+1):
    # Dterminamos si el número es primo
    creo_que_es_primo = True
    for divisor in range(2, numero):
        if numero % divisor == 0:
            creo_que_es_primo = False
            break
    # Y si es primo se añade a la lista
    if creo_que_es_primo:
        primos.append(numero)

print(primos)
