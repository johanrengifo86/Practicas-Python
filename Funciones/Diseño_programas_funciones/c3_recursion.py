# Una función que se llama a sí misma, directa o indirectamente, 
# es una función recursiva.

# factorial.py forma recursiva

def factorial(n):
    if n == 0 or n ==1:
        resultado = 1
    elif n > 1:
        resultado = n * factorial(n-1)
        return resultado

# factorial forma iterativa
def factorial_V2(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

