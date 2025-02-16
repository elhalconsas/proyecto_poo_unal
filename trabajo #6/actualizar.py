import os
from tkinter import messagebox

documento = "friendsContact.txt"

class Actualizar:
    def __init__(self, nombre, numero):
        self.nombre = nombre
        self.numero = numero
        self.ejecutor()

    def ejecutor(self):
        if not os.path.exists(documento):
            messagebox.showerror("Error", "El archivo no existe")
            return
        
        actualizado = False
        lineas_nuevas = []
        
        with open(documento, "r") as file:
            lineas = file.readlines()
        
        for linea in lineas:
            partes = linea.strip().split()
            if len(partes) >= 2:
                nombre_actual = " ".join(partes[:-1])
                numero_actual = partes[-1]
                
                if nombre_actual == self.nombre:
                    lineas_nuevas.append(f"{self.nombre} {self.numero}\n")
                    actualizado = True
                else:
                    lineas_nuevas.append(linea)
            else:
                lineas_nuevas.append(linea)
        
        if actualizado:
            with open(documento, "w") as file:
                file.writelines(lineas_nuevas)
        else:
            messagebox.showerror("Error", "El nombre no existe en los contactos")
