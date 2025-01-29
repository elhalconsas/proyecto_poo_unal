from ciclistas.velocista import Velocista
from ciclistas.escalador import Escalador
from ciclistas.contrarrelojista import Contrarrelojista
from equipo.equipo import Equipo

if __name__ == "__main__":
    
    velocista = Velocista(1, "Carlos", 400, 70, 35)
    escalador = Escalador(2, "Ana", 3.5, 25, 40)
    contrarrelojista = Contrarrelojista(3, "Luis", 60, 30)

  
    equipo = Equipo("Team Python", "España")
    equipo.agregar_ciclista(velocista)
    equipo.agregar_ciclista(escalador)
    equipo.agregar_ciclista(contrarrelojista)

  
    equipo.imprimir_equipo()

    
    nuevos_tiempos = [5, 7, 3]  
    equipo.actualizar_tiempos(nuevos_tiempos)

    print("\nDespués de la actualización de tiempos:")
    equipo.imprimir_equipo()

    
    equipo.tiempo_total_equipo()

