print("*** El Mayor de 2 Numeros v1 ***")

def obtenerNumeros():
    while True:
        try:
            numero1 = float(input("Ingresa el numero 1: ").strip())
            numero2 = float(input("Ingresa el numero 2: ").strip())
            return numero1, numero2  # Retorna ambos números como una tupla
        except ValueError:
            print("Ingrese datos validos por favor...")



def calculoNumeros(num1, num2):  # Ahora recibe los números directamente
    if num1 > num2:
        print(f"\nEl numero {num1:.2f} es mayor que el numero {num2:.2f}")
    elif num2 > num1:
        print(f"\nEl numero {num2:.2f} es mayor que el numero {num1:.2f}")
    else:
        print(f"\nLos números {num1:.2f} y {num2:.2f} son iguales") # Maneja el caso de igualdad


datos = obtenerNumeros()

if datos:  # Simplificado: si datos no está vacío (es decir, se recibieron los dos números)
    num1, num2 = datos  # Desempaqueta la tupla
    calculoNumeros(num1, num2)  # Llama a la función con los dos números            
     