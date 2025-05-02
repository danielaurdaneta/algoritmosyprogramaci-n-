num1= input("Escribe un número:")
num2= input("Escribe otro número:")

num1= float(num1)
num2= float(num2)


if num1 > num2:
    R=num1/num2
else:
    R=num2/num1

print(f"La división es: {R}")
