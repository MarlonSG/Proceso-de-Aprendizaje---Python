"""
Version Desactualizada
FUNCION: CALCULADORA BASICA
"""

import sys

print("*** Calculadora en Python ***")

def logica_programa():
    salir = False

    while not salir:
        print("\nBienvendo, Escoja una opcion:")
        print("-----------------------")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir del Sistema")
        print("-----------------------")

        #Capturar opciones y digitos para los procesos
        opcion = int(input("Ingrese una opcion: "))

        if 1 <= opcion <= 4: #esto para evitar que pida a la hora de salir
            digito1 = float(input("\nIngrese el 1er numero: "))
            digito2 = float(input("Ingrese el 2do numero: "))

        if opcion == 1:
        #   print("\nSelecciono \"Sumar\"")
        #   digito1 = float(input("\nIngrese el 1er numero: "))
        #   digito2 = float(input("Ingrese el 2do numero: "))
            resultado = digito1 + digito2
            print(f"Resultado de la suma: {resultado:.2f}")
        elif opcion == 2:
        #   print("\nSelecciono \"Restar\"")
        #   digito1 = float(input("\nIngrese el 1er numero: "))
        #   digito2 = float(input("Ingrese el 2do numero: "))
            resultado = digito1 - digito2
            print(f"Resultado de la resta: {resultado}")
        elif opcion == 3:
        #   print("\nSelecciono \"Multiplicar\"")
        #   digito1 = float(input("\nIngrese el 1er numero: "))
        #   digito2 = float(input("Ingrese el 2do numero: "))
            resultado = digito1 * digito2
            print(f"Resultado de la multiplicacion: {resultado}")
        elif opcion == 4:
        #   print("\nSelecciono \"Dividir\"")
        #   digito1 = float(input("\nIngrese el 1er numero: "))
        #   digito2 = float(input("Ingrese el 2do numero: "))
            resultado = digito1 / digito2
            print(f"Resultado de la divion: {resultado}")
        elif opcion == 5:
            print("\nSaliendo del Sistema...\n")
            salir = True
            sys.exit(0)
        else:
            print("\nOpcion no valida, Ingrese otra opcion...")
    else:
        print("Gracias por ejecutarme :D")
    return "-----------------------"

print(logica_programa())