print("*** SISTEMA DE GESTION DE ALARMAS ***")

def obtener_datos():
    while True:
        try:
            cantidad_alarmas = int(input("¿Cuantas alarmas vas a crear (máximo 5)?: ").strip())
            if 1 <= cantidad_alarmas <= 5:
                break
            else:
                print("El número de alarmas debe estar entre 1 y 5.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")
    return cantidad_alarmas


def procesar_alarmas(cantidad_alarmas):
    lista_alarmas = []
    for i in range(cantidad_alarmas):
        while True:
            try:
                alarma = float(input(f"Introduce la hora de inicio de la alarma {i+1}: ").strip())
                lista_alarmas.append(alarma)
                break
            except ValueError:
                print("Entrada inválida. Por favor, ingresa un número.")

    print("\nLas alarmas de inicio son:")
    for alarma in lista_alarmas:
        print(f"- {alarma:.2f}") # Formateo a dos decimales

    # Generación de nuevas alarmas en secuencia
    for alarma_inicial in lista_alarmas:
        nuevas_alarmas = []
        alarma_actual = alarma_inicial + 0.01
        nuevas_alarmas.append(alarma_actual)

        for _ in range(4):  # Genera 4 alarmas adicionales
            minutos = int(alarma_actual * 100) % 100 #extrae los minutos
            horas = int(alarma_actual) #extrae las horas
            minutos += 5
            if minutos >= 60:
                minutos -= 60
                horas += 1
            alarma_actual = horas + minutos / 100
            nuevas_alarmas.append(alarma_actual)
        print("--------------")
        print(f"Secuencia de nuevas alarmas para {alarma_inicial:.2f}: {['{:.2f}'.format(x) for x in nuevas_alarmas]}")


    return "--------------"


cantidad_alarmas = obtener_datos()
print(procesar_alarmas(cantidad_alarmas))