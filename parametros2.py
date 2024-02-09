#recatngulo
ancho = int(input("ingrese ancho del rectagunlo"))
altura = int(input("ingrese la altura del rectangulo"))
caracter = input("ingrese el carcter a utilizar")

def dibujar(an,al,letra):
    for i in range(an):
        for j in range(al):
            print(letra,end=" ")
        print()


dibujar(ancho,altura,caracter)




