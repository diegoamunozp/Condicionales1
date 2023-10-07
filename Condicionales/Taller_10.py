llantas = int(input("Ingrese el número de llantas que compro: "))

PrecioUnitario = 0

if llantas < 6:
    PrecioUnitario = 240000

elif llantas <= 7:
    PrecioUnitario = 221000

else:
    PrecioUnitario = 180000

Total = llantas * PrecioUnitario

print(f"El valor total a pagar por {llantas} llantas es \n ${Total}")

print("BIENVENIDOS")

Llantas = int(input("Ingrese el numero de llantas compradas: "))

PrecioUnitario = 0

if Llantas < 6:
    PrecioUnitario = 240000

elif Llantas <= 7:
    PrecioUnitario = 221000

else:
    PrecioUnitario = 180000

Total = PrecioUnitario + Llantas 

print(f"El valor a pagar por {Llantas} es: {Total} con un precio unitario de {PrecioUnitario}")




