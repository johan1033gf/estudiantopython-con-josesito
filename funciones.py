def Inicio():

    print("Menu principal")
    print("Seleccione la opcion correcta:")
    print("1. Para sumar")
    print("2. Operacion resta")
    print("3. Operacion dividir")
    print("5. Salir")

def main():
    while True:
        Inicio()
        Opcion = int("Selecciona la opcion")
        if Opcion == 1:
            print("Ha seleccionado la suma")
            Num1 = int(input("Ingresar el primer numero"))
            Num2 = int(input("Ingresar el numero 2"))
            Sumar = Num1+Num2
            print("El resultado de la suma es:",Sumar)
        elif Opcion == 2:
            print("Ha seleccionado opcion resta")
            Num1 = int(input("Ingresar el primer numero"))
            Num2 = int(input("Ingresar el numero 2"))
            Restar = Num1-Num2
            print("Ha seleccionado operacion resta",Restar)
        elif Opcion == 3:
            print("Ha seleccionado la opcion multipli")
        elif Opcion == 4:
            print("Ha seleccionado la opcion dividir")
        elif Opcion == 5:
            print("Hasta luego")
            break
        else:
            print("Opcion no valida, seleccione una opcion valida")
            main()