#diccionario ejercisio
def Ingresaralumno():
    Nombre = input("Ingrese el nombre del alumno: ")
    Notas = []
    while True:
        Nota = float(input("Ingrese la nota del alumno (ingrese un número negativo para registrar): "))
        if Nota < 0:
            break
        Notas.append(Nota)
    return Nombre, Notas

def Calcularpromedio(Notas):
    return sum(Notas) / len(Notas)

def main():
    Alumnos = {}
    while True:
        Cantidadalumnos = int(input("Ingrese la cantidad de alumnos que desea ingresar (ingrese un número negativo para registrar): "))
        if Cantidadalumnos < 0:
            break
        for _ in range(Cantidadalumnos):
            Nombre, Notas = Ingresaralumno()
            if Nombre in Alumnos:
                print("Error: El nombre del alumno ya existe.")
            else:
                Alumnos[Nombre] = Notas
                print("Alumno ingresado correctamente.")
        print("\n")
    print("Lista de alumnos con promedio:")
    for Nombre, Notas in Alumnos.items():
        Promedio = Calcularpromedio(Notas)
        print(f"{Nombre}: {Promedio}")

if __name__ == "__main__":
    main()
