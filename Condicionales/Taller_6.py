import math

def cuadrado():

    print('Has elegido "Calcular el area de un Cuadrado"')
    print()

    print("RECUERDE QUE EN UN CUADRADO TODOS LOS LADOS SON IGUALES")
    print()

    Lado = float(input("Ingrese las medidas del lado del cuadrado: "))

    Area = Lado ** 2

    print()
    print(f"El área del cuadrado es: {Area}")

def rectangulo():

    print('Has elegido "Calcular el area de un Rectángulo"')
    print()

    Base = float(input("Ingrese la base del rectángulo: "))

    Altura = float(input("Ingrese la altura del rectángulo: "))

    Area = Base * Altura

    print()
    print(f"El área del rectángulo es: {Area}")

def triangulo():
    print('Has elegido "Calcular el area de un Triángulo"')

    Altura = float(input("Ingrese la altura del triangulo: "))
    Base = float(input("Ingrese la base del triangulo: "))

    Area = 0.5 * Base * Altura

    print(f"El area del triángulo es: {Area}")

def circulo():
    print('Has elegido "Calcular el area de un Círculo"')

    Radio = float(input("Ingrese el radio del circulo: "))

    Area = math.pi * Radio ** 2

    print(f"El área del círculo es: {Area}")

def rombo():
    print('Has elegido "Calcular el area de un Rombo"')

    DiagonalMayor = float(input("Ingrese la diagonal mayor del rombo: "))
    DiagonalMenor = float(input("Ingrese la diagonal menor del rombo: "))

    Area = (DiagonalMayor * DiagonalMenor) / 2

    print(f"El area del rombo es {Area} ")

def trapecio():
    print('Has elegido "Calcular el area de un Trapecio"')

    LongitudMayor = float(input("Ingrese la longitud de la base mayor del trapecio: " ))
    LongitudMenor = float(input("Ingrese la longitud de la base menor del trapecio: " ))
    Altura = float(input("Ingrese la altura del trapecio: "))

    Area = 0.5 * (LongitudMayor + LongitudMenor) + Altura

    print(f"El area del trapecio es {Area} ")

def salir():
    print('VUELVA PRONTO')
    

print(f"BIENVENIDOS\n\n")

print("Seleccione una opcion:")
print("1) Calcular el area de un Cuadrado")
print("2) Calcular el area de un Rectángulo")
print("3) Calcular el area de un Triángulo")
print("4) Calcular el area de un Círculo")
print("5) Calcular el area de un Rombo")
print("6) Calcular el area de un Trapecio")
print("7) Salir")

opcion = input("Opcion: ")

if opcion == '1':
    cuadrado()
elif opcion == '2':
    rectangulo()
elif opcion == '3':
    triangulo()
elif opcion == '4':
    circulo()
elif opcion == '5':
    rombo()
elif opcion == '6':
    trapecio()
elif opcion == '7':
    salir()
else:
    print("Opción no válida. Por favor, seleccione una opción válida.")
