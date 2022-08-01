# 221 --> Programa que lee un lista de 10 enteros, pero se asegura de que todos
# los números introducidos son positivos. Cuando el número es negativo se le indica con un mensaje 
lista = []
while True :
    elemento = int(input('Ingresa un elemento: '))
    if elemento > 0:
            lista.append(elemento)
            if (len(lista) == 10) :
                break
    else:
        print('Ingrese un valor Positivo')

print(lista)


