# Funcion que muestra un arreglo de unidimensional como filas y columnas, 
# la unica condicion es que la cantidad de filas multiplicada por la 
# cantidad de columnas debe ser igual a la dimension del arreglo. 

# Los parametros que recibe la funcion son: un arreglo, numero de filas
# y numero de columnas.

# La funcion está hecha para funcionar con un arreglo numpy de zeros en
# donde los ceros son elementos vacios y cualquier otro valor es un
# elemento ocupado que se mostrara como una X

import numpy as np

def FilasYColumnas (arreglo, filas, columnas):
	alphabet = list(map(chr, range(65, 91)))
	if(filas*columnas == len(arreglo)):
		c = 0
		print(f"[ ]" , end =" ")
		for y in range(columnas):
			print(f"[{alphabet[y]}]" , end =" ")
		print("\n")
		for x in range(filas):
			print(f"[{x+1}]", end =" ")
			for y in range(columnas):
				if (arreglo[c] == 0):
					print("[ ]", end =" ")
				else:
					print("[X]", end =" ")
				c = c + 1
			print("\n")
	else:
		print("ERROR: no cuadra la cantidad de filas y columnas con la dimension del arreglo")
		

# Creamos un array de zeros en numpy y ocupamos algunos valores
arr = np.zeros((60,), dtype=int)
arr[7] = 1
arr[23] = 1
arr[15] = 1
arr[20] = 1
arr[30] = 1
arr[45] = 1
arr[52] = 1

# Finalmente llamamos a la funcion 
FilasYColumnas(arr, 10, 6)


# aqui va otro comentario profe de como hacer filas y comlumnas 

import numpy as np

def CargarAsientos():
    global asientos
    asientos = np.empty([33,6], dtype='object')
    for i in range(0,33):
        for j in range(0,6):
            asientos[i][j] = ' - '

def MostrarAsientos():
    print('      A     B     C     D     E     F')
    for i in range(0,33):
        if i < 9:
            print(f'{i+1}  {asientos[i]}')
        else:
            print(f'{i+1} {asientos[i]}')

def ComprarPasaje(fila, columna):
    if columna.upper() == 'A':
        columna = 0
    elif columna.upper() == 'B':
        columna = 1
    elif columna.upper() == 'C':
        columna = 2
    elif columna.upper() == 'D':
        columna = 3
    elif columna.upper() == 'E':
        columna = 4
    elif columna.upper() == 'F':
        columna = 5
    else:
        print('Debe ingresar una columna válida: A, B, C, D, E o F')
    if columna in (0, 1, 2, 3, 4, 5):
        if fila in range(0,33):
            asientos[fila-1, columna]=" X "
         

CargarAsientos()
MostrarAsientos()
ComprarPasaje(1,'A')
MostrarAsientos()