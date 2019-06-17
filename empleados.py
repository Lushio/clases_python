import numpy as np
registro = []

def registra_ingreso(nombre,hora):
	registro.append([nombre,hora])

def muestra_ingresos():
	total_empleados = len(empleados)
  #Se asume que la hora de llegada son las 800 hrs (8AM)
	hora_entrada = 800
	total_atrasos = 0
	suma_tiempo = 0
	
	for reg in registro:
		print(f"{reg[0]} llego a las {reg[1]}")
		if(reg[1] > hora_entrada):
			total_atrasos = total_atrasos + 1
			suma_tiempo = suma_tiempo + (reg[1] - hora_entrada)
			
	#pcent = float("{0:.2f}".format((total_atrasos*100)/total_empleados))
	pcent = (total_atrasos*100)/total_empleados
	print(f"El Porcentaje de Atrasos es de {pcent}%")
	
	prom_atraso = suma_tiempo/total_empleados
	print(f"El promedio de Atraso es de {prom_atraso} minutos")

empleados = ["Alejandro","Matias","Ivan","Marcelo","Marco","Eduardo","Beno","Cisco","Diego","JackBlack"]
empleados.sort()

for emp in empleados:
	print(f"Ingrese hora de llegada de {emp}")
	hor = int(input())
	#Llamamos a la funcion
	registra_ingreso(emp,hor)

#Luego de ingresarlos a todos mostramos listado
muestra_ingresos()
