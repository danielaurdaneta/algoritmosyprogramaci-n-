#Entrada que lea tres número e indique cual es mayor de ellos 

a = input("Introduce primer num")
b = input("Introduce segundo num")
c = input("Introduce tercer num")

a = float(a)
b = float(b)
c = float(c)

if a>b and a>c:
    print (f"El num más grande es {a}")
elif b>c and b>a:
    print (f"El num más grande es {b}")
else:
    print (f"El num más grande es {c}")

