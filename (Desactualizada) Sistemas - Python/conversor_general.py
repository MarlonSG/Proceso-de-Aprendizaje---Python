menu = """
Bienvenidos al conversor de monedas plus!!😎

¿Que tipo de moneda tienes ?, elige una opción:

1- Soles Peruanos
2- Pesos argentinos
3- Euros Europeos

"""

def calculos(tipo_pesos, valor_dolar):
    plata = float(input("¿Cuanto dinero " + tipo_pesos + " tienes?: "))
    dolares = plata / valor_dolar
    dolares = round(dolares,2) # Con round redondeo a 2 decimales.
    dolares = str (dolares)
    print ("Tienes $" + dolares + " dolares")

opcion = int (input (menu))

if opcion == 1:
    calculos ("Soles", 3.35)

elif opcion == 2:
    calculos ("argentinos", 65)

elif opcion == 3:
    calculos ("euros", 4.24)

else:
    print ("Ingresa una opción correcta")