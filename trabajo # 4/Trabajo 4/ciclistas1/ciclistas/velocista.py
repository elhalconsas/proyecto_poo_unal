from .cicla.ciclista import Ciclista

class Velocista(Ciclista):
    def __init__(self, identificador, nombre, potencia_promedio, velocidad_sprint, tiempo_acumulado=0):
        super().__init__(identificador, nombre, tiempo_acumulado)
        self.__potencia_promedio = potencia_promedio
        self.__velocidad_sprint = velocidad_sprint

    def imprimir_tipo(self):
        return "Es un Velocista"

    def imprimir(self):
        return (super().imprimir() +
                f", Potencia Promedio: {self.__potencia_promedio} W, Velocidad Sprint: {self.__velocidad_sprint} km/h")
