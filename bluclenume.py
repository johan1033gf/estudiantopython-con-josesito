import random

secreto = random.randint(1,10)

numero = int(input("adivina el numero 1 a 10"))

while numero !=secreto:
    if numero < secreto:
        print("el numero es mayor")
    else:
        print("el numero s menor")
        
    numero = int(input("intenta de nuevo"))
print("felicitaciones adivinaste el numero secreto:",secreto)

