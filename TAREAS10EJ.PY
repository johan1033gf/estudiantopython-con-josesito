#EJERCISIO 8

preciofrutas = {
    'manzana': 2.5,
    'banana': 1.8,
    'naranja': 2.0,
    'pera': 3.0,
    'kiwi': 2.2
}

def calculaprecfruta(fruta, cantidad):
    preciounit = preciofrutas.get(fruta)
    if preciounit is None:
        print("Lo siento, la fruta", fruta, "no está en la lista de precios.")
        return None
    else:
        preciototal = preciounit * cantidad
        return preciototal

def main():
    while True:
        fruta = input("Ingrese el nombre de la fruta vendida: ").lower()
        cantidad = int(input("Ingrese la cantidad vendida: "))

        precio = calculaprecfruta(fruta, cantidad)
        if precio is not None:
            print("El precio total de", cantidad, fruta, "es:", precio)

        respuesta = input("¿Desea hacer otra consulta? (s/n): ").lower()
        if respuesta != 's':
            print("¡Hasta luego!")
            break

if __name__ == "__main__":
    main()