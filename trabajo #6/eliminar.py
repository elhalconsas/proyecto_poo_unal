import os
from tkinter import messagebox
documento = "friendsContact.txt"
class Eliminar:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ejecutor()

    def ejecutor(self):
        if not os.path.exists(documento):
            return
        
        lineas_nuevas = []
        eliminado = False
        
        with open(documento, "r") as file:
            lineas = file.readlines()
        
        for linea in lineas:
            partes = linea.strip().split()
            if len(partes) >= 2:
                nombre_actual = " ".join(partes[:-1])
                
                if nombre_actual != self.nombre:
                    lineas_nuevas.append(linea)
                else:
                    eliminado = True
        
        if eliminado:
            with open(documento, "w") as file:
                file.writelines(lineas_nuevas)
        else:
            messagebox.showerror("Error", "El nombre no existe en los contactos")
