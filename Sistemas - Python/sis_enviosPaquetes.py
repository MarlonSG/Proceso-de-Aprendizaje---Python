print("*** Sistema de Envios de Paquetes ***")

def obtener_informacion():
    destino = input("\nEl envio sera Nacional o Internacional?: ").strip().lower()
    peso = float(input("Cuanto pesa en Kg el paquete?: ").strip())
    return destino, peso

def calcular_envio(destino, peso):
    if destino == "nacional":
        costo_total = peso * 10
        print(f"\nEl envio es Nacional")
        print(f"el precio total sera de ${costo_total:.2f}")
    elif destino == "internacional":
        costo_total = peso * 20
        print(f"\nEl envio es Internacional")
        print(f"el precio total sera de ${costo_total:.2f}")
    else:
        print("\nEl destino ingresado no se reconoce correctamente")
    return ""

destino, peso = obtener_informacion()

print(calcular_envio(destino, peso))