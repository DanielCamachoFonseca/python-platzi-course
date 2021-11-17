#Clases dentro de python
class Persona:
    def __init__(self, nombre, edad): #Constructor de la ClaseUno(), con sus atributos pasados como parametros
        self.nombre = nombre
        self.edad = edad 

   #Metodos de la clase persona
    def caminar(self):
        print(f'Daniel tiene {self.edad} años. ')


Daniel = Persona('Daniel',24) #Se creo una instancia del objeto persona, y le paso por parametro el contenido de sus atributos
Daniel.caminar() #Llamo un metodo de la clase persona con la instancia creada

    