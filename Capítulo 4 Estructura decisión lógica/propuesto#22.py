class Empleado:
    def __init__(self, nombre, salario_hora, horas_trabajadas):
        self.nombre = nombre
        self.salario_hora = salario_hora
        self.horas_trabajadas = horas_trabajadas

    def calcular_salario_mensual(self):
        return self.salario_hora * self.horas_trabajadas

    def mostrar_informacion(self):
        salario_mensual = self.calcular_salario_mensual()
        if salario_mensual > 450000:
            print(f"Empleado: {self.nombre}, Salario Mensual: ${salario_mensual:.2f}")
        else:
            print(f"Empleado: {self.nombre}")


def main():
    nombre = input("Ingrese el nombre del empleado: ")
    salario_hora = float(input("Ingrese el salario básico por hora: "))
    horas_trabajadas = int(input("Ingrese el número de horas trabajadas en el mes: "))
    
    empleado = Empleado(nombre, salario_hora, horas_trabajadas)
    empleado.mostrar_informacion()

if "_main_":
  main()
