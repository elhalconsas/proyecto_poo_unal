from caninos.lobo import Lobo
from caninos.Perro import Perro
from felinos.gato import Gato
from felinos.leon import Leon

lobo = Lobo("Canis lupus", "Aullido", "Carnívoro")
perro = Perro("Canis lupus familiaris", "Ladrido", "Omnívoro")
gato = Gato("Felis catus", "Maullido", "Carnívoro")
leon = Leon("Panthera leo", "Rugido", "Carnívoro")

animales = [lobo, perro, gato, leon]

for animal in animales:
    print(f"Nombre científico: {animal.nombre_cientifico}")
    print(f"Hábitat: {animal.obtener_habitat()}")
    print(f"Comunicación: {animal.comunicarse()}")
    print("-" * 40)
