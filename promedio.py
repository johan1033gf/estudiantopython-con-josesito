#solicitar 10 numeros y solicitar su promedio utilizando while
acumulador = 0
contnum = 0  
while contnum <10:
    numero = int(input("ingrese un numero broo"))
    
    acumulador=acumulador+numero
    
    contnum += 1
    promedio= acumulador/ 10
    print ("el promedio es",promedio)

    