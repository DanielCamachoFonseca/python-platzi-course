#Comparacion de objetos instanciados dentro de python para
class Punto:
    def __init__(self, a,b):
        self.a = a 
        self.b = b 

    def __eq__(self,other): #Sobreescribi el metodo __eq__
        return self.a == other.a and self.b == other.b #Compara el contenido de los puntos a , b



punto_a = Punto(5,7)
punto_b = Punto(5,7)
print(punto_a == punto_b) #Compara los espacios en memoria de los puntos a , b

print(punto_a.a + punto_b.a) #Suma los numeros en sus posiciones a


