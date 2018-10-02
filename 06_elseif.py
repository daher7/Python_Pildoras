edad = 145

if 0 < edad < 135:
    print("La edad es correcta")
else:
    print("La edad NO es correcta")
    
# Trabajadores de una EMPRESA
salario_presidente = int(input("Introduce el salario del presi: "))
print("Salario del Presidente es {0}".format(salario_presidente))

salario_director = int(input("Introduce el salario del director: "))
print("Salario del Presidente es {0}".format(salario_director))

salario_jefe_area = int(input("Introduce el salario del jefe de area: "))
print("Salario del Presidente es {0}".format(salario_jefe_area))

salario_administrativo = int(input("Introduce el salario del administrativo: "))
print("Salario del Presidente es {0}".format(salario_administrativo))

if salario_presidente>salario_director>salario_jefe_area>salario_administrativo:
    print("Todo funciona correctamente")
else:
    print("Algo falla en la empresa")