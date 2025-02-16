import os
from tkinter import *
from tkinter import messagebox
from leer_amigos import Leer_Amigos  
from añadir_amigos import Añadir_amigos  
from actualizar import Actualizar
from eliminar import Eliminar



documento = "friendsContact.txt"

def verificar_archivo(ruta):
    archivo_existe = os.path.exists(ruta)
    
    if not archivo_existe:
        print(f"El archivo '{ruta}' no existe. Creando un nuevo archivo...")
        with open(ruta, 'w') as archivo:
            pass  
        archivo_existe = False  
    else:
        print(f"El archivo '{ruta}' existe.")
    
    return archivo_existe

ventana = Tk()
ventana.title("Agenda")
ventana.geometry("300x100")

miFrame = Frame(ventana)
miFrame.pack()

class Interfaz:
    def __init__(self):
   
        self.archivo_existe = verificar_archivo(documento)
        
        Label(miFrame, text="Nombre:").grid(row=0, column=0, pady=5)
        Label(miFrame, text="Número:").grid(row=1, column=0, pady=10)

        self.nombre_entry = Entry(miFrame)
        self.nombre_entry.grid(row=0, column=1, columnspan=3)

        self.numero_entry = Entry(miFrame)
        self.numero_entry.grid(row=1, column=1, columnspan=3)

        Button(miFrame, text="Añadir", command=self.añadir).grid(row=2, column=0, padx=10)
        Button(miFrame, text="Leer", command=self.leer).grid(row=2, column=1, padx=10)
        Button(miFrame, text="Actualizar", command=self.actualizar).grid(row=2, column=2, padx=10)
        Button(miFrame, text="Eliminar", command=self.eliminar).grid(row=2, column=3, padx=10)

    def añadir(self):
        Añadir_amigos(self.nombre_entry.get(), self.numero_entry.get())

    def leer(self):
        leer_amigos = Leer_Amigos() 
        nombre_buscado = self.nombre_entry.get()
        numero_buscado = self.numero_entry.get()

        if nombre_buscado:
            numero = leer_amigos.Nombre(nombre_buscado)
            if numero:
                self.numero_entry.delete(0, END)
                self.numero_entry.insert(0, numero)
        elif numero_buscado:
            nombre = leer_amigos.Numero(numero_buscado)
            if nombre:
                self.nombre_entry.delete(0, END)
                self.nombre_entry.insert(0, nombre)
        else:
            messagebox.showinfo("Resultado", "Ingresa un nombre o número para buscar")
   
    def actualizar(self):
       Actualizar(self.nombre_entry.get(), self.numero_entry.get())
       
    def eliminar(self):
        Eliminar(self.nombre_entry.get())
        self.nombre_entry.delete(0, END)
        self.numero_entry.delete(0, END)
       

if __name__ == "__main__":
    Interfaz()
    ventana.mainloop()
