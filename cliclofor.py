#usando ciclo for

frase = input("ingrese una frase")
letra = input("letra que quiere buscar")
contador = 0

for i in frase:
    if i == letra:
        contador+=1
        
        
print("la letra se ve una '%s' cantidad de %2i en la frase '%s'. "%(letra,contador,frase))  



