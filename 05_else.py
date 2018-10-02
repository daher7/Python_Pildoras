print("Verificacion de Usuario")

nota_alumno = float(input("Introduce tu nota: "))

if nota_alumno < 5:
    print("Suspenso")
elif nota_alumno < 6:
    print("Suficiente")
elif nota_alumno < 7:
    print("Bien")
elif nota_alumno < 9:
    print("Notable")
elif nota_alumno < 10:
    print("Sobresaliente")
else:
    print("Matricula de Honor")
    
print("El programa ha finalizado")