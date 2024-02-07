#alturas de personas y sacar su promedio

per = int(input("Ingrese la cantidad de personas: "))
acumula = 0


for i in range(per):
    altura = float(input("Ingrese la altura de la persona en metros:"))
    acumula += altura


altura_promedio = acumula / per


print("La altura promedio de las  personas es: metros",altura_promedio)