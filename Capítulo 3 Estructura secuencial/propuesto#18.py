#Declaracion de variables
class Empleado:
    def __init__ (self, codigo, nombre, horas_trabajadas_mes, valor_hora, retencion_fuente):


        self.codigo = codigo
        self.nombre = nombre
        self.horas_trabajadas_mes = horas_trabajadas_mes
        self.valor_hora = valor_hora
        self.retencion_fuente = retencion_fuente


    def salario(self):


        retencion_fuente = self.retencion_fuente / 100
        salario_bruto = self.horas_trabajadas_mes * self.valor_hora
        salario_neto = salario_bruto - retencion_fuente
       
        return salario_bruto, salario_neto
       


sujeto1 = Empleado(123, "Jeremy", 50, 40000, 10)


salario_bruto, salario_neto = sujeto1.salario()


print(f"El código del empleado es: {sujeto1.codigo}")
print(f"El nombre del empleado es: {sujeto1.nombre}")
print(f"El salario bruto del empleado es: {salario_neto}")
print(f"El salario neto del empleado es: {salario_bruto}")