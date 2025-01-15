cadena = "Hola, Bienvenido al mundo de Python"

buscar_01 = cadena.find("Bienvenido")
buscar_02 = cadena.find("Hola")
buscar_03 = cadena.find("mundo")
buscar_04 = cadena.find("Python")
buscar_05 = cadena.find("Null")

#print(f"El primer digito de las siguientes palabras se encuentran asi: \"Hola\" se encuentra en el digito {buscar_02}, "
#      f"\"Bienvenido\" en el digito {buscar_01},"
#      f"\"mundo\" en el digito {buscar_03}, "
#      f"\"Python\" en el digito {buscar_04}, "
#      f" Mientras que \"Null\" no esta asi que botara {buscar_05} como respuesta por no encontrarlo." )

print(f"El primer digito de las siguientes palabras se encuentran asi: \"Hola\" se encuentra en el digito {buscar_02}, " )
print(f"\"Bienvenido\" en el digito {buscar_01}," )
print(f"\"mundo\" en el digito {buscar_03}, " )
print(f"\"Python\" en el digito {buscar_04}, " )
print(f" Mientras que \"Null\" no esta asi que botara {buscar_05} como respuesta por no encontrarlo." )
