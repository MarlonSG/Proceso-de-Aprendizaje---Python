import random
import string

print("*** GENERADOR DE CONTRASEÑAS v1 by MarlonSG ***")

print("""
    ______________________________________________________
    NOTA:
    Este Sistema se creo para generar un Password seguro
    Todo Fraude o Robo de la Contraseña creada por este 
    programa esta libre de nuestro alcanze.
    Proteja su Seguridad por su cuenta ...
    
    Para obtener una Contraseña Segura es Recmoendable
    que tenga una longitud entre 8 a 16 caracteres,
    Entre ellas letras, numeros y Simbolos
    ______________________________________________________
    
    
    Hola, Soy ChickenBot, y hoy te ayudare a Generar tu Contraseña Segura... 
      """)


#Sacamos su Usuario
while True:
    usuario = input("Primero... Dime cual es tu Nombre de Usuario: ").strip().lower().replace(" ","")
    if usuario:
        break
    else: 
        print("Por favor Ingresa un Usuario Valido...")


print(f""" 
    Excelente {usuario}, procedamos en tonces a generar tu contraseña Segura... 
      """)

#Indagamos su longitud de contraseña
while True:
    try:
        longitud = int(input("Indicame de cuantos caracteres quedras tu contraseña? (8 - 16): "))
        if 8 <= longitud <= 16:
            break
        else:
            print("Debe ingresar un numero entre 8 a 16, Intente Nuevamente...")
    except ValueError:
        print("Ingrese un numero Valido ...")


#Funcion para la contraseña            
def generar_contraseña(longitud):
    caracteres = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    contraseña = "".join(random.choice(caracteres) for i in range (longitud))
    return contraseña

contraseña = generar_contraseña(longitud)


#Imprimir el Resultado
print(f"""
      Bien {usuario}:
      
      Su contraseña se creo Correctamente y es:
      ________________________________
            
              {contraseña} 
      
      ________________________________
      Gracias por usar nuestro programa, Adios... :D      
      """)
