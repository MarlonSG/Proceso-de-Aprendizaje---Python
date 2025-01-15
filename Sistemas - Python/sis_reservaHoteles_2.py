print("*** Sistema de Reserva de Hoteles v2 ***")

def obtener_informacion():
    nombre_cliente = input("\nIngrese el nombre del cliente: ").strip()
    dias_estadia = int(input("Ingrese la dia de la estadia: ").strip())
    vista_mar = input("¿Desea con Vista al Mar? (Si / No): ").strip().lower()
    return nombre_cliente, dias_estadia, vista_mar

def calcular_precios(dias_estadia, vista_mar):
    precio_con_vista = 190.50
    precio_sin_vista = 150.50

    if vista_mar == "si":
        precio_total = precio_con_vista * dias_estadia
        print(f"El precio total es: ${precio_total:.2f}")
        print(f"¿Habitacion con Vista al Mar? : {vista_mar}")

    else:
        precio_total = precio_sin_vista * dias_estadia
        print(f"El precio total es: ${precio_total:.2f}")
        print(f"¿Habitacion con Vista al Mar? : {vista_mar}")
    return "\n-----------------------------"


nombre_cliente, dias_estadia, vista_mar = obtener_informacion()

print(f"\nHola {nombre_cliente}")
print(f"Dias de Estadia: {dias_estadia}")
print(calcular_precios(dias_estadia, vista_mar))