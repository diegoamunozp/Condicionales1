print("BIENVENIDOS")
print()

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

while True:
    print("\nMenú: ")
    print("1 - Convertir de Celsius a Fahrenheit")
    print("2 - Convertir de Fahrenheit a Celsius")
    print("3 - Salir")

    opcion = input("Seleccione una opción (1 - 3): ")

    if opcion == '1':

        try:
            celsius = float(input("Ingrese la temperatura en grados Celsius: "))
            fahrenheit = celsius_a_fahrenheit(celsius)

            print(f"{celsius} grados Celsius son equivalentes a {fahrenheit} grados Fahrenheit.")

        except ValueError:
            print("valor invalido, intentelo nuevamente")
                  
    elif opcion == '2':

        try:
            fahrenheit = float(input("Ingresa la temperatura en grados Fahrenheit: "))
            celsius = fahrenheit_a_celsius(fahrenheit)

            print(f"{fahrenheit} grados Fahrenheit son equivalentes a {celsius} grados Celsius.")

        except ValueError:
            print("Error: Debes ingresar un número válido.")

    elif opcion == '3':

        print("vuelva pronto")
        break
    else:
        print("Opción invalida, seleccione una opcion valida (1 - 3).")