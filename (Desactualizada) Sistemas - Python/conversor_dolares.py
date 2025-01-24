plata = int(input("¿Cuanto dinero (Soles S/.) tienes?: "))
valor_dolar = 3.45
dolares = plata / valor_dolar
dolares = round(dolares,2) # Con round redondeo a 2 decimales.
dolares = str (dolares)
print ("Tienes $" + dolares + " dolares")


dolares = float (input("¿Cuantos dolares ($) tienes?: "))
valor_dolar = 3.28
plata = dolares * valor_dolar
plata = str (plata)
print ("Tienes " + plata + " soles")

