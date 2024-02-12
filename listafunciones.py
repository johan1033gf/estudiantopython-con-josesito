def ingresar():
    enteros = []
    
    for x in range(5):
        num = int(input("ingrese el numero"))
        enteros.append(num)
        
def imprimir(enteros):
    
    print("los datos de la lista son:")
    for x in enteros:
        print(x)        
        
ingresar()
imprimir()       