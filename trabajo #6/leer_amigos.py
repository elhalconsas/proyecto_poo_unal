import re
from tkinter import messagebox


documento ="friendsContact.txt"

class Leer_Amigos:
    def Nombre(self, nombre):
        self.nombre = nombre

        patron = re.compile(r'^\s*(\S+)\s+(\S+)\s*$')
        
        with open(documento, "r") as archivo:
            for line in archivo:
                match = patron.match(line)
                if match:
                    nombres, numero = match.groups()
                    if nombres == self.nombre:
                        return numero
           

    def Numero(self, numero):
        self.numero = numero
      
        patron = re.compile(r'^\s*(\S+)\s+(\S+)\s*$')
        
        with open(documento, "r") as archivo:
            for line in archivo:
                match = patron.match(line)
                if match:
                    nombres, numeros = match.groups()
                    if numeros == self.numero:
                        return nombres
            

    def Comprobar(self):
        # Patrón que coincide con nombre y número separados por espacios
        patron = re.compile(r'^\s*(\S+)\s+(\S+)\s*$')
        
        with open(documento, 'r') as archivo:
            for line in archivo:
                match = patron.match(line)
                if match:
                    nombre, numero = match.groups()
                    if nombre == self.nombre or numero == self.numero:
                        return False
        return True
