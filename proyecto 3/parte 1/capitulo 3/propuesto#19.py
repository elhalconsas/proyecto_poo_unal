from tkinter import *
import math

raiz = Tk()
raiz.title("Datos de un Triángulo")
Principal = Frame(raiz, width=1000, height=2000)
Principal.pack()
 
class triangulo:
    def __init__(self):
       
        self.ladoA = StringVar()
        self.ladoB = StringVar()
        self.ladoC = StringVar()
        self.pedir()

    def pedir(self):
    
        Label(Principal, text="Lado A:").grid(row=0, column=0, padx=3, pady=3)
        Entry(Principal, textvariable=self.ladoA).grid(row=0, column=1, padx=3, pady=3)
        
        Label(Principal, text="Lado B:").grid(row=1, column=0, padx=3, pady=3)
        Entry(Principal, textvariable=self.ladoB).grid(row=1, column=1, padx=3, pady=3)
        
        Label(Principal, text="Lado C:").grid(row=2, column=0, padx=3, pady=3)
        Entry(Principal, textvariable=self.ladoC).grid(row=2, column=1, padx=3, pady=3)
        

        Button(Principal, text="Calcular", command=lambda:self.print()).grid(row=3, column=0, columnspan=2, pady=10)

    def perimetro(self,):
        perimetros = float(self.ladoA.get()) + float(self.ladoB.get()) + float(self.ladoC.get())
        return perimetros
    
    def altura(self,):
        base = float(self.ladoC.get()) / 2
        alturas = math.sqrt((float(self.ladoA.get())**2) - (base**2))
        return alturas
    
    def area(self):
        areas = (float(self.ladoC.get()) * self.altura()) / 2
        return areas
    def print(self):
   
        altura = self.altura()
        perimetro = self.perimetro()
        area = self.area()

        Label(Principal, text=f"La altura del triángulo es: {altura:.2f}").grid(row=4, column=0, columnspan=2, padx=3, pady=3)
        Label(Principal, text=f"El perímetro del triángulo es: {perimetro:.2f}").grid(row=5, column=0, columnspan=2, padx=3, pady=3)
        Label(Principal, text=f"El área del triángulo es: {area:.2f}").grid(row=6, column=0, columnspan=2, padx=3, pady=3)


triangulos = triangulo()


raiz.mainloop()
