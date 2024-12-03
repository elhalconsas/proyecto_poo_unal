VALCOMP = int(input("¿Cuánto es el valor de la compra?: "))
COLOR = input("¿De qué color es la pintura que comprará (AZUL, AMARILLO, VERDE, BLANCO)? ").upper()

VALPAG = 0
PDES = 0
if COLOR == "BLANCO":
  PDES = 0
elif COLOR == "VERDE":
  PDES = 10
elif COLOR == "AMARILLO":
  PDES = 25
elif COLOR == "AZUL":
  PDES = 50
else:
  print("Color no válido. Por favor, ingrese BLANCO, VERDE, AMARILLO o AZUL.")
  exit()

VALPAG = VALCOMP - PDES * VALCOMP / 100

print("El cliente debe pagar $:", round(VALPAG, 2))
