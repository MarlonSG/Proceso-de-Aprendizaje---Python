menu = """
Bienvenidos al conversor de monedas plus!!

¿Que tipo de moneda tienes ?, elige una opción:

1- Soles Peruanos
2- Pesos argentinos
3- Euros Europeos

"""

def calculos(tipo_pesos, valor_dolar):
    try:
        plata = float(input("¿Cuanto dinero " + tipo_pesos + " tienes?: "))
        if plata < 0:
            raise ValueError("La cantidad de dinero no puede ser negativa.")
        dolares = plata / valor_dolar
        dolares = round(dolares, 2)
        print("Tienes $" + str(dolares) + " dolares")
    except ValueError as e:
        print(f"Error: {e}")
    except ZeroDivisionError:
        print("Error: El valor del dólar no puede ser cero.")

while True: # Bucle para que el programa se repita hasta que el usuario decida salir.
    print(menu) # Imprime el menú ANTES de pedir la opción.
    try:
        opcion = int(input("Ingrese su opción: "))
        if opcion < 1 or opcion > 3:
            raise ValueError("Opción fuera de rango.")
        break # Sale del bucle si la opción es válida.
    except ValueError:
        print("Por favor, ingrese un número entero válido entre 1 y 3.")
    except KeyboardInterrupt: # Manejo de interrupción con Ctrl+C
        print("\nPrograma terminado por el usuario.")
        exit()

if opcion == 1:
    calculos("Soles", 3.35)

elif opcion == 2:
    calculos("argentinos", 65)

elif opcion == 3:
    calculos("euros", 4.24)

# Ya no es necesario el else porque el bucle 'while' ya se encarga de validar la opción.