print("*** El Mayor de 2 Numeros v1 ***")

def obtenerNumeros():
    while True:
        try:
            numero1 = float(input("\nIngresa el Primer Numero: ").strip())
            numero2 = float(input("Ingresa el Segundo Numero: ").strip())
            return numero1, numero2  # Retorna ambos números como una tupla
        except ValueError:
            print("\nIngrese datos validos por favor...")



def calculoNumeros(num1, num2):  # Ahora recibe los números directamente
    if num1 > num2:
        print(f"\nEl numero {num1} es mayor que el numero {num2}")
    elif num1 < num2:
        print(f"\nEl numero {num2} es mayor que el numero {num1}")
    else:
        print(f"\nLos números {num1} y {num2} son iguales") # Maneja el caso de igualdad


datos = obtenerNumeros()

if datos:  # Simplificado: si datos no está vacío (es decir, se recibieron los dos números)
    num1, num2 = datos  # Desempaqueta la tupla
    calculoNumeros(num1, num2)  # Llama a la función con los dos números            
     