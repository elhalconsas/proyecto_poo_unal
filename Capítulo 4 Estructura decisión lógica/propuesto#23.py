import math 

A = float(input("Ingrese el valor de A (coeficiente de x^2): "))
B = float(input("Ingrese el valor de B (coeficiente de x): "))
C = float(input("Ingrese el valor de C (término independiente): "))


if A == 0:
    print("El valor de A no puede ser 0. Esto no es una ecuación de segundo grado.")
else:
   
    discriminante = B**2 - 4*A*C

    
    if discriminante > 0:
        
        x1 = (-B + math.sqrt(discriminante)) / (2 * A)
        x2 = (-B - math.sqrt(discriminante)) / (2 * A)
        print(f"Las soluciones son reales y distintas: x1 = {x1:.2f}, x2 = {x2:.2f}")
    elif discriminante == 0:
       
        x = -B / (2 * A)
        print(f"Las soluciones son reales e iguales: x1 = x2 = {x:.2f}")
    else:
       
        real = -B / (2 * A)
        imaginaria = math.sqrt(abs(discriminante)) / (2 * A)
        print(f"Las soluciones son complejas:")
        print(f"x1 = {real:.2f} + {imaginaria:.2f}i")
        print(f"x2 = {real:.2f} - {imaginaria:.2f}i")
