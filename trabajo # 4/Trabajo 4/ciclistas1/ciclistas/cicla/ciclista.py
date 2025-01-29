from abc import ABC, abstractmethod

class Ciclista(ABC):
    def __init__(self, identificador, nombre, tiempo_acumulado=0):
        self.__identificador = identificador
        self.__nombre = nombre
        self.__tiempo_acumulado = tiempo_acumulado  # Se inicializa con un valor dado

    @abstractmethod
    def imprimir_tipo(self):
        """Método abstracto para imprimir el tipo de ciclista"""
        pass

    def imprimir(self):
        return (f"Ciclista ID: {self.__identificador}, Nombre: {self.__nombre}, "
                f"Tiempo Acumulado: {self.__tiempo_acumulado} min")

    def actualizar_tiempo(self, tiempo):
        """Permite actualizar el tiempo acumulado del ciclista"""
        self.__tiempo_acumulado += tiempo

    def get_tiempo_acumulado(self):
        return self.__tiempo_acumulado
