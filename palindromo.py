#PROGRAMA QUE IMPRIME SI UNA PALABRA ES PALINDROMA O NO

def palindromo(palabra):
    palabra = palabra.replace(' ', '') #eliminamos los espacios existentes en la cadena de texto
    palabra = palabra.lower() #pasamos toda la cadena de texto a minuscula
    palabra_invertida = palabra[::-1] #Cambio el sentido de la cadena de texto invertido
    if palabra == palabra_invertida:
        return True
    else: 
        return False    


def run(): #Funcion principal del programa - se puede llamar main() o run()
    palabra = input('Ingrese una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('La palabra que ingresaste es palindromo')
    else:
        print('La palabra que ingresaste no es palindromo')


if __name__ == '__main__': #punto de entrada del programa
    run()

