from tkinter import *
raiz= Tk()
raiz.title("Comparación que es mayor")

frame= Frame(raiz,width=1000, height=2000)
frame.pack()


class comparacion:
    def __init__(self):

        self.A = IntVar()
         
        self.B = IntVar()
    
    
    def proceso(self):
        if self.A.get() > self.B.get():
            Label(frame, text="A es mayor que B").grid(row=3, column=0, columnspan=2, padx=3, pady=3)
        elif self.A.get() == self.B.get():
            Label(frame, text="A es igual a B").grid(row=3, column=0, columnspan=2, padx=3, pady=3)
        elif self.A.get() < self.B.get():
            Label(frame, text="A es menor que B").grid(row=3, column=0, columnspan=2, padx=3, pady=3)
            
    def pedir(self):
        Label(frame, text="Ingrese el número A:").grid(row=0, column=0, padx=3, pady=3)
        Entry(frame, textvariable=self.A).grid(row=0, column=1, padx=3, pady=3)
        
        Label(frame, text="Ingrese el número B:").grid(row=1, column=0, padx=3, pady=3)
        Entry(frame, textvariable=self.B).grid(row=1, column=1, padx=3, pady=3)
        
        Button(frame, text="Comparar", command=lambda:self.proceso()).grid(row=2, column=0, columnspan=2, pady=10)    
        
comparar = comparacion()
comparar.pedir()        
raiz.mainloop()
