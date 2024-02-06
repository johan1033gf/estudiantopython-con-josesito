edad = int(input("ingrese su edad porfavor"))

if edad < 4:
    ingreso = 0
elif edad <=18:
    ingreso = 5000
else:
    ingreso = 10000
    
print("precio de entrada es",ingreso)