"""
FUNCION: VERIFICAR LA CONTRASEÑA Y USUARIO PREDETERMINADA DEL CODIGO
"""

print("*** Sistema de Autenticación de Usuarios ***")

def datos_fijos():
    usuario_credencial = "admin"
    contraseña_credencial = "1234"
    return usuario_credencial, contraseña_credencial

def obtener_datos():
    while True:
        obtener_usuario = input("Ingrese Usuario del Sistema: ").strip() #Se agregó strip para evitar errores con espacios.
        if obtener_usuario == "":
            print("No ingreso el usuario Valido")
        else:
            break

    while True:
        obtener_contraseña = input("Ingrese Contraseña del Usuario: ").strip() #Se agregó strip para evitar errores con espacios.
        if obtener_contraseña == "":
            print("No ingreso una contraseña Valida")
        else:
            break

    return obtener_usuario, obtener_contraseña

def acceder_credenciales(usuario_credencial, contraseña_credencial, obtener_usuario, obtener_contraseña):
    if usuario_credencial == obtener_usuario and contraseña_credencial == obtener_contraseña:
        print("\nBienvenidos al Sistema")
    elif usuario_credencial != obtener_usuario and contraseña_credencial == obtener_contraseña:
      print("\nUsuario Incorrecto")
    elif usuario_credencial == obtener_usuario and contraseña_credencial != obtener_contraseña:
      print("\nContraseña Incorrecta")
    else:
      print("\nUsuario Incorrecto y Contraseña Incorrecta")

usuario_credencial, contraseña_credencial = datos_fijos()
obtener_usuario, obtener_contraseña = obtener_datos()

acceder_credenciales(usuario_credencial, contraseña_credencial, obtener_usuario, obtener_contraseña)