#Mostrar horas y minutos de un día.

for hora in range (24):
	for minuto in range (60):
	
		if (minuto < 10):
			minuto = "0" + str(minuto)
			
		print (f"{hora}:{minuto}")