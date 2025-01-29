from inmueble_vivienda import InmueblesVivienda

class Apartamento(InmueblesVivienda):
    def __init__(self, identificadorInmobiliario, area, direccion, precioVenta, numeroBaños, numeroHabitaciones=None):
        super().__init__(identificadorInmobiliario, area, direccion, precioVenta, numeroBaños, numeroHabitaciones)

class ApartamentoFamiliar(Apartamento):
    valorArea = 2000000

    def __init__(self, identificadorInmobiliario, area, direccion, numeroBaños, numeroHabitaciones, valorAdministracion):
        super().__init__(identificadorInmobiliario, area, direccion, None, numeroBaños, numeroHabitaciones)
        self.valorAdministracion = valorAdministracion

    def imprimir(self):
        super().imprimir()
        print(f"Valor de la administración = $ {self.valorAdministracion:.2f}")

class Apartaestudio(Apartamento):
    valorArea = 1500000

    def __init__(self, identificadorInmobiliario, area, direccion):
        super().__init__(identificadorInmobiliario, area, direccion, None, 1, 1)

    def imprimir(self):
        super().imprimir()
