NOM = input(print("el nombre del tranajador es: "))
NHT = int(input(print(" cuantas horas trabajo", NOM , ": ")))
VHN = int(input(print("cuanto es el valor por hora? ")))
HET = int(0) 
salario = 0
HEE8 = int(0)

if NHT>40:
  print("el trabajador ", HET, "devengo: $", HEE8 )
  HET= NHT-40
elif HET > 8:
    HEE8 = HET-8
    salario = 40 * VHN + 16 * VHN + HEE8 * 3 * VHN
else:
    salario= 40 * VHN + HET * 2 * VHN
    
salario = NHT * VHN

print("el trabajador ", NOM, "devengo: $",salario)
