# usamos el operador and en este ejercisio

print("*** Sistema de Descuentos VIP ***")



def sis_descuentoVIP():
    nro_productos = 10
    cantidad_productos = int(input(f"\nIngresa el Nro. de Productos que compro: "))
    tiene_menbresia =  (input("¿Tiene Menbresia de la tienda? (Si/No): "))
    elegible_descuento = cantidad_productos >= nro_productos and tiene_menbresia.strip().lower() == "si"
    return elegible_descuento

elegible_descuento = sis_descuentoVIP()

print(f"\n¿Accede al descuento? : {elegible_descuento}")