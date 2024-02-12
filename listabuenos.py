nombres = []
notas = []
muybueno = 0
bueno = 0
insufi = 0
amejor = []
eliminar =  []

for x in range(1,4):
    nom = input("porfavor ingrese el nombre de socio")
    nombres.append(nom)
    no = int(input("porfavor ingresar notas :{x}"))
    notas.append(no)
#recorer lista

for y in range(1,4):
    print(nombres[y])
    print(notas[y])



if notas[y]>=8:
    print("pasa la materia estupido muy bueno")
    muybueno += 1
    amejor.append(nombres[y])
else:
    if notas[y]>=4:
         print("paso raspando patico")
         bueno +=1
    else:
        print("perdio la materia ñero")
        insufi +=1  
        
for z in len(notas):
    if notas[z]>=4 and notas[z]<=7:
        notas.pop(z)
        nombres.pop(z)       

eliminar = []
for z in range(len(notas)):
    if 4 <= notas[z] <= 7:
        
        
        eliminar.append(z)
for d in sorted(eliminar,reverse= True):
    notas.pop(d)
    nombres.pop(d)






print("cantida de alumnos muy buenos son: ",muybueno)
print("los nombres de los mejores alumnos son:",amejor)
print("listado de alumnnos",nombres[z])
     
        
        
        
          

