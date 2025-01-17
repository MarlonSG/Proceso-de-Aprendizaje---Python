def suma_acumulativa():
    numero_maximo = 5
    numero_minimo = 1
    acumulador_suma = 0

    while numero_minimo <= numero_maximo:
        acumulador_suma += numero_minimo
        numero_minimo += 1
        print(f"Suma acumulada: {acumulador_suma}")
    return "__________"

print(suma_acumulativa())
