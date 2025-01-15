def precio_final (dias, precio):
    costo_total = dias * precio
    return costo_total

nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tus apellidos: ")
dias = int(input("Cuantos dias te Hospedaras: "))
precio = 55

print(f"Tu nombre es {nombre}")
print(f"Tus apellidos son {apellido}")
print(f"y te Hospedaras {dias} dias")

print(f"Teniendo una tarifa de ${precio} por dia, estarias pagando ${precio_final(dias, precio)} por los {dias} dias alojados en el Hotel")