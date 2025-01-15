print("*** LA CASA DE LOS ESPEJOS ***")
def obtener_informacion():
    edad = int(input(f"\nIngresa tu edad: ").strip())
    miedo_oscuridad = input("¿Tienes miedo a la oscuridad?: ").strip().lower()
    tienes_miedo_oscuridad = miedo_oscuridad == "si"
    if not tienes_miedo_oscuridad and edad >= 10:
        print("Puedes Ingresar")
    else:
        print("\nNo Puedes Ingresar")
    return "---------------"

print(obtener_informacion())