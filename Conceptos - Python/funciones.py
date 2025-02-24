"""
ACA DECLARA DIRECTO (SOLO EN CIERTAS OCASIONES COMO DATOS FIJOS
"""

print('*** Funciones en Python ***')

# Definir una funcion para mandar a saludar
def saludar(mensaje):
   print(f'Mensaje recibido: {mensaje}')
# Programa principal, llamamos a la funcion
saludar('Hola a todos')


#if __name__ == "__main__"  (ESTO SE UTILIZA PARA RESTRINGIR
#                            ALGO QUE NO SE USA EN IMPORT FROM COMO UN MODULO


# Definimos la funcion
def sumar(a, b):
    resultado_suma = a + b
    return resultado_suma

# Llamar a la funcion
resultado_funcion = sumar(8, 5)
print(f'Resultado función sumar: {resultado_funcion}')

resultado_funcion = sumar(9, 15)
print(f'Resultado función sumar: {resultado_funcion}')