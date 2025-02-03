print("*** Calculadora (Nivel Basico) ***")

menu = """!Bienvenido a Nuestro Sistema!
Elija la Operacion que desea Usar:
1) Suma
2) Resta
3) Multiplicacion
4) Division
Digite el Numero de Operacion (1 - 4): """



def obtener_informacion():
    valor_01 = float(input("Ingrese el primer Numero: "))
    valor_02 = float(input("Ingrese el segundo Numero: "))

    opcion = int(input(menu))
