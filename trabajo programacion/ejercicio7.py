tiempo = float(input("Tiempo de trabajo en horas: "))
precio = float(input("Cuanto cobras por hora?: "))
sueldo = round(tiempo * precio, 3)
print("Tu sueldo es " + str(sueldo))
