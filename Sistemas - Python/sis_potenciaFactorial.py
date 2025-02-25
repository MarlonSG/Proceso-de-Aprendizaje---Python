"""
PROGRAMA BASICO
"""

# def potencia_Factorial(numero):
#     if numero == 0:
#         return 1
#     else:
#         potencia_parcial = numero ** potencia_Factorial(numero - 1)
#         return potencia_parcial
# numero = int(input('Ingresa un numero: '))
# resultado = potencia_Factorial(numero)
# print('El resultado es:', resultado)


def potencia(base, exponente):
    # Caso base
    if exponente == 0:
        return 1
    else:  # Caso recursivo
        return base * potencia(base, exponente - 1)

print(f'2 elevado a la 3: {potencia(2, 3)}')
print(f'5 elevado a la 0: {potencia(5, 0)}')
print(f'4 elevado a la 5: {potencia(4, 5)}')
