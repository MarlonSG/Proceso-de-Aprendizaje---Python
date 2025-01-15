def generador_emails(nombre_completo, empresa, dominio, pais):
    usuario = nombre_completo.replace(" ", ".").lower()
    empresa_normalizado = empresa.replace(" ", "").lower()
    dominio_normalizado = f"{dominio}.{pais}"
    correo_normalizado = f"@{empresa_normalizado}{dominio_normalizado}"
    return f"{usuario}{correo_normalizado}"

nombre_completo = "Marlon Raul Salazar Garcia"
empresa = "Nebula Team"
dominio = ".com"
pais = "pe"

print("*** SISTEMA GENERADOR DE EMAILS ***")
print()

print(f"Nombre Completo: {nombre_completo}")



print(f"Usuario normalizado: {nombre_completo.replace(" ", ".").lower()}")
print(" ")
print(f"Nombre de Empresa: {empresa}")
print(f"Extension de Dominio: {dominio}.{pais}")


print(f"Dominio de Email Personalizado: @{empresa.replace(" " ,"").lower()}{dominio}.{pais}")
print()
email = generador_emails(nombre_completo, empresa, dominio, pais)
print(f"Email Final Generado: {email}")

