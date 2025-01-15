def obtener_informacion():
    datos = int(input(f"Ingrese un numero ({VALOR_MINIMO} - {VALOR_MAXIMO}): "))
    return datos

datos = obtener_informacion()

VALOR_MINIMO = 0
VALOR_MAXIMO = 5

dentro_rango = VALOR_MINIMO <= datos <= VALOR_MAXIMO
#fuera_rango =  not(VALOR_MINIMO <= datos <= VALOR_MAXIMO)

print(f"\nEsta dentro de Rango? {dentro_rango}")
#print(f"Esta fuera de Rango? {fuera_rango}")















