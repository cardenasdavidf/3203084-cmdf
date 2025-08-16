diassemana = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")
print("Tercer día de la semana:", diassemana[2])
try:
    diassemana[1] = "MartesS"
except TypeError as error:
    print("Error al modificar la tupla:", error)
