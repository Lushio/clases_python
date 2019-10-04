personas = []

personas.append("Daniel")
personas.append("Marcelo")
personas.append("Alejandro")
personas.append("Marco")

print (personas)
print (personas[2])

frutas = ["manzana", "platano", "melon"]

for x in frutas:
    print(f"Es el dia del {x}")

print ("agrego otra fruta")

frutas.append("kiwi")

for x in frutas:
    print(f"Es el dia del {x}")



# Aqui tengo otro ejemplo simple de como funcionan los arreglos de forma simple utilizando numpy
import numpy as np
asientosA = np.arange(1,10,1)
print(f"A {asientosA}")
print(f"B {asientosA}")
print(f"C {asientosA}")
print(f"D {asientosA}")
print(f"E {asientosA}")
print(f"F {asientosA}")


vueloA = []
contador = 0
while contador < 9:
    vueloA.append(asientosA[contador])
    contador +=1


print(vueloA)
print("elija fila")
respuesta = input()

if respuesta == "a":
    print("escogiste la fila A")
    print("Numero de posicion")
    fila = int(input())
    asientosA[fila] = "X"
print(vueloA)