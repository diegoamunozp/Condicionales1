print("BIENVENIDO")

Nombre = input(f"Ingrese su nombre:\n")
Edad = int(input(f"Ingrese su edad:\n "))

if Edad < 0 or Edad > 100:
    print("Esta edad es incorrecta, intentelo de nuevo")
    exit()

else: 
    if Edad >= 18:
        print (f"Nombre: {Nombre} \nEdad: {Edad} \nUsted es mayor de edad")

    else: 
        print (f"Nombre: {Nombre} \nEdad: {Edad} \nUsted es menor de edad")       