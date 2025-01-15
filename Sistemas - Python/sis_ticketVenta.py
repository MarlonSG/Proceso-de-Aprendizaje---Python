from random import randint
from tabulate import tabulate

print("*** Sistema de Generacion de Ticket de Venta ***")
print("-------------------------------------------------")

def obtener_informacion_productos ():
    nombre_producto1 = input(f"\nNombre de Producto 1: ").strip()
    precio_producto1 = float(input("Precio de Producto 1: ").strip())
    nombre_producto2 = input(f"\nNombre de Producto 2: ").strip()
    precio_producto2 = float(input("Precio de Producto 2: ").strip())
    nombre_producto3 = input(f"\nNombre de Producto 3: ").strip()
    precio_producto3 = float(input("Precio de Producto 3: ").strip())
    nombre_producto4 = input(f"\nNombre de Producto 4: ").strip()
    precio_producto4 = float(input("Precio de Producto 4: ").strip())
    nombre_producto5 = input(f"\nNombre de Producto 5: ").strip()
    precio_producto5 = float(input("Precio de Producto 5: ").strip())
    return (nombre_producto1,precio_producto1,nombre_producto2, precio_producto2, nombre_producto3,
            precio_producto3, nombre_producto4, precio_producto4, nombre_producto5, precio_producto5)

def calular_venta (precio_producto1, precio_producto2, precio_producto3, precio_producto4, precio_producto5):
    subtotal_venta = precio_producto1 + precio_producto2 + precio_producto3 + precio_producto4 + precio_producto5
    impuesto_venta = subtotal_venta * 0.18
    venta_total = subtotal_venta + impuesto_venta
    return subtotal_venta, impuesto_venta, venta_total

def calcular_descuento (subtotal_venta):
    descuento = 0.15
    calculo_descuento = subtotal_venta * descuento
    subtotal_descuento = subtotal_venta - calculo_descuento
    impuesto_subtotal_descuento = subtotal_descuento * 0.18
    venta_total_descuento = subtotal_descuento + impuesto_subtotal_descuento
    return venta_total_descuento

def codigo_ticket ():
    codigo_ticket = randint(100000, 999999)
    return codigo_ticket

def generar_tabla(datos, encabezados):
  tabla = tabulate(datos, headers=encabezados, tablefmt="fancy_grid", colalign=("left", "right"))
  return tabla

nombre_producto1, precio_producto1, nombre_producto2, precio_producto2, nombre_producto3,precio_producto3, nombre_producto4, precio_producto4, nombre_producto5, precio_producto5 = obtener_informacion_productos()
subtotal_venta, impuesto_venta, venta_total = calular_venta (precio_producto1, precio_producto2, precio_producto3, precio_producto4, precio_producto5)
venta_total_descuento = calcular_descuento (subtotal_venta)
codigo_ticket = codigo_ticket()

datos = [
    [nombre_producto1, precio_producto1],
    [nombre_producto2, precio_producto2],
    [nombre_producto3, precio_producto3],
    [nombre_producto4, precio_producto4],
    [nombre_producto5, precio_producto5],
]

encabezados = ["Descripción", "Precio (S/)"]
mi_tabla = generar_tabla(datos, encabezados)


print("\n-------------------------------------------------")
print("************** TICKET DE VENTA GENERADA *************")
print("-------------------------------------------------")
print("****** GRACIAS POR COMPRAR EN NEBULA TEAM ******")
print(f"\nResumen de Compra #{codigo_ticket} ")
print("")
print(mi_tabla)
print("")
print("-------------------------------------------------")
print(f"SubTotal: ----------------------- {subtotal_venta:.2f}")
print(f"IGV(%): ------------------------- 18%")
print(f"Total: -------------------------- {venta_total:.2f}")
print(f"Total con Descuento (15%): ------ {venta_total_descuento:.2f}")