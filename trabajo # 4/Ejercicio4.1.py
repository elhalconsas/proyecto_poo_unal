class cuenta :
    def __init__(self, saldo, tasa_anual):
        self.saldo = saldo
        self.numero_consignaciones = 0
        self.numero_retiros = 0
        self.tasa_anual = tasa_anual
        self.comision_mensual = 0
    def consignar(self, cantidad):
        self.saldo += cantidad  
        self.numero_consignaciones += 1 
    def retirar(self, cantidad):
        nuevo_saldo =self.saldo- cantidad
        if nuevo_saldo>=0:
            self.saldo -= cantidad
            self.numero_retiros += 1
        else:
           print("La cantida a retirar excede el saldoactual.");
    def calcularInterés(self):
        self.tasa_mentual = self.tasa_anual/12
        intereses_mensuales = self.saldo * self.tasa_mentual
        self.saldo += intereses_mensuales
    def extractoMensual(self):
        self.saldo -= self.comision_mensual
        self.calcularInterés()
        
        
class cuenta_de_ahorros(cuenta):
    def __init__(self, saldo, tasa_anual):
        super().__init__(saldo, tasa_anual)
        self.activa = saldo >= 10000

    def retirar(self, cantidad):
        if self.activa:
            super().retirar(cantidad)
            
    def consignar(self, cantidad):
        if self.activa:
            super().consignar(cantidad)
    def extractoMensual(self):
        if self.numero_retiros > 4:
            self.comision_mensual +=(self.numero_retiros - 4)*1000
        super().extractoMensual()
        if self.saldo < 10000:
            self.activa = False 
    def imprimir(self):
        print("Saldo: $", self.saldo)
        print("Comision mensual= $ ", self.comision_mensual)
        print("Numero de trasacciones: ", self.numero_consignaciones + self.numero_retiros, "\n")


class CuentaCorriente(cuenta):  
    def __init__(self,saldo, tasa_anual):
        super().__init__(saldo, tasa_anual)
        self.sobre_giro = 0
        
    def retirar(self, cantidad):
        resultado= self.saldo -cantidad
        if resultado < 0 :
            self.sobre_giro += resultado
            self.saldo = 0
        else:
            super().retirar(cantidad)
    def consignar(self, cantidad):
        residuo = float(self.sobre_giro - cantidad)
        saldo, self.tasa_anual
        if (self.sobregiro > 0) :
            if ( residuo > 0):
                self.sobregiro = 0
                saldo = residuo
            else :
                self.sobregiro = residuo
                saldo = 0
        else:
            super().consignar(cantidad)
    def extractoMensual(self):
        super().extractoMensual()
    
    def imprimir(self):
        print("Saldo: $", self.saldo)
        print("Carga mensual= $", self.comision_mensual)
        print("Numero de trasacciones: ", self.numero_consignaciones + self.numero_retiros)
        print("Valor del sobregiro: $", (self.numero_consignaciones + self.numero_retiros) ,"\n")   
class PruebaCuenta:
    def __init__(self):
       print("Cuenta de ahorros")
    saldo_inicial_ahorros = float(input("Ingrese saldo inicial=$: "))
    tasa_ahorros = float(input("Ingrese tasa de interés= "))

    cuenta1 = cuenta_de_ahorros(saldo_inicial_ahorros, tasa_ahorros)

    cantidad_depositar = float(input("Ingresar cantidad a consignar: $"))
    cuenta1.consignar(cantidad_depositar)

    cantidad_retirar = float(input("Ingresar cantidad a retirar: $"))
    cuenta1.retirar(cantidad_retirar)

    cuenta1.extractoMensual()

    print("Saldo: $", cuenta1.saldo)
    print("Comisión mensual: $", cuenta1.comision_mensual)
    print("Número de transacciones: ", cuenta1.numero_consignaciones + cuenta1.numero_retiros)
    cuenta1.imprimir()
    


if __name__ == "__main__":
    PruebaCuenta()
