dato = int(input("Ingrese un numero (1 - 10): "))

dentro_rango = 1 <= dato <= 10

fuera_rango =  not(1 <= dato <= 10)

print(f"Esta dentro de Rango? {dentro_rango}")
print(f"Esta fuera de Rango? {fuera_rango}")