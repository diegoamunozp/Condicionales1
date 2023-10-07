print("BIENVENIDOS A PIZZAS ARBELAEZ")
print()
print("Que pizza desea comprar?:")
print
print("1 - $15,000")
print("2 - $24,000")
print("3 - $36,000")

Tamaño = int(input("Seleccione el tamaño de la pizza (1 - 3): "))

Precios = {
    1: 15000,
    2: 24000,
    3: 36000
}

if Tamaño in Precios:
    Precios = Precios[Tamaño]

    print("CADA INGREDIENTE CUESTA $4.000")
    NIngredientes = int(input("Ingrese el número de ingredientes adicionales: "))
    
    PrecioIngredientes = NIngredientes * 4000

    Total = Precios + PrecioIngredientes

    print(f"El total a pagar es: ${Total}")
else:
    print("opcion invalida. reintentelo seleccione un tamaño válido (1 - 3).")
