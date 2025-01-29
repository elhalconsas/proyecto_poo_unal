from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nombre_cientifico, sonido, alimentos, habitat):
        self.nombre_cientifico = nombre_cientifico
        self.sonido = sonido
        self.alimentos = alimentos
        self.habitat = habitat

    @abstractmethod
    def obtener_habitat(self):
        pass

    @abstractmethod
    def comunicarse(self):
        pass
