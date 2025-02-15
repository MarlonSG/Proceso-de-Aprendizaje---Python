import sys

intentos = 5


print("*** Juego: Piedra, Papel o Tijeras ***")

print("""
    ______________________________________________________
    Hola Humano ... Soy ChickenBot, tu opnente en este 
    juego de Piedra, Papel y Tijeras, apuesto a que no
    acertaras ... pero quien sabe ... Ya lo veremos ...
    ______________________________________________________
      """)

while True:
    try:
        jugar = input("\nDeseas Jugar Humano ... (s/n): ")
        if jugar == str("s"):
            print("Bien Humano, Juguemos...\n")
            break
        elif jugar == str("n"):
            print("Lo sabia, eres una gallina, nos vemos pronto ... Perdedor\n")
            sys.exit()
        else:
            print("Acaso no sabes escribir (s) o (n) ... Humano tonto... ")
            intentos -= 1
            if intentos == 0:
                print("""Es increible que no puedas escribir bien una letra... Nos Vemos Perdedor...\n""")
                sys.exit()
    except ValueError:
        print(" ¿Tienes miedo Humano?")


