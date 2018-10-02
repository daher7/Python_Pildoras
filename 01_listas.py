mi_lista = ["Jessica", "Troya", "David"]

mi_lista.append("Alex")                         # Agrega el elemento al final
mi_lista.insert(2, "Diego")                     # Agrega el elemento en la posicion que le indiquemos
mi_lista.extend(["Maria", "Pepe","Paquito"])    # Agrega una lista a la lista
mi_lista.remove("Paquito")                      # Elimina un elemento de la lista
mi_lista.remove(mi_lista[1])                    # Elimina un elemento de la lista por el indice
mi_lista.pop()                                  # Elimina el ultimo elemento de la lista

print(mi_lista[:])
print(mi_lista[1:])
print(mi_lista[-1])     # Con el indice -1 hace referencia al ultimo elemento, con el -2 al penultimo
print(mi_lista[::-1])   # Recorre la lista desde el ultimo elemento al primero

indice = mi_lista.index("Pepe") # Indica el indice
print(indice)

print("Alberto" in mi_lista) # Para saber si un elemento se encuentra en mi lista

nueva_lista = [1,2,3,"Hola",45.52]

lista_3 = mi_lista + nueva_lista # Une dos listas
print(lista_3 * 3) # Multiplica la lista tantas veces como le digamos
print(lista_3[:])