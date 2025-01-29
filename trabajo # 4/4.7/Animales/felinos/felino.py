from animal import Animal

class Felino(Animal):
    def __init__(self, nombre_cientifico, sonido, alimentos, habitat="Terrestre"):
        super().__init__(nombre_cientifico, sonido, alimentos, habitat)

    def obtener_habitat(self):
        return self.habitat
