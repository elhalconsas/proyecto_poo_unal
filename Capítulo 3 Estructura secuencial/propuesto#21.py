import math
class triangulo:
        def __init__(self, ladoA, ladoB, ladoC):
            self.ladoA = ladoA
            self.ladoB = ladoB
            self.ladoC = ladoC
        
        def perimetro(self,):
            perimetros = self.ladoA + self.ladoB + self.ladoC  
            return perimetros
        
        def semiperimetro(self,):
            semiP = self.perimetro()/2
            return semiP
        
        def altura(self,):
            base = self.ladoC/2
            alturas = math.sqrt((self.ladoA**2) - (base**2))
            return alturas
        
        def area(self):
            reis = self.semiperimetro() * (self.semiperimetro() - self.ladoA) * (self.semiperimetro()-self.ladoB) * (self.semiperimetro()-self.ladoC)
            areas = math.sqrt(reis) 
            return areas

        def print(self):    
            print("el perimetro del triangulo es: ", self.perimetro())
            print("el semiperimtro del triangulo es: ",self.semiperimetro() )
            print("el area del triangulo es: ", self.area() )
            
traigulos =triangulo(12,13,42)
traigulos.print()