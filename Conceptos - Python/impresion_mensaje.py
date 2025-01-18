mensaje = input("Ingresa un mensaje: ").strip()
repeticiones = int(input("Ingresa una cantidad repeticiones: ").strip())

#for _ in range(repeticiones):   #de esta forma no se usara " i " y se reeemplaza por "_" porque no se usa
for i in range(repeticiones):
    print(f"{i+1} - {mensaje}")   # el +1 aumenta amigablemente el indice para el usuario (opcional)
   # print(mensaje)