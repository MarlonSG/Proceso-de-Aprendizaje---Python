"""
FUNCION: SIMULADOR DE CAJERO AUTOMATICO CON FUNCIONES DE GESTIONAR SALDO MEDIANTE OPCIONES
"""

import sys

print("*** Sistema de Cajero automatico ***")

def logica_programa():
    saldo = 0
    salir = False

    while not salir:
        print("\n*** Menu Interactivo ***")
        print("-----------------------")
        print("1. Depositar Saldo")
        print("2. Retirar Saldo")
        print("3. Consultar Saldo")
        print("4. Salir del sistema")
        print("-----------------------")
        opcion = int(input("Ingrese una opcion: "))

        if opcion == 1:
            deposito = float(input("\n¿Cuanto saldo desea depositar? "))
            saldo += deposito
            print(f"Saldo Disponible: ${saldo}\n")

        elif opcion == 2:
            retiro = float(input("\n¿Cuanto saldo desea retirar? "))
            saldo -= retiro
            print(f"Saldo Disponible: ${saldo}\n")

        elif opcion == 3:
            print(f"\nSaldo Dsiponible: {saldo}")

        elif opcion == 4:
            print("\nSaliendo del Sistema...\n")
            salir = True
            sys.exit(0)
        else:
            print("\nOpcion no valida, Ingrese otra opcion...\n")
    else:
        print("Gracias por ejecutarme :D\n")
    return "-----------------------"

print(logica_programa())