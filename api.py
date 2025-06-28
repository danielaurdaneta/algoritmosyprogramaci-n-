import requests

class API_Configuracion:
    def __init__(self):
        self.base_url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main"
        self.jugador = None
        self.dificultad = {
            "easy": "Fácil (10% minas)",
            "medium": "Medio (30% minas)", 
            "hard": "Difícil (60% minas)",
            "impossible": "Imposible (80% minas)"
        }

    def get_config(self, dificultad):
        """Obtiene configuración y calcula minas correctamente"""
        response = requests.get(f"{self.base_url}/config.json")
        response.raise_for_status()
        config = response.json()            
        if not all(key in config.get("global", {}) for key in ["board_size", "quantity_of_mines"]):
            raise ValueError("JSON inválido")
            
        tamaño = config["global"]["board_size"]
        porcentaje = config["global"]["quantity_of_mines"].get(dificultad)
            
        if porcentaje is None:
            raise ValueError(f"Dificultad '{dificultad}' no existe")
            
        total = tamaño[0] * tamaño[1]
        minas = int(total * porcentaje)
        minas = max(1, minas)  # Mínimo 1 mina
            
        return {
            "filas": tamaño[0],
            "columnas": tamaño[1],
            "minas": minas
            }
            

    def get_records(self):
            response = requests.get(f"{self.base_url}/leaderboard.json")
            response.raise_for_status()
            records = response.json()
            return sorted(records, key=lambda x: x.get("time", 0))[:3]


    def guardar_record(self, tiempo):
        if self.jugador:
            print(f"\n¡Record de {self.jugador}: {tiempo} segundos!")
            #aquí se enviaría a la API
