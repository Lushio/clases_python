# Una empresa frutícola, ha comenzado la cosecha de 
# paltas y requiere almacenar la cantidad de kilos 
# de paltas que cosecha cada trabajador. La empresa 
# tiene 15 empleados. Se requiere mostrar la 
# información de cada empleado y el total cosechado 
# por todos.

import numpy as np
cosecha = np.empty(15, dtype=int)

for i in range(0,len(cosecha)):
	cosecha[i] = int(input(f"ingrese kilos del trabajador {i+1}\n"))
	
print("Kilos recolectados por cada trabajador")
print(cosecha)

# la funcion numpy.sum suma todos los elementos
# de un array de numeros ^^
total = np.sum(cosecha)
print(f"total de kilos: {total}")
