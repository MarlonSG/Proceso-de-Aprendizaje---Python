print("*** Sistema de Autenticacion de Usuarios ***")

def datos_fijos():
    usuario_credencial = "admin"
    contraseña_credencial = 1234
    return usuario_credencial, contraseña_credencial

def obtener_datos():
    obtener_usuario = input(f"\nIngresa el usuario: ").strip().lower()
    obtener_contraseña = int(input("Ingrese la contraseña: ").strip().lower())
    return obtener_usuario, obtener_contraseña

def acceder_credenciales(usuario_credencial, contraseña_credencial, obtener_usuario, obtener_contraseña):

    if usuario_credencial == obtener_usuario:
        print("\nContraseña Incorrecta")
    elif contraseña_credencial == obtener_contraseña:
        print("\nUsuario Incorrecto")
    elif usuario_credencial != obtener_usuario and contraseña_credencial != obtener_contraseña:
        print("\nUsuario Incorrecto y Contraseña Incorrecta")
    else:
        print("\nBienvenidos al Sistema")
    return""

usuario_credencial, contraseña_credencial = datos_fijos()
obtener_usuario, obtener_contraseña = obtener_datos()

print(acceder_credenciales(usuario_credencial, contraseña_credencial, obtener_usuario, obtener_contraseña))