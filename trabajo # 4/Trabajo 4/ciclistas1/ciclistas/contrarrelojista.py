from .cicla.ciclista import Ciclista

class Contrarrelojista(Ciclista):
    def __init__(self, identificador, nombre, velocidad_maxima, tiempo_acumulado=0):
        super().__init__(identificador, nombre, tiempo_acumulado)
        self.__velocidad_maxima = velocidad_maxima

    def imprimir_tipo(self):
        return "Es un Contrarrelojista"

    def imprimir(self):
        return (super().imprimir() +
                f", Velocidad Máxima: {self.__velocidad_maxima} km/h")