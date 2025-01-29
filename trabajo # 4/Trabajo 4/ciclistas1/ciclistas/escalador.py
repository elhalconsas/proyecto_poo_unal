from .cicla.ciclista import Ciclista

class Escalador(Ciclista):
    def __init__(self, identificador, nombre, aceleracion_promedio, grado_rampa, tiempo_acumulado=0):
        super().__init__(identificador, nombre, tiempo_acumulado)
        self.__aceleracion_promedio = aceleracion_promedio
        self.__grado_rampa = grado_rampa

    def imprimir_tipo(self):
        return "Es un Escalador"

    def imprimir(self):
        return (super().imprimir() +
                f", Aceleración Promedio: {self.__aceleracion_promedio} m/s², Grado de Rampa: {self.__grado_rampa}°")
        
