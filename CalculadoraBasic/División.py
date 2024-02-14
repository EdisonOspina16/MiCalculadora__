num1 = int(input("ingrese el primer numero: "))
num2= int(input("ingrese el segundo numero: "))

div = num1 // num2
if num2 == 0:
    print("Error, no se puede dividir por cero.")
else:
    print("El resultado es: ", div)

