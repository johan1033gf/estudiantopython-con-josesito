#sueldos de empresa 
empleados10m = 0
empleados3m = 0
gastot = 0

while True:
    sueldo = float(input("Ingrese el sueldo del empleado:"))
    if sueldo < 0:
        break
    gastot += sueldo
    if sueldo >= 10000000 and sueldo <= 30000000:
        empleados10m += 1
    if sueldo > 3000000:
        empleados3m += 1

# Mostrar resultados
print("Cantidad de empleados que cobran entre $1.000.000 y $10.000.000:", empleados10m)
print("Cantidad de empleados que cobran más de $3.000.000:", empleados3m)
print("Gasto total en sueldos al personal: $", gastot)