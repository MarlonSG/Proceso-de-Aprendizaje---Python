psw_real = "admin123"
contador = 4

while True:
    psw_user = input("Ingresa su Contraseña: ").lower().replace(" ", "")
    if psw_user == psw_real:
        print("Es correcto")
        break
    else:
        print("No es correcto")
        contador -= 1
        print(f"Te quedan {contador} intentos")
        if contador == 0:
            print("Se acabaron los intentos")
            break
        continue
