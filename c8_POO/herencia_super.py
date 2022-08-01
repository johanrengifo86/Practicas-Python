class Persona():
    def __init__(self, nombre, edad, Lugar_residencia):
        self.nombre = nombre
        self.edad = edad
        self.lugar_residencia = Lugar_residencia

    def descripcion(self):
        print('Nombre: ', self.nombre, '\nEdad: ', self.edad, '\nResidencia: ', self.lugar_residencia)

class Empleado(Persona):
    def __init__(self,nombre_empleado, edad_empleado, residencia_empleado, salario, antiguedad):
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
        self.salario = salario
        self.antiguedad = antiguedad

    def descripcion(self):
        super().descripcion()
        print('Salario:', self.salario, '\nAntiguedad: ', self.antiguedad)


Antonio = Persona('Antonio', 55, 'España')
Manuel = Empleado('Manuel', 55, 'colombia', 1500, 15)

#Antonio.descripcion()
Manuel.descripcion()

print(isinstance(Manuel, Persona))
print(isinstance(Antonio, Empleado))