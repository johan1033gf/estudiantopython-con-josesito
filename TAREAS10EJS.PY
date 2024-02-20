#EJ 9
def crearcestacompra():
    cestacompra = {}
    while True:
        articulo = input("Ingrese el nombre del artículo (o 'fin' para terminar): ")
        if articulo.lower() == 'fin':
            break
        precio = float(input("Ingrese el precio del artículo: "))
        cestacompra[articulo] = precio
    return cestacompra

def mostrarcestacompra(cesta_compra):
    print("Lista de compra:")
    total_coste = 0
    for articulo, precio in cesta_compra.items():
        print(f"{articulo:<15} {precio:.2f}")
        total_coste += precio
    print(f"\nTotal{'':<10} {total_coste:.2f}")

def main():
    print("Bienvenido a la creación de la cesta de la compra.")
    cestacompra = crearcestacompra()
    print("\n¡Cesta de la compra creada!\n")
    mostrarcestacompra(cestacompra)

if __name__ == "__main__":
    main()