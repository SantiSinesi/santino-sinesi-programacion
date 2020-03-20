inversionp = float(input("Cuanto vas a empezar invirtiendo?: "))
interes = 0.04
balance1 = inversionp * (1 + interes)
print("Balance despues del primer año:" + str(round(balance1, 2)))
balance2 = balance1 * (1 + interes)
print("Balance despues del segundo año:" + str(round(balance2, 2)))
balance3 = balance2 * (1 + interes)
print("Balance despues del tercer año:" + str(round(balance3, 2)))
