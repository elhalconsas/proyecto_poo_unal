from inmueble import Inmuebles

class InmueblesVivienda(Inmuebles):
    def __init__(self, identificadorInmobiliario, area, direccion, precioVenta, numeroBaños, numeroHabitaciones):
        super().__init__(identificadorInmobiliario, area, direccion, precioVenta)
        self.numeroBaños = numeroBaños
        self.numeroHabitaciones = numeroHabitaciones

    def imprimir(self):
        super().imprimir()
        print(f"Número de baños = {self.numeroBaños}")
        print(f"Número de habitaciones = {self.numeroHabitaciones}")
