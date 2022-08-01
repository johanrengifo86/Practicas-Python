bits = input('Ingresa un número binario: ')

n = len(bits)
valor = 0
for bit in bits:
    if bit == '1':
        valor = valor + 2 **( n-1)
    n -= 1
print('El valor decimal es: ', valor)
