valor_emp = 500
num_clientes = int(input("Ingrese Cantidad de Clientes "))

# Crea un Array vacío con el numero de clientes
clientes = [0] * num_clientes

# Asigna la cantidad de empanadas que lleva cada cliente
i = 0
while i < len(clientes):
    clientes[i] = int(input("Ingrese Cantidad de Empanadas: "))
    i += 1

# Recorre el arreglo y calcula totales y descuentos
for c in clientes:
	print (f"*** Cliente ***")
	print (f"{c} Empanadas")
	subtotal = c * valor_emp
	print (f"Subtotal:\t{subtotal}")
	descuento = 0
	if (c>=5 and c<=10):
		descuento = 0.08
	if (c>=11 and c<=30):
		descuento = 0.12
	if (c>=31 and c<=50):
		descuento = 0.16
	if (c>50):
		descuento = 0.25
	total = int(subtotal - (subtotal*descuento))
	print (f"Descuento:\t{int(subtotal*descuento)}")
	print (f"Valor Total:\t{total}")
