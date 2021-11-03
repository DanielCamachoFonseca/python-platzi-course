def run():
    lista = [1,2,3,4,5,6,7,8,9,10]
    for numeros in lista:
        print(numeros)

    for numeros in enumerate(lista): #funcion enumerate me genera una tupla con el indice y su contenido
        print(numeros)

    for index, numeros in enumerate(lista):
        print(index, numeros)


if __name__ == '__main__':
    run()