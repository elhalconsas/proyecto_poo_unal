class Esferas:
    def __init__(self, esfera_A, esfera_B, esfera_C, esfera_D):
        self.esfera_A = esfera_A
        self.esfera_B = esfera_B
        self.esfera_C = esfera_C
        self.esfera_D = esfera_D


    def Peso(self):  


        if self.esfera_A == self.esfera_B == self.esfera_C:
           
            if self.esfera_D > self.esfera_A:
                return "La esfera D es la diferente y es de mayor peso"
            else:
                return "La esfera D es la diferente y es de menor peso"
       
        elif self.esfera_A == self.esfera_B == self.esfera_D:
           
            if self.esfera_C > self.esfera_A:
                return "La esfera C es la diferente y es de mayor peso"
            else:
                return "La esfera C es la diferente y es de menor peso"


        elif self.esfera_A == self.esfera_C == self.esfera_D:
           
            if self.esfera_B > self.esfera_A:
                return "La esfera B es la diferente y es de mayor peso"
