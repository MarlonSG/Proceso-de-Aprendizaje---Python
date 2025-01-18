print("*** Sistema para Calcular Promedios ***")

lista_calificaciones = []
numero_de_calificaciones = int(input("Ingrese la cantidad de calificaciones: "))

for indice in range(numero_de_calificaciones):
    calificacion = float(input(f"Ingrese la Calificacion N°{indice+1}: "))
    lista_calificaciones.append(calificacion)

print(f"\nLas {numero_de_calificaciones} calificaciones fueron {lista_calificaciones}")
calificacion_final = sum(lista_calificaciones) / numero_de_calificaciones #usamos "sum()"

print(f"\nLa calificacion final es {calificacion_final:.2f}")
