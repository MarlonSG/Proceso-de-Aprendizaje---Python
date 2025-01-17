print("*** Sistema de Menu Interactivo ***")

def logica_programa():
    salir = False
    while not salir:
        print("""*** Menu Interactivo ***
        1. Crear Cuenta
        2. Eliminar Cuenta
        3. Salir""")
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            print("Creando una Nueva")
        elif opcion == 3:
            print("Saliendo del Sistema...\n")
            salir = True
        else:
            print("Opcion no valida, Ingrese otra opcion...\n")
    else:
        print("Gracias por ejecutarme :D\n")
    return "-----------------------"

print(logica_programa())