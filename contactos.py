import numpy as np

def MostrarMenu():
	op = 0
	while (op != 3):
		print("===Agenda Telefonica===")
		print("")
		print("1. Agregar Contacto")
		print("2. Mostrar Contactos")
		print("3. SALIR")
		print("")
		op = int(input("Opcion: "))
		
		if (op == 1):
			n = input("Ingrese Nombre: ")
			t = int(input("Ingrese Telefono: "))
			CrearContacto(n,t)
			
		if (op == 2):
			MostrarContactos()

def CrearContacto(nombre, telefono):
	print(f"Ud. ha ingresado: {nombre}, Tel:{telefono}")
	# Creamos un array con el Nombre y Telefono ingresados
	arr = [nombre, telefono]
	# Agregamos el array creado dentro del array "contactos"
	contactos.append(arr)
	# Ordenamos la lista de contactos
	contactos.sort()

def MostrarContactos():
	print("Nombre\t\tTelefono")
	for c in contactos:
		print(f"{c[0]}\t{c[1]}")

# Creamos un Array vacio para almacenar contactos
contactos = []
# Llamamos a la Funcion mostrar menu
MostrarMenu()
