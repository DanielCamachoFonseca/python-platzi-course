#Propiedades generales generales
class Punto:
    def __init__(self, a,b):
        self.a = a
        self.b = b
    
    def mostrar_puntos(self):
        print(f'{self.a},{self.b}')

punto_a = Punto(1,4)
punto_b = Punto(3,4)

