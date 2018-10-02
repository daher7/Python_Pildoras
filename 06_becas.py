print("Programa de Becas año 2018")
distancia_escuela = int(input("Introduce la distancia a la escuela en km: "))
print("Distancia a la escuela es de {} km".format(distancia_escuela))

numero_hermanos = int(input("Introduce el número de hermanos que tienes: "))
if numero_hermanos == 0:
    print("No tienes hermanos")
else:
    print("Tienes {} hermanos".format(numero_hermanos))
    

salario_familia = int(input("Introduce salario anual bruto: "))
print("El salario anual es de {} euros".format(salario_familia))

if distancia_escuela > 20 and numero_hermanos>2 or salario_familia <= 20000:
    print("Tienes derecho a beca")
else:
    print("No tienes derecho a beca")
    

"""
*******************************************************************************
"""
print("Elige una asignatura optativa")
asignatura = input("Elige entre Biología, Matématicas, Filosofía, Ética: ")
optativas = ["Biología", "Matemáticas", "Filosofía", "Ética"]

if asignatura in optativas:
    print("La asignatura elegida es {}".format(asignatura))
else:
    print("La asignatura elegida no está contemplada")