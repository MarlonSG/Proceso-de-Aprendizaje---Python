print("*** Sistema de Salud y Fitness ***")

def obtener_informacion():
    nombre_usuario = input("\nIngrese su Nombre: ").strip()
    pasos_caminados = int(input("Ingrese su cantidad de pasos caminados: ").strip())
    return nombre_usuario, pasos_caminados


def calcular_calorias(pasos_caminados, calorias_por_paso):
    calorias_quemadas = pasos_caminados * calorias_por_paso
    return calorias_quemadas

def calcular_datos(pasos_caminados, meta_pasos_diarios, calorias_quemadas, nombre_usuario):
    if pasos_caminados >= meta_pasos_diarios:
        print(f"\nHola {nombre_usuario}")
        print(f"Usted llego a la Meta Diaria de {meta_pasos_diarios} pasos. Usted Hizo {pasos_caminados} pasos caminados.")
        print(f"Y llego a Quemar {calorias_quemadas:.2f} calorias")
    else:
        print(f"\nHola {nombre_usuario}")
        print(f"Usted no llego a la Meta Diaria. La Meta era {meta_pasos_diarios} pasos y usted hizo {pasos_caminados} pasos.")
        print(f"Pero llego a Quemar {calorias_quemadas:.2f} calorias")
    return "-----------"

nombre_usuario, pasos_caminados = obtener_informacion()
meta_pasos_diarios, calorias_por_paso = 10000, 0.04
calorias_quemadas = calcular_calorias(pasos_caminados, calorias_por_paso)

print(calcular_datos(pasos_caminados, meta_pasos_diarios, calorias_quemadas, nombre_usuario))
