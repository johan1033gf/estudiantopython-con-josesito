#que diga si una es biciesto  o no
año = int(input("ingrese el año que necesita:")) #año de mi nacimiento

if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
    print("es biciesto")
else:
    print("no es biciesto")