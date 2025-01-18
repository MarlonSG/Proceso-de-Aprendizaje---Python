#Modificar mas adelante

from random import randint

print("*** Juego de Adivinanzas ***")

def juego():
    numero_aleatorio = randint(1,10)
    intentos = 0

    print("Adivina el numero entre el 1 y 10 para ganar: ")
    opcion = int(input("Escribe un numero entre 1 y 10: "))

    while not opcion == numero_aleatorio:
        intentos += 1
        if opcion < numero_aleatorio <= 10:
             print("\nEl numero sorpresa es mayor que este numero")
             opcion = int(input("\nEscribe un numero entre 1 y 10: "))
        elif opcion > numero_aleatorio <= 10:
            print("\nEl numero sorpresa es menor que este numero")
            opcion = int(input("\nEscribe un numero entre 1 y 10: "))
    print(f"\n¡Ganaste en {intentos} intentos! El número era {numero_aleatorio}")

    return "___________________________"

print(juego())