import math
class triangulo:
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA=ladoA
        self.ladoB=ladoB
        self.ladoC= ladoC
       
      
    
    def perimetro(self,):
        perimetros = self.ladoA + self.ladoB + self.ladoC  
        return perimetros
    
    def altura(self,):
        base=self.ladoC/2
        alturas = math.sqrt((self.ladoA**2) - (base**2))
        return alturas
    
    def area(self):
        areas= (self.ladoC * self.altura()) / 2
        return areas

    
    def print(self):
        
        print("el perimetro del triangulo es: ", self.perimetro())
        print("la altura del triangulo es: ", self.altura())
        print("el area del triangulo es: ", self.area() )
        
traigulos =triangulo(13,13,13)
traigulos.print()