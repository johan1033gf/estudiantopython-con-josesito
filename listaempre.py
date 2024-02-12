Nombreconductores = ["Johan Gonzalez", "Jose angel", "Duvan Totena"]
kilometros = [
    [250, 128, 115, 130, 172, 156, 223],  
    [125, 140, 130, 150, 160, 170, 180],  
    [113, 130, 123, 145, 150, 160, 170],  
    [120, 150, 188, 160, 170, 180, 190],  
    [148, 160, 150, 170, 180, 190, 255],  
    [158, 199, 188, 180, 190, 222, 210],  
    [163, 180, 179, 190, 200, 210, 220]   
]

total_kilo = [sum(fila) for fila in kilometros]

for M in range(len(Nombreconductores)):
    print(f"{Nombreconductores[M]}: {total_kilo[M]} km")
    
    