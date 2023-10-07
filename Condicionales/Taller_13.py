Peso = float(input("Ingrese el peso en KILOGRAMOS: "))
Estatura = float(input("Ingrese la estatura en METROS: "))

MasaCo = Peso / (Estatura ** 2)

if MasaCo < 18.5:
    Salud = "Desnutrido, bro un batido no va mal"

elif 18.5 <= MasaCo < 25:
    Salud = "Normal, god"

elif 25 <= MasaCo < 30:
    Salud = "Sobrepeso, come menos y ejercitate"

elif 30 <= MasaCo < 35:
    Salud = "Obesidad Grado 1, bro entraste a donde no querias, ejercitate mas"

elif 35 <= MasaCo < 40:
    Salud = "Obesidad Grado 2, como es posible subir aqui, bro deja de comer y EJERCITATE"

elif 40 <= MasaCo < 50:
    Salud = "Obesidad Grado 3, 💀💀💀"

else:
    Salud = "   Obesidad Grado 4, F bro"

print(f"Índice de Masa Corporal (IMC): {MasaCo:.2f}")
print(f"Estado de salud: {Salud}")
