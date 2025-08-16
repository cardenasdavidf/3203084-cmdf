edad = int(input("Ingresa tu edad:"))
registrado = True

# Condición para poder votar
if edad > 17 and registrado:
    print("Puedes votar.")
else:
    print("No puedes votar.")
