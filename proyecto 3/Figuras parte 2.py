import math
from tkinter import *

raiz = Tk()
raiz.title("trabajdadores")
frame1 = Frame(raiz, width=260, height=200, bg="lightblue")
frame1.grid(row=0, column=0, padx=5, pady=5)

frame2 = Frame(raiz, width=260, height=200, bg="lightgreen")
frame2.grid(row=1, column=0, padx=5, pady=5)
def limpiar_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

class circulo:
    def __init__(self):
        limpiar_frame(frame2)
        self.radio=IntVar()
        Label(frame2,text="Ingrese el radio del circulo: ").grid(row=0, column=0, padx=3, pady=3)
        Entry(frame2, textvariable=self.radio).grid(row=0, column=1, padx=3, pady=3)
        
        Button(frame2, text="Calcular", command=lambda:self.calcular()).grid(row=1, column=0, padx=3, pady=3, columnspan=2)
    def calcular(self):
        self.calcular_area()
        self.calcular_perimetro()
    def calcular_area(self):
        area= math.pi * self.radio.get()**2
        Label(frame2,text=f"El area del circulo es = {area}").grid(row=2, column=0, columnspan=2, pady=3)
    def calcular_perimetro(self):
        preimtro= 2 * math.pi * self.radio.get()
        Label(frame2,text=f"El perimetro del circulo es = {preimtro}").grid(row=3, column=0, columnspan=2, pady=3)
    
class rectangulo:

    def __init__(self,):
        limpiar_frame(frame2)
        self.base = IntVar()
        self.altura = IntVar()
        Label(frame2,text="Ingrese la base del rectangulo: ").grid(row=0, column=0, padx=3, pady=3)
        Entry(frame2, textvariable=self.base).grid(row=0, column=1, padx=3, pady=3)
        
        Label(frame2,text="Ingrese la altura del rectangulo: ").grid(row=1, column=0, padx=3, pady=3)
        Entry(frame2, textvariable=self.altura).grid(row=1, column=1, padx=3, pady=3)    
        Button(frame2, text="Calcular", command=lambda:self.calcular()).grid(row=2, column=0, padx=3, pady=3, columnspan=2)
        
    def calcular(self):
        self.calcular_area()
        self.calcular_perimetro()
        
    def calcular_area(self):
        area=self.base.get() * self.altura.get()
        Label(frame2,text=f"El area del rectangulo es = {area}").grid(row=2, column=0, columnspan=2, pady=3)
    def calcular_perimetro(self):
        perimtro=(2 * self.base.get()) + (2 * self.altura.get())
        Label(frame2,text=f"El perimetro del rectangulo es = {perimtro}").grid(row=3, column=0, columnspan=2, pady=3)

class cuadrado:

    def __init__(self):
        limpiar_frame(frame2)
        self.lado =IntVar()
        Label(frame2,text="Ingrese el lado del cuadrado: ").grid(row=0, column=0, padx=3, pady=3)
        Entry(frame2, textvariable=self.lado).grid(row=0, column=1, padx=3, pady=3)
        Button(frame2, text="Calcular", command=lambda:self.calcular()).grid(row=1, column=0, padx=3, pady=3, columnspan=2)
        
    def calcular(self):
        self.calcular_area()
        self.calcular_perimetro()

    def calcular_area(self):
        area= math.pow(self.lado.get(), 2)
        Label(frame2,text=f"El area del cuadrado es = {area}").grid(row=2, column=0, columnspan=2, pady=3)
        
    def calcular_perimetro(self):
        perimetro= self.lado.get() * 4
        Label(frame2,text=f"El perimetro del cuadrado es = {perimetro}").grid(row=3, column=0, columnspan=2, pady=3)
               
class triangulo_rectangulo:

    def __init__(self):
        limpiar_frame(frame2)
        self.base = IntVar()
        self.altura = IntVar()
        Label(frame2,text="Ingrese la base del triangulo: ").grid(row=0, column=0, padx=3, pady=3)
        Entry(frame2, textvariable=self.base).grid(row=0, column=1, padx=3, pady=3)
        
        Label(frame2,text="Ingrese la altura del triangulo: ").grid(row=1, column=0, padx=3, pady=3)
        Entry(frame2, textvariable=self.altura).grid(row=1, column=1, padx=3, pady=3)
        
        Button(frame2, text="Calcular", command=lambda:self.calcular()).grid(row=2, column=0, padx=3, pady=3, columnspan=2)
        
    def calcular(self):
        self.calcular_area()
        self.calcular_hipotenusa()
        self.calcular_perimetro()
        self.determinar_tipo_de_triangulo()

    def calcular_area(self):
        area=(self.base.get() * self.altura.get()) / 2
        Label(frame2,text=f"El area del triangulo es = {area}").grid(row=3, column=0, columnspan=2, pady=3)
    def calcular_hipotenusa(self):
        return math.sqrt(self.base.get() ** 2 + self.altura.get() ** 2 )
    
    def calcular_perimetro(self):
        perimetro=self.base.get() + self.altura.get() + self.calcular_hipotenusa()
        Label(frame2,text=f"El perimetro del triangulo es = {perimetro}").grid(row=4, column=0, columnspan=2, pady=3)
        
    def determinar_tipo_de_triangulo(self):
        hipotenusa = self.calcular_hipotenusa()
        if self.base.get() == self.altura.get() == hipotenusa:
            Label(frame2,text="Es un triangulo equilatero").grid(row=5, column=0, columnspan=2, pady=3)

        elif self.base.get() != self.altura.get() and self.base.get() != hipotenusa and self.altura.get() != hipotenusa:
            Label(frame2,text="Es un triangulo escaleno").grid(row=5, column=0, columnspan=2, pady=3)

        else: Label(frame2,text="Es un triangulo isosceles").grid(row=5, column=0, columnspan=2, pady=3)

