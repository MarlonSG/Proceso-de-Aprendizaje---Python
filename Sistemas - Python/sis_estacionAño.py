print("*** Sistema de Estacion del Año ***")
print("Segun el mes: ")

print("\nEnero = 1\tFebrero = 2\tMarzo = 3\tAbril = 4")
print("Mayo = 5\tJunio = 6\tJulio = 7\tAgosto = 8")
print("Septiembre = 9\tOctubre = 10\tNoviembre = 11\tDiciembre = 12")

def obtener_informacion():
    numero_mes = int(input("\nIngrese el numero de mes: "))
    return numero_mes

def calcular_estacion(numero_mes):
    if numero_mes == 1 or numero_mes == 2 or numero_mes == 12:
        print("\nEl estacion del mes es Invierno ")
    elif numero_mes == 3 or numero_mes == 4 or numero_mes == 5:
        print("\nEl estacion del mes es Primavera ")
    elif numero_mes == 6 or numero_mes == 7 or numero_mes == 8:
        print("\nEl estacion del mes es Verano ")
    elif numero_mes == 9 or numero_mes == 10 or numero_mes == 11:
        print("\nEl estacion del mes es Otoño ")
    else:
        print("\nLa estacion del Mes es Desconocida ")
    return"---------------------------"

numero_mes = obtener_informacion()

print(calcular_estacion(numero_mes))
