#EJER7
def menu():
    print("1-Añadir número a la lista")
    print("2-Añadir número de la lista en una posición")
    print("3-Longitud de la lista")
    print("4-Eliminar el último número")
    print("5-Eliminar un número")
    print("6-Contar números")
    print("7-Posiciones de un número")
    print("8-Mostrar números")
    print("9-Salir")

def añadirnumero(lista):
    numero = int(input("Introduce un número: "))
    lista.append(numero)

def añadirnumeposicion(lista):
    numero = int(input("Introduce un número: "))
    posicion = int(input("Introduce la posición: ")) - 1
    if 0 <= posicion <= len(lista):
        lista.insert(posicion, numero)
    else:
        print("La posición no es válida")

def longitudlista(lista):
    print("La longitud de la lista es:", len(lista))

def eliminultinumero(lista):
    if lista:
        numero_eliminado = lista.pop()
        print("Se eliminó el número:", numero_eliminado)
    else:
        print("La lista está vacía")

def elimnumero(lista):
    posicion = int(input("Introduce la posición del número a eliminar: ")) - 1
    if 0 <= posicion < len(lista):
        numelimi = lista.pop(posicion)
        print("Se eliminó el número:", numelimi)
    else:
        print("La posición no es válida")

def contarnumeros(lista):
    numero = int(input("Introduce el número a contar: "))
    conteo = lista.count(numero)
    print("El número", numero, "aparece", conteo, "veces en la lista")

def posicionesnumero(lista):
    numero = int(input("Introduce el número a buscar: "))
    posiciones = [i + 1 for i, x in enumerate(lista) if x == numero]
    if posiciones:
        print("El número", numero, "se encuentra en las posiciones:", posiciones)
    else:
        print("El número", numero, "no se encuentra en la lista")

def mostrarnumeros(lista):
    print("Los números de la lista son:", lista)

def main():
    lista = []
    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            añadirnumero(lista)
        elif opcion == "2":
            añadirnumeposicion(lista)
        elif opcion == "3":
            longitudlista(lista)
        elif opcion == "4":
            eliminultinumero(lista)
        elif opcion == "5":
            elimnumero(lista)
        elif opcion == "6":
            contarnumeros(lista)
        elif opcion == "7":
            posicionesnumero(lista)
        elif opcion == "8":
            mostrarnumeros(lista)
        elif opcion == "9":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida")

if __name__== "__main__":
    main()