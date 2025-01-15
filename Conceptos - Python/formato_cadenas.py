nombre = "Marlon"
apellido = "Salazar"
edad = 20


mensaje = f"Hola, Me llamo {nombre} {apellido} y tengo {edad} años"
print(mensaje)

mensaje = "Hola, Me llamo {} {} y tengo {} años".format(nombre, apellido, edad)
print(mensaje)

mensaje = "".join([nombre," ",apellido])
print(mensaje)