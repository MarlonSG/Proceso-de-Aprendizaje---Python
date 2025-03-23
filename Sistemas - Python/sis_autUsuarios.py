"""
Version Desactualizada
FUNCION: VERIFICAR LA CONTRASEÑA Y USUARIO PREDETERMINADA DEL CODIGO
"""

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
    confirmar_usuario = usuario_credencial == obtener_usuario
    confirmar_contraseña = contraseña_credencial == obtener_contraseña
    confirmar_acceso = confirmar_usuario and confirmar_contraseña
    return confirmar_acceso


usuario_credencial, contraseña_credencial = datos_fijos()
obtener_usuario, obtener_contraseña = obtener_datos()
confirmar_acceso = acceder_credenciales(usuario_credencial, contraseña_credencial, obtener_usuario, obtener_contraseña)

print(f"\n¿Accede al Sistema? {confirmar_acceso}")