#Herencia entre clases en python

class Animal: #Super clase
    def comer(self):
        print('El animal esta comiendo')

class Perro(Animal): #La clase perro esta heredando de la super clase (Animal)
    def __init__(self):
        self.color = 'marron'

    
class Gato(Animal): #La clase Gato esta heredando de la super clase (Animal)
    def __init__(self):
        self.color = 'verde'
    

perro = Perro() #Creo una instancia de la clase Perro()
perro.comer() #Uso esta instancia para ejecutar el metodo comer de la clase Animal 

gato = Gato()
gato.comer()


        

    