class rombo:
    def __init__(self):
        limpiar_frame(frame2)
        self.diagonal_1 = IntVar()
        self.diagonal_2 = IntVar()
        
        Label(frame2,text="Ingrese la diagonal 1 del rombo: ").grid(row=0, column=0, padx=3, pady=3)
        Entry(frame2, textvariable=self.diagonal_1).grid(row=0, column=1, padx=3, pady=3)
        
        Label(frame2,text="Ingrese la diagonal 2 del rombo: ").grid(row=1, column=0, padx=3, pady=3)
        Entry(frame2, textvariable=self.diagonal_2).grid(row=1, column=1, padx=3, pady=3)
        
        Button(frame2, text="Calcular", command=lambda:self.calcular()).grid(row=3, column=0, padx=3, pady=3, columnspan=2)
    def calcular(self):
        self.calcular_area()
        self.calcular_perimetro()
        
    def calcular_area(self):
        area=(self.diagonal_1.get()* self.diagonal_2.get()) / 2
        Label(frame2,text=f"El area del rombo es = {area}").grid(row=4, column=0, columnspan=2, pady=3)
        
    def calcular_perimetro(self):
        lado= math.sqrt((self.diagonal_1.get() / 2)**2 + (self.diagonal_2.get() / 2)**2)   
        perimtro= lado* 4
        Label(frame2,text=f"El perimetro del rombo es = {perimtro}").grid(row=5, column=0, columnspan=2, pady=3)

class trapecio:
    def __init__(self):
        limpiar_frame(frame2)
        self.base_1 = IntVar()
        self.base_2 = IntVar()
        self.altura = IntVar()
        self.lado_1 = IntVar()
        self.lado_2 = IntVar()
        
        Label(frame2,text="Ingrese la base 1 del trapecio: ").grid(row=0, column=0, padx=3, pady=3)
        Entry(frame2, textvariable=self.base_1).grid(row=0, column=1, padx=3, pady=3)
        
        Label(frame2,text="Ingrese la base 2 del trapecio: ").grid(row=1, column=0, padx=3, pady=3)
        Entry(frame2, textvariable=self.base_2).grid(row=1, column=1, padx=3, pady=3)
        
        Label(frame2,text="Ingrese la altura del trapecio: ").grid(row=2, column=0, padx=3, pady=3)
        Entry(frame2, textvariable=self.altura).grid(row=2, column=1, padx=3, pady=3)
        
        Label(frame2,text="Ingrese el lado 1 del trapecio: ").grid(row=3, column=0, padx=3, pady=3)
        Entry(frame2, textvariable=self.lado_1).grid(row=3, column=1, padx=3, pady=3)
        
        Label(frame2,text="Ingrese el lado 2 del trapecio: ").grid(row=4, column=0, padx=3, pady=3)
        Entry(frame2, textvariable=self.lado_2).grid(row=4, column=1, padx=3, pady=3)
        

    def calcular_area(self):
        
        area = ((self.base_1.get() + self.base_2.get()) * self.altura.get()) / 2
        Label(frame2,text=f"El area del trapecio es = {area}").grid(row=5, column=0, columnspan=2, pady=3)
    def calcular_perimetro(self):
        perimtro = self.base_1.get() + self.base_2.get() + self.lado_1.get() + self.lado_2.get() 
        Label(frame2,text=f"El perimetro del trapecio es = {perimtro}").grid(row=6, column=0, columnspan=2, pady=3)

class prueba_figuras:
    def __init__(self):
        Label(frame1,text="elige el pipo de figura que quieres calcular").grid(row=0, column=1, columnspan=4, pady=3)
      
        Button(frame1, text="circulo", command=lambda:circulo(),).grid(row=1, column=0,padx=2, pady=2)  
        Button(frame1, text="rectangulo", command=lambda:rectangulo()).grid(row=1, column=1, padx=2, pady=2)
        Button(frame1, text="cuadrado", command=lambda:cuadrado()).grid(row=1, column=2, padx=2, pady=2)  
        Button(frame1, text="triangulo", command=lambda:triangulo_rectangulo()).grid(row=1, column=3, padx=2, pady=2)
        Button(frame1, text="rombo", command=lambda:rombo()).grid(row=1, column=4,padx=2, pady=2)
        Button(frame1, text="trapecio", command=lambda:trapecio()).grid(row=1, column=5, padx=2, pady=2)

        

figuras=prueba_figuras()

raiz.mainloop()