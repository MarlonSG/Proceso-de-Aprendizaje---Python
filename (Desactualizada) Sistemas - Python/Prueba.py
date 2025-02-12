from random import randint
import sys

print("*** Sistema de Practica ***")
print(""" Hola, soy ChikenBot, el asistente de este Software de Generación de Codigos Aleatorios... 
Elija una opcion para continuar: 
  1. Generar Codigo Aleatorio 
  2. Salir 
  """)

while True:
    try:
        opcion = int(input("Que opcion elige usted: "))
        if 1 <= opcion <= 2:
            break
        else:
            print("Ingrese una opcion entre 1 y 2...")
    except ValueError:
        print("Ingrese un numero Valido...")

def procesar_opcion(opcion):
    try:
        if opcion == 1:
            codigo = randint(1000,9999)
            return codigo
        elif opcion == 2:
            print("Bien, Hasta Luego...")
            sys.exit()
    except TypeError:
        print("Ha sucedido un problema...")
        return None

datos = procesar_opcion(opcion)

if datos is not None:
    print(f"Su codigo es: {datos}")

def continuar():
    while True:
        try:
            opcion_continuar = input("Desea generar otro codigo? (s/n): ")
            if opcion_continuar == str("s"):
                codigo = randint(1000,9999)
                print(f"Bien su nuevo codigo es: {codigo}")
            elif opcion_continuar == str("n"):
                print("Bien .... Hasta luego..")
                sys.exit()
            else:
                print("Ingrese una opcion (s/n)...")
        except TypeError:
            print("Ingrese una opcion Valida...")

continuar()