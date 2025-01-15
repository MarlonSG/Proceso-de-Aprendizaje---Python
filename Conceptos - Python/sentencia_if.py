edad = int(input("Ingree su edad: ").strip())

if edad >= 18:
    print("Eres mayor de edad")
elif 13 <= edad < 18:
    print("Eres adolecente aun")
else:
    print("Eres menor de edad")