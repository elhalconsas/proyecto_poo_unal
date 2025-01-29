from .canido import Canido

class Perro(Canido):
    def __init__(self, nombre_cientifico, sonido, alimentos, habitat="Doméstico"):
        super().__init__(nombre_cientifico, sonido, alimentos, habitat)

    def comunicarse(self):
        return f"El {self.nombre_cientifico} ladra como sonido principal."
