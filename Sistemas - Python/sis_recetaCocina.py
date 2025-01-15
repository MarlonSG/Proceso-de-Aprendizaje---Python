print("*** Sistema de Receta Cocina ***")

def obtener_informacion ():
    nombre_receta = input("Ingrese el nombre de la receta: ")
    ingredientes = input("Ingrese los ingredientes: ")
    tiempo_preparacion = int(input("Ingrese la tiempo de la preparacion (min): "))
    dificultad = input("Ingrese la dificultad de la receta: ")
    dificultad = dificultad.upper()
    return nombre_receta, ingredientes, tiempo_preparacion, dificultad

nombre_receta, ingredientes, tiempo_preparacion, dificultad = obtener_informacion()
print("\nDatos de la Receta de Cocina")

print(f"Nombre de la receta: {nombre_receta}")
print(f"Ingredientes: {ingredientes}")
print(f"Tiempo de la preparacion (min): {tiempo_preparacion} minutos")
print(f"Dificultad de la receta: {dificultad}")