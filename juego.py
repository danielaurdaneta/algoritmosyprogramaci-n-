from api import API_Configuracion
from tablero import Tablero
import time
from casilla import CasillaMina, CasillaVacia

class Juego:
    def __init__(self):
        self.api = API_Configuracion()
        self.tablero = None
        self.minas_restantes = 0
        self.jugando = False
        self.tiempo_inicio = 0

    def iniciar_juego(self, dificultad):
        config = self.api.get_config(dificultad)
        
        print(f"\nConfiguración para {dificultad}:")
        print(f"Tablero: {config['filas']}x{config['columnas']}")
        print(f"Minas: {config['minas']} ({config['minas']/(config['filas']*config['columnas'])*100:.0f}% del tablero)")
        
        self.tablero = Tablero(
            filas=config['filas'],
            columnas=config['columnas'],
            cantidad_minas=config['minas']
        )
        self.minas_restantes = config['minas']
        self.jugando = True
        self.tiempo_inicio = time.time()

    def obtener_tiempo(self):
        return int(time.time() - self.tiempo_inicio)

    def ejecutar_turno(self, accion, fila, columna):
        if not self.jugando:
            return False
            
        casilla = self.tablero.casillas[fila][columna]
        
        if accion == 'R':  # Revelar
            if self.tablero.casillas[fila][columna].es_bandera():
                print("¡Quita la bandera primero!")
                return False
                
            if casilla.revelar():
                self.jugando = False
                return "mina"
            
                
                
            if self.verificar_victoria():
                self.jugando = False
                return "victoria"
                
        elif accion == 'M':  # Marcar
            if casilla.revelada:
                print("No se puede marcar casilla revelada")
                return False
            self.tablero.revelar_casilla(fila, columna)
        
            if isinstance(self.tablero.casillas[fila][columna], CasillaMina):
                return "mina"
            
            if self.verificar_victoria():
                return "victoria"    

            if casilla.marca is None:
                if self.minas_restantes > 0:
                    casilla.marcar('bandera')
                    self.minas_restantes -= 1
                else:
                    print("¡No hay banderas disponibles!")
            elif casilla.marca == 'bandera':
                casilla.marcar('interrogante')
                self.minas_restantes += 1
            else:
                casilla.marcar(None)
                
        return False

    def verificar_victoria(self):
        for fila in self.tablero.casillas:
            for casilla in fila:
                if not isinstance(casilla, CasillaMina) and not casilla.revelada:
                    return False
        return True
    
    def revelar_casilla(self, fila, columna):
        """Revela una casilla y sus adyacentes si no hay minas alrededor (recursivo)"""
        # Si la casilla ya está revelada o tiene bandera, no hacer nada
        if self.casillas[fila][columna].revelada or self.casillas[fila][columna].es_bandera():
            return
            
        # Revelar la casilla actual
        self.casillas[fila][columna].revelada = True
            
        # Si es mina, terminar (no revelar adyacentes)
        if isinstance(self.casillas[fila][columna], CasillaMina):
            return
            
        # Si no hay minas alrededor, revelar recursivamente las adyacentes
        if self.casillas[fila][columna].minas_colindantes == 0:
            Tablero.revelar_colindantes(fila, columna)