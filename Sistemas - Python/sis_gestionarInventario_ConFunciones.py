"""
Lo mismo que gestionarInventario nomas que con funciones (def)
"""
from random import randint
import sys

#Variables que se usaran
lista_inventario = []
contador_intentos = 4

# Cajon de Funciones
def agregar_elementos(menu):
    while True:  # Bucle para agregar múltiples elementos
        try:
            name_item = input("Ingrese nombre del producto (o 'salir' para terminar): ")
            if name_item.lower() == "salir":  # Permitir salir con 'salir' en minúsculas o mayúsculas
                break

            if not name_item:  # Verificar si el nombre está vacío
                print("Ingrese un nombre válido.")
                continue  # Volver al inicio del bucle

            price_item = float(input("Ingrese el precio del producto: "))

            category_item = input("Ingresa la categoria: ")
            if not category_item:  # Verificar si la categoría está vacía
                print("Ingrese una categoría válida.")
                continue

            # Crear Sku automaticamente con randint
            sku_item = randint(1000000000, 99999999999)

            # Crear un diccionario para el producto y agregarlo a la lista
            item = {
                "Nombre": name_item,
                "Precio": price_item,
                "Categoria": category_item,
                "SKU": sku_item
            }
            lista_inventario.append(item)  # Usar append para agregar el diccionario a la lista
            print("Producto agregado al inventario.")

        except ValueError:
            print("Precio inválido. Ingrese un número.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
    return "---------------------------"

def ver_inventario(menu):
    if not lista_inventario:
        print("No hay Elementos en el Inventario")
    else:
        print("\nInventario:")  # Encabezado para la lista
        for contador, item in enumerate(lista_inventario):
            print(f"""{contador + 1} - Nombre: {item["Nombre"]}, 
            Precio: {item["Precio"]}, 
            Categoría: {item["Categoria"]}, 
            SKU: {item["SKU"]}\n""")
    return menu

def buscar_elementos(menu):
    while True:
        try:
            contador_buscado = int(input("Ingrese el número de persona a buscar (contador): "))
            indice_buscado = contador_buscado - 1  # Ajustar el contador al índice
            if 0 <= indice_buscado < len(lista_inventario):
                persona_encontrada = lista_inventario[indice_buscado]

                print(f"Persona con número {contador_buscado} encontrada:")
                print(persona_encontrada)  # Imprimir los datos de la persona
                break  # Salir del bucle

            else:
                print(f"No se encontró ninguna persona con el número {contador_buscado}.")
                break  # Salir del bucle

        except ValueError:
            print("Por favor, ingrese un número válido (entero).")
    return menu


#Incio del Programa
print("*** Sistema de Gestion de Inventario ***")

while True:
    menu = ("""
    Bienvenido Humano:
    Elije una de las opciones:

    1. Agregar Elementos
    2. Ver el Inventario
    3. Buscar Por ID (Contador)
    4. Salir
    """)

    print(menu)

    try:
        opcion = int(input("Que opcion elije usted: "))

        if opcion == 1:
            print(agregar_elementos(menu))

        elif opcion == 2:
          print(ver_inventario(menu))

        elif opcion == 3:
            print(buscar_elementos(menu))

        elif opcion == 4:
            print("Hasta Luego")
            sys.exit()

        else:
            print("Ingrese un valor del 1 al 3 ...")
            contador_intentos -= 1
            if contador_intentos == 0:
                print("Lo sentimos pero has errado muchas veces...")
                sys.exit()

    except ValueError:
        print("No esta permitido valores Nulos, solo Numericos...")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")  # Capturar excepciones generales