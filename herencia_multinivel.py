#Herencia multinivel en python
class Padre:
    def __init__(self):
        self.nombre = 'Padre'
    def caminar(self):
        print('Todos caminan')

class Hijo(Padre):
    def __init__(self):
        self.nombre = 'Hijo'

class Nieto(Hijo):
    def __init__(self):
        self.nombre = 'Nieto'


nieto = Nieto()
nieto.caminar() 

#En este ejemplo la clase hijo hereda de la super clase Padre, y la clase nieto hereada de la clase Hijo.
#Por ende la clase nieto hereda todos los atributos y metodos de la clase hijo.