# usamos el operador or en este ejercisio


print("*** Sistema de Prestamo de libros ***")

def obtener_informacion ():
    usuario_credencial = input(f"\n¿Tiene credencial de Estudiante o Universitario? (Si/No): ")
    distancia_casa = int(input("¿A cuantos Km vive de la Biblioteca?: "))
    return usuario_credencial, distancia_casa
usuario_credencial, distancia_casa = obtener_informacion()

def calcular_prestamo (usuario_credencial, distancia_casa):
    distancia_km = 3
    solicitud_prestamo = distancia_km >= distancia_casa or usuario_credencial.strip().lower() == "si"
    return solicitud_prestamo

resultado_prestamo = calcular_prestamo (usuario_credencial, distancia_casa)

print(f"\n¿Accede al Prestamo?: {resultado_prestamo}")
