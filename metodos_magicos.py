#Metodos magicos en python, metodos predefinidos dentro de python
class Persona:
    def __init__(self):
        self.nombre = 'Daniel'
    
    def __str__(self): #Estoy reescribiendo el metodo str definido por python
        return f'este objeto se llama {self.nombre}'

daniel = Persona()
print(str(daniel))