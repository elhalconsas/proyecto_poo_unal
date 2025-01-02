from tkinter import *
import math 

raiz = Tk()
raiz.title("trabajdadores")

frame = Frame(raiz, width=260, height=200)
frame.pack()

class comparacion:
    def __init__(self):
        self.A = IntVar()
        self.B = IntVar()
        self.C = IntVar()
        self.pedir()
    def pedir(self):
        
        Label(frame, text="Ingrese el valor de A (Ax^2): ").grid(row=0, column=0,padx=3, pady=3)
        Entry(frame, textvariable=self.A).grid(row=0, column=1,padx=3, pady=3)
        Label(frame, text="Ingrese el valor de B (Bx): ").grid(row=1, column=0,padx=3, pady=3)
        Entry(frame, textvariable=self.B).grid(row=1, column=1,padx=3, pady=3)
        Label(frame, text="Ingrese el valor de C (C): ").grid(row=2, column=0,padx=3, pady=3)
        Entry(frame, textvariable=self.C).grid(row=2, column=1,padx=3, pady=3)
        Button(frame,text="calcular las comparaciones",command=lambda:self.claculo()).grid(row=3, column=0,padx=3, pady=3,columnspan=2)
    def claculo(self):
        A = self.A.get()
        B = self.B.get()
        C = self.C.get()
        if A == 0:
            Label(frame, text="El valor de A no puede ser 0. Esto no es una ecuación de segundo grado.").grid(row=4, column=0, columnspan=2, padx=3, pady=3)
        else:
            discriminante = B**2 - 4*A*C
            if discriminante > 0:
                x1 = (-B + math.sqrt(discriminante)) / (2 * A)
                x2 = (-B - math.sqrt(discriminante)) / (2 * A)
                Label(frame, text="Las soluciones son reales y distintas:").grid(row=4, column=0, columnspan=2, padx=3, pady=3)
                Label(frame, text=f"x1 = {x1:.2f}").grid(row=5, column=0, columnspan=2, padx=3, pady=3)
                Label(frame, text=f"x2 = {x2:.2f}").grid(row=6, column=0, columnspan=2, padx=3, pady=3)
            elif discriminante == 0:
                x = -B / (2 * A)
                Label(frame, text="Las soluciones son reales e iguales:").grid(row=4, column=0, columnspan=2, padx=3, pady=3)
                Label(frame, text=f"x1 = x2 = {x:.2f}").grid(row=5, column=0, columnspan=2, padx=3, pady=3)
            else:
                real = -B / (2 * A)
                imaginaria = math.sqrt(abs(discriminante)) / (2 * A)
                Label(frame, text="Las soluciones son complejas:").grid(row=4, column=0, columnspan=2, padx=3, pady=3)
                Label(frame, text=f"x1 = {real:.2f} + {imaginaria:.2f}i").grid(row=5, column=0, columnspan=2, padx=3, pady=3)
                Label(frame, text=f"x2 = {real:.2f} - {imaginaria:.2f}i").grid(row=6, column=0, columnspan=2, padx=3, pady=3)

ejecutar = comparacion()

raiz.mainloop()