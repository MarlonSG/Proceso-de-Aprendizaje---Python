"""
ESTA ES UNA ACTUALIZACION DE CALCULADORA, 
APLICANDO MANEJO DE ERRORES (TRY-EXCEPT)
"""

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
        opcion = int(input("\nCual opcion escoje usted: "))
        if 1 <= opcion <= 7:
            break
        else:
            print("Ingrese una opcion valida")
            
    except ValueError:
        print("Ingrese un Numero Valido")
       

def obtener_datos(opcion):
    try:
        if opcion in (1, 2, 3, 4):
            while True:
                try:  
                    num1 = float(input("Ingrese el primer número: "))
                    num2 = float(input("Ingrese el segundo número: "))
                    return num1,num2
                except ValueError:
                    print("No puede ingresar datos nulos. Ingrese Nuevamente...")            
        elif opcion == 5:
            while True:
                try:
                    num = float(input("Ingrese el número a tratar: "))
                    pot = float(input("A cuanto desea Potenciar?: "))
                    return num, pot
                except ValueError:
                    print("No puede ingresar datos nulos. Ingrese Nuevamente...")  
        elif opcion == 6:
            while True:
                try:
                    num = float(input("Ingrese el número a sacar Raíz: "))
                    return num,
                except ValueError:
                    print("No puede ingresar datos nulos. Ingrese Nuevamente...")  
        else:
            sys.exit()
    except ValueError:
        print("Debe Ingresar datos Validos...")
        return None

datos = obtener_datos(opcion)

if datos is not None:
        def procesar_opcion(opcion, datos):
            try:
                if opcion in (1,2,3,4):
                    resultado = datos[0] + datos[1] if opcion == 1 else \
                                datos[0] - datos[1] if opcion == 2 else \
                                datos[0] * datos[1] if opcion == 3 else \
                                datos[0] / datos[1]
                elif opcion == 5:
                    resultado = datos[0] ** datos[1]
                elif opcion == 6:
                    resultado = math.sqrt(datos[0])
                return resultado
            except TypeError:
                return None

resultado = procesar_opcion(opcion, datos)

if resultado is not None:
    print(f"\nEl resultado es: {resultado:.2f}\n")
else:
    print("\nHa ocurrido un error Inesperado...\n")

