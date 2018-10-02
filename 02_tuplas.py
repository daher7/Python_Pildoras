# LAS TUPLAS NO SE PUEDEN MODIFICAR!!!!!
mi_tupla = ("David", 27, 1977, True, 27)
print(mi_tupla)
print(mi_tupla[2])
# Las listas van entre [] y las tuplas entre ()

# Convertir una tupla en una lista -> list()
mi_lista = list(mi_tupla)
print(type(mi_lista))
print(type(mi_tupla)) 

# Convertir una lista en tupla -> tuple()
nueva_lista = ["Hola", "Paquito", 2, 4]
nueva_tupla = tuple(nueva_lista)
print(type(nueva_tupla))

# Acceder a los indices
print(mi_tupla[2])
print(nueva_tupla[3])

# Comprobar si hay un elemento dentro de la tupla
print("David" in nueva_tupla)
print("David" in mi_tupla)

# Saber los elementos que hay en la tupla
print(mi_tupla.count(27))
print(mi_tupla.count(mi_tupla[2]))

# Para saber la longitud de una tupla -> len(mi_tupla)
print(len(mi_tupla))

# Para dibujar tuplas unitarias, es decir, con un solo elemento
# hay que poner una , al final
tupla_unitaria = ("Troya",)
print(len(tupla_unitaria))

# Se pueden declarar variable usando como el valor el contenido que hay
# dentro de una tupla
valores = ("Paquito", 34, "Londres", 1987, "Perro")
nombre, edad, ciudad, anio, especie = valores
print(nombre)
print(especie)
print(ciudad)