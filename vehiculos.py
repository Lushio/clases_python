opcion = 0
registro = []
while (opcion != 2):
	print ("1 - Registrar Vehiculo")
	print ("2 - Salir")
	opcion = int(input("Ingrese Opcion: "))
	if (opcion == 1):
		print ("ingrese opcion")
		print ("1 - AUTO")
		print ("2 - CAMION")
		print ("3 - MOTO")
		registro.append(int(input()))
		
autos = 0
camion = 0
motos = 0
for r in registro:
	if r == 1:
		autos = autos + 1
	if r == 2:
		camion = camion + 1
	if r == 3:
		motos = motos + 1
		
print(f"Cantidad de Autos:\t{autos}")
print(f"Cantidad de Camiones:\t{camion}")
print(f"Cantidad de Motos:\t{motos}")
print(f"Porcentaje de Autos:\t{int((autos*100)/len(registro))}")
print(f"Porcentaje de Camiones:\t{int((camion*100)/len(registro))}")
print(f"Porcentaje de Motos:\t{int((motos*100)/len(registro))}")