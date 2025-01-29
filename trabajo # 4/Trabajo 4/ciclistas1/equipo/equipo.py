class Equipo:
    def __init__(self, nombre_equipo, pais):
        self.__nombre_equipo = nombre_equipo
        self.__pais = pais
        self.__ciclistas = []

    def agregar_ciclista(self, ciclista):
        self.__ciclistas.append(ciclista)

    def actualizar_tiempos(self, tiempos):
        """Actualiza los tiempos de los ciclistas segun la lista proporcionada."""
        for ciclista, tiempo in zip(self.__ciclistas, tiempos):
            ciclista.actualizar_tiempo(tiempo)

    def imprimir_equipo(self):
        print(f"Equipo: {self.__nombre_equipo}, Pais: {self.__pais}")
        for ciclista in self.__ciclistas:
            print(ciclista.imprimir())

    def tiempo_total_equipo(self):
        """Calcula y muestra el tiempo total acumulado del equipo."""
        total = sum(c.get_tiempo_acumulado() for c in self.__ciclistas)
        print(f"Tiempo total del equipo: {total} min")
