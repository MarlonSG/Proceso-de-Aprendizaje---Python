print('*** Operaciones con Set ***')

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

union = a | b  #SUMA
print(f'Union a | b: {union}')

interseccion = a & b   #INTERESECTAR NUMEROS REPETIDOS
print(f'Intersección a & b {interseccion}')

diferencia = a - b   #DIFERENCIAS (ELIMINAR LOS DUPLICADOS DEL SEGUNDO CONJUNTO) SOLO QUE DA DE A
print(f'Diferencia a - b {diferencia}')