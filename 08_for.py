for i in ["Hola", "Adios", "Ta luego"]:
    print("Yo")
    
for i in "tengountractoramarilloqueesloquesellevaahora":
    print("Hola")
    
for i in "tengountractoramarilloqueesloquesellevaahora":
    print("Hola", end=" ")
    
    
    
email = False
for i in "daher7@hotmail.com":
    if i == "@":
        email = True
    
if email:
    print("El email es correcto")
else:
    print("El email no es correcto")
    

for i in range(5):
    print(i)

for i in range(5):
    print(f"Valor de {i}")
    
for i in range(5,50,3):     # Entre 5 y 50 de 3 en 3
     print(f"Valor de {i}")
"""
"""
     
valido = False
email = input("Introduce tu email: ")

for i in range(len(email)):
    if email[i] == "@":
       valido = True

if valido:
    print("El email es correcto")
else:
    print("El email no es correcto")