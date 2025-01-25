class Arimetica:

    def __init__(self, operador1, operador2): #CONSTRUCTOR
       self.operador1 = float(operador1)
       self.operador2 = float(operador2)


    def mostrar_resultados(self):
        suma = self.operador1 + self.operador2
        resta = self.operador1 - self.operador2
        multiplicacion = self.operador1 * self.operador2
        division = self.operador1 / self.operador2

        print(f"""Persona:
                Operador N°1: {self.operador1}
                Operador N°2: {self.operador2}
                """)
        print(f"Resultado de la suma: {suma}")
        print(f"Resultado de la resta: {resta}")
        print(f"Resultado de la multiplicacion: {multiplicacion}")
        print(f"Resultado de la division: {division}")

        print(f"Direccion Memoria Personal: {id(self)}")
        print(f"Direccion Memoria Hexadecimal Personal: {hex(id(self))}\n")


if __name__ == '__main__':
    #CREAR UN OBJETO
    objeto1 = Arimetica("10", "12" )
    objeto1.mostrar_resultados()

    #CREAR OBJETO 2
    objeto2 = Arimetica("20", "5" )
    objeto2.mostrar_resultados()
