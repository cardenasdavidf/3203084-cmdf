def convertirtemperatura():
    print("Calculadora de temperatura")
    print("1. Celsius a Fahrenheit")
    print("2. Celsius a Kelvin")
    print("3. Fahrenheit a Celsius")
    print("4. Fahrenheit a Kelvin")
    print("5. Kelvin a Celsius")
    print("6. Kelvin a Fahrenheit")
    try:
        opcion = int(input("Seleccione alguna opción (1-6): "))
        if opcion < 1 or opcion > 6:
            print("Esa opción es inválida")
            return
        temp = float(input("Digite la temperatura: "))
        if opcion == 1:
            resultado = temp * 9/5 + 32
            print(f"Resultado: {resultado:.2f}°F")
        elif opcion == 2:
            resultado = temp + 273.15
            print(f"Resultado: {resultado:.2f}K")
        elif opcion == 3:
            resultado = (temp - 32) * 5/9
            print(f"Resultado: {resultado:.2f}°C")
        elif opcion == 4:
            resultado = (temp - 32) * 5/9 + 273.15
            print(f"Resultado: {resultado:.2f}K")
        elif opcion == 5:
            resultado = temp - 273.15
            print(f"Resultado: {resultado:.2f}°C")
        elif opcion == 6:
            resultado = (temp - 273.15) * 9/5 + 32
            print(f"Resultado: {resultado:.2f}°F")
    except ValueError:
        print("Error: Digite valores numéricos válidos.")
convertirtemperatura()
