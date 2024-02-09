texto = "buenos dias definiendo un parametro en ptrhon"




def mensaje():
    n1 = int(input("ingresa primer numero"))
    n2 = int(input("ingrese en segundo numero"))
    calcularmayor(n1,n2)
    positivo(n1,n2)
    
def calcularmayor(num1,num2):    
    if num1>num2:
         print("el n1 es mayor")
    elif num1==num2:
         print("son iguales")
    else:
         print("el n2 es mayor")
    

def positivo(p1,p2):
    if p1>0 or p2>0:
        print("nuevo psitivo")
    
    elif p1<0 and p2<0:
        print("son ngeativos")
    else:
        print("almenos un numero no es posotivo")  
        
mensaje()   
    
    
    
    
    
    
    








































