from tkinter import *
raiz= Tk()
raiz.title("datos de empleados ")

codigo = 0
nombre = ""
horas_trabajadas_mes = 0
valor_hora =0
retencion_fuente = 0.0
salario_bruto=0 
salario_neto=0
framePrincipal=Frame(raiz,width=1000, height=2000)
framePrincipal.pack()

class Empleado:      
  
        
    def grafica(self):
        def visualizar():
            etiquetaCodigo=Label(framePrincipal,text="Código:")
            etiquetaCodigo.grid(row=0, column=0, padx=3,pady=3,sticky="e")
            
            etiquetaNombre=Label(framePrincipal,text="Nombre:")
            etiquetaNombre.grid(row=1, column=0, padx=3,pady=3,sticky="e")
            
            etiquetaHoras=Label(framePrincipal,text="Horas trabajadas al mes:")
            etiquetaHoras.grid(row=2, column=0, padx=3,pady=3,sticky="e")
            
            etiquetaValHora=Label(framePrincipal,text="Valor hora:")
            etiquetaValHora.grid(row=3, column=0, padx=3,pady=3,sticky="e")
            
            etiquetaRetFuente=Label(framePrincipal,text="Retención en la fuente:")
            etiquetaRetFuente.grid(row=4, column=0, padx=3,pady=3,sticky="e")
        visualizar()
        def pedir():
            self.codigo = StringVar()
            self.nombre = StringVar()
            self.horas_trabajadas_mes = IntVar()
            self.valor_hora = IntVar()
            self.retencion_fuente = DoubleVar()

            Entry(framePrincipal, textvariable=self.codigo).grid(row=0, column=1, padx=3, pady=3)
            Entry(framePrincipal, textvariable=self.nombre).grid(row=1, column=1, padx=3, pady=3)
            Entry(framePrincipal, textvariable=self.horas_trabajadas_mes).grid(row=2, column=1, padx=3, pady=3)
            Entry(framePrincipal, textvariable=self.valor_hora).grid(row=3, column=1, padx=3, pady=3)
            Entry(framePrincipal, textvariable=self.retencion_fuente).grid(row=4, column=1, padx=3, pady=3)

        pedir()

    def salario(self):
        self.retencion_fuente = self.retencion_fuente.get() / 100
        self.salario_bruto = self.horas_trabajadas_mes.get() * self.valor_hora.get()
        self.salario_neto = self.salario_bruto - (self.salario_bruto * self.retencion_fuente)
    
    def mostrar(self):
        Label(framePrincipal, text=f"El código del empleado es: {self.codigo.get()}").grid(row=5, column=0, padx=3, pady=3, columnspan=2)
        Label(framePrincipal, text=f"El nombre del empleado es: {self.nombre.get()}").grid(row=6, column=0, padx=3, pady=3, columnspan=2)
        Label(framePrincipal, text=f"El salario bruto del empleado es: {self.salario_bruto}").grid(row=7, column=0, padx=3, pady=3, columnspan=2)
        Label(framePrincipal, text=f"El salario neto del empleado es: {self.salario_neto}").grid(row=8, column=0, padx=3, pady=3, columnspan=2)

sujeto1 = Empleado()
sujeto1.grafica()

# Añadir un botón para calcular el salario y mostrar los resultados
Button(framePrincipal, text="Calcular Salario", command=lambda: [sujeto1.salario(), sujeto1.mostrar()]).grid(row=9, column=0, columnspan=2, pady=10)

raiz.mainloop()