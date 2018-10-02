def divide():
    try:
        op1 = (float(input("Introduce un numero: ")))
        op2 = (float(input("Introduce otro numero: ")))

        print("La division es {}".format(op1/op2))   
    
    except ZeroDivisionError:
        print("Ha ocurrido un error. No se puede dividir entre 0")
        
    finally:
        print("Calculo finalizado")
    
divide()