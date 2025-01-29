from .felino import Felino

class Leon(Felino):
    def __init__(self, nombre_cientifico, sonido, alimentos, habitat="Sabana"):
        super().__init__(nombre_cientifico, sonido, alimentos, habitat)

    def comunicarse(self):
        return f"El {self.nombre_cientifico} ruge para comunicarse y demostrar dominio."
