#Seleccionada va a ser un atributo booleano, true o false, método va a ser
# placeholder, método marcar y el método revelar. Se crea mina que sería una
# clase hija de casillas, y se tienen dentro de ella los métodos terminar juego, 
# mostrar mina. otra clase hija de casillas sería blank con su método mostrar. 

class casillas:
    def __init__ (self, seleccionada= False):
        self.seleccionada = seleccionada
        self.revelar = False
        self.marcar = None
        self.alrededor = 0
    def mostrar (self):
        if self.revelar and self.marcar is True:
            self.revelar = True
            return (self.alrededor)
        return False 
    def marcar (self):
        if not self.revelada:
            pass
    def revelar (self):

class mina (casillas):
    def __init__ (self, seleccionada):
        super().__init__ (seleccionada)
    def terminar_juego (self):
        pass
    def show (self):
        print (f"{self.seleccionada}")
        
    
#esto es de la clase casillas, en edición
    def __str__(self):
        if self.revelada:
            return '💣' if self.es_mina else str(self.num_minas_alrededor)
        elif self.marcada == 'bandera':
            return '🚩'
        elif self.marcada == 'interrogante':
            return '❓'
        return '■'