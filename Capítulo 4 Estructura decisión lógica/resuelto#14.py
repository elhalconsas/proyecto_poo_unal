
VD1 = float(input("El número de ventas del departamento 1 es: "))
VD2 = float(input("El número de ventas del departamento 2 es: "))
VD3 = float(input("El número de ventas del departamento 3 es: "))
SALAR = float(input("¿Cuál es el salario de los vendedores en los departamentos?: "))


TOTVEN = VD1 + VD2 + VD3  
PORVEN = 0.33 * TOTVEN  
SALAR1 = SALAR2 = SALAR3 = 0  


if VD1 > PORVEN:
    SALAR1 = SALAR + 0.2 * SALAR
else:
    SALAR1 = SALAR

if VD2 > PORVEN:
    SALAR2 = SALAR + 0.2 * SALAR
else:
    SALAR2 = SALAR

if VD3 > PORVEN:
    SALAR3 = SALAR + 0.2 * SALAR
else:
    SALAR3 = SALAR

print(f"Salario vendedores departamento 1: ${SALAR1}")
print(f"Salario vendedores departamento 2: ${SALAR2}")
print(f"Salario vendedores departamento 3: ${SALAR3}")