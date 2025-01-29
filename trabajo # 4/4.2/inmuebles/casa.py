from .inmueble_vivienda import InmueblesVivienda

class Casa(InmueblesVivienda):
    def __init__(self, identificadorInmobiliario, area, direccion, precioVenta, numeroPisos, numeroBaños):
        super().__init__(identificadorInmobiliario, area, direccion, precioVenta, numeroBaños, None)
        self.numeroPisos = numeroPisos

    def imprimir(self):
        super().imprimir()
        print(f"Número de pisos = {self.numeroPisos}")

class CasaRural(Casa):
    valorArea = 1500000

    def __init__(self, identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBaños, numeroPisos, distanciaCabecera, altitud):
        super().__init__(identificadorInmobiliario, area, direccion, None, numeroPisos, numeroBaños)
        self.distanciaCabecera = distanciaCabecera
        self.altitud = altitud

    def imprimir(self):
        super().imprimir()
        print(f"Distancia a la cabecera municipal = {self.distanciaCabecera} km")
        print(f"Altitud sobre el nivel del mar = {self.altitud} metros")

class CasaUrbana(Casa):
    def __init__(self, identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBaños, numeroPisos):
        super().__init__(identificadorInmobiliario, area, direccion, None, numeroPisos, numeroBaños)
        self.numeroHabitaciones = numeroHabitaciones

    def imprimir(self):
        super().imprimir()

class CasaConjuntoCerrado(CasaUrbana):
    valorArea = 2500000

    def __init__(self, identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBaños, numeroPisos, valorAdministracion, tienePiscina, tieneCamposDeportivos):
        super().__init__(identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBaños, numeroPisos)
        self.valorAdministracion = valorAdministracion
        self.tienePiscina = tienePiscina
        self.tieneCamposDeportivos = tieneCamposDeportivos

    def imprimir(self):
        super().imprimir()
        print(f"Valor de la administración = $ {self.valorAdministracion:.2f}")
        print(f"Tiene piscina = {'Sí' if self.tienePiscina else 'No'}")
        print(f"Tiene campos deportivos = {'Sí' if self.tieneCamposDeportivos else 'No'}")

class CasaIndependiente(CasaUrbana):
    valorArea = 3000000

    def __init__(self, identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBaños, numeroPisos):
        super().__init__(identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBaños, numeroPisos)

    def imprimir(self):
        super().imprimir()
