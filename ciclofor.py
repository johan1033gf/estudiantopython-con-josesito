def obtener_promedio(edades):
    total = sum(edades)
    promedio = total / len(edades)
    return promedio

edades_manana = []
for i in range(6):
    edad = int(input("Ingrese la edad del estudiante del turno mañana: "))
    edades_manana.insert(edad)

edades_tarde = []
for i in range(7):
    edad = int(input("Ingrese la edad del estudiante del turno tarde: "))
    edades_tarde.insert(edad)

edades_noche = []
for i in range(12):
    edad = int(input("Ingrese la edad del estudiante del turno noche: "))
    edades_noche.insert(edad)

promedio_manana = obtener_promedio(edades_manana)
promedio_tarde = obtener_promedio(edades_tarde)
promedio_noche = obtener_promedio(edades_noche)

print("Promedio de edades del turno mañana ", promedio_manana)

print("Promedio de edades del turno tarde ", promedio_tarde)

print("Promedio de edades del turno noche ", promedio_noche)


