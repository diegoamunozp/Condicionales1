print (f"BIENVENIDO\n")

print(f"\n USE VALORES DECIMALES DEL 1.0 AL 5.0 (EJ: 50 = 5.0)")

Nota1 = float(input(f"Ingrese la nota No.1: "))
Nota2 = float(input(f"Ingrese la nota No.2: "))
Nota3 = float(input(f"Ingrese la nota No.3: "))

if Nota1 and Nota2 and Nota3 > 5.0 or Nota1 and Nota2 and Nota3 < 1.0:
    print("Alguna nota esta incorrecta y por ello invalida, reintentelo nuevamente")
    exit()

else:

    PromedioTem = Nota1 + Nota2 + Nota3
    PromedioFin = PromedioTem / 3

    if PromedioFin >= 3.0:
        print(f"Su promedio es {PromedioFin:.1f}\nHa aprobado")

    else:
        print(f"Su promedio es {PromedioFin:.1f}\nNo ha aprobado")

