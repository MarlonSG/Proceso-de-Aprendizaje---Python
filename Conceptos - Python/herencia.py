class Animal:
    def comer(self):
        print('Como muchas veces el día')

    def dormir(self):
        print('Duermo muchas horas')

class Perro(Animal):
    def hacer_sonido(self):
        print('Puedo ladrar')

    def dormir(self): # Modificar Dormir
        print('Duermo 15 Horas')

# Programa principal
print('*** Ejemplo de Herencia en Python ***')
print('Clase Padre, soy un Animal')
animal1 = Animal()
animal1.comer()
animal1.dormir()

print('\nClase Hija, soy un Perro')
perro1 = Perro()
perro1.comer()
perro1.dormir()  #SE LLAMA A LA MODIFICACION COMO UNA NORMAL
perro1.hacer_sonido()