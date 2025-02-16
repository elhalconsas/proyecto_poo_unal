import os
from tkinter import messagebox


documento = "friendsContact.txt"

class Añadir_amigos:
    def __init__(self, nombre, numero):
        self.nombre = nombre
        self.numero = numero
        print(self.nombre, self.numero, "está en proceso")
        self.ejecutor()  
        
    def ejecutor(self):
       
        if not os.path.exists(documento):
            with open(documento, 'w') as archivo:
                pass  

        if not self.comprobar():  
            with open(documento, "a") as archivo:  
                archivo.write(str(self.nombre) + " " + str(self.numero) + "\n")
                print("Se ha añadido el contacto")
        else:
            messagebox.showerror("Error", "El contacto ya existe")
                
    def comprobar(self):
        with open(documento, 'r') as archivo:
            for line in archivo:
                nombre, numero = line.strip().split()
                if nombre == self.nombre or numero == self.numero:
                    return True  
        return False
