import math


class circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio**2
    
    def calcular_perimetro(self):
        return 2 * math.pi * self.radio
    
class rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return (2 * self.base) + (2 * self.altura)
    
class cuadrado:

    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return math.pow(self.lado, 2)
    
    def calcular_perimetro(self):
        return self.lado * 4
    
class triangulo_rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2
    
    def calcular_hipotenusa(self):
        return math.sqrt(self.base ** 2 + self.altura ** 2 )
    
    def calcular_perimetro(self):
        return self.base + self.altura + self.calcular_hipotenusa()
    
    def determinar_tipo_de_triangulo(self):
        hipotenusa = self.calcular_hipotenusa()
        if self.base == self.altura == hipotenusa:
            print("Es un triangulo equilatero")

        elif self.base != self.altura and self.base != hipotenusa and self.altura != hipotenusa:
            print("Es un triangulo escaleno")

        else: print("Es un triangulo isosceles")

class rombo:
    def __init__(self, diagonal_1, diagonal_2, lado):
        self.diagonal_1 = diagonal_1
        self.diagonal_2 = diagonal_2
        self.lado = lado

    def calcular_area(self):
        return (self.diagonal_1 * self.diagonal_2) / 2
    
    def calcular_perimetro(self):
        return self.lado * 4
    
class trapecio:
    def __init__(self, base_1, base_2, altura, lado_1, lado_2):
        self.base_1 = base_1
        self.base_2 = base_2
        self.altura = altura
        self.lado_1 = lado_1
        self.lado_2 = lado_2

    def calcular_area(self):
        return ((self.base_1 + self.base_2) * self.altura) / 2
    
    def calcular_perimetro(self):
        return self.base_1 + self.base_2 + self.lado_1 + self.lado_2 

class prueba_figuras:
    figura1 = circulo(int(input("Ingrese el radio del circulo: ")))
    figura2 = rectangulo(int(input("Ingrese la base del rectangulo: ")), (int(input("Ingrese la altura del rectangulo: "))))
    figura3 = cuadrado(int(input("Ingrese el lado del cuadrado: ")))
    figura4 = triangulo_rectangulo(int(input("Ingrese la base del triangulo: ")), (int(input("Ingrese la altura del triangulo: "))))
    figura5 = rombo(int(input("Ingrese la diagonal 1 del rombo: ")), (int(input("Ingrese la diagonal 2 del rombo: "))), (int(input("Ingrese el lado del rombo: "))))
    figura6 = trapecio(int(input("Ingrese la base 1 del trapecio: ")), (int(input("Ingrese la base 2 del trapecio: "))), (int(input("Ingrese la altura del trapecio: "))), (int(input("Ingrese el lado 1 del trapecio: "))), (int(input("Ingrese el lado 2 del trapecio: "))))

    print("\n")
    print(f"El area del circulo es = {figura1.calcular_area()}")
    print(f"El perimetro del circulo es = {figura1.calcular_perimetro()}\n")


    print(f"El area del rectangulo es = {figura2.calcular_area()}")
    print(f"El perimetro del rectangulo es = {figura2.calcular_perimetro()}\n")


    print(f"El area del cuadrado es = {figura3.calcular_area()}")
    print(f"El perimetro del cuadrado es = {figura3.calcular_perimetro()}\n")


    print(f"El area del triangulo es = {figura4.calcular_area()}")
    print(f"El perimetro del triangulo es = {figura4.calcular_perimetro()}\n")
    figura4.determinar_tipo_de_triangulo()


    print(f"El area del rombo es = {figura5.calcular_area()}")
    print(f"El perimetro del rombo es = {figura5.calcular_perimetro()}\n")


    print(f"El area del trapecio es = {figura6.calcular_area()}")
    print(f"El perimetro del trapecio es = {figura6.calcular_perimetro()}\n")

