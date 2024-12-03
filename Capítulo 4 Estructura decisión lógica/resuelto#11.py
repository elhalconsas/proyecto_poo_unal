class nummayor:
    def __init__(self, n1, n2, n3) :
        self.n1 = n1
        self.n2= n2
        self.n3 = n3
        
    def comprobar(self):
        mayor=0
        if (self.n1 > self.n2) & (self.n1 > self.n3):
          mayor=self.n1
          
        elif self.n2 > self.n3:
            mayor= self.n2
        else:
            mayor= self.n3
        return mayor

          
    def print(self):
        print("EL NUMERO MAYOR ENTRE: ", self.n1, ",", self.n2,"y", self.n3, " ES: ",self.comprobar() )
        
        
NUMERO1 = int(input(print("digita el primer numero: ")))
NUMERO2= int(input(print("digita el segundo numero: ")))
NUMERO3= int(input(print("digita el tercer numero: ")))


numero=nummayor(NUMERO1,NUMERO2,NUMERO3,)
numero.print()