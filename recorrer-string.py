#Recorrer un string con el ciclo - bucle for

def run():
    # nombre = input('Ingrese su nombre: ')
    # for letra in nombre:
    #     print(letra)

    frase = input('Ingrese una frase: ')
    for caracter in frase:
        print(caracter.upper())

if __name__ == "__main__":
    run()