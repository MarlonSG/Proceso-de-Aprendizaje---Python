class Persona:

    def __init__(self, nombre, apellido, edad): #CONSTRUCTOR
       self.nombre = nombre
       self.apellido = apellido
       self.edad = edad

#    def initializar_Persona(self, nombre,apellido, edad):
#        self.nombre = nombre
#        self.apellido = apellido
#        self.edad = edad

    def mostrar_Persona(self):
        print(f"""Persona:
        Nombre: {self.nombre}
        Apellido: {self.apellido}
        Edad: {self.edad}
        """)
        print(f"Direccion Memoria Personal: {id(self)}")
        print(f"Direccion Memoria Hexadecimal Personal: {hex(id(self))}\n")



if __name__ == '__main__':
    #CREAR UN OBJETO
    persona1 = Persona("Marlon","Salazar", "20")
#    persona1.initializar_Persona("Marlon","Salazar", "20")
    persona1.mostrar_Persona()


    #CREAR OBJETO 2
    persona2= Persona("Raul","Salazar", "25")
#    persona2.initializar_Persona("Raul","Salazar", "25")
    persona2.mostrar_Persona()
