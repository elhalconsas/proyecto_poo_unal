from tkinter import *

raiz = Tk()
raiz.title("trabajdadores")

frame = Frame(raiz, width=260, height=200)
frame.pack()


class Empleado:
    def __init__(self):
        self.nombre = StringVar()
        self.salario_hora = IntVar()
        self.horas_trabajadas = IntVar()
        
    def pedir(self):
        Label(frame, text="Ingrese el nombre del empleado:").grid(row=0, column=0, padx=3, pady=3)
        Entry(frame, textvariable=self.nombre).grid(row=0, column=1, padx=3, pady=3)

        Label(frame, text="Ingrese el salario básico por hora:").grid(row=1, column=0, padx=3, pady=3)
        Entry(frame, textvariable=self.salario_hora).grid(row=1, column=1, padx=3, pady=3)

        Label(frame, text="Ingrese el número de horas trabajadas en el mes:").grid(row=2, column=0, padx=3, pady=3)
        Entry(frame, textvariable=self.horas_trabajadas).grid(row=2, column=1, padx=3, pady=3)

        Button(frame, text="Calcular", command=lambda:self.mostrar_informacion()).grid(row=4, column=0, columnspan=2, pady=10)

    def calcular_salario_mensual(self):
        return self.salario_hora.get() * self.horas_trabajadas.get()

    def mostrar_informacion(self):
        salario_mensual = self.calcular_salario_mensual()
        if salario_mensual > 450000:
            Label(frame, text=f"Empleado: {self.nombre.get()}, Salario Mensual: ${salario_mensual}").grid(row=5, column=0, columnspan=2, pady=3)
        else:
            Label(frame, text=f"Empleado: {self.nombre.get()}").grid(row=5, column=0, columnspan=2, pady=3)

empleado = Empleado()
empleado.pedir()

raiz.mainloop()
