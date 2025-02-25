from random import randint
import sys

psw_advanced = "admin123"



snacks = [
    {"Producto": "Papitas", "Nombre": "Lays", "Precio": 2.50,
    },
    "Gaseosa": {
        "Nombre": "Pepsi",
        "Precio": 3.50,
    },
    "Chocolate": {
        "Nombre": "Sublime",
        "Precio": 4.00,
    }
]


def escoger_productos(menu):
    while True:
        try:
            producto_elegido = input("\nIngrese el ID del producto para agregar (\"salir\" para terminar): ")
            buscador_productos = producto_elegido - 1
            if


            for contador, item in enumerate(snacks):


def mostrar_productos():
    print("Función para mostrar productos (aún no implementada)")
    for contador, item in enumerate(snacks):
        print(f"""{contador + 1}.Producto: {snacks[item]}
        Nombre: {snacks[item]["Nombre"]}, 
        Precio: {snacks[item]["Precio"]}, 
        """)

def escoger_productos():
    print("Función para escoger productos (aún no implementada)")

def ver_carrito():
    print("Función para ver el carrito (aún no implementada)")

def finalizar_compra():
    print("Función para finalizar compra (aún no implementada)")

def advanced_mode():
    password = input("Ingrese la contraseña: ")
    if password == "contraseña_secreta":  # Reemplaza con tu contraseña
        print("Acceso concedido al modo avanzado.")
        # Aquí irían las funciones y opciones del modo avanzado
    else:
        print("Contraseña incorrecta. Acceso denegado.")

def mostrar_menu():
    print("""
    Escoja una de Nuestras Opciones:

    1. Mostrar Productos
    2. Escoger Productos
    3. Ver Carrito
    4. Finalizar Compra
    5. Salir
    6. Advanced (Required Password)
    """)

while True:
    mostrar_menu()
    opcion = input("Ingrese su opción: ")

    if opcion == "1":
        mostrar_productos()
    elif opcion == "2":
        escoger_productos()
    elif opcion == "3":
        ver_carrito()
    elif opcion == "4":
        finalizar_compra()
    elif opcion == "5":
        print("¡Gracias por su visita!")
        sys.exit()
    elif opcion == "6":
        advanced_mode()
    else:
        print("Opción inválida. Por favor, ingrese un número del 1 al 6.")



