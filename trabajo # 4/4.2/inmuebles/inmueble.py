class Inmuebles:
    def __init__(self, identificadorInmobiliario, area, direccion, precioVenta):
        self.identificadorInmobiliario = identificadorInmobiliario
        self.area = area
        self.direccion = direccion
        self.precioVenta = precioVenta

    def calcular_precio_venta(self, valor_area):
        self.precio_venta = self.area * valor_area
        return self.precio_venta

    def imprimir(self):
        print(f"Identificador inmobiliario = {self.identificadorInmobiliario}")
        print(f"Área = {self.area}")
        print(f"Dirección = {self.direccion}")
        print(f"Precio de venta = $ {self.precioVenta:.2f}")
