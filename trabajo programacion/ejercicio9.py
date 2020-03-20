peso = input("¿Cuanto pesas en kg? ")
altura = input("¿Cuantos medis en metros?")
imc = round(float(peso)/float(altura)**2,2)
print("Tu índice de masa corporal es: " + str(imc))
