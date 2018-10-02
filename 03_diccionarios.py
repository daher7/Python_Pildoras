# Se asignan mediante {}
mi_diccionario = {"Francia":"Paris","España":"Madrid","Noruega":"Oslo"}
print(mi_diccionario["Francia"])
print(mi_diccionario)

mi_diccionario["Italia"] = "Lisboa" # Para añadir una nueva pareja
mi_diccionario["Italia"] = "Roma"   # Sobreescribe un valor

del mi_diccionario["Noruega"] # Elimina un valor

diccionario = {"Alemania":"Berlin", 23:"Jordan", "Mosqueteros":4}

mi_tupla = ("España","Francia","Inglaterra","Alemania")
nuevo_diccionario = {mi_tupla[0]:"Madrid", mi_tupla[1]:"Paris", mi_tupla[2]:"Londres", mi_tupla[3]:"Berlin"}

print(nuevo_diccionario.keys())
print(nuevo_diccionario.values())
print(len(nuevo_diccionario))