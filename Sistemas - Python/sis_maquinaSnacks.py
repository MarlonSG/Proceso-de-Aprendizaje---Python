from random import randint
import sys

contraseña_admin = "contraseña_secreta"
carrito = []
Productos = [
    {"ID": 1, "Producto": "Papitas", "Nombre": "Lays", "Precio": 2.50},
    {"ID": 2, "Producto": "Gaseosa", "Nombre": "Pepsi", "Precio": 3.50},
    {"ID": 3, "Producto": "Chocolate", "Nombre": "Sublime", "Precio": 4.00}
]

def mostrar_productos():
    print("Productos Disponibles:")
    for producto in Productos:
        print(f"{producto['ID']}. {producto['Producto']} {producto['Nombre']} - ${producto['Precio']}")

def escoger_productos():
    mostrar_productos()
    while True:
        try:
            id_producto = int(input("Ingrese el ID del producto que desea agregar al carrito (0 para terminar): "))
            if id_producto == 0:
                break
            producto_seleccionado = next((p for p in Productos if p['ID'] == id_producto), None)
            if producto_seleccionado:
                carrito.append(producto_seleccionado)
                print(f"{producto_seleccionado['Nombre']} agregado al carrito.")
            else:
                print("ID de producto inválido.")
        except ValueError:
            print("Por favor, ingrese un número entero.")

def ver_carrito():
    if not carrito:
        print("El carrito está vacío.")
    else:
        print("Carrito de Compras:")
        total = 0
        for producto in carrito:
            print(f"{producto['Nombre']} - ${producto['Precio']}")
            total += producto['Precio']
        print(f"Total: ${total}")

def finalizar_compra():
    if not carrito:
        print("El carrito está vacío. No hay nada que comprar.")
        return

    print("Resumen de su compra:")
    total = 0
    for producto in carrito:
        print(f"{producto['Nombre']} - ${producto['Precio']}")
        total += producto['Precio']
    print(f"Total: ${total}")

    2
    confirmacion = input("¿Desea confirmar la compra? (sí/no): ").lower()
    if confirmacion == "si":
        procesar_pago(total)
    else:
        print("Compra cancelada.")

def procesar_pago(total):
    print("Procesando pago...")
    print(f"Pago de ${total} realizado con éxito.")
    carrito.clear()
    print("¡Gracias por su compra!")

def modo_avanzado():
    contraseña = input("Ingrese la contraseña de administrador: ")
    if contraseña == contraseña_admin:
        print("Acceso concedido al modo avanzado.")
        mostrar_menu_admin()
    else:
        print("Contraseña incorrecta. Acceso denegado.")

def mostrar_menu_admin():
    print("""
    Modo Avanzado:

    1. Agregar Producto
    2. Eliminar Producto
    3. Actualizar Producto
    4. Salir del Modo Avanzado
    """)
    while True:
        opcion = input("Ingrese su opción: ")
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            eliminar_producto()
        elif opcion == "3":
            actualizar_producto()
        elif opcion == "4":
            print("Saliendo del Modo Avanzado.")
            break
        else:
            print("Opción inválida.")

def agregar_producto():
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio del producto: "))
    id_producto = len(Productos) + 1 # Generar ID automático
    producto = {"ID": id_producto, "Nombre": nombre, "Precio": precio}
    Productos.append(producto)
    print("Producto agregado.")

def eliminar_producto():
    nombre = input("Nombre del producto a eliminar: ")
    for producto in Productos:
        if producto["Nombre"] == nombre:
            Productos.remove(producto)
            print("Producto eliminado.")
            return
    print("Producto no encontrado.")

def actualizar_producto():
    nombre = input("Nombre del producto a actualizar: ")
    for producto in Productos:
        if producto["Nombre"] == nombre:
            precio = float(input("Nuevo precio: "))
            producto["Precio"] = precio
            print("Producto actualizado.")
            return
    print("Producto no encontrado.")

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
        modo_avanzado()
    else:
        print("Opción inválida. Por favor, ingrese un número del 1 al 6.")