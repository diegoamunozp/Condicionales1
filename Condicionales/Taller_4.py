print(f"BIENVENIDO\n")

Numero1 = float(input("Ingrese el primer numero: "))
Numero2 = float(input("Ingrese el segundo numero: "))

if Numero1 > Numero2:
    
    NumMayor = Numero1
    NumMenor = Numero2

elif Numero2 > Numero1:

    NumMayor = Numero2
    NumMenor = Numero1

else:
    print("Los dos numeros son iguales")
    exit()

print(f"\nNumero mayor: {NumMayor}\n\nNumero Menor: {NumMenor}\n")
print(f"{NumMayor} es mayor que {NumMenor}")

