persona = {
    "nombre":"johan",
    "apellido":"gonzalez",
    "estatura":1.84,
    "edad":18,
    "email":"johangonzalez.m38@gmail.com",
    "ciudaddenaci":"bogota",
    "genero":["femenino","masculino","otro"]
}

print(persona)
#mostrar un elemento de diccionario
print(f"el nombre de la persona:", {persona["nombre"]})
#agregar un elemento al diccionario
persona["telefono"]=3212496589
print(persona)
#modificar diccionario
persona["telefono"]=3133003795
print("nuevo numero de la persona es",persona)
#modfificar la clave del elemento
persona["celular"]= persona.pop("telefono")
print(persona)
#eliminar un elemento del diccionario
del persona["celular"]
print(persona)

#iterar los item de las claves y valores
for clave,valor in persona.items():
    print(clave , ":" , valor)






