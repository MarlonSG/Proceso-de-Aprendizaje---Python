print("*** Generador de password ***")

def generar_password():

    maximo_caracteres = 6
    print("____________________________________________________")
    print("NOTA: ")
    print("Este Sistema se creo para generarle un password seguro")
    print("Ingrese una Contraseña de al menos 6 digitos:")
    print("____________________________________________________")

    password_ingresado = input("\nIngrese su Nueva contraseña: ")

    while len(password_ingresado) < maximo_caracteres:
        print("\nVaya algo salio Mal")
        print(f"Contraseña creada Incorrectamente.")
        print(f"La contraseña \"{password_ingresado}\" no cumple con 6 o mas digitos")
        return generar_password()
    else:
        print("\nFelicidades!")
        print(f"Contraseña creada correctamente.")
        print(f"La contraseña \"{password_ingresado}\" cumple con 6 digitos o mas")
    return "_____________________"

print(generar_password())