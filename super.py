#Super en python - sobreescribir el metodo de construccion
class Padre:
    def __init__(self):
        self.padre = 'Daniel'
        print(f'el padre se llama {self.padre}')

class Hijo(Padre):
    def __init__(self):
        super().__init__()#Utilizdo el constructor de la super clase Padre
        self.hijo = 'Juan'
        print(f'el hijo se llama {self.hijo}')


hijo = Hijo()

#El metodo super() sirve para llamar funciones de la super clase Padre

