print("BIENVENIDOS")
print()

CantidadArticulos = int(input("Ingrese la cantidad de artículos comprados: "))
PrecioUnitario = float(input("Ingrese el precio unitario original: "))

Descuento5 = 0.05  
Descuento8 = 0.08  

if CantidadArticulos <= 5:
    PrecioUnitarioDescuento = PrecioUnitario

elif 5 < CantidadArticulos < 10:
    PrecioUnitarioDescuento = PrecioUnitario * (1 - Descuento5)

else:
    PrecioUnitarioDescuento = PrecioUnitario * (1 - Descuento8)


valor_total_pagar = CantidadArticulos * PrecioUnitarioDescuento

print(f"El valor total a pagar es: {valor_total_pagar}")