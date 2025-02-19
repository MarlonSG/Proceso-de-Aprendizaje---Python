from random import randint
import sys
import string

# Mensaje de inicio
print("*** Sistema ALL STAR - 01 ***")

print("""______________________________________________________
Hola Usuario... Este software se hizo con la idea de
hacer que el usuario aplique sus conocimientos, omitir
cualquier comentario adicional sobre este proyecto....
______________________________________________________
""")

# Menu
menu = ("""Elije una Opcion de Lista:
--------------------------
1. Manipulación de cadenas
2. Operaciones con Lista y Tuplas
3. Diccionarios
4. Flujo de control
5. Bucles
6. Funciones
7. Clases y Objetos
8. Conjuntos
9. Salir
""")
#Imprimir Menu
print(menu)


# Funcion para la opcion 1
def manipulacion():
    print("""
    ______________________________________________________
    1. Manipulación de cadenas
    Pide al usuario que ingrese una frase. Luego, pide que 
    ingrese una palabra para buscar dentro de la frase. 
    El programa debe indicar si la palabra existe, cuántas 
    veces aparece y en qué posiciones
    ______________________________________________________
    """)

    try:
        while True:
            frase = input("Introduce una frase: ")
            if frase is str(""):
                print("Ingrese Valores...")
                continue
            else:
                break

        while True:
            palabra = input("Introduce una palabra para buscar: ")
            if palabra is str(""):
                print("Ingrese Valores...")
                continue
            else:
                break

        if palabra in frase:
            print("La palabra existe en la frase...")
            conteo = frase.count(palabra)
            print(f"La palabra aparece {conteo} en la frase")
            posicion = [i for i in range(len(frase)) if frase.startswith(palabra, i)]
            print(f"Posiciones: {posicion} ")
        else:
            print("La palabra no existe en la frase...")

    except Exception as e:  # Captura cualquier error
        print(f"Error: {e}")

    return "_________"


# Funcion para la opcion 2
def operaciones(menu):
    print("""
        _______________________________________________________
        2. Operaciones con listas y tuplas
        Crea dos listas con números aleatorios. Pide al usuario 
        que elija una operación (suma, resta, multiplicación, 
        intersección, unión). El programa debe realizar la 
        operación elegida con las listas y mostrar el resultado
        _______________________________________________________
        """)

    cant = 5
    lista_1 = [randint(1, 100) for i in range(cant)]
    lista_2 = [randint(1, 100) for i in range(cant)]

    print("Se Muestran 2 listas de Numeros Aleatorios (1-100): ")

    print(print(f"Lista 1: {lista_1}"))
    print(print(f"Lista 2: {lista_2}"))

    sub_menu_2 = ("""
    Elija una Opcion de Lista:
    1. Suma
    2. Restar
    3. Multiplicacion
    4. Division
    5. Interseccion
    6. Union

    7. Regresar al Menu Principal
    """)
    print(sub_menu_2)

    while True:
        try:
            opcion_operaciones = int(input("Que opcion elije Usted: "))
            if opcion_operaciones == 1:
                suma = sum(lista_1) + sum(lista_2)
                return f"""
                Datos de listas:
                lista 1: {lista_1}({sum(lista_1)}) + Lista 2: {lista_2}({sum(lista_2)})
                La suma de las 2 listas es {suma}"""

            elif opcion_operaciones == 2:
                resta = sum(lista_1) - sum(lista_2)
                return (f"""
                Datos de listas:
                lista 1: {lista_1}({sum(lista_1)}) - Lista 2: {lista_2}({sum(lista_2)})
                La resta de las 2 listas es {resta} """)

            elif opcion_operaciones == 3:
                multiplicacion = sum(lista_1) * sum(lista_2)
                return (f"""
                Datos de listas:
                lista 1: {lista_1}({sum(lista_1)}) * Lista 2: {lista_2}({sum(lista_2)})
                La Multiplicacion de las 2 listas es {multiplicacion} """)

            elif opcion_operaciones == 4:
                division = sum(lista_1) / sum(lista_2)
                return (f"""
                Datos de listas:
                lista 1: {lista_1}({sum(lista_1)}) / Lista 2: {lista_2}({sum(lista_2)})
                La Division de las 2 listas es {division} """)

            elif opcion_operaciones == 5:
                interseccion = list(set(lista_1) & set(lista_2))
                return f"""
                Datos de listas:
                lista 1: {lista_1} ---- Lista 2: {lista_2}
                Numeros intersectados: {interseccion}"""

            elif opcion_operaciones == 6:
                union = list(set(lista_1) | set(lista_2))
                return f"""
                Datos de listas:
                lista 1: {lista_1} ---- Lista 2: {lista_2}
                Union de Listas: {union}"""

            elif opcion_operaciones == 7:
                print("Bien, Regresemos al menu principal...")
                print(menu)  # REVISAR SI SALE AL MENU, se repite un bucle

            else:
                print("Ingrese un numero entre (1-7)...")

        except ValueError:
            print("Valor Invalido...")

        except Exception as e:  # Captura cualquier error
            print(f"Error: {e}")


# # Funcion para la opcion 3
# def diccionarios():
#     print("""
#     ________________________________________________________
#     2. Diccionarios
#     Crea un diccionario con información de personas (nombre,
#     edad, ciudad). Pide al usuario que ingrese el nombre de
#     una persona. El programa debe mostrar la información de
#     esa persona o indicar que no existe
#     ________________________________________________________
#     """)
#
#     diccionario = {
#
#
#     }


print(operaciones(menu))


