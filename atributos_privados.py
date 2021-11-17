#Atributos privados en python para
class Persona:
    def __init__(self, apellido ):
        self.__nombre = 'Daniel' #Atributo privado = no debe ser modificado
        self.apellido = apellido

daniel = Persona('Camacho')
print(daniel._Persona__nombre) #Con esta nomenclatura puedo acceder a los atributos