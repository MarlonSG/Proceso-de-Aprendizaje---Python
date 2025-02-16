import sys
import random
intentos = 5

opciones = ["Piedra", "Papel", "Tijeras"]


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
        jugar = input("Deseas Jugar Humano ... (s/n): ").lower()
        if jugar == str("s"):
            print("Bien Humano, Juguemos...")
            break
        elif jugar == str("n"):
            print("Lo sabia, eres una gallina, nos vemos pronto ... Perdedor\n")
            sys.exit()
        else:
            print("Acaso no sabes escribir (s) o (n) ... Humano tonto... \n")
            intentos -= 1
            if intentos == 0:
                print("""\nEs increible que no puedas escribir bien una letra... Nos Vemos Perdedor...\n""")
                sys.exit()
    except ValueError:
        print(" ¿Tienes miedo Humano?")

print("""
    _________________________________________________________________________________
    Haremos este juego algo Aleatorio Humano ... Te dare la venaja de que mi sistema 
    elija mis Opciones aleatoriamente ...
        
    Y tu elijaras Entre estas 3 Opciones...
    1. Piedra       2. Papel        3. Tijeras
        
    Mas Facil Imposible ... Empezemos...
    _________________________________________________________________________________
    """)
print("""Elije una de las 3 opciones:
      
    1. Piedra
    2. Papel
    3. Tijeras
    """)

def juegoPPT(opciones):
        sistema = random.choice(opciones)
        try:
            desicion = int(input("¿Que opcion Elijes? (1-3): "))
            if 1 <= desicion <= 3:
                if desicion == 1: # PIEDRA
                    if sistema == str("Piedra"):
                        print(f"Escojo {sistema}!\n")
                        print(f"Hemos coincidido en sacar {opciones[0]}")

                    elif sistema == str("Papel"):
                        print(f"Escojo {sistema}!\n")
                        print(f"Te he vencido Humano, he ecogido {opciones[1]} y tu {opciones[0]}")

                    elif sistema == str("Tijeras"):
                        print(f"Escojo {sistema}!\n")
                        print(f"Me has ganado Humano, he ecogido {opciones[2]} y tu {opciones[0]}")

                if desicion == 2: #PAPEL
                    if sistema == str("Piedra"):
                        print(f"Escojo {sistema}!\n")
                        print(f"Me has ganado Humano, he ecogido {opciones[0]} y tu {opciones[1]}")

                    elif sistema == str("Papel"):
                        print(f"Escojo {sistema}!\n")
                        print(f"Hemos coincidido en sacar {opciones[1]}")

                    elif sistema == str("Tijeras"):
                        print(f"Escojo {sistema}!\n")
                        print(f"Te he vencido Humano, he ecogido {opciones[2]} y tu {opciones[1]}")

                if desicion == 3: #TIJERA
                    if sistema == str("Piedra"):
                        print(f"Escojo {sistema}!\n")
                        print(f"Te he vencido Humano, he ecogido {opciones[0]} y tu {opciones[2]}")

                    elif sistema == str("Papel"):
                        print(f"Escojo {sistema}!\n")
                        print(f"Me has ganado Humano, he ecogido {opciones[1]} y tu {opciones[2]}")

                    elif sistema == str("Tijeras"):
                        print(f"Escojo {sistema}!\n")
                        print(f"Hemos coincidido en sacar {opciones[2]}")

            else:
                print("Enserio no sabes ingresar 1, 2, o 3 ... Que verguenza...")

        except ValueError:
            print("¿Enserio pusiste otro valor ?, Confirma si continuas ...")
        return ""

print(juegoPPT(opciones))

while True:
    continuar = input("\nDeseas Continuar Jugando? (s/n): ").lower()
    if continuar == str("s"):
        print("""Elije una de las 3 opciones:

              1. Piedra
              2. Papel
              3. Tijeras
              """)
        juegoPPT(opciones)
    elif continuar == str("n"):
        print("Nos Vemos Perdedor...")
        sys.exit()
    else:
        print("Ingrese una opcion (s) o (n) IDIOTA")
        