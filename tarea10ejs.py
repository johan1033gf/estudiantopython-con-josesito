#ejercisio 10


def ingresarnotas():
    alumnos = {}
    numalumn = int(input("Ingrese el número de alumnos: "))

    for _ in range(numalumn):
        nombre = input("Ingrese el nombre del alumno: ")
        if nombre in alumnos:
            print("Error: El nombre del alumno ya existe.")
            continue

        notas = []
        while True:
            nota = float(input(f"Ingrese la nota para {nombre} (ingrese un número negativo para terminar): "))
            if nota < 0:
                break
            notas.append(nota)

        alumnos[nombre] = notas

    return alumnos

def calcumedia(notas):
    return sum(notas) / len(notas)

def mostrarresultados(alumnos):
    print("\nLista de Alumnos y Nota Media:")
    for alumno, notas in alumnos.items():
        media = calcumedia(notas)
        print(f"{alumno}: {media:.2f}")

def main():
    alumnos = ingresarnotas()
    mostrarresultados(alumnos)

if __name__ == "__main__":
    main()