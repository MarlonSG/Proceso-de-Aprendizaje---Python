print("Sistema de Playlist de Musica")

lista_reproduccion = []
numero_caciones = int(input("¿Cuantas musicas deseas agregar?: "))

for indice in range(numero_caciones):
    cancion = input(f"Ingrese la cacion {indice + 1}de la musica: ")
    lista_reproduccion.append(cancion)

#ordenar alfabeticamente ascedente
lista_reproduccion.sort()

#ordenar de manera descendente
#lista_reproduccion.sort(reverse=True)

print() #salto de linea

#iterando
for cancion in lista_reproduccion:
    print(f"- {cancion}")