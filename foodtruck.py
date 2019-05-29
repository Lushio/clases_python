# definir funcion menu
def mostrar_menu():
	print ("1 - Bebida\t\t$500")
	print ("2 - Papas Fritas\t$1300")
	print ("3 - Completo Aleman\t$1000")
	print ("4 - Completo Italiano\t$1400")
	print ("")
	print ("5 - Pagar Cuenta")

#precios de productos
ita = 1400
ale = 1000
beb = 500
papa = 1300

#cantidades llevadas
cant_ita = 0
cant_ale = 0
cant_beb = 0
cant_papa = 0

op = 0
while op != 5:
	mostrar_menu()
	# leemos la opcion
	op = int(input("Ingrese una Opcion: "))
	if op == 1:
		cant_beb = cant_beb + 1
	if op == 2:
		cant_papa = cant_papa + 1
	if op == 3:
		cant_ale = cant_ale + 1
	if op == 4:
		cant_ita = cant_ita + 1

total_sin_prop = (ita*cant_ita) + (ale*cant_ale) + (beb*cant_beb) + (papa*cant_papa)

#calcular propina
propina = int(total_sin_prop * 0.1)

#calcular total CON propina
total_con_prop = int(total_sin_prop * 1.1)

print (f"=== CUENTA ===\n")
print (f"Bebidas x {cant_beb}\t\t ${beb*cant_beb}")
print (f"Italianos x {cant_ita}\t\t ${ita*cant_ita}")
print (f"Alemanes x {cant_ale}\t\t ${ale*cant_ale}")
print (f"Papas x {cant_papa}\t\t ${papa*cant_papa}")
print ("")
print (f"Total SIN propina:\t\t${total_sin_prop}")
print (f"Propina Sugerida 10%:\t\t${propina}")
print (f"Total CON propina:\t\t${total_con_prop}")
