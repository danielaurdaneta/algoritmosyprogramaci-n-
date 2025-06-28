import os
import time
from juego import Juego
from casilla import CasillaMina
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu_principal():
    limpiar_pantalla()
    print("\n" + "═" * 50)
    print(" BUSCAMINAS ".center(50, '★'))
    print("═" * 50)
    print("1. Nueva partida")
    print("2. Ver records")
    print("3. Salir")
    print("═" * 50)

def mostrar_tablero(juego):
    """Muestra el tablero con formato mejorado y colores"""
    limpiar_pantalla()
    
    # Encabezado con información del juego
    print(f"\n{' MINAS RESTANTES: ' + str(juego.minas_restantes):<25}", end="")
    print(f"{'TIEMPO: ' + str(juego.obtener_tiempo()) + ' segundos':>25}")
    
    # Encabezado de columnas (números)
    print("   " + " ".join(f"{i+1:2}" for i in range(juego.tablero.columnas)))
    print("   " + "─" * (juego.tablero.columnas * 3 - 1))
    
    # Filas del tablero
    for f in range(juego.tablero.filas):
        # Número de fila
        print(f"{f+1:2}│", end="")
        
        for c in range(juego.tablero.columnas):
            casilla = juego.tablero.casillas[f][c]
            
            # Casilla revelada
            if casilla.revelada:
                if isinstance(casilla, CasillaMina):
                    print(" *", end="")  # Mina
                else:
                    # Mostrar número o espacio vacío
                    print (f" {casilla.minas_colindantes}" if casilla.minas_colindantes > 0 else " 0", end="")



            # Casilla oculta
            else:
                if casilla.marca == 'bandera':
                    print(" F", end="")  # Bandera
                elif casilla.marca == 'interrogante':
                    print(" ?", end="")  # Interrogante
                else:
                    print(" ■", end="")  # Casilla no revelada
        print()  # Nueva línea

def mostrar_dificultades(juego):
    print("\nSeleccione dificultad:")
    for i, (key, value) in enumerate(juego.api.dificultad.items(), 1):
        print(f"{i}. {value}")

def jugar_partida(juego):
    nombre = input("\nIngrese su nombre: ")
    juego.api.jugador = nombre
    
    mostrar_dificultades(juego)
    
    while True:
        try:
            opcion = int(input("\nOpción (1-4): "))
            dificultades = list(juego.api.dificultad.keys())
            if 1 <= opcion <= 4:
                juego.iniciar_juego(dificultades[opcion-1])
                break
            print("¡Opción inválida!")
        except ValueError:
            print("Ingrese un número válido")
    
    while juego.jugando:
        mostrar_tablero(juego)
        
        try:
            fila = int(input("\nFila (1-{}): ".format(juego.tablero.filas))) - 1
            if not 0 <= fila < juego.tablero.filas:
                print("¡Fila inválida!")
                continue
                
            col = int(input("Columna (1-{}): ".format(juego.tablero.columnas))) - 1
            if not 0 <= col < juego.tablero.columnas:
                print("¡Columna inválida!")
                continue
                
            accion = input("Acción (R: Revelar, M: Marcar, S: Salir): ").upper()
            if accion not in ('R', 'M', 'S'):
                print("Acción no válida")
                continue
                
        except ValueError:
            print("Ingrese números válidos")
            continue
            
        if accion == 'S':
            confirmar = input("¿Salir? (S/N): ").upper()
            if confirmar == 'S':
                return
                
        resultado = juego.ejecutar_turno(accion, fila, col)
        
        if resultado == "mina":
            mostrar_tablero(juego)
            print("\n¡BOOM! ¡Has perdido!")
            juego.api.guardar_record(juego.obtener_tiempo())
            input("\nPresione Enter para continuar...")
            return
            
        elif resultado == "victoria":
            mostrar_tablero(juego)
            print("\n¡FELICIDADES! ¡Has ganado!")
            print(f"Tiempo: {juego.obtener_tiempo()} segundos")
            juego.api.guardar_record(juego.obtener_tiempo())
            input("\nPresione Enter para continuar...")
            return

def mostrar_records(juego):
    limpiar_pantalla()
    print("\nMEJORES TIEMPOS")
    print("═" * 50)
    
    records = juego.api.get_records()
    if not records:
        print("No hay records registrados aún")
    else:
        for i, record in enumerate(records[:3], 1):
            print(f"{i}. {record.get('name', 'Anónimo')}: {record.get('time', '?')} segundos")
    
    input("\nPresione Enter para volver al menú...")

def main():
    juego = Juego()
    
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            jugar_partida(juego)
        elif opcion == '2':
            mostrar_records(juego)
        elif opcion == '3':
            print("¡Gracias por jugar!")
            break
        else:
            print("Opción no válida")
            input("Presione Enter para continuar...")

if __name__ == "__main__":
    main()