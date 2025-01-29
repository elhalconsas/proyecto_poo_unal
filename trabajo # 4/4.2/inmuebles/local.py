from .inmueble import Inmuebles

class Local(Inmuebles):
    def __init__(self, identificadorInmobiliario, area, direccion, tipoLocal):
        super().__init__(identificadorInmobiliario, area, direccion, None)
        self.tipoLocal = tipoLocal

    def imprimir(self):
        super().imprimir()
        print(f"Tipo de local = {self.tipoLocal}")

class LocalComercial(Local):
    def __init__(self, identificadorInmobiliario, area, direccion, tipoLocal, valorArea, centroComercial):
        super().__init__(identificadorInmobiliario, area, direccion, tipoLocal)
        self.valorArea = valorArea
        self.centroComercial = centroComercial

    def imprimir(self):
        super().imprimir()
        print(f"Valor por área = {self.valorArea}")
        print(f"Centro comercial = {self.centroComercial}")

class Oficina(Local):
    valorArea = 3500000

    def __init__(self, identificadorInmobiliario, area, direccion, tipoLocal, esGobierno):
        super().__init__(identificadorInmobiliario, area, direccion, tipoLocal)
        self.esGobierno = bool(esGobierno)

    def imprimir(self):
        super().imprimir()
        print(f"Es oficina gubernamental = {self.esGobierno}")
        print("")
