"""
Se esta haciendo una agenda aplicando Dicionarios
"""

print("*** AGENDA DE CONTACTOS ***")

agenda = {
    "Carlos": {
        "Telefono": "954643431",
        "Correo": "carlos@gmail.com",
        "Direccion": "Los Angeles, California"
    },
    "Maria": {
        "Telefono": "954649881",
        "Correo": "maria@gmail.com",
        "Direccion": "Los Alaves, Rusia"
    },
    "Juan": {
        "Telefono": "4958536561",
        "Correo": "juan@gmail.com",
        "Direccion": "Vietnan, Suecia"
    }
}
print(agenda) # IMPRIMIR AGENDA

#OBTENER INFORMACION
print(f"""Informacion de Contacto de Juan:
    Telefono: {agenda["Juan"]["Telefono"]}
    Correo: {agenda["Juan"]["Correo"]} 
    Direccion: {agenda["Juan"]["Direccion"]}
""")

#Agregar Informacion (Contacto)
agenda["Sandra"] = {
    "Telefono": "9875643121",
    "Correo": "sandra@gmail.com",
    "Direccion": "Los Miraestrellas, Peru"
}
print(agenda)

#Eliminar Dato
agenda.pop("Juan")
#del agenda["Juan"]  (OTRA MANERA DE ELIMINAR)
print(agenda)

#Imprimir y listar datos de la agenda
for nombre,detalles in agenda.items():
    print(f"""
    Nombre: {nombre}
    Telefono: {detalles.get("Telefono")}
    Correo: {detalles.get("Correo")} 
    Direccion: {detalles.get("Direccion")}
    """)
