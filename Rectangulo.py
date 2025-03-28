class Rectangulo:
    def __init__(self, punto_inicial, punto_final):
        self.punto_inicial = punto_inicial
        self.punto_final = punto_final

    def base(self):
        return abs(self.punto_final.x - self.punto_inicial.x)
    
    def altura(self):
        return abs (self.punto_final.y - self.punto_inicial.y)
    
    def area(self):
        return self.base() * self.altura()
