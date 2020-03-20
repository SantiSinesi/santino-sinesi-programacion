pan = int(input("pan vendido que no son frescas: "))
precio = 3.49 
descuento = 0.6
coste = pan * precio * (1 - descuento)
print("El coste de una barra de pan fresca es de" + str(precio) + "€")
print("El descuento sobre una barra de pan que no es fresca es de" + str(descuento * 100) + "%")
print("El coste final es " + str(round(coste, 2)) + "€")
