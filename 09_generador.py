def generaPares(limite):
    num = 1
    miLista = []
    while num < limite:
        miLista.append(num*2)
        num = num + 1
    return miLista

print(generaPares(10))

"""
"""
def generaPares2(limite):
    num = 1
    while num < limite:
        yield num*2
        num = num+1

devuelvePares = generaPares2(10)

for i in devuelvePares:
    print(i)
    
"""
"""

def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        # for subElemento in elemento:
            yield from elemento

ciudades_devueltas = devuelve_ciudades("Madrid", "Barcelona", "Zaragoza", "Santander")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))