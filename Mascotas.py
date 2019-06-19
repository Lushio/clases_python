import numpy as np

chip    = np.empty(3,dtype='object')
mascota  = np.empty(3,dtype='object')
c = 0
chip[0] = "a001"
chip[1] = "a002"
mascota[0] = "kuki"
mascota[1] = "puki"
c = 2
while True:
    print("MENU\n1 Ingresar\n2 Modificar\n3 Eliminar\n4 Mostrar\n0 Salir")
    opcion = int(input("digita opcion: "))
    if opcion == 0:
        break;
    elif opcion == 1:
        if c >= len(chip):
            print("excede capacidad, no puede agregar")
        else:
            chip[c]     = input("codigo del chip: ")
            mascota[c]  = input("nombre de la mascota: ")
            c = c + 1
    elif opcion == 2:
        print("Modificar")
        resultado = np.where(chip == input("codigo del chip: "))
        cantidad = len(resultado[0])
        if cantidad == 0:
            print("dato no encontrado")
        else:
            indice = resultado[0][0]
            print(f"mascota = {mascota[indice]}")
    elif opcion == 3:
        print("Eliminar")
    elif opcion == 4:
        print("Mostrar")
        print(mascota)
    else:
        print("opcion incorrecta")
print("gracias por utilizar programa")
        
