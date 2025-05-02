print("Bienvenidos a piedra, papel o tijeras")

Jugador_1= input ("Piedra, papel o tijera Jugador 1 ")
Jugador_2= input ("Piedra, papel o tijera Jugador 2 ")

if Jugador_1 == Jugador_2:
    print ("Empate")
elif Jugador_1 == "piedra" and Jugador_2 == "tijeras" or Jugador_1 == "papel" and Jugador_2 == "piedra" or Jugador_1 == "tijeras" and Jugador_2 == "papel":
    print("Ganó el jugador 1")
else:
    print("Ganó el jugador 2")