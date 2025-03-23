"""
FUNCION: CALCULAR LA SUMA DE LAS CALIFICACIONES INGRESADAS POR EL USUARIO
"""

print("*** Sistema para Calcular Promedios ***")

lista_calificaciones = []

while True:
    numero_de_calificaciones = int(input("Ingrese la cantidad de calificaciones: "))
    if numero_de_calificaciones != None:
        break
    else:
        print("Ingrese un Valor Valido ...")
        continue


for indice in range(numero_de_calificaciones):
    calificacion = float(input(f"Ingrese la Calificacion N°{indice+1}: "))
    if calificacion == None:
        calificacion = 0
    else:
        lista_calificaciones.append(calificacion)

print(f"\nLas {numero_de_calificaciones} calificaciones fueron {lista_calificaciones}")
calificacion_final = sum(lista_calificaciones) / numero_de_calificaciones #usamos "sum()"

print(f"\nLa calificacion final es {calificacion_final:.2f}")
