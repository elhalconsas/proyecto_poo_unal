from .canido import Canido

class Lobo(Canido):
    def __init__(self, nombre_cientifico, sonido, alimentos, habitat="Bosques"):
        super().__init__(nombre_cientifico, sonido, alimentos, habitat)

    def comunicarse(self):
        return f"El {self.nombre_cientifico} emite un {self.sonido} para comunicarse."
