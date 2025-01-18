print("Manejo de Listas")
# Se crea una lista
mi_lista = [1,2,3,4,5]
print(mi_lista)

# conteo de la lista
print(len(mi_lista))

# Acceder a un tipo de la lista [4] en este caso
print(mi_lista[4])

#en este caso seria en negativo (de atras hacia adelante)
print(mi_lista[-1])

#modificar un elemento de una lista
mi_lista[1] = 10
print(mi_lista)

#agregar elementos a la lista
mi_lista.append(6)
print(mi_lista)

#agregar un elemento en un indice especifico
mi_lista.insert(2,15)
print(mi_lista)

#eliminar elementos (especifico ya que 5 era 5) de una lista usando "remove"
mi_lista.remove(5)
print(mi_lista)

#eliminar por indice
mi_lista.pop(1)
print(mi_lista)

#eliminar usando "del"
del mi_lista[2]
print(mi_lista)

#obtener sublistas
sublista = mi_lista[1:3]
print(sublista)