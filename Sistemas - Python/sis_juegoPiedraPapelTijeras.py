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

print("""
        Haremos este juego algo Aleatorio Humano ...
        Te dare la venaja de que mi sistema elija 
        mis Opciones aleatoriamente ...
        
        Y tu elijaras Entre estas 3 Opciones...
        1. Piedra       2. Papel        3. Tijeras
        
        Mas Facil Imposible ... Empezemos...
        """)
print("""
      Elije una de las 3 opciones:
      
      1. Piedra
      2. Papel
      3. Tijeras
      """)

if jugar is str("s"):
    def juegoPPT(opciones):
        sistema = random(opciones)
        try:
            desicion = int(input("¿Que opcion Elijes? (1-3): "))
            if 1 <= desicion <= 3:
                if desicion == 1:
                    
                    
        
        
        
        except:
            return
        