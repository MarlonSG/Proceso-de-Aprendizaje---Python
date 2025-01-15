print("*** SISTEMA DE CALCULOS DE DESCUENTOS DE TIENDA ONLINE ***")
print("----------------------------------------------------------")

def obtener_informacion():
    monto_compra = float(input(f"\nIngrese el monto compra: ").strip())
    es_miembro = input("¿Es mienbro de la tienda?: ").strip().lower()
    return monto_compra, es_miembro

def cacular_montos(monto_compra, es_miembro):
    monto_final = monto_compra

    if monto_compra > 1000 and es_miembro:  # Condición 1: Compra > $1000 Y es miembro
        descuento = monto_compra * 0.10
        monto_final -= descuento
        print(f"\nUsted Obtuvo un descuento del 10%")
        print(f"El monto real fue de ${monto_compra:.2f}")
        print(f"El monto final con descuento es de ${monto_final:.2f}")

    elif es_miembro == "si":  # Condición 2: Solo es miembro (implica que la compra <= $1000)
        descuento = monto_compra * 0.05
        monto_final -= descuento
        print(f"\nUsted Obtuvo un descuento del 5%")
        print(f"El monto real fue de ${monto_compra:.2f}")
        print(f"El monto final con descuento es de ${monto_final:.2f}")

    # Condición 3: No es miembro ni compra > $1000 (no se aplica descuento, monto_final ya está inicializado correctamente).
    else:
        monto_final = monto_compra
        print(f"\nUsted No obtuvo ningun Descuento")
        print(f"El monto real fue de ${monto_compra:.2f}")
        print(f"El monto final con descuento es de ${monto_final:.2f}")

    return "-------------"

monto_compra, es_miembro = obtener_informacion()

print(cacular_montos(monto_compra, es_miembro))