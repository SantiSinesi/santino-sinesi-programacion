platai = float(input("¿Cuanto pensas invertir? "))
interesesa = float(input("¿Interés anual?(porcentaje) "))
tiempo = int(input("¿tiempo en años?"))
print("Plata final: " + str(round(platai * (interesesa / 100 + 1) ** tiempo, 2)))
