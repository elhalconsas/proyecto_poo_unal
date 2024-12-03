
class matricula:
    def __init__(self, IN,NOM,PAT, ES) :
        self.IN = IN
        self.NOM= NOM
        self.PAT= PAT
        self.ES= ES
        
    def pago(self):
        PAGMAT=5000
        if (self.PAT > 2000000) & (self.ES > 3):
          PAGMAT+= 00.3 * self.PAT
        return PAGMAT
    
    def print(self):
        print("EL ESTUDIANTE CON NUMERO DE INSCRIPCION" , self.IN ,"Y NOMBRE", self.NOM, "DEBE PAGAR: ", self.pago())
        
        
NUMERO = input(print("digita el numero de inscripcion: "))
NOMBRE= input(print("digita el nombre del estudiante: "))
PATRIMONIO= int(input(print("digita el patrimonio del estudiante: ")))
ESTRATO= int(input(print("digita el estrato del estudiante: ")))

matriculas=matricula(NUMERO,NOMBRE,PATRIMONIO,ESTRATO)
matriculas.print()