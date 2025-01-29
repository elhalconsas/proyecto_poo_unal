from apartamento import ApartamentoFamiliar, Apartaestudio

class Prueba:

    def __init__(self):
        apto1 = ApartamentoFamiliar(103067, 120, "Avenida Santander 45-45", 3, 2, 200000)
        print("Datos apartamento")
        apto1.precioVenta = apto1.calcular_precio_venta(apto1.valorArea)
        apto1.imprimir()

        aptestudio1 = Apartaestudio(12354, 50, "Avenida Caracas 30-15")
        print("Datos apartaestudio")
        aptestudio1.precioVenta = aptestudio1.calcular_precio_venta(aptestudio1.valorArea)
        aptestudio1.imprimir()

if __name__ == "__main__":
    Prueba()
