print("BIENVENIDOS")
print()

Numero1 = float(input("Ingrese el primer número: "))
Numero2 = float(input("Ingrese el segundo número: "))
Numero3 = float(input("Ingrese el tercer número: "))

Lista = [Numero1, Numero2, Numero3]

ascendente = sorted(Lista)

descendente = sorted(Lista, reverse=True)

print(f"Números en orden ascendente: {ascendente}")

print(f"Números en orden descendente: {descendente}")
