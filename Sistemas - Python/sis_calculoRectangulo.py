print("*** Calculador de Area y Perimetro de un Rectangulo ***")

def obtener_datos():
    base_rectangulo = float(input("Ingresa la base del rectangulo: ").strip())
    altura_rectangulo = float(input("Ingresa la altura del rectangulo: ").strip())
    return altura_rectangulo, base_rectangulo

def calcular_area(altura_rectangulo, base_rectangulo):
    area_rectangulo = altura_rectangulo * base_rectangulo
    return area_rectangulo


def calcular_perimetro(altura_rectangulo, base_rectangulo):
    perimetro_rectangulo = 2* (altura_rectangulo + base_rectangulo)
    return perimetro_rectangulo

altura_rectangulo, base_rectangulo = obtener_datos()
area_rectangulo = calcular_area(altura_rectangulo, base_rectangulo)
perimetro_rectangulo = calcular_perimetro(altura_rectangulo, base_rectangulo)

print(f"\nTeniendo como Base {base_rectangulo} y como Altura {altura_rectangulo}")
print(f"Se calcula que: ")
print(f"Su Area es: {area_rectangulo}")
print(f"Su Perimetro es: {perimetro_rectangulo}")