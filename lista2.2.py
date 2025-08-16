a =(int("ingrese los valores"))
b =(int("ingrese los valores"))

list = [1,2,3,4]
nose = int(input("1.suma,2.resta,3.multiplicacion, 4.division"))
if nose == list[0]:
   print("seleccionaste suma")
   print (b+a)
if nose == list[1]:
   print("seleccionaste resta")
   print (b-a)
if nose == list[2]:
   print("seleccionaste multiplicacion")
   print (b*a)
if nose == list[3]:
   print("seleccionaste division")
   print (b/a)
else:
   print("Opcion no valida")