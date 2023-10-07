print("BIENVENIGOD")

MontoCuenta = float(input("Ingrese el monto que tiene en su cuenta: "))

if MontoCuenta < 150000:
    Pago = "Paga en efectivo"

elif 150000 <= MontoCuenta <= 300000:
    Pago = "Paga con el celular"

elif 300000 < MontoCuenta <= 600000:
    Pago = "Paga en tarjeta de débito"

else:
    Pago = "Paga en tarjeta de crédito"

print(f"se uso y pago con {Pago} como metodo de pago")