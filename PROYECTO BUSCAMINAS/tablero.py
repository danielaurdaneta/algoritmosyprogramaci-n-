class tablero:
    def __init__  (self, filas, columnas, tablero):
        self.filas = filas 
        self.columnas = columnas 
        self.tablero = tablero 
    def show (self):
        print (f"{self.filas}{self.columnas}, {self.tablero}")
    def rellenar_tablero (self):
        pass
