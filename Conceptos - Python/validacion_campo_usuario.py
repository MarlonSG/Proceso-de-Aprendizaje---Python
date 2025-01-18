print('*** Validacion Campo de un Formulario ***')

nombre_usuario = None

# hasta que no escribas algo no pasara y se ciclara infinitamente

while not nombre_usuario:
    nombre_usuario = input('Ingresa tu nombre de usuario: ')

print(f'Nombre de usuario válido: {nombre_usuario}')