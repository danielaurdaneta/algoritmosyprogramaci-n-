#CREAR UN MENU PARA PIZZA VEGETARIANA Y NORMAL
print ("Bienvenidos a pizzerría Bella Napoli")
opción = input ("Escoge una opción : /n1-Vegetariana  / n2- No vegetariana/n-")
ingrediente = ""
if opción == "1":
    opcion_ingrediente = input ("Seleccioana: /n1-Tofu/ n2- Pimiento/")
    if opcion_ingrediente == "1":
        ingrediente = ("Tofu")
    else:
        ingrediente= ("Pimiento")

elif opción == "2":
    opcion_ingrediente = input("Seleccioana /n1-Pepperoni/ n2- Jamon/ n3- Piña/")
    if opcion_ingrediente == "1":
        ingrediente = ("Pepperoni")
    elif opcion_ingrediente == "2":
        ingrediente = ("Pimiento")
    else:
        ingrediente =  ("Piña")

if opción == "1":
    print (f"Tu pizza es Vegetariana y tiene{ingrediente} ")
else:
    print (f"Tu pizza no ees Vegetariana y tiene {ingrediente} ")



