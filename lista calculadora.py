

lista = [1,2,3,4,5,6,7,8,9,10]
print("escoge 2 numeros entre el 1 y el 10", lista)
a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))

if a == 1:
    print(b+a)
else:
    print("el resultado de la suma es:", b+a)

if a == 1:
    print(b-a)
else:
    print("el resultado de la resta es:", b-a)

if a == 1:
    print(b*a)
else:
    print("el resultado de la multiplicacion es:", b*a)

if a < 0:
    print("error")
else:
    print("el resultado de la division es:", b/a)