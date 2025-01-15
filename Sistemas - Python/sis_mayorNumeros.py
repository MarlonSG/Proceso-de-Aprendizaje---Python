print("*** EL MAYOR DE 2 NUMEROS ***")

def obtenerNumeros():
    numero1 = float(input("Ingresa el numero 1: ").strip())
    numero2 = float(input("Ingresa el numero 2: ").strip())
    return numero1, numero2

def cauloNumeros (numero1, numero2):
    if numero1 > numero2:
        print(f"\nEl numero {numero1} es mayor que el numero {numero2}")
    else:
        print(f"\nEl numero {numero2} es mayor que el numero {numero1}")
    return
numero1, numero2 = obtenerNumeros()

print(cauloNumeros(numero1, numero2))