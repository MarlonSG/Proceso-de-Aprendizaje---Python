print("*** Sistema Generador de Emails V2 ***")

def obtener_informacion():
    nombre = input(f"\nIngrese su Nombre: ").strip()
    apellido = input("Ingrese sus Apellidos: ").strip()
    empresa = input("Ingrese su Empresa: ").strip()
    dominio = input("Ingrese su Dominio (.com , .site , etc.): ").strip().lower()
    pais = input("Ingrese las siglas de su Pais (PE, MX, ARG. EU, etc.): ").strip().lower()
    return nombre, apellido, empresa, dominio, pais

nombre, apellido, empresa, dominio, pais = obtener_informacion()

def generador_emails(nombre,apellido, empresa, dominio, pais):
    nombre_usuario = nombre.replace(" ", ".").lower().strip()
    apellido_usuario = apellido.replace(" ", ".").lower().strip()
    empresa_normalizado = empresa.replace(" ", "").lower().strip()
    dominio_normalizado = f"{dominio}.{pais}".strip().lower()
    correo_normalizado = f"@{empresa_normalizado}{dominio_normalizado}"
    return f"{nombre_usuario}.{apellido_usuario}{correo_normalizado}"

def datos_normalizados (nombre,apellido, empresa, dominio, pais):

    nombre_usuario_final = nombre.replace(" ", ".").lower().strip()
    apellido_usuario_final = apellido.replace(" ", ".").lower().strip()
    nombre_apellido_normalizado = nombre_usuario_final + "." + apellido_usuario_final
    email_usuario_normalizado = f"@{empresa.replace(" " ,"").lower()}{dominio}.{pais}".lower().strip()
    dominio_usuario_normalizado = f"{dominio}.{pais}".lower()
    return nombre_apellido_normalizado, email_usuario_normalizado, dominio_usuario_normalizado,

nombre_apellido_normalizado, email_usuario_normalizado, dominio_usuario_normalizado = datos_normalizados (nombre,apellido, empresa, dominio, pais)

print("----------------------------------")
print("\n*** Resultados del Generador de Emails ***")
print("----------------------------------")

print(f"Nombre Completo: {nombre} {apellido}")
print(f"Usuario normalizado: {nombre_apellido_normalizado}")

print(f"\nNombre de Empresa: {empresa}")
print(f"Extension de Dominio: {dominio_usuario_normalizado}")

print(f"Dominio de Email Personalizado: {email_usuario_normalizado} ")
print("----------------------------")
email = generador_emails(nombre,apellido, empresa, dominio, pais)
print(f"\nEmail Final Generado: {email}")