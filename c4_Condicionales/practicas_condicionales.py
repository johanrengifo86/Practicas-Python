salario_presidente = int(input('Ingrese Salario Presidente: '))
print('Salario Presidente: ' + str(salario_presidente))

salario_director = int(input('Ingrese Salario Director: '))
print('Salario Presidente: ' + str(salario_director))

salario_jefe_area = int(input('Ingrese Salario Jefe de Área: '))
print('Salario Presidente: ' + str(salario_jefe_area))

salario_administrativo = int(input('Ingrese Salario Administrativo: '))
print('Salario Presidente: ' + str(salario_administrativo))

if salario_administrativo < salario_jefe_area < salario_director < salario_presidente:
    print('Todo funciona correctamente')
else:
    print('Algo Falla en la empresa.')
