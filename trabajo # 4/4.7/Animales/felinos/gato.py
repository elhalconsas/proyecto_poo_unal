from .felino import Felino

class Gato(Felino):
    def __init__(self, nombre_cientifico, sonido, alimentos, habitat="Hogares"):
        super().__init__(nombre_cientifico, sonido, alimentos, habitat)

    def comunicarse(self):
        return f"El {self.nombre_cientifico} maúlla como sonido principal."
