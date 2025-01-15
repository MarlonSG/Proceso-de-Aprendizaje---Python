from random import randint

print("*** Sistema Generador de ID Unicos ***")

def obtener_informacion():
    nombre = input("\nIngrese su Nombre: ")
    apellido = input("Ingrese su Apellido: ")
    cumpleaños = input("Ingrese el año de Nacimiento (YYYY):")
    return nombre,apellido,cumpleaños

nombre, apellido, cumpleaños = obtener_informacion()

def generarIDunico():
    nombre_usuario = nombre[:2].upper()
    apellido_usuario = apellido[-2:].upper()
    cumpleaños_usuario = cumpleaños[-2:].upper()
    binario = randint(1000,9999)
    codigo_usuario = f"{nombre_usuario}{apellido_usuario}{cumpleaños_usuario}{binario}"
    return codigo_usuario
codigo_final = generarIDunico()

print(f"\nHola {nombre}: ")
print("\t\tHemos Generado tu ID Unico de Usuario, el cual es: ")
print("-----------------------")
print(codigo_final)
print("-----------------------")
print("Felicidades!")
