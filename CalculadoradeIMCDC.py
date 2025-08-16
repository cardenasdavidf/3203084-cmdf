try:
    peso = float(input("Digite su peso en kg: "))
    altura = float(input("Digite su altura en metros: "))
    imc = peso / (altura ** 2)
    if imc < 18.5:
        categoria = "Bajo peso"
    elif imc < 25:
        categoria = "Peso normal"
    elif imc < 30:
        categoria = "Sobrepeso"
    else:
        categoria = "Obesidad"
    print(f"\nSu IMC es: {imc:.2f}")
    print(f"Categoría: {categoria}")
except ValueError:
    print("Error: Digite valores numéricos válidos.")
except ZeroDivisionError:
    print("Error: La altura no puede ser cero.")
#David Cardenas 3203084