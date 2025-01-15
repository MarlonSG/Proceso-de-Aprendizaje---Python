print("*** Sistema de Calificaciones ***")

def obtener_nota():
    nota = float(input("\nIngrese la nota: "))
    return nota

def calcular_nota(nota):
    if nota >= 9 and nota <= 10:
        print("\nCalificativo A")
    elif nota >= 8 and nota < 9:
        print("\nCalificativo B")
    elif nota >= 7 and nota < 8:
        print("\nCalificativo C")
    elif nota >= 6 and nota < 7:
        print("\nCalificativo D")
    elif nota >= 0 and nota < 6:
        print("\nCalificativo F")
    else:
        print("\nValor Desconcido")
    return "------------"

nota = obtener_nota()

print(calcular_nota(nota))