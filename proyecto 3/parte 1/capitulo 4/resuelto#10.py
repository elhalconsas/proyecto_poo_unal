from tkinter import *

raiz = Tk()
raiz.title("Cálculo de Matrícula")

frame = Frame(raiz, width=1000, height=2000)
frame.pack()

class matricula:
    def __init__(self):
        self.IN = IntVar()
        self.NOM = StringVar()
        self.PAT = IntVar()
        self.ES = IntVar()

    def pago(self):
        PAGMAT = 50000
        if self.PAT.get() > 2000000 and self.ES.get() > 3:
            PAGMAT += 0.03 * self.PAT.get()
        return PAGMAT

    def print(self):
        Label(frame, text="El estudiante con número de inscripción " +str(self.IN.get()) + " y nombre " +self.NOM.get() + " debe pagar: " +str(self.pago())).grid(row=5, column=0, columnspan=2, padx=3, pady=3)

    def pedir_datos(self):
        Label(frame, text="Ingrese el número de inscripción:").grid(row=0, column=0, padx=3, pady=3)
        Entry(frame, textvariable=self.IN).grid(row=0, column=1, padx=3, pady=3)

        Label(frame, text="Ingrese el nombre del estudiante:").grid(row=1, column=0, padx=3, pady=3)
        Entry(frame, textvariable=self.NOM).grid(row=1, column=1, padx=3, pady=3)

        Label(frame, text="Ingrese el patrimonio del estudiante:").grid(row=2, column=0, padx=3, pady=3)
        Entry(frame, textvariable=self.PAT).grid(row=2, column=1, padx=3, pady=3)

        Label(frame, text="Ingrese el número de semestres cursados:").grid(row=3, column=0, padx=3, pady=3)
        Entry(frame, textvariable=self.ES).grid(row=3, column=1, padx=3, pady=3)

        Button(frame, text="Calcular", command=self.print).grid(row=4, column=0, columnspan=2, pady=10)

matriculas = matricula()
matriculas.pedir_datos()
raiz.mainloop()
