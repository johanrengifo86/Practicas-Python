def fibonacci(n):
    if n == 1 or n == 2:
        resultado = 1
    elif n > 2:
        resultado = fibonacci(n - 1) + fibonacci(n - 2)
    return resultado

print(fibonacci(8))

def fibonnacci_iterativo(n):
    if n == 1 or n == 2:
        f = 1
    else:
        f1 = f2 = 1
        for i in range(3, n+1):
            [f, f1, f2] = [f1 + f2, f2, f]
    return f

