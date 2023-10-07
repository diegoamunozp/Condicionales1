print("EL ULTIMO BIENVENIDOS PAPUS")
print()

Edad = int(input("Ingrese su edad: "))

print(f"Ingrese su genero\n1 - Femenino\n2 - Masculino")
Genero = int(input("= "))


if Genero == 1:  
    FrecuenciaCardiaca = (220 - Edad) / 10

elif Genero == 2:  
    FrecuenciaCardiaca = (210 - Edad) / 10

else:
    print("Género invalido. Intentelo nuevamente")
    FrecuenciaCardiaca = None

if FrecuenciaCardiaca is not None:
    print(f"Número de pulsaciones por cada 10 segundos: {FrecuenciaCardiaca}")
