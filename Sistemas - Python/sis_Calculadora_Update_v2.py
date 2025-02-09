import math
import sys

print("*** Calculadora Update v2 ***")

print("""¡Bienvenido a este Programa!
      
      Seleccione una Opcion:
      1. Sumar
      2. Restar
      3. Multiplicar
      4. Dividir
      5. Potencia
      6. Raiz Cuadrada
      7. Salir
      """)



while True:
    try:    
        opcion = int(input("Cual opcion escoje usted: "))
        if 1 <= opcion <= 7:
            break
        else:
            print("Ingrese una opcion valida")
            
    except ValueError:
        print("Ingrese un Numero Valido")
       



def obtener_datos(opcion):
    try:
        if opcion in (1,2,3,4): 
            variable1 = float(input("Ingrese el Primer Numero: "))
            variable2 = float(input("Ingrese el Segundo Numero: "))
        elif opcion == 5:
            variable3 = float(input("Ingrese el numero a tratar: "))
            potenciador = float(input("A cuanto desea Potenciar?: "))
        elif opcion == 6:
            raiz_cuadrada = float(input("Ingrese el numero a sacar Raiz: "))
        else:
            sys,exit()
    except ValueError:
        print("Debe Ingresar datos Validos...")    
    return variable1, variable2, variable3, potenciador, raiz_cuadrada


variable1, variable2, variable3, potenciador, raiz_cuadrada = obtener_datos(opcion)


def procesar_opcion(opcion, variable1, variable2, variable3, 
                    potenciador, raiz_cuadrada):
    if opcion == 1:
        resultado = variable1 + variable2
    elif opcion == 2:
        resultado = variable1 - variable2
    elif opcion == 3:
        resultado = variable1 * variable2
    elif opcion == 4:
        resultado = variable1 / variable2
    elif opcion == 5:
        resultado = variable3 ** potenciador
    elif opcion == 6:
        resultado = math.sqrt(raiz_cuadrada)    
    return print(f"Resultado de la operacion{resultado}")

print(procesar_opcion(opcion, variable1, variable2, variable3, 
                    potenciador, raiz_cuadrada))
