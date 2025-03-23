"""
FUNCION: VERIFICAR SI EL USUARIO CONTINUA O NO EN EL SISTEMA
"""

print("*** SISTEMA BANCARIO - CONTINUEDAD ***")

def obtener_respuesta():
    salir_sistema = input("Deseas salir del Sistema? (SI / No) (\"No\" por Determinado): ")
    salir_sistema = salir_sistema.lower().strip() == "si"

    if not salir_sistema:
        print("Continuando en el Sistema...")
    else:
        print("Salir del sistema...")
    return "-------"

obtener_respuesta()