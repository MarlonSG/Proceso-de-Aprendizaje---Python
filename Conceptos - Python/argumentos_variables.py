print('*** Argumentos Variables ***')

def superheroe_superpoderes(superheroe, nombre, *args):
    print(f'Superheroe: {superheroe} - {nombre} - {args}')
    # Iteramos los superpoderes
    for superpoder in args:
        print(f'\tSuperpoder: {superpoder}')

# Llamar la funcion
superheroe_superpoderes('Spiderman', 'Peter Parker', 'Instinto Arácnido', 'Teleraña')
superheroe_superpoderes('Ironam', 'Tony Stark', 'Armadura','Playboy','Millonario')

# Es opcional enviar argumentos variables
superheroe_superpoderes('Mi vecino', 'Juan Perez')

"""
---------------------------------------------------------------------------------------
"""

# *args - arguments - tupla
# **kwargs - keyword arguments (key,value) como un dict
print('*** Argumentos variables en forma de dict ***')

def superheroe_superpoderes(nombre, *args, **kwargs):
    print(f'Superheroe: {nombre} - {args} - Mas info: {kwargs}')

# Llamarmos la funcion
superheroe_superpoderes('Spiderman', 'Instinto Arácnido', edad=17, empresa='Marvel')
superheroe_superpoderes('Ironman', 'Armandura','Playboy', edad=45)

# Es opcional enviar argumentos variables
superheroe_superpoderes('Mi vecino', personalidad='Buena onda!')

"""
---------------------------------------------------------------------------------------
"""

print('*** Suma con Argumentos Variables ***')

# Funcion sumar que acepta argumentos variables
def sumar(*args):
    total = 0
    for numero in args:
        total += numero
    return total

# Llamamos a la funcion sumar
resultado = sumar(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(f'Resultado de la suma: {resultado}')

"""
---------------------------------------------------------------------------------------
"""

print('*** Imprimir detalles de una persona usando kwargs ***')

# Funcion que acepta argumentos variables en forma de llave-valor dict
def imprimir_detalle_persona(**kwargs):
    print('\nValores recibidos: ')
    for llave, valor in kwargs.items():
        print(f'{llave}:{valor}')

# Llamamos a la funcion
imprimir_detalle_persona(nombre='Karla', edad=30, ciudad='México')
imprimir_detalle_persona(nombre='Carlos', edad=28, ciudad='Guadalajara', puesto='Gerente')