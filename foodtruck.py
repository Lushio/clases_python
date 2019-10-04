# definir funcion menu
def mostrar_menu(): 
	print ("1 - Gaseosa (Soda)\t\t$690")
	print ("2 - Papas Fritas (chips)\t$1500")
	print ("3 - Completo Aleman (hot dog German)\t$1300")
	print ("4 - Completo Italiano  (hot dog Italian)\t$1800")
	print ("")
	print ("5 - Pagar Cuenta (pay bill) (p)")

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
	op = int(input("Ingrese una Opcion (add a option): "))
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

print (f"=== CUENTA (account)===\n")
print (f"Bebidas (soda)x {cant_beb}\t\t ${beb*cant_beb}")
print (f"Italianos (hot dog italinas)x {cant_ita}\t\t ${ita*cant_ita}")
print (f"Alemanes (hot dog germans) x {cant_ale}\t\t ${ale*cant_ale}")
print (f"Papas (chips)x {cant_papa}\t\t ${papa*cant_papa}")
print ("")
print (f"Total SIN propina (payment):\t\t${total_sin_prop}")
print (f"Propina Sugerida 10% (tip):\t\t${propina}")
print (f"Total CON propina (payment with tip):\t\t${total_con_prop}")


# He traducido los terminos en ingles , para aquellos usuarios del habla ingles del instituo duoc 
